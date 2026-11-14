# Local icon build (C172 G1000)

A second copy of the C172 G1000 profile with key images from the Guenseli icon pack
(`A:\FS2024 Stuff\PilotsDeck\Icon Pack Guenseli_1_7_iUdcY`), built on this PC for your own use.
Addresses, commands, indicators, titles and key positions are the same as in the committed profile;
only the key images differ. Not yet tested in the Stream Deck app or the sim: see the checklist block
"P2-5: local icon build" in [tests/manual-checklist.md](../tests/manual-checklist.md).

## Licence: personal and private use only

The pack's `ReadMe.txt` allows personal and private use only and no public uploads without the author's
permission. So:

- The icon build writes only to `.local/icons/` in the repo folder, which `.gitignore` ignores (`/.local/`).
  The generator refuses to write anywhere git does not ignore.
- Never commit, upload or share anything in `.local/`, the icon profile, or a profile exported from the
  Stream Deck app after you imported it (it carries the pack's folder images inside).
- The repo holds only text: the key-to-icon mapping `tools/profilegen/icons-c172-g1000.json` names
  pack-relative paths and their sha256, and the code that reads them.

The committed profile (`pilotsdeck/MSFS2024-XL/_Package/Profiles/MSFS2024 C172 G1000.streamDeckProfile`)
stays as it is and has no pack images.

## 1. Build (in the repo folder, no sim needed)

```text
python tools/profilegen/generate.py --icons tools/profilegen/icons-c172-g1000.json
```

It checks the mapping first (every pack file present with its recorded sha256), then writes:

- `.local\icons\MSFS2024 C172 G1000 Icons.streamDeckProfile`: the icon profile;
- `.local\icons\Images\Guenseli-C172\`: 23 PNG files, byte copies of the pack files used by PilotsDeck keys.

Run it again after a pull that changes the generator, the data file or the mapping. Two runs give the
same bytes. To check the result: `python tools/profilegen/check_icons.py`.

Before a rebuild after a mapping change, delete the `.local\icons` folder: the generator never deletes, and
it stops (writing nothing) when the image folder holds a file the mapping no longer names.

## 2. Install the images (your own hand step, before the import)

1. In File Explorer, copy the folder `.local\icons\Images\Guenseli-C172` into
   `%APPDATA%\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\Images\`.
   Result: `...\Images\Guenseli-C172\*.png`, 23 files.
2. Quit and restart the Stream Deck app (normally, not "Run as administrator").

Do this **before** you import the profile or open any key's settings: if a key's image is not in the
plugin's Images folder, opening that key's settings panel resets its image field to the first image in
the list.

About this step:

- It is the plugin's documented way to add images: PilotsDeck README section 3.3 ("Custom Images": copy the
  image to the plugin's Images folder; image packs can go in subfolders). It is your own step; no Claude
  session writes in the plugin folder.
- It is a file copy into the `Images\` folder, not a settings edit. It touches none of the plugin's
  program files, so the locally patched PilotsDeck build stays as it is
  ([docs/installation.md](installation.md#known-issue-on-this-pc-pilotsdeck-exits-at-startup-worked-around-with-a-patched-build)).
- **Never re-run the PilotsDeck installer to "fix" icons.** It would replace the patched build and bring
  back the startup crash ([Fragtality/PilotsDeck#176](https://github.com/Fragtality/PilotsDeck/issues/176)).
  The plugin's Wait image (a dark square with three dots, the same image keys show while the sim loads)
  means a missing image file only when MSFS is closed or the flight has fully loaded, so do the look test
  then, not while the sim loads. A key that shows it then has its file missing: copy the folder again
  (step 1) and restart the Stream Deck app.
- If PilotsDeck is ever reinstalled or updated (after #176 is fixed), the plugin folder may be replaced:
  copy the folder again then.

## 3. Import, use, remove

- Import: double-click `.local\icons\MSFS2024 C172 G1000 Icons.streamDeckProfile` (or Stream Deck app >
  Preferences > Profiles > Import), pick the XL if asked. It appears as `MSFS2024 C172 G1000 Icons` beside
  `MSFS2024 C172 G1000`; switch the XL to it. Its own name keeps the committed profile and its Profile
  Manager aircraft mapping untouched.
- Remove: delete the `MSFS2024 C172 G1000 Icons` profile in Preferences > Profiles, then delete
  `...\Images\Guenseli-C172` from the plugin's Images folder.
- After a rebuild: delete the imported icon profile, replace the plugin's `Images\Guenseli-C172` folder
  with the new one (delete the old folder, then copy the new one as in section 2), restart the app, import.

## How the images reach the keys

| Keys | Field the icon build sets | Where the image lives |
|---|---|---|
| PilotsDeck Dynamic Buttons (BAT, lights, AP keys, PARK, COCKPIT/EXTERNAL, 1X) | `OnImage`, `OffImage` | plugin `Images\Guenseli-C172\` |
| PilotsDeck Display Value readouts | `DefaultImage` (background; the live value is drawn over it) | same |
| PilotsDeck Simple Buttons (ATC, MAP, TRIM UP/DN, PFD/MFD bezel keys, SLOWER/FASTER) | `DefaultImage` | same |
| Folder keys and the back keys | the state's `Image` | embedded in the profile (that page's `Images/` folder in the file) |
| COM1 (COM Radio) | none: left as it is | |

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

Which pack file goes on which key, and why: `tools/profilegen/icons-c172-g1000.json` (one row per key, with
a reason). To change an icon:

1. Change that key's row (or add the pack file to `files` with its sha256), and remove from `files` any
   file no row uses any more.
2. Run `check_icons.py --mapping-only`.
3. Delete the `.local\icons` folder (the generator never deletes), then rebuild (section 1).
4. Replace the plugin's `Images\Guenseli-C172` folder with the new one and import again (section 3,
   "After a rebuild").

## Open points (checked by the look test in the checklist)

- **A-3, back key image.** No saved Stream Deck profile on this PC has an image on a back key, so it is not
  known whether the app shows one. If the back keys show the plain default arrow, the 8 back-key rows go
  (nothing else changes).
- **A-5, 303x303 images.** Many G1000 and folder images in the pack are 303x303. They are used without
  resizing (PilotsDeck and the Stream Deck app scale them). If DIRECT, FMS OUT- or the PFD folder look
  cropped or blurred, the mapping switches those keys to 144x144 alternatives.
- **A-6, taste.** PARK (parking-brake handle), ATC (blank button), MAP (map icon with a "Map" label), the
  trim arrows, RNG PUSH (knob push), the folder colours, the AP-style buttons on COCKPIT/EXTERNAL and
  1X, and the white rockers are working choices. Any change is a mapping row.
- **A-7, A-8.** The image paths resolve in the plugin folder (no "wait" images), and titles and readout
  values stay readable on the chosen images.
