# Local icon builds (C172 G1000, A32NX and VisionJet)

A second copy of the C172 G1000 profile, one of the A32NX profile (section 4) and one of the VisionJet
profile (section 5), with key images from the
Guenseli icon pack (`A:\FS2024 Stuff\PilotsDeck\Icon Pack Guenseli_1_7_iUdcY`), built on this PC for your
own use. Addresses, commands, indicators, titles and key positions are the same as in the committed
profiles; only the key images differ. The C172 G1000 and A32NX icon profiles were installed with the local
icon package (sections 1 and 2) on 2026-11-15; their look tests and sim checks are not done yet: see the
checklist sections "P2-5: local icon build (C172 G1000)" and "P4-ICONS: local icon build (A32NX)" in
[tests/manual-checklist.md](../tests/manual-checklist.md).

## Licence: personal and private use only

The pack's `ReadMe.txt` allows personal and private use only and no public uploads without the author's
permission. So:

- The icon builds write only to `.local/icons/`, `.local/icons-a32nx/` and `.local/icons-visionjet-sf50/`,
  and the icon package only to `.local/package/`, in the repo folder, which `.gitignore` ignores
  (`/.local/`). The generator and the package build refuse to write anywhere git does not ignore.
- Never commit, upload or share anything in `.local/`, the icon profile, or a profile exported from the
  Stream Deck app after you imported it (it carries the pack's folder images inside).
- The repo holds only text: the key-to-icon mappings `tools/profilegen/icons-c172-g1000.json`,
  `tools/profilegen/icons-a32nx.json` and `tools/profilegen/icons-visionjet-sf50.json` name pack-relative
  paths and their sha256, and the code that reads them.

The committed profiles (`MSFS2024 C172 G1000.streamDeckProfile`, `MSFS2024 A32NX.streamDeckProfile` and
`MSFS2024 VisionJet.streamDeckProfile` in `pilotsdeck/MSFS2024-XL/_Package/Profiles/`) stay as they are and
have no pack images.

## 1. Build (in the repo folder, no sim needed)

```text
python tools/profilegen/generate.py --icons tools/profilegen/icons-c172-g1000.json
```

It checks the mapping first (every pack file present with its recorded sha256), then writes:

- `.local\icons\MSFS2024 C172 G1000 Icons.streamDeckProfile`: the icon profile;
- `.local\icons\Images\Guenseli-C172\`: 29 PNG files, byte copies of the pack files used by PilotsDeck keys.

Run it again after a pull that changes the generator, the data file or the mapping. Two runs give the
same bytes. To check the result: `python tools/profilegen/check_icons.py`.

Before a rebuild after a mapping change, delete the `.local\icons` folder: the generator never deletes, and
it stops (writing nothing) when the image folder holds a file the mapping no longer names.

Then pack it for the Profile Manager (the main install route, section 2):

```text
python tools/package/build_icon_package.py
```

It checks that every icon build (one per `tools/profilegen/icons-*.json` mapping: this one, the A32NX one
(section 4) and the VisionJet one (section 5)) is complete and matches the committed files, then writes
`.local\package\MSFS2024-XL-Icons v<version>-<commit>.ppp`: the icon profiles, their images, the committed
profiles that have no icon version, and the Lua scripts. It refuses, writing nothing, when an icon build is
missing or out of date (delete the `.local\icons` folder and rebuild as above) and when the output folder is
not a git-ignored folder inside `.local\`. Personal use only, like everything in `.local\`.

## 2. Install with the Profile Manager (your own step)

1. Open the Profile Manager and drop `.local\package\MSFS2024-XL-Icons v<version>-<commit>.ppp` on the
   arrow, as for the public package ([package.md](package.md), "Install"). If it lists profiles that are
   already installed, keep **Remove old Profiles** checked.
2. Click **Install**. It copies the images into the plugin's `Images\Guenseli-C172\` folder and the Lua
   scripts into its `Scripts\` folder before it shows the profile links; click each link and pick the XL.
3. Quit and restart the Stream Deck app (normally, not "Run as administrator") before the look test.

The images are copied before any profile is imported, so no key's settings panel resets its image (it does
that when the image file is missing). Keep only one of `MSFS2024 C172 G1000` and `MSFS2024 C172 G1000 Icons`
installed: the Profile Manager takes `MSFS2024 C172 G1000 Icons` for a copy of `MSFS2024 C172 G1000`, so an
update of the plain profile stops with "Found multiple Copies" while both exist. If the plain profile is
installed, map the icon profile instead (section 3) and delete the plain profile in the Stream Deck app.

Fallback without the package: in File Explorer, copy the folder `.local\icons\Images\Guenseli-C172` into
`%APPDATA%\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\Images\` (result:
`...\Images\Guenseli-C172\*.png`), restart the Stream Deck app, then import the profile file (section 3).
Do the copy **before** you import the profile or open any key's settings.

About this step:

- Both routes are the plugin's own ways to add images: the Profile Manager copies a package's `Images/`
  folder, one subfolder deep, into the plugin's `Images\` folder and replaces files of the same name, and
  PilotsDeck README section 3.3 ("Custom Images": copy the image to the plugin's Images folder; image packs
  can go in subfolders) describes the hand copy. Either is done on this PC with the Profile Manager or File
  Explorer; no tool in this repository writes in the plugin folder.
- Either way it is a file copy into the plugin folder, not a settings edit. It touches none of the plugin's
  program files, so the locally patched PilotsDeck build stays as it is
  ([docs/installation.md](installation.md#known-issue-on-this-pc-pilotsdeck-exits-at-startup-worked-around-with-a-patched-build)).
- **Never re-run the PilotsDeck installer to "fix" icons.** It would replace the patched build and bring
  back the startup crash ([Fragtality/PilotsDeck#176](https://github.com/Fragtality/PilotsDeck/issues/176)).
  The plugin's Wait image (a dark square with three dots, the same image keys show while the sim loads)
  means a missing image file only when MSFS is closed or the flight has fully loaded, so do the look test
  then, not while the sim loads. A key that shows it then has its file missing: install the package again
  (or do the fallback copy) and restart the Stream Deck app.
- Neither route deletes images: a file the mapping no longer uses stays in the plugin's folder until you
  delete it.
- If PilotsDeck is ever reinstalled or updated (after #176 is fixed), the plugin folder may be replaced:
  install the package again then.

## 3. Import, use, remove

- Import: the package install (section 2) imports the profiles through its links. Without the package,
  double-click `.local\icons\MSFS2024 C172 G1000 Icons.streamDeckProfile` (or Stream Deck app >
  Preferences > Profiles > Import) and pick the XL if asked. It appears as `MSFS2024 C172 G1000 Icons`;
  switch the XL to it. The import leaves `MSFS2024 C172 G1000` as it is: keep only one of the two
  installed (section 2).
- Automatic switching: map `MSFS2024 C172 G1000 Icons` as [package.md](package.md) says for
  `MSFS2024 C172 G1000` (same search string). A later install of the icon package with **Remove old
  Profiles** checked keeps that mapping.
- Remove: delete the `MSFS2024 C172 G1000 Icons` profile in Preferences > Profiles, then delete
  `...\Images\Guenseli-C172` from the plugin's Images folder.
- After a rebuild: delete `.local\icons`, rebuild and pack (section 1), then install the new package with
  **Remove old Profiles** checked (section 2). Without the package: delete the imported icon profile,
  replace the plugin's `Images\Guenseli-C172` folder with the new one (delete the old folder, then copy the
  new one), restart the app, import.

## 4. A32NX icon build

The FlyByWire A32NX profile has its own icon build, made the same way from its own mapping,
`tools/profilegen/icons-a32nx.json`. Addresses, commands, titles and key positions are those of the committed
`MSFS2024 A32NX` profile; only the key images differ. Installed with the local icon package on 2026-11-15;
not yet look-tested: see the checklist section "P4-ICONS: local icon build (A32NX)" in
[tests/manual-checklist.md](../tests/manual-checklist.md).

Build and check, in the repo folder (no sim needed; `--mapping` is needed, the default is the C172 mapping):

```text
python tools/profilegen/generate.py --icons tools/profilegen/icons-a32nx.json
python tools/profilegen/check_icons.py --mapping tools/profilegen/icons-a32nx.json
```

It writes:

- `.local\icons-a32nx\MSFS2024 A32NX Icons.streamDeckProfile`: the icon profile;
- `.local\icons-a32nx\Images\Guenseli-A32NX\`: 44 PNG files, byte copies of the pack files used by PilotsDeck
  keys.

Its own output folder and image subfolder keep it apart from the C172 build, so both can be built and
installed; the plugin's `Images\` folder then holds `Guenseli-C172\` and `Guenseli-A32NX\`. The icon package
(section 1) needs every icon build (C172, A32NX and VisionJet) and refuses while one is missing or out of
date: build them all before you pack.
Before a rebuild after a mapping change, delete `.local\icons-a32nx` (the generator never deletes).

Install, import, remove and rebuild as in sections 2 and 3, with the A32NX names. Without the package: copy
`.local\icons-a32nx\Images\Guenseli-A32NX` into the plugin's `Images\` folder and restart the Stream Deck app,
then import `.local\icons-a32nx\MSFS2024 A32NX Icons.streamDeckProfile`. Keep only one of `MSFS2024 A32NX` and
`MSFS2024 A32NX Icons` installed (the Profile Manager takes the second for a copy of the first, section 2).
The A32NX profiles have no aircraft search string yet ([package.md](package.md)); once it is recorded, map the
icon profile.

What differs from the C172 build:

- Most overhead pushbuttons, the autobrake keys and PARK set a background as well as their On and Off images.
  PilotsDeck draws the On or Off image over the background (PilotsDeck README section 2.3), so the key shows a
  blank pushbutton with its ON, OFF or MAN legend lit or dark as the key reads the cockpit. A value the key
  does not know shows the blank pushbutton only (for example BRK LO while MED is armed) or, on the keys with a
  Special State (PARK on the main and pedestal pages and 17 overhead pushbuttons, as in the plain profile),
  the plugin's Fault image over it. The pedestal page's ECAM control panel keys with a lamp do the same with
  the pack's ECAM key face, its light lit or dark as the key reads the lamp.
- Every readout has the same plain dark button face behind its value; a switch readout such as STROBE shows
  its position as text, never as a switch picture.
- ESS FEED keeps the plugin's own image: the pack has no ALTN legend for this pushbutton set.
- The A32NX is not installed yet: the look test works without it; the sim check waits for it.

## 5. VisionJet icon build

The VisionJet (Cirrus Vision SF50) profile has its own icon build, made the same way from its own mapping,
`tools/profilegen/icons-visionjet-sf50.json`. Addresses, commands, titles and key positions are those of the
committed `MSFS2024 VisionJet` profile; only the key images differ. Not yet installed or look-tested: see the
step "Icon look test" in the checklist sections "VisionJet SF50 profile (V-1)", "VisionJet SF50 profile (V-2)",
"VisionJet SF50 profile (V-3)" and "VisionJet SF50 profile (V-UX)" in
[tests/manual-checklist.md](../tests/manual-checklist.md).

Build and check, in the repo folder (no sim needed; `--mapping` is needed, the default is the C172 mapping):

```text
python tools/profilegen/generate.py --icons tools/profilegen/icons-visionjet-sf50.json
python tools/profilegen/check_icons.py --mapping tools/profilegen/icons-visionjet-sf50.json
```

It writes:

- `.local\icons-visionjet-sf50\MSFS2024 VisionJet Icons.streamDeckProfile`: the icon profile;
- `.local\icons-visionjet-sf50\Images\Guenseli-SF50\`: 24 PNG files, byte copies of the pack files used by
  PilotsDeck keys.

Its own output folder and image subfolder keep it apart from the other builds; the plugin's `Images\`
folder then holds `Guenseli-SF50\` as well. Before a rebuild after a mapping change, delete
`.local\icons-visionjet-sf50` (the generator never deletes).

Install, import, remove and rebuild as in sections 2 and 3, with the VisionJet names. Without the package:
copy `.local\icons-visionjet-sf50\Images\Guenseli-SF50` into the plugin's `Images\` folder and restart the
Stream Deck app, then import `.local\icons-visionjet-sf50\MSFS2024 VisionJet Icons.streamDeckProfile`. Keep
only one of `MSFS2024 VisionJet` and `MSFS2024 VisionJet Icons` installed (the Profile Manager takes the
second for a copy of the first, section 2). For automatic switching, map the icon profile with the
VisionJet's search string `microsoft_sf50` ([visionjet-sf50.md](visionjet-sf50.md)).

## How the images reach the keys

| Keys | Field the icon build sets | Where the image lives |
|---|---|---|
| PilotsDeck Dynamic Buttons (BAT, lights, AP keys, PARK, COCKPIT/EXTERNAL, 1X) | `OnImage`, `OffImage` | plugin `Images\Guenseli-C172\` (`Images\Guenseli-A32NX\` and `Images\Guenseli-SF50\` for the A32NX and VisionJet builds) |
| PilotsDeck Display Value readouts | `DefaultImage` (background; the live value is drawn over it) | same |
| PilotsDeck Simple Buttons (ATC, MAP, TRIM UP/DN, AIL L/R, RUD L/R, PFD/MFD bezel keys, SLOWER/FASTER) | `DefaultImage` | same |
| The VisionJet COM pad's digit, CLR and ENT keys (Dynamic Buttons with an image map) | `DefaultImage`; the green press image stays the package's own `Images/XL24-PadLit.png` (not from the pack) | same; the icon package also installs `Images\XL24-PadLit.png`, by hand copy it into the plugin's `Images\` folder |
| Folder keys and the back keys | the state's `Image` | embedded in the profile (that page's `Images/` folder in the file) |
| COM Radio keys (COM1 on the main page and the COM pad; NAV1, NAV2 and COM2 on the radios page) | none: left as it is | |
| The trim gauge (Display Gauge, trim 3,4) | none: left as it is; PilotsDeck draws the bar, pointer, center line and number, and no pack face is known to fit an upward bar ([design-trim-gauge.md](design-trim-gauge.md)) | |
| The aileron and rudder trim gauges (Display Gauges, trim 2,7 `AIL TRIM` and 3,7 `RUD TRIM`) | none: left as they are; PilotsDeck draws the bar, pointer, center line and number, as on the trim gauge | |
| The fuel gauges (Display Gauges, engine 2,2 `FUEL L` and 2,3 `FUEL R`) | none: left as they are; PilotsDeck draws the bar, pointer and number, and no pack face is known to fit a fuel bar ([phase3-engine-fuel.md](phase3-engine-fuel.md)) | |

Sources (read at PilotsDeck commit 11bdf1f, the one the installed patched 0.9.7 was built from):

- PilotsDeck passes an image path to the file system as it is, relative to the plugin folder, and shows
  `Plugin/Images/Wait.png` when the file is missing (`Plugin/AppConfiguration.cs`,
  `Plugin/Resources/Images/ManagedImage.cs`).
- The settings panel lists `Images\` and its direct subfolders only and skips names with `@`
  (`Plugin/Plugin/PropertyInspectorModel.cs`); hence one subfolder, `Guenseli-C172`, and plain file names.
- Display Value draws its background at the PNG's own pixel size, so readout backgrounds are 144x144
  (`Plugin/Plugin/Render/Renderer.cs`, `Plugin/Actions/Simple/SettingsModelSimple.cs`).
- Folder key images: the Stream Deck app saves them as `"Image": "Images/<name>.png"` with the PNG in the
  page's `Images/` folder inside the profile (real saved profiles on this PC: the GSX Pro and Fenix A320
  example packages, and a folder key in the Stream Deck app's own profiles).

Which pack file goes on which key, and why: `tools/profilegen/icons-c172-g1000.json`,
`tools/profilegen/icons-a32nx.json` and `tools/profilegen/icons-visionjet-sf50.json` (one row per key, with a
reason). To change an icon (C172 names below; the A32NX and VisionJet builds are the same with their own
names, sections 4 and 5):

1. Change that key's row (or add the pack file to `files` with its sha256), and remove from `files` any
   file no row uses any more.
2. Run `check_icons.py --mapping-only` (the mapping without the build; it still reads the pack folder, for
   the `ReadMe.txt` and each mapped file's sha256 and PNG size).
3. Delete the `.local\icons` folder (the generator never deletes), then rebuild (section 1).
4. Commit the mapping change, then pack and install the new icon package (sections 1 and 2; the package
   build refuses uncommitted changes under `tools/profilegen/`). Or, without the package, replace the
   plugin's `Images\Guenseli-C172` folder with the new one and import again (section 3, "After a rebuild").

## Open points (checked by the look test in the checklist)

- **A-3, back key image.** No saved Stream Deck profile on this PC has an image on a back key, so it is not
  known whether the app shows one. If the back keys show the plain default arrow, the back-key rows (one per
  child page) go (nothing else changes).
- **A-5, 303x303 images.** Many G1000 and folder images in the pack are 303x303. They are used without
  resizing (PilotsDeck and the Stream Deck app scale them). If DIRECT, FMS OUT- or the PFD folder look
  cropped or blurred, the mapping switches those keys to 144x144 alternatives.
- **A-6, taste.** PARK (parking-brake handle), ATC (blank button), MAP (map icon with a "Map" label), the
  trim arrows, RNG PUSH (knob push), the folder colours, the AP-style buttons on COCKPIT/EXTERNAL and
  1X, and the white rockers are working choices. Any change is a mapping row.
- **A-7, A-8.** The image paths resolve in the plugin folder (no "wait" images), and titles and readout
  values stay readable on the chosen images.
