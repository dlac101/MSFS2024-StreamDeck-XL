"""Check a generated profile against the spec doc, the Phase 1 export and real saved examples.

Usage, from the repo root (Python 3, standard library only):

    python tools/profilegen/check.py                 # uses tools/profilegen/c172-g1000.json
    python tools/profilegen/check.py <data.json> [--sources] [--fenix <MSFS-Fenix320-XL.streamDeckProfile>]

Plain check.py reads only files in the repo. --sources (and --fenix) also read files outside it.

Checks:
  zip      the profile opens and every JSON entry parses
  current  the profile on disk is what generate.py builds now from the data file: same entry names, same
           order, same uncompressed content (the compressed bytes may differ with another zlib)
  layout   the main page holds the doc's configured keys, folder keys and empty positions; the doc's
           Key table lists no position twice (in the profile, no position twice is generate.py's guard:
           a page's actions are keyed by position)
  nav      every folder key, on the main page or on a child page, opens a child page in the zip, the one the
           data file names; every child page is opened by exactly one folder key and has exactly one back key,
           at the fixed position; at most two folder levels below the main page (no folder key on a
           second-level page); a child page with no doc ("spec" missing on its data file entry) holds only
           that back key; no page is unreachable; (with --sources or --fenix) the same form as the exported
           MSFS-Fenix320-XL profile, SKIP when that file can't be read
  doc      key by key against the "Key table" of the spec doc: action, title, command and read addresses,
           On/Off values, long press, format, mappings, Decode BCD, Special State, folder keys; plus the
           template tables' values the Key table doesn't list (Toggle Switch unchecked on K-event commands,
           On/Off images, Special Image)
  child    every child page whose data file entry names a doc ("spec") against that doc's table under the
           heading "## Key table: <page id>": all 32 positions listed, the back key row at back_key_pos,
           the page's keys and Empty positions as the table says, then key by key as "doc" above (folder
           keys too: only on a first-level page, each opening the child page its row names)
  template every PilotsDeck key differs from its template only in the fields its data file entry names
           (States: Title, FontSize and TitleAlignment aside), and its FontSize is the expected title size
           (see size; TitleAlignment: see align)
  phase1   BAT, PARK and AP settings equal the Phase 1 export's apart from the fields the data file names;
           States equal apart from FontSize, which is the expected title size (see size), and apart from
           TitleAlignment only on keys with a "title_align" (see align)
  size     title sizes: generate.py's rule constants are the ruled 10 -> 14 (LR210-C4); every key entry field
           is in generate.KEY_FIELDS; every "title_size" sits on a PilotsDeck key, is an int in
           generate.TITLE_SIZES and not redundant; every PilotsDeck key's FontSize is its title_size, else 14
           where its template says 10 on a Simple or Dynamic Button, else the template's size (readout keys,
           COM Radio and Display Value, keep theirs); folder and back keys 12; prints the size counts and the
           overrides
  align    title alignment: every "title_align" is "top", "middle" or "bottom", sits on a key of the profile
           (not an empty entry) and is not redundant; on every key of every page (back keys too) every state's
           TitleAlignment is the key's title_align, else its template's; prints the alignment counts
  fields   every field name in the generated JSON occurs in a real saved example
  lua      every `lua:<Script>:<Function>(...)` command (data file "set" fields, profile settings fields) names a
           script file in pilotsdeck/MSFS2024-XL/_Package/Scripts (name case aside, as PilotsDeck) and a function
           defined at top level in it (a line `function <Function>(`, not indented, not `local`); prints the count
  sources  (--sources) every template in templates.json still equals the real file it was copied from;
           a source that can't be read is a SKIP with its path (it needs the Admin account's installed
           profiles unchanged and A:\\FS2024 Stuff\\PilotsDeck)
Exit code 0 when everything passes (a SKIP is not a failure).
"""
import io
import json
import os
import re
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
sys.dont_write_bytecode = True  # importing generate.py must not leave a __pycache__ folder in the repo
import generate  # noqa: E402  (the generator next to this file: its build() and template resolution)

FENIX_DEFAULT = "A:/FS2024 Stuff/PilotsDeck/Fenix A320 v1.6_Vj1pU/Profiles/MSFS-Fenix320-XL.streamDeckProfile"
ACTION_UUIDS = {
    "Dynamic Button": "com.extension.pilotsdeck.action.switch.display",
    "Display Value": "com.extension.pilotsdeck.action.display.switch",
    "COM Radio": "com.extension.pilotsdeck.action.display.radio",
    "Simple Button": "com.extension.pilotsdeck.action.switch",
    "Folder": "com.elgato.streamdeck.profile.openchild",
}
BACK = "com.elgato.streamdeck.profile.backtoparent"
# SimCommandType (PilotsDeck Plugin/Simulator/SimCommand.cs): LVAR 3 (also "no command"), HVAR 8, AVAR 12, BVAR 13,
# KVAR 16 (HVAR 8: the installed plugin's settings panel, Plugin/PI/js/pi-Common.js "type == 8 //HVar"), LUAFUNC 14
# (SimCommand.cs "LUAFUNC = 14"; pi-Common.js line 227 "type == 14 //LuaFunc"; the address form `lua:File:Function(...)`
# of the README 2.1.1 LUAFUNC section; the saved GSX Pro and Fenix reference keys hold type 14 with such addresses)
TYPE_BY_PREFIX = {"B:": 13, "K:": 16, "(A:": 12, "H:": 8, "lua:": 14}
# PilotsDeck 11bdf1f7 runs `lua:<Script>:<Function>(...)` as the Lua code `<Function>(...)` in Scripts/<script>.lua,
# the name lowercased, ".lua" dropped and added back (Plugin/Resources/Variables/ManagedAddress.cs lines 421, 475;
# Plugin/Resources/ScriptManager.cs lines 216, 383-402; Plugin/AppConfiguration.cs line 76): found by File.Exists,
# which ignores case on Windows. check.py looks in the package's copy (the user copies it into the plugin's Scripts);
# PilotsDeck also takes a running script from Scripts/global/ (ScriptManager.cs line 217): the package has none.
SCRIPTS_DIR = "pilotsdeck/MSFS2024-XL/_Package/Scripts"
MAX_LEVEL = 2  # docs/navigation.md "Rules": at most two folder levels below the main page
KVAR = TYPE_BY_PREFIX["K:"]
# Values from the doc's template tables (T1, T2 and "K-events are command-only") that the Key table doesn't list
ON_OFF_IMAGES = {"OnImage": "Images/KorryOnBlueTop.png", "OffImage": "Images/KorryOffWhiteBottom.png"}
SPECIAL_IMAGE = "Images/Fault.png"
FOLDER_TITLE_SIZE = 12  # folder and back keys keep their templates' FontSize (templates.json "folder", "back")
# The ruled title size change (P2-7, LR210-C4: the user reads titles at 14, not 10); generate.py's constants must
# equal these (R-1, LR231-C5)
RULED_TITLE_SIZE_FROM = 10
RULED_TITLE_SIZE_TO = 14
# The key kinds that get 10 -> 14 (LR231-C5 R-2 (a)), stated here on its own and not read from generate.py:
# Simple Button and Dynamic Button draw no text (PilotsDeck 11bdf1f7 Plugin/Actions/Simple/ActionSwitch.cs and
# ActionSwitchDisplay.cs: no DrawText or GetFont); Display Value (ActionDisplayText.cs) and COM Radio
# (ActionDisplayRadio.cs) draw their values with GetFont(), the title font when FontInherit is set
# (ActionBaseSimple.cs), so they keep their template size.
RULED_TITLE_SIZE_KINDS = {ACTION_UUIDS["Simple Button"], ACTION_UUIDS["Dynamic Button"]}
# Allowed "title_align" values (P2-7 A-8, LR232-C5): the Elgato Stream Deck SDK manifest reference, State
# "TitleAlignment": "bottom" | "middle" | "top" (https://docs.elgato.com/streamdeck/sdk/references/manifest)
TITLE_ALIGNS = ("top", "middle", "bottom")

failures = []
skips = []


def check(cond, msg):
    print(("  ok   " if cond else "  FAIL ") + msg)
    if not cond:
        failures.append(msg)
    return cond


def skip(msg):
    print("  SKIP " + msg)
    skips.append(msg)


def ctype(addr):
    """Command type of a command address; an unknown prefix is a ValueError (reported as a FAIL line)."""
    for prefix, t in TYPE_BY_PREFIX.items():
        if addr.startswith(prefix):
            return t
    raise ValueError(f"command {addr!r} has an unknown prefix ({' or '.join(TYPE_BY_PREFIX)} expected)")


def key_of(pos):
    row, col = (int(x) for x in pos.split(","))
    return f"{col - 1},{row - 1}"


def read_profile(path):
    z = zipfile.ZipFile(path)
    j = {}
    for n in z.namelist():
        if n.endswith(".json"):
            j[n] = json.loads(z.read(n).decode("utf-8"))
    return z, j


def profile_parts(names, j):
    prof = next(n for n in j if n.count("/") == 2 and n.endswith(".sdProfile/manifest.json"))
    base = prof.rsplit("/", 1)[0] + "/Profiles/"
    pages = {n[len(base):].split("/")[0]: j[n] for n in j if n.startswith(base) and n.endswith("/manifest.json")}
    return prof, base, pages


def actions(page):
    return page["Controllers"][0]["Actions"] or {}


def expected_title_size(key, states, kind):
    """(expected FontSize, problem or None) of a PilotsDeck key of action UUID `kind` whose template states are
    `states`: the key's title_size, else 14 where the template says 10 on a Simple or Dynamic Button, else the
    template's own size (the ruled constants and kinds above)."""
    bases = {s.get("FontSize") for s in states}
    if len(bases) != 1:
        return None, f"template states hold FontSize {sorted(map(repr, bases))}"
    base = bases.pop()
    auto = RULED_TITLE_SIZE_TO if base == RULED_TITLE_SIZE_FROM and kind in RULED_TITLE_SIZE_KINDS else base
    if "title_size" not in key:
        return auto, None
    v = key["title_size"]
    if type(v) is not int or v not in generate.TITLE_SIZES:
        return auto, f"title_size {v!r} is not an int in {list(generate.TITLE_SIZES)}"
    if v == auto:
        return auto, f"title_size {v} is redundant (the rule gives {auto})"
    return v, None


def template_align(states):
    """The one TitleAlignment of a template's states (a list of them if the states disagree: never equal to a
    key's alignment, so the key FAILs)."""
    aligns = {s.get("TitleAlignment") for s in states}
    return aligns.pop() if len(aligns) == 1 else sorted(map(repr, aligns))


def ticks(text):
    return re.findall(r"`([^`]*)`", text)


def parse_key_table(md, heading="## Key table"):
    """The table rows under the heading, by position (the first row of a position), and the positions
    listed more than once (a second row for a position is never read: the checks fail on it)."""
    lines = md.splitlines()
    i = lines.index(heading)
    rows = {}
    dups = []
    for line in lines[i + 1:]:
        if line.startswith("## "):
            break
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 7 and re.fullmatch(r"\d,\d", cells[0]):
            if cells[0] in rows:
                dups.append(cells[0])
                continue
            rows[cells[0]] = dict(zip(["pos", "title", "action", "template", "command", "read", "display"], cells))
    return rows, dups


def expected_from_row(r):
    """What the doc's Key table row says the saved settings must hold."""
    e = {}
    cmd, read, disp = r["command"], r["read"], r["display"]
    if r["action"] in ("Empty", "Folder", "Back"):
        return e
    if cmd.startswith("none"):
        e.update(ActionType=3, AddressAction="")
    elif cmd.startswith("Main "):
        main, second = ticks(cmd)[:2]
        e.update(AddressAction=main, ActionType=ctype(main), HasLongPress=True,
                 AddressActionLong=second, ActionTypeLong=ctype(second))
    else:
        t = ticks(cmd)
        e.update(AddressAction=t[0], ActionType=ctype(t[0]), HasLongPress=False)
        if "On `" in cmd:
            e.update(SwitchOnState=t[1], SwitchOffState=t[2])
        else:
            e.update(SwitchOnState="", SwitchOffState="")
    if e["ActionType"] == KVAR:
        e["ToggleSwitch"] = False  # "K-events are command-only": Toggle Switch unchecked
    if read.startswith("Active"):
        a, s = ticks(read)[:2]
        e.update(AddressRadioActiv=a, AddressRadioStandby=s)
    elif read.startswith("none"):
        e.update(Address="")
    else:
        e.update(Address=ticks(read)[0])
    m = re.search(r"Format `([^`]*)`", disp)
    e["Format"] = m.group(1) if m else ""
    m = re.search(r"Mappings `([^`]*)`", disp)
    e["ValueMappings"] = m.group(1) if m else ""
    e["DecodeBCD"] = "Decode BCD" in disp
    special = "Special State" in disp
    e["HasIndication"] = special
    if special:
        e.update(IndicationValueAny=True, IndicationImage=SPECIAL_IMAGE)  # T1: Special Image
    if "On/Off image" in disp:
        # T1, T2: On Image / Off Image; the On/Off States values are 1 / 0 unless the cell names others
        m = re.search(r"On/Off image: On `([^`]*)`, Off `([^`]*)`", disp)
        e.update(OnState=m.group(1) if m else "1", OffState=m.group(2) if m else "0", **ON_OFF_IMAGES)
    return e


def check_keys(label, acts, rows, keys_by_pos, page_uuid):
    """Key by key: the actions of one page against its doc Key table rows (page_uuid: page id -> page UUID)."""
    for pos, r in rows.items():
        k = key_of(pos)
        a = acts.get(k)
        title = (ticks(r["title"]) or [""])[0]
        if r["action"] == "Empty":
            check(a is None, f"{label}{pos} Empty")
            continue
        if a is None:
            check(False, f"{label}{pos} {title}: no action at {k}")
            continue
        if r["action"] == "Back":
            check(a["UUID"] == BACK, f"{label}{pos} Back: back key ({a['UUID']})")
            continue
        check(a["UUID"] == ACTION_UUIDS[r["action"]], f"{label}{pos} {title}: {r['action']} ({a['UUID']})")
        check(a["States"][0].get("Title") == title, f"{label}{pos} {title}: title")
        if r["action"] == "Folder":
            child = keys_by_pos.get(pos, {}).get("folder")
            if not check(child is not None, f"{label}{pos} {title}: the data file has a folder key here"):
                continue
            check(child.lower() in r["command"].lower(), f"{label}{pos} {title}: doc names the child page '{child}'")
            target = (a.get("Settings") or {}).get("ProfileUUID")
            check(target == page_uuid.get(child), f"{label}{pos} {title}: opens page '{child}' ({target})")
            continue
        sm = a["Settings"]["settingsModel"]
        try:
            exp = expected_from_row(r)
        except (ValueError, IndexError) as ex:
            check(False, f"{label}{pos} {title}: the Key table row can't be read: {ex}")
            continue
        bad = {f: (sm.get(f), v) for f, v in exp.items() if sm.get(f) != v}
        check(not bad, f"{label}{pos} {title}: " + ", ".join(f"{f}={v!r}" for f, v in exp.items()) + (f"  MISMATCH {bad}" if bad else ""))


def main():
    args = sys.argv[1:]
    sources = "--sources" in args
    fenix = FENIX_DEFAULT if sources else None
    if "--fenix" in args:
        fenix = args[args.index("--fenix") + 1]
    pos_args = [a for i, a in enumerate(args) if not a.startswith("--") and (i == 0 or args[i - 1] != "--fenix")]
    data_path = Path(pos_args[0]) if pos_args else HERE / "c172-g1000.json"
    data = json.loads(data_path.read_text(encoding="utf-8"))
    templates = json.loads((HERE / "templates.json").read_text(encoding="utf-8"))
    out_path = ROOT / data["output"]

    print("== zip: the profile opens, every JSON entry parses")
    try:
        z, j = read_profile(out_path)
        check(z.testzip() is None, f"{data['output']}: zip CRCs ok, {len(z.namelist())} entries")
        check(True, f"{len(j)} JSON entries parse")
    except Exception as ex:  # noqa: BLE001
        check(False, f"cannot read {out_path}: {ex}")
        return 1

    print("== current: the profile on disk is what generate.py builds now (names, order, uncompressed content)")
    try:
        _, blob = generate.build(data_path)
        fresh = zipfile.ZipFile(io.BytesIO(blob))
        check(fresh.namelist() == z.namelist(),
              f"{len(fresh.namelist())} entry names in the same order as a fresh build")
        stale = [n for n in fresh.namelist() if n in z.namelist() and fresh.read(n) != z.read(n)]
        check(not stale, "every entry's uncompressed content equals a fresh build" +
              (f"  DIFFERENT: {stale} (regenerate: python tools/profilegen/generate.py)" if stale else ""))
    except Exception as ex:  # noqa: BLE001
        check(False, f"generate.build({data_path}) failed: {type(ex).__name__}: {ex}")
    prof_name, base, pages = profile_parts(z.namelist(), j)
    profile = j[prof_name]
    check(profile["Name"] == data["profile_name"], f"profile name {profile['Name']!r}")
    main_id = profile["Pages"]["Pages"][0].upper()
    main = pages[main_id]
    p1z, p1j = read_profile(ROOT / data["phase1_export"])
    p1prof, _, p1pages = profile_parts(p1z.namelist(), p1j)
    p1main = actions(p1pages[p1j[p1prof]["Pages"]["Pages"][0].upper()])

    print("== layout: main page against the doc's Key table")
    rows, dups = parse_key_table((ROOT / data["spec"]).read_text(encoding="utf-8"))
    check(len(rows) == 32, f"doc Key table has {len(rows)} rows (32 expected)")
    check(not dups, "doc Key table lists no position twice" + (f"  TWICE: {dups}" if dups else ""))
    configured = [p for p, r in rows.items() if r["action"] not in ("Empty", "Folder")]
    folders = [p for p, r in rows.items() if r["action"] == "Folder"]
    empties = [p for p, r in rows.items() if r["action"] == "Empty"]
    print(f"  doc: {len(configured)} configured, {len(folders)} folder keys {folders}, {len(empties)} empty {empties}")
    acts = actions(main)
    gen_conf = [k for k, a in acts.items() if a["UUID"].startswith("com.extension.pilotsdeck")]
    gen_fold = [k for k, a in acts.items() if a["UUID"] == ACTION_UUIDS["Folder"]]
    check(sorted(gen_conf) == sorted(key_of(p) for p in configured), f"{len(gen_conf)} configured PilotsDeck keys at the doc's positions")
    check(sorted(gen_fold) == sorted(key_of(p) for p in folders), f"{len(gen_fold)} folder keys at the doc's positions")
    check(all(key_of(p) not in acts for p in empties), f"empty positions {empties} hold no action")
    check(len(acts) == len(configured) + len(folders), f"main page holds {len(acts)} actions in all")

    print("== nav: folders, child pages, back keys")
    back_key = key_of(data["back_key_pos"])
    listed = {p.upper() for p in profile["Pages"]["Pages"]} | {profile["Pages"]["Default"].upper()}
    data_page = {generate.uid(data["profile_name"], "page", p["id"]).upper(): p for p in data["pages"]}
    page_uuid = {p["id"]: generate.uid(data["profile_name"], "page", p["id"]) for p in data["pages"]}
    page_id = lambda pid: data_page.get(pid, {}).get("id", "?")  # noqa: E731
    children = {}  # child page -> (the page its folder key sits on, that key)
    for src in sorted(pages, key=lambda p: (p != main_id, p)):
        for k, a in sorted(actions(pages[src]).items()):
            if a["UUID"] != ACTION_UUIDS["Folder"]:
                continue
            target = a["Settings"]["ProfileUUID"]
            where = f"folder key {k}" if src == main_id else f"folder key {k} on child page {page_id(src)}"
            check(target == target.lower() and target.upper() in pages, f"{where} -> child page {target} exists in the zip")
            check(target.upper() not in children, f"{where}: page {target} is opened by no other folder key" +
                  (f"  ALSO BY {children.get(target.upper())}" if target.upper() in children else ""))
            check(target.upper() not in listed, f"{where}: its target is not the main or the Default page")
            children.setdefault(target.upper(), (src, k))
    # folder levels below the main page: 1 = opened from the main page, 2 = from a first-level page
    level = {main_id: 0}
    todo = [main_id]
    while todo:
        cur = todo.pop(0)
        for c, (src, _) in sorted(children.items()):
            if src == cur and c not in level:
                level[c] = level[cur] + 1
                todo.append(c)
    for pid, page in pages.items():
        if pid in listed:
            continue
        a = actions(page)
        dp = data_page.get(pid, {})
        name = f"child page {dp.get('id', '?')} ({pid})"
        src, key = children.get(pid, (None, None))
        check(pid in children, f"{name} is opened by folder key {key}" + ("" if src in (None, main_id) else f" on child page {page_id(src)}"))
        check(pid in level and level[pid] <= MAX_LEVEL,
              f"{name} is {level.get(pid, '?')} folder level(s) below the main page (at most {MAX_LEVEL}), reachable from it")
        if src is not None and src in data_page:
            check(dp.get("parent") == data_page[src]["id"], f"{name}: its data file parent is the page its folder key sits on ({data_page[src]['id']})")
        backs = [k for k, x in a.items() if x["UUID"] == BACK]
        check(backs == [back_key], f"{name} has exactly one back key, at {back_key} (doc {data['back_key_pos']})")
        if "spec" in dp:
            print(f"  {name}: its keys are checked against {dp['spec']} under 'child' below")
        else:
            check(list(a) == [back_key], f"{name} has no doc ('spec') and holds only the back key")
        check(f"{base}{pid}/Images/" in z.namelist(), f"{name} has its Images/ folder entry")
    check(actions(pages[profile["Pages"]["Default"].upper()]) == {}, "the profile's Default page is empty (Actions null), as in Phase 1")
    check(len(pages) == len(listed) + len(children), f"{len(pages)} pages: {len(listed)} listed + {len(children)} reachable child pages, none unreachable")
    if fenix is None:
        print("  (the comparison with the Fenix XL export runs with --sources or --fenix <path>)")
    elif not os.path.isfile(fenix):
        skip(f"Fenix XL export not readable at {fenix}: back-key and folder-key form not compared")
    else:
        fz, fj = read_profile(fenix)
        fprof, fbase, fpages = profile_parts(fz.namelist(), fj)
        fp = fj[fprof]
        print(f"  compared with {fenix} ({fprof})")
        flisted = {p.upper() for p in fp["Pages"]["Pages"]} | {fp["Pages"]["Default"].upper()}
        fchild = [p for p in fpages if p not in flisted]
        fback = [(p, k) for p in fchild for k, a in actions(fpages[p]).items() if a["UUID"] == BACK]
        fpos = {k for _, k in fback}
        print(f"  Fenix: {len(fp['Pages']['Pages'])} listed page, {len(fchild)} child pages, back keys at {sorted(fpos)} on {len(fback)} of them")
        check(len(fp["Pages"]["Pages"]) == 1 and len(profile["Pages"]["Pages"]) == 1, "one listed page; child pages are not in Pages.Pages (as Fenix)")
        check(fpos == {back_key}, f"back key position {back_key} is the Fenix one")
        strip = lambda a: {k: v for k, v in a.items() if k != "ActionID"}  # noqa: E731
        fforms = [json.dumps(strip(actions(fpages[p])[k]), sort_keys=True) for p, k in fback]
        common = max(set(fforms), key=fforms.count)
        ours = {json.dumps(strip(actions(pages[p])[back_key]), sort_keys=True) for p in children}
        check(ours == {common}, f"back key equals the Fenix form used on {fforms.count(common)} of {len(fforms)} child pages (ActionID aside)")
        fold = [a for p in fpages.values() for a in actions(p).values() if a["UUID"] == ACTION_UUIDS["Folder"]]
        check(all(set(a["Settings"]) == {"ProfileUUID"} for a in fold) and
              all(set(actions(pages[s])[k]["Settings"]) == {"ProfileUUID"} for s, k in children.values()),
              f"folder keys link by Settings.ProfileUUID only (lowercase), as all {len(fold)} Fenix folder keys")
        check(all(a["Settings"]["ProfileUUID"].upper() in fpages for a in fold), "(Fenix: every folder target is a page folder in its zip)")
        check(all(f"{fbase}{p}/Images/" in fz.namelist() for p in fchild), "(Fenix: every child page has an Images/ entry)")
        ochild = "com.elgato.streamdeck.profile.openchild"
        check(ochild in fj["package.json"]["RequiredPlugins"] and ochild in j["package.json"]["RequiredPlugins"],
              "package.json RequiredPlugins lists the folder action, as the Fenix export")

    print("== doc: key by key against the Key table")
    keys_by_pos = {}
    for page in data["pages"]:
        if page["id"] == data["pages"][0]["id"]:
            keys_by_pos = {k["pos"]: k for k in page["keys"]}
    check_keys("", acts, rows, keys_by_pos, page_uuid)

    print("== child: child pages with a doc, key by key against their own Key table")
    with_doc = [p for p in data["pages"][1:] if "spec" in p]
    if not with_doc:
        print("  (no child page names a doc yet: every child page holds only its back key, checked under 'nav')")
    for dp in with_doc:
        heading = f"## Key table: {dp['id']}"
        label = f"{dp['id']} "
        try:
            crows, cdups = parse_key_table((ROOT / dp["spec"]).read_text(encoding="utf-8"), heading)
        except (OSError, ValueError) as ex:
            check(False, f"{dp['id']}: cannot read the table '{heading}' in {dp['spec']}: {type(ex).__name__}: {ex}")
            continue
        cpid = generate.uid(data["profile_name"], "page", dp["id"]).upper()
        cacts = actions(pages[cpid])
        grid_pos = [f"{r},{c}" for r in range(1, data["grid"]["rows"] + 1) for c in range(1, data["grid"]["columns"] + 1)]
        check(sorted(crows) == sorted(grid_pos) and not cdups,
              f"{dp['id']}: {dp['spec']} '{heading}' lists all {len(grid_pos)} positions once ({len(crows) + len(cdups)} rows)" +
              (f"  TWICE: {cdups}" if cdups else ""))
        bp = data["back_key_pos"]
        check(crows.get(bp, {}).get("action") == "Back", f"{dp['id']}: the doc's row {bp} is the back key")
        backs = [p for p, r in crows.items() if r["action"] == "Back"]
        check(backs == [bp], f"{dp['id']}: the doc lists one back key, at {bp}")
        cconf = [p for p, r in crows.items() if r["action"] not in ("Empty", "Back")]
        cempty = [p for p, r in crows.items() if r["action"] == "Empty"]
        cfold = [p for p, r in crows.items() if r["action"] == "Folder"]
        print(f"  {dp['id']}: doc: {len(cconf)} keys {cconf}, {len(cempty)} empty, {len(cfold)} folder keys {cfold}")
        check(sorted(cacts) == sorted(key_of(p) for p in cconf + backs),
              f"{dp['id']}: the page holds exactly the doc's keys and back key ({len(cacts)} actions)")
        check(sorted(k["pos"] for k in dp["keys"] if "empty" not in k) == sorted(cconf),
              f"{dp['id']}: the data file's keys are at the doc's key positions")
        lvl = level.get(cpid)
        if lvl is not None and lvl >= MAX_LEVEL:
            check(not cfold, f"{dp['id']}: a page {lvl} levels below the main page lists no folder key (at most {MAX_LEVEL} levels)" +
                  (f"  FOLDER KEYS: {cfold}" if cfold else ""))
        else:
            check(sorted(k["pos"] for k in dp["keys"] if "folder" in k) == sorted(cfold),
                  f"{dp['id']}: folder keys at the doc's Folder rows {cfold} (a page {lvl} level below the main page)")
        check_keys(label, cacts, crows, {k["pos"]: k for k in dp["keys"]}, page_uuid)

    print("== template: every PilotsDeck key differs from its template only in the fields the data file names")
    resolve = generate.load_templates(generate.Phase1(ROOT / data["phase1_export"]))
    for page in data["pages"]:
        page_acts = actions(pages[generate.uid(data["profile_name"], "page", page["id"]).upper()])
        for key in page["keys"]:
            if "template" not in key:
                continue
            label = f"{page['id']} {key['pos']} {key['title']}"
            a = page_acts.get(key_of(key["pos"]))
            if a is None:
                check(False, f"{label}: no action at {key_of(key['pos'])}")
                continue
            t = resolve(key["template"])
            src = key["template"]
            if key.get("states_from"):
                t["States"] = resolve(key["states_from"])["States"]
                src += f", states from {key['states_from']}"
            named, shell = key.get("set", {}), key.get("shell", {})
            tm, am = t["Settings"]["settingsModel"], a["Settings"]["settingsModel"]
            diff = {f for f in set(tm) | set(am) if tm.get(f) != am.get(f)}
            wrong = {f: am.get(f) for f, v in named.items() if am.get(f) != v}
            check(diff <= set(named) and not wrong,
                  f"{label}: settings differ from {src} only in the named fields (found {sorted(diff) or 'none'})" +
                  (f"  NOT NAMED {sorted(diff - set(named))}" if diff - set(named) else "") +
                  (f"  NOT AS NAMED {wrong}" if wrong else ""))
            rest = {f for f in set(t) | set(a)
                    if f not in ("ActionID", "Settings", "States") and shell.get(f, t.get(f)) != a.get(f)}
            no_title = lambda states: [{k: v for k, v in s.items() if k not in ("Title", "FontSize", "TitleAlignment")} for s in states]  # noqa: E731
            check(not rest and no_title(t["States"]) == no_title(a["States"]),
                  f"{label}: other action fields and States (title, FontSize and TitleAlignment aside) as the template" +
                  (f", with {shell}" if shell else "") + (f"  DIFFERENT {sorted(rest)}" if rest else ""))
            want, problem = expected_title_size(key, t["States"], shell.get("UUID", t["UUID"]))
            got = [s.get("FontSize") for s in a["States"]]
            check(problem is None and all(g == want for g in got),
                  f"{label}: FontSize {got} = {want} (template {sorted({s.get('FontSize') for s in t['States']})}" +
                  (f", title_size {key['title_size']!r}" if "title_size" in key else "") + ")" +
                  (f"  {problem}" if problem else ""))

    print("== phase1: BAT, PARK, AP against the Phase 1 export")
    for pos in ("1,1", "1,4", "2,1"):
        key = keys_by_pos[pos]
        src = p1main[key["template"][3:]]
        a = acts[key_of(pos)]
        named = set(key.get("set", {}))
        diff = {f for f in set(src["Settings"]["settingsModel"]) | set(a["Settings"]["settingsModel"])
                if src["Settings"]["settingsModel"].get(f) != a["Settings"]["settingsModel"].get(f)}
        check(diff == named, f"{pos} {key['title']}: settings differ only in the named fields {sorted(named) or 'none'} (found {sorted(diff) or 'none'})")
        no_size = lambda states: [{k: v for k, v in s.items()  # noqa: E731
                                   if k != "FontSize" and not (k == "TitleAlignment" and "title_align" in key)} for s in states]
        same_rest = all(src[f] == a[f] for f in src if f not in ("ActionID", "Settings", "States")) and \
            no_size(src["States"]) == no_size(a["States"])
        check(same_rest, f"{pos} {key['title']}: Name, Plugin, UUID, States (FontSize aside, see size" +
              ("; TitleAlignment aside, see align" if "title_align" in key else "; TitleAlignment included") +
              "), LinkedTitle equal the Phase 1 key")
        want, problem = expected_title_size(key, src["States"], key.get("shell", {}).get("UUID", src["UUID"]))
        got = [s.get("FontSize") for s in a["States"]]
        check(problem is None and all(g == want for g in got),
              f"{pos} {key['title']}: FontSize {got} = {want} (Phase 1 {[s.get('FontSize') for s in src['States']]})" +
              (f"  {problem}" if problem else ""))

    print("== size: title sizes (States FontSize)")
    check(generate.TITLE_SIZE_FROM == RULED_TITLE_SIZE_FROM and generate.TITLE_SIZE_TO == RULED_TITLE_SIZE_TO,
          f"generate.py's title size rule is the ruled {RULED_TITLE_SIZE_FROM} -> {RULED_TITLE_SIZE_TO} (LR210-C4)" +
          (f"  FOUND TITLE_SIZE_FROM {generate.TITLE_SIZE_FROM!r} -> TITLE_SIZE_TO {generate.TITLE_SIZE_TO!r}"
           if (generate.TITLE_SIZE_FROM, generate.TITLE_SIZE_TO) != (RULED_TITLE_SIZE_FROM, RULED_TITLE_SIZE_TO) else ""))
    sizes = {}  # FontSize -> number of keys, over every page of the profile
    for page in data["pages"]:
        page_acts = actions(pages[generate.uid(data["profile_name"], "page", page["id"]).upper()])
        bad = []
        for key in page["keys"]:
            label = f"{page['id']} {key.get('pos')} {key.get('title', '')}".rstrip()
            unknown = sorted(set(key) - generate.KEY_FIELDS)
            check(not unknown, f"{label}: key entry fields all in KEY_FIELDS" + (f"  UNKNOWN {unknown}" if unknown else ""))
            if "title_size" in key and "template" not in key:
                check(False, f"{label}: title_size {key['title_size']!r} on {'a folder' if 'folder' in key else 'an empty' if 'empty' in key else 'a non-PilotsDeck'} entry")
            if "empty" in key:
                continue
            a = page_acts.get(key_of(key["pos"]))
            if a is None:
                bad.append(f"{key['pos']} no action")
                continue
            got = [s.get("FontSize") for s in a["States"]]
            if "folder" in key:
                want = FOLDER_TITLE_SIZE
            else:
                t = resolve(key["states_from"] if key.get("states_from") else key["template"])
                kind = key.get("shell", {}).get("UUID", resolve(key["template"])["UUID"])
                want, problem = expected_title_size(key, t["States"], kind)
                if "title_size" in key:
                    check(problem is None, f"{label}: title_size {key['title_size']!r} is an int in {list(generate.TITLE_SIZES)}, not redundant" +
                          (f"  {problem}" if problem else ""))
            if any(g != want for g in got):
                bad.append(f"{key['pos']} {key.get('title')} {got} (expected {want})")
        if "parent" in page:
            back = page_acts.get(key_of(data["back_key_pos"]))
            if back is None or any(s.get("FontSize") != FOLDER_TITLE_SIZE for s in back["States"]):
                bad.append(f"{data['back_key_pos']} back key {back and [s.get('FontSize') for s in back['States']]} (expected {FOLDER_TITLE_SIZE})")
        for a in page_acts.values():
            sizes[a["States"][0].get("FontSize")] = sizes.get(a["States"][0].get("FontSize"), 0) + 1
        check(not bad, f"{page['id']}: every key's FontSize as expected ({len(page_acts)} keys; folder and back keys {FOLDER_TITLE_SIZE})" +
              (f"  WRONG {bad}" if bad else ""))
    overrides = [f"{p['id']} {k['pos']} {k.get('title')}={k['title_size']!r}" for p in data["pages"] for k in p["keys"] if "title_size" in k]
    print(f"  size counts ({sum(sizes.values())} keys): " + " ".join(f"{s}:{n}" for s, n in sorted(sizes.items(), key=lambda x: -x[1])))
    print(f"  {len(overrides)} title_size overrides: {overrides}")

    print("== align: title alignment (States TitleAlignment)")
    aligns = {}  # TitleAlignment -> number of keys, over every page of the profile
    for page in data["pages"]:
        page_acts = actions(pages[generate.uid(data["profile_name"], "page", page["id"]).upper()])
        expected = {}  # position in the manifest -> (label, expected TitleAlignment)
        if "parent" in page:
            expected[key_of(data["back_key_pos"])] = (f"{page['id']} {data['back_key_pos']} back key",
                                                     template_align(templates["back"]["action"]["States"]))
        for key in page["keys"]:
            label = f"{page['id']} {key.get('pos')} {key.get('title', '')}".rstrip()
            if "empty" in key:
                if "title_align" in key:
                    check(False, f"{label}: title_align {key['title_align']!r} on an empty entry")
                continue
            if "folder" in key:
                states = templates["folder"]["action"]["States"]
            else:
                states = resolve(key["states_from"] if key.get("states_from") else key["template"])["States"]
            base = template_align(states)
            want = base
            if "title_align" in key:
                v = key["title_align"]
                ok = type(v) is str and v in TITLE_ALIGNS
                check(ok, f"{label}: title_align {v!r} is one of {list(TITLE_ALIGNS)}")
                check(v != base, f"{label}: title_align {v!r} is not redundant (template {base!r})")
                check(key_of(key["pos"]) in page_acts, f"{label}: title_align sits on a key of the profile")
                want = v
            expected[key_of(key["pos"])] = (label, want)
        bad = []
        for k, a in sorted(page_acts.items()):
            label, want = expected.get(k, (f"{page['id']} {k} (no data file entry)", None))
            got = [s.get("TitleAlignment") for s in a["States"]]
            aligns[got[0]] = aligns.get(got[0], 0) + 1
            if want is None or any(g != want for g in got):
                bad.append(f"{label} {got} (expected {want!r})")
        check(not bad, f"{page['id']}: every key's TitleAlignment as expected ({len(page_acts)} keys)" +
              (f"  WRONG {bad}" if bad else ""))
    set_aligns = [f"{p['id']} {k['pos']} {k.get('title')}={k['title_align']!r}" for p in data["pages"] for k in p["keys"] if "title_align" in k]
    print(f"  alignment counts ({sum(aligns.values())} keys): " + " ".join(f"{s}:{n}" for s, n in sorted(aligns.items(), key=lambda x: -x[1])))
    print(f"  {len(set_aligns)} title_align settings: {set_aligns}")

    print("== fields: every field name occurs in a real saved example")
    p1_model = set(next(iter(p1main.values()))["Settings"]["settingsModel"])
    p1_top = set().union(*(set(a) for a in p1main.values()))
    p1_state = set().union(*(set(s) for a in p1main.values() for s in a["States"]))
    ex = {"folder": templates["folder"]["action"], "back": templates["back"]["action"]}
    for pid, page in pages.items():
        check(set(page) <= set(p1j[next(n for n in p1j if n.endswith('manifest.json') and n.count('/') == 4)]),
              f"page {pid}: manifest fields {sorted(page)} (Phase 1 page manifest)")
        for k, a in actions(page).items():
            if a["UUID"].startswith("com.extension.pilotsdeck"):
                ok = set(a["Settings"]["settingsModel"]) <= p1_model and set(a) <= p1_top and \
                    all(set(s) <= p1_state for s in a["States"])
                check(ok, f"{pid[:8]} {k} {a['Name']}: {len(a['Settings']['settingsModel'])} settings fields, action and state fields all in the Phase 1 export's keys")
            else:
                t = ex["folder" if a["UUID"] == ACTION_UUIDS["Folder"] else "back"]
                ok = set(a) <= set(t) and set(a["Settings"] or {}) <= set(t["Settings"] or {}) and \
                    all(set(s) <= set(t["States"][0]) for s in a["States"])
                check(ok, f"{pid[:8]} {k} {a['Name']}: fields all in templates.json '{'folder' if a['UUID'] == ACTION_UUIDS['Folder'] else 'back'}' ({templates['folder' if a['UUID'] == ACTION_UUIDS['Folder'] else 'back']['source']['file']})")
    check(set(profile) <= set(p1j[p1prof]) and set(profile["Pages"]) <= set(p1j[p1prof]["Pages"]), "profile manifest fields as in the Phase 1 export")
    check(set(j["package.json"]) <= set(p1j["package.json"]), "package.json fields as in the Phase 1 export")

    print(f"== lua: every lua: command names a script file in {SCRIPTS_DIR} and a top-level function in it")
    scripts = {p.name.lower(): p for p in (ROOT / SCRIPTS_DIR).glob("*.lua")}
    calls = [(f"data file {p['id']} {k['pos']} {k.get('title', '')}", f, v) for p in data["pages"] for k in p["keys"]
             for f, v in k.get("set", {}).items() if isinstance(v, str) and v.startswith("lua:")]
    calls += [(f"profile {page_id(pid)} {int(k.split(',')[1]) + 1},{int(k.split(',')[0]) + 1} {a['States'][0].get('Title', '')}", f, v)
              for pid, page in sorted(pages.items()) for k, a in sorted(actions(page).items())
              for f, v in ((a.get("Settings") or {}).get("settingsModel") or {}).items() if isinstance(v, str) and v.startswith("lua:")]
    for where, field, cmd in calls:
        script, _, func = cmd[len("lua:"):].partition(":")
        func = func.split("(")[0].strip()
        path = scripts.get(script.lower().replace(".lua", "") + ".lua")
        if not check(path is not None, f"{where}: {field} {cmd}: script file {SCRIPTS_DIR}/{script}.lua " +
                     ("found" if path else "not found")):
            continue
        defs = re.findall(r"^function\s+([A-Za-z_]\w*)\s*\(", path.read_text(encoding="utf-8"), re.M)
        check(func in defs, f"{where}: {field} {cmd}: function {func!r} " +
              (f"defined at top level in {path.name}" if func in defs else f"not defined at top level in {path.name} (top level: {defs})"))
    print(f"  {len(calls)} lua: calls checked ({sum(w.startswith('data') for w, _, _ in calls)} in the data file, "
          f"{sum(w.startswith('profile') for w, _, _ in calls)} in the profile), scripts in {SCRIPTS_DIR}: {sorted(p.name for p in scripts.values())}")

    if sources:
        print("== sources: templates.json against the real files")
        for name, t in templates.items():
            if not isinstance(t, dict) or "action" not in t:
                continue
            s = t["source"]
            path = os.path.expandvars(s["file"])
            try:
                if s["kind"] == "zip":
                    real = json.loads(zipfile.ZipFile(path).read(s["entry"]))
                else:
                    real = json.loads(Path(path).read_text(encoding="utf-8"))
            except (OSError, zipfile.BadZipFile) as ex2:
                skip(f"{name}: source not readable, not compared: {path} ({type(ex2).__name__})")
                continue
            check(actions(real).get(s["pos"]) == t["action"], f"{name}: equals {s['file']} {s.get('entry', '')} at {s['pos']}")

    print()
    result = "PASS" if not failures else f"FAIL ({len(failures)})"
    print("RESULT:", result + (f", {len(skips)} SKIP" if skips else ""))
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
