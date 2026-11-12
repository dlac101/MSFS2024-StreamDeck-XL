"""Check a generated profile against the spec doc, the Phase 1 export and real saved examples.

Usage, from the repo root (Python 3, standard library only):

    python tools/profilegen/check.py                 # uses tools/profilegen/c172-g1000.json
    python tools/profilegen/check.py <data.json> [--sources] [--fenix <MSFS-Fenix320-XL.streamDeckProfile>]

Plain check.py reads only files in the repo. --sources (and --fenix) also read files outside it.

Checks:
  zip      the profile opens and every JSON entry parses
  current  the profile on disk is what generate.py builds now from the data file: same entry names, same
           order, same uncompressed content (the compressed bytes may differ with another zlib)
  layout   the main page holds the doc's configured keys, folder keys and empty positions
           (no position twice is generate.py's guard: a page's actions are keyed by position)
  nav      every folder key opens a child page in the zip; every child page holds exactly one key, the back
           key, at the fixed position; no page is unreachable; (with --sources or --fenix) the same form as
           the exported MSFS-Fenix320-XL profile, SKIP when that file can't be read
  doc      key by key against the "Key table" of the spec doc: action, title, command and read addresses,
           On/Off values, long press, format, mappings, Decode BCD, Special State, folder keys; plus the
           template tables' values the Key table doesn't list (Toggle Switch unchecked on K-event commands,
           On/Off images, Special Image)
  template every PilotsDeck key differs from its template only in the fields its data file entry names
  phase1   BAT, PARK and AP settings equal the Phase 1 export's apart from the fields the data file names
  fields   every field name in the generated JSON occurs in a real saved example
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
# SimCommandType (PilotsDeck Plugin/Simulator/SimCommand.cs): LVAR 3 (also "no command"), BVAR 13, KVAR 16
TYPE_BY_PREFIX = {"B:": 13, "K:": 16}
KVAR = TYPE_BY_PREFIX["K:"]
# Values from the doc's template tables (T1, T2 and "K-events are command-only") that the Key table doesn't list
ON_OFF_IMAGES = {"OnImage": "Images/KorryOnBlueTop.png", "OffImage": "Images/KorryOffWhiteBottom.png"}
SPECIAL_IMAGE = "Images/Fault.png"

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
    t = TYPE_BY_PREFIX.get(addr[:2])
    if t is None:
        raise ValueError(f"command {addr!r} has an unknown prefix ({' or '.join(TYPE_BY_PREFIX)} expected)")
    return t


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


def ticks(text):
    return re.findall(r"`([^`]*)`", text)


def parse_key_table(md):
    lines = md.splitlines()
    i = lines.index("## Key table")
    rows = {}
    for line in lines[i + 1:]:
        if line.startswith("## "):
            break
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 7 and re.fullmatch(r"\d,\d", cells[0]):
            rows[cells[0]] = dict(zip(["pos", "title", "action", "template", "command", "read", "display"], cells))
    return rows


def expected_from_row(r):
    """What the doc's Key table row says the saved settings must hold."""
    e = {}
    cmd, read, disp = r["command"], r["read"], r["display"]
    if r["action"] in ("Empty", "Folder"):
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
        e.update(OnState="1", OffState="0", **ON_OFF_IMAGES)  # T1, T2: On Image / Off Image
    return e


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
    rows = parse_key_table((ROOT / data["spec"]).read_text(encoding="utf-8"))
    check(len(rows) == 32, f"doc Key table has {len(rows)} rows (32 expected)")
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
    children = {}
    for k, a in acts.items():
        if a["UUID"] == ACTION_UUIDS["Folder"]:
            target = a["Settings"]["ProfileUUID"]
            children[target.upper()] = k
            check(target == target.lower() and target.upper() in pages, f"folder key {k} -> child page {target} exists in the zip")
    listed = {p.upper() for p in profile["Pages"]["Pages"]} | {profile["Pages"]["Default"].upper()}
    for pid, page in pages.items():
        if pid in listed:
            continue
        a = actions(page)
        check(pid in children, f"child page {pid} is opened by folder key {children.get(pid)}")
        check(list(a) == [back_key] and a[back_key]["UUID"] == BACK,
              f"child page {pid} holds exactly one key, the back key at {back_key} (doc {data['back_key_pos']})")
        check(f"{base}{pid}/Images/" in z.namelist(), f"child page {pid} has its Images/ folder entry")
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
              all(set(acts[k]["Settings"]) == {"ProfileUUID"} for k in children.values()),
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
    for pos, r in rows.items():
        k = key_of(pos)
        a = acts.get(k)
        title = (ticks(r["title"]) or [""])[0]
        if r["action"] == "Empty":
            check(a is None, f"{pos} Empty")
            continue
        if a is None:
            check(False, f"{pos} {title}: no action at {k}")
            continue
        check(a["UUID"] == ACTION_UUIDS[r["action"]], f"{pos} {title}: {r['action']} ({a['UUID']})")
        check(a["States"][0].get("Title") == title, f"{pos} {title}: title")
        if r["action"] == "Folder":
            child = keys_by_pos[pos]["folder"]
            check(child.lower() in r["command"].lower(), f"{pos} {title}: doc names the child page '{child}'")
            continue
        sm = a["Settings"]["settingsModel"]
        try:
            exp = expected_from_row(r)
        except (ValueError, IndexError) as ex:
            check(False, f"{pos} {title}: the Key table row can't be read: {ex}")
            continue
        bad = {f: (sm.get(f), v) for f, v in exp.items() if sm.get(f) != v}
        check(not bad, f"{pos} {title}: " + ", ".join(f"{f}={v!r}" for f, v in exp.items()) + (f"  MISMATCH {bad}" if bad else ""))

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
            no_title = lambda states: [{k: v for k, v in s.items() if k != "Title"} for s in states]  # noqa: E731
            check(not rest and no_title(t["States"]) == no_title(a["States"]),
                  f"{label}: other action fields and States (title aside) as the template" +
                  (f", with {shell}" if shell else "") + (f"  DIFFERENT {sorted(rest)}" if rest else ""))

    print("== phase1: BAT, PARK, AP against the Phase 1 export")
    for pos in ("1,1", "1,4", "2,1"):
        key = keys_by_pos[pos]
        src = p1main[key["template"][3:]]
        a = acts[key_of(pos)]
        named = set(key.get("set", {}))
        diff = {f for f in set(src["Settings"]["settingsModel"]) | set(a["Settings"]["settingsModel"])
                if src["Settings"]["settingsModel"].get(f) != a["Settings"]["settingsModel"].get(f)}
        check(diff == named, f"{pos} {key['title']}: settings differ only in the named fields {sorted(named) or 'none'} (found {sorted(diff) or 'none'})")
        same_rest = all(src[f] == a[f] for f in src if f not in ("ActionID", "Settings"))
        check(same_rest, f"{pos} {key['title']}: Name, Plugin, UUID, States, LinkedTitle equal the Phase 1 key")

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
