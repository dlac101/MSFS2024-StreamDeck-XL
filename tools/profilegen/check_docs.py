"""Check the repository's docs against each other and against the tracked files (no profile is read).

Usage, from the repo root (Python 3, standard library only; git on PATH):

    python tools/profilegen/check_docs.py

It reads the files git tracks (git ls-files), as they are in the working tree, and never changes a file.
check.py stays the check of each profile against its docs.

Checks:
  checklist   every checklist section that a tracked Markdown file names in quotes is a "## " heading of
              tests/manual-checklist.md, word for word (a quote may wrap across lines): 'checklist section
              "<name>"', '[tests/manual-checklist.md](...), section "<name>"' (a comma may follow "section",
              and the link may end in an #anchor)
              and the plural forms 'sections "<a>" and "<b>"' or 'sections "<a>", "<b>" and "<c>"'; also
              'section "<name>"' later in a paragraph that links the checklist ("[...](...manual-checklist.md)"),
              and inside tests/manual-checklist.md every 'section "<name>"' and its run lists 'Run "<a>"' or
              'Run "<a>", "<b>" and "<c>"'; after the singular "section" only the first quote is a section name
              ('section "<name>", "<step>"' names a step inside it); a quote after "checklist block", or after
              a "section" in a paragraph of another file that does not link the checklist, is not read
  readme      README.md's layout block (its ```text block) lists under "docs/" every tracked docs/*.md and
              no docs/*.md that git does not track (the files in docs/ itself, not in its subfolders)
  notes       the work folder's package.json "notes" name every committed profile (its file name without
              .streamDeckProfile) and every committed Lua script (its file name) under
              pilotsdeck/MSFS2024-XL/_Package, each as a whole name (not inside a longer name: "A32NX.lua" is
              not named by "XL24-A32NX.lua", nor a profile "MSFS2024 A32NX" by "MSFS2024 A32NX Pro" when that
              is a committed name too; build_package.py prints a NOTE for the same gap)
  inputevents every `B:<name>` in backticks in docs/aircraft-mappings.md under a "## " heading that starts with
              an aircraft of INPUT_EVENT_LISTS is a line of that aircraft's input event list in docs/reference/;
              a tracked list docs/reference/InputEvents-<X>.txt that INPUT_EVENT_LISTS does not name is the
              list of every other "## " heading that holds <X> as a word (a heading that holds the names of
              two such lists is a FAIL; a list that no heading gets is a note, not used); a code span may wrap
              across lines (not out of its block: a blank line, a list item, a table row or a "# " heading
              ends one; of the numbered items in a paragraph only a "1." or "1)" item, or one indented less
              than the text of the list item the paragraph is in, as CommonMark reads them), a fenced code
              block (its fence indented at most three columns past its container) is not read; the B: names of
              the other sections (no list in docs/reference/, such as the A32NX) are counted, not checked
  refs        no tracked file outside docs/chain/ cites an internal reference number: "LR" and digits as a
              word, with or without a "-C" or "-W" and digits after it; every file is read as bytes, the
              profiles and images too, a zip file (a profile) also entry by entry, uncompressed (a number in a
              stored entry that the raw bytes already give is reported once), and a file that starts with a UTF-16
              byte order mark also as UTF-16 text
Exit code 0 when everything passes, 1 on a FAIL (a file that can't be read too), 2 on a usage or environment
error (an argument, git not found or failing). A FAIL text that the console can't show is printed with
backslash escapes.
"""
import io
import json
import re
import subprocess
import sys
import zipfile
import zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

CHECKLIST = "tests/manual-checklist.md"
README = "README.md"
WORK = "pilotsdeck/MSFS2024-XL/_Package"  # the Profile Manager work folder (docs/package.md)
MAPPINGS_DOC = "docs/aircraft-mappings.md"
# The aircraft whose input event list is in docs/reference/ (one name per line, "B:<name>"), by the start of their
# "## " heading in docs/aircraft-mappings.md: the lists docs/roadmap.md A.5 names. A later list
# docs/reference/InputEvents-<X>.txt (the same file name form) is tied by <X> in the headings (LIST_FILE)
INPUT_EVENT_LISTS = {
    "Cessna 172 Skyhawk G1000": "docs/reference/InputEvents-C172-G1000.txt",
    "Cirrus Vision SF50": "docs/reference/InputEvents-SF50.txt",
}
LIST_FILE = re.compile(r"docs/reference/InputEvents-([^/]+)\.txt")
OWN_FOLDER = "docs/chain/"  # the project's working notes, outside the published docs (docs/roadmap.md section D)
# A checklist section quote: the trigger, then one quote (singular) or a list of quotes (plural), a comma allowed
# after "section(s)"; \s+ lets a quote or the words before it wrap across lines
QUOTES = r'("[^"]+"(?:\s*(?:,|,?\s+and)\s+"[^"]+")*)'
SECTION_QUOTE = re.compile(r'(?:\bchecklist|manual-checklist\.md(?:#[^)\s]*)?\)),?\s+(sections?),?\s+' + QUOTES)
# "section" without "checklist" before it: read in a paragraph that links the checklist (after the link) and
# inside the checklist itself; "Run" lists: inside the checklist only
SECTION_WORD = re.compile(r'\b(sections?),?\s+' + QUOTES)
RUN_LIST = re.compile(r'\b(Run)\s+' + QUOTES)
CHECKLIST_LINK = re.compile(r"\]\([^)\s]*manual-checklist\.md(?:#[^)\s]*)?\)")  # an #anchor may follow
REF_NUMBER = re.compile(rb"\bLR[0-9]+(?:-[CW][0-9]+)?\b")
REF_NUMBER_TEXT = re.compile(REF_NUMBER.pattern.decode("ascii"))
UTF16_BOMS = (b"\xff\xfe", b"\xfe\xff")
NEWLINE, NEWLINE_BYTE = "\n", b"\n"
B_NAME = re.compile(r"(?<![A-Za-z0-9_:])B:[A-Za-z0-9_]+")
# a run of backticks up to the next run of the same length; a run with no such end (a ``` line that is no
# fence) is text
CODE_SPAN = re.compile(r"(?<!`)(`+)(?!`)(.*?)(?<!`)\1(?!`)", re.S)

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


LIST_ITEM = re.compile(r"(\s*)(?:[-*+]|([0-9]+)[.)]) (?: {1,3}(?=\S))?")  # up to its text, one to four spaces on
HEADING = re.compile(r"\s*#{1,6}(?:[ \t]|$)")
# a ``` line with another backtick is inline code, no fence; indented four or more columns past its container
# (the document, or the list item it is in), it is indented code, no fence (CommonMark allows 0 to 3)
FENCE = re.compile(r"([ \t]*)(`{3,}(?!.*`)|~{3,})")


def block_start(line, col):
    """True if a line that goes on from a paragraph starts a new block: a table row, a "# " heading, a bullet
    item, a "1." or "1)" item, or another numbered item indented less than col, the content column of the list
    item the paragraph is in (0 outside a list). CommonMark lets no other numbered line, and no "#" without a
    space after it, interrupt a paragraph."""
    if line.lstrip().startswith("|") or HEADING.match(line):
        return True
    m = LIST_ITEM.match(line)
    if not m:
        return False
    return m.group(2) is None or int(m.group(2)) == 1 or len(m.group(1).expandtabs(4)) < col


def paragraphs(text):
    """[(offset, text)] of the Markdown blocks: a blank line ends one, and a list item, a table row or a heading
    starts a new one (block_start; a code span or a quote that wraps stays inside its block); a fenced code block
    (``` or ~~~) ends one and is in none (its lines are code, not code spans)."""
    # cols: the content columns of the list items the lines are in, outermost first (a wrapped line may be
    # indented less); inner: those a new block at this line's indent stays in; single: the last line was a
    # heading or a table row, which any list item ends
    out, start, pos, fence, cols, single = [], None, 0, None, [], False
    for line in text.split("\n"):
        indent = len(line[:len(line) - len(line.lstrip())].expandtabs(4))
        inner = cols if fence is not None else [c for c in cols if c <= indent]
        f = FENCE.match(line)
        if f and indent > (inner[-1] if inner else 0) + 3:
            f = None
        if fence is not None or f:
            if start is not None:
                out.append((start, text[start:pos - 1]))
                start = None
            if fence is None:
                fence, cols = f.group(2), inner
            elif f and f.group(2)[0] == fence[0] and len(f.group(2)) >= len(fence) and not line[f.end():].strip():
                fence = None
        elif not line.strip():
            if start is not None:
                out.append((start, text[start:pos - 1]))
            start = None
        else:
            m = LIST_ITEM.match(line)
            if start is None or (single and m) or block_start(line, cols[-1] if cols else 0):
                if start is not None:
                    out.append((start, text[start:pos - 1]))
                start, cols = pos, inner + ([len(m.group(0).expandtabs(4))] if m else [])
            elif single:  # no paragraph to go on from: a line indented less than its list item ends the item
                cols = inner
            single = line.lstrip().startswith("|") or HEADING.match(line) is not None
        pos += len(line) + 1
    if start is not None:
        out.append((start, text[start:pos - 1]))
    return out


def section_quotes(f, body):
    """[(form, offset, quote list text)] of the checklist section quotes in one file, each quote list once."""
    found = {}
    for m in SECTION_QUOTE.finditer(body):
        found[m.start(2)] = (m.group(1), m.start(), m.group(2))
    if f == CHECKLIST:
        for rx in (SECTION_WORD, RUN_LIST):
            for m in rx.finditer(body):
                found.setdefault(m.start(2), (m.group(1), m.start(), m.group(2)))
    else:
        for start, para in paragraphs(body):
            link = CHECKLIST_LINK.search(para)
            if link:
                for m in SECTION_WORD.finditer(para, link.end()):
                    found.setdefault(start + m.start(2), (m.group(1), start + m.start(), m.group(2)))
    return [found[k] for k in sorted(found)]


def check_checklist(files):
    md = [f for f in files if f.endswith(".md") and not f.startswith(OWN_FOLDER)]
    text = read_text(CHECKLIST)
    if text is None:
        return
    heads = {one_line(x[3:]) for x in text.splitlines() if x.startswith("## ")}
    quotes, missing, forms = 0, [], {"section": 0, "sections": 0, "Run": 0}
    for f in md:
        body = read_text(f)
        if body is None:
            continue
        for form, start, quoted in section_quotes(f, body):
            names = re.findall(r'"([^"]+)"', quoted)
            if form == "section":
                names = names[:1]
            forms[form] += 1
            line = body[:start].count("\n") + 1
            for name in names:
                quotes += 1
                if one_line(name) not in heads:
                    missing.append(f"{f}:{line} {one_line(name)!r}")
    check(not missing, f"{quotes} checklist section names in quotes ({forms['section']} 'section', "
          f"{forms['sections']} 'sections' lists, {forms['Run']} 'Run' lists, in {len(md)} tracked .md files) are "
          f"'## ' headings of {CHECKLIST} ({len(heads)} headings)" +
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


WHOLE_END = r"(?![A-Za-z0-9_-])(?!\.[A-Za-z0-9_-])"


def names_whole(label, text, labels=()):
    """True if text names label as a whole name: no letter, digit, "_", "-" or "." right before it, and no
    letter, digit, "_" or "-" right after it, nor a "." with one of those after it (a full stop may follow); a
    place where a longer name of labels that starts with label is named ("MSFS2024 A32NX Pro" for
    "MSFS2024 A32NX") does not count."""
    longer = [re.compile(re.escape(x) + WHOLE_END) for x in labels if len(x) > len(label) and x.startswith(label)]
    for m in re.finditer(r"(?<![A-Za-z0-9_.-])" + re.escape(label) + WHOLE_END, text):
        if not any(x.match(text, m.start()) for x in longer):
            return True
    return False


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
    absent = [x for x in labels if not names_whole(x, notes, labels)]
    check(not absent, f"{WORK}/package.json notes name the {len(labels)} committed profiles and Lua scripts" +
          (f"  NOT NAMED {absent}" if absent else ""))


def check_inputevents(files):
    text = read_text(MAPPINGS_DOC)
    if text is None:
        return
    lines = text.split("\n")
    headings = [(n, line[3:].strip()) for n, line in enumerate(lines, 1) if line.startswith("## ")]
    # a list INPUT_EVENT_LISTS does not name: tied by its file name's <X> to the headings that hold it as a word
    by_name = {}
    for f in files:
        m = LIST_FILE.fullmatch(f)
        if m and f not in INPUT_EVENT_LISTS.values():
            word = re.compile(r"(?<![A-Za-z0-9_-])" + re.escape(m.group(1)) + r"(?![A-Za-z0-9_-])")
            by_name[m.group(1)] = (f, word)
    # each heading's aircraft: the INPUT_EVENT_LISTS one it starts with, else the one later list it names; a
    # heading that names two later lists is a FAIL (TWO LISTS), and a list no heading gets is not used (note)
    tied, of_heading, twice = dict(INPUT_EVENT_LISTS), {}, []
    for n, h in headings:
        a = next((a for a in INPUT_EVENT_LISTS if h.startswith(a)), None)
        if a is None:
            named = [x for x, (_, word) in by_name.items() if word.search(h)]
            if len(named) > 1:
                twice.append(f"line {n}: {h} {[by_name[x][0] for x in named]}")
            elif named:
                a = named[0]
                tied[a] = by_name[a][0]
        of_heading[n] = a
    lists = {}
    for aircraft, rel in tied.items():
        body = read_text(rel)
        if body is not None:
            lists[aircraft] = {x.strip() for x in body.splitlines() if x.strip()}
    untied = [f for x, (f, _) in by_name.items() if x not in tied]
    if untied:
        print(f"  note {untied}: no {MAPPINGS_DOC} heading is tied to these lists (INPUT_EVENT_LISTS, or the "
              "list's name in a heading that starts with no aircraft of INPUT_EVENT_LISTS), so they are not used")

    counts, missing = {}, []
    hi = 0
    for start, para in paragraphs(text):
        first = text.count("\n", 0, start) + 1
        for m in CODE_SPAN.finditer(para):
            for b in B_NAME.finditer(m.group(2)):
                n = first + para.count("\n", 0, m.start(2) + b.start())
                while hi < len(headings) and headings[hi][0] <= n:
                    hi += 1
                heading = headings[hi - 1][1] if hi else None
                aircraft = of_heading[headings[hi - 1][0]] if hi else None
                name = b.group()
                c = counts.setdefault(aircraft or heading or "(before the first heading)", [0, set()])
                c[0] += 1
                c[1].add(name)
                if aircraft in lists and name not in lists[aircraft]:
                    missing.append(f"line {n}: {name} ({aircraft})")
    for aircraft in tied:
        if aircraft in lists:
            n, names = counts.get(aircraft, [0, set()])
            print(f"  {aircraft}: {n} B: names ({len(names)} distinct), list {tied[aircraft]} "
                  f"({len(lists[aircraft])} lines)")
    for where, (n, names) in counts.items():
        if where not in tied:
            print(f"  {where}: {n} B: names ({len(names)} distinct), no input event list in docs/reference/: "
                  "not checked")
    check(not missing and not twice, f"every B: name in {MAPPINGS_DOC} under an aircraft with an input event "
          "list is in that list" +
          (f"  NOT IN THE LIST {missing}" if missing else "") +
          (f"  TWO LISTS {twice} (a heading may name one list only)" if twice else ""))


def ref_hits(where, data):
    """The reference numbers in one file's bytes, and in its UTF-16 text if it starts with a byte order mark."""
    hits = []
    for m in REF_NUMBER.finditer(data):
        hits.append(f"{where}:{data.count(NEWLINE_BYTE, 0, m.start()) + 1} {m.group().decode('ascii')}")
    if data[:2] in UTF16_BOMS:
        text = data.decode("utf-16")
        for m in REF_NUMBER_TEXT.finditer(text):
            hits.append(f"{where}:{text.count(NEWLINE, 0, m.start()) + 1} {m.group()} (UTF-16)")
    return hits


def check_refs(files):
    hits, n, entries, utf16 = [], 0, 0, 0
    for f in files:
        if f.startswith(OWN_FOLDER):
            continue
        try:
            data = (ROOT / f).read_bytes()
            hits += ref_hits(f, data)
            utf16 += data[:2] in UTF16_BOMS
            if data[:4] == b"PK\x03\x04":
                raw = set(REF_NUMBER.findall(data))
                with zipfile.ZipFile(io.BytesIO(data)) as z:
                    for info in z.infolist():
                        entry = z.read(info)
                        entries += 1
                        utf16 += entry[:2] in UTF16_BOMS
                        found = ref_hits(f"{f}:{info.filename}", entry)
                        if info.compress_type == zipfile.ZIP_STORED:  # the raw read gave its plain numbers, all but
                            # one whose neighbors in the raw bytes (the entry's file name, say) make it no word
                            found = [h for h in found if h.endswith(" (UTF-16)") or h.split()[-1].encode() not in raw]
                        hits += [h + " (zip entry)" for h in found]
        except (OSError, ValueError, RuntimeError, zipfile.BadZipFile, zipfile.LargeZipFile, zlib.error) as ex:
            check(False, f"cannot read {f}: {type(ex).__name__}: {ex}")
            continue
        n += 1
    check(not hits, f"{n} tracked files outside {OWN_FOLDER} ({entries} zip entries read uncompressed, {utf16} UTF-16 "
          "texts) cite no internal reference number" +
          (f"  FOUND {hits}" if hits else ""))


def main():
    for stream in (sys.stdout, sys.stderr):  # a text the console can't show: escapes, not a traceback
        try:
            stream.reconfigure(errors="backslashreplace")
        except (AttributeError, ValueError):
            pass
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
