# VisionJet SF50 profile (MSFS 2024 default Cirrus Vision SF50)

**Status: generated, not yet sim-tested.** The profile `MSFS2024 VisionJet` is built by the generator, but
nothing on it has been tried in the app or the sim yet. Every name below is recorded as "Unverified" in
[aircraft-mappings.md](aircraft-mappings.md) ("Cirrus Vision SF50 (MSFS 2024 default, V-1)") until the checks
in [tests/manual-checklist.md](../tests/manual-checklist.md), section "VisionJet SF50 profile (V-1)", pass.

Goal: a first useful profile for the Cirrus Vision SF50 (VisionJet) that comes with MSFS 2024 (folder
`microsoft_sf50`, presets `sf50_executive`, `sf50_family` and `sf50_complete`; not FlightFX's add-on). It uses
the C172 G1000 profile's grid and folder positions where the function applies ([navigation.md](navigation.md),
"Pages": "a later aircraft uses this grid and these folder positions where the function applies"): 12 pages,
146 keys. Every readout and lit key shows the sim's own value; no key assumes its press worked.

**Built with the SF50's input event list (track A).** The user loaded the SF50 with PilotsDeck running on
2026-11-16, and PilotsDeck wrote its `InputEvents.txt`; the copy is
[reference/InputEvents-SF50.txt](reference/InputEvents-SF50.txt) (141 input events, cited "IE-SF50 n",
line n). The battery, nav, strobe, landing light and pitot heat keys and the autopilot VNV command use the
list's B-vars (rule: "Which route each key uses"). The list has no beacon light (BCN stays empty) and no
taxi light (TAXI keeps the standard K-event).

Research and the candidate names: [visionjet-g2-research.md](visionjet-g2-research.md). The data file is
`tools/profilegen/visionjet-sf50.json`; the key tables below are the reference, and
`python tools/profilegen/check.py tools/profilegen/visionjet-sf50.json` compares the profile with them key by
key. No Lua script is new: the sim rate, COM pad and transponder pages call the C172's scripts as they are.

Nothing in this profile uses keyboard bindings, vJoy or anything tied to a controller: the keys send the
aircraft's own input events (B-vars), standard SimConnect events, G3000 H-events (through the MobiFlight WASM
module) and Lua functions, and read SimVars, L-Vars and B-vars, so they work the same with the Xbox Elite
controller and the T.16000M + TWCS.

## What the SF50's files and the plugin log show

- **Plugin log** (PD-LOG): PilotsDeck 0.9.7 saw the SF50 on 2026-11-15 and 2026-11-16 with three presets; the
  aircraft string is the path of the preset's `aircraft.cfg` in the package `fs24-microsoft-aircraft-sf50`:
  `...\simobjects\airplanes\microsoft_sf50\presets\microsoft\<preset>\config\aircraft.cfg`. Its
  `ProfileSwitcherManager` line said "Searching 0 valid Profiles": no profile was mapped to it yet.
- **Input event list** (IE-SF50): 141 input events, among them the G3000 touch controllers
  (`as3000_tsc_1..3_*`), `sf50_electrical_battery_1_switch` and `_2_switch`, `sf50_lighting_*`,
  `lighting_strobe_1`, `deice_pitot_1`, `sf50_autopilot_*`, `sf50_deice_*`, `sf50_engine_*`, `sf50_caps_*` and
  `sf50_safe_return_*`. No `lighting_beacon_*` and no `lighting_taxi_*` name.
- **SF50 package** (SF50-PKG, read by search only): the panel is the Working Title G3000 v2 (one PFD with
  index 1, one MFD, three GTC touch controllers); the flight files hold two batteries, the generators and
  external power; the tooltip texts name FMS and MAN speed mode, ice protection (NORM, HIGH, MAX), engine
  start and stop, CAPS and Safe Return controls. The model behaviours themselves are not readable: only
  `InputEvents.txt` gives B-var names.

## Where the pages sit

The main page has no back key. Every child page has its back key at 1,1; at most two folder levels
([navigation.md](navigation.md), "MSFS2024 VisionJet pages").

| Opened by | Page | Level | Holds |
|---|---|---|---|
| main 1,7 `TRIM` | trim | 1 | the C172's trim page as it was when this profile was built (elevator trim), without the C172's later aileron and rudder trim keys |
| main 1,8 `VIEWS` | views | 1 | the C172's views page as it is |
| main 3,7 `SIM RATE` | simrate | 1 | the C172's sim rate page as it is (`XL24-SIMRATE.lua`) |
| main 3,8 `CHECKLIST` | checklist | 1 | the back key only (Phase 5) |
| main 4,8 `MORE` | more | 1 | six folder keys |
| more 1,4 `V-SPEEDS` | vspeeds | 2 | the C172's V-speeds page as it is |
| more 1,5 `COM PAD` | compad | 2 | the C172's COM1 pad as it is (`XL24-COMPAD.lua`) |
| more 1,6 `AUTOPILOT` | autopilot | 2 | the C172's autopilot page with the SF50's changes (G3000, autothrottle) |
| more 1,7 `XPDR` | xpdr | 2 | the C172's transponder page as it is (`XL24-XPDRPAD.lua`) |
| more 1,8 `RADIOS` | radios | 2 | the C172's radios page as it is |
| more 2,3 `ENGINE` | engine | 2 | engine and fuel readouts (new) |

MORE 1,2 and 1,3 (the C172's PFD and MFD bezel pages) and 2,2 (SYSTEMS) stay empty for V-2 ("Not on these
pages").

## Layouts

Positions are **row,column**, 1-based, row 1 at the top. `>` marks a folder key, `-` an empty position.

**main**

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | BAT | N1 | - | PARK | GEAR | FLAPS | TRIM > | VIEWS > |
| **Row 2** | AP | HDG | ALT | VS | NAV | APR | FLC | FD |
| **Row 3** | COM1 | XPDR | ATC | MAP | CDI | BARO | SIM RATE > | CHECKLIST > |
| **Row 4** | NAV LT | - | STRB | LDG | TAXI | PITOT | - | MORE > |

**more**

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | - | - | V-SPEEDS > | COM PAD > | AUTOPILOT > | XPDR > | RADIOS > |
| **Row 2** | - | - | ENGINE > | - | - | - | - | - |

Rows 3 and 4 are empty.

**autopilot**

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | AP | FD | HDG | NAV | APR | - | VNV |
| **Row 2** | ALT | HDG+ | CRS+ | ALT+ | VS+ | SPD+ | - | A/T |
| **Row 3** | VS | HDG BUG | CRS1 | ALT SEL | VS TGT | FLC SPD | LVL | TOGA |
| **Row 4** | FLC | HDG- | CRS- | ALT- | VS- | SPD- | - | A/T MGD |

**engine**

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | N1 | N2 | ITT | FF PPH | - | - | - |
| **Row 2** | - | ENG RUN | IGN | - | - | - | - | - |
| **Row 3** | - | FUEL L | FUEL R | FUEL TOT | - | - | - | - |

Row 4 is empty.

The pages trim, views, simrate, vspeeds, compad, xpdr and radios have the C172's layouts:
[phase2-trim-views.md](phase2-trim-views.md), [phase2-sim-rate.md](phase2-sim-rate.md),
[phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md), [phase2-com1-pad.md](phase2-com1-pad.md),
[phase3-transponder.md](phase3-transponder.md) and [phase3-radios.md](phase3-radios.md).

## Key table

Columns as in [phase2-main-page.md](phase2-main-page.md), "Key table". Tags in brackets are under "Sources".
Rows copied from a C172 doc keep its text and tags; an `A-n` in such a row is that doc's own ASSUMPTION, and
this profile's are written `V-1 A-n`.

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | `BAT` | Dynamic Button | T1 | `B:sf50_electrical_battery_1_switch`, On `1` / Off `0` [IE-SF50 80; README 2.1.1; V-1 A-5] | `B:sf50_electrical_battery_1_switch` [IE-SF50 80] | On/Off image, Special State |
| 1,2 | `N1` | Display Value | T3 | none | `(A:TURB ENG N1:1, Percent)` [SDK-ENGV] | Format `1.1` |
| 1,3 | | Empty | | | | Fuel pump: no SF50 source names one |
| 1,4 | `PARK` | Dynamic Button | T2 (copy of Phase 1 key) | `K:PARKING_BRAKES` [AM] | `(A:BRAKE PARKING POSITION, Bool)` [AM, SDK-GEARV] | On/Off image |
| 1,5 | `GEAR` | Display Value | T3 | none | `(A:GEAR HANDLE POSITION, Bool)` [SDK-GEARV] | Mappings `0=UP:1=DOWN` |
| 1,6 | `FLAPS` | Display Value | T3 | Main `K:FLAPS_INCR`, Second (long press) `K:FLAPS_DECR` [SDK-FCE, README 2.1] | `(A:FLAPS HANDLE INDEX, number)` [SDK-CTLV] | Format `1.0` |
| 1,7 | `TRIM` | Folder | (Stream Deck) | Opens the child page **trim** | none | Folder; the page's keys: "Key table: trim" below |
| 1,8 | `VIEWS` | Folder | (Stream Deck) | Opens the child page **views** | none | Folder; the page's keys: "Key table: views" below |
| 2,1 | `AP` | Dynamic Button | T2 (template) | `K:AP_MASTER` [AM] | `(A:AUTOPILOT MASTER, Bool)` [AM] | On/Off image |
| 2,2 | `HDG` | Dynamic Button | T2 | `K:AP_HDG_HOLD` [SDK-APE] | `(A:AUTOPILOT HEADING LOCK, Bool)` [SDK-APV] | On/Off image |
| 2,3 | `ALT` | Dynamic Button | T2 | `K:AP_ALT_HOLD` [SDK-APE] | `(A:AUTOPILOT ALTITUDE LOCK, Bool)` [SDK-APV] | On/Off image |
| 2,4 | `VS` | Dynamic Button | T2 | `K:AP_VS_HOLD` [SDK-APE] | `(A:AUTOPILOT VERTICAL HOLD, Bool)` [SDK-APV] | On/Off image |
| 2,5 | `NAV` | Dynamic Button | T2 | `K:AP_NAV1_HOLD` [SDK-APE] | `(A:AUTOPILOT NAV1 LOCK, Bool)` [SDK-APV] | On/Off image |
| 2,6 | `APR` | Dynamic Button | T2 | `K:AP_APR_HOLD` [SDK-APE] | `(A:AUTOPILOT APPROACH HOLD, Bool)` [SDK-APV] | On/Off image |
| 2,7 | `FLC` | Dynamic Button | T2 | `K:FLIGHT_LEVEL_CHANGE` [SDK-APE] | `(A:AUTOPILOT FLIGHT LEVEL CHANGE, Bool)` [SDK-APV] | On/Off image |
| 2,8 | `FD` | Dynamic Button | T2 | `K:TOGGLE_FLIGHT_DIRECTOR` [SDK-APE] | `(A:AUTOPILOT FLIGHT DIRECTOR ACTIVE, Bool)` [SDK-APV] | On/Off image |
| 3,1 | `COM1` | COM Radio | T4 | `K:COM_STBY_RADIO_SWAP` [SDK-RADE] | Active `(A:COM ACTIVE FREQUENCY:1, MHz)`, Standby `(A:COM STANDBY FREQUENCY:1, MHz)` [SDK-RADV, SDK-UNITS] | Format `3` |
| 3,2 | `XPDR` | Display Value | T3 | none | `(A:TRANSPONDER CODE:1, Bco16)` [SDK-RADV] | Decode BCD, Format `4.0` |
| 3,3 | `ATC` | Simple Button | T5 | `K:SIMUI_WINDOW_HIDESHOW` [SDK-MISCE] | none (a sim window has no state) | fixed image |
| 3,4 | `MAP` | Simple Button | T5 | `K:FLIGHT_MAP` [SDK-MISCE] | none (a sim window has no state) | fixed image |
| 3,5 | `CDI` | Display Value | T3 | `K:TOGGLE_GPS_DRIVES_NAV1` [SDK-RADE] | `(A:GPS DRIVES NAV1, Bool)` [SDK-RADV] | Mappings `0=VLOC:1=GPS` |
| 3,6 | `BARO` | Display Value | T3 | `K:BAROMETRIC` [SDK-INSTE] | `(A:KOHLSMAN SETTING HG:1, inHg)` [SDK-SYSV] | Format `2.2` |
| 3,7 | `SIM RATE` | Folder | (Stream Deck) | Opens the child page **simrate** | none | Folder; the page's keys: "Key table: simrate" below |
| 3,8 | `CHECKLIST` | Folder | (Stream Deck) | Opens the child page **checklist** | none | Folder; the page holds only the back key (1,1) |
| 4,1 | `NAV LT` | Dynamic Button | T1 | `B:sf50_lighting_nav_lights_intercept`, On `1` / Off `0` [IE-SF50 130; README 2.1.1; V-1 A-5, A-15] | `B:sf50_lighting_nav_lights_intercept` [IE-SF50 130] | On/Off image, Special State |
| 4,2 | | Empty | | | | BCN: the SF50 input event list names no beacon light (V-1 A-5) |
| 4,3 | `STRB` | Dynamic Button | T1 | `B:lighting_strobe_1`, On `1` / Off `0` [IE-SF50 40; README 2.1.1; V-1 A-5] | `B:lighting_strobe_1` [IE-SF50 40] | On/Off image, Special State |
| 4,4 | `LDG` | Dynamic Button | T1 | `B:sf50_lighting_landing_lights`, On `1` / Off `0` [IE-SF50 129; README 2.1.1; V-1 A-5] | `B:sf50_lighting_landing_lights` [IE-SF50 129] | On/Off image, Special State |
| 4,5 | `TAXI` | Dynamic Button | T2 | `K:TOGGLE_TAXI_LIGHTS` [SDK-ELECE; no taxi B-var in IE-SF50, V-1 A-5, A-15] | `(A:LIGHT TAXI, Bool)` [SDK-SYSV] | On/Off image |
| 4,6 | `PITOT` | Dynamic Button | T1 | `B:deice_pitot_1`, On `1` / Off `0` [IE-SF50 31; README 2.1.1; V-1 A-5] | `B:deice_pitot_1` [IE-SF50 31] | On/Off image, Special State |
| 4,7 | | Empty | | | | Anti-ice (reserved): the SF50 ice protection waits for its input event list (V-2) |
| 4,8 | `MORE` | Folder | (Stream Deck) | Opens the child page **more** | none | Folder; the page's keys: "Key table: more" below |

## Key table: trim

The C172's trim page as it was when this profile was built (elevator trim up and down, the TRIM and TRIM DEG
readouts, the trim gauge), without the aileron and rudder trim keys the C172 page has had since; the rows
are those of the "Key table: trim" in [phase2-trim-views.md](phase2-trim-views.md) at that time.

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to the main page | none | Back key |
| 1,2 | | Empty | | | | |
| 1,3 | | Empty | | | | |
| 1,4 | | Empty | | | | |
| 1,5 | | Empty | | | | |
| 1,6 | | Empty | | | | |
| 1,7 | | Empty | | | | |
| 1,8 | | Empty | | | | |
| 2,1 | | Empty | | | | |
| 2,2 | `TRIM UP` | Simple Button | T5 | `K:ELEV_TRIM_UP` [SDK-FCE] | none (the readouts 3,2 and 3,3 show the result) | fixed image |
| 2,3 | | Empty | | | | |
| 2,4 | | Empty | | | | |
| 2,5 | | Empty | | | | |
| 2,6 | | Empty | | | | |
| 2,7 | | Empty | | | | |
| 2,8 | | Empty | | | | |
| 3,1 | | Empty | | | | |
| 3,2 | `TRIM` | Display Value | T3 | none | `(A:ELEVATOR TRIM PCT EX2, percent)` [SDK-CTLV, SDK-UNITS] | Format `1.1` |
| 3,3 | `TRIM DEG` | Display Value | T3 | none | `(A:ELEVATOR TRIM POSITION, degrees)` [SDK-CTLV, SDK-UNITS] | Format `1.1` |
| 3,4 | `TRIM` | Display Gauge | T9 | none | `(A:ELEVATOR TRIM PCT EX2, percent)` [SDK-CTLV, SDK-UNITS] | Format `1.0`; vertical bar, values up (Orientation Up, saved `-90`), `-100` to `100`, center line, pointer |
| 3,5 | | Empty | | | | |
| 3,6 | | Empty | | | | |
| 3,7 | | Empty | | | | |
| 3,8 | | Empty | | | | |
| 4,1 | | Empty | | | | |
| 4,2 | `TRIM DN` | Simple Button | T5 | `K:ELEV_TRIM_DN` [SDK-FCE] | none (the readouts 3,2 and 3,3 show the result) | fixed image |
| 4,3 | | Empty | | | | |
| 4,4 | | Empty | | | | |
| 4,5 | | Empty | | | | |
| 4,6 | | Empty | | | | |
| 4,7 | | Empty | | | | |
| 4,8 | | Empty | | | | |

## Key table: views

The C172's views page ([phase2-trim-views.md](phase2-trim-views.md)); rows as that doc's "Key table: views".

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to the main page | none | Back key |
| 1,2 | `COCKPIT` | Dynamic Button | T6 | `(A:CAMERA STATE, Enum)`, On `$=2` / Off `` [SDK-CAMV, README 2.1.1, 2.1.2] | `(A:CAMERA STATE, Enum)` [SDK-CAMV, SDK-UNITS] | On/Off image: On `2`, Off `3` |
| 1,3 | `EXTERNAL` | Dynamic Button | T6 | `(A:CAMERA STATE, Enum)`, On `$2,=3<` / Off `` [SDK-CAMV, README 2.1.1, 2.1.2] | `(A:CAMERA STATE, Enum)` [SDK-CAMV, SDK-UNITS] | On/Off image: On `3`, Off `2` |
| 1,4 | `CAMERA` | Display Value | T3 | none | `(A:CAMERA STATE, Enum)` [SDK-CAMV, SDK-UNITS] | Mappings `2=COCKPIT:3=CHASE:4=FIXED:5=ENV:7=SHOWCASE:8=DRONE` |
| 1,5 | `VIEW` | Display Value | T3 | none | `(A:CAMERA VIEW TYPE AND INDEX:0, Enum)` [SDK-CAMV, SDK-UNITS] | Mappings `0=OTHER:1=PILOT:2=INSTR:3=QUICK:4=QV EXT:5=VIEW` |
| 1,6 | `VIEW NO` | Display Value | T3 | none | `(A:CAMERA VIEW TYPE AND INDEX:1, number)` [SDK-CAMV, SDK-UNITS] | Format `1.0` |
| 1,7 | | Empty | | | | |
| 1,8 | | Empty | | | | |
| 2,1 | | Empty | | | | |
| 2,2 | | Empty | | | | |
| 2,3 | | Empty | | | | |
| 2,4 | | Empty | | | | |
| 2,5 | | Empty | | | | |
| 2,6 | | Empty | | | | |
| 2,7 | | Empty | | | | |
| 2,8 | | Empty | | | | |
| 3,1 | | Empty | | | | |
| 3,2 | | Empty | | | | |
| 3,3 | | Empty | | | | |
| 3,4 | | Empty | | | | |
| 3,5 | | Empty | | | | |
| 3,6 | | Empty | | | | |
| 3,7 | | Empty | | | | |
| 3,8 | | Empty | | | | |
| 4,1 | | Empty | | | | |
| 4,2 | | Empty | | | | |
| 4,3 | | Empty | | | | |
| 4,4 | | Empty | | | | |
| 4,5 | | Empty | | | | |
| 4,6 | | Empty | | | | |
| 4,7 | | Empty | | | | |
| 4,8 | | Empty | | | | |

## Key table: more

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to the main page | none | Back key |
| 1,2 | | Empty | | | | PFD softkeys: V-2 |
| 1,3 | | Empty | | | | MFD softkeys: V-2 |
| 1,4 | `V-SPEEDS` | Folder | (Stream Deck) | Opens the child page **vspeeds** | none | Folder; the page's keys: "Key table: vspeeds" below |
| 1,5 | `COM PAD` | Folder | (Stream Deck) | Opens the child page **compad** | none | Folder; the page's keys: "Key table: compad" below |
| 1,6 | `AUTOPILOT` | Folder | (Stream Deck) | Opens the child page **autopilot** | none | Folder; the page's keys: "Key table: autopilot" below |
| 1,7 | `XPDR` | Folder | (Stream Deck) | Opens the child page **xpdr** | none | Folder; the page's keys: "Key table: xpdr" below |
| 1,8 | `RADIOS` | Folder | (Stream Deck) | Opens the child page **radios** | none | Folder; the page's keys: "Key table: radios" below |
| 2,1 | | Empty | | | | |
| 2,2 | | Empty | | | | SYSTEMS: V-2 with the input event list |
| 2,3 | `ENGINE` | Folder | (Stream Deck) | Opens the child page **engine** | none | Folder; the page's keys: "Key table: engine" below |
| 2,4 | | Empty | | | | |
| 2,5 | | Empty | | | | |
| 2,6 | | Empty | | | | |
| 2,7 | | Empty | | | | |
| 2,8 | | Empty | | | | |
| 3,1 | | Empty | | | | |
| 3,2 | | Empty | | | | |
| 3,3 | | Empty | | | | |
| 3,4 | | Empty | | | | |
| 3,5 | | Empty | | | | |
| 3,6 | | Empty | | | | |
| 3,7 | | Empty | | | | |
| 3,8 | | Empty | | | | |
| 4,1 | | Empty | | | | |
| 4,2 | | Empty | | | | |
| 4,3 | | Empty | | | | |
| 4,4 | | Empty | | | | |
| 4,5 | | Empty | | | | |
| 4,6 | | Empty | | | | |
| 4,7 | | Empty | | | | |
| 4,8 | | Empty | | | | |

## Key table: vspeeds

The C172's V-speeds page ([phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md)); rows as that doc's "Key table:
vspeeds".

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to the MORE page | none | Back key |
| 1,2 | `VS0` | Display Value | T3 | none | `(A:DESIGN SPEED VS0, knots)` [SDK-FMV, SDK-UNITS] | Format `1.0` |
| 1,3 | `VS1` | Display Value | T3 | none | `(A:DESIGN SPEED VS1, knots)` [SDK-FMV, SDK-UNITS] | Format `1.0` |
| 1,4 | `VR` | Display Value | T3 | none | `(A:DESIGN SPEED MIN ROTATION, knots)` [SDK-FMV, SDK-UNITS] | Format `1.0` |
| 1,5 | | Empty | | | | Vx: no SimVar in the MSFS 2024 SDK |
| 1,6 | `CLIMB` | Display Value | T3 | none | `(A:DESIGN SPEED CLIMB, knots)` [SDK-FMV, SDK-UNITS] | Format `1.0` |
| 1,7 | | Empty | | | | |
| 1,8 | | Empty | | | | |
| 2,1 | | Empty | | | | |
| 2,2 | `CRUISE` | Display Value | T3 | none | `(A:DESIGN SPEED VC, knots)` [SDK-FMV, SDK-UNITS] | Format `1.0` |
| 2,3 | | Empty | | | | Vno: no SimVar in the MSFS 2024 SDK |
| 2,4 | `VNE` | Display Value | T3 | none | `(A:REFERENCE SPEED MAX IAS, knots)` [SDK-FMV, SDK-UNITS] | Format `1.0` |
| 2,5 | `VFE` | Display Value | T3 | none | `(A:FLAPS CURRENT SPEED LIMITATION, knots)` [SDK-CTLV, SDK-UNITS] | Format `1.0` |
| 2,6 | | Empty | | | | |
| 2,7 | | Empty | | | | |
| 2,8 | | Empty | | | | |
| 3,1 | | Empty | | | | |
| 3,2 | | Empty | | | | |
| 3,3 | | Empty | | | | |
| 3,4 | | Empty | | | | |
| 3,5 | | Empty | | | | |
| 3,6 | | Empty | | | | |
| 3,7 | | Empty | | | | |
| 3,8 | | Empty | | | | |
| 4,1 | | Empty | | | | |
| 4,2 | | Empty | | | | |
| 4,3 | | Empty | | | | |
| 4,4 | | Empty | | | | |
| 4,5 | | Empty | | | | |
| 4,6 | | Empty | | | | |
| 4,7 | | Empty | | | | |
| 4,8 | | Empty | | | | |

## Key table: simrate

The C172's sim rate page ([phase2-sim-rate.md](phase2-sim-rate.md)); rows as that doc's "Key table: simrate".

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to the main page | none | Back key |
| 1,2 | `1X` | Dynamic Button | T2 | `lua:XL24-SIMRATE:SET(1)` (steps `K:SIM_RATE_INCR` / `K:SIM_RATE_DECR`) [README 2.1.1 LUAFUNC, 3.5.1; SDK-MISCE; LR153-C4] | `(A:SIMULATION RATE, number)` [SDK-ENVV, PD-SRC] | On/Off image: On `1`, Off `2` |
| 1,3 | `SLOWER` | Simple Button | T5 | `K:SIM_RATE_DECR` [SDK-MISCE] | none | fixed image |
| 1,4 | `RATE` | Display Value | T3 | Main `K:SIM_RATE_INCR`, Second (long press) `K:SIM_RATE_DECR` [SDK-MISCE, README 2.1] | `(A:SIMULATION RATE, number)` [SDK-ENVV, PD-SRC] | Format `1.2` |
| 1,5 | `FASTER` | Simple Button | T5 | `K:SIM_RATE_INCR` [SDK-MISCE] | none | fixed image |
| 1,6 | | Empty | | | | |
| 1,7 | | Empty | | | | |
| 1,8 | | Empty | | | | |
| 2,1 | | Empty | | | | |
| 2,2 | | Empty | | | | |
| 2,3 | | Empty | | | | |
| 2,4 | | Empty | | | | |
| 2,5 | | Empty | | | | |
| 2,6 | | Empty | | | | |
| 2,7 | | Empty | | | | |
| 2,8 | | Empty | | | | |
| 3,1 | | Empty | | | | |
| 3,2 | | Empty | | | | |
| 3,3 | | Empty | | | | |
| 3,4 | | Empty | | | | |
| 3,5 | | Empty | | | | |
| 3,6 | | Empty | | | | |
| 3,7 | | Empty | | | | |
| 3,8 | | Empty | | | | |
| 4,1 | | Empty | | | | |
| 4,2 | | Empty | | | | |
| 4,3 | | Empty | | | | |
| 4,4 | | Empty | | | | |
| 4,5 | | Empty | | | | |
| 4,6 | | Empty | | | | |
| 4,7 | | Empty | | | | |
| 4,8 | | Empty | | | | |

## Key table: compad

The C172's COM1 pad ([phase2-com1-pad.md](phase2-com1-pad.md)); rows as that doc's "Key table: compad".

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to MORE | none | Back key |
| 1,2 | `COM1` | COM Radio | T4 | `K:COM_STBY_RADIO_SWAP` [SDK-RADE] | Active `(A:COM ACTIVE FREQUENCY:1, MHz)`, Standby `(A:COM STANDBY FREQUENCY:1, MHz)` [SDK-RADV] | Format `3` |
| 1,3 | `ENTRY` | Display Value | T3 | none | `X:XL24_COMPAD_ENTRY` [README 2.1.1 INTERNAL; written by the script] | the typed digits as text, e.g. `118.5__`; Format empty |
| 1,4 | | Empty | | | | |
| 1,5 | | Empty | | | | |
| 1,6 | `7` | Simple Button | T8 | `lua:XL24-COMPAD:DIGIT(7)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 1,7 | `8` | Simple Button | T8 | `lua:XL24-COMPAD:DIGIT(8)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 1,8 | `9` | Simple Button | T8 | `lua:XL24-COMPAD:DIGIT(9)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 2,1 | | Empty | | | | |
| 2,2 | `STBY ID` | Display Value | T3 | none | `(A:COM STANDBY FREQ IDENT:1, String)` [SDK-RADV; PD-SRC string A-Var] | the station ident as text; Format empty |
| 2,3 | | Empty | | | | |
| 2,4 | | Empty | | | | |
| 2,5 | | Empty | | | | |
| 2,6 | `4` | Simple Button | T8 | `lua:XL24-COMPAD:DIGIT(4)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 2,7 | `5` | Simple Button | T8 | `lua:XL24-COMPAD:DIGIT(5)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 2,8 | `6` | Simple Button | T8 | `lua:XL24-COMPAD:DIGIT(6)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 3,1 | | Empty | | | | |
| 3,2 | | Empty | | | | |
| 3,3 | | Empty | | | | |
| 3,4 | | Empty | | | | |
| 3,5 | | Empty | | | | |
| 3,6 | `1` | Simple Button | T8 | `lua:XL24-COMPAD:DIGIT(1)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 3,7 | `2` | Simple Button | T8 | `lua:XL24-COMPAD:DIGIT(2)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 3,8 | `3` | Simple Button | T8 | `lua:XL24-COMPAD:DIGIT(3)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 4,1 | | Empty | | | | |
| 4,2 | | Empty | | | | |
| 4,3 | | Empty | | | | |
| 4,4 | | Empty | | | | |
| 4,5 | | Empty | | | | |
| 4,6 | `CLR` | Simple Button | T8 | Main `lua:XL24-COMPAD:BACK`, Second (long press) `lua:XL24-COMPAD:CLEAR` [README 2.1.1 LUAFUNC, 2.1] | none | fixed image |
| 4,7 | `0` | Simple Button | T8 | `lua:XL24-COMPAD:DIGIT(0)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 4,8 | `ENT` | Simple Button | T8 | Main `lua:XL24-COMPAD:ENTER`, Second (long press) `lua:XL24-COMPAD:ENTER_SWAP` [README 2.1.1 LUAFUNC, 2.1] | none (COM1 at 1,2 shows the result) | fixed image |

## Key table: autopilot

The C172's autopilot page ([phase3-autopilot.md](phase3-autopilot.md)) with the SF50's changes at 1,7, 1,8,
2,3, 2,7, 2,8, 3,2, 3,3, 3,7, 3,8, 4,3 and 4,8; the other rows as that doc's "Key table: autopilot".

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to the MORE page | none | Back key |
| 1,2 | `AP` | Dynamic Button | T2 | `K:AP_MASTER` [SDK-APE; AM] | `(A:AUTOPILOT MASTER, Bool)` [SDK-APV; AM] | On/Off image |
| 1,3 | `FD` | Dynamic Button | T2 | `K:TOGGLE_FLIGHT_DIRECTOR` [SDK-APE; SDK-APT] | `(A:AUTOPILOT FLIGHT DIRECTOR ACTIVE, Bool)` [SDK-APV] | On/Off image |
| 1,4 | `HDG` | Dynamic Button | T2 | `K:AP_HDG_HOLD` [SDK-APE] | `(A:AUTOPILOT HEADING LOCK, Bool)` [SDK-APV] | On/Off image |
| 1,5 | `NAV` | Dynamic Button | T2 | `K:AP_NAV1_HOLD` [SDK-APE; SDK-APT] | `(A:AUTOPILOT NAV1 LOCK, Bool)` [SDK-APV] | On/Off image |
| 1,6 | `APR` | Dynamic Button | T2 | `K:AP_APR_HOLD` [SDK-APE; SDK-APT] | `(A:AUTOPILOT APPROACH HOLD, Bool)` [SDK-APV] | On/Off image |
| 1,7 | | Empty | | | | BC: no SF50 source gives a back-course key (V-2) |
| 1,8 | `VNV` | Dynamic Button | T1 | `B:sf50_autopilot_vnav_mode`, On `1` / Off `0` [IE-SF50 62; README 2.1.1; V-1 A-5] | `L:XMLVAR_VNAVButtonValue` [HH-MS; SDK-APT] | On/Off image, Special State |
| 2,1 | `ALT` | Dynamic Button | T2 | `K:AP_ALT_HOLD` [SDK-APE; SDK-APT] | `(A:AUTOPILOT ALTITUDE LOCK, Bool)` [SDK-APV] | On/Off image |
| 2,2 | `HDG+` | Simple Button | T5 | `K:HEADING_BUG_INC` [SDK-APE] | none | fixed image |
| 2,3 | `CRS+` | Simple Button | T5 | Main `H:AS3000_PFD_1_CRS_INC` [WT-G3000H; SF50-PKG; weak, V-1 A-15], Second (long press) `K:VOR1_OBI_FAST_INC` [SDK-RADE; README 2.1] | none | fixed image |
| 2,4 | `ALT+` | Simple Button | T5 | Main `K:AP_ALT_VAR_INC` [SDK-APE], Second (long press) `K:AP_ALT_VAR_INC:1000` [SDK-APE; SDK-AS1000; README 2.1.1, 2.1; A-4] | none | fixed image |
| 2,5 | `VS+` | Simple Button | T5 | `K:AP_VS_VAR_INC` [SDK-APE] | none | fixed image |
| 2,6 | `SPD+` | Simple Button | T5 | `K:AP_SPD_VAR_INC` [SDK-APE] | none | fixed image |
| 2,7 | | Empty | | | | YD: no SF50 source gives a yaw damper key (V-2) |
| 2,8 | `A/T` | Dynamic Button | T2 | `K:AUTO_THROTTLE_ARM` [SDK-APE; FORUM-24; V-1 A-15] | `(A:AUTOPILOT THROTTLE ARM, Bool)` [SDK-APV] | On/Off image |
| 3,1 | `VS` | Dynamic Button | T2 | `K:AP_VS_HOLD` [SDK-APE] | `(A:AUTOPILOT VERTICAL HOLD, Bool)` [SDK-APV] | On/Off image |
| 3,2 | `HDG BUG` | Display Value | T3 | `H:Garmin_AP_HDG_Sync` [WT-G3000H; weak, V-1 A-15] | `(A:AUTOPILOT HEADING LOCK DIR, Degrees)` [SDK-APV] | Format `3.0:%s°` |
| 3,3 | `CRS1` | Display Value | T3 | `H:AS3000_PFD_1_CRS_PUSH` [WT-G3000H; SF50-PKG; weak, V-1 A-15] | `(A:NAV OBS:1, Degrees)` [SDK-RADV] | Format `3.0:%s°` |
| 3,4 | `ALT SEL` | Display Value | T3 | none | `(A:AUTOPILOT ALTITUDE LOCK VAR, Feet)` [SDK-APV; A-5] | Format `1.0` |
| 3,5 | `VS TGT` | Display Value | T3 | none | `(A:AUTOPILOT VERTICAL HOLD VAR, Feet/minute)` [SDK-APV] | Format `1.0` |
| 3,6 | `FLC SPD` | Display Value | T3 | none | `(A:AUTOPILOT AIRSPEED HOLD VAR, Knots)` [SDK-APV] | Format `1.0` |
| 3,7 | `LVL` | Dynamic Button | T2 | `K:AP_WING_LEVELER` [SDK-APE; V-1 A-15] | `(A:AUTOPILOT WING LEVELER, Bool)` [SDK-APV] | On/Off image |
| 3,8 | `TOGA` | Display Value | T3 | none | `L:WT_TOGA_ACTIVE` [HH-MS; weak, V-1 A-15] | Mappings `0=OFF:1=TO/GA` |
| 4,1 | `FLC` | Dynamic Button | T2 | `K:FLIGHT_LEVEL_CHANGE` [SDK-APE; SDK-APT; A-9] | `(A:AUTOPILOT FLIGHT LEVEL CHANGE, Bool)` [SDK-APV] | On/Off image |
| 4,2 | `HDG-` | Simple Button | T5 | `K:HEADING_BUG_DEC` [SDK-APE] | none | fixed image |
| 4,3 | `CRS-` | Simple Button | T5 | Main `H:AS3000_PFD_1_CRS_DEC` [WT-G3000H; SF50-PKG; weak, V-1 A-15], Second (long press) `K:VOR1_OBI_FAST_DEC` [SDK-RADE; README 2.1] | none | fixed image |
| 4,4 | `ALT-` | Simple Button | T5 | Main `K:AP_ALT_VAR_DEC` [SDK-APE], Second (long press) `K:AP_ALT_VAR_DEC:1000` [SDK-APE; SDK-AS1000; README 2.1.1, 2.1; A-4] | none | fixed image |
| 4,5 | `VS-` | Simple Button | T5 | `K:AP_VS_VAR_DEC` [SDK-APE] | none | fixed image |
| 4,6 | `SPD-` | Simple Button | T5 | `K:AP_SPD_VAR_DEC` [SDK-APE] | none | fixed image |
| 4,7 | | Empty | | | | |
| 4,8 | `A/T MGD` | Display Value | T3 | none | `(A:AUTOPILOT MANAGED THROTTLE ACTIVE, Bool)` [SDK-APV] | Mappings `0=OFF:1=ON` |

## Key table: xpdr

The C172's transponder page ([phase3-transponder.md](phase3-transponder.md)); rows as that doc's "Key table:
xpdr".

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to MORE | none | Back key |
| 1,2 | `XPDR` | Display Value | T3 | none | `(A:TRANSPONDER CODE:1, Bco16)` [SDK-RADV] | Decode BCD, Format `4.0` |
| 1,3 | `ENTRY` | Display Value | T3 | none | `X:XL24_XPDRPAD_ENTRY` [README 2.1.1 INTERNAL; written by the script] | the typed digits as text, e.g. `12__`; Format empty |
| 1,4 | `MODE` | Display Value | T3 | none | `(A:TRANSPONDER STATE:1, Enum)` [SDK-RADV] | Mappings `0=OFF:1=STBY:2=TEST:3=ON:4=ALT:5=GND` |
| 1,5 | | Empty | | | | |
| 1,6 | `7` | Simple Button | T8 | `lua:XL24-XPDRPAD:DIGIT(7)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 1,7 | | Empty | | | | no key 8 (codes use 0-7) |
| 1,8 | | Empty | | | | no key 9 (codes use 0-7) |
| 2,1 | | Empty | | | | |
| 2,2 | `STBY` | Dynamic Button | T6 | `(A:TRANSPONDER STATE:1, Enum)`, On `$=1` / Off `` [SDK-RADV, README 2.1.1, 2.1.2] | `(A:TRANSPONDER STATE:1, Enum)` [SDK-RADV] | On/Off image: On `1`, Off `4` |
| 2,3 | `ON` | Dynamic Button | T6 | `(A:TRANSPONDER STATE:1, Enum)`, On `$=3` / Off `` [SDK-RADV, README 2.1.1, 2.1.2] | `(A:TRANSPONDER STATE:1, Enum)` [SDK-RADV] | On/Off image: On `3`, Off `1` |
| 2,4 | `ALT` | Dynamic Button | T6 | `(A:TRANSPONDER STATE:1, Enum)`, On `$=4` / Off `` [SDK-RADV, README 2.1.1, 2.1.2] | `(A:TRANSPONDER STATE:1, Enum)` [SDK-RADV] | On/Off image: On `4`, Off `1` |
| 2,5 | | Empty | | | | |
| 2,6 | `4` | Simple Button | T8 | `lua:XL24-XPDRPAD:DIGIT(4)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 2,7 | `5` | Simple Button | T8 | `lua:XL24-XPDRPAD:DIGIT(5)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 2,8 | `6` | Simple Button | T8 | `lua:XL24-XPDRPAD:DIGIT(6)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 3,1 | | Empty | | | | |
| 3,2 | `IDENT` | Dynamic Button | T2 | `K:XPNDR_IDENT_ON` [SDK-RADE] | `(A:TRANSPONDER IDENT:1, Bool)` [SDK-RADV] | On/Off image |
| 3,3 | `VFR` | Simple Button | T5 | `K:XPNDR_SET:4608` [SDK-RADE] | none | fixed image |
| 3,4 | | Empty | | | | |
| 3,5 | | Empty | | | | |
| 3,6 | `1` | Simple Button | T8 | `lua:XL24-XPDRPAD:DIGIT(1)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 3,7 | `2` | Simple Button | T8 | `lua:XL24-XPDRPAD:DIGIT(2)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 3,8 | `3` | Simple Button | T8 | `lua:XL24-XPDRPAD:DIGIT(3)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 4,1 | | Empty | | | | |
| 4,2 | | Empty | | | | |
| 4,3 | | Empty | | | | |
| 4,4 | | Empty | | | | |
| 4,5 | | Empty | | | | |
| 4,6 | `CLR` | Simple Button | T8 | Main `lua:XL24-XPDRPAD:BACK`, Second (long press) `lua:XL24-XPDRPAD:CLEAR` [README 2.1.1 LUAFUNC, 2.1] | none | fixed image |
| 4,7 | `0` | Simple Button | T8 | `lua:XL24-XPDRPAD:DIGIT(0)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 4,8 | `ENT` | Simple Button | T8 | `lua:XL24-XPDRPAD:ENTER` [README 2.1.1 LUAFUNC] | none (XPDR at 1,2 shows the result) | fixed image |

## Key table: radios

The C172's radios page ([phase3-radios.md](phase3-radios.md)); rows as that doc's "Key table: radios".

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to MORE | none | Back key |
| 1,2 | `NAV1` | COM Radio | T4 | `K:NAV1_RADIO_SWAP` [SDK-RADE] | Active `(A:NAV ACTIVE FREQUENCY:1, MHz)`, Standby `(A:NAV STANDBY FREQUENCY:1, MHz)` [SDK-RADV] | Format `2` |
| 1,3 | `NAV1 ID` | Display Value | T3 | none | `(A:NAV IDENT:1, String)` [SDK-RADV] | the station ident as text; Format empty |
| 1,4 | `NAV2` | COM Radio | T4 | `K:NAV2_RADIO_SWAP` [SDK-RADE] | Active `(A:NAV ACTIVE FREQUENCY:2, MHz)`, Standby `(A:NAV STANDBY FREQUENCY:2, MHz)` [SDK-RADV] | Format `2` |
| 1,5 | `NAV2 ID` | Display Value | T3 | none | `(A:NAV IDENT:2, String)` [SDK-RADV] | the station ident as text; Format empty |
| 1,6 | `COM2` | COM Radio | T4 | `K:COM2_RADIO_SWAP` [SDK-RADE] | Active `(A:COM ACTIVE FREQUENCY:2, MHz)`, Standby `(A:COM STANDBY FREQUENCY:2, MHz)` [SDK-RADV] | Format `3` |
| 1,7 | `COM2 ID` | Display Value | T3 | none | `(A:COM ACTIVE FREQ IDENT:2, String)` [SDK-RADV] | the station ident as text; Format empty |
| 1,8 | | Empty | | | | |
| 2,1 | | Empty | | | | |
| 2,2 | `MHZ+` | Simple Button | T5 | `K:NAV1_RADIO_WHOLE_INC` [SDK-RADE] | none | fixed image |
| 2,3 | `KHZ+` | Simple Button | T5 | `K:NAV1_RADIO_FRACT_INC` [SDK-RADE] | none | fixed image |
| 2,4 | `MHZ+` | Simple Button | T5 | `K:NAV2_RADIO_WHOLE_INC` [SDK-RADE] | none | fixed image |
| 2,5 | `KHZ+` | Simple Button | T5 | `K:NAV2_RADIO_FRACT_INC` [SDK-RADE] | none | fixed image |
| 2,6 | `MHZ+` | Simple Button | T5 | `K:COM2_RADIO_WHOLE_INC` [SDK-RADE] | none | fixed image |
| 2,7 | `KHZ+` | Simple Button | T5 | `K:COM2_RADIO_FRACT_INC` [SDK-RADE] | none | fixed image |
| 2,8 | | Empty | | | | |
| 3,1 | | Empty | | | | |
| 3,2 | `MHZ-` | Simple Button | T5 | `K:NAV1_RADIO_WHOLE_DEC` [SDK-RADE] | none | fixed image |
| 3,3 | `KHZ-` | Simple Button | T5 | `K:NAV1_RADIO_FRACT_DEC` [SDK-RADE] | none | fixed image |
| 3,4 | `MHZ-` | Simple Button | T5 | `K:NAV2_RADIO_WHOLE_DEC` [SDK-RADE] | none | fixed image |
| 3,5 | `KHZ-` | Simple Button | T5 | `K:NAV2_RADIO_FRACT_DEC` [SDK-RADE] | none | fixed image |
| 3,6 | `MHZ-` | Simple Button | T5 | `K:COM2_RADIO_WHOLE_DEC` [SDK-RADE] | none | fixed image |
| 3,7 | `KHZ-` | Simple Button | T5 | `K:COM2_RADIO_FRACT_DEC` [SDK-RADE] | none | fixed image |
| 3,8 | | Empty | | | | |
| 4,1 | | Empty | | | | |
| 4,2 | | Empty | | | | |
| 4,3 | | Empty | | | | |
| 4,4 | | Empty | | | | |
| 4,5 | | Empty | | | | |
| 4,6 | `MIC1` | Dynamic Button | T2 | `K:PILOT_TRANSMITTER_SET:0` [SDK-RADE] | `(A:COM TRANSMIT:1, Bool)` [SDK-RADV] | On/Off image |
| 4,7 | `MIC2` | Dynamic Button | T2 | `K:PILOT_TRANSMITTER_SET:1` [SDK-RADE] | `(A:COM TRANSMIT:2, Bool)` [SDK-RADV] | On/Off image |
| 4,8 | | Empty | | | | |

## Key table: engine

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to the MORE page | none | Back key |
| 1,2 | `N1` | Display Value | T3 | none | `(A:TURB ENG N1:1, Percent)` [SDK-ENGV] | Format `1.1` |
| 1,3 | `N2` | Display Value | T3 | none | `(A:TURB ENG N2:1, Percent)` [SDK-ENGV] | Format `1.1` |
| 1,4 | `ITT` | Display Value | T3 | none | `(A:TURB ENG ITT:1, Celsius)` [SDK-ENGV; SDK-UNITS] | Format `1.0` |
| 1,5 | `FF PPH` | Display Value | T3 | none | `(A:TURB ENG FUEL FLOW PPH:1, Pounds per hour)` [SDK-ENGV] | Format `1.0` |
| 1,6 | | Empty | | | | |
| 1,7 | | Empty | | | | |
| 1,8 | | Empty | | | | |
| 2,1 | | Empty | | | | |
| 2,2 | `ENG RUN` | Display Value | T3 | none | `(A:GENERAL ENG COMBUSTION:1, Bool)` [SDK-ENGV] | Mappings `0=OFF:1=RUN` |
| 2,3 | `IGN` | Display Value | T3 | none | `(A:TURB ENG IGNITION SWITCH:1, Bool)` [SDK-ENGV; V-1 A-15] | Mappings `0=OFF:1=ON` |
| 2,4 | | Empty | | | | |
| 2,5 | | Empty | | | | |
| 2,6 | | Empty | | | | |
| 2,7 | | Empty | | | | |
| 2,8 | | Empty | | | | |
| 3,1 | | Empty | | | | |
| 3,2 | `FUEL L` | Display Value | T3 | none | `(A:FUEL LEFT QUANTITY, Gallons)` [SDK-FUELV] | Format `1.1` |
| 3,3 | `FUEL R` | Display Value | T3 | none | `(A:FUEL RIGHT QUANTITY, Gallons)` [SDK-FUELV] | Format `1.1` |
| 3,4 | `FUEL TOT` | Display Value | T3 | none | `(A:FUEL TOTAL QUANTITY, Gallons)` [SDK-FUELV] | Format `1.1` |
| 3,5 | | Empty | | | | |
| 3,6 | | Empty | | | | |
| 3,7 | | Empty | | | | |
| 3,8 | | Empty | | | | |
| 4,1 | | Empty | | | | |
| 4,2 | | Empty | | | | |
| 4,3 | | Empty | | | | |
| 4,4 | | Empty | | | | |
| 4,5 | | Empty | | | | |
| 4,6 | | Empty | | | | |
| 4,7 | | Empty | | | | |
| 4,8 | | Empty | | | | |

## What the keys do

- **Main, row 1:** BAT switches battery 1 (the SF50 has two; the key is lit from the switch's own B-var). N1
  shows the engine's N1 in percent. PARK toggles the parking brake, lit from the brake. GEAR shows the gear
  handle (`UP` or `DOWN`) and does nothing on a press. FLAPS shows the flap handle position as a number
  (0 = up): a press moves it one step out, a long press (half a second or more) one step in.
- **Main, rows 2 and 3:** the C172's keys as they are: AP, HDG, ALT, VS, NAV, APR, FLC and FD by the standard
  autopilot events, lit from the autopilot's SimVars; COM1 (press swaps), the XPDR code, ATC and MAP windows,
  CDI (GPS or VLOC, press toggles) and BARO (press: the standard baro event), as
  [phase2-main-page.md](phase2-main-page.md) describes.
- **Main, row 4:** NAV LT, STRB, LDG and PITOT switch the SF50's own nav lights, strobes, landing lights and
  pitot heat through its input events and show the B-var's value; TAXI sends the standard taxi light event and
  shows the taxi light SimVar.
- **Autopilot page:** the C172's mode keys, steps and readouts, plus the SF50's: VNV (the SF50's VNAV input
  event, lit from the VNAV button L-Var), A/T (arms the autothrottle, lit while armed), LVL (the wing leveler
  mode), TOGA (`TO/GA` while the go-around mode is on) and A/T MGD (`ON` while the autothrottle drives). CRS+,
  CRS- and CRS1 send the G3000 PFD 1 course knob's H-events (long press on CRS+/CRS-: the 10 degree standard
  step); HDG BUG syncs the heading bug with the G3000's own H-event.
- **Engine page:** readouts only: N1 and N2 (percent), ITT (degrees Celsius), fuel flow (pounds per hour),
  ENG RUN (`RUN` while the engine runs), IGN (the ignition switch SimVar), and the left, right and total fuel
  in gallons.
- **Copied pages:** trim, views, sim rate, V-speeds, COM pad, transponder and radios work as on the C172
  (their docs above); they use standard events, SimVars and the C172's Lua scripts, nothing C172-specific.

## Which route each key uses

The rule for the switch keys (V-1 A-5): per key, the input event list's name of its family
(`electrical_battery_*`, `lighting_nav_*`, `lighting_beacon_*`, `lighting_strobe_*`, `lighting_landing_*`,
`lighting_taxi_*`, `deice_pitot_*`; for VNV a name with `vertical_navigation` or `vnav`), as a T1 key with On
`1` / Off `0`; one match: that name; several: the lowest index (the others for V-2); none: the key keeps the
standard event and SimVar (BCN: empty when the list has no beacon).

| Key | Matches in the list | Built |
|---|---|---|
| main 1,1 `BAT` | IE-SF50 80 `B:sf50_electrical_battery_1_switch`, 81 `B:sf50_electrical_battery_2_switch`, 82 `B:sf50_electrical_battery_generator_intercept` | IE-SF50 80 (battery 1, the lowest index); 81 and 82 for V-2 |
| main 4,1 `NAV LT` | IE-SF50 130 `B:sf50_lighting_nav_lights_intercept` | IE-SF50 130 (weak: an `_intercept` input event, V-1 A-15) |
| main 4,2 `BCN` | none | Empty (the SF50's flight files name no beacon either) |
| main 4,3 `STRB` | IE-SF50 40 `B:lighting_strobe_1` | IE-SF50 40 |
| main 4,4 `LDG` | IE-SF50 129 `B:sf50_lighting_landing_lights` | IE-SF50 129 |
| main 4,5 `TAXI` | none | `K:TOGGLE_TAXI_LIGHTS` with `(A:LIGHT TAXI, Bool)` (SDK-ELECE, SDK-SYSV) |
| main 4,6 `PITOT` | IE-SF50 31 `B:deice_pitot_1` | IE-SF50 31 |
| autopilot 1,8 `VNV` | IE-SF50 62 `B:sf50_autopilot_vnav_mode` | IE-SF50 62 as the command; read `L:XMLVAR_VNAVButtonValue` |

VNV is read from `L:XMLVAR_VNAVButtonValue` (the VNAV button state, HH-MS), as V-1's VNV design and the
C172's VNV key (B-var command, L-Var read): a mode button's input event says what was pressed, the L-Var
whether VNAV is on. The other keys read the same B-var they write, as the C172's T1 keys. Whether each B-var
reads 0 and 1 is a hand-test item.

Everything else uses the routes the C172 pages use (standard K-events, SimVars) or the G3000 H-events
(WT-G3000H). The list also names SF50 autopilot input events (`sf50_autopilot_*`, IE-SF50 46 to 63), the
parking brake (IE-SF50 117), the flap selector (115) and the gear lever (116); V-1 keeps the standard routes
for those keys (V-1 A-5 covers only the switch keys and VNV), and V-2 can compare them.

## Guarded keys

- **GEAR** and **TOGA** are readouts: the gear lever, the emergency gear drop and the throttle's TOGA button
  stay in the cockpit (V-1 A-8).
- No key starts or stops the engine, switches the ignition, the fuel selector or the fuel cut-off: the engine
  page is readouts only.
- No **CAPS** (parachute) and no **Safe Return** (emergency autoland) key or readout on any page (V-1 A-7),
  though the list names their input events (IE-SF50 72, 73, 135, 136).
- BAT and A/T are plain toggles, as their cockpit switches: press them in flight only on purpose.

## What each key holds

The key kinds of [phase2-main-page.md](phase2-main-page.md), "What each key holds": every key is a copy of a
real saved key with only the listed fields changed (the generator does this).

| Kind | Action, copied from | Keys here |
|---|---|---|
| T1 B-Var switch | Dynamic Button, the Phase 1 BAT key (`p1:0,0`): Command Address and Value Address a `B:` input event, On `1` / Off `0`, Special State on | main 1,1, 4,1, 4,3, 4,4, 4,6; autopilot 1,8 (Value Address the L-Var) |
| T2 K-event mode | Dynamic Button, the Phase 1 AP key (`p1:3,0`): Command Address a `K:` event, Value Address a SimVar | main 1,4 (the Phase 1 PARK key `p1:1,0`), row 2, 4,5; autopilot 2,8, 3,7 and the C172's mode keys |
| T3 Display Value | the Phase 1 RPM key (`p1:2,0`): Value Address, Format, Mappings; command none or a press command | main 1,2, 1,5, 1,6, 3,2, 3,5, 3,6; autopilot 3,2, 3,3, 3,8, 4,8; engine |
| T4 COM Radio | `com_radio` (templates.json) | main 3,1 and the copied pages' radio keys |
| T5 Simple Button | `simple_button` with the AP key's states | main 3,3, 3,4; autopilot 2,3, 4,3 and the step keys |

The copied pages keep every kind and field of their C172 keys (their docs, "What each key holds"), including
the views page's A-Var writes to `CAMERA STATE` and the transponder's to `TRANSPONDER STATE:1` (V-1 A-14),
the trim gauge and the Lua Function keys. Title sizes follow [navigation.md](navigation.md), "Rules".

## Profile Manager mapping

A package can't carry an aircraft mapping (PKG-DOC). To make PilotsDeck switch to this profile when the SF50
loads, the user adds it once in the Profile Manager, in the form of [package.md](package.md):

1. Open the Profile Manager, **Profile Mapping**, and pick `MSFS2024 VisionJet`.
2. Check "StreamDeck Profile modified for Switching".
3. Type the search string `microsoft_sf50` and press **Plus**, then **Save**.

PilotsDeck switches to a profile when one of its search strings is part of the loaded aircraft's string (case
does not matter, PKG-DOC); `microsoft_sf50` is in the aircraft string of all three presets (PD-LOG). If the
mapping does not switch, pick the profile by hand in the Stream Deck app.

## The MobiFlight WASM module

The four `H:` commands (autopilot CRS+, CRS-, CRS1 and the HDG BUG press) go through the MobiFlight WASM
module: "PilotsDeck sends every H-event and all calculator code through the MobiFlight WASM module"
([troubleshooting.md](troubleshooting.md#the-mobiflight-wasm-module)). It is installed on this PC
([installation.md](installation.md)); those docs do not list these keys yet (V-1 A-20). Without the module
those four presses do nothing; their readouts, the long presses of CRS+ and CRS- and every other key do not
need it.

## What the keys show when the SF50 isn't there

- No sim, or no flight: PilotsDeck's own idle and waiting images, as on the other profiles.
- Another aircraft: the SimVar keys show that aircraft's own values; `L:XMLVAR_VNAVButtonValue` and
  `L:WT_TOGA_ACTIVE` read 0 or that aircraft's value. BAT, NAV LT and LDG use input events only the SF50 has
  (`sf50_` names) and read nothing there. STRB (`lighting_strobe_1`) and PITOT (`deice_pitot_1`) use generic
  names that other aircraft can have too: the 2024 C172 has `deice_pitot_1`
  ([reference/InputEvents-C172-G1000.txt](reference/InputEvents-C172-G1000.txt), line 139), so in the C172
  PITOT shows and switches the C172's pitot heat.
- **Keys act on any aircraft that has their event:** the TAXI, PARK, FLAPS, AP mode, A/T, LVL and radio keys
  (standard events) and STRB and PITOT (generic input events) move the loaded aircraft's own controls where it
  has them. Keep the profile on the SF50 with the Profile Manager mapping and do not press the light, PITOT,
  PARK, FLAPS, AP or A/T keys in another aircraft.
- If the SF50 ignores a standard event, the key's read stays where it was and the key stays dark: the hand
  test records it.

## Not on these pages, and why

V-2 needs facts no source gave for V-1 (GTC and softkey events, the meaning of the list's SF50 input events):

- **Pages:** systems (MORE 2,2), ice and environment, the GTC touch controllers, the PFD and MFD softkeys
  (MORE 1,2 and 1,3).
- **Main 1,3** (no SF50 fuel pump name), **4,2** (no beacon), **4,7** (ice protection: NORM, HIGH and MAX
  modes that a toggle event can't match; the list's `sf50_deice_*`, IE-SF50 74 to 79).
- **Autopilot:** BC and YD (no SF50 source), BARO STD, the FMS and MAN speed mode buttons (IE-SF50 53, 58).
- **Engine and cabin:** engine start and stop, fuel selector, ECS, oxygen (IE-SF50 64 to 71, 86, 87, 114,
  133).
- **Second battery** (IE-SF50 81) and the generators (IE-SF50 82 to 84).
- **Other lights:** the recognition lights (IE-SF50 132, an `_intercept` input event) and the wing light
  (IE-SF50 41); V-2 can compare the recognition lights with TAXI (the list has no taxi light).
- **Trim:** the C172's later aileron and rudder trim keys; V-2 can add rudder trim (IE-SF50 35).
- **CAPS and Safe Return:** never (V-1 A-7).

## Fallbacks

Use one only if the checklist shows the main route does not work, and say which one you used. None is tested.
A key that fails with no working fallback becomes a readout (command none) or Empty, and its row in
aircraft-mappings.md says "does not work".

| Key | If it fails | Fallback | Source |
|---|---|---|---|
| BAT, NAV LT, STRB, LDG, PITOT (V-1 A-5) | The B-var write does nothing, or the key does not follow the cockpit switch | The standard event with the SimVar read, as TAXI: `K:TOGGLE_NAV_LIGHTS` / `(A:LIGHT NAV, Bool)`, `K:STROBES_TOGGLE` / `(A:LIGHT STROBE, Bool)`, `K:LANDING_LIGHTS_TOGGLE` / `(A:LIGHT LANDING, Bool)`, `K:PITOT_HEAT_TOGGLE` / `(A:PITOT HEAT, Bool)`; BAT Empty | SDK-ELECE, SDK-SYSV, SDK-AMISCE |
| NAV LT (V-1 A-15) | The `_intercept` input event does not move the switch | As the row above | IE-SF50 130 |
| TAXI (V-1 A-15) | The K-event changes nothing or not the cockpit switch | Empty (the list has no taxi light) | |
| VNV (V-1 A-9) | The B-var press does nothing | The L-Var write `L:XMLVAR_VNAVButtonValue`, On `1` / Off `0`; else readout only, Mappings `0=OFF:1=ON` | HH-MS |
| CRS+, CRS-, CRS1 (V-1 A-15) | The H-event does nothing (the SF50 has no PFD bezel knob) | The long press K-events stay; CRS1 a readout | WT-G3000H |
| HDG BUG (V-1 A-15) | The press does not sync the bug | `K:AP_HDG_CURRENT_HDG_SET`, as the C172 | SDK-APE |
| TOGA (V-1 A-15) | The readout never shows `TO/GA` | `(A:AUTOPILOT TAKEOFF POWER ACTIVE, Bool)` | SDK-APV |
| A/T (V-1 A-8) | A stronger guard is wanted | Readout only (command none) | |
| BARO (V-1 A-15) | `K:BAROMETRIC` does nothing on the G3000 | STD in V-2 | HH-MS |
| FLAPS (V-1 A-15) | The number per detent is unclear | Mappings after the test | |
| Views, XPDR (V-1 A-14) | The A-Var writes do nothing on the SF50 | Those five keys become their readouts (command none) | |

Also hand-test items with no fallback yet (V-1 A-15): LVL and A/T (SDK only), fuel in gallons, ITT in
Celsius, IGN under the FADEC, the C172's V-speed SimVars on a jet, and the COM pad on the G3000.

## How to test

Run [tests/manual-checklist.md](../tests/manual-checklist.md), section "VisionJet SF50 profile (V-1)". As on
the other profiles, check both directions: press a key and watch the cockpit, then **work the control in the
cockpit with the mouse and check that the key follows without a key being pressed.** Never press GEAR or TOGA
expecting an action (they are readouts). Record which battery BAT moves, the value each B-var reads, the flap
number per detent, and every key the G3000 ignores.

## When it passes

1. Any change found in the test goes into `tools/profilegen/visionjet-sf50.json` and this doc; then the
   profile is regenerated (not exported from the app) and imported again.
2. Fill in the "Verified" column of the rows in aircraft-mappings.md ("Cirrus Vision SF50 (MSFS 2024 default,
   V-1)") with the date, sim version and SF50 preset, for each function that passed; mark a row "does not
   work" where a key failed.

## Sources

| Tag | Source |
|---|---|
| IE-SF50 n | [reference/InputEvents-SF50.txt](reference/InputEvents-SF50.txt), line n: the plugin's `InputEvents.txt` written when the user loaded the SF50 with PilotsDeck running (2026-11-16, 141 lines, sha256 4ca529d7...), copied as it is |
| PD-LOG | The plugin log `PilotsDeck20261116.log` (read only, searched, 2026-11-16): lines 12807, 122712 and 192813 (the SF50's aircraft strings with `sf50_family`, `sf50_executive`, `sf50_complete`), line 12830 (`ProfileSwitcherManager ... Searching 0 valid Profiles`) |
| SF50-PKG | The SF50's streamed package `%APPDATA%\Microsoft Flight Simulator 2024\Packages\StreamedPackages\fs24-microsoft-aircraft-sf50\` (read by search only, 2026-11-16): `content\minimal.fsarchive` holds panel.cfg (WTG3000v2 PFD `?Index=1`, MFD, GTC 1 to 3, near byte 115812), the flight files (`[Electrical.0]` two batteries, `[Switches.0]`, near byte 256530) and en-us.loc tooltip keys; the model behaviours are not readable |
| PKG-DOC | [package.md](package.md), lines 51 to 63: a package can't carry an aircraft mapping; the Profile Manager's Profile Mapping steps; a search string matches as a part of the aircraft string, case aside |
| README | PilotsDeck README, https://github.com/Fragtality/PilotsDeck/blob/master/README.md (read 2026-11-16): 2.1 (Second command on a long press, >= 500 ms), 2.1.1 (A-Var `(A:Name:Index, Unit)`, B-Var "The Name of the B-Var with preceding `B:`!", K-Var, L-Var with On and Off values, H-Var "can't be read"), 2.1.2, 3.5.1 |
| SDK-APE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-autopilot-and-flight-assistance-events/ (`AP_WING_LEVELER` "Toggles wing leveler mode", `AUTO_THROTTLE_ARM` "Toggles autothrottle arming mode", `AP_HDG_CURRENT_HDG_SET` and the C172's mode events), read 2026-11-16 |
| SDK-APV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-autopilot-and-assistant-variables/ (`AUTOPILOT WING LEVELER`, `AUTOPILOT THROTTLE ARM`, `AUTOPILOT MANAGED THROTTLE ACTIVE`, `AUTOPILOT TAKEOFF POWER ACTIVE`, Bool; `AUTOPILOT HEADING LOCK DIR`, Degrees), read 2026-11-16 |
| SDK-ENGV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-engine-variables/ (`TURB ENG N1`, `TURB ENG N2` Percent; `TURB ENG ITT` Rankine, read in Celsius; `TURB ENG FUEL FLOW PPH`; `TURB ENG IGNITION SWITCH` Bool; `GENERAL ENG COMBUSTION` Bool), read 2026-11-16 |
| SDK-FUELV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-fuel-variables/ (`FUEL LEFT QUANTITY`, `FUEL RIGHT QUANTITY`, `FUEL TOTAL QUANTITY`, Gallons), read 2026-11-16 |
| SDK-ELECE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-electrical-events/ (`TOGGLE_TAXI_LIGHTS`, `TOGGLE_NAV_LIGHTS`, `STROBES_TOGGLE`, `LANDING_LIGHTS_TOGGLE`), read 2026-11-16 |
| SDK-SYSV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-system-variables/ (`LIGHT TAXI`, `LIGHT NAV`, `LIGHT STROBE`, `LIGHT LANDING`, `PITOT HEAT`, Bool), read 2026-11-16 |
| SDK-AMISCE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-miscellaneous-events/ (`PITOT_HEAT_TOGGLE`), read 2026-11-16 |
| SDK-GEARV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-brake-and-landing-gear-variables/ (`GEAR HANDLE POSITION`: "0 means the handle is retracted and 1 is the handle fully applied", units Percent Over 100, read here as Bool), read 2026-11-16 |
| SDK-FCE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-flight-control-events/ (`FLAPS_INCR`, `FLAPS_DECR`) |
| SDK-CTLV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-control-variables/ (`FLAPS HANDLE INDEX`, number) |
| SDK-RADV, SDK-RADE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-radio-navigation-variables/ (`NAV OBS`), https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-radio-navigation-events/ (`VOR1_OBI_FAST_INC/DEC`) |
| SDK-UNITS | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/simulation-variable-units/ |
| WT-G3000H | MSFS Avionics Framework docs (2024), G3000 H event list, https://microsoft.github.io/msfs-avionics-mirror/2024/docs/avionics/g3000/h-event-list (`AS3000_PFD_[index]_CRS_INC`, `_CRS_DEC`, `_CRS_PUSH`, "[index] is the instrument index of the PFD (1 or 2)"; `Garmin_AP_HDG_Sync` "Autopilot selected HDG sync."), read 2026-11-16 |
| HH-MS | HubHop presets for "Cirrus SF50 Vision Jet (MSFS2024)" (vendor Microsoft), https://hubhop.mobiflight.com/presets/?aircraft=Cirrus+SF50+Vision+Jet+%28MSFS2024%29, read 2026-11-16 (for V-0): `L:WT_TOGA_ACTIVE` ("TOGA annunciator"), the VNAV toggle `(L:XMLVAR_VNAVButtonValue) ! (>L:XMLVAR_VNAVButtonValue)` |
| FORUM-24 | Official forum thread on the MSFS 2024 SF50, https://forums.flightsimulator.com/t/msfs2024-cirrus-sf50-vision-jet/664507 (the SF50 has an autothrottle), read 2026-11-16 |
| V-1 A-n | The ASSUMPTIONS of this profile's unit (V-1), ruled 2026-11-16: A-5 switch keys from the input event list, A-7 no CAPS or Safe Return, A-8 guards, A-9 VNV L-Var write, A-14 the copied A-Var writes, A-15 weak sources, A-20 the MobiFlight note |

Tags of the rows copied from the C172 docs, as those docs define them (each doc's "Sources"):

| Tag | Source |
|---|---|
| SDK-APT, SDK-AS1000, SDK-MISCE, SDK-INSTE, SDK-CAMV, SDK-FMV, SDK-ENVV | The SDK pages named in [phase3-autopilot.md](phase3-autopilot.md), [phase2-sim-rate.md](phase2-sim-rate.md), [phase2-main-page.md](phase2-main-page.md), [phase2-trim-views.md](phase2-trim-views.md) and [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md), "Sources" |
| AM | [aircraft-mappings.md](aircraft-mappings.md): verified on the 2024 C172 (2026-11-11), not on the SF50 |
| IE n (no "SF50") | [reference/InputEvents-C172-G1000.txt](reference/InputEvents-C172-G1000.txt), line n: the C172's list, not the SF50's |
| PD-SRC, LR153-C4 | As [phase2-sim-rate.md](phase2-sim-rate.md) and [phase2-com1-pad.md](phase2-com1-pad.md), "Sources" |
| JIBLET, FORUM | As [phase3-autopilot.md](phase3-autopilot.md), "Sources" (leads only) |
| A-4, A-5, A-6, A-9 (in copied autopilot rows) | [phase3-autopilot.md](phase3-autopilot.md), "Open points" |
