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
- The user's **bigly** skill (session chain) is for later: set it up **only after the Phase 1
  four-key test passes**, after a first commit, with chain sessions started in this folder.

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
- Example packages the user downloaded (Fenix A320, GSX Pro, a generic profile) are in
  `A:\FS2024 Stuff\PilotsDeck` and show real package and Lua formats.
- Commit only when the user asks.
