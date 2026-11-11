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

## FlyByWire A32NX (Phase 4 airliner)

Installed with the FlyByWire Installer (`A:\FS2024 Stuff\FlyByWire-Installer-x64.exe`).
Mostly L-Vars and custom events rather than standard SimVars. Use FlyByWire's own
flight-deck API docs and HubHop as sources, and record each one here.

Aircraft string: _TBD_

| Function | Read (variable) | Units | Write (command) | Verified |
|---|---|---|---|---|
