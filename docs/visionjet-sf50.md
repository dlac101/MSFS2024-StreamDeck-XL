# VisionJet SF50 profile (MSFS 2024 default Cirrus Vision SF50)

**Status: generated (V-1 to V-3), not yet sim-tested; 14 pages, 183 keys.** The profile `MSFS2024 VisionJet`
is built by the generator, but nothing on it has been tried in the app or the sim yet. Every name below is
recorded as "Unverified" in [aircraft-mappings.md](aircraft-mappings.md) ("Cirrus Vision SF50 (MSFS 2024
default, V-1)", "(MSFS 2024 default, V-2)" and "(MSFS 2024 default, V-3)") until the checks in
[tests/manual-checklist.md](../tests/manual-checklist.md), sections "VisionJet SF50 profile (V-1)",
"VisionJet SF50 profile (V-2)" and "VisionJet SF50 profile (V-3)", pass.

Goal: a first useful profile for the Cirrus Vision SF50 (VisionJet) that comes with MSFS 2024 (folder
`microsoft_sf50`, presets `sf50_executive`, `sf50_family` and `sf50_complete`; not FlightFX's add-on). It uses
the C172 G1000 profile's grid and folder positions where the function applies ([navigation.md](navigation.md),
"Pages": "a later aircraft uses this grid and these folder positions where the function applies"): 12 pages,
146 keys in V-1; V-2 adds the systems and ICE/ENV pages and keys on main, trim, autopilot and more: 14 pages,
180 keys; V-3 adds hold to repeat on the step keys and a BARO column on radios: 14 pages, 183 keys. Every
readout and lit key shows the sim's own value; no key assumes its press worked.

**Built with the SF50's input event list (track A).** The user loaded the SF50 with PilotsDeck running on
2026-11-16, and PilotsDeck wrote its `InputEvents.txt`; the copy is
[reference/InputEvents-SF50.txt](reference/InputEvents-SF50.txt) (141 input events, cited "IE-SF50 n",
line n). The battery, nav, strobe, landing light and pitot heat keys and the autopilot VNV command use the
list's B-vars (rule: "Which route each key uses"), and since V-2 the PARK command too. The list has no beacon
light (V-2 puts RECOG at 4,2) and no taxi light (TAXI keeps the standard K-event).

Research and the candidate names: [visionjet-g2-research.md](visionjet-g2-research.md). The data file is
`tools/profilegen/visionjet-sf50.json`; the key tables below are the reference, and
`python tools/profilegen/check.py tools/profilegen/visionjet-sf50.json` compares the profile with them key by
key. The sim rate, COM pad and transponder pages call the C172's scripts as they are. V-3 adds this
profile's own script `XL24-SF50.lua` (in the package's `Scripts` folder): it runs hold to repeat ("Hold to
repeat").

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
- **SF50 flight files** (SF50-FLT, V-2, read by search only): the nine flight files of the minimal archive
  hold a `[LocalVars_EX1.0]` section with cockpit positions and their meanings, for example
  `SF50_Engine_Run_Knob_Position` 0 STOP / 1 RUN, `SF50_Fuel_Control_Switch_Position=1` (AUTO),
  `SF50_Engine_IP_Switch_Position=0` and `SF50_WingStab_IP_Switch_Position=0` (OFF),
  `SF50_Bleed_Air_Switch_State` 0/1. The SDK (SDK-FLT) says this section holds scoped `L:1` variables: V-2
  uses them only as position meanings (Mappings), never as addresses (V-2 A-16). The tooltips (SF50-PKG) show
  the ice protection as three toggles (engine, wing/stab, windshield) plus a windshield HIGH toggle and a
  windshield MAX button held to dispense fluid. No file says which value an input event takes per position or
  which SimVar it drives.
- **scmon capture** (SCMON-SF50, 2026-11-16, MSFS 2024, version not recorded): with the SF50 loaded, the user
  worked the cockpit controls with the mouse while a copy of `tools/scmon` read the B-vars through PilotsDeck.
  The values each B-var took are in aircraft-mappings.md (V-2 section); some B-vars read 0 for up to about
  30 s after the profile loaded. V-1's PARK failed: with the brake set, `K:PARKING_BRAKES` from the deck
  moved `BRAKE PARKING POSITION` to 0 and back to 1 within about 0.1 s while `B:sf50_handling_parking_brake`
  stayed 1, so PARK now writes that input event (V-2). No other deck key was tested.
- **SF50 checklist** (SF50-CHK, V-3, read by search only): the SF50's own checklist names the fuel control
  switch's three positions ("CHECK LEFT/AUTO/RIGHT", line 1448) and says to press and hold the windshield MAX
  switch until fluid exits the spray bar (line 4163). It names no variable. With SF50-FLT's AUTO = 1 and the
  values 0, 1 and 2 that SCMON-SF50 saw, V-3 shows FUEL CTL as `LEFT`, `AUTO` or `RIGHT` (an inference until
  the sim check, V-3 A-8).
- **Plugin log, the V-1 keys in flight** (PD-LOG2, leads only): on 2026-11-16 the user pressed HDG+ 6 times
  and HDG- 16 times about 0.2 s apart, ALT+ 24 times and its long press once, CRS+ and its long press once:
  the case for hold to repeat. The log does not say whether the bugs moved. No V-2 systems, ICE/ENV, FMS SPD,
  MAN SPD, YD or BARO STD command was sent yet.

## Where the pages sit

The main page has no back key. Every child page has its back key at 1,1; at most two folder levels
([navigation.md](navigation.md), "MSFS2024 VisionJet pages").

| Opened by | Page | Level | Holds |
|---|---|---|---|
| main 1,7 `TRIM` | trim | 1 | the C172's current trim page (elevator and rudder trim) without its aileron trim keys (V-2); the trim keys hold to repeat (V-3) |
| main 1,8 `VIEWS` | views | 1 | the C172's views page as it is |
| main 3,7 `SIM RATE` | simrate | 1 | the C172's sim rate page as it is (`XL24-SIMRATE.lua`) |
| main 3,8 `CHECKLIST` | checklist | 1 | the back key only (Phase 5) |
| main 4,8 `MORE` | more | 1 | eight folder keys |
| more 1,4 `V-SPEEDS` | vspeeds | 2 | the C172's V-speeds page as it is |
| more 1,5 `COM PAD` | compad | 2 | the C172's COM1 pad as it is (`XL24-COMPAD.lua`) |
| more 1,6 `AUTOPILOT` | autopilot | 2 | the C172's autopilot page with the SF50's changes (G3000, autothrottle) |
| more 1,7 `XPDR` | xpdr | 2 | the C172's transponder page as it is (`XL24-XPDRPAD.lua`) |
| more 1,8 `RADIOS` | radios | 2 | the C172's radios page with hold to repeat on its step keys, plus a BARO column (V-3) |
| more 2,2 `SYSTEMS` | systems | 2 | battery 2 and generator switches, electrical, engine knob, starter and fuel control readouts (V-2) |
| more 2,3 `ENGINE` | engine | 2 | engine and fuel readouts (new) |
| more 2,4 `ICE/ENV` | iceenv | 2 | ice protection, wing light, oxygen, bleed air and ECS (V-2) |

MORE 1,2 and 1,3 (the C172's PFD and MFD bezel pages) stay empty: the SF50's PFD and MFD have no softkeys, and
the GTC page is V-4 ("Not on these pages").

## Layouts

Positions are **row,column**, 1-based, row 1 at the top. `>` marks a folder key, `-` an empty position.

**main**

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | BAT | N1 | - | PARK | GEAR | FLAPS | TRIM > | VIEWS > |
| **Row 2** | AP | HDG | ALT | VS | NAV | APR | FLC | FD |
| **Row 3** | COM1 | XPDR | ATC | MAP | CDI | BARO | SIM RATE > | CHECKLIST > |
| **Row 4** | NAV LT | RECOG | STRB | LDG | TAXI | PITOT | ICE | MORE > |

**trim** (V-2)

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | - | - | - | - | - | - | - |
| **Row 2** | - | TRIM UP | - | - | - | - | - | - |
| **Row 3** | - | - | - | TRIM | - | RUD L | RUD TRIM | RUD R |
| **Row 4** | - | TRIM DN | - | - | - | - | - | - |

**more**

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | - | - | V-SPEEDS > | COM PAD > | AUTOPILOT > | XPDR > | RADIOS > |
| **Row 2** | - | SYSTEMS > | ENGINE > | ICE/ENV > | - | - | - | - |

Rows 3 and 4 are empty.

**autopilot**

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | AP | FD | HDG | NAV | APR | FMS SPD | VNV |
| **Row 2** | ALT | HDG+ | CRS+ | ALT+ | VS+ | SPD+ | YD | A/T |
| **Row 3** | VS | HDG BUG | CRS1 | ALT SEL | VS TGT | FLC SPD | LVL | TOGA |
| **Row 4** | FLC | HDG- | CRS- | ALT- | VS- | SPD- | MAN SPD | A/T MGD |

**engine**

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | N1 | N2 | ITT | FF PPH | - | - | - |
| **Row 2** | - | ENG RUN | IGN | - | - | - | - | - |
| **Row 3** | - | FUEL L | FUEL R | FUEL TOT | - | - | - | - |

Row 4 is empty.

**systems** (V-2)

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | BAT 2 | GEN 1 | GEN 2 | - | BUS V | - | LOAD A |
| **Row 2** | - | ENG KNOB | STARTER | FUEL CTL | - | - | - | - |

Rows 3 and 4 are empty.

**iceenv** (V-2)

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | ENG IPS | WING/STAB | WSHLD | WSHLD HI | - | WING LT | - |
| **Row 2** | - | ENG AI | STRUCT | WSHLD SW | - | - | - | - |
| **Row 3** | - | OXYGEN | BLEED | ECS DIS | DEFOG | AFT CTL | TEMP BKUP | - |
| **Row 4** | - | TEMP FWD | TEMP AFT | FAN FWD | FAN AFT | - | - | - |

**radios** (V-3: the C172's radios page plus the BARO column)

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | NAV1 | NAV1 ID | NAV2 | NAV2 ID | COM2 | COM2 ID | BARO |
| **Row 2** | - | MHZ+ | KHZ+ | MHZ+ | KHZ+ | MHZ+ | KHZ+ | BARO+ |
| **Row 3** | - | MHZ- | KHZ- | MHZ- | KHZ- | MHZ- | KHZ- | BARO- |
| **Row 4** | - | - | - | - | - | MIC1 | MIC2 | - |

The pages views, simrate, vspeeds, compad and xpdr have the C172's layouts, radios the C172's plus its BARO
column, and trim the C172's without its aileron trim keys:
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
| 1,3 | | Empty | | | | Fuel pump: the SF50 has none (IE-SF50 and its flight files name none); the fuel control knob is on systems |
| 1,4 | `PARK` | Dynamic Button | T1 | `B:sf50_handling_parking_brake`, On `1` / Off `0` [IE-SF50 117; README 2.1.1, 2.1.2; SCMON-SF50] | `(A:BRAKE PARKING POSITION, Bool)` [AM, SDK-GEARV] | On/Off image, Special State |
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
| 3,6 | `BARO` | Display Value | T3 | Main `K:BAROMETRIC` [SDK-INSTE], Second (long press) `K:BAROMETRIC_STD_PRESSURE` [SDK-INSTE; HH-MS; README 2.1; V-2 A-10] | `(A:KOHLSMAN SETTING HG:1, inHg)` [SDK-SYSV] | Format `2.2` |
| 3,7 | `SIM RATE` | Folder | (Stream Deck) | Opens the child page **simrate** | none | Folder; the page's keys: "Key table: simrate" below |
| 3,8 | `CHECKLIST` | Folder | (Stream Deck) | Opens the child page **checklist** | none | Folder; the page holds only the back key (1,1) |
| 4,1 | `NAV LT` | Dynamic Button | T1 | `B:sf50_lighting_nav_lights_intercept`, On `1` / Off `0` [IE-SF50 130; README 2.1.1; V-1 A-5, A-15] | `B:sf50_lighting_nav_lights_intercept` [IE-SF50 130] | On/Off image, Special State |
| 4,2 | `RECOG` | Dynamic Button | T1 | `B:sf50_lighting_recognition_lights_intercept`, On `1` / Off `0` [IE-SF50 132; README 2.1.1; weak, V-2 A-4] | `B:sf50_lighting_recognition_lights_intercept` [IE-SF50 132] | On/Off image, Special State |
| 4,3 | `STRB` | Dynamic Button | T1 | `B:lighting_strobe_1`, On `1` / Off `0` [IE-SF50 40; README 2.1.1; V-1 A-5] | `B:lighting_strobe_1` [IE-SF50 40] | On/Off image, Special State |
| 4,4 | `LDG` | Dynamic Button | T1 | `B:sf50_lighting_landing_lights`, On `1` / Off `0` [IE-SF50 129; README 2.1.1; V-1 A-5] | `B:sf50_lighting_landing_lights` [IE-SF50 129] | On/Off image, Special State |
| 4,5 | `TAXI` | Dynamic Button | T2 | `K:TOGGLE_TAXI_LIGHTS` [SDK-ELECE; no taxi B-var in IE-SF50, V-1 A-5, A-15] | `(A:LIGHT TAXI, Bool)` [SDK-SYSV] | On/Off image |
| 4,6 | `PITOT` | Dynamic Button | T1 | `B:deice_pitot_1`, On `1` / Off `0` [IE-SF50 31; README 2.1.1; V-1 A-5] | `B:deice_pitot_1` [IE-SF50 31] | On/Off image, Special State |
| 4,7 | `ICE` | Dynamic Button | G1 | Main `B:sf50_deice_wingstab`, Second (long press) `B:sf50_deice_wingstab`: a press writes 1 (on), a long press 0 (off) [IE-SF50 78; README 2.1, 2.1.1; PD-LONG; V-2 A-6, A-13] | `B:sf50_deice_wingstab` [IE-SF50 78] | On/Off image, Special State |
| 4,8 | `MORE` | Folder | (Stream Deck) | Opens the child page **more** | none | Folder; the page's keys: "Key table: more" below |

## Key table: trim

The C172's current trim page (V-2): elevator trim up and down with the trim gauge, rudder trim left and right
with the rudder trim gauge, without the C172's aileron trim keys (the SF50 has no aileron trim: IE-SF50 lists
elevator and rudder trim only). The rows are those of the "Key table: trim" in
[phase2-trim-views.md](phase2-trim-views.md) at 18b36eae with 2,6 to 2,8 Empty. V-1's TRIM and TRIM DEG
readouts (3,2, 3,3) are gone, as on the C172. The rudder trim keys send the standard K-events, not the SF50's
own `B:handling_ruddertrim_1` (IE-SF50 35; fallback, V-2 A-11). V-3: the four trim keys hold to repeat (H1),
at most 8 s per hold ("Hold to repeat").

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
| 2,2 | `TRIM UP` | Simple Button | H1 | `lua:XL24-SF50:HOLD(25)` key down, `lua:XL24-SF50:RELEASE(25)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:ELEV_TRIM_UP` [SDK-FCE] | none (the gauge 3,4 shows the result) | fixed image |
| 2,3 | | Empty | | | | |
| 2,4 | | Empty | | | | |
| 2,5 | | Empty | | | | |
| 2,6 | | Empty | | | | |
| 2,7 | | Empty | | | | Aileron trim: the SF50 has none (IE-SF50 lists elevator and rudder trim only) |
| 2,8 | | Empty | | | | |
| 3,1 | | Empty | | | | |
| 3,2 | | Empty | | | | |
| 3,3 | | Empty | | | | |
| 3,4 | `TRIM` | Display Gauge | T9 | none | `(A:ELEVATOR TRIM PCT EX2, percent)` [SDK-CTLV, SDK-UNITS] | Format `1.0`; vertical bar, values up (Orientation Up, saved `-90`), `-100` to `100`, center line, pointer |
| 3,5 | | Empty | | | | |
| 3,6 | `RUD L` | Simple Button | H1 | `lua:XL24-SF50:HOLD(27)` key down, `lua:XL24-SF50:RELEASE(27)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:RUDDER_TRIM_LEFT` [SDK-FCE] | none (the gauge 3,7 shows the result) | fixed image |
| 3,7 | `RUD TRIM` | Display Gauge | T9 | none | `(A:RUDDER TRIM PCT, percent)` [SDK-CTLV, SDK20-CTLV, SDK-UNITS] | Format `1.1`; horizontal bar, values right (Orientation Right, saved `0`), `-100` to `100`, center line, pointer |
| 3,8 | `RUD R` | Simple Button | H1 | `lua:XL24-SF50:HOLD(28)` key down, `lua:XL24-SF50:RELEASE(28)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:RUDDER_TRIM_RIGHT` [SDK-FCE] | none (the gauge 3,7 shows the result) | fixed image |
| 4,1 | | Empty | | | | |
| 4,2 | `TRIM DN` | Simple Button | H1 | `lua:XL24-SF50:HOLD(26)` key down, `lua:XL24-SF50:RELEASE(26)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:ELEV_TRIM_DN` [SDK-FCE] | none (the gauge 3,4 shows the result) | fixed image |
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
| 1,2 | | Empty | | | | PFD softkeys: the SF50's PFD has none (IE-SF50 lists softkeys only on the GTCs); GTC page: V-4 |
| 1,3 | | Empty | | | | MFD softkeys: the SF50's MFD has none (IE-SF50 lists softkeys only on the GTCs); GTC page: V-4 |
| 1,4 | `V-SPEEDS` | Folder | (Stream Deck) | Opens the child page **vspeeds** | none | Folder; the page's keys: "Key table: vspeeds" below |
| 1,5 | `COM PAD` | Folder | (Stream Deck) | Opens the child page **compad** | none | Folder; the page's keys: "Key table: compad" below |
| 1,6 | `AUTOPILOT` | Folder | (Stream Deck) | Opens the child page **autopilot** | none | Folder; the page's keys: "Key table: autopilot" below |
| 1,7 | `XPDR` | Folder | (Stream Deck) | Opens the child page **xpdr** | none | Folder; the page's keys: "Key table: xpdr" below |
| 1,8 | `RADIOS` | Folder | (Stream Deck) | Opens the child page **radios** | none | Folder; the page's keys: "Key table: radios" below |
| 2,1 | | Empty | | | | |
| 2,2 | `SYSTEMS` | Folder | (Stream Deck) | Opens the child page **systems** | none | Folder; the page's keys: "Key table: systems" below |
| 2,3 | `ENGINE` | Folder | (Stream Deck) | Opens the child page **engine** | none | Folder; the page's keys: "Key table: engine" below |
| 2,4 | `ICE/ENV` | Folder | (Stream Deck) | Opens the child page **iceenv** | none | Folder; the page's keys: "Key table: iceenv" below |
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
| 1,2 | `1X` | Dynamic Button | T2 | `lua:XL24-SIMRATE:SET(1)` (steps `K:SIM_RATE_INCR` / `K:SIM_RATE_DECR`) [README 2.1.1 LUAFUNC, 3.5.1; SDK-MISCE; P2-6 route ruling] | `(A:SIMULATION RATE, number)` [SDK-ENVV, PD-SRC] | On/Off image: On `1`, Off `2` |
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
2,3, 2,7, 2,8, 3,2, 3,3, 3,7, 3,8, 4,3 and 4,8; the other rows as that doc's "Key table: autopilot". V-3: the
step keys 2,2 to 2,6 and 4,2 to 4,6 hold to repeat (H1, "Hold to repeat"); CRS and ALT lost their long press.

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to the MORE page | none | Back key |
| 1,2 | `AP` | Dynamic Button | T2 | `K:AP_MASTER` [SDK-APE; AM] | `(A:AUTOPILOT MASTER, Bool)` [SDK-APV; AM] | On/Off image |
| 1,3 | `FD` | Dynamic Button | T2 | `K:TOGGLE_FLIGHT_DIRECTOR` [SDK-APE; SDK-APT] | `(A:AUTOPILOT FLIGHT DIRECTOR ACTIVE, Bool)` [SDK-APV] | On/Off image |
| 1,4 | `HDG` | Dynamic Button | T2 | `K:AP_HDG_HOLD` [SDK-APE] | `(A:AUTOPILOT HEADING LOCK, Bool)` [SDK-APV] | On/Off image |
| 1,5 | `NAV` | Dynamic Button | T2 | `K:AP_NAV1_HOLD` [SDK-APE; SDK-APT] | `(A:AUTOPILOT NAV1 LOCK, Bool)` [SDK-APV] | On/Off image |
| 1,6 | `APR` | Dynamic Button | T2 | `K:AP_APR_HOLD` [SDK-APE; SDK-APT] | `(A:AUTOPILOT APPROACH HOLD, Bool)` [SDK-APV] | On/Off image |
| 1,7 | `FMS SPD` | Dynamic Button | T1-set | `B:sf50_autopilot_fms_speed_mode`, On `1` / Off `1` [IE-SF50 53; README 2.1.1; V-2 A-5] | `B:sf50_autopilot_fms_speed_mode` [IE-SF50 53] | On/Off image, Special State |
| 1,8 | `VNV` | Dynamic Button | T1 | `B:sf50_autopilot_vnav_mode`, On `1` / Off `0` [IE-SF50 62; README 2.1.1; V-1 A-5] | `L:XMLVAR_VNAVButtonValue` [HH-MS; SDK-APT] | On/Off image, Special State |
| 2,1 | `ALT` | Dynamic Button | T2 | `K:AP_ALT_HOLD` [SDK-APE; SDK-APT] | `(A:AUTOPILOT ALTITUDE LOCK, Bool)` [SDK-APV] | On/Off image |
| 2,2 | `HDG+` | Simple Button | H1 | `lua:XL24-SF50:HOLD(1)` key down, `lua:XL24-SF50:RELEASE(1)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:HEADING_BUG_INC` [SDK-APE] | none | fixed image |
| 2,3 | `CRS+` | Simple Button | H1 | `lua:XL24-SF50:HOLD(3)` key down, `lua:XL24-SF50:RELEASE(3)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `H:AS3000_PFD_1_CRS_INC` [WT-G3000H; SF50-PKG; weak, V-1 A-15] | none | fixed image |
| 2,4 | `ALT+` | Simple Button | H1 | `lua:XL24-SF50:HOLD(5)` key down, `lua:XL24-SF50:RELEASE(5)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:AP_ALT_VAR_INC` [SDK-APE] | none | fixed image |
| 2,5 | `VS+` | Simple Button | H1 | `lua:XL24-SF50:HOLD(7)` key down, `lua:XL24-SF50:RELEASE(7)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:AP_VS_VAR_INC` [SDK-APE] | none | fixed image |
| 2,6 | `SPD+` | Simple Button | H1 | `lua:XL24-SF50:HOLD(9)` key down, `lua:XL24-SF50:RELEASE(9)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:AP_SPD_VAR_INC` [SDK-APE] | none | fixed image |
| 2,7 | `YD` | Dynamic Button | T2 | `K:YAW_DAMPER_TOGGLE` [SDK-APE; weak, V-2 A-9] | `(A:AUTOPILOT YAW DAMPER, Bool)` [SDK-APV] | On/Off image |
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
| 4,2 | `HDG-` | Simple Button | H1 | `lua:XL24-SF50:HOLD(2)` key down, `lua:XL24-SF50:RELEASE(2)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:HEADING_BUG_DEC` [SDK-APE] | none | fixed image |
| 4,3 | `CRS-` | Simple Button | H1 | `lua:XL24-SF50:HOLD(4)` key down, `lua:XL24-SF50:RELEASE(4)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `H:AS3000_PFD_1_CRS_DEC` [WT-G3000H; SF50-PKG; weak, V-1 A-15] | none | fixed image |
| 4,4 | `ALT-` | Simple Button | H1 | `lua:XL24-SF50:HOLD(6)` key down, `lua:XL24-SF50:RELEASE(6)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:AP_ALT_VAR_DEC` [SDK-APE] | none | fixed image |
| 4,5 | `VS-` | Simple Button | H1 | `lua:XL24-SF50:HOLD(8)` key down, `lua:XL24-SF50:RELEASE(8)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:AP_VS_VAR_DEC` [SDK-APE] | none | fixed image |
| 4,6 | `SPD-` | Simple Button | H1 | `lua:XL24-SF50:HOLD(10)` key down, `lua:XL24-SF50:RELEASE(10)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:AP_SPD_VAR_DEC` [SDK-APE] | none | fixed image |
| 4,7 | `MAN SPD` | Dynamic Button | T1-set | `B:sf50_autopilot_man_speed_mode`, On `1` / Off `1` [IE-SF50 58; README 2.1.1; V-2 A-5] | `B:sf50_autopilot_man_speed_mode` [IE-SF50 58] | On/Off image, Special State |
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

The C172's radios page ([phase3-radios.md](phase3-radios.md)); rows as that doc's "Key table: radios",
except V-3's: the step keys hold to repeat (H1, "Hold to repeat"), and the BARO column is new: 1,8 shows the
altimeter setting (main 3,6's read), 2,8 and 3,8 step it.

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to MORE | none | Back key |
| 1,2 | `NAV1` | COM Radio | T4 | `K:NAV1_RADIO_SWAP` [SDK-RADE] | Active `(A:NAV ACTIVE FREQUENCY:1, MHz)`, Standby `(A:NAV STANDBY FREQUENCY:1, MHz)` [SDK-RADV] | Format `2` |
| 1,3 | `NAV1 ID` | Display Value | T3 | none | `(A:NAV IDENT:1, String)` [SDK-RADV] | the station ident as text; Format empty |
| 1,4 | `NAV2` | COM Radio | T4 | `K:NAV2_RADIO_SWAP` [SDK-RADE] | Active `(A:NAV ACTIVE FREQUENCY:2, MHz)`, Standby `(A:NAV STANDBY FREQUENCY:2, MHz)` [SDK-RADV] | Format `2` |
| 1,5 | `NAV2 ID` | Display Value | T3 | none | `(A:NAV IDENT:2, String)` [SDK-RADV] | the station ident as text; Format empty |
| 1,6 | `COM2` | COM Radio | T4 | `K:COM2_RADIO_SWAP` [SDK-RADE] | Active `(A:COM ACTIVE FREQUENCY:2, MHz)`, Standby `(A:COM STANDBY FREQUENCY:2, MHz)` [SDK-RADV] | Format `3` |
| 1,7 | `COM2 ID` | Display Value | T3 | none | `(A:COM ACTIVE FREQ IDENT:2, String)` [SDK-RADV] | the station ident as text; Format empty |
| 1,8 | `BARO` | Display Value | T3 | none | `(A:KOHLSMAN SETTING HG:1, inHg)` [SDK-SYSV] | Format `2.2` |
| 2,1 | | Empty | | | | |
| 2,2 | `MHZ+` | Simple Button | H1 | `lua:XL24-SF50:HOLD(13)` key down, `lua:XL24-SF50:RELEASE(13)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:NAV1_RADIO_WHOLE_INC` [SDK-RADE] | none | fixed image |
| 2,3 | `KHZ+` | Simple Button | H1 | `lua:XL24-SF50:HOLD(14)` key down, `lua:XL24-SF50:RELEASE(14)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:NAV1_RADIO_FRACT_INC` [SDK-RADE] | none | fixed image |
| 2,4 | `MHZ+` | Simple Button | H1 | `lua:XL24-SF50:HOLD(15)` key down, `lua:XL24-SF50:RELEASE(15)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:NAV2_RADIO_WHOLE_INC` [SDK-RADE] | none | fixed image |
| 2,5 | `KHZ+` | Simple Button | H1 | `lua:XL24-SF50:HOLD(16)` key down, `lua:XL24-SF50:RELEASE(16)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:NAV2_RADIO_FRACT_INC` [SDK-RADE] | none | fixed image |
| 2,6 | `MHZ+` | Simple Button | H1 | `lua:XL24-SF50:HOLD(17)` key down, `lua:XL24-SF50:RELEASE(17)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:COM2_RADIO_WHOLE_INC` [SDK-RADE] | none | fixed image |
| 2,7 | `KHZ+` | Simple Button | H1 | `lua:XL24-SF50:HOLD(18)` key down, `lua:XL24-SF50:RELEASE(18)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:COM2_RADIO_FRACT_INC` [SDK-RADE] | none | fixed image |
| 2,8 | `BARO+` | Simple Button | H1 | `lua:XL24-SF50:HOLD(11)` key down, `lua:XL24-SF50:RELEASE(11)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:KOHLSMAN_INC` [SDK-INSTE; weak, V-3 A-7] | none (1,8 shows the result) | fixed image |
| 3,1 | | Empty | | | | |
| 3,2 | `MHZ-` | Simple Button | H1 | `lua:XL24-SF50:HOLD(19)` key down, `lua:XL24-SF50:RELEASE(19)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:NAV1_RADIO_WHOLE_DEC` [SDK-RADE] | none | fixed image |
| 3,3 | `KHZ-` | Simple Button | H1 | `lua:XL24-SF50:HOLD(20)` key down, `lua:XL24-SF50:RELEASE(20)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:NAV1_RADIO_FRACT_DEC` [SDK-RADE] | none | fixed image |
| 3,4 | `MHZ-` | Simple Button | H1 | `lua:XL24-SF50:HOLD(21)` key down, `lua:XL24-SF50:RELEASE(21)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:NAV2_RADIO_WHOLE_DEC` [SDK-RADE] | none | fixed image |
| 3,5 | `KHZ-` | Simple Button | H1 | `lua:XL24-SF50:HOLD(22)` key down, `lua:XL24-SF50:RELEASE(22)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:NAV2_RADIO_FRACT_DEC` [SDK-RADE] | none | fixed image |
| 3,6 | `MHZ-` | Simple Button | H1 | `lua:XL24-SF50:HOLD(23)` key down, `lua:XL24-SF50:RELEASE(23)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:COM2_RADIO_WHOLE_DEC` [SDK-RADE] | none | fixed image |
| 3,7 | `KHZ-` | Simple Button | H1 | `lua:XL24-SF50:HOLD(24)` key down, `lua:XL24-SF50:RELEASE(24)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:COM2_RADIO_FRACT_DEC` [SDK-RADE] | none | fixed image |
| 3,8 | `BARO-` | Simple Button | H1 | `lua:XL24-SF50:HOLD(12)` key down, `lua:XL24-SF50:RELEASE(12)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:KOHLSMAN_DEC` [SDK-INSTE; weak, V-3 A-7] | none (1,8 shows the result) | fixed image |
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

## Key table: systems

The systems page (V-2, under MORE 2,2): the guarded battery 2 and generator switches (G1: a press
switches on, a long press off), bus volts and total load, and readouts of the engine run knob, the
starter and the fuel control knob (no write: V-2 A-7, A-8).

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to the MORE page | none | Back key |
| 1,2 | `BAT 2` | Dynamic Button | G1 | Main `B:sf50_electrical_battery_2_switch`, Second (long press) `B:sf50_electrical_battery_2_switch`: a press writes 1 (on), a long press 0 (off) [IE-SF50 81; README 2.1, 2.1.1; PD-LONG; V-2 A-6] | `B:sf50_electrical_battery_2_switch` [IE-SF50 81] | On/Off image, Special State |
| 1,3 | `GEN 1` | Dynamic Button | G1 | Main `B:sf50_electrical_gen_1_switch`, Second (long press) `B:sf50_electrical_gen_1_switch`: a press writes 1 (on), a long press 0 (off) [IE-SF50 83; README 2.1, 2.1.1; PD-LONG; V-2 A-6] | `B:sf50_electrical_gen_1_switch` [IE-SF50 83] | On/Off image, Special State |
| 1,4 | `GEN 2` | Dynamic Button | G1 | Main `B:sf50_electrical_gen_2_switch`, Second (long press) `B:sf50_electrical_gen_2_switch`: a press writes 1 (on), a long press 0 (off) [IE-SF50 84; README 2.1, 2.1.1; PD-LONG; V-2 A-6] | `B:sf50_electrical_gen_2_switch` [IE-SF50 84] | On/Off image, Special State |
| 1,5 | | Empty | | | | IE-SF50 82 `sf50_electrical_battery_generator_intercept`: what it switches is unknown (V-4) |
| 1,6 | `BUS V` | Display Value | T3 | none | `(A:ELECTRICAL BUS VOLTAGE:1, Volts)` [SDK-ELECV; phase3-systems.md] | Format `2.1` |
| 1,7 | | Empty | | | | Battery amps: which battery index the SF50's switches drive is open (V-2 A-3) |
| 1,8 | `LOAD A` | Display Value | T3 | none | `(A:ELECTRICAL TOTAL LOAD AMPS, Amperes)` [SDK-ELECV; phase3-systems.md] | Format `1.1` |
| 2,1 | | Empty | | | | |
| 2,2 | `ENG KNOB` | Display Value | T3 | none | `B:sf50_engine_run_knob` [IE-SF50 86; SF50-FLT] | Mappings `0=STOP:1=RUN` |
| 2,3 | `STARTER` | Display Value | T3 | none | `(A:GENERAL ENG STARTER:1, Bool)` [SDK-ENGV] | Mappings `0=OFF:1=ON` |
| 2,4 | `FUEL CTL` | Display Value | T3 | none | `B:sf50_fuel_control_knob` [IE-SF50 114; SF50-FLT; Mappings: SF50-CHK, SCMON-SF50, V-3 A-8] | Mappings `0=LEFT:1=AUTO:2=RIGHT` |
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

## Key table: iceenv

The ICE/ENV page (V-2, under MORE 2,4): the guarded engine, wing/stab and windshield ice protection
and oxygen switches (G1), the windshield HIGH, wing light and three ECS toggles (T1), the sim's ice
protection SimVars as readouts beside them (row 2), and readouts of bleed air, ECS disable and the
four ECS knobs (no write: V-2 A-7).

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to the MORE page | none | Back key |
| 1,2 | `ENG IPS` | Dynamic Button | G1 | Main `B:sf50_deice_engine`, Second (long press) `B:sf50_deice_engine`: a press writes 1 (on), a long press 0 (off) [IE-SF50 74; README 2.1, 2.1.1; PD-LONG; V-2 A-6] | `B:sf50_deice_engine` [IE-SF50 74] | On/Off image, Special State |
| 1,3 | `WING/STAB` | Dynamic Button | G1 | Main `B:sf50_deice_wingstab`, Second (long press) `B:sf50_deice_wingstab`: a press writes 1 (on), a long press 0 (off) [IE-SF50 78; README 2.1, 2.1.1; PD-LONG; V-2 A-6] | `B:sf50_deice_wingstab` [IE-SF50 78] | On/Off image, Special State |
| 1,4 | `WSHLD` | Dynamic Button | G1 | Main `B:sf50_deice_windshield`, Second (long press) `B:sf50_deice_windshield`: a press writes 1 (on), a long press 0 (off) [IE-SF50 76; README 2.1, 2.1.1; PD-LONG; V-2 A-6] | `B:sf50_deice_windshield` [IE-SF50 76] | On/Off image, Special State |
| 1,5 | `WSHLD HI` | Dynamic Button | T1 | `B:sf50_deice_windshield_high`, On `1` / Off `0` [IE-SF50 77; README 2.1.1] | `B:sf50_deice_windshield_high` [IE-SF50 77] | On/Off image, Special State |
| 1,6 | | Empty | | | | Windshield MAX: the cockpit button is held to dispense fluid (SF50-PKG); a key press can't hold it |
| 1,7 | `WING LT` | Dynamic Button | T1 | `B:lighting_wing_1`, On `1` / Off `0` [IE-SF50 41; README 2.1.1] | `B:lighting_wing_1` [IE-SF50 41] | On/Off image, Special State |
| 1,8 | | Empty | | | | |
| 2,1 | | Empty | | | | |
| 2,2 | `ENG AI` | Display Value | T3 | none | `(A:ENG ANTI ICE:1, Bool)` [SDK-ENGV] | Mappings `0=OFF:1=ON` |
| 2,3 | `STRUCT` | Display Value | T3 | none | `(A:STRUCTURAL DEICE SWITCH, Bool)` [SDK-SYSV] | Mappings `0=OFF:1=ON` |
| 2,4 | `WSHLD SW` | Display Value | T3 | none | `(A:WINDSHIELD DEICE SWITCH, Bool)` [SDK-SYSV] | Mappings `0=OFF:1=ON` |
| 2,5 | | Empty | | | | |
| 2,6 | | Empty | | | | |
| 2,7 | | Empty | | | | |
| 2,8 | | Empty | | | | |
| 3,1 | | Empty | | | | |
| 3,2 | `OXYGEN` | Dynamic Button | G1 | Main `B:sf50_pressurization_oxygen_master`, Second (long press) `B:sf50_pressurization_oxygen_master`: a press writes 1 (on), a long press 0 (off) [IE-SF50 133; README 2.1, 2.1.1; PD-LONG; V-2 A-6] | `B:sf50_pressurization_oxygen_master` [IE-SF50 133] | On/Off image, Special State |
| 3,3 | `BLEED` | Display Value | T3 | none | `B:sf50_pressurization_switch_air_bleed` [IE-SF50 134; SF50-FLT; SF50-PKG] | Mappings `0=FRESH:1=BLEED` |
| 3,4 | `ECS DIS` | Display Value | T3 | none | `B:sf50_cabin_ecs_disable` [IE-SF50 66] | Format `1.0` |
| 3,5 | `DEFOG` | Dynamic Button | T1 | `B:sf50_cabin_ecs_defog`, On `1` / Off `0` [IE-SF50 65; README 2.1.1] | `B:sf50_cabin_ecs_defog` [IE-SF50 65] | On/Off image, Special State |
| 3,6 | `AFT CTL` | Dynamic Button | T1 | `B:sf50_cabin_ecs_aft_control`, On `1` / Off `0` [IE-SF50 64; README 2.1.1] | `B:sf50_cabin_ecs_aft_control` [IE-SF50 64] | On/Off image, Special State |
| 3,7 | `TEMP BKUP` | Dynamic Button | T1 | `B:sf50_cabin_ecs_temp_backup`, On `1` / Off `0` [IE-SF50 69; README 2.1.1] | `B:sf50_cabin_ecs_temp_backup` [IE-SF50 69] | On/Off image, Special State |
| 3,8 | | Empty | | | | |
| 4,1 | | Empty | | | | |
| 4,2 | `TEMP FWD` | Display Value | T3 | none | `B:sf50_cabin_ecs_temp_knob_forward` [IE-SF50 71; SF50-FLT] | Format `1.0` |
| 4,3 | `TEMP AFT` | Display Value | T3 | none | `B:sf50_cabin_ecs_temp_knob_aft` [IE-SF50 70; SF50-FLT] | Format `1.0` |
| 4,4 | `FAN FWD` | Display Value | T3 | none | `B:sf50_cabin_ecs_fan_knob_forward` [IE-SF50 68] | Format `1.0` |
| 4,5 | `FAN AFT` | Display Value | T3 | none | `B:sf50_cabin_ecs_fan_knob_aft` [IE-SF50 67] | Format `1.0` |
| 4,6 | | Empty | | | | |
| 4,7 | | Empty | | | | |
| 4,8 | | Empty | | | | |

## What the keys do

- **Main, row 1:** BAT switches battery 1 (the SF50 has two; the key is lit from the switch's own B-var). N1
  shows the engine's N1 in percent. PARK toggles the parking brake by the SF50's own input event (V-2; the
  standard event failed in the SF50), lit from the brake SimVar. GEAR shows the gear handle (`UP` or `DOWN`)
  and does nothing on a press. FLAPS shows the flap handle position as a number (0 = up): a press moves it
  one step out, a long press (half a second or more) one step in.
- **Main, rows 2 and 3:** the C172's keys as they are: AP, HDG, ALT, VS, NAV, APR, FLC and FD by the standard
  autopilot events, lit from the autopilot's SimVars; COM1 (press swaps), the XPDR code, ATC and MAP windows,
  CDI (GPS or VLOC, press toggles) and BARO (press: the standard baro event), as
  [phase2-main-page.md](phase2-main-page.md) describes. V-2: a long press on BARO (half a second or more) sets
  standard pressure, 29.92 inHg (`K:BAROMETRIC_STD_PRESSURE`).
- **Main, row 4:** NAV LT, STRB, LDG and PITOT switch the SF50's own nav lights, strobes, landing lights and
  pitot heat through its input events and show the B-var's value; TAXI sends the standard taxi light event and
  shows the taxi light SimVar. V-2: RECOG switches the recognition lights by their input event (On `1` / Off
  `0`); ICE is the wing/stab ice protection switch, guarded: a press switches it on, a long press off (the
  same key as ICE/ENV 1,3).
- **Autopilot page:** the C172's mode keys, steps and readouts, plus the SF50's: VNV (the SF50's VNAV input
  event, lit from the VNAV button L-Var), A/T (arms the autothrottle, lit while armed), LVL (the wing leveler
  mode), TOGA (`TO/GA` while the go-around mode is on) and A/T MGD (`ON` while the autothrottle drives). CRS+,
  CRS- and CRS1 send the G3000 PFD 1 course knob's H-events; HDG BUG syncs the heading bug with the G3000's
  own H-event. V-2: FMS SPD and MAN SPD press the SF50's
  FMS and manual speed mode buttons (every press writes 1), each lit from its own B-var: the two B-vars are
  exclusive and each holds its state (SCMON-SF50), so the active mode's key is lit. YD toggles the yaw damper
  by the standard event, lit from `AUTOPILOT YAW DAMPER`. V-3: the HDG, CRS, ALT, VS and SPD step keys
  repeat while held ("Hold to repeat"); the long presses of CRS+/CRS- (the 10 degree step) and ALT+/ALT-
  (1,000 ft) are gone.
- **Trim page (V-2):** TRIM UP and TRIM DN step the elevator trim, RUD L and RUD R the rudder trim, by the
  standard events; the TRIM and RUD TRIM gauges show the trim positions from -100 to 100 percent. V-3: the
  four keys repeat while held, at most 8 s per hold.
- **Systems page (V-2):** BAT 2, GEN 1 and GEN 2 switch the second battery and the generators by the SF50's
  input events, guarded: a press writes 1 (on), a long press 0 (off), and the key is lit from the B-var. BUS V
  shows bus 1's volts, LOAD A the total electrical load. ENG KNOB shows the engine run knob (`STOP` or `RUN`),
  STARTER whether the starter runs, FUEL CTL the fuel control switch (`LEFT`, `AUTO` or `RIGHT`, V-3); these
  three do nothing on a press.
- **ICE/ENV page (V-2):** ENG IPS, WING/STAB, WSHLD and OXYGEN are guarded like BAT 2; WSHLD HI, WING LT,
  DEFOG, AFT CTL and TEMP BKUP are plain toggles (On `1` / Off `0`). Row 2 shows the sim's own ice protection
  SimVars (`ON` or `OFF`) beside the switches, so a B-var that does not move the sim's system shows. BLEED
  shows `FRESH` or `BLEED`, ECS DIS and the four ECS knobs their raw values; they do nothing on a press.
- **Engine page:** readouts only: N1 and N2 (percent), ITT (degrees Celsius), fuel flow (pounds per hour),
  ENG RUN (`RUN` while the engine runs), IGN (the ignition switch SimVar), and the left, right and total fuel
  in gallons.
- **Copied pages:** views, sim rate, V-speeds, COM pad, transponder and radios work as on the C172
  (their docs above); they use standard events, SimVars and the C172's Lua scripts, nothing C172-specific.
  V-3: the radios step keys repeat while held, and the BARO column shows the altimeter setting (1,8) and
  steps it (BARO+ 2,8, BARO- 3,8, by the standard baro events).

## Which route each key uses

The rule for the switch keys (V-1 A-5): per key, the input event list's name of its family
(`electrical_battery_*`, `lighting_nav_*`, `lighting_beacon_*`, `lighting_strobe_*`, `lighting_landing_*`,
`lighting_taxi_*`, `deice_pitot_*`; for VNV a name with `vertical_navigation` or `vnav`), as a T1 key with On
`1` / Off `0`; one match: that name; several: the lowest index (the others for V-2); none: the key keeps the
standard event and SimVar (BCN: empty when the list has no beacon).

| Key | Matches in the list | Built |
|---|---|---|
| main 1,1 `BAT` | IE-SF50 80 `B:sf50_electrical_battery_1_switch`, 81 `B:sf50_electrical_battery_2_switch`, 82 `B:sf50_electrical_battery_generator_intercept` | IE-SF50 80 (battery 1, the lowest index); 81 is V-2's systems BAT 2, 82 left for V-4 |
| main 4,1 `NAV LT` | IE-SF50 130 `B:sf50_lighting_nav_lights_intercept` | IE-SF50 130 (weak: an `_intercept` input event, V-1 A-15) |
| main 4,2 `BCN` (V-1) | none | Empty in V-1 (the SF50's flight files name no beacon either); RECOG since V-2 |
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
for those keys (V-1 A-5 covers only the switch keys and VNV); V-2 keeps them, except PARK: with the brake set,
`K:PARKING_BRAKES` from the deck released it and the SF50 set it again within about 0.1 s (SCMON-SF50), so
PARK writes IE-SF50 117 and keeps the brake SimVar as its read, as VNV keeps its L-Var.

V-2's keys use the list's SF50 input events where it has the control, the standard events where it has none:

| Key | Input event (IE-SF50 line) | Form |
|---|---|---|
| main 1,4 `PARK` | 117 `B:sf50_handling_parking_brake` | T1 with the brake SimVar read (`K:PARKING_BRAKES` failed, SCMON-SF50) |
| main 4,2 `RECOG` | 132 `B:sf50_lighting_recognition_lights_intercept` | T1 (weak: an `_intercept` input event, as NAV LT; V-2 A-4) |
| main 4,7 `ICE`, iceenv 1,3 `WING/STAB` | 78 `B:sf50_deice_wingstab` | G1 |
| iceenv 1,2 `ENG IPS` | 74 `B:sf50_deice_engine` | G1 |
| iceenv 1,4 `WSHLD` | 76 `B:sf50_deice_windshield` | G1 |
| iceenv 1,5 `WSHLD HI` | 77 `B:sf50_deice_windshield_high` | T1 |
| iceenv 1,7 `WING LT` | 41 `B:lighting_wing_1` | T1 (a generic name) |
| iceenv 3,2 `OXYGEN` | 133 `B:sf50_pressurization_oxygen_master` | G1 |
| iceenv 3,3 `BLEED` | 134 `B:sf50_pressurization_switch_air_bleed` | T3 readout (V-2 A-7) |
| iceenv 3,4 `ECS DIS` | 66 `B:sf50_cabin_ecs_disable` | T3 readout (V-2 A-7) |
| iceenv 3,5 `DEFOG`, 3,6 `AFT CTL`, 3,7 `TEMP BKUP` | 65, 64, 69 `B:sf50_cabin_ecs_defog`, `_aft_control`, `_temp_backup` | T1 |
| iceenv 4,2 to 4,5 (ECS knobs) | 71, 70, 68, 67 `B:sf50_cabin_ecs_temp_knob_forward`, `_temp_knob_aft`, `_fan_knob_forward`, `_fan_knob_aft` | T3 readouts (knob steps unknown, V-4) |
| systems 1,2 `BAT 2` | 81 `B:sf50_electrical_battery_2_switch` | G1 |
| systems 1,3 `GEN 1`, 1,4 `GEN 2` | 83, 84 `B:sf50_electrical_gen_1_switch`, `_gen_2_switch` | G1 |
| systems 2,2 `ENG KNOB` | 86 `B:sf50_engine_run_knob` | T3 readout (V-2 A-7, A-8) |
| systems 2,4 `FUEL CTL` | 114 `B:sf50_fuel_control_knob` | T3 readout (V-2 A-7, A-8) |
| autopilot 1,7 `FMS SPD`, 4,7 `MAN SPD` | 53, 58 `B:sf50_autopilot_fms_speed_mode`, `_man_speed_mode` | T1-set (V-2 A-5) |
| autopilot 2,7 `YD` | none (the list has no yaw damper control) | T2 `K:YAW_DAMPER_TOGGLE` (weak, V-2 A-9) |
| main 3,6 `BARO` long press | none used (29 `B:autopilot_baro_1_sync` is the fallback) | `K:BAROMETRIC_STD_PRESSURE` (V-2 A-10) |
| trim 3,6 `RUD L`, 3,8 `RUD R` | none used (35 `B:handling_ruddertrim_1` is the fallback) | T5 K-events as the C172 (V-2 A-11) |

V-3's step keys (H1) send the same events as before, now from the script `XL24-SF50.lua`: key down runs
`lua:XL24-SF50:HOLD(n)`, key up `lua:XL24-SF50:RELEASE(n)`, and the script's key table gives the event for
the code n. The new BARO+ and BARO- send the standard baro events; the SF50's own baro knob input event
(IE-SF50 28 `B:autopilot_baro_1`) is not used, its values are unknown (V-3 A-7).

| Codes | Keys | Event the script sends |
|---|---|---|
| 1, 2 | autopilot 2,2 `HDG+`, 4,2 `HDG-` | `K:HEADING_BUG_INC`, `K:HEADING_BUG_DEC` (SDK-APE) |
| 3, 4 | autopilot 2,3 `CRS+`, 4,3 `CRS-` | `H:AS3000_PFD_1_CRS_INC`, `H:AS3000_PFD_1_CRS_DEC` (WT-G3000H; weak, V-1 A-15) |
| 5, 6 | autopilot 2,4 `ALT+`, 4,4 `ALT-` | `K:AP_ALT_VAR_INC`, `K:AP_ALT_VAR_DEC` (SDK-APE) |
| 7, 8 | autopilot 2,5 `VS+`, 4,5 `VS-` | `K:AP_VS_VAR_INC`, `K:AP_VS_VAR_DEC` (SDK-APE) |
| 9, 10 | autopilot 2,6 `SPD+`, 4,6 `SPD-` | `K:AP_SPD_VAR_INC`, `K:AP_SPD_VAR_DEC` (SDK-APE) |
| 11, 12 | radios 2,8 `BARO+`, 3,8 `BARO-` | `K:KOHLSMAN_INC`, `K:KOHLSMAN_DEC` (SDK-INSTE; weak on the G3000, V-3 A-7) |
| 13 to 18 | radios 2,2 to 2,7 (NAV1, NAV2, COM2 `MHZ+` / `KHZ+`) | `K:NAV1_RADIO_WHOLE_INC`, `K:NAV1_RADIO_FRACT_INC`, `K:NAV2_RADIO_WHOLE_INC`, `K:NAV2_RADIO_FRACT_INC`, `K:COM2_RADIO_WHOLE_INC`, `K:COM2_RADIO_FRACT_INC` (SDK-RADE) |
| 19 to 24 | radios 3,2 to 3,7 (NAV1, NAV2, COM2 `MHZ-` / `KHZ-`) | the same six with `_DEC` (SDK-RADE) |
| 25, 26 | trim 2,2 `TRIM UP`, 4,2 `TRIM DN` | `K:ELEV_TRIM_UP`, `K:ELEV_TRIM_DN` (SDK-FCE) |
| 27, 28 | trim 3,6 `RUD L`, 3,8 `RUD R` | `K:RUDDER_TRIM_LEFT`, `K:RUDDER_TRIM_RIGHT` (SDK-FCE) |

## Hold to repeat

V-3, at the user's request: the step keys repeat while held, so a long bug, frequency or trim change is one
press instead of many. PilotsDeck has no repeat for keys (PD-HOLD): a key sends its command once, and a long
press (half a second or more) sends a second command once; its only repeat setting, `TickDelay`, is for the
dials of the Stream Deck +, and the Stream Deck app tells a plugin only key down and key up (ELG-SDK). So the
repeat runs in this profile's own script, `Scripts/XL24-SF50.lua`, with no change to the repo's tools.

**How it works.** Each step key is a Simple Button with **Hold Switch** on and the command type Lua Function:
key down runs `lua:XL24-SF50:HOLD(n)`, key up `lua:XL24-SF50:RELEASE(n)` (README 2.1.2: with Hold Switch "The
normal Command will be sent on KeyDown and the alternate Command on KeyUp"). n is the key's code in the
script's key table ("Which route each key uses"). PilotsDeck runs each Lua call on its own task, and `Sleep`
pauses only that task (PD-HOLD; README 3.5: "The execution won't block anything."), so HOLD can wait in a
loop while RELEASE runs. `XL24-SIMRATE.lua` already waits in a loop with `Sleep` on this PC (PD-LOG2); two
calls of one script at once are a hand test (V-3 A-14). The times below count 50 ms sleeps, so the real
times can run a little longer, and the sim itself may speed up repeated trim events (SDK-FCE).

- **A short press** sends one step at key down, as the key did before.
- **Held**, the key waits its delay, then sends more steps, faster the longer it is held (table below).
- **It stops** at key up (within about 50 ms), at the key's step cap, or after about 20 s held, whichever
  comes first. If a key up never reaches the script (for example when the page changes while the key is
  held), the repeat runs on after the release until the cap or the 20 s limit ends it (trim: about 8 s); the
  next press of that key resyncs its count. Change pages only with no step key held.
- **No long press any more on CRS and ALT** (V-3 A-5): CRS+/CRS- had the long press `K:VOR1_OBI_FAST_INC` /
  `_DEC` and ALT+/ALT- `K:AP_ALT_VAR_INC:1000` / `_DEC:1000`. A key with Hold Switch can't have a long press
  command (README 2.1.2), so they are gone; holding CRS or ALT speeds up instead.
- The step keys show fixed images; the readouts beside them (autopilot row 3, radios row 1, the trim gauges)
  show the sim's values, so a step the aircraft ignores shows as a readout that does not move.
- The script writes no variable and sends only the events of its key table (K-events and the G3000 CRS
  H-events, V-3 A-10); it does not check which aircraft is loaded (V-3 A-12).

| Profile | Keys | Delay | Then (from the end of the delay) | Cap per hold (the first step counts) |
|---|---|---|---|---|
| fast | HDG, CRS, SPD, the KHZ keys | 400 ms | 10 steps/s to 1.5 s, 20/s to 3 s, then 60/s (3 per 50 ms) | HDG, CRS 360; SPD, KHZ 200 |
| alt | ALT | 400 ms | 10/s to 1.5 s, then 20/s | 400 |
| slow | VS, the MHZ keys | 400 ms | 6.7/s (one per 150 ms) | VS 40, MHZ 30 |
| baro | BARO+, BARO- | 400 ms | 10/s to 2 s, then 20/s | 200 |
| trim | TRIM UP, TRIM DN, RUD L, RUD R | 250 ms | 20/s, no speed-up | 160 (8 s) |

For HDG with 1 degree steps: held 1 s about 8 degrees, 3 s about 40, 4.3 s about 100; the 360 cap comes at
about 8.6 s. These are working values (V-3 A-4): if the repeat is too slow or too fast, only the script's
`PROFILES` and `KEYS` tables change. Fallbacks (V-3 A-2, A-3; not built): a global script with `RunInterval`
that sends the repeats while an internal variable says a key is held; else no repeat and a long press that
sends a five-step burst ("Fallbacks").

## Guarded keys

- **GEAR** and **TOGA** are readouts: the gear lever, the emergency gear drop and the throttle's TOGA button
  stay in the cockpit (V-1 A-8).
- No key starts or stops the engine, switches the ignition, the fuel selector or the fuel cut-off: the engine
  page is readouts only. V-2: ENG KNOB (engine run/stop), STARTER, FUEL CTL (the fuel selector), BLEED (air
  source), ECS DIS and the four ECS knobs are readouts too (V-2 A-7, A-8).
- No **CAPS** (parachute) and no **Safe Return** (emergency autoland) key or readout on any page (V-1 A-7),
  though the list names their input events (IE-SF50 72, 73, 135, 136). No engine start, stop or abort key
  (IE-SF50 87 and the run knob) and no gear lever key.
- **G1, press on, long press off (V-2 A-6, A-8):** BAT 2, GEN 1, GEN 2, ENG IPS, WING/STAB and main ICE,
  WSHLD, OXYGEN. A short press always writes 1, so it can never switch one of them off; only a long press
  (half a second or more) writes 0.
- Plain toggles (benign): WSHLD HI, WING LT, RECOG, DEFOG, AFT CTL, TEMP BKUP.
- BAT and A/T are plain toggles, as their cockpit switches: press them in flight only on purpose (V-1's BAT
  stays a toggle, V-2 A-8).
- **Hold to repeat only on benign steps (V-3 A-6):** the reference bugs (HDG, CRS, ALT, VS, SPD), the radio
  steps, BARO+/- and the trim keys, each capped and stopped on release; trim repeats like a held trim switch,
  at most 8 s per hold. Never repeat: FLAPS, the sim rate keys, gear, the AP mode keys, the B-var switches,
  the G1 keys, the COM and XPDR pads, PARK.

## What each key holds

The key kinds of [phase2-main-page.md](phase2-main-page.md), "What each key holds": every key is a copy of a
real saved key with only the listed fields changed (the generator does this).

| Kind | Action, copied from | Keys here |
|---|---|---|
| T1 B-Var switch | Dynamic Button, the Phase 1 BAT key (`p1:0,0`): Command Address and Value Address a `B:` input event, On `1` / Off `0`, Special State on | main 1,1, 4,1, 4,3, 4,4, 4,6; autopilot 1,8 (Value Address the L-Var); V-2: main 1,4 (Value Address the brake SimVar), 4,2; iceenv 1,5, 1,7, 3,5 to 3,7 |
| T2 K-event mode | Dynamic Button, the Phase 1 AP key (`p1:3,0`): Command Address a `K:` event, Value Address a SimVar | main row 2, 4,5; autopilot 2,7 (V-2), 2,8, 3,7 and the C172's mode keys |
| T3 Display Value | the Phase 1 RPM key (`p1:2,0`): Value Address, Format, Mappings; command none or a press command | main 1,2, 1,5, 1,6, 3,2, 3,5, 3,6; autopilot 3,2, 3,3, 3,8, 4,8; engine; V-2: systems 1,6, 1,8, 2,3; iceenv row 2; V-3: radios 1,8 |
| T4 COM Radio | `com_radio` (templates.json) | main 3,1 and the copied pages' radio keys |
| T5 Simple Button | `simple_button` with the AP key's states | main 3,3, 3,4 (until V-3 also the autopilot, radios and trim step keys, now H1) |
| H1 hold to repeat (V-3) | as T5, with the command type Lua Function (14), Command `lua:XL24-SF50:HOLD(n)`, alternate command (`AddressActionOff`) `lua:XL24-SF50:RELEASE(n)`, Hold Switch on and no long press (README 2.1.1, 2.1.2; the saved `simple_button` template holds `HoldSwitch` and `AddressActionOff`) | autopilot 2,2 to 2,6, 4,2 to 4,6; radios 2,2 to 2,8, 3,2 to 3,8; trim 2,2, 4,2, 3,6, 3,8 |
| T1-set (V-2) | as T1, with On `1` / Off `1`: every press writes 1 (the C172 fuel selector form, [phase3-systems.md](phase3-systems.md)) | autopilot 1,7, 4,7 |
| G1 guard (V-2) | as T1-set, plus a long press: Long Press on, Second Command type B-Var (13), the same `B:` address, Long On `0` / Off `0` (`SwitchOnStateLong` / `SwitchOffStateLong`, PD-LONG), so a long press writes 0 | main 4,7; systems 1,2 to 1,4; iceenv 1,2 to 1,4, 3,2 |
| T3 with a B-var read (V-2) | as T3, with "Run as Command" unchecked (saved `DoNotRequestBvar: false`, the A32NX NAV LOGO form) so the B-var is read as a value | systems 2,2, 2,4; iceenv 3,3, 3,4, row 4 |
| T9 Display Gauge | `display_gauge` (templates.json) | trim 3,4 (elevator, vertical), 3,7 (rudder, horizontal, center line) |

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

The four `H:` commands (autopilot CRS+ and CRS-, which the script sends since V-3, CRS1 and the HDG BUG
press) go through the MobiFlight WASM
module: "PilotsDeck sends every H-event and all calculator code through the MobiFlight WASM module"
([troubleshooting.md](troubleshooting.md#the-mobiflight-wasm-module)). It is installed on this PC
([installation.md](installation.md)); those docs do not list these keys yet (V-1 A-20). Without the module
those four commands do nothing; their readouts and every other key do not need it (CRS+ and CRS- have no
long press since V-3).

## What the keys show when the SF50 isn't there

- No sim, or no flight: PilotsDeck's own idle and waiting images, as on the other profiles.
- Another aircraft: the SimVar keys show that aircraft's own values; `L:XMLVAR_VNAVButtonValue` and
  `L:WT_TOGA_ACTIVE` read 0 or that aircraft's value. BAT, NAV LT and LDG use input events only the SF50 has
  (`sf50_` names) and read nothing there. STRB (`lighting_strobe_1`) and PITOT (`deice_pitot_1`) use generic
  names that other aircraft can have too: the 2024 C172 has `deice_pitot_1`
  ([reference/InputEvents-C172-G1000.txt](reference/InputEvents-C172-G1000.txt), line 139), so in the C172
  PITOT shows and switches the C172's pitot heat.
- **Keys act on any aircraft that has their event:** the TAXI, FLAPS, AP mode, A/T, LVL and radio keys
  (standard events) and STRB and PITOT (generic input events) move the loaded aircraft's own controls where it
  has them. Keep the profile on the SF50 with the Profile Manager mapping and do not press the light, PITOT,
  FLAPS, AP or A/T keys in another aircraft.
- V-2: every `sf50_` key on systems, ICE/ENV and the autopilot (FMS SPD, MAN SPD), and main RECOG and ICE,
  read nothing in another aircraft (Off image or Special State; readouts a blank or `0`). PARK writes the
  SF50's own input event: in another aircraft it shows that aircraft's parking brake, but a press does
  nothing. WING LT (`lighting_wing_1`) is a generic name: it is not in the C172's list, but other aircraft
  may have it and then it switches their wing light. YD (`K:YAW_DAMPER_TOGGLE`), the BARO long press
  (`K:BAROMETRIC_STD_PRESSURE`) and the rudder trim keys (`K:RUDDER_TRIM_LEFT` / `_RIGHT`) are standard
  events and act on any aircraft: do not press them in another aircraft. The SimVar readouts (bus volts, load,
  starter, ice protection, yaw damper, rudder trim) show that aircraft's own values.
- V-3: the step keys (HDG, CRS, ALT, VS, SPD, the radio MHZ and KHZ keys, BARO+/-, the trim keys) send
  standard events from the script and act on any aircraft, one step per press and repeating while held, as
  their V-2 forms did once per press; CRS needs the G3000 and does nothing elsewhere. The script does not
  check the aircraft (V-3 A-12). Radios 1,8 BARO shows that aircraft's altimeter setting.
- If the SF50 ignores a standard event, the key's read stays where it was and the key stays dark: the hand
  test records it.

## Not on these pages, and why

V-2 added the systems and ICE/ENV pages, RECOG, ICE, BARO STD, FMS SPD, MAN SPD, YD and the rudder trim keys;
V-3 hold to repeat, the BARO column and FUEL CTL's words. Left for a later unit, **V-4** (V-2 A-1, A-12; V-3
A-1), because the values they take are not known yet (sim checks first):

- **The GTC page** (proposed at MORE 1,2): the SF50's touch controllers take input events (IE-SF50 3 to 26),
  not the WT G3000 H-events of the research doc, and the knob values per step are unknown.
- **The checklist wheel** (IE-SF50 1, 2).
- **Writes for the ECS knobs, the fuel control and the engine run knob** (their positions; one key per
  position after the sim check, V-2 A-7): V-2 shows them as readouts.
- **IE-SF50 82** `sf50_electrical_battery_generator_intercept` (systems 1,5): what it switches is unknown.
- **Windshield MAX** (ICE/ENV 1,6): the cockpit button is held to dispense fluid (SF50-PKG, SF50-CHK line
  4163); which input event it drives and its values are unknown. A key with Hold Switch could hold it (README
  2.1.2: the On value at key down, the Off value at key up).
- **Battery amps** (systems 1,7): which battery index the SF50's switches drive is open (V-2 A-3).

Never on these pages:

- **PFD and MFD softkey pages** (MORE 1,2 and 1,3 stay empty): IE-SF50 lists softkeys only on the GTCs; the
  SF50's PFD and MFD have none.
- **CAPS and Safe Return** (V-1 A-7), **engine start and stop keys** (V-2 A-8), the gear lever.
- **BC** (autopilot 1,7 is FMS SPD now): IE-SF50 has no back course control (V-2 A-9).
- **Main 1,3** (fuel pump: the SF50 has none) and **aileron trim** (trim 2,6 to 2,8: the SF50 has none).
- A beacon light: the SF50 has none (main 4,2 is RECOG).

## Fallbacks

Use one only if the checklist shows the main route does not work, and say which one you used. None is tested.
A key that fails with no working fallback becomes a readout (command none) or Empty, and its row in
aircraft-mappings.md says "does not work".

| Key | If it fails | Fallback | Source |
|---|---|---|---|
| BAT, NAV LT, STRB, LDG, PITOT (V-1 A-5) | The B-var write does nothing, or the key does not follow the cockpit switch | The standard event with the SimVar read, as TAXI: `K:TOGGLE_NAV_LIGHTS` / `(A:LIGHT NAV, Bool)`, `K:STROBES_TOGGLE` / `(A:LIGHT STROBE, Bool)`, `K:LANDING_LIGHTS_TOGGLE` / `(A:LIGHT LANDING, Bool)`, `K:PITOT_HEAT_TOGGLE` / `(A:PITOT HEAT, Bool)`; BAT Empty | SDK-ELECE, SDK-SYSV, SDK-AMISCE |
| NAV LT (V-1 A-15) | The `_intercept` input event does not move the switch | As the row above | IE-SF50 130 |
| TAXI (V-1 A-15) | The K-event changes nothing or not the cockpit switch | Empty (the list has no taxi light) | |
| PARK (V-2) | The B-var write does not move the brake, or the key does not follow the handle | Readout only (command none), the read as now; `K:PARKING_BRAKES` failed in the SF50 (SCMON-SF50) | IE-SF50 117 |
| VNV (V-1 A-9) | The B-var press does nothing | The L-Var write `L:XMLVAR_VNAVButtonValue`, On `1` / Off `0`; else readout only, Mappings `0=OFF:1=ON` | HH-MS |
| CRS+, CRS-, CRS1 (V-1 A-15) | The H-event does nothing (the SF50 has no PFD bezel knob) | CRS+/CRS- go back to V-2's form with the long press `K:VOR1_OBI_FAST_INC` / `_DEC`; CRS1 a readout | WT-G3000H; SDK-RADE |
| HDG BUG (V-1 A-15) | The press does not sync the bug | `K:AP_HDG_CURRENT_HDG_SET`, as the C172 | SDK-APE |
| TOGA (V-1 A-15) | The readout never shows `TO/GA` | `(A:AUTOPILOT TAKEOFF POWER ACTIVE, Bool)` | SDK-APV |
| A/T (V-1 A-8) | A stronger guard is wanted | Readout only (command none) | |
| BARO (V-1 A-15) | `K:BAROMETRIC` does nothing on the G3000 | the long press STD (V-2) | HH-MS |
| BARO long press (V-2 A-10) | `K:BAROMETRIC_STD_PRESSURE` does not set 29.92 | The long press `B:autopilot_baro_1_sync`, On `1` / Off `1`; else no STD | IE-SF50 29, HH-MS |
| G1 keys (V-2 A-6) | The long press does not write 0 | Every G1 key a readout of its B-var (command none), Mappings `0=OFF:1=ON` | PD-LONG |
| BAT 2, GEN 1, GEN 2, the IPS keys, OXYGEN (V-2 A-2) | The B-var does not follow the cockpit switch | The ice keys: a readout of their row 2 SimVar; the others Empty, recorded "does not work" | SDK-ENGV, SDK-SYSV |
| RECOG (V-2 A-4) | The `_intercept` input event does not move the switch | Empty (no other recognition light name is firm) | IE-SF50 132 |
| FMS SPD, MAN SPD (V-2 A-5) | The write does nothing (the B-vars hold their state, SCMON-SF50) | Empty | IE-SF50 53, 58 |
| YD (V-2 A-9) | `K:YAW_DAMPER_TOGGLE` does nothing | Readout only (command none) | SDK-APE |
| RUD L, RUD R (V-2 A-11) | The K-events do not move the SF50's rudder trim | `B:handling_ruddertrim_1` after the sim check's values | IE-SF50 35 |
| Systems 1,7 (V-2 A-3; V-4) | After the sim check names the battery index | `BATT A` `(A:ELECTRICAL BATTERY LOAD:<n>, Amperes)`, Format `1.1` | SDK-ELECV |
| Main ICE (V-2 A-13) | A folder is wanted instead of the key | Main 4,7 opens iceenv and MORE 2,4 stays Empty | |
| ENG KNOB, BLEED, ECS DIS, FUEL CTL, knobs (V-2 A-7; V-3 A-8) | The Mappings or numbers are wrong (FUEL CTL's `0=LEFT:1=AUTO:2=RIGHT` is an inference) | Mappings from the sim check; one key per position in V-4 | SF50-FLT; SF50-CHK |
| Hold to repeat (V-3 A-2) | The keys do not repeat, or a repeat runs on after release | R1 (not built): the keys keep Hold Switch, HOLD and RELEASE only set an internal `X:` variable, and a global script (`Scripts/global/`, `RunInterval`) sends the repeats; if that fails too: the row below | PD-HOLD |
| Hold to repeat (V-3 A-3) | No route repeats | The step keys go back to their V-2 form plus a long press that sends a five-step burst (not built) | PD-HOLD |
| Repeat speed (V-3 A-4) | Too slow or too fast | Only the script's `PROFILES` and `KEYS` values change | |
| CRS and ALT long press (V-3 A-5) | The user wants the long presses back | CRS+/CRS- and ALT+/ALT- without hold to repeat, as V-2 | |
| Trim repeat (V-3 A-6) | Repeating trim is not wanted | The four trim keys go back to V-2's one-step keys | |
| BARO+, BARO- (V-3 A-7) | `K:KOHLSMAN_INC` / `_DEC` do nothing on the G3000 | `H:AS3000_PFD_1_BARO_INC` / `_DEC` in the script's key table (not rechecked); else the column is Empty | WT-G3000H |
| FLAPS (V-1 A-15) | The number per detent is unclear | Mappings after the test | |
| Views, XPDR (V-1 A-14) | The A-Var writes do nothing on the SF50 | Those five keys become their readouts (command none) | |

Also hand-test items with no fallback yet (V-1 A-15): LVL and A/T (SDK only), fuel in gallons, ITT in
Celsius, IGN under the FADEC, the C172's V-speed SimVars on a jet, and the COM pad on the G3000.

## How to test

Run [tests/manual-checklist.md](../tests/manual-checklist.md), sections "VisionJet SF50 profile (V-1)",
"VisionJet SF50 profile (V-2)" and "VisionJet SF50 profile (V-3)". As on
the other profiles, check both directions: press a key and watch the cockpit, then **work the control in the
cockpit with the mouse and check that the key follows without a key being pressed.** Never press GEAR or TOGA
expecting an action (they are readouts). Record which battery BAT moves, the value each B-var reads, the flap
number per detent, and every key the G3000 ignores. V-2: record the value each new B-var reads per cockpit
position, whether a long press switches each G1 key off, and which battery and generator index BAT 2, GEN 1
and GEN 2 move. Some SF50 B-vars read 0 for up to about 30 s after the profile loads (SCMON-SF50): wait until
the keys show the cockpit state before you judge them. PARK (V-2) writes the parking brake input event: press
it with the brake set and with it released, and work the handle with the mouse. V-3: hold each step key for
1, 3 and 10 s and check that the repeat stops at once on release and never runs on; record the step per press
of ALT and BARO+/-, whether the G3000 PFD's baro follows BARO+/-, and the word FUEL CTL shows per position.

## When it passes

1. Any change found in the test goes into `tools/profilegen/visionjet-sf50.json` and this doc; then the
   profile is regenerated (not exported from the app) and imported again.
2. Fill in the "Verified" column of the rows in aircraft-mappings.md ("Cirrus Vision SF50 (MSFS 2024 default,
   V-1)", "(MSFS 2024 default, V-2)" and "(MSFS 2024 default, V-3)") with the date, sim version and SF50
   preset, for each function that passed; mark a row "does not work" where a key failed.

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
| SDK-FCE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-flight-control-events/ (`FLAPS_INCR`, `FLAPS_DECR`; the trim page's `ELEV_TRIM_UP`, `ELEV_TRIM_DN`, `RUDDER_TRIM_LEFT`, `RUDDER_TRIM_RIGHT` as [phase2-trim-views.md](phase2-trim-views.md)) |
| SDK-CTLV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-control-variables/ (`FLAPS HANDLE INDEX`, number; the trim page's `ELEVATOR TRIM PCT EX2`, `RUDDER TRIM PCT` as [phase2-trim-views.md](phase2-trim-views.md)) |
| SDK-RADV, SDK-RADE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-radio-navigation-variables/ (`NAV OBS`), https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-radio-navigation-events/ (`VOR1_OBI_FAST_INC/DEC`) |
| SDK-UNITS | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/simulation-variable-units/ |
| WT-G3000H | MSFS Avionics Framework docs (2024), G3000 H event list, https://microsoft.github.io/msfs-avionics-mirror/2024/docs/avionics/g3000/h-event-list (`AS3000_PFD_[index]_CRS_INC`, `_CRS_DEC`, `_CRS_PUSH`, "[index] is the instrument index of the PFD (1 or 2)"; `Garmin_AP_HDG_Sync` "Autopilot selected HDG sync."), read 2026-11-16 |
| HH-MS | HubHop presets for "Cirrus SF50 Vision Jet (MSFS2024)" (vendor Microsoft), https://hubhop.mobiflight.com/presets/?aircraft=Cirrus+SF50+Vision+Jet+%28MSFS2024%29, read 2026-11-16 (for V-0): `L:WT_TOGA_ACTIVE` ("TOGA annunciator"), the VNAV toggle `(L:XMLVAR_VNAVButtonValue) ! (>L:XMLVAR_VNAVButtonValue)` |
| FORUM-24 | Official forum thread on the MSFS 2024 SF50, https://forums.flightsimulator.com/t/msfs2024-cirrus-sf50-vision-jet/664507 (the SF50 has an autothrottle), read 2026-11-16 |
| V-1 A-n | The ASSUMPTIONS of this profile's unit (V-1), ruled 2026-11-16: A-5 switch keys from the input event list, A-7 no CAPS or Safe Return, A-8 guards, A-9 VNV L-Var write, A-14 the copied A-Var writes, A-15 weak sources, A-20 the MobiFlight note |
| V-2 A-n | The ASSUMPTIONS of V-2, ruled 2026-11-16: A-1 the V-2 / V-3 split, A-2 B-var to SimVar links unknown, A-3 battery and generator indexes, A-4 RECOG, A-5 FMS/MAN SPD, A-6 the G1 guard, A-7 multi-position controls as readouts, A-8 guards, A-9 YD (no BC), A-10 BARO STD, A-11 rudder trim, A-12 GTC and softkeys, A-13 main ICE, A-14 the MORE folders, A-16 no A-Var or L-Var write, A-17 no new script, A-21 weak sources |
| PD-LONG | PilotsDeck source at commit 11bdf1f7daf4828f822c18919952fe5b66153e58 (master, "Push Build" 2026-10-30, the 0.9.7 build of [installation.md](installation.md); no v0.9.7 tag exists), https://github.com/Fragtality/PilotsDeck, read 2026-11-16: `Plugin/Actions/Simple/ActionCommand.cs` lines 189 to 207 (`CreateLong`: a B-var value command gets `new(... settingsModel.SwitchOnStateLong, settingsModel.SwitchOffStateLong, command)`, `ToggleSwitch = false`), `Plugin/Actions/Simple/ValueState.cs` lines 286 to 321 and `Plugin/Actions/ToolsValueState.cs` lines 9 to 17 (the value written: Off, or On when the read equals Off, so `0` with both `0`), `Plugin/Simulator/SimCommand.cs` lines 66 to 69 (a B-var is a value command when `DoNotRequestBvar` is false), `Plugin/Actions/Simple/ActionBaseSimple.cs` lines 548 to 561 (a long press runs the long command when the main command is not holdable) |
| SDK-INSTE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-instrumentation-events/ (`BAROMETRIC_STD_PRESSURE` "Set the altimeter setting to ... 1013.25 hPa", "[0]: the index of the altimeter"), read 2026-11-16 (the C172 docs' tag, same page) |
| SDK-ELECV | The SDK electrical variables page as [phase3-systems.md](phase3-systems.md), "Sources" (`ELECTRICAL BUS VOLTAGE`, `ELECTRICAL TOTAL LOAD AMPS`) |
| SDK-FLT | https://docs.flightsimulator.com/msfs2024/retail/content-configuration/flt-files/flt-file-properties/ (`[LocalVars_EX1.N]` "can be used to define and initialise scoped local variables", with the "L:1" identifier), read 2026-11-16 |
| SF50-FLT | The SF50's flight files in `content\minimal.fsarchive` of SF50-PKG (read by search only, 2026-11-16): `[LocalVars_EX1.0]` positions and meanings (`SF50_Engine_Run_Knob_Position`, `SF50_Fuel_Control_Switch_Position`, `SF50_Engine_IP_Switch_Position`, `SF50_WingStab_IP_Switch_Position`, `SF50_Oxygen_Master_Switch_Position`, `SF50_Bleed_Air_Switch_State`, `SF50_Ecs_Temp_Knob_Forward_Position`), `[AutoPilot.0]` `YawDamper`, `[Switches.0]` `WingLights` |
| PD-HOLD | PilotsDeck README at commit 11bdf1f (https://raw.githubusercontent.com/Fragtality/PilotsDeck/11bdf1f/README.md), read 2026-11-17 (V-3): 2.1 (a Second Command when pressed 500 ms or longer, sent once), 2.1.2 (Hold Switch: the normal command on key down, the alternate command on key up; with Hold Switch no long press command), 3.5 (standard scripts in `Scripts`, their state kept while loaded), 3.5.1 (`SimCommand`, `Sleep`, `Log`), 3.5.2 (global scripts, `RunInterval`), 4.1 (`TickDelay` only between encoder ticks); and its source at 11bdf1f7daf4828f822c18919952fe5b66153e58: `Plugin/Actions/Simple/ActionBaseSimple.cs` 534 to 536, 549, 563 to 566 (a holdable command at key down, its key-up form at key up, nothing repeats), `Plugin/Simulator/SimCommand.cs` 77 to 82, 94 to 97 (a Lua Function is holdable), `Plugin/Simulator/ConnectorNone.cs` 45 to 48 (each Lua call on its own task), `Plugin/Resources/Scripts/ManagedScript.cs` 359 (`SimCommand` queues the event), 406 (`Sleep` is `Thread.Sleep`) |
| ELG-SDK | Elgato Stream Deck SDK, plugin WebSocket events, https://docs.elgato.com/streamdeck/sdk/references/websocket/plugin/ (keyDown, keyUp; dial events for the Stream Deck +; no key-held event), read 2026-11-17 (V-3) |
| SF50-CHK | The SF50's own checklist in SF50-PKG, `content\html_ui\airplanes\microsoft_sf50\checklist\checklist.xml` (read by search only, 2026-11-17, V-3): line 1448 (fuel control switch "CHECK LEFT/AUTO/RIGHT"), line 4163 (windshield IPS MAX switch, press and hold); no variable names |
| PD-LOG2 | The plugin logs `PilotsDeck20261116.log` and `PilotsDeck20261117.log` (read only, searched, 2026-11-17, V-3): the V-1 keys sent in the SF50 on 2026-11-16 (HDG+ 6 and HDG- 16 times about 0.2 s apart, 20:29:10 to 20:29:21; ALT+ 24 times and its long press once, 22:53:13 to 22:53:21; CRS+ and its long press once); `lua:xl24-simrate:SET(1)` then `K:SIM_RATE_DECR` twice about 0.1 s apart (20261117.log lines 120 to 123). Leads only, never a test pass |
| V-3 A-n | The ASSUMPTIONS of V-3, ruled 2026-11-17: A-1 the V-3 / V-4 split, A-2 Hold Switch and a script loop (the step cap and the 20 s limit always end it), A-3 the long press burst fallback, A-4 speed profiles, A-5 the CRS and ALT long presses go (the user's answer), A-6 repeat only on benign steps, A-7 BARO+/- by `KOHLSMAN_INC` / `_DEC`, A-8 FUEL CTL Mappings, A-9 no tool change, A-10 events only, A-11 README, A-12 no aircraft check, A-13 sim answers later as a repair, A-14 weak sources |
| SCMON-SF50 | A `tools/scmon` capture with the SF50 loaded (2026-11-16, MSFS 2024, version not recorded): a local copy of the tool that also read the SF50's B-vars through PilotsDeck's local API (read only) while the user worked the cockpit controls with the mouse. The values each B-var took are in [aircraft-mappings.md](aircraft-mappings.md), "Cirrus Vision SF50 (MSFS 2024 default, V-2)". With the brake set, `K:PARKING_BRAKES` from the deck moved `BRAKE PARKING POSITION` from 1 to 0 and back to 1 within about 0.1 s while `B:sf50_handling_parking_brake` stayed 1; the cockpit handle moved the B-var between 0 and 1 and the SimVar followed it |

V-2 rechecked at their pages on 2026-11-16 (the brief writer): SDK-APE (`YAW_DAMPER_TOGGLE` "Toggles yaw
damper on/off"), SDK-APV (`AUTOPILOT YAW DAMPER` "Yaw damper active"), SDK-SYSV (`STRUCTURAL DEICE SWITCH`,
`WINDSHIELD DEICE SWITCH`), SDK-ENGV (`ENG ANTI ICE`, `GENERAL ENG STARTER`), README (2.1, 2.1.1, 2.1.2).
V-3 rechecked at their pages on 2026-11-17 (the brief writer): SDK-APE (`HEADING_BUG_INC` "Increments heading
hold reference bug", `_DEC`, `AP_ALT_VAR_INC` "Increments the reference altitude.", `AP_VS_VAR_INC`,
`AP_SPD_VAR_INC` and their `_DEC` forms; no step sizes), SDK-INSTE (`KOHLSMAN_INC` "Increments altimeter
setting.", `KOHLSMAN_DEC`, no parameter).

Tags of the rows copied from the C172 docs, as those docs define them (each doc's "Sources"):

| Tag | Source |
|---|---|
| SDK-APT, SDK-AS1000, SDK-MISCE, SDK-CAMV, SDK-FMV, SDK-ENVV, SDK20-CTLV | The SDK pages named in [phase3-autopilot.md](phase3-autopilot.md), [phase2-sim-rate.md](phase2-sim-rate.md), [phase2-main-page.md](phase2-main-page.md), [phase2-trim-views.md](phase2-trim-views.md) and [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md), "Sources" |
| AM | [aircraft-mappings.md](aircraft-mappings.md): verified on the 2024 C172 (2026-11-11), not on the SF50 |
| IE n (no "SF50") | [reference/InputEvents-C172-G1000.txt](reference/InputEvents-C172-G1000.txt), line n: the C172's list, not the SF50's |
| PD-SRC, P2-6 route ruling | As [phase2-sim-rate.md](phase2-sim-rate.md) and [phase2-com1-pad.md](phase2-com1-pad.md), "Sources" |
| JIBLET, FORUM | As [phase3-autopilot.md](phase3-autopilot.md), "Sources" (leads only) |
| A-4, A-5, A-6, A-9 (in copied autopilot rows) | [phase3-autopilot.md](phase3-autopilot.md), "Open points" |
