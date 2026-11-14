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
| Elevator trim up (trim 2,2) | none (readouts trim 3,2 and 3,3) | | `K:ELEV_TRIM_UP` | input event `B:handling_elevatortrim_wheel` (values unknown, not used) | SDK-FCE; IE 182 | Unverified |
| Elevator trim down (trim 4,2) | none (readouts trim 3,2 and 3,3) | | `K:ELEV_TRIM_DN` | as trim up | SDK-FCE; IE 182 | Unverified |
| Elevator trim position, percent (trim 3,2) | `(A:ELEVATOR TRIM PCT EX2, percent)` | percent, -100 (down limit) to 100 (up limit), 0 = 0° | (read only here; the SimVar is settable, SDK-CTLV) | `(A:ELEVATOR TRIM PCT, percent)` (legacy SimVar) | SDK-CTLV; SDK-UNITS | Unverified |
| Elevator trim deflection (trim 3,3) | `(A:ELEVATOR TRIM POSITION, degrees)` | degrees | (read only here; the SimVar is settable, SDK-CTLV) | none | SDK-CTLV; SDK-UNITS | Unverified |
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

The view events are aircraft-independent (they act on the sim's camera, not the C172); they are listed
here because every event the project uses goes in this file. Sources as above, plus:
- SDK-VCE: key-events/view-and-camera-events/
- SDK-CAMV: simvars/camera-variables/

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
PilotsDeck source (`SimCommand.cs` LUAFUNC = 14; an A-Var with unit `String` is read as text), see
phase2-com1-pad.md.

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
