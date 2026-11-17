# Aircraft mappings

Every aircraft-specific action is recorded here: the source variable or event, its units,
and when and where it was verified. **"Unverified" means taken from the MSFS SDK / PilotsDeck
docs but not yet tested in the sim.** Change it only after a test passes.

Address syntax follows the PilotsDeck README section 2.1.1.

## Cessna 172 Skyhawk G1000 (MSFS 2024 default)

Aircraft string (from the PilotsDeck log, 2026-11-11):
`...\fs24-asobo-aircraft-c172sp-as1000\content\simobjects\airplanes\asobo_c172sp_g1000\presets\asobo\c172sp_avionics_passengers\config\aircraft.cfg`
(`asobo_c172sp_g1000` is the part to match on.)

| Function | Read (variable) | Units | Write (command) | Verified |
|---|---|---|---|---|
| Battery master | `B:electrical_battery_1` (B-Var, "Run as Command" unchecked) | 0/1 | `B:electrical_battery_1`, On `1` / Off `0` | 2026-11-11, MSFS 1.9.24.0, both directions |
| Parking brake | `(A:BRAKE PARKING POSITION, Bool)` | 0/1 | `K:PARKING_BRAKES` | 2026-11-11, MSFS 1.9.24.0, both directions |
| Magnetic heading | `(A:PLANE HEADING DEGREES MAGNETIC, Degrees)` | 0-360 | (read only) | 2026-11-11, MSFS 1.9.24.0 |
| Autopilot master | `(A:AUTOPILOT MASTER, Bool)` | 0/1 | `K:AP_MASTER` | 2026-11-11, MSFS 1.9.24.0, both directions |
| Selected heading (Phase 3) | `(A:AUTOPILOT HEADING LOCK DIR, Degrees)` | 0-360 | _TBD_ | Unverified |

**Battery: don't use the standard SimVar/K-event pair in this aircraft.** Recorded with a SimConnect
monitor on 2026-11-11: the cockpit BAT switch changes `B:electrical_battery_1` and
`(A:ELECTRICAL MASTER BATTERY:2, Bool)`, while `(A:ELECTRICAL MASTER BATTERY:1, Bool)` stays put.
`K:TOGGLE_MASTER_BATTERY` toggles battery index 1, so a key built on it moves out of step with the
cockpit switch. The B-Var keeps both directions in sync. Other B-Vars this aircraft lists include
`B:landing_gear_parkingbrake` and `B:as1000_autopilot_ap_pfd` (see InputEvents.txt).

Parking brake and AP master: the SimConnect monitor showed both SimVars following mouse clicks in the
cockpit, and the keys followed too (2026-11-11). The full input event list for this aircraft is in
[reference/InputEvents-C172-G1000.txt](reference/InputEvents-C172-G1000.txt).

### Phase 2 main page

For [phase2-main-page.md](phase2-main-page.md). All rows are **Unverified** until the Phase 2 checklist
passes. Battery, parking brake and AP master are the verified rows above (reused, not repeated). Switches
use the aircraft's input event where it lists one for the switch (battery pattern); the standard
SimVar/K-event pair is the fallback. If the ATC or MAP key does nothing in the sim test, its row is marked
"does not work" and stays.

| Function | Read | Units | Write | Fallback | Source | Verified |
|---|---|---|---|---|---|---|
| Engine RPM (1,2) | `(A:GENERAL ENG RPM:1, rpm)` | rpm | (read only) | none | SDK-ENGV | Unverified |
| Electric fuel pump (1,3) | `B:fuel_pump_1` (B-Var, "Run as Command" unchecked) | 0/1 assumed | `B:fuel_pump_1`, On `1` / Off `0` | `K:FUEL_PUMP:1`, read `(A:GENERAL ENG FUEL PUMP SWITCH:1, Bool)` | IE 179; SDK-ENGE; SDK-ENGV | Unverified |
| Gear type (1,5) | `(A:IS GEAR RETRACTABLE, Bool)` | Bool | (read only) | none | SDK-GEARV | Unverified |
| Flaps handle (1,6) | `(A:FLAPS HANDLE INDEX, number)` | number, 0-3 assumed | `K:FLAPS_INCR` (press), `K:FLAPS_DECR` (long press) | `B:handling_flaps` exists, values unknown, not used | SDK-CTLV; SDK-FCE; IE 184; README 2.1 | Unverified |
| Flaps handle positions (diagnostic) | `(A:FLAPS NUM HANDLE POSITIONS, number)` | number | (read only) | none | SDK-CTLV | Unverified |
| AP heading mode (2,2) | `(A:AUTOPILOT HEADING LOCK, Bool)` | Bool | `K:AP_HDG_HOLD` | `B:as1000_autopilot_heading_pfd` (push value unknown) | SDK-APV; SDK-APE; IE 25 | Unverified |
| AP altitude mode (2,3) | `(A:AUTOPILOT ALTITUDE LOCK, Bool)` | Bool | `K:AP_ALT_HOLD` | `B:as1000_autopilot_altitude_pfd` (push value unknown) | SDK-APV; SDK-APE; IE 13 | Unverified |
| AP vertical speed mode (2,4) | `(A:AUTOPILOT VERTICAL HOLD, Bool)` | Bool | `K:AP_VS_HOLD` | `B:as1000_autopilot_verticalspeed_pfd` (push value unknown) | SDK-APV; SDK-APE; IE 33 | Unverified |
| AP NAV mode (2,5) | `(A:AUTOPILOT NAV1 LOCK, Bool)` | Bool | `K:AP_NAV1_HOLD` | `B:as1000_autopilot_navigation_pfd` (push value unknown) | SDK-APV; SDK-APE; IE 27 | Unverified |
| AP approach mode (2,6) | `(A:AUTOPILOT APPROACH HOLD, Bool)` | Bool | `K:AP_APR_HOLD` | `B:as1000_autopilot_approach_pfd` (push value unknown) | SDK-APV; SDK-APE; IE 17 | Unverified |
| AP FLC mode (2,7) | `(A:AUTOPILOT FLIGHT LEVEL CHANGE, Bool)` | Bool | `K:FLIGHT_LEVEL_CHANGE` | `B:as1000_autopilot_flightlevelchange_pfd` (push value unknown) | SDK-APV; SDK-APE; IE 23 | Unverified |
| Flight director (2,8) | `(A:AUTOPILOT FLIGHT DIRECTOR ACTIVE, Bool)` | Bool | `K:TOGGLE_FLIGHT_DIRECTOR` | `B:as1000_autopilot_fd_pfd` (push value unknown) | SDK-APV; SDK-APE; IE 21 | Unverified |
| COM1 active / standby (3,1) | `(A:COM ACTIVE FREQUENCY:1, MHz)`, `(A:COM STANDBY FREQUENCY:1, MHz)` | MHz assumed (SDK lists Frequency BCD16) | `K:COM_STBY_RADIO_SWAP` | `(A:COM ACTIVE FREQUENCY:1, Frequency BCD16)`, `(A:COM STANDBY FREQUENCY:1, Frequency BCD16)`, Decode BCD, Format `2:1%s`; if it shows `11850.00`, set Scalar `0.01` | SDK-RADV; SDK-RADE; SDK-UNITS; README 2.2.2 | Unverified |
| Transponder code (3,2) | `(A:TRANSPONDER CODE:1, Bco16)`, Decode BCD | Bco16 | (read only) | `(A:TRANSPONDER CODE:1, number)`, no Decode BCD | SDK-RADV; SDK-UNITS | Unverified |
| ATC window (3,3) | none (no state) | | `K:SIMUI_WINDOW_HIDESHOW` | none | SDK-MISCE | Unverified |
| Flight map (3,4) | none (no state) | | `K:FLIGHT_MAP` | none | SDK-MISCE | Unverified |
| CDI source (3,5) | `(A:GPS DRIVES NAV1, Bool)` | Bool | `K:TOGGLE_GPS_DRIVES_NAV1` | none | SDK-RADV; SDK-RADE | Unverified |
| Altimeter setting (3,6) | `(A:KOHLSMAN SETTING HG:1, inHg)` (index 1 assumed) | inHg | `K:BAROMETRIC` | another altimeter index, e.g. `(A:KOHLSMAN SETTING HG:2, inHg)`; knob input event `B:as1000_baro_pfd` exists, not used | SDK-SYSV; SDK-INSTE; IE 38 | Unverified |
| NAV lights (4,1, key title `NAV LT`) | `B:lighting_nav_0` (B-Var, "Run as Command" unchecked) | 0/1 assumed | `B:lighting_nav_0`, On `1` / Off `0` | `K:TOGGLE_NAV_LIGHTS`, read `(A:LIGHT NAV, Bool)` | IE 197; SDK-ELECE; SDK-SYSV | Unverified |
| Beacon (4,2) | `B:lighting_beacon_1` (as NAV lights) | 0/1 assumed | `B:lighting_beacon_1`, On `1` / Off `0` | `K:TOGGLE_BEACON_LIGHTS`, read `(A:LIGHT BEACON, Bool)` | IE 193; SDK-ELECE; SDK-SYSV | Unverified |
| Strobes (4,3) | `B:lighting_strobe_0` (as NAV lights) | 0/1 assumed | `B:lighting_strobe_0`, On `1` / Off `0` | `K:STROBES_TOGGLE`, read `(A:LIGHT STROBE, Bool)` | IE 202; SDK-ELECE; SDK-SYSV | Unverified |
| Landing light (4,4) | `B:lighting_landing_1` (as NAV lights) | 0/1 assumed | `B:lighting_landing_1`, On `1` / Off `0` | `K:LANDING_LIGHTS_TOGGLE`, read `(A:LIGHT LANDING, Bool)` | IE 196; SDK-ELECE; SDK-SYSV | Unverified |
| Taxi light (4,5) | `B:lighting_taxi_1` (as NAV lights) | 0/1 assumed | `B:lighting_taxi_1`, On `1` / Off `0` | `K:TOGGLE_TAXI_LIGHTS`, read `(A:LIGHT TAXI, Bool)` | IE 203; SDK-ELECE; SDK-SYSV | Unverified |
| Pitot heat (4,6) | `B:deice_pitot_1` (as NAV lights) | 0/1 assumed | `B:deice_pitot_1`, On `1` / Off `0` | `K:PITOT_HEAT_TOGGLE`, read `(A:PITOT HEAT, Bool)` | IE 139; SDK-AMISCE; SDK-SYSV | Unverified |

Sources: IE n = line n of [reference/InputEvents-C172-G1000.txt](reference/InputEvents-C172-G1000.txt).
README = https://github.com/Fragtality/PilotsDeck/blob/master/README.md. The SDK pages (MSFS 2024 SDK,
under https://docs.flightsimulator.com/msfs2024/retail/programming-apis/):
- SDK-APV: simvars/aircraft-simvars/aircraft-autopilot-and-assistant-variables/
- SDK-APE: key-events/aircraft-autopilot-and-flight-assistance-events/
- SDK-SYSV: simvars/aircraft-simvars/aircraft-system-variables/
- SDK-RADV: simvars/aircraft-simvars/aircraft-radio-navigation-variables/
- SDK-CTLV: simvars/aircraft-simvars/aircraft-control-variables/
- SDK-GEARV: simvars/aircraft-simvars/aircraft-brake-and-landing-gear-variables/
- SDK-ENGV: simvars/aircraft-simvars/aircraft-engine-variables/
- SDK-UNITS: simvars/simulation-variable-units/
- SDK-ELECE: key-events/aircraft-electrical-events/
- SDK-FCE: key-events/aircraft-flight-control-events/
- SDK-RADE: key-events/aircraft-radio-navigation-events/
- SDK-INSTE: key-events/aircraft-instrumentation-events/
- SDK-MISCE: key-events/miscellaneous-events/
- SDK-AMISCE: key-events/aircraft-miscellaneous-events/
- SDK-ENGE: key-events/aircraft-engine-events/

### Phase 2 Trim and Views pages

For [phase2-trim-views.md](phase2-trim-views.md) (the child pages behind main page keys 1,7 `TRIM` and
1,8 `VIEWS`; positions below are on those pages). Rows are **Unverified** until the Phase 2 trim and
views checks pass, unless the Verified column says otherwise. The view K-events were tested in the sim on
2026-11-11 (LR95-C2): the plugin sent them and MSFS 2024 ignored them, so their keys are Empty; the rows
stay as a record ("does not work" for the five that were pressed, "not tested" for the rest).

| Function | Read | Units | Write | Fallback | Source | Verified |
|---|---|---|---|---|---|---|
| Elevator trim up (trim 2,2) | none (the trim gauge 3,4) | | `K:ELEV_TRIM_UP` | input event `B:handling_elevatortrim_wheel` (values unknown, not used) | SDK-FCE; IE 182 | Unverified |
| Elevator trim down (trim 4,2) | none (the trim gauge 3,4) | | `K:ELEV_TRIM_DN` | as trim up | SDK-FCE; IE 182 | Unverified |
| Elevator trim position, percent (trim gauge 3,4; readout 3,2 until P3-TRIM2) | `(A:ELEVATOR TRIM PCT EX2, percent)` | percent, -100 (down limit) to 100 (up limit), 0 = 0° | (read only here; the SimVar is settable, SDK-CTLV) | `(A:ELEVATOR TRIM PCT, percent)` (legacy SimVar) | SDK-CTLV; SDK-UNITS | Unverified |
| Elevator trim deflection (not on a key since P3-TRIM2, a fallback lead; was trim 3,3) | `(A:ELEVATOR TRIM POSITION, degrees)` | degrees | (read only here; the SimVar is settable, SDK-CTLV) | none | SDK-CTLV; SDK-UNITS | Unverified |
| Yoke trim switch (not on a key) | `B:handling_elevatortrim_yoke` exists | unknown | not used | | IE 183 | Unverified (not used) |
| Trim disconnect (not on a key) | `B:handling_trim_disconnect` exists | unknown | not used | | IE 185 | Unverified (not used) |
| Cockpit view (views 1,2) | `(A:CAMERA STATE, Enum)`, On `2` (cockpit) / Off `3` | Enum | `(A:CAMERA STATE, Enum)` A-Var write (command type 12), On Value `$=2` (always writes 2), Off Value empty | EXTERNAL (views 1,3) also returns to the cockpit from the external view | SDK-CAMV; README 2.1.1, 2.1.2; SDK-UNITS | Unverified |
| External (chase) view (views 1,3) | `(A:CAMERA STATE, Enum)`, On `3` / Off `2` | Enum | `(A:CAMERA STATE, Enum)` A-Var write (command type 12), On Value `$2,=3<` (2 -> 3, 3 -> 2, other -> 3), Off Value empty | none | SDK-CAMV; README 2.1.1, 2.1.2; SDK-UNITS | Verified 2026-11-11 (LR101-C2: the user's hand test of this key; plugin log wrote 3, 2, 3, camera state followed); sim version with the follow-up |
| Cockpit view by K-event (was views 1,2; not on the page) | none | | `K:VIEW_VIRTUAL_COCKPIT_FORWARD` | `K:VIEW_COCKPIT_FORWARD`: not tested, left out with the K-event view family (LR95-C2) | SDK-VCE | does not work (2026-11-11, LR95-C2) |
| External view by K-event (was views 1,3; not on the page) | none | | `K:CHASE_VIEW_TOGGLE` | `K:VIEW_MODE` (see below) | SDK-VCE | does not work (2026-11-11, LR95-C2) |
| Camera state readout (views 1,4) | `(A:CAMERA STATE, Enum)` | Enum (2 Cockpit, 3 Chase Plane Drone, 4 Fixed On Plane, 5 Environment 6DOF, 7 Showcase, 8 Drone Plane); 2 = cockpit, 3 = external, seen in the sim 2026-11-11 (LR95-C2) | A-Var write, values 2 and 3, by views 1,2 and 1,3 (rows above); SDK-CAMV marks it settable | none | SDK-CAMV; SDK-UNITS | Unverified |
| View type readout (views 1,5) | `(A:CAMERA VIEW TYPE AND INDEX:0, Enum)` | Enum (0 default, 1 Pilot View, 2 Instruments, 3 Quickview, 4 Quickview External, 5 View) | (read only here; the SimVar is settable) | none | SDK-CAMV; SDK-UNITS | Unverified |
| View option readout (views 1,6) | `(A:CAMERA VIEW TYPE AND INDEX:1, number)` | number | (read only here; the SimVar is settable) | none | SDK-CAMV; SDK-UNITS | Unverified |
| Previous / next view category (was views 2,1 / 2,2; now Empty) | none | | `K:VIEW_MODE_REV` / `K:VIEW_MODE` | none | SDK-VCE | not tested, left out with the K-event view family (LR95-C2) |
| Previous / next view in the category (was views 2,3 / 2,4; now Empty) | none | | `K:PREV_SUB_VIEW` / `K:NEXT_SUB_VIEW` | none | SDK-VCE | does not work (2026-11-11, LR95-C2) |
| View reset (was views 2,5; now Empty) | none | | `K:VIEW_RESET` | none | SDK-VCE | does not work (2026-11-11, LR95-C2) |
| Zoom out / in (was views 2,6 / 2,7; now Empty) | none | | `K:ZOOM_MINUS` / `K:ZOOM_PLUS` | none | SDK-VCE | not tested, left out with the K-event view family (LR95-C2) |
| Previous view toggle (was views 2,8; now Empty) | none | | `K:VIEW_PREVIOUS_TOGGLE` | none | SDK-VCE | not tested, left out with the K-event view family (LR95-C2) |
| Camera select 1 to 9, 0 (was views 3,1 to 3,8, 4,1, 4,2; now Empty) | none | | `K:VIEW_CAMERA_SELECT_1`, `K:VIEW_CAMERA_SELECT_2`, `K:VIEW_CAMERA_SELECT_3`, `K:VIEW_CAMERA_SELECT_4`, `K:VIEW_CAMERA_SELECT_5`, `K:VIEW_CAMERA_SELECT_6`, `K:VIEW_CAMERA_SELECT_7`, `K:VIEW_CAMERA_SELECT_8`, `K:VIEW_CAMERA_SELECT_9`, `K:VIEW_CAMERA_SELECT_0` (which view each selects is not documented) | none | SDK-VCE | not tested, left out with the K-event view family (LR95-C2) |

The trim gauge (trim 3,4, P3-4, Display Gauge) reads `(A:ELEVATOR TRIM PCT EX2, percent)` (the row "Elevator trim position, percent" above), Minimum -100 / Maximum 100; Unverified.

The view events are aircraft-independent (they act on the sim's camera, not the C172); they are listed
here because every event the project uses goes in this file. Sources as above, plus:
- SDK-VCE: key-events/view-and-camera-events/
- SDK-CAMV: simvars/camera-variables/

### Phase 3 aileron and rudder trim (P3-TRIM2)

On the trim page ([phase2-trim-views.md](phase2-trim-views.md)). The 2024 C172 G1000 has no cockpit aileron or
rudder trim control (no such input event, IE), so the keys send the sim's generic trim K-events. All rows are
**Unverified** until the checklist section "P3-TRIM2: Aileron and rudder trim (C172 G1000)" passes; whether
the C172's flight model honours the events is open (the user's keyboard J / L, bound to aileron trim left /
right, "seem to work in C172", LR742-C16; U / O, rudder trim, not yet tried, LR743-C16).

| Function | Read | Units | Write | Fallback | Source | Verified |
|---|---|---|---|---|---|---|
| Aileron trim left / right (trim 2,6 / 2,8) | none (the gauge trim 2,7) | | `K:AILERON_TRIM_LEFT` / `K:AILERON_TRIM_RIGHT` ("Increments the left [right] aileron trim by 0.001") | none (no aileron trim input event) | SDK-FCE; IE | Unverified |
| Aileron trim position (trim 2,7, Display Gauge) | `(A:AILERON TRIM PCT, percent)`, Format `1.1` | percent, -100 to 100, 0 = no trim (SDK: "between -1 and 1"; unit "Float", MSFS 2020 SDK "Percent Over 100") | (read only here; the SimVar is settable, SDK-CTLV) | `(A:AILERON TRIM PCT, percent over 100)` with Scalar 100 (lead: TorontoWill's generic profile); `(A:AILERON TRIM, degrees)` | SDK-CTLV; SDK20-CTLV; SDK-UNITS | Unverified |
| Rudder trim left / right (trim 3,6 / 3,8) | none (the gauge trim 3,7) | | `K:RUDDER_TRIM_LEFT` / `K:RUDDER_TRIM_RIGHT` ("Increments rudder trim left [right]"; step not stated) | none (no rudder trim input event) | SDK-FCE; IE | Unverified |
| Rudder trim position (trim 3,7, Display Gauge) | `(A:RUDDER TRIM PCT, percent)`, Format `1.1` | percent, -100 to 100, 0 = no trim (SDK: "between -1 and 1"; unit "Float", MSFS 2020 SDK "Percent Over 100") | (read only here; the SimVar is settable, SDK-CTLV) | `(A:RUDDER TRIM PCT, percent over 100)` with Scalar 100; `(A:RUDDER TRIM, degrees)` | SDK-CTLV; SDK20-CTLV; SDK-UNITS | Unverified |
| Aileron / rudder trim disabled (not on a key; for the `tools/scmon` check) | `AILERON TRIM DISABLED`, `RUDDER TRIM DISABLED` | Bool | not used | | SDK-CTLV | Unverified (not used) |

Sources as the trim and views section above (SDK-FCE: key-events/aircraft-flight-control-events/, sections
Ailerons and Rudder; SDK-CTLV: simvars/aircraft-simvars/aircraft-control-variables/), plus SDK20-CTLV: the MSFS
2020 SDK's Aircraft_Control_Variables page (`AILERON TRIM PCT`, `RUDDER TRIM PCT`: "Percent Over 100").

### Phase 2 G1000 bezel and V-speeds pages

For [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md) (the second-level pages behind MORE: main page key
4,8 `MORE`, then MORE 1,2 `PFD`, 1,3 `MFD`, 1,4 `V-SPEEDS`; positions below are on those pages). All rows
are **Unverified** until the Phase 2 G1000 and V-speeds checks pass. The PFD and MFD pages have the same
layout: each row names the PFD event and the MFD event of one bezel control. If a bezel key does nothing in
the sim test, its row is marked "does not work" and stays; the key becomes Empty.

| Function | Read | Units | Write | Fallback | Source | Verified |
|---|---|---|---|---|---|---|
| Direct-To button (pfd 1,2 and mfd 1,2, `DIRECT`) | none (H-events can't be read) | | `H:AS1000_PFD_DIRECTTO` / `H:AS1000_MFD_DIRECTTO` (H-event, command type 8) (EX-G1000 has the MFD one) | input event `B:as1000_directto_pfd` / `B:as1000_directto_mfd` (value unknown: hand test first) | SDK-AS1000; SDK-RPN; EX-G1000; IE 66, 65; README 2.1.1 | Unverified |
| MENU button (pfd 1,3 and mfd 1,3, `MENU`) | none (H-events can't be read) | | `H:AS1000_PFD_MENU_Push` / `H:AS1000_MFD_MENU_Push` (H-event, command type 8) (EX-G1000 has the MFD one) | input event `B:as1000_menu_push_pfd` / `B:as1000_menu_push_mfd` (value unknown: hand test first) | SDK-AS1000; SDK-RPN; EX-G1000; IE 89, 88; README 2.1.1 | Unverified |
| FPL button (pfd 1,4 and mfd 1,4, `FPL`) | none (H-events can't be read) | | `H:AS1000_PFD_FPL_Push` / `H:AS1000_MFD_FPL_Push` (H-event, command type 8) (EX-G1000 has the MFD one) | input event `B:as1000_fpl_push_pfd` / `B:as1000_fpl_push_mfd` (value unknown: hand test first) | SDK-AS1000; SDK-RPN; EX-G1000; IE 78, 77; README 2.1.1 | Unverified |
| PROC button (pfd 1,5 and mfd 1,5, `PROC`) | none (H-events can't be read) | | `H:AS1000_PFD_PROC_Push` / `H:AS1000_MFD_PROC_Push` (H-event, command type 8) (EX-G1000 has the MFD one) | input event `B:as1000_proc_push_pfd` / `B:as1000_proc_push_mfd` (value unknown: hand test first) | SDK-AS1000; SDK-RPN; EX-G1000; IE 107, 106; README 2.1.1 | Unverified |
| CLR button (pfd 1,6 and mfd 1,6, `CLR`) | none (H-events can't be read) | | `H:AS1000_PFD_CLR` / `H:AS1000_MFD_CLR` (H-event, command type 8) (EX-G1000 has the MFD one) | input event `B:as1000_clr_pfd` / `B:as1000_clr_mfd` (value unknown: hand test first) | SDK-AS1000; SDK-RPN; EX-G1000; IE 40, 39; README 2.1.1 | Unverified |
| CLR button, long press (2 s) (pfd 1,7 and mfd 1,7, `CLR HOLD`) | none (H-events can't be read) | | `H:AS1000_PFD_CLR_Long` / `H:AS1000_MFD_CLR_Long` (H-event, command type 8) | input event `B:as1000_clr_pfd` / `B:as1000_clr_mfd` (value unknown: hand test first) | SDK-AS1000; SDK-RPN; EX-G1000; IE 40, 39; README 2.1.1 | Unverified |
| ENT button (pfd 1,8 and mfd 1,8, `ENT`) | none (H-events can't be read) | | `H:AS1000_PFD_ENT_Push` / `H:AS1000_MFD_ENT_Push` (H-event, command type 8) (EX-G1000 has the MFD one) | input event `B:as1000_ent_push_pfd` / `B:as1000_ent_push_mfd` (value unknown: hand test first) | SDK-AS1000; SDK-RPN; EX-G1000; IE 70, 69; README 2.1.1 | Unverified |
| FMS inner knob push (pfd 2,1 and mfd 2,1, `FMS PUSH`) | none (H-events can't be read) | | `H:AS1000_PFD_FMS_Upper_PUSH` / `H:AS1000_MFD_FMS_Upper_PUSH` (H-event, command type 8) | input event `B:as1000_fms_upper_push_pfd` / `B:as1000_fms_upper_push_mfd` (value unknown: hand test first) | SDK-AS1000; SDK-RPN; EX-G1000; IE 76, 75; README 2.1.1 | Unverified |
| FMS outer knob, one step down (pfd 2,2 and mfd 2,2, `FMS OUT-`) | none (H-events can't be read) | | `H:AS1000_PFD_FMS_Lower_DEC` / `H:AS1000_MFD_FMS_Lower_DEC` (H-event, command type 8) | input event `B:as1000_fms_lower_pfd` / `B:as1000_fms_lower_mfd` (value unknown: hand test first) | SDK-AS1000; SDK-RPN; EX-G1000; IE 72, 71; README 2.1.1 | Unverified |
| FMS outer knob, one step up (pfd 2,3 and mfd 2,3, `FMS OUT+`) | none (H-events can't be read) | | `H:AS1000_PFD_FMS_Lower_INC` / `H:AS1000_MFD_FMS_Lower_INC` (H-event, command type 8) | input event `B:as1000_fms_lower_pfd` / `B:as1000_fms_lower_mfd` (value unknown: hand test first) | SDK-AS1000; SDK-RPN; EX-G1000; IE 72, 71; README 2.1.1 | Unverified |
| FMS inner knob, one step down (pfd 2,4 and mfd 2,4, `FMS IN-`) | none (H-events can't be read) | | `H:AS1000_PFD_FMS_Upper_DEC` / `H:AS1000_MFD_FMS_Upper_DEC` (H-event, command type 8) | input event `B:as1000_fms_upper_pfd` / `B:as1000_fms_upper_mfd` (value unknown: hand test first) | SDK-AS1000; SDK-RPN; EX-G1000; IE 74, 73; README 2.1.1 | Unverified |
| FMS inner knob, one step up (pfd 2,5 and mfd 2,5, `FMS IN+`) | none (H-events can't be read) | | `H:AS1000_PFD_FMS_Upper_INC` / `H:AS1000_MFD_FMS_Upper_INC` (H-event, command type 8) | input event `B:as1000_fms_upper_pfd` / `B:as1000_fms_upper_mfd` (value unknown: hand test first) | SDK-AS1000; SDK-RPN; EX-G1000; IE 74, 73; README 2.1.1 | Unverified |
| Range knob, one step down (pfd 2,6 and mfd 2,6, `RANGE-`) | none (H-events can't be read) | | `H:AS1000_PFD_RANGE_DEC` / `H:AS1000_MFD_RANGE_DEC` (H-event, command type 8) | input event `B:as1000_range_zoom_pfd` / `B:as1000_range_zoom_mfd` (the range knob, likely; `B:as1000_range_pfd` / `B:as1000_range_mfd` the other candidate; value unknown: hand test first) | SDK-AS1000; SDK-RPN; EX-G1000; IE 113, 112 (likely), IE 109, 108 (the other candidate); README 2.1.1 | Unverified |
| Range knob, one step up (pfd 2,7 and mfd 2,7, `RANGE+`) | none (H-events can't be read) | | `H:AS1000_PFD_RANGE_INC` / `H:AS1000_MFD_RANGE_INC` (H-event, command type 8) | input event `B:as1000_range_zoom_pfd` / `B:as1000_range_zoom_mfd` (the range knob, likely; `B:as1000_range_pfd` / `B:as1000_range_mfd` the other candidate; value unknown: hand test first) | SDK-AS1000; SDK-RPN; EX-G1000; IE 113, 112 (likely), IE 109, 108 (the other candidate); README 2.1.1 | Unverified |
| Range knob push (joystick push) (pfd 2,8 and mfd 2,8, `RNG PUSH`) | none (H-events can't be read) | | `H:AS1000_PFD_JOYSTICK_PUSH` / `H:AS1000_MFD_JOYSTICK_PUSH` (H-event, command type 8) | input event `B:as1000_range_push_pfd` / `B:as1000_range_push_mfd` (value unknown: hand test first) | SDK-AS1000; SDK-RPN; EX-G1000; IE 111, 110; README 2.1.1 | Unverified |
| Softkey 1 (pfd 3,1 and mfd 3,1, `SK 1`) | none (H-events can't be read) | | `H:AS1000_PFD_SOFTKEYS_1` / `H:AS1000_MFD_SOFTKEYS_1` (H-event, command type 8) | input event `B:as1000_softkey_1_pfd` / `B:as1000_softkey_1_mfd` (value unknown: hand test first) | SDK-AS1000; SDK-RPN; EX-G1000; IE 115, 114; README 2.1.1 | Unverified |
| Softkey 2 (pfd 3,2 and mfd 3,2, `SK 2`) | none (H-events can't be read) | | `H:AS1000_PFD_SOFTKEYS_2` / `H:AS1000_MFD_SOFTKEYS_2` (H-event, command type 8) | input event `B:as1000_softkey_2_pfd` / `B:as1000_softkey_2_mfd` (value unknown: hand test first) | SDK-AS1000; SDK-RPN; EX-G1000; IE 123, 122; README 2.1.1 | Unverified |
| Softkey 3 (pfd 3,3 and mfd 3,3, `SK 3`) | none (H-events can't be read) | | `H:AS1000_PFD_SOFTKEYS_3` / `H:AS1000_MFD_SOFTKEYS_3` (H-event, command type 8) | input event `B:as1000_softkey_3_pfd` / `B:as1000_softkey_3_mfd` (value unknown: hand test first) | SDK-AS1000; SDK-RPN; EX-G1000; IE 125, 124; README 2.1.1 | Unverified |
| Softkey 4 (pfd 3,4 and mfd 3,4, `SK 4`) | none (H-events can't be read) | | `H:AS1000_PFD_SOFTKEYS_4` / `H:AS1000_MFD_SOFTKEYS_4` (H-event, command type 8) | input event `B:as1000_softkey_4_pfd` / `B:as1000_softkey_4_mfd` (value unknown: hand test first) | SDK-AS1000; SDK-RPN; EX-G1000; IE 127, 126; README 2.1.1 | Unverified |
| Softkey 5 (pfd 3,5 and mfd 3,5, `SK 5`) | none (H-events can't be read) | | `H:AS1000_PFD_SOFTKEYS_5` / `H:AS1000_MFD_SOFTKEYS_5` (H-event, command type 8) | input event `B:as1000_softkey_5_pfd` / `B:as1000_softkey_5_mfd` (value unknown: hand test first) | SDK-AS1000; SDK-RPN; EX-G1000; IE 129, 128; README 2.1.1 | Unverified |
| Softkey 6 (pfd 3,6 and mfd 3,6, `SK 6`) | none (H-events can't be read) | | `H:AS1000_PFD_SOFTKEYS_6` / `H:AS1000_MFD_SOFTKEYS_6` (H-event, command type 8) | input event `B:as1000_softkey_6_pfd` / `B:as1000_softkey_6_mfd` (value unknown: hand test first) | SDK-AS1000; SDK-RPN; EX-G1000; IE 131, 130; README 2.1.1 | Unverified |
| Softkey 7 (pfd 4,1 and mfd 4,1, `SK 7`) | none (H-events can't be read) | | `H:AS1000_PFD_SOFTKEYS_7` / `H:AS1000_MFD_SOFTKEYS_7` (H-event, command type 8) | input event `B:as1000_softkey_7_pfd` / `B:as1000_softkey_7_mfd` (value unknown: hand test first) | SDK-AS1000; SDK-RPN; EX-G1000; IE 133, 132; README 2.1.1 | Unverified |
| Softkey 8 (pfd 4,2 and mfd 4,2, `SK 8`) | none (H-events can't be read) | | `H:AS1000_PFD_SOFTKEYS_8` / `H:AS1000_MFD_SOFTKEYS_8` (H-event, command type 8) | input event `B:as1000_softkey_8_pfd` / `B:as1000_softkey_8_mfd` (value unknown: hand test first) | SDK-AS1000; SDK-RPN; EX-G1000; IE 135, 134; README 2.1.1 | Unverified |
| Softkey 9 (pfd 4,3 and mfd 4,3, `SK 9`) | none (H-events can't be read) | | `H:AS1000_PFD_SOFTKEYS_9` / `H:AS1000_MFD_SOFTKEYS_9` (H-event, command type 8) | input event `B:as1000_softkey_9_pfd` / `B:as1000_softkey_9_mfd` (value unknown: hand test first) | SDK-AS1000; SDK-RPN; EX-G1000; IE 137, 136; README 2.1.1 | Unverified |
| Softkey 10 (pfd 4,4 and mfd 4,4, `SK 10`) | none (H-events can't be read) | | `H:AS1000_PFD_SOFTKEYS_10` / `H:AS1000_MFD_SOFTKEYS_10` (H-event, command type 8) | input event `B:as1000_softkey_10_pfd` / `B:as1000_softkey_10_mfd` (value unknown: hand test first) | SDK-AS1000; SDK-RPN; EX-G1000; IE 117, 116; README 2.1.1 | Unverified |
| Softkey 11 (pfd 4,5 and mfd 4,5, `SK 11`) | none (H-events can't be read) | | `H:AS1000_PFD_SOFTKEYS_11` / `H:AS1000_MFD_SOFTKEYS_11` (H-event, command type 8) | input event `B:as1000_softkey_11_pfd` / `B:as1000_softkey_11_mfd` (value unknown: hand test first) | SDK-AS1000; SDK-RPN; EX-G1000; IE 119, 118; README 2.1.1 | Unverified |
| Softkey 12 (pfd 4,6 and mfd 4,6, `SK 12`) | none (H-events can't be read) | | `H:AS1000_PFD_SOFTKEYS_12` / `H:AS1000_MFD_SOFTKEYS_12` (H-event, command type 8) | input event `B:as1000_softkey_12_pfd` / `B:as1000_softkey_12_mfd` (value unknown: hand test first) | SDK-AS1000; SDK-RPN; EX-G1000; IE 121, 120; README 2.1.1 | Unverified |
| Stall speed, flaps fully extended (vspeeds 1,2, `VS0`) | `(A:DESIGN SPEED VS0, knots)`, Format `1.0` | kias in the SDK; read in knots; design constant | (read only; not settable in the SDK) | none | SDK-FMV; SDK-UNITS | Unverified |
| Stall speed, flaps fully retracted (vspeeds 1,3, `VS1`) | `(A:DESIGN SPEED VS1, knots)`, Format `1.0` | kias in the SDK; read in knots; design constant | (read only; not settable in the SDK) | none | SDK-FMV; SDK-UNITS | Unverified |
| Minimum rotation speed (vspeeds 1,4, `VR`) | `(A:DESIGN SPEED MIN ROTATION, knots)`, Format `1.0` | ft/s in the SDK; read in knots; design constant | (read only; not settable in the SDK) | none | SDK-FMV; SDK-UNITS | Unverified |
| Climb speed, the sim's `climb_speed` (not defined as Vy) (vspeeds 1,6, `CLIMB`) | `(A:DESIGN SPEED CLIMB, knots)`, Format `1.0` | ft/s in the SDK; read in knots; design constant | (read only; not settable in the SDK) | none | SDK-FMV; SDK-CFG; SDK-UNITS | Unverified |
| Design cruise speed, a true airspeed (cfg `cruise_speed`, ktas; not Vno) (vspeeds 2,2, `CRUISE`) | `(A:DESIGN SPEED VC, knots)`, Format `1.0` | ft/s in the SDK; true airspeed (ktas in the cfg); read in knots; design constant | (read only; not settable in the SDK) | none | SDK-FMV; SDK-CFG; SDK-UNITS | Unverified |
| Maximum IAS (vspeeds 2,4, `VNE`) | `(A:REFERENCE SPEED MAX IAS, knots)`, Format `1.0` | knots; design constant | (read only; not settable in the SDK) | none | SDK-FMV; SDK-UNITS | Unverified |
| Maximum speed for the current flap position (vspeeds 2,5, `VFE`) | `(A:FLAPS CURRENT SPEED LIMITATION, knots)`, Format `1.0` | knots; changes with the flaps | (read only; not settable in the SDK) | none | SDK-CTLV; SDK-UNITS | Unverified |
| Vx (vspeeds 1,5, Empty) | no SimVar in the MSFS 2024 SDK (flight_model.cfg holds it as `best_angle_climb_speed`; no SimVar reads it) | | | none | SDK-FMV; SDK-CFG | not on a key |
| Vno (vspeeds 2,3, Empty) | no SimVar in the MSFS 2024 SDK (flight_model.cfg holds it as `normal_operating_speed`; no SimVar reads it; `(A:ESTIMATED CRUISE SPEED, knots)`, a lead from Jiblet's package, is "Estimated cruise speed", not Vno: dropped) | | | none | SDK-FMV; SDK-CFG | not on a key |

H-events are aircraft-panel events: PilotsDeck sends them through the MobiFlight WASM module (PilotsDeck source
`Plugin/Simulator/ConnectorMSFS.cs` and `Plugin/Simulator/MSFS/ToolsMSFS.cs`; README 1.4 says only that the
installer installs the module).
Sources as above, plus:
- SDK-FMV: simvars/aircraft-simvars/aircraft-flight-model-variables/
- SDK-CFG: https://docs.flightsimulator.com/msfs2024/retail/content-configuration/cfg-files/flight_model.cfg/ ([REFERENCE SPEEDS])
- SDK-RPN: reverse-polish-notation/ (H: events in MSFS 2024 cockpit panels)
- SDK-AS1000: the SDK Template Explorer page `Asobo\GlassCockpit\AS1000.xml`,
  https://docs.flightsimulator.com/html/Content_Configuration/Models/ModelBehaviors/TemplateExplorer/Asobo/GlassCockpit/AS1000.html
  (the SDK documentation's general section; no MSFS 2024 copy found)
- EX-G1000: the user's installed profile `G1000` (ProfilesV3 `4A4C2DB1-...`, page `EC7CA592-...`): six keys
  of the Generic package (TorontoWill v1.3, zip dated 2025-01-26, profile format 2.0), saved with a pre-0.8.9
  PilotsDeck (BUILD_VERSION 7, no Plugin block), imported 2026-11-11 02:35 when the Stream Deck app wrote the
  0.9.7.0 Plugin block; command type 8 with `H:AS1000_MFD_*` addresses. They show the address form only and
  were never pressed on this PC. Command type 8 itself: the installed `pi-Common.js` line 215 and the source
  `SimCommand.cs` (`HVAR = 8`), on the 0.9.7 template `simple_button` (see the page doc; ruling LR144-C4)

### Phase 2 sim rate page

For [phase2-sim-rate.md](phase2-sim-rate.md) (the child page behind main page key 3,7 `SIM RATE`; positions
below are on that page). First sim test 2026-11-12 (LR259-C5, LR263-C5; sim version not recorded); repaired
in P2-6R, not yet sim-tested again; new layout on the user's word (LR298-C5): 1,2 `1X`, 1,3 `SLOWER`, 1,4 `RATE`,
1,5 `FASTER`. All rows are **Unverified** until the hand test HT-C and the Phase 2 sim rate checks pass.
The sim rate is not tied to the C172: the events and the variable act on the sim; they are listed here
because every event the project uses goes in this file. If an event does nothing in the sim test, its row is
marked "does not work" and stays.

| Function | Read | Units | Write | Fallback | Source | Verified |
|---|---|---|---|---|---|---|
| Sim rate readout (simrate 1,4, `RATE`; also the read of 1,2 `1X` and of the script `XL24-SIMRATE.lua`) | `(A:SIMULATION RATE, number)` (the environment variable `SIMULATION RATE`; PilotsDeck reads `A:` and `E:` alike), Format `1.2` | Number: 0.0625 to 128, powers of two, 1 = real time | (read only here; the SDK marks it get/set, but no A-Var or E-Var write for the sim rate, LR153-C4) | `(E:SIMULATION RATE, number)` (the same request) | SDK-ENVV; PD-SRC (TypeMatching.cs, SubManager.cs); README 2.1.1 | Unverified |
| Set sim rate 1x (simrate 1,2 `1X`) | `(A:SIMULATION RATE, number)`: On `1` / Off `2` (no image at any other rate, PD-SRC ActionSwitchDisplay.cs) | | `lua:XL24-SIMRATE:SET(1)` (command type 14, Lua Function): the script steps the rate with `K:SIM_RATE_INCR` / `K:SIM_RATE_DECR`, one event at a time against the read rate, until it is 1x (at most 8 steps per press; stops when the rate stays or passes 1x) | SLOWER, FASTER and RATE | README 2.1.1 LUAFUNC, 3.5.1; SDK-MISCE; PD-SRC (ConnectorNone.cs, ManagedScript.cs, ScriptManager.cs); PD-PI line 196; LR153-C4, LR277-C5, LR298-C5 | Unverified |
| Set sim rate 2x, 4x (the P2-6R build's simrate 1,3 `2X`, 1,4 `4X`) | `(A:SIMULATION RATE, number)`: 2X On `2` / Off `1`, 4X On `4` / Off `1` | | `lua:XL24-SIMRATE:SET(2)`, `lua:XL24-SIMRATE:SET(4)` (command type 14) | | README 2.1.1 LUAFUNC; LR277-C5 | removed in P2-6R (LR298-C5): the user's layout has no 2X or 4X key; never sim-tested |
| Set sim rate by `K:SIM_RATE_SET` (the first build of 1X/2X/4X, replaced in P2-6R) | as above | | `K:SIM_RATE_SET:1`, `K:SIM_RATE_SET:2`, `K:SIM_RATE_SET:4` (K-event with one parameter, command type 16; the SDK doesn't define the parameter) | the x256 scale (`K:SIM_RATE_SET:256` = 1x; a lead from the FSUIPC offset 0x0C1A, never tried: its hand test went with the 2X key, LR298-C5) | SDK-MISCE; README 2.1.1; PD-SRC (ToolsMSFS.cs); PD-PI line 195; LR161-C4 | does not work (2026-11-12, LR259-C5, LR263-C5; sim version not recorded): sent with no error (plugin log), the rate did not change |
| Sim rate one step up (simrate 1,4 `RATE`, press; also sent by the script) | readout as above | | `K:SIM_RATE_INCR` | FASTER (1,5) | SDK-MISCE | Unverified; worked in the sim 2026-11-12 (LR263-C5); sim version not recorded |
| Sim rate one step up (simrate 1,5 `FASTER`, press) | none (RATE shows the result) | | `K:SIM_RATE_INCR` | RATE press | SDK-MISCE; LR298-C5 | Unverified |
| Sim rate one step down (simrate 1,4 `RATE`, long press: hold at least 0.5 s; also sent by the script) | readout as above | | `K:SIM_RATE_DECR` (Second command, `HasLongPress`) | SLOWER (1,3) | SDK-MISCE; README 2.1; PD-SRC (ActionBaseSimple.cs, ActionCommand.cs, AppConfiguration.cs) | Unverified; not fired 2026-11-12: holds 0.06-0.25 s < 500 ms (plugin log, no "Build Long Command") |
| Sim rate one step down (simrate 1,3 `SLOWER`, press) | none (RATE shows the result) | | `K:SIM_RATE_DECR` | RATE long press | SDK-MISCE | Unverified |

Sources as above (SDK-MISCE, "Sim Rate" section: `SIM_RATE_SET` "[0] Value", "Set the simulation rate.";
`SIM_RATE_INCR`, `SIM_RATE_DECR` without a parameter), plus:
- SDK-ENVV: environment-variables/ (`SIMULATION RATE`)
- PD-SRC: PilotsDeck source at commit 11bdf1f7daf4828f822c18919952fe5b66153e58, `Plugin/Tools/TypeMatching.cs`,
  `Plugin/Simulator/MSFS/SubManager.cs`, `Plugin/Simulator/MSFS/ToolsMSFS.cs`,
  `Plugin/Actions/Simple/ActionBaseSimple.cs`, `Plugin/Actions/Simple/ActionCommand.cs`, `Plugin/AppConfiguration.cs`
  (long press only when held >= LongPressTime, default 500 ms), `Plugin/Simulator/ConnectorNone.cs` (a Lua Function
  command runs on its own task), `Plugin/Resources/Scripts/ManagedScript.cs` (`SimVar`, `SimRead`, `SimCommand`,
  `Sleep`, `Log`), `Plugin/Resources/ScriptManager.cs` (`RunFunction`), `Plugin/Simulator/MSFS/SubMapping.cs`
  (OnReceived: updates the variable `SimRead` returns each time the sim sends a new value)
- PD-PI: the installed plugin's `Plugin/PI/js/pi-Common.js` lines 195 (`rxKvarCmd`) and 196 (`regLuaFunc`)
- README 2.1 (Second command ">= 500ms"), 2.1.1 LUAFUNC, 3.5.1 (the script functions)
- The plugin log `PilotsDeck20261112.log` (read only, searched): the K:SIM_RATE_SET sends with no error; RATE
  "Key TimeDiff" 0.06 to 0.25 s; no "Build Long Command"
- LR161-C4, LR153-C4: the coordinator's rulings in the chain ledger (2026-11-12); LR259-C5, LR263-C5: the user's
  sim test reports (2026-11-12); LR277-C5: the P2-6R rulings (Lua stepping, SLOWER, `K:SIM_RATE_INCR` stays
  Unverified without a sim version); LR298-C5: the user's layout (1X, SLOWER, RATE, FASTER; 2X and 4X removed)
- PD-SRC `Plugin/Actions/Simple/ActionSwitchDisplay.cs` (`Refresh()`: no On/Off image when the value matches neither
  On nor Off and Special State is off)

### Phase 2 COM1 pad

For [phase2-com1-pad.md](phase2-com1-pad.md) (the second-level page behind MORE 1,5 `COM PAD`; positions
below are on that page). Generated, not yet sim-tested: all rows are Unverified until the checklist section
"Phase 2: COM1 pad (C172 G1000)" passes. The COM1 key on the page (1,2) is the main page's 3,1 key (row
above, reused). The trim gauge
([design-trim-gauge.md](design-trim-gauge.md)) adds no row: it reads `ELEVATOR TRIM PCT EX2`, already
listed under the trim page.

| Function | Read | Units | Write | Fallback | Source | Verified |
|---|---|---|---|---|---|---|
| Set COM1 standby frequency (compad 4,8 `ENT`, by the script `XL24-COMPAD.lua`) | `(A:COM STANDBY FREQUENCY:1, MHz)` (compad 1,2, as main 3,1) | Hz parameter, 118000000 to 136990000 | `K:COM_STBY_RADIO_SET_HZ:<Hz>` sent by `SimCommand` | `K:COM_STBY_RADIO_SET` (BCD16; two decimals only) | SDK-RADE; README 2.1.1, 3.5.1 | Unverified |
| Set COM1 and make it active (compad 4,8 `ENT`, long press) | `(A:COM ACTIVE FREQUENCY:1, MHz)` | | `K:COM_STBY_RADIO_SET_HZ:<Hz>`, then `K:COM_STBY_RADIO_SWAP` after 100 ms | none | SDK-RADE | Unverified |
| COM1 channel spacing (read by the script for the 25 kHz shorthand) | `(A:COM SPACING MODE:1, Enum)` | Enum: 0 = 25 kHz, 1 = 8.33 kHz | (read only here) | none (without it, no shorthand) | SDK-RADV | Unverified |
| COM1 standby station ident (compad 2,2 `STBY ID`, optional) | `(A:COM STANDBY FREQ IDENT:1, String)` | String | (read only) | none (drop the key) | SDK-RADV | Unverified |
| Typed entry (compad 1,3 `ENTRY`) | `X:XL24_COMPAD_ENTRY` (PilotsDeck internal variable, written by the script) | String, e.g. `118.5__` | the script's `DIGIT(n)`, `BACK`, `CLEAR`, `ENTER`, `ENTER_SWAP` (`lua:XL24-COMPAD:...`, command type 14) | the script function as the key's Address instead of the `X:` variable | README 2.1.1 (INTERNAL, LUAFUNC); REF-GSX | Unverified |

Sources: SDK-RADE and SDK-RADV as above (read again 2026-11-12 for `COM_STBY_RADIO_SET_HZ`,
`COM SPACING MODE`, `COM STANDBY FREQ IDENT`); README = PilotsDeck README; REF-GSX = the GSX Pro reference
profile in ProfilesV3 (an `X:` string shown on a key, Lua commands of type 14), a lead only; PD-SRC =
PilotsDeck source (`SimCommand.cs` LUAFUNC = 14; `Plugin/Simulator/MSFS/SubMapping.cs` `OnReceived` at
11bdf1f7: a value that is not numeric is stored as text, so an A-Var with unit `String` shown as text is
Unverified), see phase2-com1-pad.md.

### Phase 3 autopilot page

For [phase3-autopilot.md](phase3-autopilot.md) (the second-level page behind MORE 1,6 `AUTOPILOT`; positions
below are on that page). Generated, not yet sim-tested: all rows are **Unverified** until the checklist
section "P3-1: Autopilot page (C172 G1000)" passes. The mode keys use the K-event even where the aircraft
lists an input event, because the value a B-Var push needs is unknown and the cockpit buttons drive the
same SimVars through these K-events (SDK-APT); VNV is the one B-Var key (no K-event or SimVar exists). The
reasons per key: phase3-autopilot.md, "Which route each key uses, and why". The mode rows repeat the Phase 2
main page rows' addresses (same pairs, a second key); the "Selected heading (Phase 3)" row at the top is the
HDG BUG readout below.

| Function | Read | Units | Write | Fallback | Source | Verified |
|---|---|---|---|---|---|---|
| AP master (autopilot 1,2 `AP`) | `(A:AUTOPILOT MASTER, Bool)` | Bool | `K:AP_MASTER` | none needed | SDK-APV; SDK-APE; IE 15 | Unverified on this page (the same pair passed on the Phase 1 key, 2026-11-11, row at the top) |
| Flight director (1,3 `FD`) | `(A:AUTOPILOT FLIGHT DIRECTOR ACTIVE, Bool)` | Bool | `K:TOGGLE_FLIGHT_DIRECTOR` | `B:as1000_autopilot_fd_pfd` (push value unknown) | SDK-APV; SDK-APE; SDK-APT; IE 21 | Unverified |
| AP heading mode (1,4 `HDG`) | `(A:AUTOPILOT HEADING LOCK, Bool)` | Bool | `K:AP_HDG_HOLD` | `K:AP_PANEL_HEADING_HOLD`, then `B:as1000_autopilot_heading_pfd` | SDK-APV; SDK-APE; SDK-APT; IE 25 | Unverified |
| AP NAV mode (1,5 `NAV`) | `(A:AUTOPILOT NAV1 LOCK, Bool)` | Bool | `K:AP_NAV1_HOLD` | `B:as1000_autopilot_navigation_pfd` | SDK-APV; SDK-APE; SDK-APT; IE 27 | Unverified |
| AP approach mode (1,6 `APR`) | `(A:AUTOPILOT APPROACH HOLD, Bool)` | Bool | `K:AP_APR_HOLD` | `B:as1000_autopilot_approach_pfd` | SDK-APV; SDK-APE; SDK-APT; IE 17 | Unverified |
| AP back course mode (1,7 `BC`) | `(A:AUTOPILOT BACKCOURSE HOLD, Bool)` | Bool | `K:AP_BC_HOLD` | `B:as1000_autopilot_backcourse_pfd` | SDK-APV; SDK-APE; SDK-APT; IE 19 | Unverified |
| AP vertical navigation (1,8 `VNV`) | `L:XMLVAR_VNAVButtonValue` (L-Var read; **weak source**: a general-path SDK template page and a pre-2024 profile, no 2024 source, A-6) | 0/1 assumed | `B:as1000_autopilot_vertical_navigation_pfd`, On `1` / Off `0` (command type 13) | write: an L-Var toggle of `L:XMLVAR_VNAVButtonValue` (needs a ruling and a TOOLS LOCK), else Empty; read: the B-Var itself, else no state; every second press only: the Reset Switch (`UseLvarReset`, README 2.1.2) | IE 29; SDK-APT; lead: Jiblet's C172 G1000 profile; README 2.1.1 | Unverified |
| AP altitude mode (2,1 `ALT`) | `(A:AUTOPILOT ALTITUDE LOCK, Bool)` | Bool | `K:AP_ALT_HOLD` | `K:AP_PANEL_ALTITUDE_HOLD`, then `B:as1000_autopilot_altitude_pfd` | SDK-APV; SDK-APE; SDK-APT; IE 13 | Unverified |
| AP vertical speed mode (3,1 `VS`) | `(A:AUTOPILOT VERTICAL HOLD, Bool)` | Bool | `K:AP_VS_HOLD` | `K:AP_PANEL_VS_HOLD`, then `B:as1000_autopilot_verticalspeed_pfd` | SDK-APV; SDK-APE; SDK-APT; IE 33 | Unverified |
| AP FLC mode (4,1 `FLC`) | `(A:AUTOPILOT FLIGHT LEVEL CHANGE, Bool)` | Bool | `K:FLIGHT_LEVEL_CHANGE` (does not set the speed target to IAS as the cockpit button does, A-9) | `B:as1000_autopilot_flightlevelchange_pfd`, or a Lua script with `K:AP_SPD_VAR_SET` (ruling needed) | SDK-APV; SDK-APE; SDK-APT; IE 23 | Unverified |
| Heading bug (3,2 `HDG BUG` readout; press = sync) | `(A:AUTOPILOT HEADING LOCK DIR, Degrees)`, Format `3.0:%s°` | Degrees, 0-359 | press `K:AP_HDG_CURRENT_HDG_SET` (no parameter = slot 0, A-5) | read `(A:AUTOPILOT HEADING LOCK DIR:1, Degrees)`; sync `K:AP_HDG_CURRENT_HDG_SET:1`, then `B:as1000_heading_sync_pfd` | SDK-APV; SDK-APE; IE 82; lead: forum report | Unverified |
| Heading bug step (2,2 `HDG+`, 4,2 `HDG-`) | none (HDG BUG shows it) | 1 degree expected; wrap 359-000 expected (checklist step 4) | `K:HEADING_BUG_INC`, `K:HEADING_BUG_DEC` | `B:as1000_heading_pfd` (value unknown) | SDK-APE; IE 80 | Unverified |
| NAV1 course (3,3 `CRS1` readout; press = CRS push) | `(A:NAV OBS:1, Degrees)`, Format `3.0:%s°` | Degrees | press `H:AS1000_PFD_CRS_PUSH` (command type 8) | `B:as1000_course_push_pfd` (value unknown) | SDK-RADV; SDK-AS1000; IE 64 | Unverified |
| Course step (2,3 `CRS+`, 4,3 `CRS-`; long press 10 degrees) | none (CRS1 shows it) | 1 degree; long press 10 degrees, stops at 0/360 | `H:AS1000_PFD_CRS_INC`, `H:AS1000_PFD_CRS_DEC`; long press `K:VOR1_OBI_FAST_INC`, `K:VOR1_OBI_FAST_DEC` | `K:VOR1_OBI_INC`, `K:VOR1_OBI_DEC` | SDK-AS1000; SDK-RADE; README 2.1; IE 62 | Unverified |
| Selected altitude (3,4 `ALT SEL` readout) | `(A:AUTOPILOT ALTITUDE LOCK VAR, Feet)`, Format `1.0` | Feet | (read only) | `(A:AUTOPILOT ALTITUDE LOCK VAR:1, Feet)` | SDK-APV | Unverified |
| Selected altitude step (2,4 `ALT+`, 4,4 `ALT-`) | none (ALT SEL shows it) | the sim's step, 100 ft expected; long press 1000 ft expected | `K:AP_ALT_VAR_INC`, `K:AP_ALT_VAR_DEC`; long press `K:AP_ALT_VAR_INC:1000`, `K:AP_ALT_VAR_DEC:1000` (**risk, A-4:** the SDK calls the parameter "New reference altitude", so the long press may set 1000 ft instead of stepping) | long press: the README sequence of ten single steps, or no long press; short press 1000 ft: `K:AP_ALT_VAR_INC:100` / `K:AP_ALT_VAR_DEC:100` | SDK-APE; SDK-AS1000; README 2.1.1, 2.1; IE 7, 9; lead: Jiblet passes 100 and 1000 | Unverified |
| Vertical speed target (3,5 `VS TGT` readout) | `(A:AUTOPILOT VERTICAL HOLD VAR, Feet/minute)`, Format `1.0` | ft/min, signed (no `+` drawn) | (read only) | none | SDK-APV; README 2.2.2 | Unverified |
| Vertical speed target step (2,5 `VS+`, 4,5 `VS-`) | none (VS TGT shows it) | the sim's step, 100 fpm expected | `K:AP_VS_VAR_INC`, `K:AP_VS_VAR_DEC` | `B:as1000_autopilot_verticalspeed_up_pfd` / `B:as1000_autopilot_verticalspeed_down_pfd` (value unknown) | SDK-APE; SDK-AS1000; IE 35, 31 | Unverified |
| FLC speed target (3,6 `FLC SPD` readout) | `(A:AUTOPILOT AIRSPEED HOLD VAR, Knots)`, Format `1.0` | Knots | (read only) | none | SDK-APV | Unverified |
| FLC speed target step (2,6 `SPD+`, 4,6 `SPD-`) | none (FLC SPD shows it) | the sim's step | `K:AP_SPD_VAR_INC`, `K:AP_SPD_VAR_DEC` | none | SDK-APE | Unverified |

Sources (read 2026-11-14; URLs in phase3-autopilot.md, "Sources"): SDK-APE = MSFS 2024 SDK autopilot key
events; SDK-APV = MSFS 2024 SDK autopilot SimVars; SDK-RADV / SDK-RADE = MSFS 2024 SDK radio navigation
SimVars / events; SDK-AS1000 and SDK-APT = SDK template explorer pages (general `/html/` path) for the
AS1000 glass cockpit and Asobo's autopilot buttons; README = PilotsDeck README; IE n = line n of
[reference/InputEvents-C172-G1000.txt](reference/InputEvents-C172-G1000.txt). Jiblet's profile and the
forum report are leads only. YD and LVL are not built (no button or input event in this aircraft).

### Phase 3 transponder page

For [phase3-transponder.md](phase3-transponder.md) (the second-level page behind MORE 1,7 `XPDR`; positions
below are on that page). Generated, not yet sim-tested: all rows are **Unverified** until the checklist
section "P3-2: Transponder page (C172 G1000)" passes. The 2024 C172 G1000 has **no transponder input event**
(IE: only the breaker `B:electrical_breaker_btn_breaker_xpndr`, IE 172), so every key uses SDK K-events or
SimVars. The XPDR readout (1,2) repeats the main page's "Transponder code (3,2)" row (same address, a second
key). STBY / ON / ALT write an A-Var (command type 12): the SDK has no transponder mode event, the SDK marks
`TRANSPONDER STATE` settable (SDK-RADV, rechecked 2026-11-14), and the coordinator's P3-2 ruling A-4 allows
this write for these three keys only; a key that changes the SimVar but not the PFD's XPDR mode display fails
the hand test (repair: the three keys go Empty, the PFD softkeys set the mode).

| Function | Read | Units | Write | Fallback | Source | Verified |
|---|---|---|---|---|---|---|
| Squawk code readout (xpdr 1,2 `XPDR`) | `(A:TRANSPONDER CODE:1, Bco16)`, Decode BCD, Format `4.0` | Bco16 (four octal digits, one per hex nibble) | (read only) | `(A:TRANSPONDER CODE:1, number)`, no Decode BCD | SDK-RADV; SDK-UNITS | Unverified |
| Set the squawk code (xpdr 4,8 `ENT`, by the script `XL24-XPDRPAD.lua`) | `(A:TRANSPONDER CODE:1, Bco16)` (1,2) | parameter: the four digits read as hex, sent in decimal (7000 = `28672`) | `K:XPNDR_SET:<n>` sent by `SimCommand` | per-digit `K:XPNDR_1000_INC`, `K:XPNDR_100_INC`, `K:XPNDR_10_INC`, `K:XPNDR_1_INC` (and `_DEC`) | SDK-RADE; README 2.1.1, 3.5.1 | Unverified |
| Typed entry (xpdr 1,3 `ENTRY`) | `X:XL24_XPDRPAD_ENTRY` (PilotsDeck internal variable, written by the script) | String, e.g. `70__` | the script's `DIGIT(n)`, `BACK`, `CLEAR`, `ENTER` (`lua:XL24-XPDRPAD:...`, command type 14) | the script function as the key's Address instead of the `X:` variable | README 2.1.1 (INTERNAL, LUAFUNC) | Unverified |
| Transponder mode readout (xpdr 1,4 `MODE`) | `(A:TRANSPONDER STATE:1, Enum)`, Mappings `0=OFF:1=STBY:2=TEST:3=ON:4=ALT:5=GND` | Enum: 0 = Off, 1 = Standby, 2 = Test, 3 = On, 4 = Alt, 5 = Ground | (read only) | none | SDK-RADV | Unverified |
| Mode STBY / ON / ALT (xpdr 2,2 `STBY`, 2,3 `ON`, 2,4 `ALT`) | `(A:TRANSPONDER STATE:1, Enum)`; lit at 1 / 3 / 4 | Enum as above | A-Var `(A:TRANSPONDER STATE:1, Enum)`, On Value `$=1` / `$=3` / `$=4`, Off Value empty (command type 12) | none by event: the keys go Empty and the PFD softkeys (XPDR, then STBY / ON / ALT) set the mode | SDK-RADV (settable mark); README 2.1.1 AVAR, 2.1.2; ruling A-4 | Unverified (the PFD's own mode display must follow) |
| Ident (xpdr 3,2 `IDENT`) | `(A:TRANSPONDER IDENT:1, Bool)` | Bool; the sim sets it back to 0 after 18 s | `K:XPNDR_IDENT_ON` | `K:XPNDR_IDENT_TOGGLE`, then `K:XPNDR_IDENT_SET:1` | SDK-RADE; SDK-RADV | Unverified |
| VFR code 1200 (xpdr 3,3 `VFR`) | (XPDR at 1,2 shows it) | 4608 = 0x1200 | `K:XPNDR_SET:4608` | `K:XPNDR_SET:0x1200` | SDK-RADE; README 2.1.1 | Unverified |

Sources (read 2026-11-14; URLs in phase3-transponder.md, "Sources"): SDK-RADE / SDK-RADV = MSFS 2024 SDK radio
navigation events / SimVars (the Settable mark of `TRANSPONDER STATE` read from the page source: a green tick;
`TRANSPONDER CODE` has the red cross); SDK-UNITS = MSFS 2024 SDK SimVar units; README = PilotsDeck README;
IE n = line n of [reference/InputEvents-C172-G1000.txt](reference/InputEvents-C172-G1000.txt). Jiblet's
C172 G1000 profile (per-digit XPNDR keys) is a lead only.

### Phase 3 radios page

For [phase3-radios.md](phase3-radios.md) (the second-level page behind MORE 1,8 `RADIOS`; positions below
are on that page). Generated, not yet sim-tested: all rows are **Unverified** until the checklist section
"P3-2b: Radios page (C172 G1000)" passes. Every key uses a K-event that names its radio index, and the
readouts read the indexed SimVars: the aircraft's NAV/COM input events (the PFD knobs and swap buttons, IE 95,
99, 101, 48, 52, 57) act on whichever radio the G1000's tuning box has selected, and their push values are
unknown. Open points (hand test): A-6 (index 1 / 2 are the PFD's NAV1 / NAV2, index 2 its COM2), A-7 (the
steps change the standby, not the active frequency), A-8 (the kHz step size; 8.33 kHz not handled), A-9 (mic
select). COM1 is not repeated here: main 3,1 and the COM1 pad rows above.

| Function | Read | Units | Write | Fallback | Source | Verified |
|---|---|---|---|---|---|---|
| NAV1 active / standby, swap (radios 1,2 `NAV1`) | `(A:NAV ACTIVE FREQUENCY:1, MHz)`, `(A:NAV STANDBY FREQUENCY:1, MHz)`, Format `2` | MHz, 108.00 to 117.95 | press `K:NAV1_RADIO_SWAP` | index change (A-6); `B:as1000_nav_switch_pfd` (acts on the selected NAV radio, value unknown) | SDK-RADV; SDK-RADE; IE 101 | Unverified |
| NAV2 active / standby, swap (1,4 `NAV2`) | `(A:NAV ACTIVE FREQUENCY:2, MHz)`, `(A:NAV STANDBY FREQUENCY:2, MHz)`, Format `2` | MHz | press `K:NAV2_RADIO_SWAP` | as NAV1 | SDK-RADV; SDK-RADE; IE 101 | Unverified |
| NAV1 / NAV2 station ident (1,3 `NAV1 ID`, 1,5 `NAV2 ID`) | `(A:NAV IDENT:1, String)`, `(A:NAV IDENT:2, String)` | String | (read only) | the key goes Empty | SDK-RADV | Unverified |
| COM2 active / standby, swap (1,6 `COM2`) | `(A:COM ACTIVE FREQUENCY:2, MHz)`, `(A:COM STANDBY FREQUENCY:2, MHz)`, Format `3` | SDK unit "Frequency BCD16", read in MHz as COM1 | press `K:COM2_RADIO_SWAP` | read as BCD16 (the COM1 keys' fallback); `B:as1000_com_switch_pfd` (selected COM radio, value unknown) | SDK-RADV; SDK-RADE; IE 57 | Unverified |
| COM2 station ident (1,7 `COM2 ID`) | `(A:COM ACTIVE FREQ IDENT:2, String)` | String | (read only) | the key goes Empty | SDK-RADV | Unverified |
| NAV1 MHz step (2,2 `MHZ+`, 3,2 `MHZ-`) | none (NAV1 shows it) | 1 MHz; standby expected (A-7) | `K:NAV1_RADIO_WHOLE_INC`, `K:NAV1_RADIO_WHOLE_DEC` | A-7: a script with `K:NAV1_STBY_SET_HZ` (new ruling), else Empty | SDK-RADE; IE 95 | Unverified |
| NAV1 kHz step (2,3 `KHZ+`, 3,3 `KHZ-`) | none (NAV1 shows it) | SDK "by 25 KHz", no carry; 50 kHz expected (A-8) | `K:NAV1_RADIO_FRACT_INC`, `K:NAV1_RADIO_FRACT_DEC` | `K:NAV1_RADIO_FRACT_INC_CARRY`, `K:NAV1_RADIO_FRACT_DEC_CARRY` ("by 50 KHz, and will carry"); A-7 as above | SDK-RADE; IE 99 | Unverified |
| NAV2 MHz step (2,4 `MHZ+`, 3,4 `MHZ-`) | none (NAV2 shows it) | as NAV1 | `K:NAV2_RADIO_WHOLE_INC`, `K:NAV2_RADIO_WHOLE_DEC` | A-7: a script with `K:NAV2_STBY_SET_HZ` (new ruling), else Empty | SDK-RADE; IE 95 | Unverified |
| NAV2 kHz step (2,5 `KHZ+`, 3,5 `KHZ-`) | none (NAV2 shows it) | as NAV1 | `K:NAV2_RADIO_FRACT_INC`, `K:NAV2_RADIO_FRACT_DEC` | `K:NAV2_RADIO_FRACT_INC_CARRY`, `K:NAV2_RADIO_FRACT_DEC_CARRY`; A-7 as above | SDK-RADE; IE 99 | Unverified |
| COM2 MHz step (2,6 `MHZ+`, 3,6 `MHZ-`) | none (COM2 shows it) | 1 MHz, 118 to 137 with wrap; standby expected (A-7) | `K:COM2_RADIO_WHOLE_INC`, `K:COM2_RADIO_WHOLE_DEC` | A-7: a script with `K:COM2_STBY_RADIO_SET_HZ` (new ruling), else Empty | SDK-RADE; IE 48 | Unverified |
| COM2 kHz step (2,7 `KHZ+`, 3,7 `KHZ-`) | none (COM2 shows it) | 25 kHz, no carry (A-8; 8.33 kHz mode not handled) | `K:COM2_RADIO_FRACT_INC`, `K:COM2_RADIO_FRACT_DEC` | `K:COM2_RADIO_FRACT_INC_CARRY`, `K:COM2_RADIO_FRACT_DEC_CARRY`; A-7 as above | SDK-RADE; IE 52 | Unverified |
| COM1 / COM2 mic select (4,6 `MIC1`, 4,7 `MIC2`) | `(A:COM TRANSMIT:1, Bool)`, `(A:COM TRANSMIT:2, Bool)` | Bool; lit for the transmitting COM | `K:PILOT_TRANSMITTER_SET:0` (COM1), `K:PILOT_TRANSMITTER_SET:1` (COM2) | A-9: `K:COM1_TRANSMIT_SELECT` / `K:COM2_TRANSMIT_SELECT`, then `B:as1000_com_1_mic_midcom` / `B:as1000_com_2_mic_midcom` (scmon check first); if the read fails, Simple Buttons | SDK-RADE; SDK-RADV; IE 41, 43 | Unverified |

Sources (read 2026-11-14; URLs in phase3-radios.md, "Sources"): SDK-RADE / SDK-RADV = MSFS 2024 SDK radio
navigation events / SimVars (the `_CARRY` event names rechecked 2026-11-14 for P3-2b); IE n = line n of
[reference/InputEvents-C172-G1000.txt](reference/InputEvents-C172-G1000.txt). Jiblet's C172 G1000 profile
(NAV/COM dials on the same WHOLE/FRACT events) is a lead only.

### Phase 3 systems page

For [phase3-systems.md](phase3-systems.md) (the second-level page behind MORE 2,2 `SYSTEMS`; positions below
are on that page). Generated, not yet sim-tested: all rows are **Unverified** until the checklist section
"P3-3: Systems page (C172 G1000)" passes. Every switch on the page is in the aircraft's input event list, so
every switch key reads and writes its input event (command type 13, On `1` / Off `0` unless the row says
otherwise; the battery precedent above); the SDK K-event and SimVar pairs are fallbacks (the alternator
events are for the v1.00 electrical system only, and the indexes the cockpit drives are unknown). The
readouts read SimVars. Open points (hand test): A-3 (switch values: STBY BATT has three positions, the light
switches may be dimmers), A-4 (fuel selector values), A-6 (readout indexes), A-7 (what the dimmer readout
follows), A-8 (which light each light key drives). FUEL VLV is for the ground only (A-5).

| Function | Read | Units | Write | Fallback | Source | Verified |
|---|---|---|---|---|---|---|
| Alternator switch (systems 1,2 `ALT`) | `B:electrical_alternator_1` | 1 = on, 0 = off (A-3) | `B:electrical_alternator_1`, On `1` / Off `0` | read `(A:GENERAL ENG MASTER ALTERNATOR:1, Bool)`, write `K:TOGGLE_ALTERNATOR1` (v1.00 only) | IE 140; README 2.1.1; SDK-ELECV; SDK-ELECE; lead: Jiblet | Unverified |
| Avionics bus 1 / 2 switches (1,3 `AVN 1`, 1,4 `AVN 2`) | `B:electrical_line_bus_1_to_avionics_bus_1`, `B:electrical_line_bus_2_to_avionics_bus_2` | 1 = on, 0 = off (A-3) | the same input events, On `1` / Off `0` | read `(A:LINE CONNECTION ON:n, Bool)` or `(A:AVIONICS MASTER SWITCH:n, Bool)`, write `K:ELECTRICAL_LINE_CONNECTION_TOGGLE:n`; n unknown | IE 174, 175; SDK-ELECV; SDK-SYSV; SDK-ELECE; lead: Jiblet | Unverified |
| Standby battery switch (1,5 `STBY BAT`) | `B:electrical_battery_stby_2` | 1 / 0 assumed; the switch is ARM / OFF / TEST (A-3) | `B:electrical_battery_stby_2`, On `1` / Off `0` | read `(A:ELECTRICAL MASTER BATTERY:n, Bool)`; n unknown | IE 142; SDK-ELECV | Unverified |
| Bus volts (1,6 `BUS V`) | `(A:ELECTRICAL BUS VOLTAGE:1, Volts)`, Format `2.1` | Volts; bus index 1 is a global index (A-6) | (read only) | `(A:ELECTRICAL MAIN BUS VOLTAGE:1, Volts)` (v1.00), another index | SDK-ELECV | Unverified |
| Battery amps (1,7 `BATT A`) | `(A:ELECTRICAL BATTERY LOAD:2, Amperes)`, Format `1.1` | Amperes, the load drawn from the battery while it supplies (SDK: not when charging); its sign against the EIS M BATT is open; battery index 2 = the cockpit BAT's (A-6) | (read only) | index 1; `(A:ELECTRICAL BUS AMPS:1, Amperes)` | SDK-ELECV | Unverified |
| Total load amps (1,8 `LOAD A`) | `(A:ELECTRICAL TOTAL LOAD AMPS, Amperes)`, Format `1.1` | Amperes, no index | (read only) | none | SDK-ELECV | Unverified |
| Cabin lights 1 / 2 (2,2 `CABIN 1`, 2,3 `CABIN 2`) | `B:lighting_cabin_1`, `B:lighting_cabin_2` | 1 / 0 assumed; may be dimmers (A-3); which light: A-8 | the same input events, On `1` / Off `0` | `K:TOGGLE_CABIN_LIGHTS`, read `(A:LIGHT CABIN, Bool)` | IE 194, 195; SDK-ELECE; SDK-SYSV | Unverified |
| Panel lights 1 / 2 (2,4 `PANEL 1`, 2,5 `PANEL 2`) | `B:lighting_panel_1`, `B:lighting_panel_2` | 1 / 0 assumed; may be dimmer knobs (A-3); which light: A-8 | the same input events, On `1` / Off `0` | `K:PANEL_LIGHTS_TOGGLE`, read `(A:LIGHT PANEL, Bool)`; a dimmer becomes a Display Value of its input event | IE 198, 199; SDK-ELECE; SDK-SYSV | Unverified |
| Pedestal light (2,6 `PED LT`) | `B:lighting_pedestral_1` (the aircraft's spelling) | 1 / 0 assumed (A-3) | `B:lighting_pedestral_1`, On `1` / Off `0` | `K:PEDESTRAL_LIGHTS_TOGGLE`, read `(A:LIGHT PEDESTRAL, Bool)` | IE 200; SDK-ELECE; SDK-SYSV | Unverified |
| Light dimmer readout (2,7 `DIMMER`) | `(A:LIGHT POTENTIOMETER:5, Percent)`, Format `1.0` | Percent; what potentiometer 5 dims is unknown (A-7) | (read only) | read `B:lighting_potentiometer_5` | SDK-SYSV; IE 201 | Unverified |
| Fuel selector LEFT / BOTH / RIGHT (3,2 `LEFT`, 3,3 `BOTH`, 3,4 `RIGHT`) | `B:fuel_selector_1`; lit at `1` / `2` / `3` | 1 = LEFT, 2 = BOTH, 3 = RIGHT assumed (A-4, weak: a lead's junction option numbers) | `B:fuel_selector_1`, On = Off = `1` / `2` / `3` (every press sets that position) | the values from the scmon check; `K:FUEL_SELECTOR_LEFT` / `K:FUEL_SELECTOR_ALL` / `K:FUEL_SELECTOR_RIGHT` as Simple Buttons | IE 180; SDK-FUELE; lead: Jiblet | Unverified |
| Fuel selector readout (3,5 `FUEL SEL`) | `(A:FUELSYSTEM JUNCTION SETTING:1, Number)`, Mappings `1=LEFT:2=BOTH:3=RIGHT` | Number (junction option) | (read only) | `(A:FUEL TANK SELECTOR:1, Enum)` (legacy only) | SDK-FUELV; lead: Jiblet | Unverified |
| Fuel shutoff valve (3,6 `FUEL VLV`; ground only, A-5) | `B:fuel_valve_shutoffvalve` | 1 = open (fuel on), 0 = closed assumed (A-3) | `B:fuel_valve_shutoffvalve`, On `1` / Off `0` | `K:FUELSYSTEM_VALVE_TOGGLE:n`, read `(A:FUELSYSTEM VALVE SWITCH:n, Bool)`; n unknown | IE 181; SDK-FUELE; SDK-FUELV | Unverified |
| Fuel quantity left / right / total (4,2 `FUEL L`, 4,3 `FUEL R`, 4,4 `FUEL TOT`) | `(A:FUEL LEFT QUANTITY, Gallons)`, `(A:FUEL RIGHT QUANTITY, Gallons)`, `(A:FUEL TOTAL QUANTITY, Gallons)`, Format `1.1` | Gallons, no index (the EIS shows usable fuel) | (read only) | `(A:FUELSYSTEM TANK QUANTITY:n, Gallons)` | SDK-FUELV | Unverified |

Sources (read 2026-11-14; URLs in phase3-systems.md, "Sources"): SDK-ELECE / SDK-ELECV = MSFS 2024 SDK
electrical events / electrics SimVars; SDK-SYSV = MSFS 2024 SDK system SimVars (lights, avionics master);
SDK-FUELV / SDK-FUELE = MSFS 2024 SDK fuel SimVars / fuel system events; README = PilotsDeck README; IE n =
line n of [reference/InputEvents-C172-G1000.txt](reference/InputEvents-C172-G1000.txt). Jiblet's C172 G1000
profile (the alternator and bus input events, the fuel selector read as junction options 1/2/3) is a lead
only.

### Phase 3 engine and fuel page

For [phase3-engine-fuel.md](phase3-engine-fuel.md) (the second-level page behind MORE 2,3 `ENGINE`; positions
below are on that page). Generated, not yet sim-tested: all rows are **Unverified** until the checklist section
"P3-5: Engine and fuel page (C172 G1000)" passes. Every key only reads a SimVar (no input event is a readout:
the aircraft's engine input events, IE 176-178, are controls). Open points (hand test): A-IDX (engine `1`, bus
`1` = M BUS, battery `2` = M BATT), A-AMPS (BATT A's sign against the EIS), A-FUELVAR (the General fuel SimVars
in a 2024 aircraft), A-FUELRANGE (the gauges' `0` to `26` gallons), A-UNITS (the unit strings convert).

| Function | Read | Units | Write | Fallback | Source | Verified |
|---|---|---|---|---|---|---|
| Fuel flow (1,3 `FFLOW`) | `(A:ENG FUEL FLOW GPH:1, gallons per hour)`, Format `1.1` | gallons per hour (native); engine index 1 | (read only) | `(A:ENG FUEL FLOW PPH:1, pounds per hour)` (a weight rate, not gallons) | SDK-ENGV; SDK-UNITS; lead: TorontoWill | Unverified |
| Oil pressure (1,4 `OIL PRES`) | `(A:GENERAL ENG OIL PRESSURE:1, psi)`, Format `1.0` | psf -> psi (A-UNITS) | (read only) | `(A:ENG OIL PRESSURE:1, psi)`; the native `psf` with a Scalar | SDK-ENGV; SDK-UNITS | Unverified |
| Oil temperature (1,5 `OIL TEMP`) | `(A:GENERAL ENG OIL TEMPERATURE:1, fahrenheit)`, Format `1.0` | rankine -> deg F (A-UNITS) | (read only) | `(A:ENG OIL TEMPERATURE:1, fahrenheit)`; the native `rankine` with a Scalar | SDK-ENGV; SDK-UNITS | Unverified |
| Exhaust gas temperature (1,6 `EGT`) | `(A:GENERAL ENG EXHAUST GAS TEMPERATURE:1, fahrenheit)`, Format `1.0` | rankine -> deg F (A-UNITS) | (read only) | `(A:ENG EXHAUST GAS TEMPERATURE:1, fahrenheit)`; the native `rankine` with a Scalar | SDK-ENGV; SDK-UNITS | Unverified |
| Vacuum suction (1,7 `VAC`) | `(A:SUCTION PRESSURE, inHg)`, Format `1.1` | inches of mercury, no index | (read only) | none (the only vacuum value on SDK-SYSV) | SDK-SYSV; SDK-UNITS | Unverified |

Reused reads (rows above in this file): RPM 1,2 = the main page's 1,2 (`GENERAL ENG RPM:1`, Format `1.0`); FUEL
L 2,2 and FUEL R 2,3 read the systems page's `FUEL LEFT QUANTITY` / `FUEL RIGHT QUANTITY` (systems 4,2, 4,3), here
as Display Gauges from `0` to `26` gallons [GARMIN] with Format `1.0` (fallback `(A:FUELSYSTEM TANK QUANTITY:n,
Gallons)`; the scale against the sim's 28-gallon tanks: "Phase 3 fuel gauge scale (P3-FUELCAP)" below); BUS V 3,2
and BATT A 3,3 = systems 1,6 and 1,7. All Unverified.

Sources (read 2026-11-16; URLs in phase3-engine-fuel.md, "Sources"): SDK-ENGV / SDK-SYSV / SDK-FUELV / SDK-UNITS
= MSFS 2024 SDK engine, system and fuel SimVars and SimVar units; GARMIN = Garmin G1000 Reference Manual, Cessna
Nav III, Section 3 EIS (the real aircraft: the 172S fuel gauge full scale, 26 gallons per side); IE n = line n of
[reference/InputEvents-C172-G1000.txt](reference/InputEvents-C172-G1000.txt). TorontoWill's generic profile
(the same fuel flow name, index and unit) is a lead only.

### Phase 3 fuel gauge scale (P3-FUELCAP)

For the engine page's FUEL L 2,2 and FUEL R 2,3 ([phase3-engine-fuel.md](phase3-engine-fuel.md), A-FUELRANGE).
No key changed: the gauges keep `0` to `26` gallons (the G1000 EIS scale). The rows below are the tank SimVars
behind that choice and the scmon watch list of the checklist section "P3-FUELCAP: Fuel gauge scale (C172 G1000)";
no key reads them. All **Unverified**: the scmon values are observations (2026-11-16, sim version not
read), not a passed test. Open points: A-TANKIDX (which index is the left tank), A-USABLE
(whether the quantities count unusable fuel), A-SCALE (the scale).

| Function | Read | Units | Write | Fallback | Source | Verified |
|---|---|---|---|---|---|---|
| Tank capacity, tanks 1 and 2 | `(A:FUELSYSTEM TANK CAPACITY:1, Gallons)`, `(A:FUELSYSTEM TANK CAPACITY:2, Gallons)` | gallons, "Total capacity"; scmon read `28` and `28` | (read only) | `FUEL LEFT CAPACITY` / `FUEL RIGHT CAPACITY` (General SimVars) | SDK-FUELV; SCMON | Unverified |
| Tank usable capacity, tanks 1 and 2 (scmon watch only) | `(A:FUELSYSTEM TANK USABLE CAPACITY:1, Gallons)`, `:2` | gallons; 172S 26.5 per tank expected (CESSNA) | (read only) | none | SDK-FUELV | Unverified |
| Tank quantity, tanks 1 and 2 (the gauges' fallback) | `(A:FUELSYSTEM TANK QUANTITY:1, Gallons)`, `:2` | gallons, "currently available"; scmon read 12.1, 12.9, 8.0, both tanks equal | (read only) | `FUEL LEFT QUANTITY` / `FUEL RIGHT QUANTITY` (the gauges' reads) | SDK-FUELV; SCMON | Unverified |
| Tank quantity with unusable fuel, tanks 1 and 2 (scmon watch only) | `(A:FUELSYSTEM TANK TOTAL QUANTITY:1, Gallons)`, `:2` | gallons, "including any unusable fuel" | (read only) | none | SDK-FUELV | Unverified |
| Fuel capacity left / right (scmon watch only) | `(A:FUEL LEFT CAPACITY, Gallons)`, `(A:FUEL RIGHT CAPACITY, Gallons)` | gallons, General SimVars ("legacy") | (read only) | `FUELSYSTEM TANK CAPACITY:n` | SDK-FUELV | Unverified |
| Unusable fuel, all tanks (scmon watch only) | `(A:UNUSABLE FUEL TOTAL QUANTITY, Gallons)` | gallons, General SimVar | (read only) | none | SDK-FUELV | Unverified |

Sources (read 2026-11-16; URLs in phase3-engine-fuel.md, "Sources"): SDK-FUELV = MSFS 2024 SDK fuel SimVars;
SCMON = the scmon run of 2026-11-16 with the 2024 C172 G1000 loaded; CESSNA = Textron Aviation's Skyhawk specifications
(53 gallons usable), with a Boldmethod article as a lead (28 gallons per tank, 56 total).

## FlyByWire A32NX (Phase 4 airliner)

Installed with the FlyByWire Installer (`A:\FS2024 Stuff\FlyByWire-Installer-x64.exe`).
Mostly L-Vars and custom events rather than standard SimVars. Use FlyByWire's own
flight-deck API docs and HubHop as sources, and record each one here.

Aircraft string: _TBD_

| Function | Read (variable) | Units | Write (command) | Verified |
|---|---|---|---|---|

### FlyByWire A32NX (MSFS 2024)

For [phase4-a32nx.md](phase4-a32nx.md): the profile `MSFS2024 A32NX` (main page, FCU page, OVHD page; positions
below are page and row,column) and its Lua script `XL24-A32NX.lua`. The A32NX is not installed on this PC yet
(2026-11-14); FlyByWire's MSFS 2024 release is "FS2024 A32NX Stable Release v2024.1.0", "not yet a native 2024
package" (FBW-REL). Generated, not yet sim-tested: every row is **Unverified** until the checklist section
"Phase 4: A32NX profile (P4-1)" passes (then the date, MSFS version and A32NX version). A key that fails gets
"does not work" in its row, and the row stays. The table above stays empty; these are the rows.

Aircraft string: to be recorded at the first A32NX flight (from the PilotsDeck log).

| Function | Read | Units | Write | Fallback | Source | Verified |
|---|---|---|---|---|---|---|
| AP1 push button (main 1,1; fcu 2,4) | `L:A32NX_FCU_AP_1_LIGHT_ON` | 0/1 | `K:A32NX.FCU_AP_1_PUSH` | Lua `SimCalculator` with the same event | FBW-SIMVARS, FBW-EVENTS | Unverified |
| AP2 push button (main 1,2; fcu 2,5) | `L:A32NX_FCU_AP_2_LIGHT_ON` | 0/1 | `K:A32NX.FCU_AP_2_PUSH` | as AP1 | FBW-SIMVARS, FBW-EVENTS | Unverified |
| A/THR push button (main 1,3; fcu 3,4) | `L:A32NX_FCU_ATHR_LIGHT_ON` | 0/1 | `K:A32NX.FCU_ATHR_PUSH` | as AP1 | FBW-SIMVARS, FBW-EVENTS | Unverified |
| LOC push button (main 1,4; fcu 4,4) | `L:A32NX_FCU_LOC_LIGHT_ON` | 0/1 | `K:A32NX.FCU_LOC_PUSH` | as AP1 | FBW-SIMVARS, FBW-EVENTS | Unverified |
| APPR push button (main 1,5; fcu 4,5) | `L:A32NX_FCU_APPR_LIGHT_ON` | 0/1 | `K:A32NX.FCU_APPR_PUSH` | as AP1 | FBW-SIMVARS, FBW-EVENTS | Unverified |
| EXPED push button (fcu 3,5) | `L:A32NX_FCU_EXPED_LIGHT_ON` | 0/1 | `K:A32NX.FCU_EXPED_PUSH` | as AP1 | FBW-SIMVARS, FBW-EVENTS | Unverified |
| FD push button, Captain (main 1,6; fcu 2,1) | `L:A32NX_FCU_EFIS_L_FD_LIGHT_ON` | 0/1 | `K:A32NX.FCU_EFIS_L_FD_PUSH` | as AP1 | FBW-SIMVARS, FBW-EVENTS | Unverified |
| LS push button, Captain (main 1,7; fcu 3,1) | `L:A32NX_FCU_EFIS_L_LS_LIGHT_ON` | 0/1 | `K:A32NX.FCU_EFIS_L_LS_PUSH` | as AP1 | FBW-SIMVARS, FBW-EVENTS | Unverified |
| FCU powered (read by the script; blank readouts when not 1) | `L:A32NX_FCU_HEALTHY` | 0/1 | (read only) | none | FBW-SIMVARS | Unverified |
| SPD/MACH window (main 2,1; fcu 2,2) | `lua:XL24-A32NX:SPD`, which reads `L:A32NX_FCU_AFS_DISPLAY_SPD_MACH_VALUE`, `L:A32NX_FCU_AFS_DISPLAY_SPD_MACH_DASHES`, `L:A32NX_FCU_AFS_DISPLAY_SPD_MACH_MANAGED`, `L:A32NX_FCU_AFS_DISPLAY_MACH_MODE` | knots, or Mach as a decimal (0.1..0.99); dashes and managed dot 0/1 | knob push `K:A32NX.FCU_SPD_PUSH` (readout press), pull `K:A32NX.FCU_SPD_PULL` (fcu 4,2), turn `K:A32NX.FCU_SPD_INC` / `K:A32NX.FCU_SPD_DEC` (fcu 1,2 / 3,2) | other text format in the script only | FBW-SIMVARS, FBW-EVENTS, FBW-API | Unverified |
| SPD/MACH button (fcu 1,4) | `L:A32NX_FCU_AFS_DISPLAY_MACH_MODE` | 0 SPD, 1 MACH | `K:A32NX.FCU_SPD_MACH_TOGGLE_PUSH` | as AP1 | FBW-SIMVARS, FBW-EVENTS | Unverified |
| HDG/TRK window (main 2,2; fcu 2,3) | `lua:XL24-A32NX:HDG`, which reads `L:A32NX_FCU_AFS_DISPLAY_HDG_TRK_VALUE`, `L:A32NX_FCU_AFS_DISPLAY_HDG_TRK_DASHES`, `L:A32NX_FCU_AFS_DISPLAY_HDG_TRK_MANAGED` | degrees 0..359 | knob push `K:A32NX.FCU_HDG_PUSH`, pull `K:A32NX.FCU_HDG_PULL` (fcu 4,3), turn `K:A32NX.FCU_HDG_INC` / `K:A32NX.FCU_HDG_DEC` (fcu 1,3 / 3,3) | as SPD | FBW-SIMVARS, FBW-EVENTS, FBW-API | Unverified |
| HDG-V/S / TRK-FPA button (fcu 1,5; also read by the script for V/S) | `L:A32NX_FCU_AFS_DISPLAY_TRK_FPA_MODE` | 0 HDG-V/S, 1 TRK-FPA | `K:A32NX.FCU_TRK_FPA_TOGGLE_PUSH` | as AP1 | FBW-SIMVARS, FBW-EVENTS | Unverified |
| ALT window (main 2,3; fcu 2,6) | `lua:XL24-A32NX:ALT`, which reads `L:A32NX_FCU_AFS_DISPLAY_ALT_VALUE`, `L:A32NX_FCU_AFS_DISPLAY_LVL_CH_MANAGED` | feet 100..49000 | knob push `K:A32NX.FCU_ALT_PUSH`, pull `K:A32NX.FCU_ALT_PULL` (fcu 4,6), turn `K:A32NX.FCU_ALT_INC` / `K:A32NX.FCU_ALT_DEC` (fcu 1,6 / 3,6; no parameter = "Use FCU setting") | as SPD | FBW-SIMVARS, FBW-EVENTS, FBW-API | Unverified |
| ALT increment 100/1000 (fcu 4,1) | `L:A32NX_FCU_ALT_INCREMENT_1000` | 0 = 100, 1 = 1000 | `K:A32NX.FCU_ALT_INCREMENT_TOGGLE` | as AP1 | FBW-SIMVARS, FBW-EVENTS | Unverified |
| V/S-FPA window (main 2,4; fcu 2,7) | `lua:XL24-A32NX:VS`, which reads `L:A32NX_FCU_AFS_DISPLAY_VS_FPA_VALUE`, `L:A32NX_FCU_AFS_DISPLAY_VS_FPA_DASHES` | ft/min, or degrees in FPA mode | knob push `K:A32NX.FCU_VS_PUSH`, pull `K:A32NX.FCU_VS_PULL` (fcu 4,7), turn `K:A32NX.FCU_VS_INC` / `K:A32NX.FCU_VS_DEC` (fcu 1,7 / 3,7) | as SPD | FBW-SIMVARS, FBW-EVENTS, FBW-API | Unverified |
| Baro window, Captain (main 2,5; fcu 2,8) | `lua:XL24-A32NX:BARO`, which reads `L:A32NX_FCU_EFIS_L_DISPLAY_BARO_VALUE`, `L:A32NX_FCU_EFIS_L_DISPLAY_BARO_VALUE_MODE` | hPa or inHg; mode 0 STD, 1 hPa, 2 inHg | push (QNH) `K:A32NX.FCU_EFIS_L_BARO_PUSH` (readout press), pull (STD) `K:A32NX.FCU_EFIS_L_BARO_PULL` (readout long press), turn `K:A32NX.FCU_EFIS_L_BARO_INC` / `K:A32NX.FCU_EFIS_L_BARO_DEC` (fcu 1,8 / 3,8) | as SPD; push/pull meaning is aircraft knowledge | FBW-SIMVARS, FBW-EVENTS, FBW-API | Unverified |
| Baro unit hPa/inHg, Captain (fcu 4,8) | `L:A32NX_FCU_EFIS_L_BARO_IS_INHG` | 0 hPa, 1 inHg | `L:A32NX_FCU_EFIS_L_BARO_IS_INHG`, On `1` / Off `0` (L-Var write) | readout only | FBW-API, FBW-SIMVARS | Unverified |
| ND mode, Captain (main 2,6) | `L:A32NX_FCU_EFIS_L_EFIS_MODE` | 0 ROSE ILS, 1 ROSE VOR, 2 ROSE NAV, 3 ARC, 4 PLAN | `lua:XL24-A32NX:NDMODE(1)`, long press `lua:XL24-A32NX:NDMODE(-1)` (the script writes the L-Var, 0..4) | readout only | FBW-API, FBW-SIMVARS; README 2.1.1 LUAFUNC | Unverified |
| ND range, Captain (main 2,7) | `L:A32NX_FCU_EFIS_L_EFIS_RANGE` | 0 = 10, 1 = 20, 2 = 40, 3 = 80, 4 = 160, 5 = 320 NM | `lua:XL24-A32NX:NDRANGE(1)`, long press `lua:XL24-A32NX:NDRANGE(-1)` (the script writes the L-Var, 0..5) | readout only | FBW-API, FBW-SIMVARS; README 2.1.1 LUAFUNC | Unverified |
| MASTER WARNING (main 3,1) | `L:A32NX_MASTER_WARNING` | 0/1 | `L:A32NX_MASTER_WARNING`, On `0` / Off `0` (writes 0; no press event documented) | readout only | FBW-API, FBW-WARN | Unverified |
| MASTER CAUTION (main 3,2) | `L:A32NX_MASTER_CAUTION` | 0/1 | `L:A32NX_MASTER_CAUTION`, On `0` / Off `0` | readout only | FBW-API, FBW-WARN | Unverified |
| Parking brake lever (main 3,3) | `L:A32NX_PARK_BRAKE_LEVER_POS` | 0/1 | `L:A32NX_PARK_BRAKE_LEVER_POS`, On `1` / Off `0` | `K:PARKING_BRAKES` | FBW-API, FBW-SIMVARS, FBW-REL | Unverified |
| Flaps lever (main 3,4) | `L:A32NX_FLAPS_HANDLE_INDEX` | 0 UP, 1, 2, 3, 4 FULL | `K:FLAPS_INCR` (press), `K:FLAPS_DECR` (long press) | none | FBW-API, FBW-SIMVARS | Unverified |
| Ground spoilers armed (main 3,5) | `L:A32NX_SPOILERS_ARMED` | 0/1 | `K:SPOILERS_ARM_TOGGLE` | none | FBW-API, FBW-SIMVARS | Unverified |
| Autobrake LO / MED / MAX (main 3,6 / 3,7 / 3,8) | `L:A32NX_AUTOBRAKES_ARMED_MODE` (On `1` / `2` / `3`, Off `0`) | 0 DIS, 1 LO, 2 MED, 3 MAX | `K:A32NX.AUTOBRAKE_BUTTON_LO`, `K:A32NX.AUTOBRAKE_BUTTON_MED`, `K:A32NX.AUTOBRAKE_BUTTON_MAX` | as AP1 | FBW-EVENTS, FBW-API | Unverified |
| Strobe (main 4,1; ovhd 1,2) | `L:LIGHTING_STROBE_0` | 0 ON, 1 AUTO, 2 OFF | `L:LIGHTING_STROBE_0`, On `0` / Off `1` (ON / AUTO) | `K:STROBES_TOGGLE` (ON and OFF only, no AUTO) | FBW-API | Unverified |
| Beacon (main 4,2; ovhd 1,3) | `(A:LIGHT BEACON, Bool)` | 0/1 | `K:TOGGLE_BEACON_LIGHTS` | none | FBW-API, SDK-ELECE | Unverified |
| Wing lights (ovhd 1,4) | `(A:LIGHT WING, Bool)` | 0/1 | `K:TOGGLE_WING_LIGHTS` | none | FBW-API, SDK-ELECE | Unverified |
| NAV & LOGO (main 4,3; ovhd 1,5) | `B:A32NX_OVH_LIGHTS_NAV_LOGO_SW` (input event) | 0 OFF, 1 SYS 1, 2 SYS 2 | `B:A32NX_OVH_LIGHTS_NAV_LOGO_SW`, On `1` / Off `0` (B-Var command) | the form `InputEvents.txt` lists; read `L:A32NX_LIGHTS_NAV_LOGO` (FBW-REL) | FBW-IE, FBW-REL; README 2.1.1 BVAR | Unverified |
| Runway turn-off lights (ovhd 1,6) | `(A:CIRCUIT SWITCH ON:21, Bool)` (left; right is `:22`) | 0/1 | `K:ELECTRICAL_CIRCUIT_TOGGLE:21:K:ELECTRICAL_CIRCUIT_TOGGLE:22` (K-event sequence) | readout only | FBW-API, SDK-ELECE; PD-PI line 195 | Unverified |
| Landing light left / right (main 4,4 / 4,5; ovhd 1,7 / 1,8) | `L:LIGHTING_LANDING_2` / `L:LIGHTING_LANDING_3` | 0 ON, 1 OFF, 2 RETRACT | `L:LIGHTING_LANDING_2` / `L:LIGHTING_LANDING_3`, On `0` / Off `2` | readout only | FBW-API | Unverified |
| Nose light (main 4,6; ovhd 2,1) | `L:LIGHTING_LANDING_1` | 0 T.O., 1 TAXI, 2 OFF | `L:LIGHTING_LANDING_1`, On `0` / Off `1` | readout only | FBW-API | Unverified |
| Seat belts sign (main 4,7; ovhd 2,2) | `(A:CABIN SEATBELTS ALERT SWITCH, Bool)` | 0/1 | `K:CABIN_SEATBELTS_ALERT_SWITCH_TOGGLE` | none | FBW-API | Unverified |
| No smoking sign (ovhd 2,3) | `L:XMLVAR_SWITCH_OVHD_INTLT_NOSMOKING_POSITION` | 0 ON, 1 AUTO, 2 OFF | `L:XMLVAR_SWITCH_OVHD_INTLT_NOSMOKING_POSITION`, On `0` / Off `1` | readout only | FBW-API | Unverified |
| BAT 1 / BAT 2 (ovhd 3,1 / 3,2) | `L:A32NX_OVHD_ELEC_BAT_1_PB_IS_AUTO` / `L:A32NX_OVHD_ELEC_BAT_2_PB_IS_AUTO` | 1 AUTO, 0 OFF | `L:A32NX_OVHD_ELEC_BAT_1_PB_IS_AUTO` / `L:A32NX_OVHD_ELEC_BAT_2_PB_IS_AUTO`, On `1` / Off `0` | readout only | FBW-API, FBW-SIMVARS | Unverified |
| EXT PWR (ovhd 3,3) | `L:A32NX_OVHD_ELEC_EXT_PWR_PB_IS_ON` | 0/1 | `L:A32NX_OVHD_ELEC_EXT_PWR_PB_IS_ON`, On `1` / Off `0` | readout only | FBW-API | Unverified |
| APU master switch (ovhd 3,4) | `L:A32NX_OVHD_APU_MASTER_SW_PB_IS_ON` | 0/1 | `L:A32NX_OVHD_APU_MASTER_SW_PB_IS_ON`, On `1` / Off `0` | readout only | FBW-API, FBW-SIMVARS | Unverified |
| APU start (ovhd 3,5) | `L:A32NX_OVHD_APU_START_PB_IS_ON` | 0/1 | `L:A32NX_OVHD_APU_START_PB_IS_ON`, On `1` / Off `1` (always writes 1) | readout only | FBW-API, FBW-SIMVARS | Unverified |
| APU available (ovhd 3,6) | `L:A32NX_OVHD_APU_START_PB_IS_AVAILABLE` | 0/1 | (read only) | none | FBW-API, FBW-SIMVARS | Unverified |

Sources: the tags of [phase4-a32nx.md](phase4-a32nx.md), "Sources": FBW-SIMVARS (FlyByWire
`fbw-a32nx/docs/a320-simvars.md`), FBW-EVENTS (`fbw-a32nx/docs/a320-events.md`), FBW-IE
(`fbw-a32nx/docs/a32nx-input-events.md`), FBW-API (the FlyByWire Flight Deck API page; "might lag behind the
current developments of the A32NX"), FBW-REL (the v2024.1.0 release notes), FBW-WARN (the glareshield warning
page), SDK-ELECE (MSFS 2024 SDK Aircraft Electrical Events), README and PD-PI (PilotsDeck). Weak points the
hand test decides: the `A32NX.*` events sent as K-Vars (inferred from FlyByWire's SimConnect interface and
PilotsDeck's source), WARN/CAUT cleared by writing 0, the `LIGHTING_*` L-Vars in the MSFS 2024 build, the NAV
LOGO B-Var form, RWY TURN by circuit toggles, baro push = QNH / pull = STD, the Mach and FPA display scale.

### FlyByWire A32NX EFIS page (P4-2)

For [phase4-a32nx-efis.md](phase4-a32nx-efis.md): the EFIS page `efis` of the profile `MSFS2024 A32NX` (opened by
main 4,8 `EFIS`; positions are page and row,column) and the four functions P4-2 added to `XL24-A32NX.lua`
(`NAV1`, `NAV2`, `MWARN`, `MCAUT`). The A32NX is not installed on this PC yet (2026-11-14). Generated, not yet
sim-tested: every row is **Unverified** until the checklist section "Phase 4: A32NX EFIS page (P4-2)" passes
(then the date, MSFS version and A32NX version). FD, LS, BARO+, BARO, BARO-, hPa/inHg, ND MODE and ND RNG on
this page (efis 1,3, 2,3, 1,2, 2,2, 3,2, 3,3, 2,4, 2,5) are the P4-1 keys of the rows above, same addresses.
**Main 3,1 / 3,2 changed in P4-2:** the press is now the script's `MWARN` / `MCAUT` (rows below), not the P4-1
write of 0 to the lamp L-Var that the "MASTER WARNING (main 3,1)" and "MASTER CAUTION (main 3,2)" rows above
describe (kept as P4-1's record; that write is now the fallback).

| Function | Read | Units | Write | Fallback | Source | Verified |
|---|---|---|---|---|---|---|
| ND option CSTR, Captain (efis 1,4) | `L:A32NX_FCU_EFIS_L_CSTR_LIGHT_ON` | 0/1 | `K:A32NX.FCU_EFIS_L_CSTR_PUSH` | Lua `SimCalculator` with the same event | FBW-SIMVARS, FBW-EVENTS, FBW-API, FBW-EFIS-XML | Unverified |
| ND option WPT, Captain (efis 1,5) | `L:A32NX_FCU_EFIS_L_WPT_LIGHT_ON` | 0/1 | `K:A32NX.FCU_EFIS_L_WPT_PUSH` | as CSTR | FBW-SIMVARS, FBW-EVENTS, FBW-API, FBW-EFIS-XML | Unverified |
| ND option VOR.D, Captain (efis 1,6) | `L:A32NX_FCU_EFIS_L_VORD_LIGHT_ON` | 0/1 | `K:A32NX.FCU_EFIS_L_VORD_PUSH` | as CSTR | FBW-SIMVARS, FBW-EVENTS, FBW-API, FBW-EFIS-XML | Unverified |
| ND option NDB, Captain (efis 1,7) | `L:A32NX_FCU_EFIS_L_NDB_LIGHT_ON` | 0/1 | `K:A32NX.FCU_EFIS_L_NDB_PUSH` | as CSTR | FBW-SIMVARS, FBW-EVENTS, FBW-API, FBW-EFIS-XML | Unverified |
| ND option ARPT, Captain (efis 1,8) | `L:A32NX_FCU_EFIS_L_ARPT_LIGHT_ON` | 0/1 | `K:A32NX.FCU_EFIS_L_ARPT_PUSH` | as CSTR | FBW-SIMVARS, FBW-EVENTS, FBW-API, FBW-EFIS-XML | Unverified |
| Baro mode QNH / STD, Captain (efis 2,1 QNH lit at 1; efis 3,1 STD lit at 0) | `L:A32NX_FCU_EFIS_L_DISPLAY_BARO_MODE` | 0 STD, 1 QNH, 2 QFE | QNH: knob push `K:A32NX.FCU_EFIS_L_BARO_PUSH`; STD: knob pull `K:A32NX.FCU_EFIS_L_BARO_PULL` | as CSTR | FBW-SIMVARS, FBW-API, FBW-EVENTS, FBW-EFIS-PILOT | Unverified |
| ADF/VOR switch 1, Captain (efis 2,6) | `L:A32NX_FCU_EFIS_L_NAVAID_1_MODE` | 0 OFF, 1 ADF, 2 VOR (FBW-API, FBW-EFIS-XML; FBW-SIMVARS says 1 VOR, 2 ADF) | `lua:XL24-A32NX:NAV1(1)` (one position toward VOR), long press `lua:XL24-A32NX:NAV1(-1)` (toward ADF); the script writes the L-Var (L-Var write, A-5) | values swapped (1 VOR, 2 ADF) in the mappings and the script; else readout only | FBW-API, FBW-EFIS-XML, FBW-SIMVARS; README 2.1.1 LUAFUNC, 3.5.1 | Unverified |
| ADF/VOR switch 2, Captain (efis 2,7) | `L:A32NX_FCU_EFIS_L_NAVAID_2_MODE` | as switch 1 | `lua:XL24-A32NX:NAV2(1)`, long press `lua:XL24-A32NX:NAV2(-1)` (the script writes the L-Var) | as switch 1 | FBW-API, FBW-EFIS-XML, FBW-SIMVARS; README 2.1.1 LUAFUNC, 3.5.1 | Unverified |
| CHRONO, Captain ND (efis 2,8) | (none: the ND shows the time) | - | `K:A32NX.EFIS_L_CHRONO_PUSHED` | `H:A32NX_EFIS_L_CHRONO_PUSHED` (Simple Button, H-Var, `ActionType` 8) | FBW-EVENTS, FBW-API | Unverified |
| AUTOLAND lamp (efis 3,8) | `L:A32NX_AUTOPILOT_AUTOLAND_WARNING` | 0/1 | (read only) | the key becomes Empty | FBW-API, FBW-FCU-XML; listed as deprecated in FBW-SIMVARS | Unverified |
| MASTER WARN press, Captain (efis 4,1; main 3,1 since P4-2) | `L:A32NX_MASTER_WARNING` | 0/1 | `lua:XL24-A32NX:MWARN`: the script writes `L:PUSH_AUTOPILOT_MASTERAWARN_L` 1, waits 200 ms, writes 0 (the cockpit button's own press; L-Var write, A-5) | a longer `Sleep`; then P4-1's write of 0 to `L:A32NX_MASTER_WARNING`; then readout only | FBW-INTERIOR, FBW-FWC, FBW-API; README 3.5.1 | Unverified |
| MASTER CAUT press, Captain (efis 4,2; main 3,2 since P4-2) | `L:A32NX_MASTER_CAUTION` | 0/1 | `lua:XL24-A32NX:MCAUT`: the script writes `L:PUSH_AUTOPILOT_MASTERCAUT_L` 1, waits 200 ms, writes 0 | as MASTER WARN, with `L:A32NX_MASTER_CAUTION` | FBW-INTERIOR, FBW-FWC, FBW-API; README 3.5.1 | Unverified |

Sources: the tags of [phase4-a32nx-efis.md](phase4-a32nx-efis.md), "Sources": FBW-SIMVARS, FBW-EVENTS, FBW-API
and README as above; FBW-EFIS-XML (FlyByWire `A32NX_Interior_EFIS.xml`), FBW-INTERIOR (`A320_NEO_INTERIOR.xml`),
FBW-FCU-XML (`A32NX_Interior_FCU.xml`), FBW-FWC (`PseudoFWC.ts`), FBW-EFIS-PILOT (FlyByWire's EFIS control
panel page). Weak points the hand test decides: the ADF/VOR values (1 ADF, 2 VOR against `a320-simvars.md`),
CHRONO as a K-Var custom event, the deprecated AUTOLAND L-Var, the 200 ms press length, and the `A32NX.*`
events sent as K-Vars (as P4-1).

### FlyByWire A32NX overhead pages (P4-3)

For [phase4-a32nx-overhead.md](phase4-a32nx-overhead.md): the 12 new keys of the OVHD page `ovhd` (main 2,8) and
the SYSTEMS page `ovhdsys` (ovhd 2,8) of the profile `MSFS2024 A32NX` (positions are page and row,column), and
the function `FUELMODE` P4-3 added to `XL24-A32NX.lua`. P4-1's 16 OVHD keys are the rows of "FlyByWire A32NX
(MSFS 2024)" above, unchanged. The A32NX is not installed on this PC yet (2026-11-14). Generated, not yet
sim-tested: every row is **Unverified** until the checklist section "Phase 4: A32NX overhead pages (P4-3)"
passes (then the date, MSFS version and A32NX version). The standard-event rows (GEN, APU GEN, tank pumps,
X FEED) act on any aircraft with those indexes (phase4-a32nx-overhead.md).

| Function | Read | Units | Write | Fallback | Source | Verified |
|---|---|---|---|---|---|---|
| EMER EXIT LT switch (ovhd 2,4) | `L:XMLVAR_SWITCH_OVHD_INTLT_EMEREXIT_POSITION` | 0 ON, 1 ARM (FBW-API: AUTO), 2 OFF | `L:XMLVAR_SWITCH_OVHD_INTLT_EMEREXIT_POSITION`, On `1` / Off `2` (ARM / OFF) | readout only | FBW-API | Unverified |
| ANN LT switch (ovhd 2,5) | `L:A32NX_OVHD_INTLT_ANN` | 0 TEST, 1 BRT, 2 DIM | `L:A32NX_OVHD_INTLT_ANN`, On `0` / Off `1` (TEST / BRT) | readout only | FBW-API, FBW-SIMVARS | Unverified |
| APU BLEED pushbutton (ovhd 3,7) | `L:A32NX_OVHD_PNEU_APU_BLEED_PB_IS_ON` | 0/1 | `L:A32NX_OVHD_PNEU_APU_BLEED_PB_IS_ON`, On `1` / Off `0` | readout only | FBW-API, FBW-MISC | Unverified |
| APU N (ovhd 3,8) | `L:A32NX_APU_N_RAW` | percent | (read only) | the key becomes Empty | FBW-SIMVARS | Unverified |
| BAT 1 / BAT 2 voltage (ovhd 4,1 / 4,2) | `L:A32NX_ELEC_BAT_1_POTENTIAL` / `L:A32NX_ELEC_BAT_2_POTENTIAL` | volts | (read only) | none | FBW-API, FBW-SIMVARS | Unverified |
| EXT PWR AVAIL (ovhd 4,3) | `L:A32NX_EXT_PWR_AVAIL:1` | 0/1 | (read only) | read `L:A32NX_ELEC_EXT_PWR_POTENTIAL_NORMAL` | FBW-API, FBW-SIMVARS, FBW-ELEC; PD-PI line 181 | Unverified |
| GEN 1 / GEN 2 (ovhd 4,4 / 4,5) | `(A:GENERAL ENG MASTER ALTERNATOR:1, Bool)` / `(A:GENERAL ENG MASTER ALTERNATOR:2, Bool)` | 0/1 | `K:TOGGLE_ALTERNATOR1` / `K:TOGGLE_ALTERNATOR2` | none | FBW-ELEC, FBW-API, SDK-ELECE | Unverified |
| APU GEN (ovhd 4,6) | `(A:APU GENERATOR SWITCH:1, Bool)` | 0/1 | `K:APU_GENERATOR_SWITCH_TOGGLE:1` | none | FBW-ELEC, SDK-ELECE; README 3.5.1 | Unverified |
| BUS TIE pushbutton (ovhd 4,7) | `L:A32NX_OVHD_ELEC_BUS_TIE_PB_IS_AUTO` | 1 AUTO, 0 OFF | `L:A32NX_OVHD_ELEC_BUS_TIE_PB_IS_AUTO`, On `1` / Off `0` | readout only | FBW-API, FBW-INTERIOR, FBW-GEN | Unverified |
| L TK pumps 1 / 2 (ovhdsys 1,2 / 1,3) | `(A:FUELSYSTEM PUMP SWITCH:2, Enum)` / `(A:FUELSYSTEM PUMP SWITCH:5, Enum)` | 0 off, 1 on (the key lights at 1) | `K:FUELSYSTEM_PUMP_TOGGLE:2` / `K:FUELSYSTEM_PUMP_TOGGLE:5` | none | FBW-MISC, FBW-INTERIOR, FBW-API, SDK-FUELE | Unverified |
| CTR TK jet pump valves 1 / 2 (ovhdsys 1,4 / 1,5) | `(A:FUELSYSTEM VALVE SWITCH:9, Enum)` / `(A:FUELSYSTEM VALVE SWITCH:10, Enum)` | 0 off, 1 on (the key lights at 1) | `K:FUELSYSTEM_VALVE_TOGGLE:9` / `K:FUELSYSTEM_VALVE_TOGGLE:10` | none | FBW-MISC, FBW-INTERIOR, FBW-API, SDK-FUELE | Unverified |
| R TK pumps 1 / 2 (ovhdsys 1,6 / 1,7) | `(A:FUELSYSTEM PUMP SWITCH:3, Enum)` / `(A:FUELSYSTEM PUMP SWITCH:6, Enum)` | 0 off, 1 on (the key lights at 1) | `K:FUELSYSTEM_PUMP_TOGGLE:3` / `K:FUELSYSTEM_PUMP_TOGGLE:6` | none | FBW-MISC, FBW-INTERIOR, FBW-API, SDK-FUELE | Unverified |
| Fuel MODE SEL (ovhdsys 1,8) | `L:A32NX_OVHD_FUEL_MODESEL_MANUAL` | 1 MAN, 0 AUTO | `lua:XL24-A32NX:FUELMODE`: when `L:A32NX_TOTAL_FUEL_QUANTITY` > 0, the script runs the cockpit's code by `SimCalculator`, which writes `L:A32NX_OVHD_FUEL_MODESEL_MANUAL` and sends `(>K:2:FUELSYSTEM_JUNCTION_SET)` for junctions 4 and 5 (needs the MobiFlight WASM module, PD-SRC) | `SimWrite` the L-Var and `SimCommand("K:FUELSYSTEM_JUNCTION_SET:4:<1\|2>")` and `:5:`; then readout only | FBW-INTERIOR, SDK-FUELE, FBW-API; README 3.5.1; PD-SRC | Unverified |
| Total fuel, the script's guard for FUELMODE (no key) | `L:A32NX_TOTAL_FUEL_QUANTITY` | kg | (read only) | none | FBW-SIMVARS | Unverified |
| X FEED switch (ovhdsys 2,1) | `(A:FUELSYSTEM VALVE SWITCH:3, Bool)` | 0/1 | `K:FUELSYSTEM_VALVE_TOGGLE:3` | none | FBW-MISC, FBW-INTERIOR, FBW-API, SDK-FUELE | Unverified |
| X FEED valve open (ovhdsys 2,2) | `(A:FUELSYSTEM VALVE OPEN:3, Bool)` | 0 SHUT, 1 OPEN | (read only) | none | FBW-MISC, FBW-API | Unverified |
| IR 1 / IR 3 / IR 2 mode knobs (ovhdsys 2,3 / 2,4 / 2,5) | `L:A32NX_OVHD_ADIRS_IR_1_MODE_SELECTOR_KNOB` / `L:A32NX_OVHD_ADIRS_IR_3_MODE_SELECTOR_KNOB` / `L:A32NX_OVHD_ADIRS_IR_2_MODE_SELECTOR_KNOB` | 0 OFF, 1 NAV, 2 ATT | the same L-Vars, On `1` / Off `0` (NAV / OFF) | readout only | FBW-API, FBW-SIMVARS, FBW-ADIRS | Unverified |
| ADIRS ON BAT light (ovhdsys 2,6) | `L:A32NX_OVHD_ADIRS_ON_BAT_IS_ILLUMINATED` | 0/1 | (read only) | none | FBW-API, FBW-INTERIOR | Unverified |
| IR alignment time left (ovhdsys 2,7) | `L:A32NX_ADIRS_REMAINING_IR_ALIGNMENT_TIME` | seconds (deprecated in FBW-SIMVARS) | (read only) | the key becomes Empty | FBW-API, FBW-SIMVARS | Unverified |
| ENG 1 / ENG 2 BLEED pushbuttons (ovhdsys 3,1 / 3,2) | `L:A32NX_OVHD_PNEU_ENG_1_BLEED_PB_IS_AUTO` / `L:A32NX_OVHD_PNEU_ENG_2_BLEED_PB_IS_AUTO` | 1 AUTO, 0 OFF | the same L-Vars, On `1` / Off `0` | readout only | FBW-SIMVARS, FBW-MISC | Unverified |
| PACK 1 / PACK 2 pushbuttons (ovhdsys 3,3 / 3,4) | `L:A32NX_OVHD_COND_PACK_1_PB_IS_ON` / `L:A32NX_OVHD_COND_PACK_2_PB_IS_ON` | 0/1 | the same L-Vars, On `1` / Off `0` | readout only | FBW-API, FBW-SIMVARS, FBW-INTERIOR, FBW-GEN | Unverified |
| AC ESS FEED pushbutton (ovhdsys 3,5) | `L:A32NX_OVHD_ELEC_AC_ESS_FEED_PB_IS_NORMAL` | 1 NORMAL, 0 ALTN | the same L-Var, On `1` / Off `0` | readout only | FBW-API, FBW-SIMVARS, FBW-INTERIOR, FBW-GEN | Unverified |
| GALY & CAB pushbutton (ovhdsys 3,6) | `L:A32NX_OVHD_ELEC_GALY_AND_CAB_PB_IS_AUTO` | 1 AUTO, 0 OFF | the same L-Var, On `1` / Off `0` | readout only | FBW-API, FBW-SIMVARS, FBW-INTERIOR, FBW-GEN | Unverified |
| COMMERCIAL pushbutton (ovhdsys 3,7) | `L:A32NX_OVHD_ELEC_COMMERCIAL_PB_IS_ON` | 0/1 | the same L-Var, On `1` / Off `0` | readout only | FBW-SIMVARS, FBW-INTERIOR, FBW-GEN (FBW-API's `_PB_IS_AUTO` is older) | Unverified |
| WING anti-ice pushbutton (ovhdsys 4,1) | `L:A32NX_BUTTON_OVHD_ANTI_ICE_WING_POSITION` | 0/1 | the same L-Var, On `1` / Off `0` | readout only | FBW-MISC | Unverified |
| ENG 1 / ENG 2 anti-ice pushbuttons (ovhdsys 4,2 / 4,3) | `L:A32NX_BUTTON_OVHD_ANTI_ICE_ENG_1_POSITION` / `L:A32NX_BUTTON_OVHD_ANTI_ICE_ENG_2_POSITION` | 0/1 | the same L-Vars, On `1` / Off `0` | readout only | FBW-MISC, FBW-SIMVARS | Unverified |
| PROBE/WINDOW HEAT pushbutton (ovhdsys 4,4) | `L:A32NX_MAN_PITOT_HEAT` | 0/1 | the same L-Var, On `1` / Off `0` | readout only | FBW-API, FBW-MISC | Unverified |

Sources: the tags of [phase4-a32nx-overhead.md](phase4-a32nx-overhead.md), "Sources": FBW-API, FBW-SIMVARS,
SDK-ELECE, README and PD-PI as above; FBW-INTERIOR (`A320_NEO_INTERIOR.xml`), FBW-ELEC
(`A32NX_Interior_Elec.xml`), FBW-MISC (`A32NX_Interior_Misc.xml`), FBW-GEN (`A32NX_Interior_Generics.xml`),
FBW-ADIRS (`A32NX_Interior_ADIRS.xml`), SDK-FUELE (MSFS 2024 SDK Aircraft Fuel System Events), PD-SRC
(PilotsDeck source at `11bdf1f`). Weak points the hand test decides: MODE SEL by `SimCalculator` (and the
MobiFlight module it needs), `L:A32NX_EXT_PWR_AVAIL:1` read with its `:1`, APU N from the raw L-Var, the
deprecated alignment time L-Var, the IR knob order 1, 3, 2.

### FlyByWire A32NX radio and transponder pages (P4-4)

For [phase4-a32nx-radios.md](phase4-a32nx-radios.md): the second-level pages `radio` (efis 3,4 `RADIO`, the
Captain's RMP 1) and `xpdr` (efis 3,5 `XPDR`, the ATC/TCAS panel) of the profile `MSFS2024 A32NX` (positions
are page and row,column), and the five functions P4-4 added to `XL24-A32NX.lua` (`RMPACT`, `RMPSTBY`,
`XPDRMODE`, `TCASMODE`, `TCASTRAF`). The A32NX is not installed on this PC yet (2026-11-16). Generated, not
yet sim-tested: every row is **Unverified** until the checklist section "Phase 4: A32NX radio and transponder
pages (P4-4)" passes (then the date, MSFS version and A32NX version). Every `H:` command needs the MobiFlight
WASM module ([troubleshooting.md](troubleshooting.md#the-mobiflight-wasm-module)).

| Function | Read | Units | Write | Fallback | Source | Verified |
|---|---|---|---|---|---|---|
| RMP 1 VHF1 key (radio 1,2) | `L:A32NX_RMP_L_SELECTED_MODE` (lit at 1) | 1 VHF1, 2 VHF2, 3 VHF3, 6 to 10 NAV modes (FBW-API lists 0..3) | `H:A32NX_RMP_L_VHF1_BUTTON_PRESSED` | none | FBW-RMP-XML, FBW-RMP-BASE, FBW-API | Unverified |
| RMP 1 VHF2 key (radio 1,3) | `L:A32NX_RMP_L_SELECTED_MODE` (lit at 2) | as VHF1 | `H:A32NX_RMP_L_VHF2_BUTTON_PRESSED` | none | FBW-RMP-XML, FBW-RMP-BASE, FBW-API | Unverified |
| RMP 1 ON/OFF switch (radio 1,6) | `L:A32NX_RMP_L_TOGGLE_SWITCH` | 0/1 | `L:A32NX_RMP_L_TOGGLE_SWITCH`, On `1` / Off `0` (L-Var write, FBW-API: R/W; not `H:A32NX_RMP_L_TOGGLE_SWITCH`, which only makes the RMP read the L-Var again, FBW-REACT) | readout only | FBW-API, FBW-RMP-XML, FBW-RMP-BASE, FBW-SIMVARS, FBW-REACT | Unverified |
| RMP 1 outer knob, MHz (radio 1,7 / 2,7) | (none: STBY shows the result) | MHz step, 118 to 136 | `H:A32NX_RMP_L_OUTER_KNOB_TURNED_CLOCKWISE` / `H:A32NX_RMP_L_OUTER_KNOB_TURNED_ANTICLOCKWISE` | none | FBW-RMP-XML, FBW-RMP-STBY | Unverified |
| RMP 1 inner knob, kHz (radio 1,8 / 2,8) | (none: STBY shows the result) | one channel, 8.33 or 25 kHz | `H:A32NX_RMP_L_INNER_KNOB_TURNED_CLOCKWISE` / `H:A32NX_RMP_L_INNER_KNOB_TURNED_ANTICLOCKWISE` | none | FBW-RMP-XML, FBW-RMP-STBY | Unverified |
| RMP 1 transfer key (radio 2,5) | (none: ACTIVE and STBY show the result) | - | `H:A32NX_RMP_L_TRANSFER_BUTTON_PRESSED` | none | FBW-RMP-XML, FBW-RMP-VHF | Unverified |
| COM1 / COM2 active frequency (radio 2,1 / 2,2) | `(A:COM ACTIVE FREQUENCY:1, MHz)` / `(A:COM ACTIVE FREQUENCY:2, MHz)` | MHz | (read only) | none | SDK-RADV, FBW-API, FBW-RMP-VHF | Unverified |
| RMP 1 active window (radio 2,4) | `lua:XL24-A32NX:RMPACT`: the script reads `L:A32NX_RMP_L_TOGGLE_SWITCH`, `L:A32NX_ELEC_DC_ESS_BUS_IS_POWERED`, `L:A32NX_RMP_L_SELECTED_MODE` and `(A:COM ACTIVE FREQUENCY:1, Hz)`, `(A:COM ACTIVE FREQUENCY:2, Hz)` or `(A:COM ACTIVE FREQUENCY:3, Hz)` | text `118.700`, blank, or `DATA` (VHF3) | (read only) | none | FBW-RMP-VHF, FBW-RMP-BASE; README 2.1.1 LUAFUNC, 3.5.1 | Unverified |
| RMP 1 standby window (radio 2,6) | `lua:XL24-A32NX:RMPSTBY`: the script reads the three L-Vars above and `(A:COM STANDBY FREQUENCY:1, Hz)` (VHF1), `L:A32NX_RMP_L_VHF2_STANDBY_FREQUENCY` (VHF2) or `L:A32NX_RMP_L_VHF3_STANDBY_FREQUENCY` (VHF3) | text `118.700` or blank; the L-Vars in Hz (FBW-SIMVARS names the VHF2 one `A32NX_RMP_L_VHF2_STANDBY`; the code wins) | (read only) | none | FBW-RMP-VHF, FBW-RMP-BASE, FBW-SIMVARS; README 2.1.1 LUAFUNC, 3.5.1 | Unverified |
| DC ESS bus powered, the scripts' RMP 1 power check (no key) | `L:A32NX_ELEC_DC_ESS_BUS_IS_POWERED` | 0/1 | (read only) | none | FBW-RMP-BASE | Unverified |
| Transponder code (xpdr 1,2) | `(A:TRANSPONDER CODE:1, Bco16)` | Bco16, Decode BCD | (read only; the panel writes it with `K:XPNDR_SET`) | none | SDK-RADV, FBW-API, FBW-ATC-GAUGE | Unverified |
| Transponder state (xpdr 1,3) | `(A:TRANSPONDER STATE:1, Enum)` | 0 OFF, 1 STBY, 2 TEST, 3 ON, 4 ALT, 5 GND | (read only: FlyByWire writes it) | none | SDK-RADV, FBW-ATC-XML | Unverified |
| IDENT (xpdr 1,4) | `(A:TRANSPONDER IDENT:1, Bool)` | 0/1 (off by itself after 18 s, SDK-RADE) | `K:XPNDR_IDENT_ON` | K6 Simple Button, same command, no light | FBW-API, FBW-ATC-XML, SDK-RADE, SDK-RADV | Unverified |
| ATC keypad digits (xpdr 4,7 0, 3,6 1, 3,7 2, 3,8 3, 2,6 4, 2,7 5, 2,8 6, 1,6 7) | (none: XPDR shows the code after the fourth digit, typed after CLR, CLR) | - | `H:A320_Neo_ATC_BTN_0`, `H:A320_Neo_ATC_BTN_1`, `H:A320_Neo_ATC_BTN_2`, `H:A320_Neo_ATC_BTN_3`, `H:A320_Neo_ATC_BTN_4`, `H:A320_Neo_ATC_BTN_5`, `H:A320_Neo_ATC_BTN_6`, `H:A320_Neo_ATC_BTN_7` | a code pad of the script's own that sends `K:XPNDR_SET` (not built) | FBW-ATC-XML, FBW-ATC-GAUGE, FBW-BEGIN | Unverified |
| ATC keypad CLR (xpdr 4,6) | (none) | - | `H:A320_Neo_ATC_BTN_CLR` | as the digits | FBW-ATC-XML, FBW-ATC-GAUGE | Unverified |
| Transponder mode selector (xpdr 2,2) | `L:A32NX_TRANSPONDER_MODE` | 0 STBY, 1 AUTO, 2 ON | `lua:XL24-A32NX:XPDRMODE(1)` (one position clockwise), long press `lua:XL24-A32NX:XPDRMODE(-1)`; the script writes the L-Var (L-Var write) | readout only | FBW-ATC-XML, FBW-API, FBW-SIMVARS; README 2.1.1 LUAFUNC, 3.5.1 | Unverified |
| ALT RPTG switch (xpdr 2,3) | `L:A32NX_SWITCH_ATC_ALT` | 0 OFF, 1 ON | `L:A32NX_SWITCH_ATC_ALT`, On `1` / Off `0` | readout only | FBW-ATC-XML, FBW-API, FBW-SIMVARS | Unverified |
| TCAS mode selector (xpdr 3,2) | `L:A32NX_SWITCH_TCAS_Position` | 0 STBY, 1 TA, 2 TA/RA | `lua:XL24-A32NX:TCASMODE(1)`, long press `lua:XL24-A32NX:TCASMODE(-1)`; the script writes the L-Var (FBW-SIMVARS says Read-Only, FBW-API R/W) | the upper-case name `L:A32NX_SWITCH_TCAS_POSITION` (FBW-API); then readout only | FBW-ATC-XML, FBW-API, FBW-SIMVARS; README 2.1.1 LUAFUNC, 3.5.1 | Unverified |
| TCAS traffic selector (xpdr 3,3) | `L:A32NX_SWITCH_TCAS_Traffic_Position` | 0 THRT, 1 ALL, 2 ABV, 3 BLW | `lua:XL24-A32NX:TCASTRAF(1)`, long press `lua:XL24-A32NX:TCASTRAF(-1)`; the script writes the L-Var (as TCAS mode) | the upper-case name `L:A32NX_SWITCH_TCAS_TRAFFIC_POSITION` (FBW-API); then readout only | FBW-ATC-XML, FBW-API, FBW-SIMVARS; README 2.1.1 LUAFUNC, 3.5.1 | Unverified |

Sources: the tags of [phase4-a32nx-radios.md](phase4-a32nx-radios.md), "Sources" (FlyByWire at the tag
v2024.1.0): FBW-RMP-VHF (`VhfRadioPanel.tsx`), FBW-RMP-STBY (`StandbyFrequency.tsx`), FBW-RMP-BASE
(`BaseRadioPanels.tsx`), FBW-RMP-XML (`A32NX_Interior_RMP.xml`), FBW-ATC-XML (`A32NX_Interior_ATC.xml`),
FBW-ATC-GAUGE (the ATC panel gauge `ATC/index.tsx`), FBW-REACT (`simVars.tsx`), FBW-BEGIN, FBW-SIMVARS,
FBW-API, SDK-RADE, SDK-RADV and README as above. Weak points the hand test decides: the H-events sent through
the MobiFlight module, the RMP ON L-Var write, the transponder mode by L-Var write (STATE following), the TCAS
L-Var names' case and their writes, IDENT lit from the sim's ident SimVar, and the VHF1/VHF2 keys showing no
image while the other radio is selected.

### FlyByWire A32NX pedestal page (P4-6)

For [phase4-a32nx-pedestal.md](phase4-a32nx-pedestal.md): the second-level page `ped` (efis 3,6 `PED`: the
ECAM control panel, speed brake, flaps, park brake, gear, autobrake state, engine masters and ENG MODE, rudder
trim, A/SKID and brake pressure) of the profile `MSFS2024 A32NX` (positions are page and row,column), and the
six functions P4-6 added to `XL24-A32NX.lua` (`SPDBRK`, `GEARIND`, `ABRK`, `ENGMODE`, `RUDTRIM`, `BRKPSI`).
The A32NX is not installed on this PC yet (2026-11-16). Generated, not yet sim-tested: every row is
**Unverified** until the checklist section "Phase 4: A32NX pedestal page (P4-6)" passes (then the date, MSFS
version and A32NX version). Every `H:` command and the ENG MODE calculator code need the MobiFlight WASM
module ([troubleshooting.md](troubleshooting.md#the-mobiflight-wasm-module)).

| Function | Read | Units | Write | Fallback | Source | Verified |
|---|---|---|---|---|---|---|
| ECAM control panel ENG page key (ped 1,2) | `L:A32NX_ECP_LIGHT_ENG` (lit while the SD shows the page) | 1 bright, 0.1 dim, 0 off | `H:A32NX_ECP_ENG_PRESSED:A32NX_ECP_ENG_RELEASED` (H-Var sequence: `H:A32NX_ECP_ENG_PRESSED`, then `H:A32NX_ECP_ENG_RELEASED`) | Use Delay on; a Lua `ECP` press with `Sleep` (not built) | FBW-ECP-XML, FBW-ECP-TS, FBW-OVHD-DISC; README 2.1.1 HVAR | Unverified |
| ECAM control panel BLEED page key (ped 1,3) | `L:A32NX_ECP_LIGHT_BLEED` (lit while the SD shows the page) | 1 bright, 0.1 dim, 0 off | `H:A32NX_ECP_BLEED_PRESSED:A32NX_ECP_BLEED_RELEASED` (H-Var sequence: `H:A32NX_ECP_BLEED_PRESSED`, then `H:A32NX_ECP_BLEED_RELEASED`) | Use Delay on; a Lua `ECP` press with `Sleep` (not built) | FBW-ECP-XML, FBW-ECP-TS, FBW-OVHD-DISC; README 2.1.1 HVAR | Unverified |
| ECAM control panel PRESS page key (ped 1,4) | `L:A32NX_ECP_LIGHT_PRESS` (lit while the SD shows the page) | 1 bright, 0.1 dim, 0 off | `H:A32NX_ECP_PRESS_PRESSED:A32NX_ECP_PRESS_RELEASED` (H-Var sequence: `H:A32NX_ECP_PRESS_PRESSED`, then `H:A32NX_ECP_PRESS_RELEASED`) | Use Delay on; a Lua `ECP` press with `Sleep` (not built) | FBW-ECP-XML, FBW-ECP-TS, FBW-OVHD-DISC; README 2.1.1 HVAR | Unverified |
| ECAM control panel ELEC page key (ped 1,5) | `L:A32NX_ECP_LIGHT_ELEC` (lit while the SD shows the page) | 1 bright, 0.1 dim, 0 off | `H:A32NX_ECP_ELEC_PRESSED:A32NX_ECP_ELEC_RELEASED` (H-Var sequence: `H:A32NX_ECP_ELEC_PRESSED`, then `H:A32NX_ECP_ELEC_RELEASED`) | Use Delay on; a Lua `ECP` press with `Sleep` (not built) | FBW-ECP-XML, FBW-ECP-TS, FBW-OVHD-DISC; README 2.1.1 HVAR | Unverified |
| ECAM control panel HYD page key (ped 1,6) | `L:A32NX_ECP_LIGHT_HYD` (lit while the SD shows the page) | 1 bright, 0.1 dim, 0 off | `H:A32NX_ECP_HYD_PRESSED:A32NX_ECP_HYD_RELEASED` (H-Var sequence: `H:A32NX_ECP_HYD_PRESSED`, then `H:A32NX_ECP_HYD_RELEASED`) | Use Delay on; a Lua `ECP` press with `Sleep` (not built) | FBW-ECP-XML, FBW-ECP-TS, FBW-OVHD-DISC; README 2.1.1 HVAR | Unverified |
| ECAM control panel FUEL page key (ped 1,7) | `L:A32NX_ECP_LIGHT_FUEL` (lit while the SD shows the page) | 1 bright, 0.1 dim, 0 off | `H:A32NX_ECP_FUEL_PRESSED:A32NX_ECP_FUEL_RELEASED` (H-Var sequence: `H:A32NX_ECP_FUEL_PRESSED`, then `H:A32NX_ECP_FUEL_RELEASED`) | Use Delay on; a Lua `ECP` press with `Sleep` (not built) | FBW-ECP-XML, FBW-ECP-TS, FBW-OVHD-DISC; README 2.1.1 HVAR | Unverified |
| ECAM control panel APU page key (ped 2,2) | `L:A32NX_ECP_LIGHT_APU` (lit while the SD shows the page) | 1 bright, 0.1 dim, 0 off | `H:A32NX_ECP_APU_PRESSED:A32NX_ECP_APU_RELEASED` (H-Var sequence: `H:A32NX_ECP_APU_PRESSED`, then `H:A32NX_ECP_APU_RELEASED`) | Use Delay on; a Lua `ECP` press with `Sleep` (not built) | FBW-ECP-XML, FBW-ECP-TS, FBW-OVHD-DISC; README 2.1.1 HVAR | Unverified |
| ECAM control panel COND page key (ped 2,3) | `L:A32NX_ECP_LIGHT_COND` (lit while the SD shows the page) | 1 bright, 0.1 dim, 0 off | `H:A32NX_ECP_COND_PRESSED:A32NX_ECP_COND_RELEASED` (H-Var sequence: `H:A32NX_ECP_COND_PRESSED`, then `H:A32NX_ECP_COND_RELEASED`) | Use Delay on; a Lua `ECP` press with `Sleep` (not built) | FBW-ECP-XML, FBW-ECP-TS, FBW-OVHD-DISC; README 2.1.1 HVAR | Unverified |
| ECAM control panel DOOR page key (ped 2,4) | `L:A32NX_ECP_LIGHT_DOOR` (lit while the SD shows the page) | 1 bright, 0.1 dim, 0 off | `H:A32NX_ECP_DOOR_PRESSED:A32NX_ECP_DOOR_RELEASED` (H-Var sequence: `H:A32NX_ECP_DOOR_PRESSED`, then `H:A32NX_ECP_DOOR_RELEASED`) | Use Delay on; a Lua `ECP` press with `Sleep` (not built) | FBW-ECP-XML, FBW-ECP-TS, FBW-OVHD-DISC; README 2.1.1 HVAR | Unverified |
| ECAM control panel WHEEL page key (ped 2,5) | `L:A32NX_ECP_LIGHT_BRAKES` (lit while the SD shows the page) | 1 bright, 0.1 dim, 0 off | `H:A32NX_ECP_BRAKES_PRESSED:A32NX_ECP_BRAKES_RELEASED` (H-Var sequence: `H:A32NX_ECP_BRAKES_PRESSED`, then `H:A32NX_ECP_BRAKES_RELEASED`) | Use Delay on; a Lua `ECP` press with `Sleep` (not built) | FBW-ECP-XML, FBW-ECP-TS, FBW-OVHD-DISC; README 2.1.1 HVAR | Unverified |
| ECAM control panel F/CTL page key (ped 2,6) | `L:A32NX_ECP_LIGHT_FLT_CTL` (lit while the SD shows the page) | 1 bright, 0.1 dim, 0 off | `H:A32NX_ECP_FLT_CTL_PRESSED:A32NX_ECP_FLT_CTL_RELEASED` (H-Var sequence: `H:A32NX_ECP_FLT_CTL_PRESSED`, then `H:A32NX_ECP_FLT_CTL_RELEASED`) | Use Delay on; a Lua `ECP` press with `Sleep` (not built) | FBW-ECP-XML, FBW-ECP-TS, FBW-OVHD-DISC; README 2.1.1 HVAR | Unverified |
| ECAM control panel CLR (ped 2,1) | `L:A32NX_ECP_LIGHT_CLR_1` (lit while there is something to clear) | 1 bright, 0.1 dim, 0 off | `H:A32NX_ECP_CLR_1_PRESSED:A32NX_ECP_CLR_1_RELEASED` (`H:A32NX_ECP_CLR_1_PRESSED`, then `H:A32NX_ECP_CLR_1_RELEASED`) | as the page keys | FBW-ECP-XML, FBW-ECP-TS, FBW-OVHD-DISC | Unverified |
| ECAM control panel STS (ped 2,8) | `L:A32NX_ECP_LIGHT_STS` (lit while STATUS is shown) | 1 bright, 0.1 dim, 0 off | `H:A32NX_ECP_STS_PRESSED:A32NX_ECP_STS_RELEASED` (`H:A32NX_ECP_STS_PRESSED`, then `H:A32NX_ECP_STS_RELEASED`) | as the page keys | FBW-ECP-XML, FBW-ECP-TS, FBW-OVHD-DISC | Unverified |
| ECAM control panel T.O CONFIG (ped 1,8 `TO CONF`) | (none: no lamp; the E/WD or SD shows the result) | - | `H:A32NX_ECP_TO_CONF_TEST_PRESSED:A32NX_ECP_TO_CONF_TEST_RELEASED` (`H:A32NX_ECP_TO_CONF_TEST_PRESSED`, then `H:A32NX_ECP_TO_CONF_TEST_RELEASED`) | as the page keys | FBW-ECP-XML, FBW-ECP-TS, FBW-ECP-PR | Unverified |
| ECAM control panel ALL (ped 2,7) | (none: no lamp; the E/WD or SD shows the result) | - | `H:A32NX_ECP_ALL_PRESSED:A32NX_ECP_ALL_RELEASED` (`H:A32NX_ECP_ALL_PRESSED`, then `H:A32NX_ECP_ALL_RELEASED`) | as the page keys | FBW-ECP-XML, FBW-ECP-TS, FBW-ECP-PR | Unverified |
| ECAM control panel RCL (ped 3,1) | (none: no lamp; the E/WD or SD shows the result) | - | `H:A32NX_ECP_RCL_PRESSED:A32NX_ECP_RCL_RELEASED` (`H:A32NX_ECP_RCL_PRESSED`, then `H:A32NX_ECP_RCL_RELEASED`) | as the page keys | FBW-ECP-XML, FBW-ECP-TS, FBW-ECP-PR | Unverified |
| Speed brake lever (ped 3,2 `SPD BRK`) | `lua:XL24-A32NX:SPDBRK`: the script reads `L:A32NX_SPOILERS_ARMED` and `L:A32NX_SPOILERS_HANDLE_POSITION` | text `RET`, `ARM`, `50%`, `FULL`; the handle 0 retracted .. 1 full | `K:SPOILERS_TOGGLE` (RET <-> FULL), long press `K:SPOILERS_SET:8192` (1/2; 0..16384); both disarm | the parameter of `K:SPOILERS_SET` | FBW-SPLR, FBW-SCI, FBW-SIMVARS, FBW-API; README 2.1.1 KVAR, LUAFUNC | Unverified |
| Ground spoilers arm (ped 3,3 `GND SPLR`, the main page's 3,5 key repeated) | `L:A32NX_SPOILERS_ARMED` | 0/1 | `K:SPOILERS_ARM_TOGGLE` | as main 3,5 | FBW-API, FBW-SIMVARS, FBW-SPLR | Unverified |
| Flaps lever (ped 3,4 `FLAPS`, the main page's 3,4 key repeated) | `L:A32NX_FLAPS_HANDLE_INDEX` | 0 UP .. 4 FULL | `K:FLAPS_INCR`, long press `K:FLAPS_DECR` | as main 3,4 | FBW-API, FBW-SIMVARS, FBW-HANDLING | Unverified |
| Park brake (ped 3,5 `PARK`, the main page's 3,3 key repeated) | `L:A32NX_PARK_BRAKE_LEVER_POS` | 0/1 | `L:A32NX_PARK_BRAKE_LEVER_POS`, On `1` / Off `0` (L-Var write) | `K:PARKING_BRAKES` (as main 3,3) | FBW-API, FBW-SIMVARS, FBW-HANDLING | Unverified |
| Gear lever (ped 3,6 `GEAR`) | `L:A32NX_GEAR_HANDLE_POSITION` | 0 up .. 1 down (between while it moves) | `K:GEAR_DOWN`, long press only `K:GEAR_UP` (FlyByWire maps both to `L:A32NX_GEAR_LEVER_POSITION_REQUEST`) | readout only | FBW-HANDLING, FBW-GEAR-RS, FBW-SIMVARS, FBW-API | Unverified |
| LDG GEAR panel (ped 3,7) | `lua:XL24-A32NX:GEARIND`: the script reads `L:A32NX_ELEC_DC_2_BUS_IS_POWERED`, `L:A32NX_LGCIU_1_NOSE_GEAR_DOWNLOCKED`, `L:A32NX_LGCIU_1_LEFT_GEAR_DOWNLOCKED`, `L:A32NX_LGCIU_1_RIGHT_GEAR_DOWNLOCKED`, `L:A32NX_LGCIU_1_NOSE_GEAR_UNLOCKED`, `L:A32NX_LGCIU_1_LEFT_GEAR_UNLOCKED`, `L:A32NX_LGCIU_1_RIGHT_GEAR_UNLOCKED` | text `3 GRN`, `UNLK`, `UP`, blank without DC 2 | (read only) | none | FBW-MISC, FBW-SIMVARS; README 2.1.1 LUAFUNC, 3.5.1 | Unverified |
| Autobrake state (ped 3,8 `A/BRK`) | `lua:XL24-A32NX:ABRK`: the script reads `L:A32NX_AUTOBRAKES_ARMED_MODE` and `L:A32NX_AUTOBRAKES_DECEL_LIGHT` | text `OFF`, `LO`, `MED`, `MAX`, `DECEL`; mode 0..3 | (read only; the buttons are main 3,6 to 3,8) | none | FBW-SIMVARS, FBW-API, FBW-INTERIOR; README 2.1.1 LUAFUNC | Unverified |
| ENG 1 master switch (ped 4,1) | `(A:FUELSYSTEM VALVE SWITCH:1, Bool)` | 0/1 | `K:FUELSYSTEM_VALVE_OPEN:1` (ON), long press only `K:FUELSYSTEM_VALVE_CLOSE:1` (OFF) | the T3 form (Display Value, same commands, Mappings `0=OFF:1=ON`); readout only | FBW-MISC, FBW-INTERIOR, FBW-API; README 2.1 | Unverified |
| ENG 2 master switch (ped 4,2) | `(A:FUELSYSTEM VALVE SWITCH:2, Bool)` | 0/1 | `K:FUELSYSTEM_VALVE_OPEN:2` (ON), long press only `K:FUELSYSTEM_VALVE_CLOSE:2` (OFF) | as ENG 1 | FBW-MISC, FBW-INTERIOR, FBW-API; README 2.1 | Unverified |
| ENG MODE selector (ped 4,3) | `L:XMLVAR_ENG_MODE_SEL` | 0 CRANK, 1 NORM, 2 IGN | `lua:XL24-A32NX:ENGMODE(1)` (one position clockwise), long press `lua:XL24-A32NX:ENGMODE(-1)`; the script writes the L-Var (L-Var write, no FlyByWire R/W row) and sends the selector's own code by `SimCalculator`: `2 (>K:TURBINE_IGNITION_SWITCH_SET1) 2 (>K:TURBINE_IGNITION_SWITCH_SET2) (>H:A320_Neo_EICAS_2_Ignition_Start)` (IGN), `1 (>K:TURBINE_IGNITION_SWITCH_SET1) 1 (>K:TURBINE_IGNITION_SWITCH_SET2)` (NORM), `0 (>K:TURBINE_IGNITION_SWITCH_SET)` (CRANK); only while `L:A32NX_TOTAL_FUEL_QUANTITY` reads more than 0 | readout only | FBW-AIRBUS, FBW-INTERIOR, FBW-API; README 2.1.1 LUAFUNC, CALCULATOR, 3.5.1 | Unverified |
| Rudder trim left / right (ped 4,4 `RUD L` / 4,6 `RUD R`) | (none: RUD TRIM shows the result) | one trim step | `K:RUDDER_TRIM_LEFT` / `K:RUDDER_TRIM_RIGHT` | none | FBW-HANDLING, FBW-SCI | Unverified |
| Rudder trim readout and reset (ped 4,5 `RUD TRIM`) | `lua:XL24-A32NX:RUDTRIM`: the script reads `L:A32NX_ELEC_DC_2_BUS_IS_POWERED` and `L:A32NX_HYD_RUDDER_TRIM_FEEDBACK_ANGLE` | degrees, negative = left; text `L 2.5`, `R 1.0`, `0.0`, blank without DC 2 | `K:RUDDER_TRIM_RESET` | the script reads `(A:RUDDER TRIM PCT, Percent over 100)` x 20 (Flight Deck API) | FBW-SIMVARS, FBW-RTPI, FBW-FBI, FBW-HANDLING, FBW-SCI; README 2.1.1 LUAFUNC | Unverified |
| A/SKID & N/W STRG switch (ped 4,7 `A/SKID`) | `(A:ANTISKID BRAKES ACTIVE, Bool)` | 0 OFF, 1 ON | (read only by design; the cockpit switch sends `K:ANTISKID_BRAKES_TOGGLE`) | none | FBW-HANDLING, FBW-INTERIOR, FBW-API | Unverified |
| Brake pressure, triple indicator (ped 4,8 `BRK PSI`) | `lua:XL24-A32NX:BRKPSI`: the script reads `L:A32NX_ELEC_DC_ESS_BUS_IS_POWERED`, `L:A32NX_HYD_BRAKE_ALTN_LEFT_PRESS`, `L:A32NX_HYD_BRAKE_ALTN_RIGHT_PRESS` | psi; text `2.0 2.0` in 1000 psi (the needles' scale), blank without DC ESS | (read only) | none | FBW-INTERIOR-BRK; README 2.1.1 LUAFUNC | Unverified |
| DC 2 bus powered, the LDG GEAR panel's and the rudder trim display's bus (no key) | `L:A32NX_ELEC_DC_2_BUS_IS_POWERED` | 0/1 | (read only) | none | FBW-MISC, FBW-RTPI | Unverified |

Sources: the tags of [phase4-a32nx-pedestal.md](phase4-a32nx-pedestal.md), "Sources" (FlyByWire at the tag
v2024.1.0): FBW-ECP-XML (`A32NX_ECP.xml`), FBW-ECP-TS (`Ecp.ts`), FBW-OVHD-DISC
(`A32NXOverheadDiscretePublisher.ts`), FBW-ECP-PR (pull request #9840), FBW-HANDLING
(`A32NX_Interior_Handling.xml`), FBW-MISC (`A32NX_Interior_Misc.xml`), FBW-AIRBUS (`Airbus.xml`), FBW-GEAR-RS
(`gear.rs`), FBW-SPLR (`SpoilersHandler.cpp`), FBW-SCI (`SimConnectInterface.cpp`), FBW-FBI
(`FlyByWireInterface.cpp`), FBW-RTPI (`RTPI/instrument.tsx`), FBW-INTERIOR and FBW-INTERIOR-BRK
(`A320_NEO_INTERIOR.xml`), FBW-SIMVARS, FBW-API and README as above. Weak points the hand test decides: the
ECAM H-event sequences sent through the MobiFlight module and their lamps (code only, not in FBW-SIMVARS),
the ENG MODE L-Var write and its code, GEAR long press (never on the ground), the `K:SPOILERS_SET`
parameter, the rudder trim step and the trim readout's variable and sign, LDG GEAR from landing gear
computer 1 only, the brake pressure unit, and the long press on the ENG 1 / ENG 2 Dynamic Buttons.

## Cirrus Vision SF50 (MSFS 2024 default, V-1)

For [visionjet-sf50.md](visionjet-sf50.md): the profile `MSFS2024 VisionJet` for the Cirrus Vision SF50
(VisionJet) that comes with MSFS 2024 (not FlightFX's add-on). Every key of the profile has a row (positions
are page and row,column), the keys copied from the C172 G1000 pages too: their names are verified on the C172
only where its rows above say so, never on the SF50. Built with the SF50's input event list,
[reference/InputEvents-SF50.txt](reference/InputEvents-SF50.txt) (2026-11-16, 141 lines; "IE-SF50 n" = line
n). Generated, not yet sim-tested: every row is **Unverified** until the checklist section "VisionJet SF50
profile (V-1)" passes (then the date, MSFS version and SF50 preset). A key that fails gets "does not work" in
its row, and the row stays. Tags: the page doc's "Sources". Every `H:` command needs the MobiFlight WASM
module.

Aircraft string (PD-LOG, PilotsDeck20261116.log): the path of the preset's `aircraft.cfg` in the package
`fs24-microsoft-aircraft-sf50`:
`...\simobjects\airplanes\microsoft_sf50\presets\microsoft\<preset>\config\aircraft.cfg`, with the presets
`sf50_family`, `sf50_executive` and `sf50_complete`; the Profile Manager search string is `microsoft_sf50`.

| Function | Read | Units | Write | Fallback | Source | Verified |
|---|---|---|---|---|---|---|
| main 1,1 `BAT` | `B:sf50_electrical_battery_1_switch` | B-var value (0/1 expected) | `B:sf50_electrical_battery_1_switch`, On `1` / Off `0` | Empty (no battery key) | IE-SF50 80; README 2.1.1; V-1 A-5 | Unverified |
| main 1,2 `N1` | `(A:TURB ENG N1:1, Percent)` | Percent | none | - | SDK-ENGV | Unverified |
| main 1,4 `PARK` | `(A:BRAKE PARKING POSITION, Bool)` | Bool | `K:PARKING_BRAKES` | - | AM; AM, SDK-GEARV | Unverified |
| main 1,5 `GEAR` | `(A:GEAR HANDLE POSITION, Bool)` | Bool | none | - | SDK-GEARV | Unverified |
| main 1,6 `FLAPS` | `(A:FLAPS HANDLE INDEX, number)` | number | Main `K:FLAPS_INCR`, Second (long press) `K:FLAPS_DECR` | Mappings after the test (number per detent) | SDK-FCE, README 2.1; SDK-CTLV | Unverified |
| main 2,1 `AP` | `(A:AUTOPILOT MASTER, Bool)` | Bool | `K:AP_MASTER` | - | AM | Unverified |
| main 2,2 `HDG` | `(A:AUTOPILOT HEADING LOCK, Bool)` | Bool | `K:AP_HDG_HOLD` | - | SDK-APE; SDK-APV | Unverified |
| main 2,3 `ALT` | `(A:AUTOPILOT ALTITUDE LOCK, Bool)` | Bool | `K:AP_ALT_HOLD` | - | SDK-APE; SDK-APV | Unverified |
| main 2,4 `VS` | `(A:AUTOPILOT VERTICAL HOLD, Bool)` | Bool | `K:AP_VS_HOLD` | - | SDK-APE; SDK-APV | Unverified |
| main 2,5 `NAV` | `(A:AUTOPILOT NAV1 LOCK, Bool)` | Bool | `K:AP_NAV1_HOLD` | - | SDK-APE; SDK-APV | Unverified |
| main 2,6 `APR` | `(A:AUTOPILOT APPROACH HOLD, Bool)` | Bool | `K:AP_APR_HOLD` | - | SDK-APE; SDK-APV | Unverified |
| main 2,7 `FLC` | `(A:AUTOPILOT FLIGHT LEVEL CHANGE, Bool)` | Bool | `K:FLIGHT_LEVEL_CHANGE` | - | SDK-APE; SDK-APV | Unverified |
| main 2,8 `FD` | `(A:AUTOPILOT FLIGHT DIRECTOR ACTIVE, Bool)` | Bool | `K:TOGGLE_FLIGHT_DIRECTOR` | - | SDK-APE; SDK-APV | Unverified |
| main 3,1 `COM1` | Active `(A:COM ACTIVE FREQUENCY:1, MHz)`, Standby `(A:COM STANDBY FREQUENCY:1, MHz)` | MHz | `K:COM_STBY_RADIO_SWAP` | - | SDK-RADE; SDK-RADV, SDK-UNITS | Unverified |
| main 3,2 `XPDR` | `(A:TRANSPONDER CODE:1, Bco16)` | Bco16 | none | - | SDK-RADV | Unverified |
| main 3,3 `ATC` | none (a sim window has no state) | - | `K:SIMUI_WINDOW_HIDESHOW` | - | SDK-MISCE | Unverified |
| main 3,4 `MAP` | none (a sim window has no state) | - | `K:FLIGHT_MAP` | - | SDK-MISCE | Unverified |
| main 3,5 `CDI` | `(A:GPS DRIVES NAV1, Bool)` | Bool | `K:TOGGLE_GPS_DRIVES_NAV1` | - | SDK-RADE; SDK-RADV | Unverified |
| main 3,6 `BARO` | `(A:KOHLSMAN SETTING HG:1, inHg)` | inHg | `K:BAROMETRIC` | STD in V-2 (HH-MS) | SDK-INSTE; SDK-SYSV | Unverified |
| main 4,1 `NAV LT` | `B:sf50_lighting_nav_lights_intercept` | B-var value (0/1 expected) | `B:sf50_lighting_nav_lights_intercept`, On `1` / Off `0` | `K:TOGGLE_NAV_LIGHTS`, read `(A:LIGHT NAV, Bool)` | IE-SF50 130; README 2.1.1; V-1 A-5, A-15 | Unverified |
| main 4,3 `STRB` | `B:lighting_strobe_1` | B-var value (0/1 expected) | `B:lighting_strobe_1`, On `1` / Off `0` | `K:STROBES_TOGGLE`, read `(A:LIGHT STROBE, Bool)` | IE-SF50 40; README 2.1.1; V-1 A-5 | Unverified |
| main 4,4 `LDG` | `B:sf50_lighting_landing_lights` | B-var value (0/1 expected) | `B:sf50_lighting_landing_lights`, On `1` / Off `0` | `K:LANDING_LIGHTS_TOGGLE`, read `(A:LIGHT LANDING, Bool)` | IE-SF50 129; README 2.1.1; V-1 A-5 | Unverified |
| main 4,5 `TAXI` | `(A:LIGHT TAXI, Bool)` | Bool | `K:TOGGLE_TAXI_LIGHTS` | Empty (the list has no taxi light) | SDK-ELECE; no taxi B-var in IE-SF50, V-1 A-5, A-15; SDK-SYSV | Unverified |
| main 4,6 `PITOT` | `B:deice_pitot_1` | B-var value (0/1 expected) | `B:deice_pitot_1`, On `1` / Off `0` | `K:PITOT_HEAT_TOGGLE`, read `(A:PITOT HEAT, Bool)` | IE-SF50 31; README 2.1.1; V-1 A-5 | Unverified |
| trim 2,2 `TRIM UP` (the C172's key) | none (the readouts 3,2 and 3,3 show the result) | - | `K:ELEV_TRIM_UP` | - | SDK-FCE | Unverified |
| trim 3,2 `TRIM` (the C172's key) | `(A:ELEVATOR TRIM PCT EX2, percent)` | percent | none | - | SDK-CTLV, SDK-UNITS | Unverified |
| trim 3,3 `TRIM DEG` (the C172's key) | `(A:ELEVATOR TRIM POSITION, degrees)` | degrees | none | - | SDK-CTLV, SDK-UNITS | Unverified |
| trim 3,4 `TRIM` (the C172's key) | `(A:ELEVATOR TRIM PCT EX2, percent)` | percent | none | - | SDK-CTLV, SDK-UNITS | Unverified |
| trim 4,2 `TRIM DN` (the C172's key) | none (the readouts 3,2 and 3,3 show the result) | - | `K:ELEV_TRIM_DN` | - | SDK-FCE | Unverified |
| views 1,2 `COCKPIT` (the C172's key) | `(A:CAMERA STATE, Enum)` | Enum | `(A:CAMERA STATE, Enum)`, On `$=2` / Off `` | - | SDK-CAMV, README 2.1.1, 2.1.2; SDK-CAMV, SDK-UNITS | Unverified |
| views 1,3 `EXTERNAL` (the C172's key) | `(A:CAMERA STATE, Enum)` | Enum | `(A:CAMERA STATE, Enum)`, On `$2,=3<` / Off `` | - | SDK-CAMV, README 2.1.1, 2.1.2; SDK-CAMV, SDK-UNITS | Unverified |
| views 1,4 `CAMERA` (the C172's key) | `(A:CAMERA STATE, Enum)` | Enum | none | - | SDK-CAMV, SDK-UNITS | Unverified |
| views 1,5 `VIEW` (the C172's key) | `(A:CAMERA VIEW TYPE AND INDEX:0, Enum)` | Enum | none | - | SDK-CAMV, SDK-UNITS | Unverified |
| views 1,6 `VIEW NO` (the C172's key) | `(A:CAMERA VIEW TYPE AND INDEX:1, number)` | number | none | - | SDK-CAMV, SDK-UNITS | Unverified |
| vspeeds 1,2 `VS0` (the C172's key) | `(A:DESIGN SPEED VS0, knots)` | knots | none | - | SDK-FMV, SDK-UNITS | Unverified |
| vspeeds 1,3 `VS1` (the C172's key) | `(A:DESIGN SPEED VS1, knots)` | knots | none | - | SDK-FMV, SDK-UNITS | Unverified |
| vspeeds 1,4 `VR` (the C172's key) | `(A:DESIGN SPEED MIN ROTATION, knots)` | knots | none | - | SDK-FMV, SDK-UNITS | Unverified |
| vspeeds 1,6 `CLIMB` (the C172's key) | `(A:DESIGN SPEED CLIMB, knots)` | knots | none | - | SDK-FMV, SDK-UNITS | Unverified |
| vspeeds 2,2 `CRUISE` (the C172's key) | `(A:DESIGN SPEED VC, knots)` | knots | none | - | SDK-FMV, SDK-UNITS | Unverified |
| vspeeds 2,4 `VNE` (the C172's key) | `(A:REFERENCE SPEED MAX IAS, knots)` | knots | none | - | SDK-FMV, SDK-UNITS | Unverified |
| vspeeds 2,5 `VFE` (the C172's key) | `(A:FLAPS CURRENT SPEED LIMITATION, knots)` | knots | none | - | SDK-CTLV, SDK-UNITS | Unverified |
| simrate 1,2 `1X` (the C172's key) | `(A:SIMULATION RATE, number)` | number | `lua:XL24-SIMRATE:SET(1)` (steps `K:SIM_RATE_INCR` / `K:SIM_RATE_DECR`) | - | README 2.1.1 LUAFUNC, 3.5.1; SDK-MISCE; LR153-C4; SDK-ENVV, PD-SRC | Unverified |
| simrate 1,3 `SLOWER` (the C172's key) | none | - | `K:SIM_RATE_DECR` | - | SDK-MISCE | Unverified |
| simrate 1,4 `RATE` (the C172's key) | `(A:SIMULATION RATE, number)` | number | Main `K:SIM_RATE_INCR`, Second (long press) `K:SIM_RATE_DECR` | - | SDK-MISCE, README 2.1; SDK-ENVV, PD-SRC | Unverified |
| simrate 1,5 `FASTER` (the C172's key) | none | - | `K:SIM_RATE_INCR` | - | SDK-MISCE | Unverified |
| compad 1,2 `COM1` (the C172's key) | Active `(A:COM ACTIVE FREQUENCY:1, MHz)`, Standby `(A:COM STANDBY FREQUENCY:1, MHz)` | MHz | `K:COM_STBY_RADIO_SWAP` | - | SDK-RADE; SDK-RADV | Unverified |
| compad 1,3 `ENTRY` (the C172's key) | `X:XL24_COMPAD_ENTRY` | PilotsDeck internal variable | none | - | README 2.1.1 INTERNAL; written by the script | Unverified |
| compad 1,6 `7` (the C172's key) | none | - | `lua:XL24-COMPAD:DIGIT(7)` | - | README 2.1.1 LUAFUNC | Unverified |
| compad 1,7 `8` (the C172's key) | none | - | `lua:XL24-COMPAD:DIGIT(8)` | - | README 2.1.1 LUAFUNC | Unverified |
| compad 1,8 `9` (the C172's key) | none | - | `lua:XL24-COMPAD:DIGIT(9)` | - | README 2.1.1 LUAFUNC | Unverified |
| compad 2,2 `STBY ID` (the C172's key) | `(A:COM STANDBY FREQ IDENT:1, String)` | String | none | - | SDK-RADV; PD-SRC string A-Var | Unverified |
| compad 2,6 `4` (the C172's key) | none | - | `lua:XL24-COMPAD:DIGIT(4)` | - | README 2.1.1 LUAFUNC | Unverified |
| compad 2,7 `5` (the C172's key) | none | - | `lua:XL24-COMPAD:DIGIT(5)` | - | README 2.1.1 LUAFUNC | Unverified |
| compad 2,8 `6` (the C172's key) | none | - | `lua:XL24-COMPAD:DIGIT(6)` | - | README 2.1.1 LUAFUNC | Unverified |
| compad 3,6 `1` (the C172's key) | none | - | `lua:XL24-COMPAD:DIGIT(1)` | - | README 2.1.1 LUAFUNC | Unverified |
| compad 3,7 `2` (the C172's key) | none | - | `lua:XL24-COMPAD:DIGIT(2)` | - | README 2.1.1 LUAFUNC | Unverified |
| compad 3,8 `3` (the C172's key) | none | - | `lua:XL24-COMPAD:DIGIT(3)` | - | README 2.1.1 LUAFUNC | Unverified |
| compad 4,6 `CLR` (the C172's key) | none | - | Main `lua:XL24-COMPAD:BACK`, Second (long press) `lua:XL24-COMPAD:CLEAR` | - | README 2.1.1 LUAFUNC, 2.1 | Unverified |
| compad 4,7 `0` (the C172's key) | none | - | `lua:XL24-COMPAD:DIGIT(0)` | - | README 2.1.1 LUAFUNC | Unverified |
| compad 4,8 `ENT` (the C172's key) | none (COM1 at 1,2 shows the result) | - | Main `lua:XL24-COMPAD:ENTER`, Second (long press) `lua:XL24-COMPAD:ENTER_SWAP` | - | README 2.1.1 LUAFUNC, 2.1 | Unverified |
| autopilot 1,2 `AP` | `(A:AUTOPILOT MASTER, Bool)` | Bool | `K:AP_MASTER` | - | SDK-APE; AM; SDK-APV | Unverified |
| autopilot 1,3 `FD` | `(A:AUTOPILOT FLIGHT DIRECTOR ACTIVE, Bool)` | Bool | `K:TOGGLE_FLIGHT_DIRECTOR` | - | SDK-APE; SDK-APT; SDK-APV | Unverified |
| autopilot 1,4 `HDG` | `(A:AUTOPILOT HEADING LOCK, Bool)` | Bool | `K:AP_HDG_HOLD` | - | SDK-APE; SDK-APV | Unverified |
| autopilot 1,5 `NAV` | `(A:AUTOPILOT NAV1 LOCK, Bool)` | Bool | `K:AP_NAV1_HOLD` | - | SDK-APE; SDK-APT; SDK-APV | Unverified |
| autopilot 1,6 `APR` | `(A:AUTOPILOT APPROACH HOLD, Bool)` | Bool | `K:AP_APR_HOLD` | - | SDK-APE; SDK-APT; SDK-APV | Unverified |
| autopilot 1,8 `VNV` | `L:XMLVAR_VNAVButtonValue` | L-Var value | `B:sf50_autopilot_vnav_mode`, On `1` / Off `0` | L-Var write `L:XMLVAR_VNAVButtonValue` On `1` / Off `0`; else readout only | IE-SF50 62; README 2.1.1; V-1 A-5; HH-MS; SDK-APT | Unverified |
| autopilot 2,1 `ALT` | `(A:AUTOPILOT ALTITUDE LOCK, Bool)` | Bool | `K:AP_ALT_HOLD` | - | SDK-APE; SDK-APT; SDK-APV | Unverified |
| autopilot 2,2 `HDG+` | none | - | `K:HEADING_BUG_INC` | - | SDK-APE | Unverified |
| autopilot 2,3 `CRS+` | none | - | Main `H:AS3000_PFD_1_CRS_INC`, Second (long press) `K:VOR1_OBI_FAST_INC` | the long press K-event only | WT-G3000H; SF50-PKG; weak, V-1 A-15; SDK-RADE; README 2.1 | Unverified |
| autopilot 2,4 `ALT+` | none | - | Main `K:AP_ALT_VAR_INC`, Second (long press) `K:AP_ALT_VAR_INC:1000` | - | SDK-APE; SDK-AS1000; README 2.1.1, 2.1; A-4 | Unverified |
| autopilot 2,5 `VS+` | none | - | `K:AP_VS_VAR_INC` | - | SDK-APE | Unverified |
| autopilot 2,6 `SPD+` | none | - | `K:AP_SPD_VAR_INC` | - | SDK-APE | Unverified |
| autopilot 2,8 `A/T` | `(A:AUTOPILOT THROTTLE ARM, Bool)` | Bool | `K:AUTO_THROTTLE_ARM` | readout only (command none) | SDK-APE; FORUM-24; V-1 A-15; SDK-APV | Unverified |
| autopilot 3,1 `VS` | `(A:AUTOPILOT VERTICAL HOLD, Bool)` | Bool | `K:AP_VS_HOLD` | - | SDK-APE; SDK-APV | Unverified |
| autopilot 3,2 `HDG BUG` | `(A:AUTOPILOT HEADING LOCK DIR, Degrees)` | Degrees | `H:Garmin_AP_HDG_Sync` | `K:AP_HDG_CURRENT_HDG_SET` (as the C172) | WT-G3000H; weak, V-1 A-15; SDK-APV | Unverified |
| autopilot 3,3 `CRS1` | `(A:NAV OBS:1, Degrees)` | Degrees | `H:AS3000_PFD_1_CRS_PUSH` | readout only | WT-G3000H; SF50-PKG; weak, V-1 A-15; SDK-RADV | Unverified |
| autopilot 3,4 `ALT SEL` | `(A:AUTOPILOT ALTITUDE LOCK VAR, Feet)` | Feet | none | - | SDK-APV; A-5 | Unverified |
| autopilot 3,5 `VS TGT` | `(A:AUTOPILOT VERTICAL HOLD VAR, Feet/minute)` | Feet/minute | none | - | SDK-APV | Unverified |
| autopilot 3,6 `FLC SPD` | `(A:AUTOPILOT AIRSPEED HOLD VAR, Knots)` | Knots | none | - | SDK-APV | Unverified |
| autopilot 3,7 `LVL` | `(A:AUTOPILOT WING LEVELER, Bool)` | Bool | `K:AP_WING_LEVELER` | - | SDK-APE; V-1 A-15; SDK-APV | Unverified |
| autopilot 3,8 `TOGA` | `L:WT_TOGA_ACTIVE` | L-Var value | none | `(A:AUTOPILOT TAKEOFF POWER ACTIVE, Bool)` | HH-MS; weak, V-1 A-15 | Unverified |
| autopilot 4,1 `FLC` | `(A:AUTOPILOT FLIGHT LEVEL CHANGE, Bool)` | Bool | `K:FLIGHT_LEVEL_CHANGE` | - | SDK-APE; SDK-APT; A-9; SDK-APV | Unverified |
| autopilot 4,2 `HDG-` | none | - | `K:HEADING_BUG_DEC` | - | SDK-APE | Unverified |
| autopilot 4,3 `CRS-` | none | - | Main `H:AS3000_PFD_1_CRS_DEC`, Second (long press) `K:VOR1_OBI_FAST_DEC` | the long press K-event only | WT-G3000H; SF50-PKG; weak, V-1 A-15; SDK-RADE; README 2.1 | Unverified |
| autopilot 4,4 `ALT-` | none | - | Main `K:AP_ALT_VAR_DEC`, Second (long press) `K:AP_ALT_VAR_DEC:1000` | - | SDK-APE; SDK-AS1000; README 2.1.1, 2.1; A-4 | Unverified |
| autopilot 4,5 `VS-` | none | - | `K:AP_VS_VAR_DEC` | - | SDK-APE | Unverified |
| autopilot 4,6 `SPD-` | none | - | `K:AP_SPD_VAR_DEC` | - | SDK-APE | Unverified |
| autopilot 4,8 `A/T MGD` | `(A:AUTOPILOT MANAGED THROTTLE ACTIVE, Bool)` | Bool | none | - | SDK-APV | Unverified |
| xpdr 1,2 `XPDR` (the C172's key) | `(A:TRANSPONDER CODE:1, Bco16)` | Bco16 | none | - | SDK-RADV | Unverified |
| xpdr 1,3 `ENTRY` (the C172's key) | `X:XL24_XPDRPAD_ENTRY` | PilotsDeck internal variable | none | - | README 2.1.1 INTERNAL; written by the script | Unverified |
| xpdr 1,4 `MODE` (the C172's key) | `(A:TRANSPONDER STATE:1, Enum)` | Enum | none | - | SDK-RADV | Unverified |
| xpdr 1,6 `7` (the C172's key) | none | - | `lua:XL24-XPDRPAD:DIGIT(7)` | - | README 2.1.1 LUAFUNC | Unverified |
| xpdr 2,2 `STBY` (the C172's key) | `(A:TRANSPONDER STATE:1, Enum)` | Enum | `(A:TRANSPONDER STATE:1, Enum)`, On `$=1` / Off `` | - | SDK-RADV, README 2.1.1, 2.1.2; SDK-RADV | Unverified |
| xpdr 2,3 `ON` (the C172's key) | `(A:TRANSPONDER STATE:1, Enum)` | Enum | `(A:TRANSPONDER STATE:1, Enum)`, On `$=3` / Off `` | - | SDK-RADV, README 2.1.1, 2.1.2; SDK-RADV | Unverified |
| xpdr 2,4 `ALT` (the C172's key) | `(A:TRANSPONDER STATE:1, Enum)` | Enum | `(A:TRANSPONDER STATE:1, Enum)`, On `$=4` / Off `` | - | SDK-RADV, README 2.1.1, 2.1.2; SDK-RADV | Unverified |
| xpdr 2,6 `4` (the C172's key) | none | - | `lua:XL24-XPDRPAD:DIGIT(4)` | - | README 2.1.1 LUAFUNC | Unverified |
| xpdr 2,7 `5` (the C172's key) | none | - | `lua:XL24-XPDRPAD:DIGIT(5)` | - | README 2.1.1 LUAFUNC | Unverified |
| xpdr 2,8 `6` (the C172's key) | none | - | `lua:XL24-XPDRPAD:DIGIT(6)` | - | README 2.1.1 LUAFUNC | Unverified |
| xpdr 3,2 `IDENT` (the C172's key) | `(A:TRANSPONDER IDENT:1, Bool)` | Bool | `K:XPNDR_IDENT_ON` | - | SDK-RADE; SDK-RADV | Unverified |
| xpdr 3,3 `VFR` (the C172's key) | none | - | `K:XPNDR_SET:4608` | - | SDK-RADE | Unverified |
| xpdr 3,6 `1` (the C172's key) | none | - | `lua:XL24-XPDRPAD:DIGIT(1)` | - | README 2.1.1 LUAFUNC | Unverified |
| xpdr 3,7 `2` (the C172's key) | none | - | `lua:XL24-XPDRPAD:DIGIT(2)` | - | README 2.1.1 LUAFUNC | Unverified |
| xpdr 3,8 `3` (the C172's key) | none | - | `lua:XL24-XPDRPAD:DIGIT(3)` | - | README 2.1.1 LUAFUNC | Unverified |
| xpdr 4,6 `CLR` (the C172's key) | none | - | Main `lua:XL24-XPDRPAD:BACK`, Second (long press) `lua:XL24-XPDRPAD:CLEAR` | - | README 2.1.1 LUAFUNC, 2.1 | Unverified |
| xpdr 4,7 `0` (the C172's key) | none | - | `lua:XL24-XPDRPAD:DIGIT(0)` | - | README 2.1.1 LUAFUNC | Unverified |
| xpdr 4,8 `ENT` (the C172's key) | none (XPDR at 1,2 shows the result) | - | `lua:XL24-XPDRPAD:ENTER` | - | README 2.1.1 LUAFUNC | Unverified |
| radios 1,2 `NAV1` (the C172's key) | Active `(A:NAV ACTIVE FREQUENCY:1, MHz)`, Standby `(A:NAV STANDBY FREQUENCY:1, MHz)` | MHz | `K:NAV1_RADIO_SWAP` | - | SDK-RADE; SDK-RADV | Unverified |
| radios 1,3 `NAV1 ID` (the C172's key) | `(A:NAV IDENT:1, String)` | String | none | - | SDK-RADV | Unverified |
| radios 1,4 `NAV2` (the C172's key) | Active `(A:NAV ACTIVE FREQUENCY:2, MHz)`, Standby `(A:NAV STANDBY FREQUENCY:2, MHz)` | MHz | `K:NAV2_RADIO_SWAP` | - | SDK-RADE; SDK-RADV | Unverified |
| radios 1,5 `NAV2 ID` (the C172's key) | `(A:NAV IDENT:2, String)` | String | none | - | SDK-RADV | Unverified |
| radios 1,6 `COM2` (the C172's key) | Active `(A:COM ACTIVE FREQUENCY:2, MHz)`, Standby `(A:COM STANDBY FREQUENCY:2, MHz)` | MHz | `K:COM2_RADIO_SWAP` | - | SDK-RADE; SDK-RADV | Unverified |
| radios 1,7 `COM2 ID` (the C172's key) | `(A:COM ACTIVE FREQ IDENT:2, String)` | String | none | - | SDK-RADV | Unverified |
| radios 2,2 `MHZ+` (the C172's key) | none | - | `K:NAV1_RADIO_WHOLE_INC` | - | SDK-RADE | Unverified |
| radios 2,3 `KHZ+` (the C172's key) | none | - | `K:NAV1_RADIO_FRACT_INC` | - | SDK-RADE | Unverified |
| radios 2,4 `MHZ+` (the C172's key) | none | - | `K:NAV2_RADIO_WHOLE_INC` | - | SDK-RADE | Unverified |
| radios 2,5 `KHZ+` (the C172's key) | none | - | `K:NAV2_RADIO_FRACT_INC` | - | SDK-RADE | Unverified |
| radios 2,6 `MHZ+` (the C172's key) | none | - | `K:COM2_RADIO_WHOLE_INC` | - | SDK-RADE | Unverified |
| radios 2,7 `KHZ+` (the C172's key) | none | - | `K:COM2_RADIO_FRACT_INC` | - | SDK-RADE | Unverified |
| radios 3,2 `MHZ-` (the C172's key) | none | - | `K:NAV1_RADIO_WHOLE_DEC` | - | SDK-RADE | Unverified |
| radios 3,3 `KHZ-` (the C172's key) | none | - | `K:NAV1_RADIO_FRACT_DEC` | - | SDK-RADE | Unverified |
| radios 3,4 `MHZ-` (the C172's key) | none | - | `K:NAV2_RADIO_WHOLE_DEC` | - | SDK-RADE | Unverified |
| radios 3,5 `KHZ-` (the C172's key) | none | - | `K:NAV2_RADIO_FRACT_DEC` | - | SDK-RADE | Unverified |
| radios 3,6 `MHZ-` (the C172's key) | none | - | `K:COM2_RADIO_WHOLE_DEC` | - | SDK-RADE | Unverified |
| radios 3,7 `KHZ-` (the C172's key) | none | - | `K:COM2_RADIO_FRACT_DEC` | - | SDK-RADE | Unverified |
| radios 4,6 `MIC1` (the C172's key) | `(A:COM TRANSMIT:1, Bool)` | Bool | `K:PILOT_TRANSMITTER_SET:0` | - | SDK-RADE; SDK-RADV | Unverified |
| radios 4,7 `MIC2` (the C172's key) | `(A:COM TRANSMIT:2, Bool)` | Bool | `K:PILOT_TRANSMITTER_SET:1` | - | SDK-RADE; SDK-RADV | Unverified |
| engine 1,2 `N1` | `(A:TURB ENG N1:1, Percent)` | Percent | none | - | SDK-ENGV | Unverified |
| engine 1,3 `N2` | `(A:TURB ENG N2:1, Percent)` | Percent | none | - | SDK-ENGV | Unverified |
| engine 1,4 `ITT` | `(A:TURB ENG ITT:1, Celsius)` | Celsius | none | - | SDK-ENGV; SDK-UNITS | Unverified |
| engine 1,5 `FF PPH` | `(A:TURB ENG FUEL FLOW PPH:1, Pounds per hour)` | Pounds per hour | none | - | SDK-ENGV | Unverified |
| engine 2,2 `ENG RUN` | `(A:GENERAL ENG COMBUSTION:1, Bool)` | Bool | none | - | SDK-ENGV | Unverified |
| engine 2,3 `IGN` | `(A:TURB ENG IGNITION SWITCH:1, Bool)` | Bool | none | - | SDK-ENGV; V-1 A-15 | Unverified |
| engine 3,2 `FUEL L` | `(A:FUEL LEFT QUANTITY, Gallons)` | Gallons | none | - | SDK-FUELV | Unverified |
| engine 3,3 `FUEL R` | `(A:FUEL RIGHT QUANTITY, Gallons)` | Gallons | none | - | SDK-FUELV | Unverified |
| engine 3,4 `FUEL TOT` | `(A:FUEL TOTAL QUANTITY, Gallons)` | Gallons | none | - | SDK-FUELV | Unverified |

## Cirrus Vision SF50 (MSFS 2024 default, V-2)

For [visionjet-sf50.md](visionjet-sf50.md), V-2: the keys V-2 adds to or changes in the profile `MSFS2024
VisionJet` (14 pages, 180 keys). The V-1 rows above stay for every other key; where a key below has a V-1 row
(main 1,4, 3,6 and the trim page), this section's row is the current one, and V-1's trim 3,2 `TRIM` and 3,3
`TRIM DEG` rows are no longer keys of the profile. Names from the SF50's input event list
([reference/InputEvents-SF50.txt](reference/InputEvents-SF50.txt), "IE-SF50 n" = line n), the MSFS SDK and the
C172 trim page. Which value each SF50 input event takes per position, and which SimVar it drives, is not
published: On/Off values, Mappings and Formats are working values until the sim check (V-2 A-2, A-21). G1 =
press writes 1 (on), long press writes 0 (off) (PD-LONG, V-2 A-6). Generated, not yet sim-tested: every row is
**Unverified** until the checklist section "VisionJet SF50 profile (V-2)" passes. Tags: the page doc's
"Sources". "Verified by scmon capture 2026-11-16": the cockpit control showed these values in a `tools/scmon`
capture (MSFS 2024, version not recorded; SCMON-SF50); the key's own press stays Unverified.

| Function | Read | Units | Write | Fallback | Source | Verified |
|---|---|---|---|---|---|---|
| main 1,4 `PARK` | `(A:BRAKE PARKING POSITION, Bool)` | Bool | `B:sf50_handling_parking_brake`, On `1` / Off `0` | readout only (command none) | IE-SF50 117; README 2.1.1, 2.1.2; AM, SDK-GEARV; SCMON-SF50 | Unverified (key press); the cockpit handle moves the B-var 0/1 and `BRAKE PARKING POSITION` follows it: verified by scmon capture 2026-11-16 |
| main 1,4 `PARK`, V-1's write | `(A:BRAKE PARKING POSITION, Bool)` | Bool | `K:PARKING_BRAKES` | replaced by the B-var row above | AM; SCMON-SF50 | **Does not work** in the SF50 (hand test 2026-11-16, scmon capture; MSFS 2024, version not recorded): with the brake set, the SimVar went 1, 0, 1 within about 0.1 s and the B-var stayed 1 |
| main 3,6 `BARO` | `(A:KOHLSMAN SETTING HG:1, inHg)` | inHg | Main `K:BAROMETRIC`, Second (long press) `K:BAROMETRIC_STD_PRESSURE` | long press `B:autopilot_baro_1_sync` On `1` / Off `1` (IE-SF50 29); else no STD | SDK-INSTE; HH-MS; README 2.1; V-2 A-10; SDK-SYSV | Unverified |
| main 4,2 `RECOG` | `B:sf50_lighting_recognition_lights_intercept` | B-var value (0/1 expected) | `B:sf50_lighting_recognition_lights_intercept`, On `1` / Off `0` | Empty | IE-SF50 132; README 2.1.1; weak, V-2 A-4 | Unverified (no change seen in two scmon runs, 2026-11-16) |
| main 4,7 `ICE` (= iceenv 1,3) | `B:sf50_deice_wingstab` | B-var value (0/1 expected) | G1 `B:sf50_deice_wingstab` | readout of the B-var, Mappings `0=OFF:1=ON` (A-6); readout of `STRUCTURAL DEICE SWITCH` (A-2) | IE-SF50 78; SF50-PKG; SF50-FLT; PD-LONG; V-2 A-6, A-13 | Unverified (key press); 0 off / 1 on and `STRUCTURAL DEICE SWITCH` following it: verified by scmon capture 2026-11-16 |
| trim 2,2 `TRIM UP` (the C172's key) | none (the gauge 3,4 shows the result) | - | `K:ELEV_TRIM_UP` | - | SDK-FCE | Unverified |
| trim 3,4 `TRIM` gauge (the C172's key) | `(A:ELEVATOR TRIM PCT EX2, percent)` | percent | none | - | SDK-CTLV, SDK-UNITS | Unverified |
| trim 3,6 `RUD L` (the C172's key) | none (the gauge 3,7 shows the result) | - | `K:RUDDER_TRIM_LEFT` | `B:handling_ruddertrim_1` (IE-SF50 35) after the sim check | SDK-FCE; V-2 A-11 | Unverified |
| trim 3,7 `RUD TRIM` gauge (the C172's key) | `(A:RUDDER TRIM PCT, percent)` | percent | none | - | SDK-CTLV, SDK20-CTLV, SDK-UNITS | Unverified |
| trim 3,8 `RUD R` (the C172's key) | none (the gauge 3,7 shows the result) | - | `K:RUDDER_TRIM_RIGHT` | `B:handling_ruddertrim_1` (IE-SF50 35) after the sim check | SDK-FCE; V-2 A-11 | Unverified |
| trim 4,2 `TRIM DN` (the C172's key) | none (the gauge 3,4 shows the result) | - | `K:ELEV_TRIM_DN` | - | SDK-FCE | Unverified |
| autopilot 1,7 `FMS SPD` | `B:sf50_autopilot_fms_speed_mode` | B-var value (holds its state) | `B:sf50_autopilot_fms_speed_mode`, On `1` / Off `1` (every press writes 1) | Empty | IE-SF50 53; SF50-PKG; README 2.1.1; V-2 A-5 | Unverified (key press); exclusive with MAN SPD (1 and 0), each holds its state: verified by scmon capture 2026-11-16 |
| autopilot 2,7 `YD` | `(A:AUTOPILOT YAW DAMPER, Bool)` | Bool | `K:YAW_DAMPER_TOGGLE` | readout only | SDK-APE; SDK-APV; SF50-FLT; weak, V-2 A-9 | Unverified |
| autopilot 4,7 `MAN SPD` | `B:sf50_autopilot_man_speed_mode` | B-var value (holds its state) | `B:sf50_autopilot_man_speed_mode`, On `1` / Off `1` (every press writes 1) | Empty | IE-SF50 58; SF50-PKG; README 2.1.1; V-2 A-5 | Unverified (key press); exclusive with FMS SPD (1 and 0), each holds its state: verified by scmon capture 2026-11-16 |
| systems 1,2 `BAT 2` | `B:sf50_electrical_battery_2_switch` | B-var value (0/1 expected) | G1 `B:sf50_electrical_battery_2_switch` | readout of the B-var, Mappings `0=OFF:1=ON` (A-6); Empty (A-2) | IE-SF50 81; PD-LONG; V-2 A-3, A-6 | Unverified (key press, battery index); 1 on / 0 off: verified by scmon capture 2026-11-16 (`ELECTRICAL MASTER BATTERY:1` to `:3` did not change) |
| systems 1,3 `GEN 1` | `B:sf50_electrical_gen_1_switch` | B-var value (0/1 expected) | G1 `B:sf50_electrical_gen_1_switch` | as BAT 2 | IE-SF50 83; SF50-FLT; PD-LONG; V-2 A-3, A-6 | Unverified (key press, generator index); 1 on / 0 off: verified by scmon capture 2026-11-16 (`GENERAL ENG MASTER ALTERNATOR:1` and `:2` did not change) |
| systems 1,4 `GEN 2` | `B:sf50_electrical_gen_2_switch` | B-var value (0/1 expected) | G1 `B:sf50_electrical_gen_2_switch` | as BAT 2 | IE-SF50 84; SF50-FLT; PD-LONG; V-2 A-3, A-6 | Unverified (key press, generator index); 1 on / 0 off: verified by scmon capture 2026-11-16 (`GENERAL ENG MASTER ALTERNATOR:1` and `:2` did not change) |
| systems 1,6 `BUS V` | `(A:ELECTRICAL BUS VOLTAGE:1, Volts)`, Format `2.1` | Volts; bus index 1 on the SF50's named buses is open | none | another index | SDK-ELECV; phase3-systems.md | Unverified |
| systems 1,8 `LOAD A` | `(A:ELECTRICAL TOTAL LOAD AMPS, Amperes)`, Format `1.1` | Amperes | none | - | SDK-ELECV; phase3-systems.md | Unverified |
| systems 2,2 `ENG KNOB` | `B:sf50_engine_run_knob`, Mappings `0=STOP:1=RUN` | B-var value (0 STOP / 1 RUN expected) | none (guard) | Mappings from the sim check | IE-SF50 86; SF50-FLT; SF50-PKG; V-2 A-7, A-8 | Unverified (readout); 1 RUN / 0 STOP: verified by scmon capture 2026-11-16 |
| systems 2,3 `STARTER` | `(A:GENERAL ENG STARTER:1, Bool)`, Mappings `0=OFF:1=ON` | Bool | none | - | SDK-ENGV | Unverified |
| systems 2,4 `FUEL CTL` | `B:sf50_fuel_control_knob`, Format `1.0` | B-var value (positions unknown) | none (guard) | Mappings from the sim check | IE-SF50 114; SF50-FLT; SF50-PKG; V-2 A-7, A-8 | Unverified; 0, 1 and 2 (1 at the start) seen in the scmon capture 2026-11-16; which position each value is: open |
| iceenv 1,2 `ENG IPS` | `B:sf50_deice_engine` | B-var value (0/1 expected) | G1 `B:sf50_deice_engine` | readout of the B-var, Mappings `0=OFF:1=ON` (A-6); readout of `ENG ANTI ICE:1` (A-2) | IE-SF50 74; SF50-PKG; SF50-FLT; PD-LONG; V-2 A-6 | Unverified (key press); 0 off / 1 on and `ENG ANTI ICE:1` following it: verified by scmon capture 2026-11-16 |
| iceenv 1,3 `WING/STAB` | `B:sf50_deice_wingstab` | B-var value (0/1 expected) | G1 `B:sf50_deice_wingstab` | as main 4,7 | IE-SF50 78; SF50-PKG; SF50-FLT; PD-LONG; V-2 A-6 | Unverified (key press); 0 off / 1 on and `STRUCTURAL DEICE SWITCH` following it: verified by scmon capture 2026-11-16 |
| iceenv 1,4 `WSHLD` | `B:sf50_deice_windshield` | B-var value (0/1 expected) | G1 `B:sf50_deice_windshield` | readout of the B-var (A-6); readout of `WINDSHIELD DEICE SWITCH` (A-2) | IE-SF50 76; SF50-PKG; PD-LONG; V-2 A-6 | Unverified (key press); 0 off / 1 on and `WINDSHIELD DEICE SWITCH` following it: verified by scmon capture 2026-11-16 |
| iceenv 1,5 `WSHLD HI` | `B:sf50_deice_windshield_high` | B-var value (0/1 expected) | `B:sf50_deice_windshield_high`, On `1` / Off `0` | Empty | IE-SF50 77; SF50-PKG; README 2.1.1 | Unverified (key press); 0 / 1: verified by scmon capture 2026-11-16 |
| iceenv 1,7 `WING LT` | `B:lighting_wing_1` | B-var value (0/1 expected) | `B:lighting_wing_1`, On `1` / Off `0` | Empty | IE-SF50 41; SF50-FLT; README 2.1.1; V-2 A-21 | Unverified |
| iceenv 2,2 `ENG AI` | `(A:ENG ANTI ICE:1, Bool)`, Mappings `0=OFF:1=ON` | Bool | none | - | SDK-ENGV | Unverified (key); follows `B:sf50_deice_engine`: verified by scmon capture 2026-11-16 |
| iceenv 2,3 `STRUCT` | `(A:STRUCTURAL DEICE SWITCH, Bool)`, Mappings `0=OFF:1=ON` | Bool | none | - | SDK-SYSV | Unverified (key); follows `B:sf50_deice_wingstab`: verified by scmon capture 2026-11-16 |
| iceenv 2,4 `WSHLD SW` | `(A:WINDSHIELD DEICE SWITCH, Bool)`, Mappings `0=OFF:1=ON` | Bool | none | - | SDK-SYSV | Unverified (key); follows `B:sf50_deice_windshield`: verified by scmon capture 2026-11-16 |
| iceenv 3,2 `OXYGEN` | `B:sf50_pressurization_oxygen_master` | B-var value (0/1 expected) | G1 `B:sf50_pressurization_oxygen_master` | readout of the B-var, Mappings `0=OFF:1=ON` (A-6); Empty (A-2) | IE-SF50 133; SF50-PKG; SF50-FLT; PD-LONG; V-2 A-6 | Unverified (key press); 0 / 1: verified by scmon capture 2026-11-16 |
| iceenv 3,3 `BLEED` | `B:sf50_pressurization_switch_air_bleed`, Mappings `0=FRESH:1=BLEED` | B-var value (working value) | none (guard) | Mappings from the sim check | IE-SF50 134; SF50-FLT; SF50-PKG; V-2 A-7 | Unverified; 0 / 1 (1 at the start) seen in the scmon capture 2026-11-16; which value is FRESH or BLEED: open |
| iceenv 3,4 `ECS DIS` | `B:sf50_cabin_ecs_disable`, Format `1.0` | B-var value | none (guard) | Mappings from the sim check | IE-SF50 66; SF50-PKG; V-2 A-7 | Unverified (no change seen in two scmon runs, 2026-11-16) |
| iceenv 3,5 `DEFOG` | `B:sf50_cabin_ecs_defog` | B-var value (0/1 expected) | `B:sf50_cabin_ecs_defog`, On `1` / Off `0` | Empty | IE-SF50 65; SF50-PKG; README 2.1.1 | Unverified |
| iceenv 3,6 `AFT CTL` | `B:sf50_cabin_ecs_aft_control` | B-var value (0/1 expected) | `B:sf50_cabin_ecs_aft_control`, On `1` / Off `0` | Empty | IE-SF50 64; SF50-PKG; README 2.1.1 | Unverified |
| iceenv 3,7 `TEMP BKUP` | `B:sf50_cabin_ecs_temp_backup` | B-var value (0/1 expected) | `B:sf50_cabin_ecs_temp_backup`, On `1` / Off `0` | Empty | IE-SF50 69; SF50-PKG; README 2.1.1 | Unverified |
| iceenv 4,2 `TEMP FWD` | `B:sf50_cabin_ecs_temp_knob_forward`, Format `1.0` | B-var value (flight file default 50) | none (knob steps unknown, V-3) | - | IE-SF50 71; SF50-FLT | Unverified |
| iceenv 4,3 `TEMP AFT` | `B:sf50_cabin_ecs_temp_knob_aft`, Format `1.0` | B-var value | none (V-3) | - | IE-SF50 70; SF50-FLT | Unverified |
| iceenv 4,4 `FAN FWD` | `B:sf50_cabin_ecs_fan_knob_forward`, Format `1.0` | B-var value | none (V-3) | - | IE-SF50 68 | Unverified |
| iceenv 4,5 `FAN AFT` | `B:sf50_cabin_ecs_fan_knob_aft`, Format `1.0` | B-var value | none (V-3) | - | IE-SF50 67 | Unverified |
