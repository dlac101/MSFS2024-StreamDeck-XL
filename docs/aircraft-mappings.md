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

## FlyByWire A32NX (Phase 4 airliner)

Installed with the FlyByWire Installer (`A:\FS2024 Stuff\FlyByWire-Installer-x64.exe`).
Mostly L-Vars and custom events rather than standard SimVars. Use FlyByWire's own
flight-deck API docs and HubHop as sources, and record each one here.

Aircraft string: _TBD_

| Function | Read (variable) | Units | Write (command) | Verified |
|---|---|---|---|---|
