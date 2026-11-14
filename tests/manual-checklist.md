# Manual test checklist

Copy the relevant section into a dated note (or the CHANGELOG) each time you run it.
Record: date, MSFS 2024 version, PilotsDeck version, aircraft.

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
- [ ] Exported profile saved to `pilotsdeck/MSFS2024-XL/_Package/Profiles/`.
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
- [ ] The Phase 1 profile `MSFS2024 C172 POC` is still there, unchanged.
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

**Result for the worker**
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
  2026-11-11 (LR95-C2)). If the cockpit or external camera shows another number than `2` / `3`, record it:
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
  follow (hand-tested 2026-11-11, LR101-C2; check it again on the generated key).
- [ ] If `COCKPIT` or `EXTERNAL` does nothing: record it. It becomes Empty and its row in
  aircraft-mappings.md is marked "does not work" (the row stays).

**Controller independence**
- [ ] The trim and view keys work the same with the Xbox Elite controller and with the T.16000M + TWCS
  connected (no key needs a binding on either).

**Result for the worker**
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

**Result for the worker**
- [ ] Record which bezel keys worked (PFD and MFD separately), the knob directions, what `CLR HOLD` and
  `RNG PUSH` did, every V-speeds number (and `VFE` at each flap position), whether the MobiFlight WASM line
  was in the log, and every fallback or value change.

## Phase 2: Sim rate page (C172 G1000)

Reference: [docs/phase2-sim-rate.md](../docs/phase2-sim-rate.md). The page is in the same profile file as
the main page, behind `SIM RATE` (main page 3,7), and its `1X` key needs the script `XL24-SIMRATE.lua`.
Repaired after the first sim test (P2-6R, not yet sim-tested): on 2026-11-12 `1X`/`2X`/`4X`
(`K:SIM_RATE_SET`) did nothing and `RATE` never stepped down (no press was held 0.5 s). The page now has
the user's layout (LR298-C5): `1X` 1,2, `SLOWER` 1,3, `RATE` 1,4, `FASTER` 1,5; the 2X and 4X keys are
gone. Record: date, MSFS 2024 version, PilotsDeck version, and every fallback or changed value you used.

**Safety first.** If the rate ever runs away (very high or very low), set it back to 1x with the sim's own
sim rate controls (your bindings, Controls > Miscellaneous > "Sim rate"), then record what happened.

**The hand test HT-C (in the profile you have now, before the import below)**

HT-A (the step size) is answered by the user's report: the sim steps by x2 up to 128x (LR298-C5). Nothing
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
- [ ] Send the results of HT-C (each `RATE` value, the log lines) to the coordinator.

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
  the `.local\icons` folder, rebuild, and import it as in the section "P2-5: local icon build" and
  [docs/icons.md](../docs/icons.md) (delete the old `MSFS2024 C172 G1000 Icons` profiles and their copies
  first). The checks below apply to it the same way.
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

**Result for the worker**
- [ ] Record HT-C's results, each key's result in both directions, the script stop cases and their
  `lua.log` lines, what the keys show while paused, the 8x / 0.5x observations, the sim version, and every
  fallback or value change.

## P2-5: local icon build (C172 G1000)

Reference: [docs/icons.md](../docs/icons.md). A second profile, `MSFS2024 C172 G1000 Icons`, with key images
from the Guenseli icon pack. **Personal and private use only:** never commit, upload or share `.local/`, the
icon profile, or an export of it. The committed `MSFS2024 C172 G1000` profile is not changed and stays
installed. Record: date, Stream Deck app version, PilotsDeck version, MSFS 2024 version (sim check only).

**Build and install (no sim needed)**
- [ ] In the repo folder: `python tools/profilegen/generate.py --icons tools/profilegen/icons-c172-g1000.json`.
  It prints the profile path and the image folder (`.local\icons\Images\Guenseli-C172`, 23 files).
- [ ] Copy the folder `.local\icons\Images\Guenseli-C172` (File Explorer) into
  `%APPDATA%\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\Images\` (result:
  `...\Images\Guenseli-C172\*.png`, 23 files). This is your own hand step, the plugin's documented way to add
  images (PilotsDeck README 3.3); it is a file copy, not a settings edit, and touches none of the patched
  plugin's program files. **Never re-run the PilotsDeck installer to "fix" icons** (it would undo the
  patched build: #176, docs/installation.md).
- [ ] Quit and restart the Stream Deck app (not as administrator). Do this BEFORE importing or opening any
  key's settings: a key whose image is missing gets its image field reset when its settings panel opens.
- [ ] Import `.local\icons\MSFS2024 C172 G1000 Icons.streamDeckProfile` (double-click, pick the XL if asked).
  It appears as `MSFS2024 C172 G1000 Icons` beside `MSFS2024 C172 G1000`. Switch the XL to it.

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

**Result for the worker**
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
  `Images\Guenseli-C172` folder stays as it is. (Or import the early profile whose path the worker gives you.)
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

**Result for the worker**
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

**Result for the worker**
- [ ] Record each step's result, the real steps (HDG, CRS, ALT short and long, VS, SPD), the ALT long-press
  outcome (step or set), the VNV three answers, whether FLC took the current IAS, armed versus active for
  NAV/APR, the sim version, and every fallback or change.
