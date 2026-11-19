# The package: build, install, map, update

The profiles and Lua scripts in `pilotsdeck/MSFS2024-XL/_Package/` ship as one PilotsDeck Profile Manager
package, `MSFS2024-XL v<version>.ppp` (a zip archive the Profile Manager installs). Sources: the
[PilotsDeck README](https://github.com/Fragtality/PilotsDeck/blob/master/README.md), sections 1.5 (installing
a package), 3.4 (profile switching) and 3.6 (packages). **Not yet installed or tested with the Profile
Manager**: the checklist section "P5-PKG: package install (C172 G1000)" in
[../tests/manual-checklist.md](../tests/manual-checklist.md) is the test.

## Build

In the repository folder (Python 3 and git, nothing else):

    python tools/package/build_package.py

It writes `pilotsdeck/MSFS2024-XL/_Releases/MSFS2024-XL v<version>.ppp` (git ignores `_Releases/`; use
`--out-dir DIR` for another folder) and prints the source commit, one line per entry with its sha256, and the
package's sha256. The version is `versionpackage` in `package.json`.

- It packs only what is **committed** at HEAD in the work folder: `package.json`, `Profiles/*.streamDeckProfile`,
  `Scripts/*.lua` (also `Scripts/global/` and `Scripts/image/`) and `Images/*.png` (also one subfolder deep).
  Lua files get CRLF line endings, as on disk; everything else is packed byte for byte.
- Two builds of the same commit give the same bytes (stored entries, fixed time), so anyone can check a
  package against its sha256.
- It refuses, with the path and the rule, and writes nothing: uncommitted or untracked files in the work
  folder; any other file kind; an invalid `package.json`; a profile whose name differs from its file name or
  that embeds an image; a package of the same version with different content in the output folder (bump the
  version). It compares only with the file already in that folder: a build into another folder, or after that
  file is deleted, is not refused. Run `python tools/package/build_package.py --help` or read the script's
  docstring for the full list.
- Don't use the Profile Manager's **Create Package** button for this repository: it rewrites `package.json`
  and packs the folder as it is on disk, including uncommitted changes and the `.gitkeep` files.

## Install

You need PilotsDeck 0.9.7 or later (the package's `versionplugin`; the Profile Manager refuses older
plugins). Installing a package doesn't need the PilotsDeck installer: if you run the patched 0.9.7 build
described in [installation.md](installation.md), don't re-run the installer or update the plugin.

1. Open the Profile Manager: the PilotsDeck icon in the Windows tray, or `ProfileManager.exe` in
   `%APPDATA%\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\`.
2. Drop `MSFS2024-XL v<version>.ppp` on the arrow, or browse to it.
3. Read the notes and the version it shows. If it reports profiles of the same name that are already
   installed (`MSFS2024 C172 G1000`, `MSFS2024 A32NX`, `MSFS2024 VisionJet`), keep **Remove old Profiles**
   checked.
4. Click **Install**. The Profile Manager stops and starts the Stream Deck app as needed and copies the Lua
   scripts into the plugin's `Scripts` folder (replacing older copies), so you no longer copy them by hand.
5. It shows one link per profile: click each one and pick your Stream Deck XL. It goes on when every profile
   is installed or ignored.

Then the Stream Deck app lists each profile once (no "Copy" profile left over).

## Map the C172 G1000 profile (automatic switching)

A package can't carry an aircraft mapping; you set it once in the Profile Manager:

1. Open **Profile Mapping** (stop the Stream Deck app when it asks).
2. Pick `MSFS2024 C172 G1000` and check **StreamDeck Profile modified for Switching**.
3. Type the search string `asobo_c172sp_g1000`, click the **Plus** button, then **Save**.

PilotsDeck switches to a profile when one of its search strings is part of the loaded aircraft's string
(case does not matter). `asobo_c172sp_g1000` is in the aircraft string PilotsDeck logs for the default
Cessna 172 Skyhawk G1000 ([aircraft-mappings.md](aircraft-mappings.md)). The `MSFS2024 A32NX` profile has
no search string yet: its aircraft string is recorded at the first A32NX flight (same file), so pick that
profile on the Stream Deck by hand until then.

The `MSFS2024 VisionJet` profile maps the same way with the search string `microsoft_sf50`
([visionjet-sf50.md](visionjet-sf50.md)); not yet tested.

## Update to a newer package

Install the new `.ppp` the same way, with **Remove old Profiles** checked. The Profile Manager matches
profiles by name: the new profile takes the old one's place, the old one goes to the recycle bin, and its
aircraft mapping moves to the new one. It never compares package versions, so installing the same version
again works the same way.

A profile that the new package doesn't hold is left as it is: the Profile Manager matches profiles by name,
and `removefiles` can't remove a profile ("For maintainers" below). Earlier builds of this package also
held the Phase 1 profile `MSFS2024 C172 POC` (the four-key test, [poc-c172.md](poc-c172.md)); the package
no longer ships it. If you don't need it any more, delete it in the Stream Deck app (Preferences >
Profiles).

## Local icon package (personal use)

`python tools/package/build_icon_package.py` builds a second package from the local icon builds in the
git-ignored `.local/` folder: the icon profiles in place of the plain profiles they copy, their images, the
other committed profiles and the scripts, written only to `.local/package/`. It is for your own Profile
Manager install, never for a release or an upload; build and install steps: [icons.md](icons.md). It was
installed with the Profile Manager on 2026-11-15 (the C172 G1000 and A32NX icon profiles imported, its images
and scripts copied into the plugin folder); its look tests are not done yet. The public package above stays
icon-free and unchanged.

## For maintainers: versions and releases

- The version lives only in `package.json` `versionpackage`, as `MAJOR.MINOR`. Each release bumps MINOR;
  1.0 is for a complete C172 G1000 profile.
- A newly committed profile or script in the work folder is packed by the next build without any change to
  the build script; its name belongs in the `package.json` notes (`python tools/profilegen/check_docs.py`
  fails until they name it). A file of another kind (another folder, `Extras/`) is refused until the build
  script supports it.
- A release: bump `versionpackage`, update `notes` and `aircraft` (the build prints a NOTE, and
  `check_docs.py` a FAIL, for each packed profile or script the notes don't name as a whole name:
  `A32NX.lua` inside `XL24-A32NX.lua` does not count), commit, then build.
  Rebuilding an existing version with new content is refused only while that version's `.ppp` is still in
  the output folder (`_Releases/` by default), so keep each released `.ppp` there.
- Never rename a profile (the manifest `Name` and the file name stay the same between versions): the
  Profile Manager uses the name to update the profile and keep its mapping.
- When a script or image is renamed or dropped, add its old plugin path (`Scripts/<old>.lua`,
  `Images/...`) to `removefiles` and keep it there in later versions. `removefiles` can't remove a profile:
  delete a dropped profile in the Stream Deck app.
- The build makes no git tag and no GitHub release. To publish a version, build it and attach the `.ppp` to
  a GitHub release yourself.
