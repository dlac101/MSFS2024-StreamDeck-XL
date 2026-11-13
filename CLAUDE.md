# Project instructions: MSFS 2024 Stream Deck XL

A free Stream Deck XL cockpit for MSFS 2024, built entirely from PilotsDeck configuration, Lua
scripts and images. The full brief is `docs/original-plan.md`; current status is in `README.md`
and `CHANGELOG.md`.

## Environment

- One PC, two Windows accounts. MSFS 2024 (Steam), the Stream Deck app (7.6.1), PilotsDeck
  (0.9.7 dev build) and FSUIPC7 are installed in the **Admin** account. Details: `docs/installation.md`.
- This repo is at `A:\FS2024 Stuff\msfs2024-streamdeck-xl` so every account can use it. Keep project
  files here, never in a user profile.
- A session running in **another** account can't read `C:\Users\Admin\...` and must ask the
  user to copy files (logs, `InputEvents.txt`, profile exports) into the repo.
- A session running **in Admin** can read the plugin folder directly:
  `%APPDATA%\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\` (logs in `log\`,
  `InputEvents.txt` once a flight has loaded). Read freely, but change plugin and Stream Deck
  settings through their own interfaces, not by editing their files by hand, unless the user asks.
- Never run the PilotsDeck installer, the plugin or the Stream Deck app elevated ("Run as
  administrator"). PilotsDeck's docs warn against it.
- Git across accounts: each account needs
  `git config --global --add safe.directory "A:/FS2024 Stuff/msfs2024-streamdeck-xl"` once.

## Decisions so far

- First aircraft: default **Cessna 172 Skyhawk G1000**. The steam-gauge C172 may come later.
- Phase 4 airliner: **FlyByWire A32NX** (installer in `A:\FS2024 Stuff`).
- Use the installed PilotsDeck 0.9.7, not the stable 0.9.1.
- Who does what: Claude researches variable/event names, writes Lua, docs and checklists;
  the user sets up keys in the Stream Deck app and runs the sim tests. (A session in Admin may
  also read logs and files directly to check setups.)
- The user's **bigly** skill (session chain): its preconditions are met (Phase 1 four-key test
  passed and committed 2026-11-11). Chain sessions start in this folder.
- PilotsDeck in the Admin account is a **locally patched 0.9.7 build** (startup crash,
  Fragtality/PilotsDeck#176). Don't re-run the PilotsDeck installer or "update" the plugin until
  #176 is fixed, or the crash comes back. Details: `docs/installation.md`.
- Battery in the 2024 C172 uses the input event `B:electrical_battery_1`, not the standard
  SimVar/K-event (the cockpit switch drives battery index 2). See `docs/aircraft-mappings.md`.

## Working rules

- Don't invent variable or event names. Use the PilotsDeck README (address syntax, section 2.1.1),
  the MSFS SDK, FlyByWire's docs, HubHop or `InputEvents.txt`, and say which.
- Every aircraft variable/event goes in `docs/aircraft-mappings.md`. Mark it "Unverified" until
  a sim test passes, then record the date and sim version.
- Read actual sim state for every indicator; never assume a key press worked.
- Nothing may depend on which flight controls are connected (Xbox Elite or T.16000M/TWCS).
- Package layout follows PilotsDeck's Profile Manager work folder: `pilotsdeck/MSFS2024-XL/_Package/`.
  Keep each profile's name the same between versions, since the Profile Manager uses it to
  update profiles and keep their aircraft mappings.
- Example packages the user downloaded are in `A:\FS2024 Stuff\PilotsDeck` and show real package
  and Lua formats. The user keeps adding PilotsDeck profiles there for reference and reuse (so far
  Fenix A320, GSX Pro, a generic profile, Jiblet's C172 G1000 for the Stream Deck + XL). Check that
  folder for real saved examples and leads before building something new. Their addresses are
  leads only: confirm each one for MSFS 2024 as above. Don't copy their files into this public repo.
- Icon pack: `A:\FS2024 Stuff\PilotsDeck\Icon Pack Guenseli_1_7_iUdcY` (per-aircraft folders,
  `Folder Icons`, `Standard Avionics Suite`, `StandardProp` and more). The user rates it highly; use
  it for key and folder images. Its `ReadMe.txt` allows personal and private use only, with no
  public uploads without the author's permission. So never commit its icons, or a profile with them
  embedded, to this public repo. Use them only in a local build that stays out of git, unless the
  user gets the author's permission.
- Commit only when the user asks.

## Checking sim state (Admin account)

- **Which variable does a cockpit control really drive?** Don't guess. Run `tools/scmon` (read-only
  SimConnect monitor, see its README) while the user works the control with the mouse. Also check
  the aircraft's input events (`docs/reference/InputEvents-*.txt`): in MSFS 2024 aircraft the
  cockpit control may drive a B-Var and a different SimVar index than the standard K-event.
- **PilotsDeck's local API** (`http://localhost:42042/v1/get|register|unregister|list`) doesn't
  URL-decode addresses: A-Vars with spaces read `0`. Use it only for B-Vars and L-Vars, and
  unregister anything you register. Don't use its `set/` or `send/` calls without the user's OK.
- **What a key is configured to do:** read its saved settings from the profile's `manifest.json`
  under `%APPDATA%\Elgato\StreamDeck\ProfilesV3\`, and what it sent from the plugin log
  (`log\PilotsDeck<date>.log`, "Running Command" lines). Read only; change keys in the Stream Deck app.
- The Stream Deck settings panel saves a text field only when focus leaves it. A key that ignores
  its On/Off values usually has them empty in the saved settings.
- The .NET 10 SDK is installed per user at `%LOCALAPPDATA%\Microsoft\dotnet` (not on PATH).
