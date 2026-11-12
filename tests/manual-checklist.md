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
the main page, behind `SIM RATE` (main page 3,7). Not yet sim-tested: the SDK doesn't say what
`K:SIM_RATE_SET`'s value means, so HT-1 checks the route first. Record: date, MSFS 2024 version, PilotsDeck
version, and every fallback or changed value you used.

**HT-1: hand test of the route (optional, before the import)**

Only if you want to check the route before importing the new profile. Otherwise skip it: the imported
`1X`, `2X`, `4X` and `RATE` keys test the same thing in the blocks below. On the ground, parked, engine off
or idle, in the **installed** `MSFS2024 C172 G1000` profile (the one before this import), main page, on
the two empty positions 3,7 and 4,7. Nothing is imported for it.

| Step | Key | Settings (Tab out of each field) | Press | The sim should show | The deck should show | The plugin log should show |
|---|---|---|---|---|---|---|
| 1 | 3,7: drop **PilotsDeck > Display Value** | Value tab Address `(A:SIMULATION RATE, number)`, Format `1.2` | none | rate 1x | `1.00` | (no command) |
| 2 | 3,7 | none | change the rate with the sim's own control (your keybinding or the toolbar), then back to 1x | the rate changes | 3,7 follows (`2.00`, back to `1.00`) | nothing |
| 3 | 4,7: drop **PilotsDeck > Simple Button** | Command Type MSFS: K-Var (SimEvent), Command Address `K:SIM_RATE_SET:2`, On/Off Value empty, Toggle Switch unchecked | once, at 1x | rate 2x (any on-screen rate notice; the aircraft and clock run faster) | 3,7 `2.00` | "Running Command (Type: KVAR \| Address: K:SIM_RATE_SET..." with the 2 in some form, no error line |
| 4 | 4,7 | Command Address `K:SIM_RATE_SET:4` | once | 4x | `4.00` | as step 3 with 4 |
| 5 | 4,7 | Command Address `K:SIM_RATE_SET:1` | once | 1x | `1.00` | as step 3 with 1 |
| 6 | 4,7 | Command Address `K:SIM_RATE_INCR`, then press; then `K:SIM_RATE_DECR`, press | once each | 2x, then 1x | `2.00`, `1.00` | "Running Command (Type: KVAR \| Address: K:SIM_RATE_INCR" / "_DECR" |
| 7 | 4,7 | set it back to `K:SIM_RATE_SET:2` and leave both keys saved | none | | | |

- [ ] Stop and set the rate back with the sim's own control if anything other than the expected rate appears
  (for example a very high or very low rate on step 3): record it. Try no other values than the step below.
- [ ] **If 2X gives no change or a wrong rate** (step 3 here, or the `2X` key after the import): in the
  settings panel of that one key change the Command Address to `K:SIM_RATE_SET:512` (Tab out) and press it.
  (512 is 2 x 256: the FSUIPC offset 0x0C1A stores the rate x256; a lead only.) If that gives 2x, also try
  `K:SIM_RATE_SET:1024` on the 4X key (or on 4,7): 4x expected. If the sim jumps to a very high rate (up to
  128x), set it back at once with the sim's own control. Write down each result, then set the rate back to
  1x with the sim's own control. Afterwards set each key you changed back to its built address
  (`K:SIM_RATE_SET:2` on `2X`, `K:SIM_RATE_SET:4` on `4X`; Tab out) before the per-key tests below, and
  record what you changed.
- [ ] What the results mean: steps 3 to 5 give 2x, 4x, 1x: the built keys are right. Step 1 shows nothing,
  `0` or a stuck value while the rate visibly changes: try `(E:SIMULATION RATE, number)` in the same key
  and record it. Steps 3 to 5 fail but step 6 works: the keys need another route (stepping). Steps 3 to 6
  all do nothing while the log shows the sends: the sim ignores these events.
- [ ] Send the results (each step, the 512/1024 results if tried, the log lines) to the coordinator. A repair
  rules the scale from them. HT-1's two hand-made keys go away with the import below.

**Reimport (no sim needed)**
- [ ] If you changed any key by hand during the earlier tests (HT-1's keys at 3,7 and 4,7 too), write down
  which key and field first.
- [ ] In the Stream Deck app, export the installed `MSFS2024 C172 G1000` to the backup folder. Then delete
  **every** installed profile of that name, including the app's copies (`MSFS2024 C172 G1000 copy`,
  `MSFS2024 C172 G1000 copy 1`, ...). **Leave the profile named `G1000`**: that is a downloaded generic
  profile, not this project's.
- [ ] Double-click `pilotsdeck/MSFS2024-XL/_Package/Profiles/MSFS2024 C172 G1000.streamDeckProfile` (pick the
  XL if asked), select `MSFS2024 C172 G1000`. Check its aircraft mapping in the Profile Manager.
- [ ] The main page looks as before except 3,7, which is now the folder `SIM RATE`; 4,7 is still empty.
  The other pages look as before. From this import on, the main page has 5 folder keys (`SIM RATE` 3,7
  added) and 1 empty key (4,7); the main page and Trim/Views sections above give the counts of their own
  imports.

**Layout and round trip (no sim needed)**
- [ ] `SIM RATE` opens the sim rate page: back key at 1,1; row 1 `1X` 1,2, `2X` 1,3, `4X` 1,4, `RATE` 1,5;
  everything else empty. Its back key returns to the main page.
- [ ] Select `2X` and compare its settings panel with the doc: Command Type K-Var, Command Address
  `K:SIM_RATE_SET:2`, Value Address `(A:SIMULATION RATE, number)`, On/Off States `2` / `1`. Select `RATE`:
  Value Address as `2X`, Format `1.2`, Main Command `K:SIM_RATE_INCR`, long press on, Second Command
  `K:SIM_RATE_DECR`. Record every field that differs or looks different in the panel.

**Diagnostic first**
- [ ] Flight loaded at 1x: `RATE` shows `1.00`, `1X` On, `2X` and `4X` Off. If `RATE` shows nothing or `0`,
  use the `(E:SIMULATION RATE, number)` fallback on `RATE` and record it.
- [ ] Record what the four keys show while the sim is paused (Esc menu, and active pause if you use it).

**Sim -> Stream Deck (change it in the sim, don't press a key)**
- [ ] Change the rate with the sim's own control to 2x, 4x, then back to 1x: `RATE` follows and the lit key
  follows (`2X` at 2x, `4X` at 4x, `1X` at 1x).
- [ ] Step to 8x and to 0.5x if the sim allows: no rate key On (background only), `RATE` `8.00` / `0.50`.
  Record anything the sim refuses (for example above 4x on the ground) and which control you used.

**Stream Deck -> sim (press the key)**
- [ ] At 1x press `2X`: the sim goes to 2x (its own rate notice, if any), `2X` On, `RATE` `2.00`. Press `4X`:
  4x, `4X` On. Press `1X`: 1x, `1X` On. Press `2X` twice in a row: it stays 2x.
- [ ] Press `RATE`: one step up; long press (>= 0.5 s): one step down. `RATE` shows each new rate.
- [ ] For a press that did nothing or gave a wrong rate: the plugin log line "Running Command (Type: KVAR |
  Address: K:SIM_RATE_..." for that key, and any error. For `2X` / `4X`, the 512/1024 step in HT-1 above.

**Controller independence**
- [ ] The sim rate keys work the same with the Xbox Elite controller and with the T.16000M + TWCS connected
  (no key needs a binding on either).

**Result for the worker**
- [ ] Record HT-1's results (if run), each key's result in both directions, what the keys show while paused,
  the 8x / 0.5x observations, any 512/1024 result, the sim version, and every fallback or value change.

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
  softkeys. V-speeds: seven readouts. Sim rate: 1X / 2X / 4X buttons, RATE readout.
- [ ] A-5: DIRECT and FMS OUT- (PFD page) and the PFD folder (More page) look sharp and whole, not cropped.
- [ ] A-8: every title is readable on its icon, and every readout's value is readable on its background.
  Note each key that is hard to read.
- [ ] A-6 (taste): note any icon you would rather change (PARK, ATC, MAP, trim arrows, RNG PUSH, folder
  colours, the buttons on COCKPIT/EXTERNAL and 1X/2X/4X, the white rockers). Changes are mapping rows only.

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
