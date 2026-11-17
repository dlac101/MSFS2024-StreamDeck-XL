"""Build the PilotsDeck Profile Manager package for this repository.

Usage: python tools/package/build_package.py [--out-dir DIR]

What it builds: `MSFS2024-XL v<versionpackage>.ppp` (default folder
pilotsdeck/MSFS2024-XL/_Releases/, which git ignores), a plain zip archive that
PilotsDeck's Profile Manager installs. It packs the files COMMITTED at HEAD under
the work folder pilotsdeck/MSFS2024-XL/_Package/, read from git objects, never
from the working tree:
  - package.json first, byte for byte;
  - Profiles/*.streamDeckProfile byte for byte;
  - Scripts/*.lua, Scripts/global/*.lua, Scripts/image/*.lua with LF turned into
    CRLF (the line endings .gitattributes gives them on disk);
  - Images/*.png and Images/<folder>/*.png byte for byte;
  - a directory entry for each allowed folder that holds only .gitkeep files
    (.gitkeep itself is never packed).
Every entry is stored (no compression) with the time 1980-01-01 00:00, so two
builds of the same commit give the same bytes.

What it refuses (exit 1, nothing written), by rule:
  R1  uncommitted changes or untracked files in the work folder
  R2  a tree entry that is not a regular file (symlink, submodule)
  R3  a path with CLAUDE.md, .local, _Releases or .., a backslash, or a
      character outside printable ASCII
  R4  a file outside the package allowlist above
  R5  a missing or invalid package.json (BOM, not UTF-8, not the nine fields,
      bad versions, removefiles naming a file the package installs)
  R6  a profile that is not a readable zip, has no single .sdProfile manifest,
      whose Name differs from its file name, two profiles with one Name, or a
      profile with an embedded image
  R7  a committed Lua file holding a CR or NUL byte
  R8  no profile to pack
  R9  an existing output file of the same version with different bytes
      (bump versionpackage); same bytes: prints "unchanged". It compares only
      with the file in the output folder: a build into another folder, or
      after that file is deleted, is not refused
  R10 --out-dir inside the work folder
Exit 2: usage or environment error (unknown option, not this repo, git fails,
the output folder cannot be read or written).
"""

import argparse
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import zipfile
import zlib
from pathlib import Path

WORK = "pilotsdeck/MSFS2024-XL/_Package"
PACKAGE_NAME = "MSFS2024-XL"  # the work folder's name, as Create Package names its output
RELEASES = "pilotsdeck/MSFS2024-XL/_Releases"
FIELDS = ["packageformat", "title", "versionpackage", "aircraft", "author",
          "url", "notes", "versionplugin", "removefiles"]
ZIP_TIME = (1980, 1, 1, 0, 0, 0)

ALLOWED_FILES = [
    re.compile(r"package\.json"),
    re.compile(r"Profiles/[^/]+\.streamDeckProfile"),
    re.compile(r"Images/[^/]+\.png"),
    re.compile(r"Images/[^/]+/[^/]+\.png"),
    re.compile(r"Scripts/[^/]+\.lua"),
    re.compile(r"Scripts/(global|image)/[^/]+\.lua"),
]
GITKEEP = re.compile(r"(?:[^/]+/)*\.gitkeep")
ALLOWED_DIRS = re.compile(r"Profiles|Images|Images/[^/]+|Scripts|Scripts/(global|image)")
IMAGE_EXTS = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp")
IMAGE_MARKS = (b"\x89PNG\r\n\x1a\n", b"data:image")


class Refused(Exception):
    """A package rule failed (exit 1)."""


class EnvError(Exception):
    """A usage or environment error (exit 2)."""


def git(root, *cmd):
    """Run a read-only git command in root and return its stdout bytes."""
    try:
        res = subprocess.run(["git", "--no-optional-locks", "-C", str(root), *cmd],
                             capture_output=True)
    except OSError as exc:
        raise EnvError(f"cannot run git: {exc}")
    if res.returncode != 0:
        msg = res.stderr.decode("utf-8", "replace").strip()
        raise EnvError(f"git {' '.join(cmd)} failed: {msg}")
    return res.stdout


def same_path(a, b):
    return os.path.normcase(os.path.abspath(a)) == os.path.normcase(os.path.abspath(b))


def is_inside(path, folder):
    path = os.path.normcase(os.path.abspath(path))
    folder = os.path.normcase(os.path.abspath(folder))
    return path == folder or path.startswith(folder.rstrip("\\/") + os.sep)


def find_root():
    root = Path(__file__).resolve().parents[2]
    top = git(root, "rev-parse", "--show-toplevel").decode("utf-8").strip()
    if not same_path(Path(top).resolve(), root):
        raise EnvError(f"the script is not in its repository: {root} (git top {top})")
    return root


def head_commit(root):
    sha = git(root, "rev-parse", "--verify", "HEAD^{commit}").decode().strip()
    tree = git(root, "rev-parse", "--verify", sha + "^{tree}").decode().strip()
    return sha, tree


def check_clean(root):
    """R1: the work folder must match HEAD (nothing modified, staged, deleted or untracked)."""
    out = git(root, "status", "--porcelain=v1", "-z", "--untracked-files=all", "--", WORK + "/")
    items = iter(x for x in out.decode("utf-8", "surrogateescape").split("\0") if x)
    problems = []
    for item in items:
        status, path = item[:2], item[3:]
        if "R" in status or "C" in status:
            next(items, None)  # a rename or copy record carries its old path next
        problems.append(f"R1 {path}: not committed (git status '{status}'); commit it or undo it")
    return problems


def list_tree(root, sha):
    """Return [(mode, type, object id, path relative to the work folder)] for HEAD."""
    out = git(root, "ls-tree", "-r", "-z", "--full-tree", sha, "--", WORK + "/")
    entries = []
    for rec in out.decode("utf-8", "surrogateescape").split("\0"):
        if not rec:
            continue
        meta, path = rec.split("\t", 1)
        mode, kind, oid = meta.split(" ")
        entries.append((mode, kind, oid, path[len(WORK) + 1:]))
    return entries


def check_path(rel):
    """R3: forbidden names and characters."""
    if "\\" in rel or any(not (" " <= c <= "~") for c in rel):
        return f"R3 {rel}: backslash or character outside printable ASCII"
    for part in rel.split("/"):
        if part == ".." or part.lower() in ("claude.md", ".local", "_releases"):
            return f"R3 {rel}: forbidden path component '{part}'"
    return None


def check_package_json(data, installed):
    """R5: package.json must be the Profile Manager's nine fields with valid values."""
    if data.startswith(b"\xef\xbb\xbf"):
        return ["R5 package.json: starts with a BOM"]
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return ["R5 package.json: not UTF-8"]
    dupes = []

    def pairs(items):
        keys = [k for k, _ in items]
        dupes.extend(k for k in set(keys) if keys.count(k) > 1)
        return dict(items)

    try:
        doc = json.loads(text, object_pairs_hook=pairs)
    except ValueError as exc:
        return [f"R5 package.json: not valid JSON ({exc})"]
    if not isinstance(doc, dict):
        return ["R5 package.json: not a JSON object"]
    if dupes or sorted(doc) != sorted(FIELDS):
        return [f"R5 package.json: keys must be exactly {', '.join(FIELDS)}"
                f" (found {', '.join(doc)}{'; duplicates ' + ', '.join(dupes) if dupes else ''})"]
    p = []
    if type(doc["packageformat"]) is not int or doc["packageformat"] != 1:
        p.append("R5 package.json: packageformat must be the number 1")
    for key in ("title", "versionpackage", "aircraft", "author", "url", "notes", "versionplugin"):
        if not isinstance(doc[key], str):
            p.append(f"R5 package.json: {key} must be a string")
    if p:
        return p
    if not doc["title"].strip():
        p.append("R5 package.json: title is empty")
    if not re.fullmatch(r"[0-9]+\.[0-9]+", doc["versionpackage"]):
        p.append(f"R5 package.json: versionpackage '{doc['versionpackage']}' is not MAJOR.MINOR")
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", doc["versionplugin"]):
        p.append(f"R5 package.json: versionplugin '{doc['versionplugin']}' is not X.Y.Z")
    remove = doc["removefiles"]
    if not isinstance(remove, list):
        return p + ["R5 package.json: removefiles must be a list"]
    lower = {name.lower() for name in installed}
    for item in remove:
        if not isinstance(item, str) or not re.fullmatch(r"(Scripts|Images)/[^\\]+", item) \
                or ".." in item:
            p.append(f"R5 package.json: removefiles entry {item!r} is not Scripts/... or Images/...")
        elif item.lower() in lower:
            p.append(f"R5 package.json: removefiles entry {item!r} names a file this package "
                     "installs (the Profile Manager deletes it after the copy)")
    return p


def profile_name(rel, data):
    """R6: return (profile Name, problems) for one .streamDeckProfile blob."""
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as zf:
            inner = {info.filename: zf.read(info) for info in zf.infolist()}
    except (zipfile.BadZipFile, zipfile.LargeZipFile, OSError, RuntimeError, ValueError,
            zlib.error) as exc:
        return None, [f"R6 {rel}: not a readable zip ({exc})"]
    p = []
    for name, body in inner.items():
        if name.lower().endswith(IMAGE_EXTS) or any(m in body for m in IMAGE_MARKS):
            p.append(f"R6 {rel}: embeds an image ({name})")
    if any(m in data for m in IMAGE_MARKS):
        p.append(f"R6 {rel}: embeds an image (raw bytes)")
    manifests = [n for n in inner
                 if ".sdprofile/manifest.json" in n.replace("\\", "/").lower()]
    if len(manifests) != 1:
        return None, p + [f"R6 {rel}: needs exactly one .sdProfile/manifest.json, "
                          f"found {len(manifests)}"]
    try:
        name = json.loads(inner[manifests[0]].decode("utf-8-sig")).get("Name")
    except (ValueError, AttributeError) as exc:
        return None, p + [f"R6 {rel}: unreadable manifest {manifests[0]} ({exc})"]
    stem = rel.split("/")[-1][: -len(".streamDeckProfile")]
    if name != stem:
        p.append(f"R6 {rel}: profile Name {name!r} differs from the file name {stem!r}")
    return name, p


def collect(root, sha):
    """Read and check every committed file under the work folder; return the entries to pack."""
    problems, files, keep_dirs = [], {}, set()
    for mode, kind, oid, rel in list_tree(root, sha):
        bad = check_path(rel)
        if mode not in ("100644", "100755") or kind != "blob":
            problems.append(f"R2 {rel}: not a regular file (mode {mode}, {kind})")
        elif bad:
            problems.append(bad)
        elif GITKEEP.fullmatch(rel):
            folder = rel.rpartition("/")[0]
            if ALLOWED_DIRS.fullmatch(folder):
                keep_dirs.add(folder)
        elif not any(rx.fullmatch(rel) for rx in ALLOWED_FILES):
            problems.append(f"R4 {rel}: not on the package allowlist (package.json, "
                            "Profiles/*.streamDeckProfile, Images/[folder/]*.png, "
                            "Scripts/[global/|image/]*.lua)")
        else:
            files[rel] = (oid, git(root, "cat-file", "blob", oid))
    if problems:
        return problems, None
    if "package.json" not in files:
        return ["R5 package.json: missing"], None

    entries, names = {}, {}
    for rel, (oid, blob) in files.items():
        data, crlf = blob, False
        if rel.endswith(".lua"):
            if b"\r" in blob or b"\0" in blob:
                problems.append(f"R7 {rel}: the committed file holds a CR or NUL byte")
                continue
            data, crlf = blob.replace(b"\n", b"\r\n"), True
        elif rel.endswith(".streamDeckProfile"):
            name, p = profile_name(rel, blob)
            problems += p
            if name is not None and name in names:
                problems.append(f"R6 {rel}: same profile Name {name!r} as {names[name]}")
            elif name is not None:
                names[name] = rel
        entries[rel] = (oid, data, crlf)
    installed = [r for r in entries if r.startswith(("Scripts/", "Images/"))]
    problems += check_package_json(files["package.json"][1], installed)
    if not any(r.endswith(".streamDeckProfile") for r in files):
        problems.append(f"R8 {WORK}/Profiles: no profile to pack")
    packed = list(entries)  # files only, so the result does not depend on set order
    for folder in sorted(keep_dirs):
        if not any(r.startswith(folder + "/") for r in packed):
            entries[folder + "/"] = (None, b"", False)
    return problems, entries


def build_zip(entries):
    """Return the archive bytes: package.json first, then names in ordinal order."""
    order = ["package.json"] + sorted((n for n in entries if n != "package.json"),
                                      key=lambda n: n.encode("ascii"))
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", compression=zipfile.ZIP_STORED) as zf:
        for name in order:
            info = zipfile.ZipInfo(name, date_time=ZIP_TIME)
            info.compress_type = zipfile.ZIP_STORED
            zf.writestr(info, entries[name][1])
        # writestr fills in Unix permissions; these fields live only in the central
        # directory, which is written on close, so set them here (MS-DOS, no attributes).
        for info in zf.infolist():
            info.create_system = 0
            info.external_attr = 0x10 if info.filename.endswith("/") else 0
    return order, buf.getvalue()


def notes_lines(entries):
    """NOTE lines for packed profiles and scripts the package.json notes do not name."""
    notes = json.loads(entries["package.json"][1].decode("utf-8"))["notes"]
    out = []
    for rel in entries:
        if rel.endswith(".streamDeckProfile"):
            label = rel.split("/")[-1][: -len(".streamDeckProfile")]
        elif rel.endswith(".lua"):
            label = rel.split("/")[-1]
        else:
            continue
        if label not in notes:
            out.append(f"NOTE {rel}: '{label}' is not named in package.json notes")
    return out


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out-dir", help=f"output folder (default <repo>/{RELEASES}/)")
    opts = parser.parse_args(argv)  # an unknown option exits 2
    try:
        root = find_root()
        out_dir = Path(opts.out_dir).resolve() if opts.out_dir else root / RELEASES
        if is_inside(out_dir, root / WORK):
            raise Refused(f"R10 {out_dir}: the output folder is inside the work folder {WORK}")
        sha, tree = head_commit(root)
        problems = check_clean(root)
        if not problems:
            problems, entries = collect(root, sha)
        if problems:
            raise Refused("\n".join(problems))
        version = json.loads(entries["package.json"][1].decode("utf-8"))["versionpackage"]
        order, archive = build_zip(entries)
        target = out_dir / f"{PACKAGE_NAME} v{version}.ppp"
        if target.exists():
            if not target.is_file() or target.read_bytes() != archive:
                raise Refused(f"R9 {target}: exists with other bytes; bump versionpackage "
                              f"(now {version}) for new content")
    except (EnvError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    except Refused as exc:
        for line in str(exc).splitlines():
            print(f"REFUSED {line}", file=sys.stderr)
        return 1

    print(f"source HEAD {sha} tree {tree}")
    for name in order:
        oid, data, crlf = entries[name]
        if oid is None:
            print(f"-  0  {name}")
        else:
            digest = hashlib.sha256(data).hexdigest()
            print(f"{digest}  {len(data)}  {name}  blob {oid}{' crlf' if crlf else ''}")
    for line in notes_lines(entries):
        print(line)
    if target.exists():
        print(f"unchanged {target}")
    else:
        tmp = out_dir / f".{target.name}.tmp"
        try:
            out_dir.mkdir(parents=True, exist_ok=True)
            tmp.unlink(missing_ok=True)  # never write through a leftover file or link of this name
            tmp.write_bytes(archive)
            os.replace(tmp, target)
        except OSError as exc:
            print(f"ERROR: cannot write {target}: {exc}", file=sys.stderr)
            return 2
        finally:
            if tmp.exists():
                tmp.unlink()
    print(f"package {target}")
    print(f"sha256 {hashlib.sha256(archive).hexdigest()}")
    print(f"size {len(archive)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
