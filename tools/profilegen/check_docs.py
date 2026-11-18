"""Check the repository's docs against each other and against the tracked files (no profile is read).

Usage, from the repo root (Python 3, standard library only; git on PATH):

    python tools/profilegen/check_docs.py

It reads the files git tracks (git ls-files), as they are in the working tree, and never changes a file.
check.py stays the check of each profile against its docs.

Checks:
  checklist   every checklist section that a tracked Markdown file names in quotes is a "## " heading of
              tests/manual-checklist.md, word for word (a quote may wrap across lines): 'checklist section
              "<name>"', '[tests/manual-checklist.md](...), section "<name>"' (a comma may follow "section")
              and the plural forms 'sections "<a>" and "<b>"' or 'sections "<a>", "<b>" and "<c>"'; after
              the singular "section" only the first quote is a section name ('section "<name>", "<step>"'
              names a step inside it); a quote after "checklist block", or after a "section" that follows
              neither "checklist" nor the checklist link, is not read
  readme      README.md's layout block (its ```text block) lists under "docs/" every tracked docs/*.md and
              no docs/*.md that git does not track (the files in docs/ itself, not in its subfolders)
  notes       the work folder's package.json "notes" name every committed profile (its file name without
              .streamDeckProfile) and every committed Lua script (its file name) under
              pilotsdeck/MSFS2024-XL/_Package (build_package.py prints a NOTE for the same gap)
  inputevents every `B:<name>` in backticks in docs/aircraft-mappings.md under a "## " heading that starts with
              an aircraft of INPUT_EVENT_LISTS is a line of that aircraft's input event list in docs/reference/;
              the B: names of the other sections (no list in docs/reference/, such as the A32NX) are counted,
              not checked
  refs        no tracked file outside docs/chain/ cites an internal reference number: "LR" and digits as a
              word, with or without a "-C" or "-W" and digits after it; every file is read as bytes, the
              profiles and images too
Exit code 0 when everything passes, 1 on a FAIL (a file that can't be read too), 2 on a usage or environment
error (an argument, git not found or failing).
"""
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

CHECKLIST = "tests/manual-checklist.md"
README = "README.md"
WORK = "pilotsdeck/MSFS2024-XL/_Package"  # the Profile Manager work folder (docs/package.md)
MAPPINGS_DOC = "docs/aircraft-mappings.md"
# The aircraft whose input event list is in docs/reference/ (one name per line, "B:<name>"), by the start of their
# "## " heading in docs/aircraft-mappings.md: the lists docs/roadmap.md A.5 names
INPUT_EVENT_LISTS = {
    "Cessna 172 Skyhawk G1000": "docs/reference/InputEvents-C172-G1000.txt",
    "Cirrus Vision SF50": "docs/reference/InputEvents-SF50.txt",
}
OWN_FOLDER = "docs/chain/"  # the project's working notes, outside the published docs (docs/roadmap.md section D)
# A checklist section quote: the trigger, then one quote (singular) or a list of quotes (plural), a comma allowed
# after "section(s)"; \s+ lets a quote or the words before it wrap across lines
SECTION_QUOTE = re.compile(r'(?:\bchecklist|manual-checklist\.md\)),?\s+(sections?),?\s+'
                           r'("[^"]+"(?:\s*(?:,|,?\s+and)\s+"[^"]+")*)')
REF_NUMBER = re.compile(rb"\bLR[0-9]+(?:-[CW][0-9]+)?\b")
B_NAME = re.compile(r"(?<![A-Za-z0-9_:])B:[A-Za-z0-9_]+")

failures = []


def check(cond, msg):
    print(("  ok   " if cond else "  FAIL ") + msg)
    if not cond:
        failures.append(msg)
    return cond


def finish():
    """Print the RESULT line; return the exit code (0 PASS, 1 FAIL)."""
    print()
    print("RESULT:", "PASS" if not failures else f"FAIL ({len(failures)})")
    return 0 if not failures else 1


class EnvError(Exception):
    """git not found or failing (exit 2)."""


def tracked(root):
    """The paths git tracks in root, in git's order."""
    try:
        r = subprocess.run(["git", "--no-optional-locks", "-C", str(root), "ls-files", "-z"], capture_output=True)
    except OSError as ex:
        raise EnvError(f"cannot run git: {ex}")
    if r.returncode != 0:
        raise EnvError(f"git ls-files failed: {r.stderr.decode('utf-8', 'replace').strip()}")
    return [p for p in r.stdout.decode("utf-8", "surrogateescape").split("\0") if p]


def read_text(rel):
    """A file's text, or None after a FAIL naming it."""
    try:
        return (ROOT / rel).read_text(encoding="utf-8")
    except (OSError, ValueError) as ex:
        check(False, f"cannot read {rel}: {type(ex).__name__}: {ex}")
        return None


def one_line(text):
    return re.sub(r"\s+", " ", text).strip()


def check_checklist(files):
    md = [f for f in files if f.endswith(".md") and not f.startswith(OWN_FOLDER)]
    text = read_text(CHECKLIST)
    if text is None:
        return
    heads = {one_line(x[3:]) for x in text.splitlines() if x.startswith("## ")}
    quotes, missing, forms = 0, [], {"section": 0, "sections": 0}
    for f in md:
        body = read_text(f)
        if body is None:
            continue
        for m in SECTION_QUOTE.finditer(body):
            names = re.findall(r'"([^"]+)"', m.group(2))
            if m.group(1) == "section":
                names = names[:1]
            forms[m.group(1)] += 1
            line = body[:m.start()].count("\n") + 1
            for name in names:
                quotes += 1
                if one_line(name) not in heads:
                    missing.append(f"{f}:{line} {one_line(name)!r}")
    check(not missing, f"{quotes} checklist section names in quotes ({forms['section']} 'section', "
          f"{forms['sections']} 'sections' lists, in {len(md)} tracked .md files) are '## ' headings of "
          f"{CHECKLIST} ({len(heads)} headings)" +
          (f"  NO SUCH HEADING {missing}" if missing else ""))


def check_readme(files):
    text = read_text(README)
    if text is None:
        return
    docs = sorted(f[len("docs/"):] for f in files if re.fullmatch(r"docs/[^/]+\.md", f))
    block = re.search(r"^```text\n(.*?)^```", text.replace("\r\n", "\n"), re.M | re.S)
    listed, inside = [], False
    for line in (block.group(1).splitlines() if block else []):
        if not line.startswith(" "):
            inside = line.strip() == "docs/"
        elif inside and re.match(r"  \S", line):
            listed.append(line.split()[0])
    named = sorted(x for x in listed if x.endswith(".md"))
    if not check(block is not None, f"{README} has a layout block (```text)"):
        return
    absent = [x for x in docs if x not in named]
    extra = [x for x in named if x not in docs]
    twice = sorted({x for x in named if named.count(x) > 1})
    check(not absent and not extra and not twice,
          f"{README}'s layout block lists the {len(docs)} tracked docs/*.md under 'docs/' ({len(named)} listed)" +
          (f"  NOT LISTED {absent}" if absent else "") + (f"  NOT TRACKED {extra}" if extra else "") +
          (f"  TWICE {twice}" if twice else ""))


def check_notes(files):
    text = read_text(f"{WORK}/package.json")
    if text is None:
        return
    try:
        notes = json.loads(text)["notes"]
        if not isinstance(notes, str):
            raise TypeError("notes is not a string")
    except (ValueError, KeyError, TypeError) as ex:
        check(False, f"cannot read the notes of {WORK}/package.json: {type(ex).__name__}: {ex}")
        return
    labels = []
    for f in files:
        if f.startswith(WORK + "/Profiles/") and f.endswith(".streamDeckProfile"):
            labels.append(f.split("/")[-1][: -len(".streamDeckProfile")])
        elif f.startswith(WORK + "/Scripts/") and f.endswith(".lua"):
            labels.append(f.split("/")[-1])
    absent = [x for x in labels if x not in notes]
    check(not absent, f"{WORK}/package.json notes name the {len(labels)} committed profiles and Lua scripts" +
          (f"  NOT NAMED {absent}" if absent else ""))


def check_inputevents(files):
    text = read_text(MAPPINGS_DOC)
    if text is None:
        return
    lists = {}
    for aircraft, rel in INPUT_EVENT_LISTS.items():
        body = read_text(rel)
        if body is not None:
            lists[aircraft] = {x.strip() for x in body.splitlines() if x.strip()}
    untied = [f for f in files if re.fullmatch(r"docs/reference/InputEvents-[^/]+\.txt", f)
              and f not in INPUT_EVENT_LISTS.values()]
    if untied:
        print(f"  note {untied}: no {MAPPINGS_DOC} heading is tied to these lists (INPUT_EVENT_LISTS), "
              "so they are not used")
    heading, counts, missing = None, {}, []
    for n, line in enumerate(text.splitlines(), 1):
        if line.startswith("## "):
            heading = line[3:].strip()
        for tick in re.findall(r"`([^`]*)`", line):
            for name in B_NAME.findall(tick):
                aircraft = next((a for a in INPUT_EVENT_LISTS if heading and heading.startswith(a)), None)
                c = counts.setdefault(aircraft or heading or "(before the first heading)", [0, set()])
                c[0] += 1
                c[1].add(name)
                if aircraft in lists and name not in lists[aircraft]:
                    missing.append(f"line {n}: {name} ({aircraft})")
    for aircraft in INPUT_EVENT_LISTS:
        if aircraft in lists:
            n, names = counts.get(aircraft, [0, set()])
            print(f"  {aircraft}: {n} B: names ({len(names)} distinct), list {INPUT_EVENT_LISTS[aircraft]} "
                  f"({len(lists[aircraft])} lines)")
    for where, (n, names) in counts.items():
        if where not in INPUT_EVENT_LISTS:
            print(f"  {where}: {n} B: names ({len(names)} distinct), no input event list in docs/reference/: "
                  "not checked")
    check(not missing, f"every B: name in {MAPPINGS_DOC} under an aircraft with an input event list is in that "
          "list" +
          (f"  NOT IN THE LIST {missing}" if missing else ""))


def check_refs(files):
    hits, n = [], 0
    for f in files:
        if f.startswith(OWN_FOLDER):
            continue
        try:
            data = (ROOT / f).read_bytes()
        except OSError as ex:
            check(False, f"cannot read {f}: {type(ex).__name__}: {ex}")
            continue
        n += 1
        for m in REF_NUMBER.finditer(data):
            line = data.count(b"\n", 0, m.start()) + 1
            hits.append(f"{f}:{line} {m.group().decode('ascii')}")
    check(not hits, f"{n} tracked files outside {OWN_FOLDER} cite no internal reference number" +
          (f"  FOUND {hits}" if hits else ""))


def main():
    if sys.argv[1:]:
        print("usage: check_docs.py (no arguments; run it from anywhere, it checks the repository it is in)")
        return 2
    try:
        files = tracked(ROOT)
    except EnvError as ex:
        print(f"ERROR: {ex}", file=sys.stderr)
        return 2
    print(f"== checklist: the checklist sections the docs name in quotes are headings of {CHECKLIST}")
    check_checklist(files)
    print(f"== readme: {README}'s layout block lists every doc in docs/")
    check_readme(files)
    print(f"== notes: the package.json notes name every committed profile and script in {WORK}")
    check_notes(files)
    print(f"== inputevents: the B: input events in {MAPPINGS_DOC} are in their aircraft's list in docs/reference/")
    check_inputevents(files)
    print(f"== refs: no tracked file outside {OWN_FOLDER} cites an internal reference number")
    check_refs(files)
    return finish()


if __name__ == "__main__":
    sys.exit(main())
