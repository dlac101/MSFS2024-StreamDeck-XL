# Changelog

## Unreleased
- Repo created. Phase 1 four-key proof-of-concept spec written (untested).
- FlyByWire A32NX chosen as the Phase 4 airliner.
- Added CLAUDE.md so Claude sessions in any Windows account get the project context.
- Added MIT license.
- PilotsDeck 0.9.7 exits at startup on this PC (Efficiency mode API rejected by Windows).
  Reported as Fragtality/PilotsDeck#176; running a locally patched build until it's fixed.
  Details in docs/installation.md.
- Phase 1 core test passed (2026-11-11, MSFS 1.9.24.0, PilotsDeck 0.9.7 patched, C172 G1000):
  - Connection: plugin reached READY with the flight loaded; HDG tracks the PFD heading. (The
    hourglass-while-loading check wasn't seen: the keys were made after the flight loaded.)
  - Stream Deck -> sim: BAT, PARK and AP keys switch the cockpit controls.
  - Sim -> Stream Deck: BAT, PARK and AP keys follow mouse clicks in the cockpit.
  - Battery uses the C172's input event `B:electrical_battery_1`: the cockpit switch drives battery
    index 2, so the standard index-1 SimVar and `K:TOGGLE_MASTER_BATTERY` don't stay in sync.
  - Not yet run: restart survival, controller independence, disconnected sim, profile round trip.
- Added docs/reference/InputEvents-C172-G1000.txt (233 input events).
- Phase 2 main page spec written (untested): docs/phase2-main-page.md (C172 G1000, 26 keys, 6 reserved).
- Phase 2 profile generated (untested, not yet imported): tools/profilegen builds `MSFS2024 C172 G1000.streamDeckProfile` (26 keys, 4 folder keys to empty Trim/Views/Checklist/More pages, back key at 1,1); setup is now "import the file"; navigation plan in docs/navigation.md.
- Phase 2 Trim and Views pages generated (untested): docs/phase2-trim-views.md; trim page = elevator trim up/down (K-events) and two trim readouts; views page = COCKPIT and EXTERNAL by A-Var write to CAMERA STATE (no vJoy, no key bindings; the 20 view K-event keys of the first build were ignored by MSFS 2024 in the sim test and are gone) and 3 camera-state readouts; check.py now checks child pages against their doc and fails on a Key table position listed twice.
- Phase 2 G1000 and V-speeds pages generated (untested): docs/phase2-g1000-vspeeds.md; the More page (main 4,8) now opens three second-level pages: PFD and MFD (G1000 bezel: 12 softkeys, MENU, PROC, ENT, CLR, CLR long, FPL, Direct-To, FMS and range knobs, by H-event) and V-speeds (7 readouts of the SDK design/reference speeds; Vx and Vno Empty, no SimVar); check.py now checks folder keys on child pages and at most two folder levels.
- Phase 2 Sim rate page generated (not yet sim-tested): docs/phase2-sim-rate.md; main 3,7 (was reserved for a timer) is now the folder `SIM RATE`; the page holds 1X, 2X, 4X (`K:SIM_RATE_SET:1/2/4`, each lit when `(A:SIMULATION RATE, number)` equals its rate) and RATE (readout, press `K:SIM_RATE_INCR`, long press `K:SIM_RATE_DECR`); all Unverified; the checklist starts with the hand test HT-1.
- Local icon build option (not yet tested in the app or the sim): `generate.py --icons tools/profilegen/icons-c172-g1000.json` builds `MSFS2024 C172 G1000 Icons` with key images from the Guenseli icon pack into the git-ignored `.local/icons/` (personal use only, never committed; the repo holds only the key-to-icon mapping as text); new `check_icons.py`; `.gitignore` ignores `/.local/`; how to install and import: docs/icons.md. The committed profile is unchanged.
- Designs written (not built, not sim-tested), ideas taken from the Flight Tracker Stream Deck plugin (no code or images): docs/design-com1-pad.md, a COM1 frequency number pad (MORE > COM PAD; Lua script `XL24-COMPAD.lua` sends `K:COM_STBY_RADIO_SET_HZ`, long ENT also swaps; 25 kHz shorthand; read-back on a COM1 key); docs/design-trim-gauge.md, an elevator trim bar gauge (PilotsDeck Display Gauge on `ELEVATOR TRIM PCT EX2`, trim page 3,4). New Unverified rows in docs/aircraft-mappings.md ("Planned: COM1 pad").
- Larger key titles (not yet checked in the app): `generate.py` now saves Simple and Dynamic Button titles that were 10 at 14 (the user's request), in the committed G1000 profile and in the icon build; readout keys (COM Radio, Display Value) keep their size because their values use the title font (COM1 stays 10); a per-key `title_size` in the data file sets another size where a title does not fit (RNG PUSH and EXTERNAL 13, FUEL PMP 14); keys at 15 (readouts and the Phase 1 style switches) and folder/back keys at 12 unchanged; a per-key `title_align` (top, middle, bottom) puts the titles of the main page folder keys VIEWS, CHECKLIST and MORE in the middle (the user's own edit), every other key keeps its alignment; check.py checks every key's size and alignment.
- Phase 2 COM1 pad generated (not yet tested in the app or the sim): docs/phase2-com1-pad.md (was docs/design-com1-pad.md); MORE 1,5 is the folder `COM PAD` (the user's choice) to the second-level page compad: number pad 0-9, CLR (long press clears), ENT (sets COM1 standby by `K:COM_STBY_RADIO_SET_HZ`; long press also swaps it to active), ENTRY (the typed digits from the internal variable `X:XL24_COMPAD_ENTRY`), STBY ID (`COM STANDBY FREQ IDENT:1`, optional) and the COM1 key; the keys run the new standard Lua script `pilotsdeck/MSFS2024-XL/_Package/Scripts/XL24-COMPAD.lua` (command type Lua Function, 14), which must be copied into the plugin's Scripts folder; check.py knows the `lua:` command type; the icon mapping covers the new keys (local build only); checklist section "Phase 2: COM1 pad (C172 G1000)"; all new names Unverified.
