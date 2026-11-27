# Manual test checklist

Copy the relevant section into a dated note (or the CHANGELOG) each time you run it.
Record: date, MSFS 2024 version, PilotsDeck version, aircraft.
Script steps below: the package install ([docs/package.md](../docs/package.md), "Install") copies every script; copying by hand is the fallback.

## Phase 1: four-key proof of concept (C172 G1000)

Setup: cold and dark or parked, profile `MSFS2024 C172 POC` active.

**Connection**
- [ ] Keys show the hourglass while the sim loads, then live content once in the cockpit.
- [ ] Heading key shows a 3-digit heading that changes as the aircraft turns (taxi or slew).

**Stream Deck -> sim**
- [ ] Battery key turns the battery on; the cockpit switch moves and the key shows "on".
- [ ] Battery key turns it off again.
- [ ] Parking brake key sets and releases the brake.
- [ ] With battery and avionics on, AP key engages and disengages the autopilot.

**Sim -> Stream Deck (the important one)**
- [ ] Battery switched with the mouse: key updates without being pressed.
- [ ] Parking brake changed with the mouse: key updates.
- [ ] AP engaged/disengaged with the mouse on the G1000 (or AP disconnect on the controller): key updates.

**Restart survival**
- [ ] Quit to main menu and reload the flight: keys recover by themselves.
- [ ] Restart MSFS: keys recover.
- [ ] Quit and restart the Stream Deck app: the profile and all four keys are intact.

**Controller independence**
- [ ] All of the above works flying with the Xbox Elite controller.
- [ ] All of the above works flying with the T.16000M + TWCS.

**Disconnected sim**
- [ ] With MSFS closed, keys show the plugin's idle preview, not a stale "on" state.

**Profile round trip**
- [ ] Exported profile saved to your backup folder, not into the repository (the package no longer ships it,
  and the generator's copy in `tools/profilegen/` stays unchanged).
- [ ] Re-imported copy works the same as the original.

## Phase 2: main page (C172 G1000)

Setup: profile `MSFS2024 C172 G1000` imported from the generated file and active (see
[docs/phase2-main-page.md](../docs/phase2-main-page.md), "Import the profile"). C172 G1000 loaded cold and
dark. Wait until the keys no longer show the Wait image (hourglass) before judging any key: B-Var keys can
show Off or the Fault image while the flight loads.

Record: date, MSFS 2024 version, PilotsDeck version, aircraft, and for each fallback or changed value
below, which one you used.

**Import (no sim needed)**
- [ ] A profile already named `MSFS2024 C172 G1000` (hand-made or older): exported to the backup folder and
  deleted before the import. None existed: tick and note "none".
- [ ] Double-click `pilotsdeck/MSFS2024-XL/_Package/Profiles/MSFS2024 C172 G1000.streamDeckProfile` (or
  Preferences > Profiles > Import): the Stream Deck app imports it for the XL without an error, and the
  profile list shows `MSFS2024 C172 G1000` once. Select it. Record any message the app showed.
- [ ] Your other profiles (the Phase 1 profile `MSFS2024 C172 POC` too, if it is still installed) are
  still there, unchanged.
- [ ] The main page shows 26 PilotsDeck keys, 4 folder keys (`TRIM` 1,7, `VIEWS` 1,8, `CHECKLIST` 3,8,
  `MORE` 4,8) and 2 empty keys (3,7 and 4,7), as in the doc's Layout.

**Round trip: the keys against the doc (no sim needed)**
- [ ] Select each of the 26 keys in the Stream Deck app and compare its settings panel with the doc's Key
  table and template tables: action, title, command type and address, On/Off values, value address, format,
  mappings, Decode BCD, Special State, long press. Record every key that differs, with the field.
- [ ] COM1 (3,1) in particular (built from the plugin's source, no saved example existed): the panel opens,
  shows Active `(A:COM ACTIVE FREQUENCY:1, MHz)`, Standby `(A:COM STANDBY FREQUENCY:1, MHz)`, Format `3`,
  command `K:COM_STBY_RADIO_SWAP`. Record anything odd.

**Folders and back keys (no sim needed)**
- [ ] The four folder keys show a folder image and their titles (`TRIM`, `VIEWS`, `CHECKLIST`, `MORE`).
  Record it if a key is blank (title only, or nothing).
- [ ] `TRIM` opens a page that holds only a back key at top left (1,1); the back key returns to the main page.
- [ ] `VIEWS`: same.
- [ ] `CHECKLIST`: same.
- [ ] `MORE`: same.

**Diagnostic first (before the tests below)**
- [ ] For each B-Var switch key (FUEL PMP, NAV LT, BCN, STRB, LDG, TAXI, PITOT): flip the cockpit switch
  with the mouse, both ways, and watch the key. Three cases:
  - The key shows On when the switch is on and Off when it is off: the values are `1`/`0`. Nothing to change.
  - The key shows the Fault image (Special State) in either position: that value is something else.
  - The key doesn't change, or shows On and Off the wrong way round: the B-Var doesn't follow the switch
    as set up.

  In the last two cases, put the address in a temporary Display Value key (Value: Address = the B-Var,
  no Format) to read the raw on and off values, and record them here. If the raw value changes with the
  switch, the key's On/Off values change to what you find; if it doesn't change at all, use that key's
  fallback in the doc and record it.
- [ ] Temporary Display Value key with `(A:FLAPS NUM HANDLE POSITIONS, number)`: record the number
  (the FLAPS mapping assumes 4 positions, `0` to `3`). `3` or `4` both fit, since the SDK doesn't say
  whether UP counts; the flaps-lever line below decides. Delete the temporary key afterwards.
- [ ] COM1 key: record what it shows for active and standby compared with the PFD (e.g. `118.000` /
  `121.500`). Nonsense numbers: try the COM1 fallback in the doc and record which one works. With the
  BCD16 fallback, if it shows `11850.00`, set Scalar `0.01`.
- [ ] XPDR key: record what it shows compared with the PFD code (e.g. `1200`). Wrong number: try the
  XPDR fallback (unit `number`, Decode BCD unchecked) and record which one works.
- [ ] BARO key: record which altimeter index the PFD baro was seen on. Turn the PFD baro knob with the
  mouse; the key follows with `:1` = index 1. If it doesn't, try `:2` (then `:3`) and record the index
  that follows the PFD.
- [ ] Press BARO with the index found: does the PFD baro change? (yes/no)

**Sim -> Stream Deck (the important one: change the control with the mouse, don't press the key)**
- [ ] Battery switch: BAT key follows.
- [ ] Electric fuel pump switch: FUEL PMP key follows.
- [ ] Parking brake: PARK key follows.
- [ ] Flaps lever through every notch, down and up: FLAPS shows `UP`, `10`, `20`, `30` in step.
- [ ] NAV light switch: NAV LT key follows.
- [ ] Beacon switch: BCN key follows.
- [ ] Strobe switch: STRB key follows.
- [ ] Landing light switch: LDG key follows.
- [ ] Taxi light switch: TAXI key follows.
- [ ] Pitot heat switch: PITOT key follows.
- [ ] With battery and avionics on, on the G1000 bezel: AP on/off, AP key follows.
- [ ] HDG mode on/off: HDG key follows.
- [ ] ALT mode on/off: ALT key follows.
- [ ] VS mode on/off: VS key follows.
- [ ] NAV mode with the CDI on GPS: NAV (row 2) key follows.
- [ ] NAV mode with the CDI on VLOC (LOC1/VOR1): NAV (row 2) key follows.
- [ ] APR mode on/off: APR key follows.
- [ ] FLC mode on/off: FLC key follows.
- [ ] FD on/off: FD key follows.
- [ ] COM1 swap on the PFD: COM1 key's active and standby swap. Tune the standby frequency: the key follows.
- [ ] Change the transponder code on the PFD: XPDR key follows.
- [ ] Turn the baro knob, then press the BARO softkey / STD: BARO key follows both.
- [ ] Press the CDI softkey on the PFD: CDI key changes between `GPS` and `VLOC`.
- [ ] Move the throttle: RPM key follows the engine RPM (engine running).
- [ ] GEAR key shows `FIXED`.

**Stream Deck -> sim (press the key; the cockpit changes, then the key shows the new state)**
- [ ] BAT turns the battery on and off.
- [ ] FUEL PMP turns the fuel pump on and off.
- [ ] PARK sets and releases the parking brake.
- [ ] FLAPS press: one notch down each press, down to 30. Long press: one notch up each time, back to UP.
  (Want them the other way round? Note it; the two commands get swapped.)
- [ ] NAV LT, BCN, STRB, LDG, TAXI, PITOT each switch their cockpit switch on and off.
- [ ] AP, HDG, ALT, VS, NAV (row 2), APR, FLC, FD each switch their mode on and off on the G1000.
- [ ] COM1 press swaps active and standby on the PFD.
- [ ] CDI press switches the PFD's CDI source.
- [ ] BARO press sets the altimeter to sea-level pressure (or 29.92 above 18000 ft).
- [ ] ATC press opens the ATC window; a second press closes it.
- [ ] MAP press opens the flight map.
- [ ] ATC or MAP does nothing: that key becomes Empty and its row in aircraft-mappings.md is marked
  "does not work" (the row stays). Record which.

**Disconnected sim**
- [ ] With MSFS closed: every key shows its idle preview; none shows a stale "on" state or a stale value.
- [ ] While the sim loads: keys show the Wait image.
- [ ] After the flight loads: live values on every key within a few seconds.

**Unavailable value** (not a Phase 4 test)
- [ ] Switch to another default aircraft and back, or start the sim to the main menu only: no key claims
  a misleading state. Record what each key showed.
- [ ] Flight loaded cold and dark, battery off: record what COM1, XPDR, BARO, CDI and RPM show (record only).

**Restart survival**
- [ ] Quit to main menu and reload the flight: keys recover by themselves.
- [ ] Restart MSFS: keys recover.
- [ ] Quit and restart the Stream Deck app: the profile, all 26 keys and the 4 folder keys are intact.

**Controller independence**
- [ ] All of the above works flying with the Xbox Elite controller.
- [ ] All of the above works flying with the T.16000M + TWCS.

**Results to record**
- [ ] Record which keys passed Sim -> Stream Deck, which passed Stream Deck -> sim, every fallback used,
  every On/Off value or index that changed, and the altimeter index seen.

## Phase 2: Trim and Views pages (C172 G1000)

Reference: [docs/phase2-trim-views.md](../docs/phase2-trim-views.md). These pages are in the same profile
file as the main page. Record: date, MSFS 2024 version, PilotsDeck version, and every fallback or changed
value you used.

**Reimport (no sim needed)**
- [ ] If you changed any key by hand during the main-page test, write down which key and field first.
- [ ] In the Stream Deck app, export the installed `MSFS2024 C172 G1000` to the backup folder, then delete
  it (the Profile Manager finds profiles by name: never keep two with this name).
- [ ] Double-click `pilotsdeck/MSFS2024-XL/_Package/Profiles/MSFS2024 C172 G1000.streamDeckProfile` (pick the
  XL if asked), select `MSFS2024 C172 G1000`. Check its aircraft mapping in the Profile Manager.
- [ ] The main page looks as before (26 keys, 4 folder keys, 3,7 and 4,7 empty). `CHECKLIST` and `MORE`
  still open back-key-only pages.

**Layout and round trip (no sim needed)**
- [ ] `TRIM` opens the trim page: back key at 1,1, `TRIM UP` 2,2, `TRIM` 3,2, `TRIM DEG` 3,3, `TRIM DN` 4,2,
  everything else empty. The back key returns to the main page.
- [ ] `VIEWS` opens the views page: back key at 1,1; row 1 `COCKPIT`, `EXTERNAL`, `CAMERA`, `VIEW`,
  `VIEW NO`; everything else empty (rows 2 to 4 too). The back key returns to the main page.
- [ ] Select each key on both pages and compare its settings panel with the doc's Key tables (action,
  title, command type and address, value address, format, mappings, On/Off values). Record every key that
  differs, with the field.

**Diagnostic first**
- [ ] Flight loaded, sitting in the cockpit: record what `CAMERA`, `VIEW` and `VIEW NO` show (expected
  `COCKPIT`, `PILOT`, a number). Switch to the external view (with the sim's own key or menu, not the deck)
  and record the three again (expected `CHASE` for `CAMERA`: 2 = cockpit, 3 = external, seen in the sim
  2026-11-11). If the cockpit or external camera shows another number than `2` / `3`, record it:
  the On Value and On/Off values of `COCKPIT` and `EXTERNAL` change to it.
- [ ] Trim neutral (if you don't know, leave it as loaded): record what `TRIM` and `TRIM DEG` show. If
  `TRIM` shows nothing or stays `0.0` while `TRIM DEG` moves in the steps below, use the TRIM fallback in the
  doc and record it.

**Sim -> Stream Deck (change it in the sim, don't press the key)**
- [ ] Turn the trim wheel with the mouse, nose up and nose down: `TRIM` and `TRIM DEG` follow. Record which
  sign nose-up trim gives on each (expected: positive on `TRIM`).
- [ ] If the cockpit has an electric trim switch on the yoke: work it with the mouse; the readouts follow.
  Record whether there is one.
- [ ] Switch cockpit -> external -> cockpit with the sim's own controls: `COCKPIT` shows On in the cockpit
  and Off outside; `EXTERNAL` the other way round; `CAMERA` follows.
- [ ] Change to an instrument view and between pilot views (Close, Pilot, Landing, Copilot) with the sim's
  own controls: `VIEW` and `VIEW NO` follow. Record what they show for each.
- [ ] In the drone or showcase camera: `COCKPIT` and `EXTERNAL` show neither their On nor their Off image
  (background only), `CAMERA` shows `DRONE`, `SHOWCASE` or a number. Record what you see.

**Stream Deck -> sim (press the key)**
- [ ] `TRIM UP`: count the presses until `TRIM` changes by about 1 (or until you see the wheel move), and
  record the number. Does the cockpit trim wheel turn, and which way (nose up expected)? Do the readouts go
  up?
- [ ] `TRIM DN`: the same, the other way. If the readouts move but the cockpit wheel doesn't, or a step is
  too small to use, record it (the doc's "Command choice" says what happens next).
- [ ] `COCKPIT` (from the external view): the sim camera changes to the cockpit; `COCKPIT` shows On,
  `EXTERNAL` Off, `CAMERA` shows `COCKPIT`. Press it again in the cockpit: nothing changes (it always writes 2).
- [ ] `EXTERNAL` (from the cockpit): the sim camera changes to the external view; `EXTERNAL` shows On,
  `COCKPIT` Off, `CAMERA` shows `CHASE`. Press again: the camera goes back to the cockpit and the key states
  follow (hand-tested 2026-11-11; check it again on the generated key).
- [ ] If `COCKPIT` or `EXTERNAL` does nothing: record it. It becomes Empty and its row in
  aircraft-mappings.md is marked "does not work" (the row stays).

**Controller independence**
- [ ] The trim and view keys work the same with the Xbox Elite controller and with the T.16000M + TWCS
  connected (no key needs a binding on either).

**Results to record**
- [ ] Record which trim and view keys passed each direction, the presses per trim step, the trim wheel
  direction, the camera numbers seen, what `COCKPIT` and `EXTERNAL` did, and every fallback or value change.

## Phase 2: G1000 and V-speeds pages (C172 G1000)

Reference: [docs/phase2-g1000-vspeeds.md](../docs/phase2-g1000-vspeeds.md). These pages are in the same
profile file as the main page, behind `MORE` (main page 4,8). Record: date, MSFS 2024 version, PilotsDeck
version, and every fallback or changed value you used.

**Reimport (no sim needed)**
- [ ] If you changed any key by hand during the earlier tests, write down which key and field first.
- [ ] In the Stream Deck app, export the installed `MSFS2024 C172 G1000` to the backup folder. Then delete
  **every** installed profile of that name, including the app's copies (`MSFS2024 C172 G1000 copy`,
  `MSFS2024 C172 G1000 copy 1`, ...): the Profile Manager finds profiles by name, never keep two.
- [ ] Double-click `pilotsdeck/MSFS2024-XL/_Package/Profiles/MSFS2024 C172 G1000.streamDeckProfile` (pick the
  XL if asked), select `MSFS2024 C172 G1000`. Check its aircraft mapping in the Profile Manager.
- [ ] The main page, the trim page and the views page look as before. `CHECKLIST` still opens a
  back-key-only page.

**Layout and round trip (no sim needed)**
- [ ] `MORE` opens the More page: back key at 1,1, folder keys `PFD` 1,2, `MFD` 1,3, `V-SPEEDS` 1,4,
  everything else empty. Its back key returns to the main page.
- [ ] `PFD` opens the PFD page: back key at 1,1; row 1 `DIRECT`, `MENU`, `FPL`, `PROC`, `CLR`, `CLR HOLD`,
  `ENT`; row 2 `FMS PUSH`, `FMS OUT-`, `FMS OUT+`, `FMS IN-`, `FMS IN+`, `RANGE-`, `RANGE+`, `RNG PUSH`;
  row 3 `SK 1` to `SK 6`; row 4 `SK 7` to `SK 12`; 3,7, 3,8, 4,7, 4,8 empty. Its back key returns to the
  More page (not the main page).
- [ ] `MFD` opens the MFD page with the same layout; its back key returns to the More page.
- [ ] `V-SPEEDS` opens the V-speeds page: back key at 1,1; row 1 `VS0`, `VS1`, `VR`, (1,5 empty), `CLIMB`;
  row 2 (2,1 empty) `CRUISE`, (2,3 empty), `VNE`, `VFE`; everything else empty. Its back key returns to the
  More page.
- [ ] Select a few keys on each page and compare the settings panel with the doc's Key tables (bezel keys:
  Command Type H-Var, the address; readouts: the address, Format `1.0`). Record every key that differs,
  with the field. Record how the folder keys look.

**Diagnostic first**
- [ ] Flight loaded, PFD and MFD on: look at the plugin log (`log\PilotsDeck<date>.log`) for the line
  "MobiFlight WASM Client Connection opened" after the flight loaded. H-events need it. Record whether it is
  there.
- [ ] On the ground, flaps up: record what each V-speeds key shows (`VS0`, `VS1`, `VR`, `CLIMB`, `CRUISE`,
  `VNE`, `VFE`). Expected: whole numbers of knots, `VS0` < `VS1` < `VR` < `CLIMB`, `VNE` the highest;
  `CLIMB` and `CRUISE` are the sim's climb and cruise speeds, not the POH Vy and Vc, and `CRUISE` is a true
  airspeed (ktas), so it need not fit the order. A key that shows nothing, `0`, `-1` or another negative
  number (the SDK default when the aircraft's flight_model.cfg does not set it) or about 1.7 times a
  sensible number: record it (the doc's "Fallbacks").

**Sim -> Stream Deck (change it in the sim, don't press the key)**
- [ ] Move the flap handle with the mouse through every position: `VFE` changes with it. Record the number
  at each position, UP included.
- [ ] Take off (or use slew to climb): the design constants (`VS0`, `VS1`, `VR`, `CLIMB`, `CRUISE`, `VNE`) don't
  change in flight.
- [ ] The bezel keys show no state (fixed image), so there is nothing to follow: click a few bezel buttons
  with the mouse and check that the deck keys don't change (they shouldn't).

**Stream Deck -> sim (press the key, watch the G1000)**
- [ ] PFD page, softkeys: press `SK 1` to `SK 12` in turn with the PFD's softkey bar showing. Each press does
  what a mouse click on that softkey does (the label above it on the PFD). Record the keys that do nothing.
- [ ] PFD page, buttons: `MENU`, `FPL`, `PROC`, `DIRECT`, `CLR`, `ENT` each do what a mouse click on that
  bezel button does (try each once with the mouse first, then with the deck); `CLR HOLD` does what holding
  CLR with the mouse for 2 s does.
- [ ] PFD page, knobs: compare each with the mouse on the bezel knob: `FMS OUT-` / `FMS OUT+` (outer ring)
  and `FMS IN-` / `FMS IN+` (inner knob) one step per press, `FMS PUSH` (inner knob push), `RANGE-` /
  `RANGE+` one range step, `RNG PUSH` (range knob push). Record each direction (which of `-` / `+` is
  clockwise on the bezel).
- [ ] MFD page: the same for the MFD (map range, MENU, FPL, PROC, DIRECT, CLR, CLR HOLD, ENT, softkeys, FMS
  knobs, RNG PUSH).
- [ ] For each press that did nothing: check the plugin log for "Running Command (Type: HVAR" with the key's
  address. Record the key, whether the line is there, and any error. The key becomes Empty and its row in
  aircraft-mappings.md is marked "does not work" (the row stays), unless the doc's hand test gives it the
  input-event fallback.
- [ ] Press a V-speeds key: nothing happens (the log shows a warning, as for the views readouts).

**Controller independence**
- [ ] The G1000 and V-speeds keys work the same with the Xbox Elite controller and with the T.16000M + TWCS
  connected (no key needs a binding on either).

**Results to record**
- [ ] Record which bezel keys worked (PFD and MFD separately), the knob directions, what `CLR HOLD` and
  `RNG PUSH` did, every V-speeds number (and `VFE` at each flap position), whether the MobiFlight WASM line
  was in the log, and every fallback or value change.

## Phase 2: Sim rate page (C172 G1000)

Reference: [docs/phase2-sim-rate.md](../docs/phase2-sim-rate.md). The page is in the same profile file as
the main page, behind `SIM RATE` (main page 3,7), and its `1X` key needs the script `XL24-SIMRATE.lua`.
Repaired after the first sim test (P2-6R, not yet sim-tested): on 2026-11-12 `1X`/`2X`/`4X`
(`K:SIM_RATE_SET`) did nothing and `RATE` never stepped down (no press was held 0.5 s). The page now has
the user's layout (2026-11-13): `1X` 1,2, `SLOWER` 1,3, `RATE` 1,4, `FASTER` 1,5; the 2X and 4X keys are
gone. Record: date, MSFS 2024 version, PilotsDeck version, and every fallback or changed value you used.

**Safety first.** If the rate ever runs away (very high or very low), set it back to 1x with the sim's own
sim rate controls (your bindings, Controls > Miscellaneous > "Sim rate"), then record what happened.

**The hand test HT-C (in the profile you have now, before the import below)**

HT-A (the step size) is answered by the user's report: the sim steps by x2 up to 128x (2026-11-13). Nothing
to run for it. HT-C needs no new profile: run it on the sim rate page of the profile you use now (your
local `MSFS2024 C172 G1000 Icons` build). On the ground, parked. Write down what `RATE` shows after every
step.

HT-C, the long press on `RATE` (a way down first):
- [ ] At 1x press `RATE` once: expect `2.00`.
- [ ] Now press and **hold `RATE` a full second**, then let go: expect one step down (`1.00`).
- [ ] The plugin log (`log\PilotsDeck<date>.log`) should show "Key TimeDiff: 00:00:01..." then "Build Long
  Command" and "K:SIM_RATE_DECR".
- [ ] What the results mean: works = `RATE` stays as built. Held at least 0.5 s but no "Build Long Command"
  in the log = the long press is broken in this build (report it; the new `SLOWER` key is the way down). The
  log shows `K:SIM_RATE_DECR` but the rate stays = the sim ignores DECR: stop here and report it (the
  stepping script has no way down then).
- [ ] Record the results of HT-C (each `RATE` value, the log lines) with the other results.

**Install the script (no sim needed)**
- [ ] Copy `pilotsdeck/MSFS2024-XL/_Package/Scripts/XL24-SIMRATE.lua` into
  `%APPDATA%\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\Scripts\` (or install the built
  package with the Profile Manager). Copy it again after any change to it in the repo (P2-6R changed its
  header comment for the new layout, so copy it again now). Without it, `1X` does nothing (the plugin log
  says the script is not registered); `SLOWER`, `RATE` and `FASTER` still work.
  (If the sim rate page was open while you copied it, go back and open the page again.)

**Reimport (no sim needed)**
- [ ] If you changed any key by hand during the earlier tests, write down which key and field first.
- [ ] In the Stream Deck app, export the installed `MSFS2024 C172 G1000` to the backup folder. Then delete
  **every** installed profile of that name, including the app's copies (`MSFS2024 C172 G1000 copy`,
  `MSFS2024 C172 G1000 copy 1`, ...). **Leave the profile named `G1000`**: that is a downloaded generic
  profile, not this project's.
- [ ] Double-click `pilotsdeck/MSFS2024-XL/_Package/Profiles/MSFS2024 C172 G1000.streamDeckProfile` (pick the
  XL if asked), select `MSFS2024 C172 G1000`. Check its aircraft mapping in the Profile Manager.
- [ ] **If you test with the local icon build** (`MSFS2024 C172 G1000 Icons`, as on 2026-11-12): it must be
  rebuilt from the new data first, or it still holds the old keys (and no `FASTER`). Delete
  the `.local\icons` folder, rebuild, and import it as in the checklist section "P2-5: local icon build
  (C172 G1000)" and [docs/icons.md](../docs/icons.md) (delete the old `MSFS2024 C172 G1000 Icons` profiles
  and their copies first). The checks below apply to it the same way.
- [ ] The main page looks as before (3,7 is the folder `SIM RATE`; 4,7 is empty). The other pages look as
  before.

**Layout and round trip (no sim needed)**
- [ ] `SIM RATE` opens the sim rate page: back key at 1,1; row 1 `1X` 1,2, `SLOWER` 1,3, `RATE` 1,4,
  `FASTER` 1,5; everything else empty (1,6 too). Its back key returns to the main page.
- [ ] Select `1X` and compare its settings panel with the doc: Command Type "All Sims: Lua Function", Command
  Address `lua:XL24-SIMRATE:SET(1)`, Value Address `(A:SIMULATION RATE, number)`, On/Off States `1` / `2`.
  Select `RATE`: Value Address as `1X`, Format `1.2`, Main Command `K:SIM_RATE_INCR`, long press on, Second
  Command `K:SIM_RATE_DECR`. Select `SLOWER`: Command Type MSFS: K-Var (SimEvent), Command Address
  `K:SIM_RATE_DECR`, no long press. Select `FASTER`: the same as `SLOWER` but Command Address
  `K:SIM_RATE_INCR`. Record every field that differs or looks different in the panel.

**Diagnostic first**
- [ ] Flight loaded at 1x: `RATE` shows `1.00`, `1X` On. If `RATE` shows nothing or `0`, use the
  `(E:SIMULATION RATE, number)` fallback on `RATE` and record it.
- [ ] Record what the rate keys show while the sim is paused (Esc menu, and active pause if you use it), and
  whether your own sim rate binding changes the rate while paused.

**Sim -> Stream Deck (change it in the sim, don't press a key)**
- [ ] Change the rate with the sim's own control to 2x, 4x, then back to 1x: `RATE` follows (`2.00`,
  `4.00`, `1.00`); `1X` shows its Off image at 2x, **no image** at 4x (only its background and title: the
  expected look, not a fault, see the doc "What the keys show"), and On at 1x.
- [ ] Step to 8x and to 0.5x if the sim allows: `1X` no image (background and title only), `RATE` `8.00` /
  `0.50`. Record anything the sim refuses (for example high rates on the ground) and which control you used.

**Stream Deck -> sim (press the key)**
- [ ] `SLOWER` first: at 2x (or higher) press `SLOWER`: one step down per press, `RATE` follows. At the
  lowest rate it does nothing more (`RATE` `0.06`).
- [ ] `FASTER`: at 1x press `FASTER`: one step up per press (`2.00`, `4.00`, ...), `RATE` follows. Then press
  `SLOWER` back to 1x.
- [ ] `RATE`: a short press is one step up; **hold a full second** for one step down. `RATE` shows each
  new rate.
- [ ] From 16x or higher (step up with `FASTER`) press `1X`: the rate steps down to 1x one step at a time,
  `1X` On. Record roughly how long it took.
- [ ] From 0.25x (step down with `SLOWER`) press `1X`: the rate steps up to 1x, `1X` On.
- [ ] At 1x press `1X`: nothing happens (already 1x). From 8x press `1X` twice quickly: the second press is
  ignored while the first run is still stepping; the rate ends at 1x. Record what happens.

**The script's stop cases (check `log\lua.log` after each)**
- [ ] At 4x pause the sim, then press `1X`: record what happens. If the rate can't change while paused, the
  script stops after 2 s and `lua.log` has a line "XL24-SIMRATE: rate stayed 4, stopped" (the number as
  Lua prints it); nothing else happens.
- [ ] For a press that did nothing or gave a wrong rate: the plugin log line "Running Command" for that key
  (`lua:XL24-SIMRATE:SET(1)`, or `K:SIM_RATE_...` for `RATE` / `SLOWER` / `FASTER`), any "not registered"
  warning, and every `XL24-SIMRATE:` line in `lua.log`. "Not registered" = the script is not in the Scripts
  folder.
- [ ] A press at the moment the page opens (`RATE` still blank) may log `XL24-SIMRATE: no rate read, stopped`:
  press again.

**Controller independence**
- [ ] The sim rate keys work the same with the Xbox Elite controller and with the T.16000M + TWCS connected
  (no key needs a binding on either).

**Results to record**
- [ ] Record HT-C's results, each key's result in both directions, the script stop cases and their
  `lua.log` lines, what the keys show while paused, the 8x / 0.5x observations, the sim version, and every
  fallback or value change.

## P2-5: local icon build (C172 G1000)

Reference: [docs/icons.md](../docs/icons.md). A second profile, `MSFS2024 C172 G1000 Icons`, with key images
from the Guenseli icon pack. **Personal and private use only:** never commit, upload or share `.local/`, the
icon profile, or an export of it. The committed `MSFS2024 C172 G1000` profile is not changed; keep only
one of the two installed (docs/icons.md section 2). Record: date, Stream Deck app version, PilotsDeck
version, MSFS 2024 version (sim check only).

**Build and install (no sim needed)**
- [ ] In the repo folder: `python tools/profilegen/generate.py --icons tools/profilegen/icons-c172-g1000.json`.
  It prints the profile path and the image folder (`.local\icons\Images\Guenseli-C172`, 29 files).
- [ ] Copy the folder `.local\icons\Images\Guenseli-C172` (File Explorer) into
  `%APPDATA%\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\Images\` (result:
  `...\Images\Guenseli-C172\*.png`, 29 files). This is your own hand step, the plugin's documented way to add
  images (PilotsDeck README 3.3); it is a file copy, not a settings edit, and touches none of the patched
  plugin's program files. **Never re-run the PilotsDeck installer to "fix" icons** (it would undo the
  patched build: #176, docs/installation.md).
- [ ] Quit and restart the Stream Deck app (not as administrator). Do this BEFORE importing or opening any
  key's settings: a key whose image is missing gets its image field reset when its settings panel opens.
- [ ] Import `.local\icons\MSFS2024 C172 G1000 Icons.streamDeckProfile` (double-click, pick the XL if asked).
  It appears as `MSFS2024 C172 G1000 Icons`; delete `MSFS2024 C172 G1000` if it is installed (keep only one,
  docs/icons.md section 2). Switch the XL to it.

**Look test, page by page (no sim needed)** (do it with MSFS closed, or after the flight has fully loaded,
not while the sim loads. The plugin's Wait image (a dark square with three dots, the same image keys show
while the sim loads) then means that key's file is not in the plugin's Images folder; note the key)
- [ ] Main: BAT red rocker; FUEL PMP, NAV LT, BCN, STRB, LDG, TAXI, PITOT white rockers; PARK the
  parking-brake handle; AP, HDG, ALT, VS, NAV, APR, FLC, FD dark G1000 buttons; RPM, GEAR, FLAPS, XPDR, CDI,
  BARO dark display face; ATC dark button; MAP map icon; COM1 unchanged; folders TRIM (grey Garmin), VIEWS
  (green, aircraft), SIM RATE (Flight Simulator logo), CHECKLIST (brown Garmin), MORE (green folder), each
  with its title and each still opening its page.
- [ ] Each child page: the back key (1,1) shows the green "out" folder icon and still goes back. If it shows
  the plain default arrow instead (A-3), note it; nothing else is affected.
- [ ] Trim: TRIM UP / TRIM DN arrows; TRIM and TRIM DEG readouts. Views: COCKPIT / EXTERNAL buttons, CAMERA /
  VIEW / VIEW NO readouts. More: PFD (yellow Garmin, corner left), MFD (yellow Garmin, corner right),
  V-SPEEDS (green Garmin). PFD and MFD: DIRECT with the D-arrow; MENU, FPL, PROC, CLR, CLR HOLD, ENT blank
  G1000 keys; FMS knobs with turn arrows; RANGE joystick with - / +; RNG PUSH knob; SK 1 to SK 12 dark
  softkeys. V-speeds: seven readouts. Sim rate: SLOWER and FASTER blank G1000 keys, RATE readout; 1X shows its
  button with the flight loaded at 1x, and only its title with MSFS closed (expected, as at 4x).
- [ ] A-5: DIRECT and FMS OUT- (PFD page) and the PFD folder (More page) look sharp and whole, not cropped.
- [ ] A-8: every title is readable on its icon, and every readout's value is readable on its background.
  Note each key that is hard to read.
- [ ] A-6 (taste): note any icon you would rather change (PARK, ATC, MAP, trim arrows, RNG PUSH, folder
  colours, the buttons on COCKPIT/EXTERNAL and 1X, the white rockers). Changes are mapping rows only.

**One short sim check (C172 G1000, flight loaded, icon profile on the XL)**
- [ ] RPM and BARO change as on the committed profile (start the engine, turn the baro knob).
- [ ] AP on: the AP key shows the green bar; AP off: it clears. BAT follows the battery switch (red rocker
  on / off).

**Remove (when you no longer want it)**
- [ ] Delete `MSFS2024 C172 G1000 Icons` in Stream Deck Preferences > Profiles, and delete
  `...\Images\Guenseli-C172` from the plugin's Images folder. The committed profile is untouched throughout.

**Results to record**
- [ ] Record each page's look (the keys with a "wait" image, A-3 back keys, A-5 sharpness, A-8 readability,
  A-6 changes you want) and the sim check results.

## P2-7: title sizes (C172 G1000)

Key titles of Simple and Dynamic Buttons that were saved at 10 are now generated at 14 (`generate.py`; the
same sizes in the committed profile and in the icon build). Readout keys (COM Radio, Display Value) keep their
size, because they draw their values with the title font: COM1 stays 10. Where a title does not fit at 14, a
`title_size` line in `tools/profilegen/c172-g1000.json` sets another size: RNG PUSH (PFD and MFD) and
EXTERNAL 13, FUEL PMP 14 (was 15). Keys at 15 (readouts, BAT, PARK and the switches like them) and folder and
back keys at 12 are unchanged. The main page folder keys VIEWS, CHECKLIST and MORE now have their titles in
the middle of the key (`"title_align": "middle"` in the data file, as your own edit); every other key keeps
its title alignment. No sim needed. Record: date, Stream Deck app version.

- [ ] In the Stream Deck app, Preferences > Profiles: delete the old `MSFS2024 C172 G1000 Icons` profile
  ([docs/icons.md](../docs/icons.md) section 3). This drops your hand size edits; the new build has its own
  sizes, and now has the middle titles on VIEWS, CHECKLIST and MORE that you had set by hand.
- [ ] Delete `.local\icons`, then rebuild: `python tools/profilegen/generate.py --icons
  tools/profilegen/icons-c172-g1000.json` (docs/icons.md section 1). The 23 images are unchanged: the plugin's
  `Images\Guenseli-C172` folder stays as it is.
- [ ] Import `.local\icons\MSFS2024 C172 G1000 Icons.streamDeckProfile`, switch the XL to it, then check each
  page: main, Trim, Views, More, PFD, MFD, V-speeds, Sim rate.
  - [ ] Titles at 14 are readable.
  - [ ] RNG PUSH and EXTERNAL (13), FUEL PMP (14), CLR HOLD, FMS PUSH and TRIM DEG sit fully inside the key.
  - [ ] Readouts look as before: COM1 frequencies (10), and the Display Value keys at 15 (main RPM, XPDR,
    GEAR, CDI, FLAPS, BARO; Trim TRIM, TRIM DEG; Views CAMERA, VIEW, VIEW NO; Sim rate RATE; V-speeds VS0,
    VS1, VR, VFE, VNE, CRUISE, CLIMB).
  - [ ] VIEWS, CHECKLIST and MORE on the main page show their titles in the middle of the key; TRIM, SIM RATE,
    the More page's PFD, MFD, V-SPEEDS and the back keys keep theirs at the bottom. Say if you want other
    folder titles in the middle too.
  - [ ] No key changed function (titles, images and folders as before).
- [ ] FUEL PMP is 14 (you had set it to 11 by hand) and COM1 stays 10: say if you want either changed.
- [ ] (Optional) The committed `MSFS2024 C172 G1000` profile has the same new sizes and the same middle titles
  on VIEWS, CHECKLIST and MORE when you next import it (reimport as in the Reimport steps above).
- [ ] Report any title cut off or still too small, by page and title (a different size is one data-file line).

## Phase 2: COM1 pad (C172 G1000)

Reference: [docs/phase2-com1-pad.md](../docs/phase2-com1-pad.md). The page is in the same profile file as the
main page, behind MORE 1,5 `COM PAD`, and needs the script `XL24-COMPAD.lua`. Not yet tested in the app or
the sim. Record: date, MSFS 2024 version, PilotsDeck version, and every fallback or changed value you used.

**Install the script (no sim needed)**
- [ ] Copy `pilotsdeck/MSFS2024-XL/_Package/Scripts/XL24-COMPAD.lua` into
  `%APPDATA%\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\Scripts\` (or install the built
  package with the Profile Manager). Copy it again after any change to it in the repo.

**Reimport (no sim needed)**
- [ ] As in the Sim rate section's Reimport steps: export the installed `MSFS2024 C172 G1000` to the backup
  folder, delete every installed profile of that name (and its `copy` versions; leave the profile named
  `G1000`), double-click the generated profile, select it, check its aircraft mapping.
- [ ] The main page and the other pages look as before; the More page now has a fourth folder key,
  `COM PAD` at 1,5.

**Layout and round trip (no sim needed)**
- [ ] `COM PAD` opens the pad: back key 1,1; `COM1` 1,2; `ENTRY` 1,3; `STBY ID` 2,2; digits `7 8 9` at
  1,6-1,8, `4 5 6` at 2,6-2,8, `1 2 3` at 3,6-3,8; `CLR` 4,6, `0` 4,7, `ENT` 4,8; everything else empty.
  Its back key returns to MORE.
- [ ] Select `7` and compare its settings panel with the doc: Command Type "All Sims: Lua Function", Command
  Address `lua:XL24-COMPAD:DIGIT(7)`. Select `ENT`: Main Command `lua:XL24-COMPAD:ENTER`, long press on,
  Second Command `lua:XL24-COMPAD:ENTER_SWAP`. Select `ENTRY`: Value Address `X:XL24_COMPAD_ENTRY`.
  Record every field that differs or looks different in the panel.

**Typing (flight loaded; the script only runs while the sim is connected)**
- [ ] On opening the pad, `ENTRY` shows `___.___`. If it shows nothing or `0` until the first key, record it.
- [ ] Type `1 1 8 5`: `ENTRY` shows `1__.___`, `11_.___`, `118.___`, `118.5__`.
- [ ] Type `4` as the second digit (`1 4`): ignored, `ENTRY` stays `1__.___`. `CLR` deletes one digit;
  long `CLR` (>= 0.5 s) clears all.
- [ ] Leave the pad (back key) and open it again: `ENTRY` is empty again.
- [ ] If `ENTRY` never changes while you type: plugin log `log\PilotsDeck<date>.log` ("Running Command" for
  `lua:XL24-COMPAD:DIGIT(...)`, any "not registered" warning) and `log\lua.log`. "Not registered" = the
  script is not in the Scripts folder. If the commands run but `ENTRY` doesn't change, use the ENTRY
  fallback in the doc and record it.

**Stream Deck -> sim (press ENT)**
- [ ] Type `1 1 8 5`, press `ENT`: COM1 standby on the PFD and on the pad's `COM1` key becomes 118.500;
  `ENTRY` clears; `lua.log` says "XL24-COMPAD: COM1 standby set to 118500000 Hz".
- [ ] Type `1 2 1 5 2`, press `ENT`: standby 121.525 (25 kHz mode). Record the radio's spacing mode if you
  can see it (8.33 / 25 kHz); in 8.33 mode it should be 121.520.
- [ ] Type `1 2 4 3 5`, **long press** `ENT`: 124.350 becomes **active**, the old active goes to standby.
- [ ] Type `1 3 7`: the 7 is ignored (after 13 only 0 to 6 are allowed), `ENTRY` shows `13_.___`. Clear it,
  type `1 1 8`, press `ENT`: standby becomes 118.000 (missing decimals are zeros).
- [ ] `STBY ID` shows a station ident for a frequency that has one (for example the local ATIS), or record
  that it shows nothing (then it becomes Empty).
- [ ] (If the G1000 offers 8.33 kHz mode) set it, enter `1 1 8 0 0 5`, press `ENT`, record what the radio shows.

**Sim -> Stream Deck (change it in the sim, don't press a key)**
- [ ] Turn the G1000 COM knob: the pad's `COM1` key standby follows; press the G1000 swap button: the
  key follows. Press `COM1` on the pad: active and standby swap in the sim.

**Controller independence**
- [ ] The pad works the same with the Xbox Elite controller and with the T.16000M + TWCS connected.

**Results to record**
- [ ] Record each step's result, the log lines for any step that failed, the spacing mode, the 8.33 result
  if tried, what `STBY ID` showed, the sim version, and every fallback or change.

## P3-1: Autopilot page (C172 G1000)

Reference: [docs/phase3-autopilot.md](../docs/phase3-autopilot.md). The page is in the same profile file as
the main page, behind MORE 1,6 `AUTOPILOT`. No script to install. Not yet tested in the app or the sim.
Record: date, MSFS 2024 version, PilotsDeck version, and every fallback or changed value you used.

**Reimport (no sim needed)**
- [ ] As in the Sim rate section's Reimport steps: export the installed `MSFS2024 C172 G1000` to the backup
  folder, delete every installed profile of that name (and its `copy` versions; leave the profile named
  `G1000`), double-click the generated profile, select it, check its aircraft mapping. For the local icon
  profile, rebuild it first as [docs/icons.md](../docs/icons.md) says (delete `.local\icons`, rebuild, replace
  the plugin's `Images\Guenseli-C172` folder, restart the app, import).
- [ ] The main page and the other pages look as before; the More page now has a fifth folder key,
  `AUTOPILOT` at 1,6.

**Layout and round trip (no sim needed)**
- [ ] `AUTOPILOT` opens the page: back key 1,1; row 1 `AP FD HDG NAV APR BC VNV` (1,2-1,8); column 1 `ALT`
  2,1, `VS` 3,1, `FLC` 4,1; `HDG+ CRS+ ALT+ VS+ SPD+` at 2,2-2,6; readouts `HDG BUG CRS1 ALT SEL VS TGT FLC SPD`
  at 3,2-3,6; `HDG- CRS- ALT- VS- SPD-` at 4,2-4,6; everything else empty (2,7 and 3,7 are reserved for YD
  and LVL, which this aircraft lacks). Its back key returns to MORE.
- [ ] Select `ALT+` and compare its settings panel with the doc: Command `K:AP_ALT_VAR_INC`, long press on,
  Second Command `K:AP_ALT_VAR_INC:1000`. Select `VNV`: Command `B:as1000_autopilot_vertical_navigation_pfd`,
  On `1` / Off `0`, Value Address `L:XMLVAR_VNAVButtonValue`. Select `HDG BUG`: Value Address
  `(A:AUTOPILOT HEADING LOCK DIR, Degrees)`, Format `3.0:%s°`. Record every field that differs. Select
  `VS TGT`: Value Address `(A:AUTOPILOT VERTICAL HOLD VAR, Feet/minute)`, Format `1.0`; the settings panel may
  draw that field red while it has focus (its pattern has no `/` in the unit; the plugin itself accepts it):
  leave it, don't retype it.

**In the air (flight loaded, engine running, about 5000 ft, AP off first)**
- [ ] 1. AP: press -> AP engages on the PFD, key lit; press again -> off, dark. Click the cockpit AP button:
  the key follows.
- [ ] 2. FD: press -> FD bars shown, key lit; again -> off, dark (with AP on, the sim may keep FD on: note it).
- [ ] 3. HDG: with AP on, press -> the PFD shows HDG, key lit; press again -> dark. Click the cockpit HDG
  button: the key follows.
- [ ] 4. `HDG BUG` = the PFD's HDG box (if not, record both values: fallback `:1` index, A-5). `HDG+` / `HDG-`
  -> bug and readout +1 / -1 per press; step across 360/000. Press `HDG BUG` -> the bug jumps to the current
  heading (sync; if nothing happens, record it: fallback `K:AP_HDG_CURRENT_HDG_SET:1`).
- [ ] 5. `ALT SEL` = the selected altitude above the PFD altitude tape (if not, or if it does not follow
  `ALT+` / `ALT-`, record both values: fallback `:1` index, A-5). `ALT+` / `ALT-` -> +/-100 ft per press
  (record the real step). Then **hold** `ALT+` a full second and record what happens: +1000 ft is the expected
  result; **if the selected altitude jumps to 1000 ft instead** (A-4: the SDK calls the parameter "New
  reference altitude"), say so, set it back with short presses, and don't use the long press until the repair
  (ten single steps per long press, or no long press). Same for `ALT-`. `ALT`: press -> ALT hold lit; again ->
  dark.
- [ ] 6. VS: press -> the PFD shows VS with a target, key lit; `VS+` / `VS-` change `VS TGT` and the PFD
  target (record the step, likely 100 fpm; a descent shows `-`, a climb shows no `+`). Press VS again -> dark.
- [ ] 7. FLC: note `FLC SPD` first; press FLC -> FLC lit; record whether the target speed jumped to the
  current IAS (A-9: the key doesn't set it, the cockpit button does); `SPD+` / `SPD-` change `FLC SPD` and
  the PFD target (record the step). Press FLC again -> dark.
- [ ] 8. NAV / APR / BC: tune a VOR/ILS (or CDI GPS with a flight plan); NAV -> lit when the PFD shows NAV
  armed or active (record which: A-8); APR and BC the same on a localizer; each press again -> dark.
- [ ] 9. `CRS1` = the PFD CRS (in VLOC mode). `CRS+` / `CRS-` -> +/-1 degree; hold a full second -> +/-10
  degrees; press `CRS1` -> the CDI centres (course to the station). In GPS mode record what the CRS keys do.
  With the CDI on NAV2 (if tuned), record what `CRS+` / `CRS-` and the `CRS1` readout do (the long press and
  the readout are NAV1 only).
- [ ] 10. VNV (weak source, A-6: the read `L:XMLVAR_VNAVButtonValue` comes from a general-path SDK template
  page and a pre-2024 profile only): with a flight plan with altitudes, press -> VNV on the PFD, key lit;
  again -> dark; press it four more times and record whether every press toggles VNV or only every second one
  (fallback: the Reset Switch, A-6); click the cockpit VNV button: does the key follow? Record each of the
  three separately (press works / key lights / key follows the cockpit).
- [ ] 11. Turn each mode off from the cockpit with the mouse and check its key goes dark; the readouts follow
  the cockpit knobs (HDG, CRS, ALT, VS wheel) without a key being pressed.
- [ ] 12. No flight loaded (sim at the main menu): the page opens and every key shows the plugin's Wait image,
  no mode key lit (phase2-main-page.md, "What the keys show when the sim isn't there"). Record what the
  readouts show.

**scmon checks (Admin account, optional; [tools/scmon/README.md](../tools/scmon/README.md))**
- [ ] Build once:
  `& "$env:LOCALAPPDATA\Microsoft\dotnet\dotnet.exe" build "A:\FS2024 Stuff\msfs2024-streamdeck-xl\tools\scmon\scmon.csproj" -c Release -o "$env:TEMP\scmon-bin"`.
- [ ] VNV: `& "$env:LOCALAPPDATA\Microsoft\dotnet\dotnet.exe" "$env:TEMP\scmon-bin\scmon.dll" 180 L:XMLVAR_VNAVButtonValue`,
  then click the cockpit VNV button a few times: does the `plugin L:XMLVAR_VNAVButtonValue=` value change
  0/1? Repeat with `B:as1000_autopilot_vertical_navigation_pfd` as the second argument (does the B-Var have
  a value to read?). `AP=...` in the same lines shows AP master.
- [ ] A readout that disagrees with the PFD (`HDG BUG`, `ALT SEL`): report it for a later scmon run with the
  index `:1`.

**Controller independence**
- [ ] The page works the same with the Xbox Elite controller and with the T.16000M + TWCS connected.

**Results to record**
- [ ] Record each step's result, the real steps (HDG, CRS, ALT short and long, VS, SPD), the ALT long-press
  outcome (step or set), the VNV three answers, whether FLC took the current IAS, armed versus active for
  NAV/APR, the sim version, and every fallback or change.

## P3-2: Transponder page (C172 G1000)

Reference: [docs/phase3-transponder.md](../docs/phase3-transponder.md). The page is in the same profile file
as the main page, behind MORE 1,7 `XPDR`, and needs the script `XL24-XPDRPAD.lua`. Not yet tested in the app
or the sim. Record: date, MSFS 2024 version, PilotsDeck version, and every fallback or changed value you used.

**Install the script (no sim needed)**
- [ ] Copy `pilotsdeck/MSFS2024-XL/_Package/Scripts/XL24-XPDRPAD.lua` into
  `%APPDATA%\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\Scripts\` (as the COM1 pad's
  script, [docs/phase2-com1-pad.md](../docs/phase2-com1-pad.md), "Install the script"). Copy it again after
  any change to it in the repo.

**Reimport (no sim needed)**
- [ ] As in the P3-1 section's Reimport steps: export the installed `MSFS2024 C172 G1000` to the backup
  folder, delete every installed profile of that name (and its `copy` versions; leave the profile named
  `G1000`), double-click the generated profile, select it, check its aircraft mapping. For the local icon
  profile, rebuild it first as [docs/icons.md](../docs/icons.md) says.
- [ ] The main page and the other pages look as before; the More page now has a sixth folder key, `XPDR`
  at 1,7.

**Layout and round trip (no sim needed)**
- [ ] `XPDR` opens the page: back key 1,1; readouts `XPDR ENTRY MODE` at 1,2-1,4; `STBY ON ALT` at 2,2-2,4;
  `IDENT` 3,2, `VFR` 3,3; digits `7` at 1,6, `4 5 6` at 2,6-2,8, `1 2 3` at 3,6-3,8; `CLR` 4,6, `0` 4,7,
  `ENT` 4,8; everything else empty (no 8 and 9). Its back key returns to MORE.
- [ ] Select `ALT` and compare its settings panel with the doc: Command Type A-Var, Command Address
  `(A:TRANSPONDER STATE:1, Enum)`, On Value `$=4`, Off Value empty; Value Address the same, On/Off States
  `4` / `1`. Select `CLR`: Main Command `lua:XL24-XPDRPAD:BACK`, long press on, Second Command
  `lua:XL24-XPDRPAD:CLEAR`. Select `XPDR`: Decode BCD on, Format `4.0`. Record every field that differs.

**In the sim (flight loaded, battery and avionics on)**
- [ ] 1. `XPDR` = the code in the PFD's XPDR box; `MODE` = the PFD's transponder mode (STBY / ON / ALT).
  Record what `MODE` shows on the ground.
- [ ] 2. Type `7 0 0 0`: `ENTRY` shows `7___` ... `7000`; press `ENT` -> the PFD code becomes 7000, `XPDR`
  shows `7000`, `ENTRY` clears. `CLR` deletes one digit; hold `CLR` a full second -> the entry clears.
  `ENT` with 3 digits -> nothing is sent (`lua.log` line "need 4 digits"). Leave the page and open it
  again: `ENTRY` is empty.
- [ ] 3. `VFR` -> code 1200 on the PFD and on `XPDR`.
- [ ] 4. `STBY` / `ON` / `ALT` -> **the PFD's own XPDR mode display** changes to that mode, `MODE` follows,
  and the pressed key is lit. Check the PFD itself, not only `MODE`: the G1000 can hold its own mode and set
  the SimVar back. A key that changes `MODE` (the SimVar) but not the PFD's mode display **fails** this
  step: record what the PFD and `MODE` showed; the repair then empties the three keys and the PFD softkeys
  set the mode (A-4). On the ground the transponder may go to its ground mode after `ALT` (the PFD and
  `MODE` show `GND`, SDK enum 5): record that and repeat `ALT` in the air before you count the key as
  failed. Then change the mode with the PFD softkeys (XPDR, then STBY / ON / ALT): `MODE` and the keys
  follow.
- [ ] 5. `IDENT` -> the PFD shows IDENT, the key is lit about 18 s, then dark. Also press the PFD's IDENT
  softkey: the key follows.
- [ ] 6. No flight loaded (sim at the main menu): the page opens; readouts empty (or the plugin's Wait
  image); no key lit.
- [ ] If the pad keys do nothing: plugin log `log\PilotsDeck<date>.log` ("Running Command" for
  `lua:XL24-XPDRPAD:...`, any "not registered" warning) and `log\lua.log`. "Not registered" = the script is
  not in the Scripts folder.

**Controller independence**
- [ ] The page works the same with the Xbox Elite controller and with the T.16000M + TWCS connected.

**Results to record**
- [ ] Record each step's result, what `MODE` showed on the ground, for step 4 what the PFD's mode display
  and `MODE` showed for each key, the log lines for any step that failed, the sim version, and every fallback
  or change.

## P3-2b: Radios page (C172 G1000)

Reference: [docs/phase3-radios.md](../docs/phase3-radios.md). The page is in the same profile file as the
main page, behind MORE 1,8 `RADIOS`; it needs no script. Not yet tested in the app or the sim. Record: date,
MSFS 2024 version, PilotsDeck version, and every fallback or changed value you used.

**Reimport (no sim needed)**
- [ ] As in the P3-1 section's Reimport steps: export the installed `MSFS2024 C172 G1000` to the backup
  folder, delete every installed profile of that name (and its `copy` versions; leave the profile named
  `G1000`), double-click the generated profile, select it, check its aircraft mapping. For the local icon
  profile, rebuild it first as [docs/icons.md](../docs/icons.md) says.
- [ ] The main page and the other pages look as before; the More page now has a seventh folder key,
  `RADIOS` at 1,8.

**Layout and round trip (no sim needed)**
- [ ] `RADIOS` opens the page: back key 1,1; `NAV1 NAV1 ID NAV2 NAV2 ID COM2 COM2 ID` at 1,2-1,7;
  `MHZ+ KHZ+` under each radio at 2,2-2,7 and `MHZ- KHZ-` at 3,2-3,7; `MIC1` 4,6, `MIC2` 4,7; everything
  else empty. Its back key returns to MORE.
- [ ] Select `NAV1` and compare its settings panel with the doc: COM Radio, Active
  `(A:NAV ACTIVE FREQUENCY:1, MHz)`, Standby `(A:NAV STANDBY FREQUENCY:1, MHz)`, Format `2`, Command
  `K:NAV1_RADIO_SWAP`. Select `MIC2`: Command `K:PILOT_TRANSMITTER_SET:1`, Value Address
  `(A:COM TRANSMIT:2, Bool)`. Record every field that differs.

**In the sim (flight loaded, battery and avionics on)**
First write down the NAV1, NAV2 and COM2 active and standby frequencies and which MIC light is on. Way back
after each step: swap back with a second press, step back with the opposite key (or tune on the G1000 with the
mouse), and press the MIC key that was lit before.
- [ ] 1. `NAV1` key: top = the PFD's NAV1 active frequency, bottom = NAV1 standby; `NAV2` the same for NAV2;
  `COM2` = the PFD's COM2 active and standby. If `NAV1` shows NAV2's frequencies (or none), record it
  (index, **A-6**). Press each -> that radio swaps on the PFD, and the key follows.
- [ ] 2. `MHZ+` / `MHZ-` / `KHZ+` / `KHZ-` under each radio: record **which frequency changes** (standby
  expected, **A-7**), **the step** (NAV 50 kHz expected; COM2 25 kHz or 8.33 kHz, **A-8**) and the wrap at
  117.95 / 108.00 (NAV) and 136.975 / 118.000 (COM2).
- [ ] 3. Idents: tune a VOR in range -> `NAV1 ID` / `NAV2 ID` show its ident; `COM2 ID` shows the tuned
  station (it may stay empty: record it; the repair then makes the key Empty).
- [ ] 4. `MIC1` / `MIC2` -> the audio panel's COM1 MIC / COM2 MIC light moves and the lit key follows
  (**A-9**); press the audio panel's MIC buttons with the mouse: the keys follow.
- [ ] 5. Turn the G1000's NAV and COM knobs with the mouse (and use its swap buttons): the readouts follow
  without a key press.
- [ ] 6. No flight loaded (sim at the main menu): the page opens; readouts empty (or the plugin's Wait
  image); no key lit.
- [ ] scmon (Admin; [tools/scmon/README.md](../tools/scmon/README.md)), **only if step 4 fails** (A-9): build
  it once with
  `& "$env:LOCALAPPDATA\Microsoft\dotnet\dotnet.exe" build "A:\FS2024 Stuff\msfs2024-streamdeck-xl\tools\scmon\scmon.csproj" -c Release -o "$env:TEMP\scmon-bin"`,
  then run
  `& "$env:LOCALAPPDATA\Microsoft\dotnet\dotnet.exe" "$env:TEMP\scmon-bin\scmon.dll" 180 B:as1000_com_2_mic_midcom`
  and click the audio panel's COM2 MIC button: does the `plugin B:as1000_com_2_mic_midcom=` value change (a
  readable B-Var for the fallback)? Radio SimVars are not in scmon's list; the page's own readouts are the
  monitor.

**Which results decide the open points**
- A-6 (radio indexes): step 1. A-7 (standby or active): step 2, which frequency changes. A-8 (kHz step):
  step 2, the step size. A-9 (mic select): step 4, and the scmon check if step 4 fails.

**Controller independence**
- [ ] The page works the same with the Xbox Elite controller and with the T.16000M + TWCS connected.

**Results to record**
- [ ] Record each step's result, for step 2 which frequency changed and by how much for each radio, the log
  lines for any step that failed, the sim version, and every fallback or change.

## P3-3: Systems page (C172 G1000)

Reference: [docs/phase3-systems.md](../docs/phase3-systems.md). The page is in the same profile file as the
main page, behind MORE 2,2 `SYSTEMS`; it needs no script. Not yet tested in the app or the sim. Record: date,
MSFS 2024 version, PilotsDeck version, and every fallback or changed value you used.

**Reimport (no sim needed)**
- [ ] As in the P3-1 section's Reimport steps: export the installed `MSFS2024 C172 G1000` to the backup
  folder, delete every installed profile of that name (and its `copy` versions; leave the profile named
  `G1000`), double-click the generated profile, select it, check its aircraft mapping. For the local icon
  profile, rebuild it first as [docs/icons.md](../docs/icons.md) says.
- [ ] The main page and the other pages look as before; the More page now has an eighth folder key,
  `SYSTEMS` at 2,2 (the first key of its second row).

**Layout and round trip (no sim needed)**
- [ ] `SYSTEMS` opens the page: back key 1,1; `ALT AVN 1 AVN 2 STBY BAT BUS V BATT A LOAD A` at 1,2-1,8;
  `CABIN 1 CABIN 2 PANEL 1 PANEL 2 PED LT DIMMER` at 2,2-2,7; `LEFT BOTH RIGHT FUEL SEL FUEL VLV` at 3,2-3,6;
  `FUEL L FUEL R FUEL TOT` at 4,2-4,4; everything else empty. Its back key returns to MORE.
- [ ] Select `ALT` and compare its settings panel with the doc: Dynamic Button, Command Type B-Var,
  "Run as Command" unchecked, Command Address and Value Address `B:electrical_alternator_1`, On `1` / Off `0`,
  Special State on with Any Value. Select `BOTH`: Command and Value Address `B:fuel_selector_1`, On Value `2`,
  Off Value `2`, image states On `2` / Off `1`, Special State off. Select `FUEL SEL`: Value Address
  `(A:FUELSYSTEM JUNCTION SETTING:1, Number)`, Mappings `1=LEFT:2=BOTH:3=RIGHT`. Record every field that differs.

**First, the fuel selector values (scmon, A-4)**
- [ ] scmon (Admin; [tools/scmon/README.md](../tools/scmon/README.md)): build it once with
  `& "$env:LOCALAPPDATA\Microsoft\dotnet\dotnet.exe" build "A:\FS2024 Stuff\msfs2024-streamdeck-xl\tools\scmon\scmon.csproj" -c Release -o "$env:TEMP\scmon-bin"`,
  then, with the flight loaded, run
  `& "$env:LOCALAPPDATA\Microsoft\dotnet\dotnet.exe" "$env:TEMP\scmon-bin\scmon.dll" 180 B:fuel_selector_1`
  and turn the cockpit fuel selector with the mouse through LEFT, BOTH and RIGHT: record the
  `plugin B:fuel_selector_1=` value in each position. These are the On/Off values the three selector keys need
  (expected `1` / `2` / `3`). Do the same for any key that does not follow in the steps below:
  `B:electrical_battery_stby_2` (each switch position), `B:lighting_panel_1` / `B:lighting_panel_2` (the knob
  range), `B:lighting_potentiometer_5`. scmon's SimVar list does not hold these systems SimVars; the page's
  own readouts are the monitor.

**In the sim (2024 C172 G1000, flight loaded, parked, engine off unless a step says)**
Way back after each step: press the key again (or set the cockpit control back with the mouse); leave the
fuel selector on BOTH and the fuel shutoff valve open (fuel on) at the end.
- [ ] 1. Cold and dark: `ALT`, `AVN 1`, `AVN 2`, `STBY BAT` and the five light keys show their Off image (no
  Fault); `FUEL L` / `FUEL R` / `FUEL TOT` = the EIS fuel gauges; `FUEL SEL` and the lit selector key = the
  cockpit selector; `FUEL VLV` lit if the shutoff knob is in (fuel on). Record any Fault image.
- [ ] 2. Main BAT on (main page 1,1): `BUS V` and `BATT A` = the EIS "M BUS" volts and "M BATT" amps (record
  both, **A-6**); `LOAD A` shows a load.
- [ ] 3. `ALT`, `AVN 1`, `AVN 2`, `STBY BAT`: press each -> the cockpit switch moves and the key follows; press
  again -> back. Work each switch with the mouse: the key follows. `AVN 1` / `AVN 2` on -> the G1000 displays
  and radios power (bus 1 / bus 2). `STBY BAT`: record the value in each position (ARM / OFF / TEST; TEST may
  show the Fault image, **A-3**).
- [ ] 4. `CABIN 1`, `CABIN 2`, `PANEL 1`, `PANEL 2`, `PED LT`: press -> record which cockpit light changes (dome,
  flood, panel, pedestal, **A-8**) and whether it goes full on or only to a dim step (a dimmer knob: the key may
  show the Fault image after a mouse turn, **A-3**). Turn the panel dimmer knobs with the mouse: does `DIMMER`
  follow one of them (record which, **A-7**)?
- [ ] 5. Fuel selector: `LEFT`, `BOTH`, `RIGHT` -> the cockpit selector moves, only the pressed key is lit, and
  `FUEL SEL` shows the same word. Turn the selector with the mouse: the keys and `FUEL SEL` follow. Record what
  the two unlit keys show in each position (the doc expects no On or Off image on a key whose Off value is
  not the selector's value, W-5). If a key lights for another position, record the values (scmon check above,
  **A-4**).
- [ ] 6. `FUEL VLV` (**on the ground, engine off; never in flight**, A-5): press -> the shutoff knob pulls out
  (fuel off), the key shows Off; press -> knob in, the key shows On. Leave it ON.
- [ ] 7. Engine running at idle (optional): `BUS V` rises to charging volts with `ALT` on; `ALT` off -> `BATT A`
  shows a discharge.
- [ ] 8. No flight loaded (sim at the main menu): the page opens; the keys show the Wait image.

**Which results decide the open points**
- A-3 (switch values): steps 3 and 4 (the STBY BAT positions, the light switches full on or dimmed, any
  Fault image). A-4 (fuel selector values): the scmon check first, then step 5. A-6 (readout indexes): step 2.
  A-7 (what DIMMER follows): step 4. A-8 (which light each light key drives): step 4.

**Controller independence**
- [ ] The page works the same with the Xbox Elite controller and with the T.16000M + TWCS connected: every
  key is an input event or a SimVar read.

**Results to record**
- [ ] Record each step's result, the scmon values of the fuel selector (and of any other input event
  checked), which light each light key drove, the log lines for any step that failed, the sim version, and
  every fallback or change.

## P3-4: Trim gauge (C172 G1000)

Reference: [docs/phase2-trim-views.md](../docs/phase2-trim-views.md) (trim 3,4, "What each key holds", T9)
and [docs/design-trim-gauge.md](../docs/design-trim-gauge.md). The gauge is a new key on the trim page (main
1,7 `TRIM`), in the same profile file as the main page; it needs no script and only reads a SimVar. The trim
page now also holds 3,4: the Phase 2 section's "everything else empty" and the P2-5 and P2-7 key lists
predate it. Not yet tested in the app or the sim. Record: date, MSFS 2024 version, PilotsDeck version, and
every fallback or changed value you used.

**Reimport and layout (no sim needed)**
- [ ] 1. Export a backup of the installed profile, then rebuild and import the icon profile or package as
  [docs/icons.md](../docs/icons.md) says (or the plain profile, [docs/phase2-main-page.md](../docs/phase2-main-page.md),
  "Import the profile"). Main 1,7 `TRIM` opens the trim page: `TRIM UP` 2,2, `TRIM` 3,2, `TRIM DEG` 3,3,
  the gauge `TRIM` 3,4, `TRIM DN` 4,2. The other pages look as before.
- [ ] Select 3,4 and compare its settings panel with the doc (T9): Display Gauge, Value tab Address
  `(A:ELEVATOR TRIM PCT EX2, percent)`, Minimum `-100`, Maximum `100`; Gauge tab Draw Arc off, Orientation
  Up, Size `52; 12`, Offset `-6; 0`; Center Line on; Indicator yellow; Text on, Format `1.0`; no command.
  Record every field that differs.
- [ ] 2. No flight (sim at the main menu): the trim page opens and 3,4 shows the Wait image (with the sim
  closed, PilotsDeck shows a still preview: the bar with no number is expected).

**In the sim (2024 C172 G1000, flight loaded, parked)**
Way back: at the end, set the trim wheel back with the mouse (neutral, or where it was when the flight
loaded); if the new profile misbehaves, delete it and import the backup exported in step 1.
- [ ] 3. The look: a vertical bar in the middle of 3,4, `TRIM` at the top, a yellow triangle on the bar's
  left edge, a white line across it, the number on the right edge reading bottom to top (**A-TEXT**: say if
  you want the number off). Say whether the size and colors suit (**A-SIZE**).
- [ ] 4. Trim wheel with the mouse fully down, neutral, fully up: the pointer goes to the bottom, the white
  line, the top; the gauge's number equals `TRIM` at 3,2 (rounded). Record the numbers. If the bar grows
  downward instead, record it (**A-ORIENT**). If 3,2 shows only -1 to 1 and the pointer barely moves,
  record it (**A-SCALE**).
- [ ] 5. `TRIM UP` / `TRIM DN` presses: the pointer moves the same way as the 3,2 readout.
- [ ] 6. Pressing the gauge sends nothing: PilotsDeck shows its yellow alert sign on the key for a moment and
  the plugin log notes that no command could be built (expected).
  Nothing depends on the connected flight controls (Xbox Elite or T.16000M + TWCS): the key only reads a
  SimVar.
- [ ] 7. Say whether to keep the gauge at 3,4 or move it to 3,2 in place of the percent readout (**A-POS**).

**Results to record**
- [ ] Record each step's result, the numbers of step 4, the log lines for any step that failed, the sim
  version, and every fallback or change.

## P3-5: Engine and fuel page (C172 G1000)

Reference: [docs/phase3-engine-fuel.md](../docs/phase3-engine-fuel.md) (Key table, "What each key holds", T3
and T9). The page is a new second-level page behind the new folder key MORE 2,3 `ENGINE`, in the same profile
file as the main page; it needs no script and only reads SimVars. The More page now also holds 2,3: the older
sections' MORE key lists predate it. Not yet tested in the app or the sim. Record: date, MSFS 2024 version,
PilotsDeck version, and every fallback or changed value you used.

**Reimport and layout (no sim needed)**
- [ ] 1. Export a backup of the installed profile, then rebuild and import the icon profile or package as
  [docs/icons.md](../docs/icons.md) says (or the plain profile, [docs/phase2-main-page.md](../docs/phase2-main-page.md),
  "Import the profile"). MORE 2,3 `ENGINE` opens the engine page: back 1,1, `RPM` 1,2, `FFLOW` 1,3,
  `OIL PRES` 1,4, `OIL TEMP` 1,5, `EGT` 1,6, `VAC` 1,7, the gauges `FUEL L` 2,2 and `FUEL R` 2,3, `BUS V` 3,2,
  `BATT A` 3,3; everything else empty. The other pages look as before.
- [ ] Select 2,2 `FUEL L` and compare its settings panel with the doc (T9): Display Gauge, Value tab Address
  `(A:FUEL LEFT QUANTITY, Gallons)`, Minimum `0`, Maximum `26`; Gauge tab Draw Arc off, Orientation Right,
  Size `58; 10`; Warning Range off; Text on, Format `1.0`; no command. Record every field that differs.
- [ ] 2. No flight (sim at the main menu): every key on the page shows the Wait image (with the sim closed,
  PilotsDeck shows a still preview).

**In the sim (2024 C172 G1000, flight loaded, parked, cold and dark)**
Way back: at the end, set the fuel and the switches back as they were when the flight loaded; if the new
profile misbehaves, delete it and import the backup exported in step 1.
- [ ] 3. Cold and dark: record every key against the MFD EIS (the EIS is dark: say whether the keys showing
  sim values then suits you, **A-DARK**). FUEL L and FUEL R: the bar and the number against the EIS fuel gauges
  and the systems page's FUEL L / FUEL R readouts (systems 4,2, 4,3). Set the fuel to full in the sim's fuel and
  payload panel and record the numbers (**A-FUELRANGE**: is full `26`?; **A-FUELVAR**: do they read at all?).
- [ ] 4. BAT on (main 1,1), then ALT on (systems 1,2): BUS V and BATT A against the EIS M BUS and M BATT,
  sign included (**A-AMPS**). If they match E BUS or S BATT instead, record it (**A-IDX**).
- [ ] 5. Start the engine; at idle, then at cruise power: RPM, FFLOW, OIL PRES, OIL TEMP, EGT and VAC against
  the EIS (numbers and units: psi, deg F, gph, inHg; a key at `0` while the EIS moves: **A-UNITS**); BUS V and
  BATT A again (alternator charging).
- [ ] 6. Pressing any key changes nothing in the sim (a gauge key shows PilotsDeck's yellow alert sign for a
  moment: expected). Nothing depends on the connected flight controls (Xbox Elite or T.16000M + TWCS): the keys
  only read SimVars.
- [ ] 7. Say whether the horizontal fuel bars suit (**A-BAR**) and whether RPM should stay repeated here
  (**A-RPM**).

**Results to record**
- [ ] Record each step's result, the numbers of steps 3 to 5, the log lines for any step that failed, the sim
  version, and every fallback or change.

## P3-TRIM2: Aileron and rudder trim (C172 G1000)

Reference: [docs/phase2-trim-views.md](../docs/phase2-trim-views.md) (Key table: trim, "What the trim keys
do", T5 and T9, "Fallbacks"). New keys on the trim page (main 1,7 `TRIM`), in the same profile file as the main
page; no script. The C172 G1000 has no cockpit aileron or rudder trim control: the keys send the sim's generic
trim events, and this test decides whether they stay. The trim page no longer has `TRIM` 3,2 and `TRIM DEG`
3,3: skip those keys in the older sections (Phase 2 trim steps, P2-5, P2-7, P3-4 steps 4 and 5: compare with
the gauge's number instead). Not yet tested in the app or the sim. Record: date, MSFS 2024 version, PilotsDeck
version, and every fallback or changed value you used.

**Reimport and layout (no sim needed)**
- [ ] 1. Export a backup of the installed profile, then rebuild and import the icon profile or package as
  [docs/icons.md](../docs/icons.md) says (or the plain profile, [docs/phase2-main-page.md](../docs/phase2-main-page.md),
  "Import the profile"). Main 1,7 `TRIM` opens the trim page: back 1,1, `TRIM UP` 2,2, `AIL L` 2,6, the gauge
  `AIL TRIM` 2,7, `AIL R` 2,8, the gauge `TRIM` 3,4, `RUD L` 3,6, the gauge `RUD TRIM` 3,7, `RUD R` 3,8,
  `TRIM DN` 4,2; everything else empty. The other pages look as before.
- [ ] Select 2,7 `AIL TRIM` and compare its settings panel with the doc (T9): Display Gauge, Value tab Address
  `(A:AILERON TRIM PCT, percent)`, Minimum `-100`, Maximum `100`; Gauge tab Draw Arc off, Orientation Right,
  Size `58; 10`; Center Line on; Indicator yellow; Text on, Format `1.1`; no command. Select 2,6 `AIL L`:
  Simple Button, Command Type MSFS: K-Var (SimEvent), Command Address `K:AILERON_TRIM_LEFT`. Record every field that differs.
- [ ] 2. No flight (sim at the main menu): the trim page opens and the gauges show the Wait image (with the
  sim closed, PilotsDeck shows a still preview).

**In the sim (2024 C172 G1000, flight loaded, parked or in flight)**
Way back: at the end, centre the aileron and rudder trim with the keyboard (J / L, U / O) or the deck keys
until both gauges read `0.0`; if the new profile misbehaves, delete it and import the backup exported in step 1.
- [ ] 3. Flight loaded: record what `AIL TRIM` and `RUD TRIM` show (expected `0.0`). The look: a horizontal
  bar, `AIL TRIM` / `RUD TRIM` at the top, a white center line, a yellow pointer, the number upright below the
  bar. Say whether the size and Format `1.1` suit (**A-BAR2**, **A-FMT**).
- [ ] 4. Keyboard first: press J five times, then L five times; then U five times, then O five times.
  Record what `AIL TRIM` and `RUD TRIM` show after each group (the step size per press, **A-STEP**), and
  whether the aircraft rolls or yaws in flight (**A-EFFECT**).
- [ ] 5. Deck keys, five times each in this order: `AIL L`, `AIL R`, `RUD L`, `RUD R`. Each should move its gauge as J, L, U and O
  did. Record the numbers. A key that moves nothing (the gauge and the sim's trim stay put while the keyboard
  key works) is dropped (**A-EVENTS**). If a left key moves the pointer right, record it (**A-SIGN**). If a
  number stays within -1 to 1 and the pointer barely moves, record it (**A-UNIT**).
- [ ] 6. Pressing a gauge sends nothing: PilotsDeck shows its yellow alert sign on the key for a moment
  (expected). Nothing depends on the connected flight controls (Xbox Elite or T.16000M + TWCS): the keys send
  SimConnect events and the gauges only read SimVars.
- [ ] 7. With `tools/scmon` ([tools/scmon/README.md](../tools/scmon/README.md); a session in the Admin account sets
  it up, with its `Vars` list edited to these 11 SimVars: `AILERON TRIM PCT` and `RUDDER TRIM PCT`, each in
  `percent over 100` and in `percent`; `AILERON TRIM PCT EX1` and `RUDDER TRIM PCT EX1` in `percent over 100`;
  `AILERON TRIM` and `RUDDER TRIM` in `degrees`; `AILERON TRIM DISABLED` and `RUDDER TRIM DISABLED` in `Bool`;
  `ELEVATOR TRIM PCT EX2` in `percent over 100`): repeat steps 4 and 5 and save its output with the results (it
  settles A-UNIT, A-STEP and A-SIGN; a DISABLED value of 1 explains a key that moves nothing).
- [ ] 8. Say whether the page layout suits (**A-POS2**) and, if a pair does nothing in the C172, whether to
  drop it.

**Results to record**
- [ ] Record each step's result, the numbers of steps 3 to 5, the scmon output, the log lines for any step
  that failed, the sim version, and every fallback or change.

## P3-FUELCAP: Fuel gauge scale (C172 G1000)

Reference: [docs/phase3-engine-fuel.md](../docs/phase3-engine-fuel.md) (FUEL L 2,2 and FUEL R 2,3, A-FUELRANGE,
A-FUELVAR, Fallbacks) and [docs/aircraft-mappings.md](../docs/aircraft-mappings.md), "Phase 3 fuel gauge scale
(P3-FUELCAP)". P3-FUELCAP changed no key: the gauges keep `0` to `26` gallons (the G1000 EIS scale), while the
sim's tanks read `28` gallons of capacity. This test shows what a full tank and a part load read. Run it after
P3-5's steps 1 and 2 (the engine page installed). Record: date, MSFS 2024 version, PilotsDeck version.

**In the sim (2024 C172 G1000, flight loaded, parked, engine off)**
Way back: at the end, set the fuel load, BAT and the fuel selector back as they were when the flight loaded.
- [ ] 1. BAT on (main 1,1), so the EIS shows fuel; fuel selector `BOTH` (systems 3,3). Open MORE 2,3 `ENGINE`.
- [ ] 2. In the sim's fuel and payload menu, set both tanks full. Record FUEL L and FUEL R (the number and
  whether the pointer sits at the bar's end), the EIS FUEL QTY L and R, and the systems page's FUEL L 4,2 and
  FUEL R 4,3 (one decimal). Expected: about `26.5` (usable fuel) or `28` (**A-USABLE**); the pointer at the end;
  FUEL L and FUEL R show whole gallons (Format `1.0`: `26` or `27` for about 26.5, `28` for 28).
- [ ] 3. Set both tanks to about half, then the left tank fuller than the right if the menu allows it, then
  both low (about 5 gallons). Record the same values each time. The gauge whose number follows the left tank
  shows which read is left (**A-TANKIDX**, with step 5).
- [ ] 4. Pressing a fuel gauge sends nothing (PilotsDeck's yellow alert sign for a moment: expected). Nothing
  depends on the connected flight controls (Xbox Elite or T.16000M + TWCS): the gauges only read SimVars.
- [ ] 5. With `tools/scmon` ([tools/scmon/README.md](../tools/scmon/README.md); a session in the Admin account sets
  it up, with its `Vars` list edited to these 13 SimVars, all in `Gallons`: `FUEL LEFT QUANTITY`, `FUEL RIGHT
  QUANTITY`, `FUEL LEFT CAPACITY`, `FUEL RIGHT CAPACITY`, `UNUSABLE FUEL TOTAL QUANTITY`, and for tanks 1 and 2
  each `FUELSYSTEM TANK QUANTITY`, `FUELSYSTEM TANK TOTAL QUANTITY`, `FUELSYSTEM TANK CAPACITY`, `FUELSYSTEM
  TANK USABLE CAPACITY` (`:1`, `:2`); 13 of its 16 slots): repeat steps 2 and 3 and save its output with
  the results. A SimConnect exception for a name means the aircraft does not have it: record it.
- [ ] 6. Say whether the scale suits you: keep `0` to `26` (the EIS scale; a full tank pins at the end), or
  `0` to `28` (the sim's capacity; the pointer reaches the end only at `28`) (**A-SCALE**).

**Results to record**
- [ ] Record each step's numbers, the scmon output, the sim version and the scale you want.

## Phase 4: A32NX profile (P4-1)

Reference: [docs/phase4-a32nx.md](../docs/phase4-a32nx.md). The profile `MSFS2024 A32NX` (main, FCU and OVHD
pages) and the script `XL24-A32NX.lua`. Not yet tested in the app or the sim. Record: date, MSFS 2024
version, A32NX version (FlyByWire Installer), PilotsDeck version, and every fallback or changed value you used.

**Before you start**
- [ ] Install the A32NX for MSFS 2024 with the FlyByWire Installer (`A:\FS2024 Stuff`; Stable, v2024.1.0 or
  later, MSFS 2024 selected in its header). Record the version.
- [ ] Copy `pilotsdeck/MSFS2024-XL/_Package/Scripts/XL24-A32NX.lua` into
  `%APPDATA%\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\Scripts\` (or install the built
  package with the Profile Manager). Copy it again after any change to it in the repo.

**Import (no sim needed)**
- [ ] Import `pilotsdeck/MSFS2024-XL/_Package/Profiles/MSFS2024 A32NX.streamDeckProfile` as
  docs/phase4-a32nx.md "Import the profile" says, and select `MSFS2024 A32NX`. The C172 profiles stay as
  they were.
- [ ] The main page matches the layout in the doc; `FCU` (1,8) and `OVHD` (2,8) open their pages; each back
  key (1,1) returns to the main page; 4,8 on the main page and the 15 reserved OVHD positions are empty.
- [ ] Select `AP1`, `STROBE`, `ND MODE`, `SPD` and `WARN` and compare their settings panels with the doc's Key
  table (command type, addresses, On/Off values, long press). Record every field that differs.

**Read only, first flight (load the A32NX cold and dark)**
- [ ] Record the aircraft string from the PilotsDeck log (`log\PilotsDeck<date>.log`, "Aircraft String
  changed to") and map the profile to it in the Profile Manager.
- [ ] Open the plugin's `InputEvents.txt` (written for the loaded aircraft) and record which `A32NX_` and
  `LIGHTING_` input events it lists, and whether `A32NX_OVH_LIGHTS_NAV_LOGO_SW` is there and in which form.
- [ ] Cold and dark: the SPD, HDG, ALT, V/S and BARO readouts are blank; the other keys show the cockpit's
  switch positions.

**Each key, both directions (power on: batteries, external power or APU)**
For every key: press it and check the cockpit control and the key; then move the control in the cockpit
with the mouse and check that the key follows without a key being pressed.
- [ ] Main: AP1, AP2, A/THR, LOC, APPR, FD, LS light with the FCU and EFIS buttons.
- [ ] Main: SPD, HDG, ALT, V/S, BARO show the FCU and EFIS windows: dashes, ` *` when managed, Mach as `.78`
  after SPD/MACH, the V/S sign, FPA after TRK/FPA, `STD` after a baro pull. A readout press pushes its knob;
  a BARO long press (at least 0.5 s) pulls it (STD) and a press pushes it (QNH): record what each does.
- [ ] Main: ND MODE and ND RNG step once per press (long press one step back) and match the ND.
- [ ] Main: WARN and CAUT light with a master warning or caution; a press clears the light. Record whether
  the aural warning stops too.
- [ ] Main: PARK, FLAPS (press one notch down, long press one notch up), GND SPLR, BRK LO/MED/MAX (record
  the image of the two not-selected BRK keys), STROBE (ON/AUTO), BEACON, NAV LOGO (SYS 1/OFF; set SYS 2 in
  the cockpit and check the key shows it), LAND L, LAND R (ON/RETRACT), NOSE (T.O./TAXI), SEAT BELT.
- [ ] FCU: each `+` / `-` key steps its window once per press (ALT by 100 or 1000 ft, as ALT STEP shows);
  each PULL key pulls its knob; SPD/MACH, TRK/FPA, ALT STEP and hPa/inHg toggle and read back.
- [ ] OVHD: WING, RWY TURN (both lights), NO SMOKE (ON/AUTO), BAT 1, BAT 2, EXT PWR (with a GPU connected),
  APU MSTR, APU START, APU AVAIL (lights when the APU is available).
- [ ] If an `A32NX.*` key does nothing: plugin log "Running Command" line for it, and any error; then
  record it (the doc's fallback is a Lua `SimCalculator` call).

**Unpowered and other aircraft**
- [ ] Batteries off: the FCU readouts are blank, ND MODE / ND RNG presses do nothing, and the keys show the
  read state.
- [ ] Load the C172 G1000 and select `MSFS2024 A32NX` by hand: readouts blank. Press STROBE, LAND L, NOSE,
  BEACON and record whether anything in the C172 moves; then switch back to the C172 profile.

**Controller independence**
- [ ] The keys work the same with the Xbox Elite controller and with the T.16000M + TWCS connected.

**Results to record**
- [ ] Record each step's result, the log lines for any step that failed, the aircraft string, the input
  events found, the MSFS and A32NX versions, and every fallback or change.

## P5-PKG: package install (C172 G1000)

Reference: [docs/package.md](../docs/package.md). The package `MSFS2024-XL v0.2.ppp` holds four profiles
(`MSFS2024 C172 G1000`, `MSFS2024 A32NX`, `MSFS2024 VisionJet`, `MSFS2024 CJ4`), six Lua scripts
(`XL24-SIMRATE.lua`, `XL24-COMPAD.lua`, `XL24-XPDRPAD.lua`, `XL24-A32NX.lua`, `XL24-SF50.lua`,
`XL24-CJ4.lua`) and one image (`Images/XL24-PadLit.png`). Not yet tested with the Profile Manager.
Record: date, Stream Deck app version, PilotsDeck version (0.9.7, patched build), MSFS 2024 version. Never
re-run the PilotsDeck installer or update the plugin for this (docs/installation.md).

**Build (no sim needed)**
- [ ] In the repository folder: `python tools/package/build_package.py`. It ends with `package ...`,
  `sha256 ...` and `size ...`; record the sha256.

**HT-PKG-1 Install (no sim needed)**
- [ ] Before the install: if the plugin's `Images\XL24-PadLit.png` is already there (for example a hand
  copy), note it and delete it (the repository holds it), so that the image step below shows whether this
  install copies it. Until the image is back, don't open the settings of a VisionJet or CJ4 COM pad key
  (docs/icons.md: the panel resets a key's image when the file is missing).
- [ ] Open the Profile Manager (PilotsDeck tray icon, or `ProfileManager.exe` in
  `%APPDATA%\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\`) and drop
  `pilotsdeck\MSFS2024-XL\_Releases\MSFS2024-XL v0.2.ppp` on the arrow. Check that the notes and version 0.2
  are shown.
- [ ] If it lists `MSFS2024 C172 G1000`, `MSFS2024 A32NX`, `MSFS2024 VisionJet` or `MSFS2024 CJ4` as already
  installed, keep **Remove old Profiles** checked. Click **Install**, click each profile link and pick the
  XL, wait until it finishes.
- [ ] The Stream Deck app lists each profile once (no "Copy" profile).
- [ ] An earlier install's `MSFS2024 C172 POC` (the Phase 1 profile; this package no longer holds it) is left
  as it is: delete it in the Stream Deck app (Preferences > Profiles) if you don't need it, or tick "none".
- [ ] `Get-FileHash` of the plugin's `Scripts\XL24-COMPAD.lua`, `Scripts\XL24-SIMRATE.lua`,
  `Scripts\XL24-XPDRPAD.lua`, `Scripts\XL24-A32NX.lua`, `Scripts\XL24-SF50.lua` and
  `Scripts\XL24-CJ4.lua` equals the sha256 the build printed for the same `Scripts/` entry. The image: record
  whether the plugin's `Images\XL24-PadLit.png` is there after the install and, if so, whether its
  `Get-FileHash` equals the sha256 the build printed for `Images/XL24-PadLit.png`. If it is not there, copy it
  by hand (docs/package.md, "Install").
- [ ] The plugin's `Profiles\` folder holds the package's four `.streamDeckProfile` files, `DeviceInfo.json`,
  and no `_work` folder (note any `MSFS2024 C172 POC.streamDeckProfile` an earlier install left there).

**HT-PKG-2 Mapping (flight needed)**
- [ ] Profile Mapping view: map `MSFS2024 C172 G1000` with the search string `asobo_c172sp_g1000`, Save
  (docs/package.md, "Map the C172 G1000 profile").
- [ ] Put another profile on the XL and load a C172 G1000 flight: the XL switches to `MSFS2024 C172 G1000`.
  The plugin log's `ProfileSwitcherManager` line now searches 1 valid profile.
- [ ] Load another aircraft: the XL does not switch to `MSFS2024 C172 G1000`.

**HT-PKG-3 Scripts (flight loaded)**
- [ ] SIM RATE page `1X` (XL24-SIMRATE) and MORE > COM PAD `ENT` (XL24-COMPAD) each do what their docs say
  (docs/phase2-sim-rate.md, docs/phase2-com1-pad.md), read on the sim's own state. `XL24-A32NX.lua` is
  tested by the section "Phase 4: A32NX profile (P4-1)" once the A32NX is installed.

**HT-PKG-4 Same version again**
- [ ] Install v0.2 again with Remove old Profiles checked: one profile of each name, the mapping still in the
  Profile Mapping view, and the HT-PKG-2 switch still works.

**HT-PKG-5 Bumped version (at the first real version bump, 0.3)**
- [ ] Same steps and results as HT-PKG-4 (the Profile Manager compares no versions).

**Results to record**
- [ ] Record the build sha256, each step's result, the versions, and anything the Profile Manager showed that
  differs from these steps.

## P5-ICONPKG: local icon package install (C172 G1000)

Reference: [docs/icons.md](../docs/icons.md), sections 1 to 3. Personal use only: never commit, upload or
share `.local/` or the icon package. Never re-run the PilotsDeck installer or update the plugin for this.
Installed once, on 2026-11-15: both icon profiles imported, the plain profiles removed, and the images and
scripts in the plugin folder equal to the package's (the install and hash steps below); the look, mapping
and second-install steps are still open.

- [ ] After the icon build (docs/icons.md section 1), in the repo folder:
  `python tools/package/build_icon_package.py`. It ends with `package ...`, `sha256 ...` and `size ...`;
  record the sha256. Run it again: it prints `unchanged` and the same sha256.
- [ ] If `MSFS2024 C172 G1000` is installed: delete it in the Stream Deck app (Preferences > Profiles), so
  only the icon profile stays installed (docs/icons.md section 2); the mapping step below maps the icon
  profile instead.
- [ ] Profile Manager: drop `.local\package\MSFS2024-XL-Icons v<version>-<commit>.ppp` on the arrow, keep
  **Remove old Profiles** checked if it lists installed profiles, click **Install**, click each profile link
  and pick the XL. The Stream Deck app then lists each profile once (no "Copy" profile).
- [ ] For each `Images/Guenseli-C172/...` and `Scripts/...` entry the build printed, `Get-FileHash` of the
  same file in the plugin's `Images\Guenseli-C172\` or `Scripts\` folder equals the printed sha256.
- [ ] Restart the Stream Deck app. With MSFS closed (or the flight fully loaded), switch the XL to
  `MSFS2024 C172 G1000 Icons`: the keys show the pack images as in the checklist section "P2-5: local icon
  build (C172 G1000)", and no key shows the Wait image (dark square, three dots).
- [ ] Map `MSFS2024 C172 G1000 Icons` with `asobo_c172sp_g1000` (docs/package.md) and load a C172 G1000
  flight: the XL switches to it. Install the same package again with Remove old Profiles checked: one icon
  profile, the mapping kept.
- [ ] Record the build sha256, each step's result and the versions (Stream Deck app, PilotsDeck 0.9.7
  patched, MSFS 2024).

## Phase 4: A32NX EFIS page (P4-2)

Reference: [docs/phase4-a32nx-efis.md](../docs/phase4-a32nx-efis.md). The new page `efis` (main 4,8 `EFIS`) of
the profile `MSFS2024 A32NX`, main 3,1 `WARN` and 3,2 `CAUT` (their press changed in P4-2), and the four new
functions of `XL24-A32NX.lua`. Not yet tested in the app or the sim. This section replaces the P4-1 section's
items on main 4,8 (now the EFIS folder, not empty) and on WARN/CAUT (the press is now the cockpit button's
press, not a write of 0). Record: date, MSFS 2024 version, A32NX version, PilotsDeck version, and every
fallback or changed value you used.

**Before you start**
- [ ] The P4-1 section's "Before you start" and "Import" steps, with the regenerated
  `MSFS2024 A32NX.streamDeckProfile` and the new `XL24-A32NX.lua` copied into the plugin's Scripts folder
  (the old copy lacks `NAV1`, `NAV2`, `MWARN`, `MCAUT`). Skip that section's items on main 4,8 ("empty") and
  on WARN/CAUT: the items below replace them.

**Import (no sim needed)**
- [ ] Main 4,8 `EFIS` opens the EFIS page; its back key (1,1) returns to the main page. The page matches the
  layout in the doc; 3,4 to 3,7 and 4,3 to 4,8 are empty.
- [ ] Select `CSTR`, `QNH`, `STD`, `ADF/VOR1`, `CHRONO`, `AUTOLAND` and `WARN` (EFIS page) and main `WARN`, and
  compare their settings panels with the doc's Key table (command type, addresses, On/Off values, long
  press). Record every field that differs.

**Each key, both directions (A32NX powered: batteries, external power or APU)**
For every key: press it and check the cockpit control and the key; then move the control in the cockpit
with the mouse and check that the key follows without a key being pressed.
- [ ] CSTR, WPT, VOR.D, NDB, ARPT: each lights with its ND option button, one at a time, and the ND shows the
  option. FD and LS as on the main page.
- [ ] BARO+ / BARO- step the Captain's baro; BARO shows it. QNH pushes the knob and is lit in QNH; STD pulls it
  and is lit in STD. Press QNH while it is lit and record whether the baro goes to QFE (FlyByWire: off STD a
  push changes between QNH and QFE). Set QFE in the cockpit and record what QNH and STD show then.
- [ ] hPa/inHg toggles the unit and reads back; ND MODE and ND RNG as on the main page.
- [ ] ADF/VOR1 and ADF/VOR2: a press moves the switch one position toward VOR, a long press (at least 0.5 s)
  one position toward ADF; the key shows `ADF`, `OFF` or `VOR` matching the cockpit switch and the ND
  pointers. **Record the value the cockpit switch writes for ADF and for VOR** (if the key shows `ADF` with
  the switch on VOR, the values are swapped: docs/phase4-a32nx-efis.md "Fallbacks").
- [ ] CHRONO starts the chrono on the Captain's ND; record what a second and a third press do. If nothing
  happens: the plugin log "Running Command" line, then try the H-event fallback.
- [ ] AUTOLAND shows `ON` only while the cockpit's AUTOLAND lamp is lit (record if you see it lit, for example
  in an autoland approach).
- [ ] WARN and CAUT, on the EFIS page and main 3,1 / 3,2: with a master caution or warning lit (for example a
  caution from a system switch left off; for a warning, in flight with AP1 engaged, press main AP1 to
  disconnect it: MASTER WARN flashes with the cavalry charge), a press puts the lamp out and stops the chime
  or the cavalry charge, as the cockpit button does; the key follows the lamp. The cockpit button cannot
  cancel every warning either (the flight warning computer ignores it while a non-cancellable warning is on):
  if the lamp stays on, press the cockpit's MASTER WARN with the mouse and compare. Record if the 200 ms
  press is too short (the lamp stays on while the cockpit button puts it out).

**P4-1 regression**
- [ ] Run the P4-1 section's "Each key" steps for every other main, FCU and OVHD key: unchanged.

**Unpowered and other aircraft**
- [ ] Batteries off: BARO blank, ND MODE / ND RNG / ADF/VOR presses do nothing, the keys show the read state.
- [ ] Load the C172 G1000 and select `MSFS2024 A32NX` by hand, EFIS page: BARO blank, ND and ADF/VOR steps do
  nothing, QNH off and STD lit (the 0 of missing L-Vars). Press CSTR, CHRONO and WARN and record whether
  anything in the C172 moves; then switch back to the C172 profile.

**Controller independence**
- [ ] The keys work the same with the Xbox Elite controller and with the T.16000M + TWCS connected.

**Results to record**
- [ ] Record each step's result, the log lines for any step that failed, the ADF/VOR values, the CHRONO and
  AUTOLAND results, the MSFS and A32NX versions, and every fallback or change.

## Phase 4: A32NX overhead pages (P4-3)

Reference: [docs/phase4-a32nx-overhead.md](../docs/phase4-a32nx-overhead.md). The OVHD page `ovhd` (main 2,8;
12 new keys beside P4-1's 16) and the new SYSTEMS page `ovhdsys` (ovhd 2,8) of the profile `MSFS2024 A32NX`, and
the new function `FUELMODE` of `XL24-A32NX.lua`. Not yet tested in the app or the sim. This section replaces
the P4-1 section's item on the "15 reserved OVHD positions" (now 3). Record: date, MSFS 2024 version, A32NX
version, PilotsDeck version, and every fallback or changed value you used.

**Before you start**
- [ ] The P4-1 section's "Before you start" and "Import" steps, with the regenerated
  `MSFS2024 A32NX.streamDeckProfile` and the new `XL24-A32NX.lua` copied into the plugin's Scripts folder
  (the old copy lacks `FUELMODE`).
- [ ] For MODE SEL: the MobiFlight WASM module installed (see docs/installation.md, "MobiFlight WASM module");
  after the flight loads, the plugin log shows "MobiFlight WASM Client Connection opened". PilotsDeck sends a
  script's `SimCalculator` code through that module (PilotsDeck and CFIT.SimConnectLib source): without it
  MODE SEL does nothing, most likely with no alert sign on the key.

**Import (no sim needed)**
- [ ] Main 2,8 `OVHD` opens the OVHD page; ovhd 2,8 `SYSTEMS` opens the SYSTEMS page; its back key (1,1)
  returns to the OVHD page, and the OVHD back key to the main page. Both pages match the layouts in the doc;
  ovhd 2,6, 2,7, 4,8 and ovhdsys 2,8, 3,8, 4,5 to 4,8 are empty.
- [ ] Select `EMER EXIT`, `APU N`, `EXT AVAIL`, `GEN 1`, `BUS TIE` (OVHD) and `L TK 1`, `MODE SEL`, `IR 1`,
  `ALIGN`, `WING A/I` (SYSTEMS) and compare their settings panels with the doc's key tables (command type,
  addresses, On/Off values, format, mappings). Record every field that differs.

**Cold-and-dark power-up (flight loaded cold and dark, parked)**
For every key: press it and check the cockpit control and the key; then move the control in the cockpit
with the mouse and check that the key follows without a key being pressed.
- [ ] BAT 1, BAT 2 lit (AUTO); BAT1 V and BAT2 V show about 25 to 28 V (record the values).
- [ ] With a GPU connected: EXT AVAIL shows `AVAIL` (record whether it matches the cockpit's AVAIL light while
  EXT PWR is off; once EXT PWR is on the cockpit shows ON and the key stays `AVAIL`), EXT PWR lit and the
  ECAM shows external power. Else the APU: APU MSTR lit, APU START lit, APU N climbs to about 100 (record
  whether it matches the ECAM's APU N), APU AVAIL `AVAIL`.
- [ ] APU GEN lit (on); APU BLEED lit; EMER EXIT `ARM`; SEAT BELT lit (on); NO SMOKE `AUTO`.
- [ ] SYSTEMS page: IR 1, IR 3, IR 2 `NAV` (the cockpit knobs follow; record whether the keys are in the
  cockpit's left-to-right order); ON BAT shows `ON BAT` briefly; ALIGN counts down to 0 (record the start value
  and whether it counts).
- [ ] L TK 1/2, R TK 1/2, CTR TK 1/2 lit (pumps on, the cockpit's OFF lights out); BLEED 1/2 and PACK 1/2 lit;
  ESS FEED, GALY CAB, COMML lit (normal).

**Each remaining key once**
- [ ] GEN 1 and GEN 2 off and on (engines off: the cockpit's OFF light follows; record what the ECAM shows),
  BUS TIE.
- [ ] X FEED: XFEED VLV moves from `SHUT` to `OPEN` and back (record the delay).
- [ ] MODE SEL: the cockpit's MAN light follows (record whether the fuel ECAM page changes). If it does
  nothing: the plugin log "Running Command" line, the MobiFlight line above, then the doc's fallback.
- [ ] WING A/I, ENG1 A/I, ENG2 A/I and PROBE HT: the cockpit's ON lights follow.
- [ ] ANN LT `TEST` lights every annunciator, then `BRT`; ESS FEED off shows the cockpit's ALTN light.

**P4-1 / P4-2 regression**
- [ ] Run "Phase 4: A32NX profile (P4-1)" for every main, FCU and OVHD key and "Phase 4: A32NX EFIS page
  (P4-2)": unchanged.

**Other aircraft**
- [ ] Load the C172 G1000 and select `MSFS2024 A32NX` by hand: the A32NX L-Var keys show the 0 values of the
  doc ("What the keys show when the A32NX isn't there") and their presses move nothing; MODE SEL does nothing.
  **Do not press GEN 1, GEN 2, APU GEN, the tank keys or X FEED there**: they are standard sim events that act
  on any aircraft. Then switch back to the C172 profile.

**Controller independence**
- [ ] The keys work the same with the Xbox Elite controller and with the T.16000M + TWCS connected.

**Results to record**
- [ ] Record each step's result, the log lines for any step that failed, the voltages, the EXT AVAIL, APU N,
  ALIGN and MODE SEL results, the IR order, the MSFS and A32NX versions, and every fallback or change.

## Phase 4: A32NX radio and transponder pages (P4-4)

Reference: [docs/phase4-a32nx-radios.md](../docs/phase4-a32nx-radios.md). The second-level pages `radio` (efis
3,4 `RADIO`, the Captain's RMP 1) and `xpdr` (efis 3,5 `XPDR`, the ATC/TCAS panel) of the profile
`MSFS2024 A32NX`, and the five new functions of `XL24-A32NX.lua` (`RMPACT`, `RMPSTBY`, `XPDRMODE`, `TCASMODE`,
`TCASTRAF`). Not yet tested in the app or the sim. This section replaces the P4-2 section's item "3,4 to 3,7
and 4,3 to 4,8 are empty" (3,4 and 3,5 are now folder keys). Record: date, MSFS 2024 version, A32NX version,
PilotsDeck version, and every fallback or changed value you used.

**Before you start**
- [ ] The P4-1 section's "Before you start" and "Import" steps, with the regenerated
  `MSFS2024 A32NX.streamDeckProfile` (or the icon profile) and the new `XL24-A32NX.lua` installed (the new
  package with the Profile Manager, or the script copied into the plugin's Scripts folder; the old copy lacks
  the five new functions).
- [ ] The MobiFlight WASM module installed (docs/installation.md, "MobiFlight WASM module (which keys need
  it)"); after the flight loads, the plugin log shows "MobiFlight WASM Client Connection opened". Every
  H-event key on these pages (VHF1, VHF2, XFER, the four knob keys, the keypad and CLR) goes through
  it: without it they do nothing, most likely with no alert sign on the key.

**Import (no sim needed)**
- [ ] Main 4,8 `EFIS` opens the EFIS page; efis 3,4 `RADIO` opens the RADIO page and efis 3,5 `XPDR` the XPDR
  page; each back key (1,1) returns to the EFIS page. Both pages match the layouts in the doc; efis 3,6, 3,7
  and 4,3 to 4,8 are empty.
- [ ] Select `VHF2`, `MHz+`, `ACTIVE`, `COM1` (RADIO) and `XPDR`, `IDENT`, `MODE`, `ALT RPTG`, `TCAS`, `7`
  (XPDR) and compare their settings panels with the doc's key tables (command type, addresses, On/Off
  values, long press, format, Decode BCD, mappings). Record every field that differs.

**COM set and swap (flight loaded cold and dark, then batteries on)**
For every key: press it and check the cockpit control and the key; then work the control in the cockpit
with the mouse and check that the key follows without a key being pressed.
- [ ] RMP ON lit and the cockpit's RMP 1 lit; ACTIVE and STBY show RMP 1's windows; VHF1 lit.
- [ ] kHz+ three times and MHz+ once: STBY and the cockpit's STBY window change alike (record whether a kHz
  step is 8.33 or 25 kHz); kHz- and MHz- step back.
- [ ] XFER: ACTIVE and STBY swap, as the cockpit windows; COM1 shows the new active frequency.
- [ ] VHF2: VHF2 lit, the cockpit's VHF2 key and SEL light lit (record what VHF1 shows now: no image is
  expected); set a VHF2 standby with the knob keys, XFER, COM2 shows it. VHF1 again.
- [ ] RMP ON off: ACTIVE and STBY blank, the cockpit's RMP 1 dark; on again.

**Transponder and TCAS (A32NX powered)**
- [ ] Press CLR twice (the cockpit's ATC display clears), then type four digits (for example 2 0 0 0): XPDR
  shows the old code until the fourth digit, then the new one, as the cockpit's ATC display. Type a digit
  with no entry open (no CLR first): nothing changes. CLR, CLR, three digits, then wait 7 seconds: the
  display shows the old code again and XPDR is unchanged.
- [ ] MODE STBY -> AUTO -> ON (press) and back (long press, at least 0.5 s): the cockpit knob follows; record
  what STATE shows in each position (STBY; on the ground in AUTO `GND`; ON or ALT).
- [ ] ALT RPTG off and on: the cockpit switch follows; record STATE (ON or ALT) each way.
- [ ] IDENT: the key lights and the cockpit's ATC display shows the ident; record how long it stays lit.
- [ ] TCAS STBY -> TA -> TA/RA and TRAFFIC THRT -> ALL -> ABV -> BLW, and back with long presses: record
  whether the cockpit knobs follow and whether the ND shows TA ONLY and the traffic as expected. If a key
  shows `STBY` / `THRT` while the cockpit knob is elsewhere: the doc's fallback (the upper-case names).

**P4-1 to P4-3 regression**
- [ ] Run "Phase 4: A32NX profile (P4-1)", "Phase 4: A32NX EFIS page (P4-2)" and "Phase 4: A32NX overhead
  pages (P4-3)": unchanged (efis 3,4 and 3,5 are now folder keys).

**Icon look test (icon profile, no sim)**
- [ ] The two folder keys, the two back keys and the 28 other new keys show the images of their rows in
  `tools/profilegen/icons-a32nx.json`; titles readable.

**Other aircraft**
- [ ] Load the C172 G1000 and select `MSFS2024 A32NX` by hand: VHF1, VHF2 and RMP ON dark, ACTIVE and STBY
  blank, COM1, COM2, XPDR and STATE show the C172's values; MODE, TCAS and TRAFFIC presses change only the
  keys' text; nothing in the C172 moves. **Do not press IDENT there** unless you want an ident (a standard
  event). Then switch back to the C172 profile.

**Controller independence**
- [ ] The keys work the same with the Xbox Elite controller and with the T.16000M + TWCS connected.

**Results to record**
- [ ] Record each step's result, the log lines for any step that failed, the kHz step, what VHF1 shows with
  VHF2 selected, STATE in each mode, the IDENT time, the TCAS results, the MSFS and A32NX versions, and every
  fallback or change.

## Phase 4: A32NX pedestal page (P4-6)

Reference: [docs/phase4-a32nx-pedestal.md](../docs/phase4-a32nx-pedestal.md). The second-level page `ped`
(efis 3,6 `PED`: the ECAM control panel, speed brake, flaps, park brake, gear, autobrake state, engine
masters, ENG MODE, rudder trim, A/SKID and brake pressure) of the profile `MSFS2024 A32NX`, and the six new
functions of `XL24-A32NX.lua` (`SPDBRK`, `GEARIND`, `ABRK`, `ENGMODE`, `RUDTRIM`, `BRKPSI`). Not yet tested in
the app or the sim. This section replaces the P4-4 section's item "efis 3,6, 3,7 and 4,3 to 4,8 are empty"
(3,6 is now the folder key `PED`). **Never long-press GEAR on the ground.** Record: date, MSFS 2024 version,
A32NX version, PilotsDeck version, and every fallback or changed value you used.

**Before you start**
- [ ] The P4-1 section's "Before you start" and "Import" steps, with the regenerated
  `MSFS2024 A32NX.streamDeckProfile` (or the icon profile) and the new `XL24-A32NX.lua` installed (the new
  package with the Profile Manager, or the script copied into the plugin's Scripts folder; the old copy lacks
  the six new functions).
- [ ] The MobiFlight WASM module installed (docs/installation.md, "MobiFlight WASM module (which keys need
  it)"); after the flight loads, the plugin log shows "MobiFlight WASM Client Connection opened". The 16 ECAM
  keys and ENG MODE's code go through it.

**Import (no sim needed)**
- [ ] Main 4,8 `EFIS` opens the EFIS page; efis 3,6 `PED` opens the PED page; its back key (1,1) returns to
  the EFIS page. The page matches the layout in the doc; efis 3,7 and 4,3 to 4,8 are empty.
- [ ] Select `ENG`, `TO CONF`, `SPD BRK`, `GEAR`, `ENG 1`, `ENG MODE`, `RUD L` and `A/SKID` and compare their
  settings panels with the doc's key table (command type, addresses, the H-Var sequence, On/Off values, long
  press and Second Command, format, mappings). Record every field that differs.

**ECAM control panel (cold and dark, then batteries and DC ESS on)**
For every key: press it and check the cockpit control and the key; then work the control in the cockpit
with the mouse and check that the key follows without a key being pressed.
- [ ] ENG, BLEED, PRESS, ELEC, HYD, FUEL, APU, COND, DOOR, WHEEL, F/CTL, one after the other: the SD shows
  that page and only that key is lit, as the cockpit's key. Press the lit key again (record what the SD does).
- [ ] ALL: the SD steps through its pages (record one page or more per press). STS: the STATUS page, STS lit.
- [ ] With a caution shown (for example a fuel pump off with the engines running, or as the aircraft gives
  one): CLR lit; press CLR, the message clears; RCL recalls it.
- [ ] TO CONF on the ground: the E/WD shows the T.O CONFIG result.
- [ ] ANN LT on DIM: record what the lit ECAM keys show (no image is expected, ASSUMPTION A-16).
- [ ] With the MobiFlight module stopped (or before it connects): the ECAM keys do nothing (record).

**Speed brake, ground spoilers, flaps, park brake (on the ground)**
- [ ] GND SPLR arms: SPD BRK shows `ARM`, the cockpit lever armed. SPD BRK long press: `50%`, the lever at
  1/2, GND SPLR off. Press: `RET`; press again: `FULL`; press: `RET`. Move the lever with the mouse: SPD BRK
  follows.
- [ ] FLAPS on PED and on main show the same and step the same lever; PARK on PED and on main set and release
  the same lever.

**Gear (readout only on the ground: never long-press GEAR there)**
- [ ] On the ground: GEAR `DOWN`, LDG GEAR `3 GRN`; with DC 2 off: LDG GEAR blank.
- [ ] In flight after take-off: GEAR long press: GEAR `UP`, LDG GEAR `UNLK` then `UP`; GEAR press: `DOWN`,
  LDG GEAR `3 GRN`.

**Autobrake and brake pressure**
- [ ] Main BRK LO, MED, MAX: A/BRK shows `LO`, `MED`, `MAX`, and `OFF` when disarmed. On a landing with
  autobrake: `DECEL` while the DECEL light is on (record).
- [ ] BRK PSI with PARK set (about `2.0 2.0` expected, record) and released (`0.0 0.0` expected, record); with
  DC ESS off: blank.

**Engines (cold start, APU bleed on)**
- [ ] ENG MODE press: `NORM` -> `IGN`, the cockpit knob follows (record, ASSUMPTION A-8).
- [ ] ENG 2 press: master ON, key lit, the engine starts; ENG 1 the same. ENG MODE long press back to `NORM`.
- [ ] Shutdown: ENG 1 and ENG 2 **long press**: masters OFF, keys dark. A short press of a lit ENG key does
  nothing harmful (record: ON stays ON).

**Rudder trim, A/SKID**
- [ ] RUD L three times: RUD TRIM `L 0.x`, the cockpit trim display alike (record the step and both values;
  if RUD TRIM does not follow the display, the doc's "Fallbacks" names the other read); RUD R back; RUD
  TRIM press: `0.0`. With DC 2 off: RUD TRIM blank.
- [ ] Flip the cockpit A/SKID & N/W STRG switch: A/SKID follows (`ON`, `OFF`); a press of the key changes
  nothing.

**P4-1 to P4-4 regression**
- [ ] Run "Phase 4: A32NX profile (P4-1)", "Phase 4: A32NX EFIS page (P4-2)", "Phase 4: A32NX overhead pages
  (P4-3)" and "Phase 4: A32NX radio and transponder pages (P4-4)": unchanged (efis 3,6 is now a folder key).
  Main GND SPLR, FLAPS and PARK and their PED copies show the same.

**Icon look test (icon profile, no sim)**
- [ ] The folder key efis 3,6, the back key and the 31 keys of the PED page show the images of their rows in
  `tools/profilegen/icons-a32nx.json`; titles readable (record the ECAM and ENG key legends against their
  titles).

**Other aircraft**
- [ ] Load the C172 G1000 and select `MSFS2024 A32NX` by hand: the ECAM keys dark, A/BRK `OFF`, SPD BRK `RET`,
  GEAR `UP`, LDG GEAR, RUD TRIM and BRK PSI blank, ENG MODE `CRANK`; ENG 1, ENG 2 and A/SKID show the C172's
  own values. **Do not press GEAR, ENG 1, ENG 2, SPD BRK, FLAPS, RUD L, RUD R, RUD TRIM or GND SPLR there**
  (standard events: they move the C172's own controls where it has them). ENG MODE does nothing. Then switch
  back to the C172 profile.

**Controller independence**
- [ ] The keys work the same with the Xbox Elite controller and with the T.16000M + TWCS connected.

**Results to record**
- [ ] Record each step's result, the log lines for any step that failed, what a second press of a lit ECAM
  key does, the ALL step, the DIM look, the brake pressures, the ENG MODE result, the rudder trim step, the
  MSFS and A32NX versions, and every fallback or change.

## P4-ICONS: local icon build (A32NX)

Reference: [docs/icons.md](../docs/icons.md), section 4. A second A32NX profile, `MSFS2024 A32NX Icons`, with key
images from the Guenseli icon pack. **Personal and private use only:** never commit, upload or share `.local/`,
the icon profile, the icon package or an export of them. Never re-run the PilotsDeck installer for icons.
Record: date, Stream Deck app version, PilotsDeck version (0.9.7 patched), MSFS 2024 and A32NX versions.

**Build and install (no sim needed)**
- [ ] In the repo folder: `python tools/profilegen/generate.py --icons tools/profilegen/icons-a32nx.json`, then
  `python tools/profilegen/check_icons.py --mapping tools/profilegen/icons-a32nx.json`: `RESULT: PASS`.
- [ ] Install as docs/icons.md sections 2 and 4 say (the icon package, or the hand copy of
  `.local\icons-a32nx\Images\Guenseli-A32NX`, 44 files, then a restart of the Stream Deck app), BEFORE you import
  the profile or open any key's settings. Keep only one of `MSFS2024 A32NX` and `MSFS2024 A32NX Icons`.

**Look test, page by page** (MSFS closed, or the A32NX flight fully loaded; a Wait image then means that key's
file is missing: note the key)
- [ ] Main: AP1, AP2, A/THR, LOC, APPR, FD, LS dark FCU buttons; WARN and CAUT master lights; PARK the park
  brake panel with its handle; GND SPLR the armed legend; BRK LO, MED, MAX blank pushbuttons with an ON legend;
  BEACON and SEAT BELT white rockers; the 13 readouts on a plain dark face; folders FCU (magenta), OVHD (green),
  EFIS (amber), each with its title and each still opening its page.
- [ ] FCU: knob images on SPD+/-, HDG+/-, ALT+/-, V/S+/-, the PULL keys and BARO+/-; the FCU buttons; nine
  readouts. EFIS: BARO+/-, CHRONO, the EFIS buttons (FD, CSTR, WPT, VOR.D, NDB, ARPT, QNH, LS, STD), WARN/CAUT,
  seven readouts. OVHD: BEACON, WING, RWY TURN, SEAT BELT rockers; BAT 1, BAT 2, BUS TIE, GEN 1, GEN 2, APU GEN
  with an OFF legend; EXT PWR, APU MSTR, APU START, APU BLEED with an ON legend; 13 readouts; folder SYSTEMS.
  SYSTEMS: fuel pump and centre tank keys with an OFF legend, MODE SEL with MAN, X FEED and the anti-ice and
  PROBE HT keys with ON, BLEED 1/2, PACK 1/2, GALY CAB, COMML with OFF; ESS FEED unchanged; six readouts.
- [ ] Each child page's back key (1,1) shows the green "out" folder icon and still goes back.
- [ ] Every title readable on its icon, every readout value readable (note each key that is not; WARN, CAUT
  and GND SPLR carry a legend under the title).
- [ ] Taste: note any icon you would rather change (for example the WARN, CAUT and GND SPLR legends, the white
  rockers, the folder colours, the knob images). Changes are mapping rows only.

**Sim check (needs the A32NX installed; not yet possible)**
- [ ] Cold and dark: BAT 1 and BAT 2 show the lit OFF legend; press each: the legend goes dark and the
  overhead's BAT button agrees. AP1 lit and dark with the FCU. BRK MED: MED shows the lit ON legend, LO and
  MAX the blank button only.

**Remove**
- [ ] Delete `MSFS2024 A32NX Icons` in Stream Deck Preferences > Profiles and the plugin's
  `Images\Guenseli-A32NX` folder.

**Results to record**
- [ ] Record each page's look (Wait images, back keys, readability, taste changes) and the sim check when it
  can run.

## VisionJet SF50 profile (V-1)

Reference: [docs/visionjet-sf50.md](../docs/visionjet-sf50.md). The profile `MSFS2024 VisionJet` for the
MSFS 2024 default Cirrus Vision SF50 (12 pages, 146 keys), built with the SF50's input event list
([docs/reference/InputEvents-SF50.txt](../docs/reference/InputEvents-SF50.txt)). Not yet tested in the app or
the sim. **GEAR and TOGA are readouts: never expect an action from them.** Record: date, MSFS 2024 version,
SF50 preset (`sf50_executive`, `sf50_family` or `sf50_complete`), PilotsDeck version, and every fallback or
changed value you used.

**Before you start**
- [ ] The input event list is already captured (2026-11-16). If PilotsDeck writes a new `InputEvents.txt` for
  the SF50 after a sim update, keep a copy and compare it with docs/reference/InputEvents-SF50.txt.
- [ ] Install the new package with the Profile Manager, or import `MSFS2024 VisionJet.streamDeckProfile` by
  hand (as the C172 profile, docs/phase2-main-page.md "Import the profile"). The C172's scripts
  `XL24-SIMRATE.lua`, `XL24-COMPAD.lua` and `XL24-XPDRPAD.lua` are installed (the sim rate, COM pad and
  transponder pages call them).
- [ ] The MobiFlight WASM module installed (CRS+, CRS-, CRS1 and the HDG BUG press need it).
- [ ] Profile Manager, **Profile Mapping**: pick `MSFS2024 VisionJet`, check "StreamDeck Profile modified for
  Switching", search string `microsoft_sf50`, **Plus**, **Save** (docs/visionjet-sf50.md, "Profile Manager
  mapping").

**Profile switching**
- [ ] Load the SF50: the deck switches to `MSFS2024 VisionJet`, and the plugin log's `ProfileSwitcherManager`
  line no longer says "Searching 0 valid Profiles" for the SF50. Load the C172: the deck switches to the C172
  profile.

**Main page, cold and dark, then powered**
- [ ] BAT: press, the cockpit battery switch moves and the key follows; flip the switch with the mouse, the
  key follows. Record which battery it is (1 or 2) and the values the key shows.
- [ ] NAV LT, STRB, LDG, PITOT: press, the cockpit switch moves; flip the cockpit switch with the mouse, the
  key follows. Record any key that does not (NAV LT uses an `_intercept` input event).
- [ ] TAXI: press, the taxi light changes; record whether the cockpit switch follows, and whether the SF50
  has a taxi light switch at all.
- [ ] 4,2 (BCN), 1,3 and 4,7 are empty.
- [ ] PARK: press, the parking brake sets and releases, the key follows. FLAPS: press, one detent out; long
  press, one detent in; record the number per detent. GEAR shows `DOWN` on the ground (no press). N1 matches
  the engine display.
- [ ] COM1, XPDR, ATC, MAP, CDI and BARO as in the C172 checklist's main page items; record whether BARO
  works on the G3000.

**Autopilot page (MORE > AUTOPILOT), in flight**
- [ ] AP, FD, HDG, NAV, APR, ALT, VS, FLC, LVL and VNV: each press, the PFD mode annunciator and the key
  agree; engage each mode in the cockpit too: the key follows.
- [ ] A/T (since V-AT the SF50's autothrottle arm input event; its steps are in the V-UX section, block "A/T
  arm and disconnect"): record whether the autothrottle arms and the key lights (since V-AT2 the key's light
  reads that input event); A/T MGD shows `ON` while the autothrottle drives.
- [ ] HDG+/-, ALT+/-, VS+/-, SPD+/- step and the readouts follow. HDG BUG press syncs the heading bug.
- [ ] CRS+ and CRS- step the course and CRS1 follows; record what a CRS1 press does, and any of the three
  that does nothing (the long press of CRS+ and CRS- steps by 10 with the standard event).
- [ ] On a takeoff with the cockpit TOGA button: TOGA shows `TO/GA`.

**Other pages**
- [ ] Radios, COM pad, transponder, views, sim rate and V-speeds: the C172 checklist's items of those pages,
  on the SF50; record any key the G3000 ignores, especially XPDR STBY/ON/ALT and the COM pad ENT.
- [ ] Engine page (MORE > ENGINE): N1, N2, ITT, FF PPH, ENG RUN, IGN and the fuel readouts against the
  engine display; record the units and whether IGN follows the FADEC.

**Guarded**
- [ ] GEAR and TOGA do nothing on a press. No CAPS, Safe Return or engine start key exists on any page.

**Icon look test (optional local icon build, no sim)**
- [ ] Build `MSFS2024 VisionJet Icons` with `tools/profilegen/icons-visionjet-sf50.json` (docs/icons.md),
  import it: the 157 mapped or as-is keys show the mapped images, titles readable.

**Other aircraft**
- [ ] Load the C172 G1000 and select `MSFS2024 VisionJet` by hand: the readouts show the C172's own values,
  BAT, NAV LT, STRB and LDG show nothing, PITOT shows the C172's pitot heat (the C172 has the same
  `deice_pitot_1` input event). **Do not press the light keys (NAV LT, STRB, LDG, TAXI), PITOT, PARK, FLAPS,
  the AP keys or LVL there** (they act on the C172). Then switch back to the C172 profile.

**Controller independence**
- [ ] The keys work the same with the Xbox Elite controller and with the T.16000M + TWCS connected.

**Results to record**
- [ ] Record each step's result, the log lines for any step that failed, the battery number, the B-var values,
  the flap number per detent, the keys the G3000 ignores, the MSFS version and SF50 preset, and every fallback
  or change.

## VisionJet SF50 profile (V-2)

Reference: [docs/visionjet-sf50.md](../docs/visionjet-sf50.md). V-2 grows the profile `MSFS2024 VisionJet` to
14 pages and 180 keys: RECOG and ICE on main, BARO's long press, the trim page's rudder trim, FMS SPD, YD and
MAN SPD on the autopilot page, and the new SYSTEMS (MORE 2,2) and ICE/ENV (MORE 2,4) pages. Run it after the
V-1 section; V-1's step "4,2 (BCN), 1,3 and 4,7 are empty" now reads: only main 1,3 is empty. Not yet tested
in the app or the sim. The values the SF50's input events take are working values: record what each key reads.
**G1 keys** (BAT 2, GEN 1, GEN 2, ENG IPS, WING/STAB, main ICE, WSHLD, OXYGEN): a press switches on, a long
press (half a second or more) switches off.

**Before you start**
- [ ] Import the new package (or the profile); the Profile Manager mapping from V-1 stays (same profile name).
- [ ] After the flight loads, wait about 30 s before you judge a key: some SF50 B-vars read 0 until then (a
  scmon capture, 2026-11-16).

**Main page**
- [ ] PARK (now the SF50's parking brake input event; V-1's `K:PARKING_BRAKES` failed in the SF50): with the
  brake set, press: the brake releases and stays released; press again: it sets; work the handle with the
  mouse: the key follows.
- [ ] RECOG: press, the cockpit recognition light switch moves; flip it with the mouse: the key follows (it
  uses an `_intercept` input event, as NAV LT).
- [ ] ICE: press, the wing/stab ice protection comes on (ICE/ENV STRUCT shows `ON`); long press: off.
- [ ] BARO: long press, the altimeter shows 29.92 / STD; a short press still does what V-1's BARO did.

**Trim page**
- [ ] RUD L and RUD R step the rudder trim and the RUD TRIM gauge follows; trim the SF50's rudder trim with
  the mouse: the gauge follows. TRIM UP, TRIM DN and the TRIM gauge as before. No aileron trim key exists.

**Autopilot page, in flight**
- [ ] YD: press, the PFD yaw damper annunciation and the key agree; record if nothing happens.
- [ ] FMS SPD and MAN SPD: press each, the speed reference changes on the PFD, that key lights and the other
  goes dark (the two B-vars are exclusive and hold their state); record what you see.

**Systems page (MORE > SYSTEMS)**
- [ ] BAT 2, GEN 1, GEN 2: press = on, long press = off, each against the cockpit switch and the EIS; flip
  each cockpit switch: the key follows. Record which battery and generator index each one moves.
- [ ] BUS V and LOAD A against the EIS. ENG KNOB shows `RUN` with the engine running; STARTER shows `ON`
  during a start; FUEL CTL shows a number per fuel control position (record each).

**ICE/ENV page (MORE > ICE/ENV)**
- [ ] ENG IPS, WING/STAB, WSHLD: press on, long press off; ENG AI, STRUCT and WSHLD SW in row 2 follow.
- [ ] WSHLD HI, WING LT, DEFOG, AFT CTL, TEMP BKUP toggle; OXYGEN: press on, long press off.
- [ ] BLEED, ECS DIS and the four knob readouts (TEMP FWD, TEMP AFT, FAN FWD, FAN AFT) show values as you work
  the cockpit controls; record the numbers.

**Working values (one by one, record the value read)**
- [ ] Every G1 and T1 key above: the value the key reads with the cockpit control off and on, and whether a
  long press on each G1 key really switches it off.

**Guarded**
- [ ] A short press never switches BAT 2, a generator, an ice protection switch or oxygen off. ENG KNOB,
  STARTER, FUEL CTL, BLEED, ECS DIS and the knob readouts do nothing on a press.

**Icon look test (optional local icon build, no sim)**
- [ ] Build `MSFS2024 VisionJet Icons` with `tools/profilegen/icons-visionjet-sf50.json` (docs/icons.md),
  import it: the 193 mapped or as-is keys show the mapped images, titles readable.

**Other aircraft**
- [ ] With the C172 loaded and `MSFS2024 VisionJet` picked by hand: the `sf50_` keys show nothing; PARK shows
  the C172's parking brake, and a press should do nothing; WING LT (`lighting_wing_1`, not in the C172's list)
  shows nothing there but may act on other aircraft. **Do not press YD, the BARO long press, the rudder trim
  keys or WING LT there** (standard events and generic input events act on any aircraft that has them).

**Results to record**
- [ ] Record each step's result, the values each new B-var read per position, the battery and generator
  indexes, whether the long presses switched off, the MSFS version and SF50 preset, and every fallback or
  change.

## VisionJet SF50 profile (V-3)

Reference: [docs/visionjet-sf50.md](../docs/visionjet-sf50.md), "Hold to repeat". V-3 keeps the profile
`MSFS2024 VisionJet` at 14 pages and grows it to 183 keys: the step keys of the autopilot, radios and trim
pages repeat while held (the new script `XL24-SF50.lua`), radios gets a BARO column (1,8 readout, 2,8 BARO+,
3,8 BARO-) and FUEL CTL shows words. CRS+/CRS- and ALT+/ALT- have no long press any more. Run it after the V-2
section. Not yet tested in the app or the sim. Hold times run from key down.

**Before you start**
- [ ] Import the new package (or the profile and `XL24-SF50.lua` into the plugin's Scripts folder); the
  Profile Manager mapping stays (same profile name). Load the SF50 and wait about 30 s.

**Autopilot page, hold to repeat**
- [ ] HDG+ / HDG-: a short press moves the heading bug one step (HDG BUG 3,2 follows). Hold 1 s: a few
  degrees; hold 3 s: about 40; hold 10 s: well over 100 (it stops by itself at 360 steps or 20 s). On release
  it **stops at once and never runs on**. Turn the cockpit heading knob with the mouse: HDG BUG follows.
- [ ] The same short press and 1, 3 and 10 s holds on CRS+/CRS- (CRS1 3,3), ALT+/ALT- (ALT SEL 3,4; record
  the step per press), VS+/VS- (VS TGT 3,5; it stops by 40 steps) and SPD+/SPD- (FLC SPD 3,6). A long press on
  CRS or ALT does nothing extra any more.

**Radios page**
- [ ] MHZ+/-, KHZ+/- on NAV1, NAV2 and COM2: a short press steps once; holds of 1, 3 and 10 s; each stops on
  release (watch the standby frequency in the NAV1, NAV2 and COM2 keys).
- [ ] BARO+ / BARO-: a short press steps once (BARO 1,8 and main BARO follow; record whether the G3000 PFD's
  baro moves), the same holds; turn the cockpit baro knob with the mouse: BARO 1,8 follows.

**Trim page**
- [ ] TRIM UP, TRIM DN, RUD L, RUD R: a short press steps once; hold 1 s and 3 s: the gauges move steadily and
  stop on release; a 10 s hold stops by itself at about 8 s.

**Never runs on**
- [ ] Press and release a step key very fast ten times: no extra steps after the last release; then hold that
  key 3 s: it still repeats (record it if it does not). Hold two step keys at once: each stops on its own
  release.
- [ ] On the ground: hold HDG+ and press the back key (1,1) with another finger, then release both. Record
  whether the heading bug stops at once or runs on until its cap (360 steps, about 9 s); go back to the
  autopilot page and check that HDG+ works normally again.

**Systems page**
- [ ] FUEL CTL (2,4): turn the cockpit fuel control switch to LEFT, AUTO and RIGHT: the key shows the same
  word (record the raw value if a word is wrong).

**Unchanged keys**
- [ ] FLAPS, SIM RATE, the AP mode keys and the G1 keys work as before; none repeats when held.

**Icon look test (optional local icon build, no sim)**
- [ ] Build `MSFS2024 VisionJet Icons` with `tools/profilegen/icons-visionjet-sf50.json` (docs/icons.md),
  import it: the 196 mapped or as-is keys show the mapped images; the BARO column is readable.

**Other aircraft**
- [ ] With the C172 loaded and `MSFS2024 VisionJet` picked by hand: the step keys act on the C172's bugs,
  radios and trim (standard events); hold one briefly and check that it stops on release. CRS needs the G3000
  and does nothing there.

**Results to record**
- [ ] Record each step's result (the "Verified" cells of aircraft-mappings.md's V-3 rows), the step per press
  of ALT and BARO, whether the PFD baro followed, the repeat feel (too slow, right, too fast), the MSFS
  version and SF50 preset, and every fallback or change.

## VisionJet SF50 profile (V-UX)

Reference: [docs/visionjet-sf50.md](../docs/visionjet-sf50.md), "The main page (V-UX)". V-UX keeps the profile
`MSFS2024 VisionJet` at 14 pages and grows it to 195 keys: the VisionJet gets its own main page (the HDG, ALT
and SPD columns with hold to repeat, the autothrottle column with the new A/T DISC key, the other mode keys,
FLAPS, LDG, ATC and the folders in columns 7 and 8); AUTOPILOT, RADIOS, SYSTEMS and COM PAD open from main,
CHECKLIST moves to MORE 1,5, and the keys that left main are on systems, radios and views. Run it after the
V-3 section; the earlier sections' main and MORE positions are those before V-UX. Not yet tested in the app or
the sim, except A/T (V-AT3 below). V-AT: A/T was reported as not working (the user's report, 2026-11-25), so
both A/T keys (main 1,4 and autopilot 2,8) write the SF50's input event `B:sf50_autopilot_autothrottle_arm`
instead of the standard event; whether that arms the autothrottle is not known. V-AT2: on the ground on
2026-11-26 a press armed the autothrottle and a second press disarmed it, but the keys' light never came on:
it read the SimVar `AUTOPILOT THROTTLE ARM`, which stayed 0. Since V-AT2 both A/T keys read the input event
itself (lit at 1, dark at 0). V-AT3: hand-tested 2026-11-26 after the import of the V-AT2 profile: the A/T
keys arm and disarm the autothrottle and their light follows, on the ground and in flight (which key and which
speed mode are not stated); the A/T steps below that this does not answer (which key, the speed modes, the
cockpit button with the mouse, A/T DISC) are still open.

**Before you start**
- [ ] Import the new package (or the profile and `XL24-SF50.lua` into the plugin's Scripts folder); the
  Profile Manager mapping stays (same profile name). Load the SF50 and wait about 30 s. V-AT: a profile (plain
  or icon build) imported before V-AT still sends the standard event on A/T, so import the new one first.
  V-AT2: one imported before V-AT2 still lights A/T from the SimVar; import the new one first.

**Main page walk by column** (each key against the cockpit, then the cockpit against the key)
- [ ] HDG column: HDG (1,1) lights while the heading mode is on; HDG+ (2,1) and HDG- (4,1) move the heading
  bug and HDG BUG (3,1) follows; a press on HDG BUG syncs the bug to the current heading. Turn the cockpit
  heading knob with the mouse: HDG BUG follows.
- [ ] ALT column: ALT (1,2) lights while altitude hold is on; ALT+ (2,2) and ALT- (4,2) move the selected
  altitude and ALT SEL (3,2) follows; turn the cockpit altitude knob: ALT SEL follows.
- [ ] FLC/SPD column: FLC (1,3) lights while flight level change is on; SPD (3,3) shows the autopilot's speed
  reference in knots (SPD+ and SPD- below).
- [ ] A/T column: A/T (1,4), FMS SPD (2,4), MAN SPD (3,4) and A/T DISC (4,4) (next two blocks).
- [ ] NAV (1,5), APR (2,5), VNV (3,5) and VS (4,5): each switches its mode and lights while the mode is on;
  switch each mode in the cockpit: the key follows.
- [ ] AP (1,6) switches the autopilot and lights while it is on; FLAPS (2,6) shows the flap handle, a press
  one step out, a long press one step in; LDG (3,6) switches the landing lights and follows the cockpit
  switch; ATC (4,6) opens and closes the ATC window.

**A/T arm and disconnect** (A/T first; the answers belong to visionjet-sf50.md, "Open points of the A/T keys
(V-AT)". Where a step needs the autothrottle armed or off and the keys have not done it, set it in the cockpit
and record that.)
- [ ] Before any press: record the flight state (ground or flight, FMS SPD or MAN SPD lit), what the cockpit
  A/T key and the PFD's autothrottle annunciation show, and whether A/T (main 1,4 and autopilot 2,8) and A/T
  DISC (4,4) are lit or dark.
- [ ] V-AT2, on the ground, autothrottle off: press A/T on main (1,4). Expected: the key lights with the
  cockpit's A/T light; press it again: the key goes dark with it. Record whether it does.
- [ ] V-AT2, on the ground: the same with A/T on the autopilot page (2,8); then check that main 1,4 shows the
  same state when you return to main.
- [ ] V-AT2, on the ground: arm and disarm with the cockpit A/T button and the mouse only: record whether both
  A/T keys' lights follow without a key press.
- [ ] V-AT2, on the ground: arm with A/T (1,4), then press A/T DISC (4,4): record whether A/T's light goes
  dark with the cockpit light, and whether A/T DISC's light (the SimVar) ever came on.
- [ ] V-AT2: if an A/T key's light does not follow, record which key (main 1,4 or autopilot 2,8), ground or
  flight, FMS SPD or MAN SPD, what the cockpit's A/T light and the PFD's autothrottle annunciation show, and
  whether it was the key's press or the mouse.
- [ ] On the ground, autothrottle off: press A/T on main (1,4) once; then, with the autothrottle off again if
  it armed, A/T on the autopilot page (2,8) once. Record for each key whether the PFD shows the autothrottle
  armed and whether the light follows.
- [ ] In flight, autothrottle off, once with FMS SPD lit and once with MAN SPD lit: the same with A/T on main
  (1,4). Record in which of them the autothrottle arms, and whether A/T and A/T DISC light with the PFD's
  annunciation.
- [ ] In flight, autothrottle off again: the same with A/T on the autopilot page (2,8).
- [ ] V-AT2, in flight, once with FMS SPD lit and once with MAN SPD lit: the four V-AT2 steps on the ground
  above again.
- [ ] With the autothrottle armed: press A/T (1,4) a second time. Record whether it disarms, stays armed or
  shows something else, and whether the lights agree with the PFD; then the same with autopilot 2,8.
- [ ] In flight with the autothrottle engaged: press A/T DISC (4,4). A/T and A/T DISC go dark, the autopilot
  page's A/T MGD shows OFF and the PFD's autothrottle annunciation goes. Record it if nothing changes (then
  try the fallbacks of visionjet-sf50.md, "Fallbacks", in order, and record which one worked).
- [ ] After A/T DISC, press A/T (1,4) again: record whether the autothrottle arms again (the input event may
  already hold the value 1) and whether A/T and A/T DISC light.
- [ ] Work the cockpit A/T key with the mouse, on the ground and in flight, with FMS SPD and with MAN SPD lit:
  record whether it arms and whether a second press disarms, whether it stays in or springs back, and whether
  the lights of A/T and A/T DISC follow without a key press. Then disconnect in the cockpit and press A/T
  (1,4): record whether it arms.
- [ ] If a press on A/T does nothing: record which key (main 1,4 or autopilot 2,8), ground or flight, FMS SPD
  or MAN SPD, whether the press or only the light failed, and whether the cockpit A/T key arms the
  autothrottle in the same state. Then (optional) a capture of the cockpit A/T key with the read-only monitor
  `tools/scmon` (its README): the input event as the second argument, and `AUTOPILOT THROTTLE ARM` added first
  to the `Vars` list of `Program.cs`, which does not hold it. Record the values both take.

**FMS SPD / MAN SPD on main**
- [ ] Press MAN SPD (3,4), then FMS SPD (2,4): the active one is lit and the other dark, as on the autopilot
  page (1,7 and 4,7); the PFD shows the matching speed reference. Press the cockpit buttons with the mouse:
  the keys follow.

**SPD hold**
- [ ] With MAN SPD on: a short press on SPD+ (2,3) steps once; hold 1, 3 and 10 s; SPD- (4,3) the same. Record
  whether the PFD speed bug and main SPD (3,3) move, and whether each hold stops at once on release.

**HDG and ALT hold on main**
- [ ] HDG+ / HDG- and ALT+ / ALT- on main: a short press steps once; holds of 1, 3 and 10 s as in the V-3
  section, with the readouts HDG BUG (3,1) and ALT SEL (3,2); each stops at once on release and never runs on.

**Folder and back-key walk**
- [ ] From main open AUTOPILOT (2,7), RADIOS (2,8), SYSTEMS (4,7) and COM PAD (3,8); on each the back key
  (1,1) returns to main. Neither press acts on the page it opens: YD (2,7), BARO+ (2,8), PITOT (4,7), the
  digit 3 (3,8) and HDG (main 1,1) do nothing by themselves.
- [ ] From main open MORE (4,8), then CHECKLIST (1,5): the page holds only its back key, which returns to
  MORE. MORE 1,6, 1,8 and 2,2 are empty; V-SPEEDS, XPDR, ENGINE and ICE/ENV open their pages as before.
- [ ] TRIM (1,7), VIEWS (1,8) and SIM RATE (3,7) open their pages as before.

**Moved keys**
- [ ] Systems row 3: BAT (3,2) and PARK (3,3) switch and follow the cockpit battery 1 switch and parking
  brake; GEAR (3,4) and N1 (3,5) show the gear handle and the engine's N1.
- [ ] Systems row 4: NAV LT, RECOG, STRB, LDG, TAXI and PITOT (4,2 to 4,7) switch their lights and pitot heat
  and follow the cockpit switches; ICE (4,8): a press switches wing/stab ice protection on, a long press off.
- [ ] Radios: COM1 (4,2) shows the active and standby frequency, a press swaps them; CDI (4,3) shows GPS or
  VLOC, a press toggles it; BARO (1,8): a press sends the baro event, a long press sets 29.92 (record what the
  G3000 PFD's baro does on each).
- [ ] Views: MAP (1,7) opens and closes the map window.

**COM PAD from main**
- [ ] Open COM PAD (3,8) and enter a frequency: the standby frequency in COM1 (1,2) changes as on the C172.

**The same code on two pages**
- [ ] Hold main HDG+ (2,1) for 2 s and release; then open AUTOPILOT and hold HDG+ (2,2) for 2 s and release:
  both repeat and stop normally. Do the same with ALT+ and SPD+.
- [ ] On the ground: hold main HDG+ and press AUTOPILOT (2,7) with another finger, then release both. Record
  whether the heading bug stops at once or runs on until its cap, and whether the autopilot page's ALT (2,1)
  or YD (2,7), now under your fingers, switched; then autopilot HDG+ works normally again.
- [ ] The same with main ALT+ (2,2); the autopilot page has HDG+ at 2,2. Then hold HDG+ on autopilot and on
  main, and ALT+ on both: each must still repeat. Record any that now moves only one step per press.

**Icon look test (optional local icon build, no sim)**
- [ ] Build `MSFS2024 VisionJet Icons` with `tools/profilegen/icons-visionjet-sf50.json` (docs/icons.md),
  import it: the 208 mapped or as-is keys show the mapped images; A/T DISC's title fits at the template size
  (record it if not).

**Other aircraft**
- [ ] With the C172 loaded and `MSFS2024 VisionJet` picked by hand: A/T DISC does nothing on a press (an SF50
  input event); its light shows the C172's autothrottle arm state. Since V-AT a press on A/T (main 1,4 and
  autopilot 2,8) does nothing too. V-AT2: A/T's light reads the SF50 input event, not the C172's autothrottle
  arm state; record what it shows in the C172.

**Results to record**
- [ ] Record each step's result (the "Verified" cells of aircraft-mappings.md's V-UX rows and of its V-1 row
  autopilot 2,8 `A/T`), the A/T DISC outcome and which fallback was needed, whether A/T arms the SF50's
  autothrottle (per key, on the ground and in flight), what a second press does, whether the lights follow the
  cockpit (V-AT2: each A/T key's light on the input event, on the ground and in flight), the SPD outcome
  (did SPD+/- move the PFD speed bug), whether a key up was lost across a page change or reached the other
  page's key, the BARO press on the G3000, the MSFS version and SF50 preset, and every change.

## VisionJet SF50 profile (V-PAD)

The COM pad page (main 3,8) of `MSFS2024 VisionJet`: centered key titles and a green key when a press took effect
(docs/visionjet-sf50.md, "COM pad: centered text and press feedback"). Not yet tested. Needs the new
`XL24-COMPAD.lua` and `Images\XL24-PadLit.png` in the plugin folder (the package installs the script and
holds the image; the install test shows whether the image is copied; until then copy it by hand as
docs/package.md says). The fast presses and every step after the Look steps need the SF50 loaded and COM1
on; the Look steps need no sim.

**Fast presses (do these first)**

These steps decide whether a wait in the script (the end of a light, the reads after ENT) holds up the next press
(not proven); if a press is late or lost, the fallback is the script without these waits or a global script
(docs/visionjet-sf50.md, "Fallbacks"). Clear the entry (CLR held) before each step and after the last one.
- [ ] Clear and type 1 1 8 5 2 5 as fast as you can, then clear and type 1 2 2 8 0 0: no digit is lost or late,
  and no key stays green.
- [ ] Press the same digit twice quickly (1, 1): record whether two separate flashes show or one longer one.
- [ ] Type a frequency and press ENT, then at once type the next entry: no digit is lost while ENT waits.

**Look (no sim needed)**
- [ ] Open COM PAD: 7 8 9, 4 5 6, 1 2 3, CLR 0 ENT show their text in the middle of the key; COM1, ENTRY and STBY
  ID look as before. No key is green.
- [ ] The same with the local icon build (`MSFS2024 VisionJet Icons`): the text is in the middle of the bezel key.
- [ ] With no sim connected, press 1: no key turns green and the entry does not change.

**Digits**
- [ ] Press 1, 1, 8, 5, 2, 5 slowly: each key turns green for a moment on release, and ENTRY shows `118.525`. The
  text stays readable in the middle while green. In the icon build too.
- [ ] Press 9 now (a 7th digit): not green, ENTRY unchanged.
- [ ] Clear, then press 2, 0, 9 as the first digit: none turns green, ENTRY stays `___.___`. Press 1, then 4: 4 is
  not green. Press 1 again, then 7 (`11_` typed): 7 is not green. Clear, 1, 3, 7: 7 is not green. Only the taken
  digits turned green.

**CLR**
- [ ] With digits typed: CLR short removes one digit and turns green; CLR held 1 s clears all and turns green on
  release. With nothing typed: CLR short and long stay dark.

**ENT**
- [ ] With another frequency in COM1 standby, type 118525, ENT: COM1 (1,2) standby shows 118.525 and then ENT turns
  green for about a second; `lua.log` has no "did not read back" line. Record the delay you see.
- [ ] Type 118525 again with 118.525 still in standby, ENT: ENT turns green (the sim has the frequency already).
- [ ] Type 11, ENT (refused): not green, ENTRY stays; the same with nothing typed. Right after a green ENT, press
  ENT with nothing typed: the green ends.
- [ ] Type 121500, hold ENT 1 s: COM1 active shows 121.500 and ENT turns green. Standby holds the old active
  frequency.
- [ ] With the avionics or COM1 off, type a frequency that standby does not hold, ENT: if the standby does not
  change, ENT stays dark and `lua.log` says "did not read back". Record what the sim did.

**Leaving the page**
- [ ] Press 1 and at once the back key; open COM PAD again: no key is green. Do it again after more than a minute.

**C172 (the script is shared)**
- [ ] With the C172 and `MSFS2024 C172 G1000`: MORE > COM PAD works as before (digits, also typed fast and at once
  after ENT, refused digits, CLR short and long, ENT, long ENT; section "Phase 2: COM1 pad (C172 G1000)"), its
  keys look as before and none turns green.

**Results to record**
- [ ] Record each step's result with the date, the MSFS version, the SF50 preset and which build (plain or icon);
  the "Verified" cells of aircraft-mappings.md's V-PAD rows; whether the green is clear and long enough, whether
  14 is the right text size, and every change.

## Citation CJ4 profile (CJ-1)

Reference: [docs/cj4.md](../docs/cj4.md). The profile `MSFS2024 CJ4` for the MSFS 2024 default Cessna
Citation CJ4 (15 pages, 195 keys), built without the CJ4's input event list. Not yet tested in the app or
the sim. **GEAR and the engine page are readouts: never expect an action from them.** Record: date, MSFS
2024 version, PilotsDeck version, and every fallback or changed value you used. Hold times run from key
down.

**Capture first (sim step S-1 of docs/cj4-research.md)**
- [ ] If it is not done yet: start the Stream Deck app with PilotsDeck, load a CJ4 flight, wait about 30 s
  after it loads, then quit. Keep PilotsDeck's `InputEvents.txt` and the log line with the CJ4's aircraft
  string (for docs/reference/ and the Profile Manager mapping).

**Before you start**
- [ ] Install the new package with the Profile Manager, or import `MSFS2024 CJ4.streamDeckProfile` by hand
  (as the C172 profile, docs/phase2-main-page.md "Import the profile") and copy `XL24-CJ4.lua`.
  `XL24-COMPAD.lua` and `Images\XL24-PadLit.png` must be in the plugin folder before the profile is imported
  (the package installs the script and holds the image; the install test shows whether the image is
  copied; until then copy it by hand as docs/package.md says), and so must `XL24-SIMRATE.lua` and
  `XL24-XPDRPAD.lua`.
- [ ] Pick `MSFS2024 CJ4` on the Stream Deck by hand (it has no search string yet). If the capture gave the
  aircraft string, map the profile in the Profile Manager (docs/cj4.md, "Profile Manager mapping") and check
  that the deck switches to it when the CJ4 loads.

**Main page, cold and dark, then powered**
- [ ] BAT, PARK, NAV LT, BCN, STRB, LDG, TAXI, PITOT and ICE: press each both ways, the cockpit switch moves
  and the key follows; then work the cockpit switch with the mouse, the key follows. Record each key that
  does nothing or does not follow (its input event is the fix).
- [ ] GEAR shows `DOWN` on the ground (no press). FLAPS: press, one detent out; long press, one detent in;
  record the number per detent. N1 matches the left engine's display.
- [ ] COM1 swaps, XPDR shows the code, ATC and MAP open and close their windows, CDI toggles `GPS` / `VLOC`.
- [ ] BARO: it matches the cockpit altimeter; a press (`K:BAROMETRIC`) and a long press (standard pressure):
  record what each does.
- [ ] 1,3 is empty.

**Folders**
- [ ] Open every folder key of main (TRIM, VIEWS, SIM RATE, CHECKLIST, MORE) and of MORE (V-SPEEDS, COM PAD,
  AUTOPILOT, XPDR, RADIOS, SYSTEMS, ENGINE, ICE/ENV, LIGHTS): the named page opens and its back key (1,1)
  returns to the page that opened it.
- [ ] MORE 1,2, 1,3, 2,6 to 2,8 and checklist 1,2 show nothing and do nothing.

**Autopilot page (MORE > AUTOPILOT), in flight**
- [ ] AP, FD, HDG, NAV, APR, BC, ALT, VS, FLC, YD and IAS/MACH: each press, the PFD annunciator and the key
  agree; engage each mode in the cockpit too: the key follows. Record each key the CJ4 ignores.
- [ ] BANK: press and long press change the bank limit; record the number per position.
- [ ] HDG+ / HDG-: a short press moves the heading bug one step (HDG BUG 3,2 follows). Hold 1 s, 3 s and 10
  s: it moves faster the longer it is held, stops by itself at 360 steps, and on release **stops at once and
  never runs on**. Turn the cockpit heading knob with the mouse: HDG BUG follows.
- [ ] The same short press and 1, 3 and 10 s holds on CRS+/CRS- (CRS1 3,3; stops by 360 steps), ALT+/ALT-
  (ALT SEL 3,4; record the step per press; stops by 400 steps), VS+/VS- (VS TGT 3,5; stops by 40 steps) and
  SPD+/SPD- (SPD TGT 3,6; stops by 200 steps). MACH TGT (3,7) follows the Mach target.

**Radios page (MORE > RADIOS)**
- [ ] NAV1, NAV2 and COM2 swap and show the idents; MIC1 and MIC2 pick the transmitting radio.
- [ ] MHZ+/-, KHZ+/- on NAV1, NAV2 and COM2: a short press steps once; holds of 1, 3 and 10 s; each stops on
  release (watch the standby frequency); a 10 s hold stops by itself, MHZ at 30 steps and KHZ at 200.
- [ ] BARO+ / BARO-: a short press steps once (BARO 1,8 and main BARO follow; record whether the PFD's baro
  moves), the same holds; turn the cockpit baro knob with the mouse: BARO 1,8 follows.

**Trim page**
- [ ] TRIM UP, TRIM DN, AIL L, AIL R, RUD L and RUD R: a short press steps once; hold 1 s and 3 s: the
  gauges move steadily and stop on release; a 10 s hold stops by itself at about 8 s.

**Never runs on**
- [ ] Press and release a step key very fast ten times: no extra steps after the last release; then hold
  that key 3 s: it still repeats (record it if it does not). Hold two step keys at once: each stops on its
  own release.
- [ ] On the ground: hold HDG+ on the autopilot page and press the back key (1,1) with another finger, then
  release both. Record whether the heading bug stops at once or runs on until its cap, and whether SYSTEMS
  (MORE 2,2, now under your finger) opened; go back and check that HDG+ works normally again.
- [ ] On the ground: hold TRIM UP on the trim page and press the back key, then release both. Record whether
  the trim stops and whether main HDG (2,2, now under your finger) switched; then TRIM UP works normally
  again.

**Views, sim rate, V-speeds and transponder pages**
- [ ] The C172 checklist's items of those pages, in the CJ4; record any key the CJ4 ignores, especially XPDR
  STBY, ON and ALT, and whether the V-speeds are the CJ4's.

**COM pad (MORE 1,5): fast presses (do these first)**

The COM pad page of `MSFS2024 CJ4` is the VisionJet's, with the same script (docs/cj4.md, "COM pad: centered
text and press feedback"). The fast presses and every step after the Look steps need the CJ4 loaded and COM1
on; the Look steps need no sim. The fast presses decide whether a wait in the script (the end of a light,
the reads after ENT) holds up the next press (not proven). The same script on the VisionJet is not yet
sim-tested, so a failed fast press is the script's and goes to both aircraft. Clear the entry (CLR held)
before each step and after the last one.

- [ ] Clear and type 1 1 8 5 2 5 as fast as you can, then clear and type 1 2 2 8 0 0: no digit is lost or
  late, and no key stays green.
- [ ] Press the same digit twice quickly (1, 1): record whether two separate flashes show or one longer one.
- [ ] Type a frequency and press ENT, then at once type the next entry: no digit is lost while ENT waits.

**COM pad: look (no sim needed)**
- [ ] Open COM PAD: 7 8 9, 4 5 6, 1 2 3, CLR 0 ENT show their text in the middle of the key; COM1 (1,2),
  ENTRY (1,3) and STBY ID (2,2) are there (their values need the sim). No key is green.
- [ ] The same with the local icon build (`MSFS2024 CJ4 Icons`): the text is in the middle of the bezel key.
- [ ] With no sim connected, press 1: no key turns green and the entry does not change.

**COM pad: digits**
- [ ] Press 1, 1, 8, 5, 2, 5 slowly: each key turns green for a moment on release, and ENTRY shows
  `118.525`. The text stays readable in the middle while green. In the icon build too.
- [ ] Press 9 now (a 7th digit): not green, ENTRY unchanged.
- [ ] Clear, then press 2, 0, 9 as the first digit: none turns green, ENTRY stays `___.___`. Press 1, then
  4: 4 is not green. Press 1 again, then 7 (`11_` typed): 7 is not green. Clear, 1, 3, 7: 7 is not green.
  Only the taken digits turned green.

**COM pad: CLR**
- [ ] With digits typed: CLR short removes one digit and turns green; CLR held 1 s clears all and turns
  green on release. With nothing typed: CLR short and long stay dark.

**COM pad: ENT**
- [ ] With another frequency in COM1 standby, type 118525, ENT: COM1 (1,2) standby shows 118.525 and then
  ENT turns green for about a second; `lua.log` has no "did not read back" line. Record the delay you see,
  or that the CJ4's COM1 does not take the event.
- [ ] Type 118525 again with 118.525 still in standby, ENT: ENT turns green (the sim has the frequency
  already).
- [ ] Type 11, ENT (refused): not green, ENTRY stays; the same with nothing typed. Right after a green ENT,
  press ENT with nothing typed: the green ends.
- [ ] Type 121500, hold ENT 1 s: COM1 active shows 121.500 and ENT turns green. Standby holds the old active
  frequency.
- [ ] With the avionics or COM1 off, type a frequency that standby does not hold, ENT: if the standby does
  not change, ENT stays dark and `lua.log` says "did not read back". Record what the sim did.

**COM pad: leaving the page**
- [ ] Press 1 and at once the back key; open COM PAD again: no key is green. Do it again after more than a
  minute.

**Systems, engine, ICE/ENV and lights pages**
- [ ] Systems: BAT, GEN L and GEN R both ways against the cockpit; AVIONICS, EXT PWR, BUS V, BATT A, HYD
  PSI, PUMP L and PUMP R against the cockpit (record units and the HYD PSI scale); XFER: record the number
  per selector position.
- [ ] Engine: every readout against the engine display, left and right (record units); START, RUN and IGN
  through a start; record the IGN number per position.
- [ ] ICE/ENV: ENG AI L, ENG AI R, WING/STAB and WSHLD both ways against the cockpit; CAB ALT, CAB RATE,
  DIFF and DUMP against the cockpit.
- [ ] Lights: RECOG, WING, BELTS, NO SMOKE, CABIN and PANEL both ways against the cockpit; record which
  lights the CJ4 does not have and which keys do nothing.

**Readouts only**
- [ ] GEAR and the engine page's keys do nothing on a press. No gear, engine start or TOGA key exists on any
  page.

**Icon look test (optional local icon build, no sim)**
- [ ] Build `MSFS2024 CJ4 Icons` with `tools/profilegen/icons-cj4.json` (docs/icons.md), import it: the 209
  mapped or as-is keys show the mapped images, titles readable (record any title that does not fit at the
  template size, for example WING/STAB, NO SMOKE, IAS/MACH and MACH TGT).

**Other aircraft**
- [ ] Load another aircraft and pick `MSFS2024 CJ4` by hand: the readouts show that aircraft's own values.
  **Do not press the keys that send events there** (they act on that aircraft). Then switch back.

**Controller independence**
- [ ] The keys work the same with the Xbox Elite controller and with the T.16000M + TWCS connected.

**Results to record**
- [ ] Record each step's result in the "Verified" cells of aircraft-mappings.md's CJ4 rows (date, MSFS
  version), the keys that do nothing, the repeat feel (too slow, right, too fast), the numbers and units
  asked for above, the aircraft string, which build (plain or icon), and every fallback or change.
