"""Generate a Stream Deck XL profile (.streamDeckProfile) for PilotsDeck from a page data file.

Usage, from the repo root (Python 3, standard library only):

    python tools/profilegen/generate.py                      # uses tools/profilegen/c172-g1000.json
    python tools/profilegen/generate.py <data.json>

    # LOCAL icon build (docs/icons.md): personal use only, written to a git-ignored folder, never committed
    python tools/profilegen/generate.py --icons tools/profilegen/icons-c172-g1000.json [--pack <pack root>] [--out <folder>] [<data.json>]

What it does:
- Every key copies a real saved action and changes only the fields its entry in the data file names:
  "p1:<col,row>" = that key of the Phase 1 export (read from the repo at run time), any other template
  name = an entry of templates.json (real saved actions copied verbatim, with their source).
- Unknown settings fields are refused, so no field name is ever made up here. A key's "shell" entry
  changes action fields outside the settings (for example "LinkedTitle"); only fields the template
  already has, with the same type.
- Pages: the first page in the data file is the profile's page; every other page is a Stream Deck
  folder (child page) opened by a folder key on its parent and holding a back key at "back_key_pos".
- Title size (States FontSize, drawn by the Stream Deck app): a Simple Button or Dynamic Button whose template
  state says 10 gets 14; other sizes (15, and 12 on folder and back keys) stay, and readout keys (COM Radio,
  Display Value) keep their template size, since they draw their values with the title font (FontInherit).
  A key's optional "title_size" (10 to 15) is for a title that does not fit at 14; it is refused on folder
  and empty entries and where it equals the size the rule gives. Any other key entry field than those in
  KEY_FIELDS is refused.
- Title alignment (States TitleAlignment): every key keeps its template's alignment. A key's optional
  "title_align" ("top", "middle" or "bottom") sets it on every state of a folder key or an ordinary key (main
  VIEWS, CHECKLIST, MORE: "middle", P2-7 A-8, LR232-C5); it is refused on empty entries, when it is not one of
  those three strings, and where it equals the template's alignment.
- The output is byte-identical for the same inputs: fixed entry order and timestamps, UUIDs derived
  from the profile name and page/key ids (uuid5), JSON written the way the Stream Deck app writes it
  (sorted keys, no spaces, UTF-8).

Check the result with tools/profilegen/check.py.

--icons <mapping.json> (the local icon build; the default run above is unchanged byte for byte):
- Checks the mapping first with check_icons.py's own function (every pack file present with its recorded
  sha256, every key row resolving), and writes nothing if it fails (exit 2).
- Builds the same profile with the mapped image fields set: DefaultImage / OnImage / OffImage of PilotsDeck
  keys = "Images/<plugin_subfolder>/<file>" (files the user copies into the plugin's Images folder), and a
  state "Image" on mapped folder and back keys, its PNG embedded in that page's Images/ folder in the zip.
  Profile Name = the mapping's profile_name; page and action UUIDs stay those of the data file.
- Writes "<out>/<profile_name>.streamDeckProfile" and byte copies of the PilotsDeck-key images to
  "<out>/Images/<plugin_subfolder>/". --out (default <repo>/<mapping "out">) must be inside the repo and
  git-ignored: every file is checked with "git check-ignore" before anything is written (exit 2 if not).
- --pack (default the mapping's pack_root): the icon pack folder, read only.
Check the result with tools/profilegen/check_icons.py.
"""
import argparse
import base64
import copy
import hashlib
import io
import json
import subprocess
import sys
import uuid
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
NAMESPACE = uuid.uuid5(uuid.NAMESPACE_URL, "msfs2024-streamdeck-xl/tools/profilegen")
ZIP_DATE = (2026, 11, 11, 0, 0, 0)  # fixed timestamp for every zip entry
OPENCHILD = "com.elgato.streamdeck.profile.openchild"
# Title size (States FontSize; P2-7, LR210-C4): a template state at 10 becomes 14 on the kinds in
# TITLE_SIZE_KINDS, any other size or kind keeps its size; a key's "title_size" overrides it with one of TITLE_SIZES
TITLE_SIZE_FROM = 10
TITLE_SIZE_TO = 14
TITLE_SIZES = (10, 11, 12, 13, 14, 15)
# Only Simple Buttons and Dynamic Buttons get the 10 -> 14 rule (LR231-C5 R-2 (a)): they draw no text of their
# own (PilotsDeck 11bdf1f7 Plugin/Actions/Simple/ActionSwitch.cs and ActionSwitchDisplay.cs: no DrawText or
# GetFont), so only the Stream Deck app's title uses the size. COM Radio (ActionDisplayRadio.cs) and Display
# Value (ActionDisplayText.cs) draw their values with GetFont(), which returns the title font when FontInherit
# is set (ActionBaseSimple.cs), so they keep their template size.
TITLE_SIZE_KINDS = ("com.extension.pilotsdeck.action.switch", "com.extension.pilotsdeck.action.switch.display")
# Title alignment (States TitleAlignment; P2-7 A-8, LR232-C5): the values of the Elgato Stream Deck SDK manifest
# reference, State "TitleAlignment": "bottom" | "middle" | "top" (https://docs.elgato.com/streamdeck/sdk/references/manifest),
# and the field and value of the user's own saved edit (ProfilesV3 B83EB496-78B3-46DF-896E-8B9F656B713E.sdProfile,
# main 1,8 / 3,8 / 4,8 folder keys: States[0].TitleAlignment "bottom" -> "middle")
TITLE_ALIGNS = ("top", "middle", "bottom")
KEY_FIELDS = {"pos", "title", "template", "set", "shell", "states_from", "folder", "empty", "title_size", "title_align"}


def dumps(obj):
    """JSON the way the Stream Deck app writes it (checked byte for byte against the Phase 1 export)."""
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def uid(*parts):
    return str(uuid.uuid5(NAMESPACE, "/".join(parts)))


def doc_pos_to_key(pos, grid):
    """Docs use row,column (1-based); the manifest keys actions by "column,row" (0-based)."""
    row, col = (int(x) for x in pos.split(","))
    if not (1 <= row <= grid["rows"] and 1 <= col <= grid["columns"]):
        raise ValueError(f"position {pos} is outside the {grid['rows']}x{grid['columns']} grid")
    return f"{col - 1},{row - 1}"


class Phase1:
    """The Phase 1 export: the format template (profile manifest, package.json, page and key layout)."""

    def __init__(self, path):
        z = zipfile.ZipFile(path)
        self.names = z.namelist()
        self.package = json.loads(z.read("package.json"))
        prof = [n for n in self.names if n.count("/") == 2 and n.endswith(".sdProfile/manifest.json")]
        if len(prof) != 1:
            raise ValueError("Phase 1 export: expected one profile manifest")
        self.profile = json.loads(z.read(prof[0]))
        page = self.profile["Pages"]["Pages"][0].upper()
        default = self.profile["Pages"]["Default"].upper()
        base = prof[0].rsplit("/", 1)[0] + "/Profiles/"
        self.page = json.loads(z.read(base + page + "/manifest.json"))
        self.default_page = json.loads(z.read(base + default + "/manifest.json"))
        self.actions = self.page["Controllers"][0]["Actions"]


def load_templates(phase1):
    data = json.loads((HERE / "templates.json").read_text(encoding="utf-8"))

    def resolve(name):
        if name.startswith("p1:"):
            return copy.deepcopy(phase1.actions[name[3:]])
        entry = data[name]
        if "action" in entry:
            return copy.deepcopy(entry["action"])
        # derived template: a real saved action of the same settings class, with named changes
        action = resolve(entry["derived_from"])
        action.update(entry["shell"])
        apply_settings(action, entry["set"], name)
        if "states_from" in entry:
            action["States"] = copy.deepcopy(resolve(entry["states_from"])["States"])
        for state in action["States"]:
            for k, v in entry.get("states_set", {}).items():
                if k not in state:
                    raise KeyError(f"{name}: state field {k} not in template")
                state[k] = v
        return action

    return resolve


def apply_settings(action, changes, label):
    model = action["Settings"]["settingsModel"]
    for k, v in changes.items():
        if k not in model:
            raise KeyError(f"{label}: settings field {k!r} does not exist in the template")
        if type(model[k]) is not type(v):
            raise TypeError(f"{label}: {k} is {type(model[k]).__name__} in the template, got {type(v).__name__}")
        model[k] = v


def apply_shell(action, changes, label):
    for k, v in changes.items():
        if k in ("ActionID", "Settings", "States") or k not in action:
            raise KeyError(f"{label}: action field {k!r} can't be set by 'shell' (not in the template, or set elsewhere)")
        if type(action[k]) is not type(v):
            raise TypeError(f"{label}: {k} is {type(action[k]).__name__} in the template, got {type(v).__name__}")
        action[k] = v


def set_title(action, title, label):
    for state in action["States"]:
        if "Title" not in state:
            raise KeyError(f"{label}: template state has no Title field")
        state["Title"] = title


def set_title_size(action, key, label):
    """Every state's FontSize: the key's "title_size" if it has one, else 14 where the template says 10 on a
    Simple or Dynamic Button (TITLE_SIZE_KINDS), else the template's own size. All states must hold one int
    FontSize; a redundant override is refused."""
    sizes = {state.get("FontSize") for state in action["States"]}
    if len(sizes) != 1 or type(next(iter(sizes))) is not int:
        raise ValueError(f"{label}: template states need one int FontSize, found {sorted(map(repr, sizes))}")
    base = sizes.pop()
    auto = TITLE_SIZE_TO if base == TITLE_SIZE_FROM and action["UUID"] in TITLE_SIZE_KINDS else base
    size = auto
    if "title_size" in key:
        size = key["title_size"]
        if type(size) is not int:
            raise ValueError(f"{label}: title_size must be an int, got {size!r}")
        if size not in TITLE_SIZES:
            raise ValueError(f"{label}: title_size {size} is not one of {TITLE_SIZES}")
        if size == auto:
            raise ValueError(f"{label}: title_size {size} is redundant (the rule already gives {auto}); remove it")
    for state in action["States"]:
        state["FontSize"] = size


def set_title_align(action, key, label):
    """Every state's TitleAlignment = the key's "title_align", if it has one (else the template's stays). The
    value must be one of TITLE_ALIGNS, the template states must hold one string TitleAlignment, and a value
    equal to it (redundant) is refused."""
    if "title_align" not in key:
        return
    align = key["title_align"]
    if type(align) is not str or align not in TITLE_ALIGNS:
        raise ValueError(f"{label}: title_align must be one of {list(TITLE_ALIGNS)}, got {align!r}")
    bases = {state.get("TitleAlignment") for state in action["States"]}
    if len(bases) != 1 or type(next(iter(bases))) is not str:
        raise ValueError(f"{label}: template states need one TitleAlignment, found {sorted(map(repr, bases))}")
    base = bases.pop()
    if align == base:
        raise ValueError(f"{label}: title_align {align!r} is redundant (the template already gives {base!r}); remove it")
    for state in action["States"]:
        state["TitleAlignment"] = align


def state_image_name(page_id, pos):
    """Name of an embedded folder/back key image: 27 upper-case letters and digits ending in Z, the shape the
    Stream Deck app saves (base32 here): base32 of sha256("<data page id>/<row,column>"), so it is the same on
    every run."""
    digest = hashlib.sha256(f"{page_id}/{pos}".encode("utf-8")).digest()
    return base64.b32encode(digest).decode("ascii")[:26] + "Z.png"


def build(data_path, icons=None):
    """icons=None: the normal build. Otherwise a dict from icon_plan(): "profile_name" and "keys" =
    {(page id, "row,column"): {"settings": {field: value}, "image": (zip file name, PNG bytes) or None}}."""
    spec = json.loads(Path(data_path).read_text(encoding="utf-8"))
    grid = spec["grid"]
    name = spec["profile_name"]
    phase1 = Phase1(ROOT / spec["phase1_export"])
    resolve = load_templates(phase1)
    templates = json.loads((HERE / "templates.json").read_text(encoding="utf-8"))

    pages = spec["pages"]
    ids = [p["id"] for p in pages]
    if len(set(ids)) != len(ids):
        raise ValueError("page ids must be unique")
    for page in pages:
        if page.get("parent") == page["id"]:
            raise ValueError(f"page {page['id']}: a page can't be its own parent")
    targets = [k["folder"] for p in pages for k in p["keys"] if "folder" in k]
    twice = sorted({t for t in targets if targets.count(t) > 1})
    if twice:
        raise ValueError(f"child page(s) {twice}: opened by more than one folder key")
    page_uuid = {p["id"]: uid(name, "page", p["id"]) for p in pages}
    default_uuid = uid(name, "page", "_default")
    profile_uuid = uid(name, "profile")
    back_key = doc_pos_to_key(spec["back_key_pos"], grid)

    manifests = {}
    page_images = {}  # page uuid -> [(zip file name, PNG bytes)] (icon build only)
    folder_used = False
    for page in pages:
        actions = {}
        images = []
        if "parent" in page:
            back = copy.deepcopy(templates["back"]["action"])
            back["ActionID"] = uid(name, page["id"], "back")
            icon = icons["keys"].get((page["id"], spec["back_key_pos"])) if icons else None
            if icon and icon["image"]:
                # the only field the icon build adds (ASSUMPTION A-3, docs/icons.md): as on folder keys
                back["States"][0]["Image"] = "Images/" + icon["image"][0]
                images.append((spec["back_key_pos"], icon["image"]))
            actions[back_key] = back
        for key in page["keys"]:
            label = f"{page['id']} {key['pos']}"
            pos = doc_pos_to_key(key["pos"], grid)
            if pos in actions:
                raise ValueError(f"{label}: position used twice")
            named = f"{label} {key['title']}" if "title" in key else label
            unknown = sorted(set(key) - KEY_FIELDS)
            if unknown:
                raise ValueError(f"{named}: unknown key field(s) {unknown} (allowed: {sorted(KEY_FIELDS)})")
            if "title_size" in key and ("empty" in key or "folder" in key):
                raise ValueError(f"{named}: title_size is not allowed on {'a folder' if 'folder' in key else 'an empty'} entry")
            if "title_align" in key and "empty" in key:
                raise ValueError(f"{named}: title_align is not allowed on an empty entry")
            if "empty" in key:
                continue
            icon = icons["keys"].get((page["id"], key["pos"])) if icons else None
            if "folder" in key:
                child = key["folder"]
                if child not in page_uuid or next(p for p in pages if p["id"] == child).get("parent") != page["id"]:
                    raise ValueError(f"{label}: folder target {child!r} is not a child page of {page['id']!r}")
                action = copy.deepcopy(templates["folder"]["action"])
                action["Settings"] = {"ProfileUUID": page_uuid[child]}
                for state in action["States"]:
                    if icon and icon["image"]:
                        state["Image"] = "Images/" + icon["image"][0]  # icon build: the template's own field
                    else:
                        state.pop("Image", None)  # no own image: the Stream Deck app's folder default (C-4)
                if icon and icon["image"]:
                    images.append((key["pos"], icon["image"]))
                folder_used = True
            else:
                action = resolve(key["template"])
                if key.get("states_from"):
                    action["States"] = copy.deepcopy(resolve(key["states_from"])["States"])
                apply_settings(action, key.get("set", {}), label)
                apply_shell(action, key.get("shell", {}), label)
                if icon and icon["settings"]:
                    apply_settings(action, icon["settings"], label + " (icons)")  # existing fields only
                set_title_size(action, key, named)
            set_title_align(action, key, named)
            set_title(action, key["title"], label)
            action["ActionID"] = uid(name, page["id"], key["pos"])
            actions[pos] = action
        manifest = copy.deepcopy(phase1.page)
        manifest["Controllers"][0]["Actions"] = actions or None
        manifests[page_uuid[page["id"]]] = manifest
        if images:
            images.sort(key=lambda item: tuple(int(x) for x in item[0].split(",")))  # position order (row, column)
            page_images[page_uuid[page["id"]]] = [img for _, img in images]
    manifests[default_uuid] = copy.deepcopy(phase1.default_page)

    # every child page needs a parent and a folder key that opens it
    for page in pages[1:]:
        if page.get("parent") not in ids:
            raise ValueError(f"page {page['id']}: parent missing")
        if not any(k.get("folder") == page["id"] for p in pages for k in p["keys"]):
            raise ValueError(f"page {page['id']}: no folder key opens it")

    profile = copy.deepcopy(phase1.profile)
    profile["Name"] = icons["profile_name"] if icons else name
    profile["Pages"] = {
        "Current": "00000000-0000-0000-0000-000000000000",
        "Default": default_uuid,
        "Pages": [page_uuid[pages[0]["id"]]],
    }
    package = copy.deepcopy(phase1.package)
    if folder_used and OPENCHILD not in package["RequiredPlugins"]:
        package["RequiredPlugins"].append(OPENCHILD)

    # entry order as in the Phase 1 export
    top = f"Profiles/{profile_uuid.upper()}.sdProfile/"
    entries = [("package.json", dumps(package)), ("Profiles/", None), (top, None),
               (top + "manifest.json", dumps(profile)), (top + "Profiles/", None)]
    for pid in sorted(manifests, key=str.upper):
        d = f"{top}Profiles/{pid.upper()}/"
        entries += [(d, None), (d + "Images/", None), (d + "manifest.json", dumps(manifests[pid]))]
        # icon build: embedded folder/back key images right after the page's manifest (as the app exports them)
        entries += [(d + "Images/" + img_name, img_bytes) for img_name, img_bytes in page_images.get(pid, [])]

    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        for entry, content in entries:
            info = zipfile.ZipInfo(entry, ZIP_DATE)
            info.create_system = 0
            if content is None:
                info.external_attr = 0x10
                info.compress_type = zipfile.ZIP_STORED
                z.writestr(info, b"")
            else:
                info.external_attr = 0x20
                info.compress_type = zipfile.ZIP_DEFLATED
                z.writestr(info, content)
    return ROOT / spec["output"], buf.getvalue()


def is_ignored(path):
    """True if git says the file is ignored in this repo (the icon build writes only there)."""
    try:
        r = subprocess.run(["git", "-C", str(ROOT), "check-ignore", "-q", str(path)], capture_output=True)
    except OSError:
        return False
    if r.returncode not in (0, 1):  # 1 = not ignored; anything else is a git error: report it, still refuse
        err = r.stderr.decode("utf-8", "replace").strip()
        if err:
            print(err)
        print(f"git check-ignore failed (exit {r.returncode}) for {path}")
        return False
    return r.returncode == 0


def main_icons(args):
    sys.dont_write_bytecode = True  # importing check_icons.py must not leave a __pycache__ folder in the repo
    import check_icons  # the mapping check (one implementation, shared with check_icons.py)

    mapping_path = Path(args.icons)
    errors, plan = check_icons.load_plan(mapping_path, pack=args.pack, data=args.data)
    if errors:
        for e in errors:
            print(f"FAIL: {e}")
        print("icon build: mapping check failed, nothing written")
        return 2
    out = Path(args.out).resolve() if args.out else (ROOT / plan["out"]).resolve()
    if out != ROOT and ROOT not in out.parents:
        print(f"refused: --out {out} is not inside the repo {ROOT}; nothing written")
        return 2
    profile_path = out / (plan["profile_name"] + ".streamDeckProfile")
    img_dir = out / "Images" / plan["plugin_subfolder"]
    targets = [profile_path] + [img_dir / n for n in sorted(plan["copies"])]
    not_ignored = [t for t in targets if not is_ignored(t)]
    if not_ignored:
        for t in not_ignored:
            print(f"refused: {t} is not git-ignored (git check-ignore); the icon build writes only to an ignored folder")
        print("nothing written (personal-use icons must never be committed: docs/icons.md)")
        return 2
    if img_dir.is_dir():
        extra = sorted(p.name for p in img_dir.iterdir() if p.name not in plan["copies"])
        if extra:
            print(f"stopped: {img_dir} holds file(s) the mapping does not name: {extra}; nothing written, nothing deleted. "
                  f"Delete {out} and rebuild (see docs/icons.md)")
            return 2
    _, blob = build(plan["data"], icons=plan)
    img_dir.mkdir(parents=True, exist_ok=True)
    profile_path.write_bytes(blob)
    for local_name in sorted(plan["copies"]):
        (img_dir / local_name).write_bytes(plan["copies"][local_name])  # the pack bytes, sha256-checked, unchanged
    print(f"wrote {profile_path} ({len(blob)} bytes)")
    print(f"wrote {len(plan['copies'])} images to {img_dir}")
    print("Next (docs/icons.md): copy that folder into the PilotsDeck plugin's Images folder and restart the "
          "Stream Deck app BEFORE you import the profile. Personal use only: never commit or upload these files.")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Generate a PilotsDeck Stream Deck XL profile from a page data file.")
    ap.add_argument("data", nargs="?", help="page data file (default tools/profilegen/c172-g1000.json)")
    ap.add_argument("--icons", help="LOCAL icon build from this key-to-icon mapping (docs/icons.md)")
    ap.add_argument("--pack", help="with --icons: the icon pack folder (default: the mapping's pack_root)")
    ap.add_argument("--out", help="with --icons: output folder inside the repo, git-ignored (default: the mapping's out)")
    args = ap.parse_args()
    if args.icons:
        sys.exit(main_icons(args))
    if args.pack or args.out:
        ap.error("--pack and --out need --icons")
    data = Path(args.data) if args.data else HERE / "c172-g1000.json"
    out, blob = build(data)
    out.write_bytes(blob)
    print(f"wrote {out.relative_to(ROOT).as_posix()} ({len(blob)} bytes)")


if __name__ == "__main__":
    main()
