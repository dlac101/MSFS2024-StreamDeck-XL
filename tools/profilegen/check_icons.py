"""Check the key-to-icon mapping and the LOCAL icon profile that generate.py --icons builds (docs/icons.md).

Usage, from the repo root (Python 3, standard library only):

    python tools/profilegen/check_icons.py                  # mapping tools/profilegen/icons-c172-g1000.json + its output
    python tools/profilegen/check_icons.py [--mapping <mapping.json>] [--pack <pack root>] [--out <folder>]
                                           [--mapping-only] [<data.json>]

The icon pack (Guenseli) is personal and private use only: this script only reads it, and the icon profile
and image copies it checks live in a git-ignored folder (default <repo>/.local/icons). Never commit them.
check.py stays the check for the committed profile; this script never changes a file.

Checks:
  mapping  the JSON parses (no key twice); the pack's ReadMe.txt has the recorded sha256; every "files"
           entry exists in the pack with its recorded sha256, is a PNG of its recorded size, square, named
           like its pack file with only [A-Za-z0-9_.-] (no "@": PilotsDeck's image list skips those), and is
           used by some row; every "keys"/"left_as_is" row names a real key (a data-file key or a child
           page's back key) with its title, and every key appears exactly once; every "keys" row has
           "pass" 1 or 2 matching the rule against the committed profile (1 = folder key, back key, or a
           Display Value with the empty background now; 2 = a key that shows a built-in plugin image now:
           Images/Switch.png, or the Korry On/Off pair); fields fit the key kind ("image" only on
           folder/back keys, "on" and "off" only together and only on Dynamic Buttons, "default" only on
           PilotsDeck keys whose settings have DefaultImage); Display Value backgrounds are 144x144 or 72x72
  profile  (not with --mapping-only) the icon profile in <out> opens and every JSON entry parses; its entry
           list is the committed profile's plus exactly the embedded folder/back key images, each right after
           its page's manifest; package.json equal; profile manifest equal apart from Name (= the mapping's
           profile_name); every page manifest equal once DefaultImage/OnImage/OffImage and States[*].Image
           are removed; each mapped field has the mapped value, every other image field the committed one;
           every Images/<plugin_subfolder>/ path has its file in <out> with the pack sha256; every embedded
           image is in its page's Images/ with the pack sha256; <out> holds no file the mapping does not name
"""
import hashlib
import io
import json
import re
import struct
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.dont_write_bytecode = True  # importing generate.py must not leave a __pycache__ folder in the repo
import generate  # noqa: E402  (uid, doc_pos_to_key, state_image_name, build)

DEFAULT_MAPPING = HERE / "icons-c172-g1000.json"
PNG_SIG = b"\x89PNG\r\n\x1a\n"
# the PNG header chunk type, written as hex so the repo's image-byte scan (which looks for the chunk name) stays at 0
HEADER_CHUNK = bytes.fromhex("49484452")
NAME_RE = re.compile(r"^[A-Za-z0-9_.-]+$")
KINDS = {  # action UUID -> key kind
    "com.extension.pilotsdeck.action.switch.display": "dynamic",  # Dynamic Button
    "com.extension.pilotsdeck.action.display.switch": "display",  # Display Value
    "com.extension.pilotsdeck.action.switch": "simple",  # Simple Button
    "com.extension.pilotsdeck.action.display.radio": "radio",  # COM Radio
    "com.elgato.streamdeck.profile.openchild": "folder",
    "com.elgato.streamdeck.profile.backtoparent": "back",
}
R1_FIELDS = {"default": "DefaultImage", "on": "OnImage", "off": "OffImage"}
KEY_ROW_FIELDS = {"page", "pos", "title", "pass", "default", "on", "off", "image", "reason"}
LEFT_ROW_FIELDS = {"page", "pos", "title", "reason"}
TOP_FIELDS = {"_about", "pack_root", "pack_readme_sha256", "data", "profile_name", "out", "plugin_subfolder",
              "files", "keys", "left_as_is"}
IMAGE_SETTINGS = ("DefaultImage", "OnImage", "OffImage")


def no_dup_keys(pairs):
    seen = {}
    for k, v in pairs:
        if k in seen:
            raise ValueError(f"key {k!r} appears twice in one JSON object")
        seen[k] = v
    return seen


def png_size(blob):
    """(width, height) from the PNG header, or None if it is not a PNG."""
    if blob[:8] != PNG_SIG or blob[12:16] != HEADER_CHUNK:
        return None
    return struct.unpack(">II", blob[16:24])


def read_zip(path_or_bytes):
    z = zipfile.ZipFile(io.BytesIO(path_or_bytes) if isinstance(path_or_bytes, bytes) else path_or_bytes)
    j = {n: json.loads(z.read(n)) for n in z.namelist() if n.endswith(".json")}
    return z, j


def page_manifests(names):
    """{page dir upper (uuid): entry name of its manifest.json} for the pages inside the profile."""
    out = {}
    for n in names:
        parts = n.split("/")
        if len(parts) == 5 and parts[2] == "Profiles" and parts[4] == "manifest.json":  # Profiles/<p>.sdProfile/Profiles/<page>/
            out[parts[3].upper()] = n
    return out


def actions(manifest):
    return manifest["Controllers"][0]["Actions"] or {}


def key_table(spec, committed_j, names):
    """{(page id, "row,col"): (kind, committed action, title, page dir, manifest pos)} for every key."""
    name = spec["profile_name"]
    pm = page_manifests(names)
    table = {}
    for page in spec["pages"]:
        pdir = generate.uid(name, "page", page["id"]).upper()
        acts = actions(committed_j[pm[pdir]])
        rows = []
        if "parent" in page:
            rows.append((spec["back_key_pos"], None))
        rows += [(k["pos"], k["title"]) for k in page["keys"] if "empty" not in k]
        for pos, title in rows:
            mpos = generate.doc_pos_to_key(pos, spec["grid"])
            a = acts.get(mpos)
            if a is None:
                raise ValueError(f"{page['id']} {pos}: no key in the committed profile (regenerate it first)")
            table[(page["id"], pos)] = (KINDS.get(a["UUID"], "?"), a, title, pdir, mpos)
    return table


def expected_pass(kind, action):
    sm = (action.get("Settings") or {}).get("settingsModel") or {}
    if kind in ("folder", "back"):
        return 1
    if kind == "display" and sm.get("DefaultImage") == "Images/Empty.png":
        return 1
    if kind == "simple" and sm.get("DefaultImage") == "Images/Switch.png":
        return 2
    if kind == "dynamic" and sm.get("OnImage") == "Images/KorryOnBlueTop.png" \
            and sm.get("OffImage") == "Images/KorryOffWhiteBottom.png":
        return 2
    return None


def load_plan(mapping_path, pack=None, data=None):
    """Check the mapping; return (errors, plan). The plan is what generate.build(icons=...) and the
    profile check use. generate.py --icons calls this before it writes anything."""
    errors = []
    err = errors.append
    try:
        m = json.loads(Path(mapping_path).read_text(encoding="utf-8"), object_pairs_hook=no_dup_keys)
    except (OSError, ValueError) as ex:
        return [f"mapping {mapping_path}: can't read: {ex}"], None
    missing = sorted(TOP_FIELDS - {"_about"} - set(m))
    unknown = sorted(set(m) - TOP_FIELDS)
    if missing or unknown:
        return [f"mapping: missing field(s) {missing}, unknown field(s) {unknown}"], None
    sub = m["plugin_subfolder"]
    if not (isinstance(sub, str) and NAME_RE.match(sub)) or sub.strip(".") == "":
        err(f"plugin_subfolder {sub!r}: use only [A-Za-z0-9_.-] (one folder level, no '@', not only dots)")
    if not (isinstance(m["profile_name"], str) and m["profile_name"].strip()):
        err("profile_name must be a non-empty string")

    # the pack: read only
    pack_root = Path(pack if pack else m["pack_root"]).resolve()
    readme = pack_root / "ReadMe.txt"
    try:
        rs = hashlib.sha256(readme.read_bytes()).hexdigest()
        if rs != m["pack_readme_sha256"]:
            err(f"pack ReadMe.txt sha256 {rs} differs from the recorded {m['pack_readme_sha256']} (another pack version?)")
    except OSError as ex:
        err(f"pack ReadMe.txt not readable at {readme}: {ex}")
    files = {}  # local name -> (bytes, (w, h))
    for local, e in m["files"].items():
        label = f"files {local}"
        if set(e) != {"pack", "sha256", "size"}:
            err(f"{label}: fields must be pack, sha256, size (got {sorted(e)})")
            continue
        if not NAME_RE.match(local) or not local.lower().endswith(".png"):
            err(f"{label}: name must be [A-Za-z0-9_.-] only and end in .png (no '@', no spaces)")
        if e["pack"].replace("\\", "/").rsplit("/", 1)[-1] != local:
            err(f"{label}: local name must be the pack file's base name ({e['pack']})")
        src = (pack_root / e["pack"]).resolve()
        if pack_root not in src.parents:
            err(f"{label}: pack path {e['pack']!r} leaves the pack folder")
            continue
        try:
            blob = src.read_bytes()
        except OSError:
            err(f"{label}: pack file does not exist: {e['pack']}")
            continue
        h = hashlib.sha256(blob).hexdigest()
        if h != e["sha256"]:
            err(f"{label}: sha256 {h} differs from the recorded {e['sha256']}")
            continue
        size = png_size(blob)
        if size is None:
            err(f"{label}: not a PNG (signature or header chunk)")
            continue
        if f"{size[0]}x{size[1]}" != e["size"]:
            err(f"{label}: PNG is {size[0]}x{size[1]}, recorded {e['size']}")
        if size[0] != size[1]:
            err(f"{label}: PNG is not square ({size[0]}x{size[1]})")
        files[local] = (blob, size)

    # the keys
    data_path = Path(data) if data else ROOT / m["data"]
    try:
        spec = json.loads(data_path.read_text(encoding="utf-8"))
        committed_path = ROOT / spec["output"]
        cz, cj = read_zip(committed_path)
        table = key_table(spec, cj, cz.namelist())
    except (OSError, ValueError, KeyError, zipfile.BadZipFile) as ex:
        errors.append(f"data file / committed profile not usable: {type(ex).__name__}: {ex}")
        return errors, None
    seen = {}
    plan_keys = {}
    used = {}  # local name -> set of routes ("R1", "R2")
    for where, rows, allowed in (("keys", m["keys"], KEY_ROW_FIELDS), ("left_as_is", m["left_as_is"], LEFT_ROW_FIELDS)):
        for i, row in enumerate(rows):
            label = f"{where}[{i}] {row.get('page')} {row.get('pos')} {row.get('title')!r}"
            extra = sorted(set(row) - allowed)
            if extra:
                err(f"{label}: unknown field(s) {extra}")
            k = (row.get("page"), row.get("pos"))
            if k not in table:
                err(f"{label}: unknown key (no such page/position in the data file, and not a child page's back key)")
                continue
            kind, action, title, _, _ = table[k]
            if row.get("title") != title:
                err(f"{label}: title differs from the data file's {title!r}")
            if k in seen:
                err(f"{label}: key listed twice (also {seen[k]})")
                continue
            seen[k] = label
            if not (isinstance(row.get("reason"), str) and row["reason"].strip()):
                err(f"{label}: needs a reason")
            if where == "left_as_is":
                continue
            exp = expected_pass(kind, action)
            if "pass" not in row:
                err(f"{label}: no 'pass' field (1 or 2)")
            elif row["pass"] not in (1, 2):
                err(f"{label}: pass must be 1 or 2, got {row['pass']!r}")
            elif exp is None:
                err(f"{label}: a {kind} key with this image setup has no pass under the rule; list it in left_as_is")
            elif row["pass"] != exp:
                err(f"{label}: pass {row['pass']} but the rule says pass {exp} for this {kind} key "
                    f"(1 = no image now, 2 = a built-in plugin image now)")
            fields = [f for f in ("default", "on", "off", "image") if f in row]
            if not fields:
                err(f"{label}: sets no image field (default, on/off or image)")
            sm = (action.get("Settings") or {}).get("settingsModel") or {}
            if "image" in row and kind not in ("folder", "back"):
                err(f"{label}: 'image' is only for folder and back keys (this is a {kind} key)")
            if ("on" in row) != ("off" in row):
                err(f"{label}: 'on' and 'off' go together (one is missing)")
            if ("on" in row or "off" in row) and kind != "dynamic":
                err(f"{label}: 'on'/'off' are only for Dynamic Buttons (this is a {kind} key)")
            if "default" in row and (kind in ("folder", "back") or "DefaultImage" not in sm):
                err(f"{label}: 'default' only on PilotsDeck keys whose settings have DefaultImage (this is a {kind} key)")
            for f in fields:
                v = row[f]
                if v not in m["files"]:
                    err(f"{label}: {f} {v!r} is not in 'files'")
                    continue
                used.setdefault(v, set()).add("R2" if f == "image" else "R1")
                if f == "default" and kind == "display" and v in files and files[v][1] not in ((144, 144), (72, 72)):
                    w, h = files[v][1]
                    err(f"{label}: Display Value background {v} is {w}x{h}; it is drawn at its own pixel size, so use 144x144 (or 72x72)")
            settings = {R1_FIELDS[f]: f"Images/{sub}/{row[f]}" for f in R1_FIELDS if f in row}
            image = None
            if "image" in row and row["image"] in files:
                image = (generate.state_image_name(k[0], k[1]), files[row["image"]][0])
            plan_keys[k] = {"settings": settings, "image": image, "row": row}
    missing_keys = [f"{p} {pos} {t[2]!r}" for (p, pos), t in table.items() if (p, pos) not in seen]
    if missing_keys:
        err(f"key(s) in neither 'keys' nor 'left_as_is': {missing_keys}")
    unused = sorted(set(m["files"]) - set(used))
    if unused:
        err(f"'files' entries no row uses: {unused}")
    copies = {n: files[n][0] for n, r in used.items() if "R1" in r and n in files}
    plan = {"profile_name": m["profile_name"], "out": m["out"], "plugin_subfolder": sub, "data": data_path,
            "keys": plan_keys, "copies": copies, "files": {n: e["sha256"] for n, e in m["files"].items()},
            "table": table, "spec": spec, "committed_path": committed_path, "routes": used}
    return errors, plan


def check_profile(plan, out_dir):
    """Check the icon profile and image copies in out_dir against the committed profile. Returns (errors, notes)."""
    errors, notes = [], []
    err = errors.append
    sub = plan["plugin_subfolder"]
    profile_path = out_dir / (plan["profile_name"] + ".streamDeckProfile")
    img_dir = out_dir / "Images" / sub
    try:
        z, j = read_zip(profile_path)
        if z.testzip() is not None:
            err(f"{profile_path}: zip CRC error")
    except (OSError, ValueError, zipfile.BadZipFile) as ex:
        return [f"icon profile not readable at {profile_path}: {ex} (build it: python tools/profilegen/generate.py --icons ...)"], notes
    notes.append(f"{profile_path.name}: opens, {len(z.namelist())} entries, {len(j)} JSON entries parse, "
                 f"sha256 {hashlib.sha256(profile_path.read_bytes()).hexdigest()}")
    cz, cj = read_zip(plan["committed_path"])
    # the committed profile is the default build (so the comparison below is against current generator output)
    fresh, _ = read_zip(generate.build(plan["data"])[1])
    if fresh.namelist() != cz.namelist() or any(fresh.read(n) != cz.read(n) for n in cz.namelist()):
        err("the committed profile differs from a fresh default build (run python tools/profilegen/generate.py)")
    table, keys = plan["table"], plan["keys"]

    # entry list: committed + the embedded images after each page's manifest, in position order
    per_page = {}
    for k, p in sorted(keys.items(), key=lambda kv: tuple(int(x) for x in kv[0][1].split(","))):
        if p["image"]:
            per_page.setdefault(table[k][3], []).append(p["image"])
    expected = []
    pm = page_manifests(cz.namelist())
    for n in cz.namelist():
        expected.append(n)
        for pdir, mname in pm.items():
            if n == mname:
                expected += [n.rsplit("/", 1)[0] + "/Images/" + name for name, _ in per_page.get(pdir, [])]
    if z.namelist() != expected:
        err(f"entry list differs from the committed profile + embedded images: extra "
            f"{sorted(set(z.namelist()) - set(expected))}, missing {sorted(set(expected) - set(z.namelist()))}"
            + (", or the order differs" if set(z.namelist()) == set(expected) else ""))
    n_img = sum(len(v) for v in per_page.values())
    for info in z.infolist():
        if info.filename not in cz.namelist() and info.filename.endswith(".png"):
            if (info.date_time != generate.ZIP_DATE or info.compress_type != zipfile.ZIP_DEFLATED
                    or info.external_attr != 0x20 or info.create_system != 0):
                err(f"{info.filename}: zip entry attributes differ from the generator's other file entries")
    if j.get("package.json") != cj["package.json"]:
        err("package.json differs from the committed profile's")
    prof = [n for n in cz.namelist() if n.count("/") == 2 and n.endswith(".sdProfile/manifest.json")][0]
    a, b = dict(j.get(prof, {})), dict(cj[prof])
    if a.get("Name") != plan["profile_name"]:
        err(f"profile Name {a.get('Name')!r}, expected {plan['profile_name']!r}")
    a.pop("Name", None), b.pop("Name", None)
    if a != b:
        err("profile manifest differs from the committed one apart from Name")

    def strip(manifest):
        m2 = json.loads(json.dumps(manifest))
        for act in actions(m2).values():
            sm = (act.get("Settings") or {}).get("settingsModel")
            if isinstance(sm, dict):
                for f in IMAGE_SETTINGS:
                    sm.pop(f, None)
            for s in act.get("States", []):
                s.pop("Image", None)
        return m2

    by_page_pos = {(t[3], t[4]): k for k, t in table.items()}
    checked = 0
    for pdir, mname in pm.items():
        if mname not in j:
            continue
        mi, mc = j[mname], cj[mname]
        if strip(mi) != strip(mc):
            err(f"page {pdir[:8]}: manifest differs from the committed one beyond the image fields")
        for pos, ac in actions(mc).items():
            ai = actions(mi).get(pos)
            if ai is None:
                continue
            k = by_page_pos.get((pdir, pos))
            p = keys.get(k) if k else None
            label = f"{k[0]} {k[1]} {table[k][2]!r}" if k else f"{pdir[:8]} {pos}"
            smc = (ac.get("Settings") or {}).get("settingsModel") or {}
            smi = (ai.get("Settings") or {}).get("settingsModel") or {}
            for f in IMAGE_SETTINGS:
                want = p["settings"][f] if p and f in p["settings"] else smc.get(f, "<absent>")
                if smi.get(f, "<absent>") != want:
                    err(f"{label}: {f} = {smi.get(f, '<absent>')!r}, expected {want!r}")
            for si, (sti, stc) in enumerate(zip(ai.get("States", []), ac.get("States", []))):
                want = ("Images/" + p["image"][0]) if p and p["image"] and si == 0 else stc.get("Image", "<absent>")
                if sti.get("Image", "<absent>") != want:
                    err(f"{label}: States[{si}].Image = {sti.get('Image', '<absent>')!r}, expected {want!r}")
            checked += 1
    notes.append(f"{checked} keys compared field by field; {n_img} embedded folder/back key images")

    # every R1 path resolves to a copied file with the pack sha256; every R2 image in its page's Images/
    for k, p in keys.items():
        for f, v in p["settings"].items():
            name = v.split("/", 2)[2]
            fp = img_dir / name
            try:
                h = hashlib.sha256(fp.read_bytes()).hexdigest()
                if h != plan["files"][name]:
                    err(f"{k[0]} {k[1]}: {fp} sha256 {h} differs from the pack file's")
            except OSError:
                err(f"{k[0]} {k[1]}: {f} {v} has no file at {fp}")
        if p["image"]:
            entry = page_manifests(z.namelist()).get(table[k][3], "").rsplit("/", 1)[0] + "/Images/" + p["image"][0]
            try:
                h = hashlib.sha256(z.read(entry)).hexdigest()
                if h != plan["files"][p["row"]["image"]]:
                    err(f"{k[0]} {k[1]}: embedded {entry} sha256 differs from the pack file's")
            except KeyError:
                err(f"{k[0]} {k[1]}: embedded image {entry} missing from the zip")
    allowed = {profile_path.resolve()} | {(img_dir / n).resolve() for n in plan["copies"]}
    present = {p.resolve() for p in out_dir.rglob("*") if p.is_file()}
    if present - allowed:
        err(f"{out_dir} holds file(s) the mapping does not name: {sorted(str(p) for p in present - allowed)}")
    if allowed - present:
        err(f"{out_dir} lacks: {sorted(str(p) for p in allowed - present)}")
    notes.append(f"{len(plan['copies'])} image copies in {img_dir}, each with the pack sha256")
    return errors, notes


def main():
    args = sys.argv[1:]
    opts = {}
    for flag in ("--mapping", "--pack", "--out"):
        if flag in args:
            i = args.index(flag)
            if i + 1 >= len(args):
                print(f"error: {flag} needs a value", file=sys.stderr)
                return 2
            opts[flag] = args[i + 1]
            del args[i:i + 2]
    mapping_only = "--mapping-only" in args
    args = [a for a in args if a != "--mapping-only"]
    data = args[0] if args else None
    mapping = Path(opts.get("--mapping", DEFAULT_MAPPING))

    print(f"== mapping: {mapping}")
    errors, plan = load_plan(mapping, pack=opts.get("--pack"), data=data)
    for e in errors:
        print(f"  FAIL  {e}")
    if plan and not errors:
        rows = [p["row"] for p in plan["keys"].values()]
        p1 = sum(1 for r in rows if r.get("pass") == 1)
        r2 = sorted(n for n, r in plan["routes"].items() if "R2" in r)
        print(f"  ok    {len(plan['files'])} pack files present with their sha256, PNG, square")
        print(f"  ok    {len(rows)} key rows (pass 1: {p1}, pass 2: {len(rows) - p1}) + "
              f"{len(plan['table']) - len(rows)} left as is = {len(plan['table'])} keys, each once")
        print(f"  ok    {len(plan['copies'])} files for PilotsDeck keys (copied), {len(r2)} embedded only")
    if not mapping_only and plan is not None and not errors:
        out = Path(opts["--out"]).resolve() if "--out" in opts else (ROOT / plan["out"]).resolve()
        print(f"== profile: {out}")
        perr, notes = check_profile(plan, out)
        for n in notes:
            print(f"  {'ok' if not perr else 'info':<5} {n}")
        for e in perr:
            print(f"  FAIL  {e}")
        errors += perr
    print()
    print("RESULT:", "PASS" if not errors else f"FAIL ({len(errors)})")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
