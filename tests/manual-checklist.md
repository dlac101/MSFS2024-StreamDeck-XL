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
