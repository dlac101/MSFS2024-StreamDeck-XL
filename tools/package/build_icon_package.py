"""Build the LOCAL icon package: a Profile Manager package for your own installs, with the icon images.

Usage: python tools/package/build_icon_package.py [--out-dir DIR]

PERSONAL USE ONLY: the package holds images from a personal-use icon pack (docs/icons.md, "Licence").
Keep it on this PC: never commit, upload, share or attach it to a release.

What it builds: `MSFS2024-XL-Icons v<versionpackage>-<HEAD sha, 7 hex>.ppp` (default folder .local/package/,
which git ignores), in the same archive format as build_package.py (stored entries, 1980-01-01 00:00,
package.json first, then ordinal order). It does not build the icon profiles: it needs a fresh local icon
build (python tools/profilegen/generate.py --icons <mapping>, docs/icons.md) for every icon mapping
committed at HEAD (tools/profilegen/icons-*.json), checks it, and packs:
  - package.json, made here (never written to the work folder): the committed one's fields, its title plus
    " (local icon build)", an empty url and notes naming every packed profile;
  - Profiles/<profile_name>.streamDeckProfile of each icon build, byte for byte from the mapping's out folder;
  - every committed profile except the ones an icon build copies (its data file's "output"), from git objects;
  - the committed Scripts/ (LF turned into CRLF) and Images/ files, as build_package.py packs them;
  - Images/<plugin_subfolder>/<file>.png of each icon build, byte for byte;
  - a directory entry for each allowed folder that holds only .gitkeep files and no packed file.

What it refuses (exit 1, nothing written), by rule:
  R1-R8 the rules of build_package.py on the work folder pilotsdeck/MSFS2024-XL/_Package/
  I1  uncommitted changes or untracked files under tools/profilegen/ or tools/package/
  I2  no icon mapping (tools/profilegen/icons-*.json) at HEAD
  I3  a mapping that check_icons.py's load_plan refuses
  I4  an icon build that is missing or out of date (check_icons.py's profile check fails, or the profile
      differs from a fresh generate.py --icons build); delete its out folder and rebuild
  I5  two mappings with the same profile_name, plugin_subfolder or out (or one out inside another), an icon
      profile Name equal to a committed profile Name, an icon image path equal to a committed Images/ path,
      a new entry name failing R3 or the package allowlist
  I6  an output folder not inside .local/, inside a mapping's out or the work folder, or a target file that
      git does not ignore
  I7  an existing package of the same name with other bytes (delete it or commit first); same bytes:
      prints "unchanged"
The icon profiles may embed folder/back key images; every other R6 problem refuses them.
Exit 2: usage or environment error (unknown option, not this repo, git fails, a folder cannot be read
or written).
"""

import sys

sys.dont_write_bytecode = True  # the imports below must not leave a __pycache__ folder in the repo

import argparse  # noqa: E402
import hashlib  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import re  # noqa: E402
import subprocess  # noqa: E402
import zipfile  # noqa: E402
import zlib  # noqa: E402
from pathlib import Path  # noqa: E402

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parent / "profilegen")]
import build_package as bp  # noqa: E402  (find_root, check_clean, collect, build_zip, rule checks)
import check_icons  # noqa: E402  (load_plan, check_profile)
import generate  # noqa: E402  (build)

PACKAGE_NAME = "MSFS2024-XL-Icons"
LOCAL = ".local"
DEFAULT_OUT = ".local/package"
INPUTS = ("tools/profilegen/", "tools/package/")
MAPPING_RE = re.compile(r"tools/profilegen/icons-[^/]+\.json")
EMBEDS = ": embeds an image ("
NOTICE = ('PERSONAL USE ONLY: this package holds images from a personal-use icon pack (docs/icons.md, '
          '"Licence"). Keep it on this PC: never commit, upload, share or attach it to a release.')


def rel_path(root, path):
    """Repo-relative path with '/' (the absolute path if it is outside the repo)."""
    try:
        return Path(path).resolve().relative_to(root).as_posix()
    except ValueError:
        return str(path)


def check_inputs(root):
    """I1: the generator, its data, templates, mappings and this tool must match HEAD."""
    out = bp.git(root, "status", "--porcelain=v1", "-z", "--untracked-files=all", "--", *INPUTS)
    items = iter(x for x in out.decode("utf-8", "surrogateescape").split("\0") if x)
    problems = []
    for item in items:
        status, path = item[:2], item[3:]
        if "R" in status or "C" in status:
            next(items, None)  # a rename or copy record carries its old path next
        problems.append(f"I1 {path}: not committed (git status '{status}'); commit it or undo it")
    return problems


def mappings(root, sha):
    """Every icon mapping committed at HEAD, sorted by path."""
    out = bp.git(root, "ls-tree", "-r", "-z", "--name-only", "--full-tree", sha, "--", "tools/profilegen/")
    names = out.decode("utf-8", "surrogateescape").split("\0")
    return sorted(n for n in names if MAPPING_RE.fullmatch(n))


def gitkeep_dirs(root, sha):
    """The allowed folders that hold a .gitkeep file at HEAD (as build_package.collect finds them)."""
    dirs = set()
    for _, _, _, rel in bp.list_tree(root, sha):
        if bp.GITKEEP.fullmatch(rel) and bp.ALLOWED_DIRS.fullmatch(rel.rpartition("/")[0]):
            dirs.add(rel.rpartition("/")[0])
    return dirs


def stale_reason(plan, out, data):
    """I4: None if the icon build in out is complete and fresh, else the first reason."""
    if data is None:
        return f"no {plan['profile_name']}.streamDeckProfile"
    try:
        errors, _ = check_icons.check_profile(plan, out)
        if errors:
            return errors[0]
        if generate.build(plan["data"], icons=plan)[1] != data:
            return "the icon profile differs from a fresh generate.py --icons build"
    except (ValueError, KeyError, EOFError, RuntimeError, zipfile.BadZipFile, zlib.error) as exc:
        return f"{type(exc).__name__}: {exc}"
    return None


def load_builds(root, sha, entries):
    """Check every icon mapping and its build; return (problems, builds)."""
    found = mappings(root, sha)
    if not found:
        return ["I2 no tools/profilegen/icons-*.json mapping"], []
    problems, builds = [], []
    for path in found:
        errors, plan = check_icons.load_plan(root / path)
        problems += [f"I3 {path}: {e}" for e in errors]
        if plan is not None and not errors:
            builds.append({"mapping": path, "plan": plan, "out": (root / plan["out"]).resolve()})
    if problems:
        return problems, []

    committed = {}  # profile Name (casefolded) -> entry
    for rel, (_, data, _) in entries.items():
        if rel.endswith(".streamDeckProfile"):
            name, _ = bp.profile_name(rel, data)
            if name is not None:
                committed[name.casefold()] = rel
    lower = {rel.casefold() for rel in entries}
    for i, b in enumerate(builds):
        plan = b["plan"]
        for other in builds[:i]:
            for key in ("profile_name", "plugin_subfolder"):
                if plan[key].casefold() == other["plan"][key].casefold():
                    problems.append(f"I5 {b['mapping']}: same {key} {plan[key]!r} as {other['mapping']}")
            if bp.is_inside(b["out"], other["out"]) or bp.is_inside(other["out"], b["out"]):
                problems.append(f"I5 {b['mapping']}: out {plan['out']!r} is or holds the out "
                                f"{other['plan']['out']!r} of {other['mapping']}")
        if plan["profile_name"].casefold() in committed:
            problems.append(f"I5 {b['mapping']}: profile_name {plan['profile_name']!r} is the Name of "
                            f"the committed {committed[plan['profile_name'].casefold()]}")
        b["profile"] = f"Profiles/{plan['profile_name']}.streamDeckProfile"
        b["images"] = [f"Images/{plan['plugin_subfolder']}/{n}" for n in sorted(plan["copies"])]
        for rel in [b["profile"]] + b["images"]:
            bad = bp.check_path(rel)
            if bad:
                problems.append(f"I5 {bad}")
            elif not any(rx.fullmatch(rel) for rx in bp.ALLOWED_FILES):
                problems.append(f"I5 {rel}: not on the package allowlist")
            elif rel.casefold() in lower:
                problems.append(f"I5 {rel}: the same path as a committed file")

        out = b["out"]
        profile_path = out / (plan["profile_name"] + ".streamDeckProfile")
        data = profile_path.read_bytes() if profile_path.is_file() else None
        reason = stale_reason(plan, out, data)
        images = {}
        if reason is None:
            img_dir = out / "Images" / plan["plugin_subfolder"]
            for name in sorted(plan["copies"]):
                blob = (img_dir / name).read_bytes()
                if blob != plan["copies"][name]:
                    reason = f"{rel_path(root, img_dir / name)} differs from the pack file"
                    break
                images[f"Images/{plan['plugin_subfolder']}/{name}"] = (blob, rel_path(root, img_dir / name))
        if reason is not None:
            m, o = b["mapping"], rel_path(root, out)
            problems.append(f"I4 {o}: icon build missing or out of date ({reason}); delete {o} and rebuild: "
                            f"python tools/profilegen/generate.py --icons {m}, then "
                            f"python tools/profilegen/check_icons.py --mapping {m}")
            continue
        name, p = bp.profile_name(b["profile"], data)
        problems += [x for x in p if EMBEDS not in x]
        if name is not None and name != plan["profile_name"]:
            problems.append(f"R6 {b['profile']}: profile Name {name!r} differs from the mapping's "
                            f"profile_name {plan['profile_name']!r}")
        b["data"], b["files"] = data, images
        b["source"] = rel_path(root, profile_path)
    return problems, builds


def merge(root, sha, entries, builds):
    """The package entries: {name: (oid, data, crlf)} and {name: repo-relative .local path}."""
    replaced = set()
    for b in builds:
        output = Path(b["plan"]["spec"]["output"]).as_posix()
        if output.startswith(bp.WORK + "/"):
            replaced.add(output[len(bp.WORK) + 1:])
    merged = {n: e for n, e in entries.items() if not n.endswith("/") and n not in replaced}
    local = {}
    for b in builds:
        merged[b["profile"]] = (None, b["data"], False)
        local[b["profile"]] = b["source"]
        for rel, (blob, source) in b["files"].items():
            merged[rel] = (None, blob, False)
            local[rel] = source
    packed = list(merged)
    for folder in sorted(gitkeep_dirs(root, sha)):
        if not any(r.startswith(folder + "/") for r in packed):
            merged[folder + "/"] = (None, b"", False)
    return merged, local


def package_json(public, merged, sha):
    """Return the package.json bytes (FIELDS order, no BOM, no newline) for the merged entries."""
    doc = json.loads(public.decode("utf-8"))
    names = [n.split("/")[-1][: -len(".streamDeckProfile")]
             for n in sorted(merged, key=lambda n: n.encode("ascii")) if n.endswith(".streamDeckProfile")]
    folders = sorted({n.rpartition("/")[0] + "/" for n in merged if n.startswith("Images/")
                      and not n.endswith("/")}, key=lambda n: n.encode("ascii"))
    doc["title"] = doc["title"] + " (local icon build)"
    doc["url"] = ""
    doc["notes"] = ("LOCAL BUILD, PERSONAL USE ONLY: holds images from a personal-use icon pack; never "
                    f"upload or share it. Profiles: {', '.join(names)}. Images go into the plugin Images "
                    f"folder ({', '.join(folders)}), scripts into its Scripts folder. Map the icon profiles "
                    f"in Profile Mapping as docs/package.md says. Built from commit {sha[:7]}.")
    doc = {key: doc[key] for key in bp.FIELDS}
    return json.dumps(doc, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def check_target(root, out_dir, target, builds):
    """I6: the output folder and target file rules."""
    if not bp.is_inside(out_dir, root / LOCAL):
        return [f"I6 {out_dir}: the output folder is not inside {root / LOCAL}"]
    for b in builds:
        if bp.is_inside(out_dir, b["out"]):
            return [f"I6 {out_dir}: the output folder is inside the icon build {b['plan']['out']} "
                    f"of {b['mapping']}"]
    if bp.is_inside(out_dir, root / bp.WORK):
        return [f"I6 {out_dir}: the output folder is inside the work folder {bp.WORK}"]
    try:
        res = subprocess.run(["git", "--no-optional-locks", "-C", str(root), "check-ignore", "-q",
                              str(target)], capture_output=True)
    except OSError as exc:
        raise bp.EnvError(f"cannot run git: {exc}")
    if res.returncode == 1:
        return [f"I6 {target}: git does not ignore this file (or it is tracked); write only into an "
                "ignored folder inside .local/"]
    if res.returncode != 0:
        msg = res.stderr.decode("utf-8", "replace").strip()
        raise bp.EnvError(f"git check-ignore failed (exit {res.returncode}) for {target}: {msg}")
    return []


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out-dir", help=f"output folder (default <repo>/{DEFAULT_OUT}/)")
    opts = parser.parse_args(argv)  # an unknown option exits 2
    try:
        root = bp.find_root()
        out_dir = Path(opts.out_dir).resolve() if opts.out_dir else (root / DEFAULT_OUT).resolve()
        sha, tree = bp.head_commit(root)
        problems = bp.check_clean(root) + check_inputs(root)
        if problems:
            raise bp.Refused("\n".join(problems))
        problems, entries = bp.collect(root, sha)
        if problems:
            raise bp.Refused("\n".join(problems))
        problems, builds = load_builds(root, sha, entries)
        if problems:
            raise bp.Refused("\n".join(problems))
        merged, local = merge(root, sha, entries, builds)
        merged["package.json"] = (None, package_json(entries["package.json"][1], merged, sha), False)
        local["package.json"] = None
        installed = [r for r in merged if r.startswith(("Scripts/", "Images/")) and not r.endswith("/")]
        problems = bp.check_package_json(merged["package.json"][1], installed)
        version = json.loads(entries["package.json"][1].decode("utf-8"))["versionpackage"]
        target = out_dir / f"{PACKAGE_NAME} v{version}-{sha[:7]}.ppp"
        problems += check_target(root, out_dir, target, builds)
        if problems:
            raise bp.Refused("\n".join(problems))
        order, archive = bp.build_zip(merged)
        if target.exists():
            if not target.is_file() or target.read_bytes() != archive:
                raise bp.Refused(f"I7 {target}: exists with other bytes; delete it or commit first")
    except (bp.EnvError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    except bp.Refused as exc:
        for line in str(exc).splitlines():
            print(f"REFUSED {line}", file=sys.stderr)
        return 1

    print(f"source HEAD {sha} tree {tree}")
    for b in builds:
        print(f"icon profile {b['plan']['profile_name']} from {rel_path(root, b['out'])} "
              f"({len(b['files'])} images, mapping {b['mapping']})")
    for name in order:
        oid, data, crlf = merged[name]
        if name.endswith("/"):
            print(f"-  0  {name}")
            continue
        digest = hashlib.sha256(data).hexdigest()
        if oid is not None:
            print(f"{digest}  {len(data)}  {name}  blob {oid}{' crlf' if crlf else ''}")
        elif local.get(name):
            print(f"{digest}  {len(data)}  {name}  local {local[name]}")
        else:
            print(f"{digest}  {len(data)}  {name}  generated")
    print(NOTICE)
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
