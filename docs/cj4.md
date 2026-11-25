# Citation CJ4 profile (MSFS 2024 default Cessna Citation CJ4)

**Status: generated (CJ-1), not yet sim-tested; 15 pages, 195 keys.** The profile `MSFS2024 CJ4` is built by
the generator, but nothing on it has been tried in the app or the sim yet. Every name below is recorded as
"Unverified" in [aircraft-mappings.md](aircraft-mappings.md) ("Cessna Citation CJ4 (MSFS 2024 default,
CJ-1)") until the checks in [tests/manual-checklist.md](../tests/manual-checklist.md), section "Citation CJ4
profile (CJ-1)", pass.

Goal: a first useful profile for the Cessna Citation CJ4 that comes with MSFS 2024 (the default aircraft, no
add-on or mod). It uses the C172 G1000 profile's main page grid and folder positions where the function
applies ([navigation.md](navigation.md), "Pages": "a later aircraft uses this grid and these folder
positions where the function applies"): 15 pages, 195 keys. Every readout and lit key shows the sim's own
value, except the two pads' ENTRY readouts and the COM pad's digit and CLR lights: they show only what the
script holds or took ("COM pad: centered text and press feedback"). No key assumes its press worked.

**Built without the CJ4's input event list.** PilotsDeck writes that list (`InputEvents.txt`) when a flight
in the aircraft loads, and no CJ4 flight has been loaded with it yet (sim step S-1 of
[cj4-research.md](cj4-research.md)). So the profile uses the standard SDK events and SimVars only, 22 switch
keys use a standard event where the cockpit switch is likely an input event ("Which route each key uses"),
and eight positions without a name or a function are empty ("Not on these pages, and why").

Research and the candidate names: [cj4-research.md](cj4-research.md), whose draft layout has 20 pages; this
is its first part. The data file is `tools/profilegen/cj4.json`; the key tables below are the reference, and
`python tools/profilegen/check.py tools/profilegen/cj4.json` compares the profile with them key by key. The
sim rate, COM pad and transponder pages call the C172's scripts `XL24-SIMRATE.lua`, `XL24-COMPAD.lua` and
`XL24-XPDRPAD.lua`; this profile's own script `XL24-CJ4.lua` (in the package's `Scripts` folder) runs hold
to repeat ("Hold to repeat"). The COM pad also needs the package's image `Images/XL24-PadLit.png`.

Nothing in this profile uses keyboard bindings, vJoy or anything tied to a controller: the keys send
standard SimConnect events and Lua functions, write two SimVars (the camera state and the transponder
state), and read SimVars and PilotsDeck's internal variables, so they work the same with the Xbox Elite
controller and the T.16000M + TWCS. No key uses an H-event, so the profile does not need the MobiFlight WASM
module.

## What the CJ4's files and the plugin log show

- **Plugin folder and log** (looked at on 2026-11-24): no `InputEvents.txt` in PilotsDeck's plugin folder,
  and no PilotsDeck log there names the CJ4. So no input event (B-var) name and no aircraft string of the
  CJ4 is known (S-1).
- **Package** ([cj4-research.md](cj4-research.md), "Is a CJ4 installed"): the default CJ4 is in the sim's
  streamed-package cache on the development PC; its systems files are packed and only its checklist file can
  be read.
- **Checklist file** (CKL): it names the cockpit controls, never a variable, for example the battery switch
  (CKL 7), the emergency lights switch (CKL 11), the standby flight display switch (CKL 15), the avionics
  switch (CKL 19), the climate control selector (CKL 55), an engine starter and a run/stop button (CKL 66,
  70), external power (CKL 86), a pass lights safety button (CKL 105), engine-only anti-ice (CKL 129), the
  ice protection system (CKL 191), pitot/static heat buttons (CKL 239), the yaw damper (CKL 285), a landing
  lights button (CKL 301) and a fuel transfer selector (CKL 366).
- **Avionics: open.** The research page takes them as likely of the WT21 type; no source read says so for
  the default CJ4 (sim step S-4 settles it). No key here uses a WT21 name.
- **Autothrottle: none found** in any source read, so there is no A/T key.

## Where the pages sit

The main page has no back key. Every child page has its back key at 1,1; at most two folder levels
([navigation.md](navigation.md), "MSFS2024 CJ4 pages"). The first-level pages open from main and their back
keys return to main; the nine pages under MORE return to more.

| Opened by | Page | Level | Holds |
|---|---|---|---|
| main 1,7 `TRIM` | trim | 1 | the C172's trim page: elevator, aileron and rudder trim keys and gauges; the six trim keys hold to repeat |
| main 1,8 `VIEWS` | views | 1 | the C172's views page as it is |
| main 3,7 `SIM RATE` | simrate | 1 | the C172's sim rate page as it is (`XL24-SIMRATE.lua`) |
| main 3,8 `CHECKLIST` | checklist | 1 | the back key only; 1,2 is kept empty for a checklist key |
| main 4,8 `MORE` | more | 1 | nine folder keys |
| more 1,4 `V-SPEEDS` | vspeeds | 2 | the C172's V-speeds page as it is |
| more 1,5 `COM PAD` | compad | 2 | the VisionJet's COM pad page (`XL24-COMPAD.lua`): centered titles and press feedback |
| more 1,6 `AUTOPILOT` | autopilot | 2 | mode keys, hold-to-repeat step keys and the bug and target readouts |
| more 1,7 `XPDR` | xpdr | 2 | the C172's transponder page as it is (`XL24-XPDRPAD.lua`) |
| more 1,8 `RADIOS` | radios | 2 | NAV1, NAV2 and COM2 with hold to repeat, the BARO column, MIC1 and MIC2 |
| more 2,2 `SYSTEMS` | systems | 2 | battery and generator keys; electrical, hydraulic, fuel transfer and pump readouts |
| more 2,3 `ENGINE` | engine | 2 | both engines and the fuel quantities, readouts only |
| more 2,4 `ICE/ENV` | iceenv | 2 | ice protection keys, pressurization readouts |
| more 2,5 `LIGHTS` | lights | 2 | the exterior lights that are not on main, the cabin signs, cabin and panel lights |

MORE 1,2, 1,3 and 2,6 to 2,8 show nothing and do nothing: they are kept for five pages of a later unit ("Not
on these pages, and why").

## Layouts

Positions are **row,column**, 1-based, row 1 at the top. `>` marks a folder key, `-` an empty position.
**Bold** keys hold to repeat ("Hold to repeat").

**main**

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | BAT | N1 | - | PARK | GEAR | FLAPS | TRIM > | VIEWS > |
| **Row 2** | AP | HDG | ALT | VS | NAV | APR | FLC | FD |
| **Row 3** | COM1 | XPDR | ATC | MAP | CDI | BARO | SIM RATE > | CHECKLIST > |
| **Row 4** | NAV LT | BCN | STRB | LDG | TAXI | PITOT | ICE | MORE > |

**trim**

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | - | - | - | - | - | - | - |
| **Row 2** | - | **TRIM UP** | - | - | - | **AIL L** | AIL TRIM | **AIL R** |
| **Row 3** | - | - | - | TRIM | - | **RUD L** | RUD TRIM | **RUD R** |
| **Row 4** | - | **TRIM DN** | - | - | - | - | - | - |

**views**

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | COCKPIT | EXTERNAL | CAMERA | VIEW | VIEW NO | - | - |
| **Row 2** | - | - | - | - | - | - | - | - |
| **Row 3** | - | - | - | - | - | - | - | - |
| **Row 4** | - | - | - | - | - | - | - | - |

**checklist**

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | - | - | - | - | - | - | - |
| **Row 2** | - | - | - | - | - | - | - | - |
| **Row 3** | - | - | - | - | - | - | - | - |
| **Row 4** | - | - | - | - | - | - | - | - |

**more**

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | - | - | V-SPEEDS > | COM PAD > | AUTOPILOT > | XPDR > | RADIOS > |
| **Row 2** | - | SYSTEMS > | ENGINE > | ICE/ENV > | LIGHTS > | - | - | - |
| **Row 3** | - | - | - | - | - | - | - | - |
| **Row 4** | - | - | - | - | - | - | - | - |

**vspeeds**

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | VS0 | VS1 | VR | - | CLIMB | - | - |
| **Row 2** | - | CRUISE | - | VNE | VFE | - | - | - |
| **Row 3** | - | - | - | - | - | - | - | - |
| **Row 4** | - | - | - | - | - | - | - | - |

**simrate**

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | 1X | SLOWER | RATE | FASTER | - | - | - |
| **Row 2** | - | - | - | - | - | - | - | - |
| **Row 3** | - | - | - | - | - | - | - | - |
| **Row 4** | - | - | - | - | - | - | - | - |

**compad**

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | COM1 | ENTRY | - | - | 7 | 8 | 9 |
| **Row 2** | - | STBY ID | - | - | - | 4 | 5 | 6 |
| **Row 3** | - | - | - | - | - | 1 | 2 | 3 |
| **Row 4** | - | - | - | - | - | CLR | 0 | ENT |

**autopilot**

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | AP | FD | HDG | NAV | APR | BC | - |
| **Row 2** | ALT | **HDG+** | **CRS+** | **ALT+** | **VS+** | **SPD+** | YD | BANK |
| **Row 3** | VS | HDG BUG | CRS1 | ALT SEL | VS TGT | SPD TGT | MACH TGT | IAS/MACH |
| **Row 4** | FLC | **HDG-** | **CRS-** | **ALT-** | **VS-** | **SPD-** | - | - |

**xpdr**

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | XPDR | ENTRY | MODE | - | 7 | - | - |
| **Row 2** | - | STBY | ON | ALT | - | 4 | 5 | 6 |
| **Row 3** | - | IDENT | VFR | - | - | 1 | 2 | 3 |
| **Row 4** | - | - | - | - | - | CLR | 0 | ENT |

**radios**

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | NAV1 | NAV1 ID | NAV2 | NAV2 ID | COM2 | COM2 ID | BARO |
| **Row 2** | - | **MHZ+** | **KHZ+** | **MHZ+** | **KHZ+** | **MHZ+** | **KHZ+** | **BARO+** |
| **Row 3** | - | **MHZ-** | **KHZ-** | **MHZ-** | **KHZ-** | **MHZ-** | **KHZ-** | **BARO-** |
| **Row 4** | - | - | - | - | - | MIC1 | MIC2 | - |

**systems**

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | BAT | GEN L | GEN R | AVIONICS | - | - | EXT PWR |
| **Row 2** | - | BUS V | BATT A | HYD PSI | - | - | - | - |
| **Row 3** | - | XFER | PUMP L | PUMP R | - | - | - | - |
| **Row 4** | - | - | - | - | - | - | - | - |

**engine**

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | N1 L | N2 L | ITT L | FF L | OIL P L | OIL T L | - |
| **Row 2** | - | N1 R | N2 R | ITT R | FF R | OIL P R | OIL T R | - |
| **Row 3** | - | START L | RUN L | IGN L | - | FUEL L | FUEL R | FUEL TOT |
| **Row 4** | - | START R | RUN R | IGN R | - | - | - | - |

**iceenv**

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | ENG AI L | ENG AI R | WING/STAB | WSHLD | - | - | - |
| **Row 2** | - | - | - | - | - | - | - | - |
| **Row 3** | - | - | CAB ALT | CAB RATE | DIFF | DUMP | - | - |
| **Row 4** | - | - | - | - | - | - | - | - |

**lights**

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | RECOG | WING | - | - | - | - | - |
| **Row 2** | - | BELTS | NO SMOKE | - | - | - | - | - |
| **Row 3** | - | CABIN | PANEL | - | - | - | - | - |
| **Row 4** | - | - | - | - | - | - | - | - |

The views, simrate, vspeeds and xpdr pages have the C172's layouts
([phase2-trim-views.md](phase2-trim-views.md), [phase2-sim-rate.md](phase2-sim-rate.md),
[phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md) and [phase3-transponder.md](phase3-transponder.md)), trim
the C172's too, and compad the VisionJet's ([visionjet-sf50.md](visionjet-sf50.md), "Key table: compad").

## Key table

Columns as in [phase2-main-page.md](phase2-main-page.md), "Key table"; the template codes (T2 to H1) are
under "What each key holds". Tags in brackets are under "Sources". The main page keeps the C172 G1000 grid
(which was the VisionJet's too before its main page changed, V-UX). AP, COM1, XPDR, ATC, MAP, CDI and BARO
are the VisionJet's keys from before its main page changed (V-UX). The main page has no hold-to-repeat key.

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | `BAT` | Dynamic Button | T2 | `K:TOGGLE_MASTER_BATTERY:1` [SDK-ELECE; CKL 7] | `(A:ELECTRICAL MASTER BATTERY:1, Bool)` [SDK-ELECV] | On/Off image |
| 1,2 | `N1` | Display Value | T3 | none | `(A:TURB ENG N1:1, Percent)` [SDK-ENGV] | Format `1.1` |
| 1,3 |  | Empty |  |  |  | Fuel pump: the CJ4's pumps are readouts on SYSTEMS (docs/cj4-research.md, Main page) |
| 1,4 | `PARK` | Dynamic Button | T2 | `K:PARKING_BRAKES` [AM; failed in the SF50] | `(A:BRAKE PARKING POSITION, Bool)` [AM, SDK-GEARV] | On/Off image |
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
| 3,6 | `BARO` | Display Value | T3 | Main `K:BAROMETRIC` [SDK-INSTE], Second (long press) `K:BAROMETRIC_STD_PRESSURE` [SDK-INSTE; HH-MS; README 2.1; as visionjet-sf50.md] | `(A:KOHLSMAN SETTING HG:1, inHg)` [SDK-SYSV] | Format `2.2` |
| 3,7 | `SIM RATE` | Folder | (Stream Deck) | Opens the child page **simrate** | none | Folder; the page's keys: "Key table: simrate" below |
| 3,8 | `CHECKLIST` | Folder | (Stream Deck) | Opens the child page **checklist** | none | Folder; the page's keys: "Key table: checklist" below |
| 4,1 | `NAV LT` | Dynamic Button | T2 | `K:TOGGLE_NAV_LIGHTS` [SDK-ELECE] | `(A:LIGHT NAV, Bool)` [SDK-SYSV] | On/Off image |
| 4,2 | `BCN` | Dynamic Button | T2 | `K:TOGGLE_BEACON_LIGHTS` [SDK-ELECE] | `(A:LIGHT BEACON, Bool)` [SDK-SYSV] | On/Off image |
| 4,3 | `STRB` | Dynamic Button | T2 | `K:STROBES_TOGGLE` [SDK-ELECE] | `(A:LIGHT STROBE, Bool)` [SDK-SYSV] | On/Off image |
| 4,4 | `LDG` | Dynamic Button | T2 | `K:LANDING_LIGHTS_TOGGLE` [SDK-ELECE; CKL 301] | `(A:LIGHT LANDING, Bool)` [SDK-SYSV] | On/Off image |
| 4,5 | `TAXI` | Dynamic Button | T2 | `K:TOGGLE_TAXI_LIGHTS` [SDK-ELECE] | `(A:LIGHT TAXI, Bool)` [SDK-SYSV] | On/Off image |
| 4,6 | `PITOT` | Dynamic Button | T2 | `K:PITOT_HEAT_TOGGLE` [SDK-AMISCE; CKL 239] | `(A:PITOT HEAT, Bool)` [SDK-SYSV] | On/Off image |
| 4,7 | `ICE` | Dynamic Button | T2 | `K:TOGGLE_STRUCTURAL_DEICE` [SDK-AMISCE; CKL 191] | `(A:STRUCTURAL DEICE SWITCH, Bool)` [SDK-SYSV] | On/Off image |
| 4,8 | `MORE` | Folder | (Stream Deck) | Opens the child page **more** | none | Folder; the page's keys: "Key table: more" below |

## Key table: trim

The C172's trim page ([phase2-trim-views.md](phase2-trim-views.md)) with its aileron trim keys and gauge:
the CJ4 has three trims (CKL 211). The six trim keys hold to repeat (H1), at most 8 s per hold.

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | (Stream Deck) | Returns to the main page | none | Back key |
| 1,2 |  | Empty |  |  |  |  |
| 1,3 |  | Empty |  |  |  |  |
| 1,4 |  | Empty |  |  |  |  |
| 1,5 |  | Empty |  |  |  |  |
| 1,6 |  | Empty |  |  |  |  |
| 1,7 |  | Empty |  |  |  |  |
| 1,8 |  | Empty |  |  |  |  |
| 2,1 |  | Empty |  |  |  |  |
| 2,2 | `TRIM UP` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(25)` key down, `lua:XL24-CJ4:RELEASE(25)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:ELEV_TRIM_UP` [SDK-FCE] | none (the gauge 3,4 shows the result) | fixed image |
| 2,3 |  | Empty |  |  |  |  |
| 2,4 |  | Empty |  |  |  |  |
| 2,5 |  | Empty |  |  |  |  |
| 2,6 | `AIL L` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(27)` key down, `lua:XL24-CJ4:RELEASE(27)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:AILERON_TRIM_LEFT` [SDK-FCE] | none (the gauge 2,7 shows the result) | fixed image |
| 2,7 | `AIL TRIM` | Display Gauge | T9 | none | `(A:AILERON TRIM PCT, percent)` [SDK-CTLV, SDK-UNITS] | Format `1.1`; horizontal bar, values right (Orientation Right, saved `0`), `-100` to `100`, center line, pointer |
| 2,8 | `AIL R` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(28)` key down, `lua:XL24-CJ4:RELEASE(28)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:AILERON_TRIM_RIGHT` [SDK-FCE] | none (the gauge 2,7 shows the result) | fixed image |
| 3,1 |  | Empty |  |  |  |  |
| 3,2 |  | Empty |  |  |  |  |
| 3,3 |  | Empty |  |  |  |  |
| 3,4 | `TRIM` | Display Gauge | T9 | none | `(A:ELEVATOR TRIM PCT EX2, percent)` [SDK-CTLV, SDK-UNITS] | Format `1.0`; vertical bar, values up (Orientation Up, saved `-90`), `-100` to `100`, center line, pointer |
| 3,5 |  | Empty |  |  |  |  |
| 3,6 | `RUD L` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(29)` key down, `lua:XL24-CJ4:RELEASE(29)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:RUDDER_TRIM_LEFT` [SDK-FCE] | none (the gauge 3,7 shows the result) | fixed image |
| 3,7 | `RUD TRIM` | Display Gauge | T9 | none | `(A:RUDDER TRIM PCT, percent)` [SDK-CTLV, SDK20-CTLV, SDK-UNITS] | Format `1.1`; horizontal bar, values right (Orientation Right, saved `0`), `-100` to `100`, center line, pointer |
| 3,8 | `RUD R` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(30)` key down, `lua:XL24-CJ4:RELEASE(30)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:RUDDER_TRIM_RIGHT` [SDK-FCE] | none (the gauge 3,7 shows the result) | fixed image |
| 4,1 |  | Empty |  |  |  |  |
| 4,2 | `TRIM DN` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(26)` key down, `lua:XL24-CJ4:RELEASE(26)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:ELEV_TRIM_DN` [SDK-FCE] | none (the gauge 3,4 shows the result) | fixed image |
| 4,3 |  | Empty |  |  |  |  |
| 4,4 |  | Empty |  |  |  |  |
| 4,5 |  | Empty |  |  |  |  |
| 4,6 |  | Empty |  |  |  |  |
| 4,7 |  | Empty |  |  |  |  |
| 4,8 |  | Empty |  |  |  |  |

## Key table: views

The C172's views page ([phase2-trim-views.md](phase2-trim-views.md)); rows as that doc's "Key table: views".
The map window key is main 3,4.

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | (Stream Deck) | Returns to the main page | none | Back key |
| 1,2 | `COCKPIT` | Dynamic Button | T6 | `(A:CAMERA STATE, Enum)`, On `$=2` / Off `` [SDK-CAMV, README 2.1.1, 2.1.2] | `(A:CAMERA STATE, Enum)` [SDK-CAMV, SDK-UNITS] | On/Off image: On `2`, Off `3` |
| 1,3 | `EXTERNAL` | Dynamic Button | T6 | `(A:CAMERA STATE, Enum)`, On `$2,=3<` / Off `` [SDK-CAMV, README 2.1.1, 2.1.2] | `(A:CAMERA STATE, Enum)` [SDK-CAMV, SDK-UNITS] | On/Off image: On `3`, Off `2` |
| 1,4 | `CAMERA` | Display Value | T3 | none | `(A:CAMERA STATE, Enum)` [SDK-CAMV, SDK-UNITS] | Mappings `2=COCKPIT:3=CHASE:4=FIXED:5=ENV:7=SHOWCASE:8=DRONE` |
| 1,5 | `VIEW` | Display Value | T3 | none | `(A:CAMERA VIEW TYPE AND INDEX:0, Enum)` [SDK-CAMV, SDK-UNITS] | Mappings `0=OTHER:1=PILOT:2=INSTR:3=QUICK:4=QV EXT:5=VIEW` |
| 1,6 | `VIEW NO` | Display Value | T3 | none | `(A:CAMERA VIEW TYPE AND INDEX:1, number)` [SDK-CAMV, SDK-UNITS] | Format `1.0` |
| 1,7 |  | Empty |  |  |  |  |
| 1,8 |  | Empty |  |  |  |  |
| 2,1 |  | Empty |  |  |  |  |
| 2,2 |  | Empty |  |  |  |  |
| 2,3 |  | Empty |  |  |  |  |
| 2,4 |  | Empty |  |  |  |  |
| 2,5 |  | Empty |  |  |  |  |
| 2,6 |  | Empty |  |  |  |  |
| 2,7 |  | Empty |  |  |  |  |
| 2,8 |  | Empty |  |  |  |  |
| 3,1 |  | Empty |  |  |  |  |
| 3,2 |  | Empty |  |  |  |  |
| 3,3 |  | Empty |  |  |  |  |
| 3,4 |  | Empty |  |  |  |  |
| 3,5 |  | Empty |  |  |  |  |
| 3,6 |  | Empty |  |  |  |  |
| 3,7 |  | Empty |  |  |  |  |
| 3,8 |  | Empty |  |  |  |  |
| 4,1 |  | Empty |  |  |  |  |
| 4,2 |  | Empty |  |  |  |  |
| 4,3 |  | Empty |  |  |  |  |
| 4,4 |  | Empty |  |  |  |  |
| 4,5 |  | Empty |  |  |  |  |
| 4,6 |  | Empty |  |  |  |  |
| 4,7 |  | Empty |  |  |  |  |
| 4,8 |  | Empty |  |  |  |  |

## Key table: checklist

The back key only. 1,2 is kept for the cursor control panel's checklist key ("Not on these pages, and why").

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | (Stream Deck) | Returns to the main page | none | Back key |
| 1,2 |  | Empty |  |  |  | CKLST: kept for the cursor control panel's checklist key; it waits for a test of the WT21 key names in the default CJ4 (docs/cj4-research.md) |
| 1,3 |  | Empty |  |  |  |  |
| 1,4 |  | Empty |  |  |  |  |
| 1,5 |  | Empty |  |  |  |  |
| 1,6 |  | Empty |  |  |  |  |
| 1,7 |  | Empty |  |  |  |  |
| 1,8 |  | Empty |  |  |  |  |
| 2,1 |  | Empty |  |  |  |  |
| 2,2 |  | Empty |  |  |  |  |
| 2,3 |  | Empty |  |  |  |  |
| 2,4 |  | Empty |  |  |  |  |
| 2,5 |  | Empty |  |  |  |  |
| 2,6 |  | Empty |  |  |  |  |
| 2,7 |  | Empty |  |  |  |  |
| 2,8 |  | Empty |  |  |  |  |
| 3,1 |  | Empty |  |  |  |  |
| 3,2 |  | Empty |  |  |  |  |
| 3,3 |  | Empty |  |  |  |  |
| 3,4 |  | Empty |  |  |  |  |
| 3,5 |  | Empty |  |  |  |  |
| 3,6 |  | Empty |  |  |  |  |
| 3,7 |  | Empty |  |  |  |  |
| 3,8 |  | Empty |  |  |  |  |
| 4,1 |  | Empty |  |  |  |  |
| 4,2 |  | Empty |  |  |  |  |
| 4,3 |  | Empty |  |  |  |  |
| 4,4 |  | Empty |  |  |  |  |
| 4,5 |  | Empty |  |  |  |  |
| 4,6 |  | Empty |  |  |  |  |
| 4,7 |  | Empty |  |  |  |  |
| 4,8 |  | Empty |  |  |  |  |

## Key table: more

Nine folder keys: V-SPEEDS to RADIOS at 1,4 to 1,8, SYSTEMS to LIGHTS at 2,2 to 2,5.

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | (Stream Deck) | Returns to the main page | none | Back key |
| 1,2 |  | Empty |  |  |  | DCP: kept for the display control panel page; it waits for a test of the WT21 key names in the default CJ4 (docs/cj4-research.md) |
| 1,3 |  | Empty |  |  |  | CCP: kept for the cursor control panel page; it waits for a test of the WT21 key names in the default CJ4 (docs/cj4-research.md) |
| 1,4 | `V-SPEEDS` | Folder | (Stream Deck) | Opens the child page **vspeeds** | none | Folder; the page's keys: "Key table: vspeeds" below |
| 1,5 | `COM PAD` | Folder | (Stream Deck) | Opens the child page **compad** | none | Folder; the page's keys: "Key table: compad" below |
| 1,6 | `AUTOPILOT` | Folder | (Stream Deck) | Opens the child page **autopilot** | none | Folder; the page's keys: "Key table: autopilot" below |
| 1,7 | `XPDR` | Folder | (Stream Deck) | Opens the child page **xpdr** | none | Folder; the page's keys: "Key table: xpdr" below |
| 1,8 | `RADIOS` | Folder | (Stream Deck) | Opens the child page **radios** | none | Folder; the page's keys: "Key table: radios" below |
| 2,1 |  | Empty |  |  |  |  |
| 2,2 | `SYSTEMS` | Folder | (Stream Deck) | Opens the child page **systems** | none | Folder; the page's keys: "Key table: systems" below |
| 2,3 | `ENGINE` | Folder | (Stream Deck) | Opens the child page **engine** | none | Folder; the page's keys: "Key table: engine" below |
| 2,4 | `ICE/ENV` | Folder | (Stream Deck) | Opens the child page **iceenv** | none | Folder; the page's keys: "Key table: iceenv" below |
| 2,5 | `LIGHTS` | Folder | (Stream Deck) | Opens the child page **lights** | none | Folder; the page's keys: "Key table: lights" below |
| 2,6 |  | Empty |  |  |  | FMS: kept for the page of the FMC's function and line select keys; it waits for a test of the WT21 key names in the default CJ4 (docs/cj4-research.md) |
| 2,7 |  | Empty |  |  |  | FMS ABC: kept for the page of the FMC's letter keys; it waits for a test of the WT21 key names in the default CJ4 (docs/cj4-research.md) |
| 2,8 |  | Empty |  |  |  | FMS 123: kept for the page of the FMC's number keys; it waits for a test of the WT21 key names in the default CJ4 (docs/cj4-research.md) |
| 3,1 |  | Empty |  |  |  |  |
| 3,2 |  | Empty |  |  |  |  |
| 3,3 |  | Empty |  |  |  |  |
| 3,4 |  | Empty |  |  |  |  |
| 3,5 |  | Empty |  |  |  |  |
| 3,6 |  | Empty |  |  |  |  |
| 3,7 |  | Empty |  |  |  |  |
| 3,8 |  | Empty |  |  |  |  |
| 4,1 |  | Empty |  |  |  |  |
| 4,2 |  | Empty |  |  |  |  |
| 4,3 |  | Empty |  |  |  |  |
| 4,4 |  | Empty |  |  |  |  |
| 4,5 |  | Empty |  |  |  |  |
| 4,6 |  | Empty |  |  |  |  |
| 4,7 |  | Empty |  |  |  |  |
| 4,8 |  | Empty |  |  |  |  |

## Key table: vspeeds

The C172's V-speeds page ([phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md)), with the SimVars' own values
in the CJ4. Whether they hold the CJ4's speeds is a test item.

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | (Stream Deck) | Returns to the MORE page | none | Back key |
| 1,2 | `VS0` | Display Value | T3 | none | `(A:DESIGN SPEED VS0, knots)` [SDK-FMV, SDK-UNITS] | Format `1.0` |
| 1,3 | `VS1` | Display Value | T3 | none | `(A:DESIGN SPEED VS1, knots)` [SDK-FMV, SDK-UNITS] | Format `1.0` |
| 1,4 | `VR` | Display Value | T3 | none | `(A:DESIGN SPEED MIN ROTATION, knots)` [SDK-FMV, SDK-UNITS] | Format `1.0` |
| 1,5 |  | Empty |  |  |  | Vx: no SimVar in the MSFS 2024 SDK |
| 1,6 | `CLIMB` | Display Value | T3 | none | `(A:DESIGN SPEED CLIMB, knots)` [SDK-FMV, SDK-UNITS] | Format `1.0` |
| 1,7 |  | Empty |  |  |  |  |
| 1,8 |  | Empty |  |  |  |  |
| 2,1 |  | Empty |  |  |  |  |
| 2,2 | `CRUISE` | Display Value | T3 | none | `(A:DESIGN SPEED VC, knots)` [SDK-FMV, SDK-UNITS] | Format `1.0` |
| 2,3 |  | Empty |  |  |  | Vno: no SimVar in the MSFS 2024 SDK |
| 2,4 | `VNE` | Display Value | T3 | none | `(A:REFERENCE SPEED MAX IAS, knots)` [SDK-FMV, SDK-UNITS] | Format `1.0` |
| 2,5 | `VFE` | Display Value | T3 | none | `(A:FLAPS CURRENT SPEED LIMITATION, knots)` [SDK-CTLV, SDK-UNITS] | Format `1.0` |
| 2,6 |  | Empty |  |  |  |  |
| 2,7 |  | Empty |  |  |  |  |
| 2,8 |  | Empty |  |  |  |  |
| 3,1 |  | Empty |  |  |  |  |
| 3,2 |  | Empty |  |  |  |  |
| 3,3 |  | Empty |  |  |  |  |
| 3,4 |  | Empty |  |  |  |  |
| 3,5 |  | Empty |  |  |  |  |
| 3,6 |  | Empty |  |  |  |  |
| 3,7 |  | Empty |  |  |  |  |
| 3,8 |  | Empty |  |  |  |  |
| 4,1 |  | Empty |  |  |  |  |
| 4,2 |  | Empty |  |  |  |  |
| 4,3 |  | Empty |  |  |  |  |
| 4,4 |  | Empty |  |  |  |  |
| 4,5 |  | Empty |  |  |  |  |
| 4,6 |  | Empty |  |  |  |  |
| 4,7 |  | Empty |  |  |  |  |
| 4,8 |  | Empty |  |  |  |  |

## Key table: simrate

The C172's sim rate page ([phase2-sim-rate.md](phase2-sim-rate.md)).

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | (Stream Deck) | Returns to the main page | none | Back key |
| 1,2 | `1X` | Dynamic Button | T2 | `lua:XL24-SIMRATE:SET(1)` (steps `K:SIM_RATE_INCR` / `K:SIM_RATE_DECR`) [README 2.1.1 LUAFUNC, 3.5.1; SDK-MISCE; P2-6 route ruling] | `(A:SIMULATION RATE, number)` [SDK-ENVV, PD-SRC] | On/Off image: On `1`, Off `2` |
| 1,3 | `SLOWER` | Simple Button | T5 | `K:SIM_RATE_DECR` [SDK-MISCE] | none | fixed image |
| 1,4 | `RATE` | Display Value | T3 | Main `K:SIM_RATE_INCR`, Second (long press) `K:SIM_RATE_DECR` [SDK-MISCE, README 2.1] | `(A:SIMULATION RATE, number)` [SDK-ENVV, PD-SRC] | Format `1.2` |
| 1,5 | `FASTER` | Simple Button | T5 | `K:SIM_RATE_INCR` [SDK-MISCE] | none | fixed image |
| 1,6 |  | Empty |  |  |  |  |
| 1,7 |  | Empty |  |  |  |  |
| 1,8 |  | Empty |  |  |  |  |
| 2,1 |  | Empty |  |  |  |  |
| 2,2 |  | Empty |  |  |  |  |
| 2,3 |  | Empty |  |  |  |  |
| 2,4 |  | Empty |  |  |  |  |
| 2,5 |  | Empty |  |  |  |  |
| 2,6 |  | Empty |  |  |  |  |
| 2,7 |  | Empty |  |  |  |  |
| 2,8 |  | Empty |  |  |  |  |
| 3,1 |  | Empty |  |  |  |  |
| 3,2 |  | Empty |  |  |  |  |
| 3,3 |  | Empty |  |  |  |  |
| 3,4 |  | Empty |  |  |  |  |
| 3,5 |  | Empty |  |  |  |  |
| 3,6 |  | Empty |  |  |  |  |
| 3,7 |  | Empty |  |  |  |  |
| 3,8 |  | Empty |  |  |  |  |
| 4,1 |  | Empty |  |  |  |  |
| 4,2 |  | Empty |  |  |  |  |
| 4,3 |  | Empty |  |  |  |  |
| 4,4 |  | Empty |  |  |  |  |
| 4,5 |  | Empty |  |  |  |  |
| 4,6 |  | Empty |  |  |  |  |
| 4,7 |  | Empty |  |  |  |  |
| 4,8 |  | Empty |  |  |  |  |

## Key table: compad

The VisionJet's COM pad page ([visionjet-sf50.md](visionjet-sf50.md), "Key table: compad"), key for key; its
positions and commands are those of the C172's COM1 pad ([phase2-com1-pad.md](phase2-com1-pad.md)). The
digit, CLR and ENT keys are T8L (centered title, press feedback, below). Opened from MORE 1,5, so its back
key returns to the MORE page.

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | (Stream Deck) | Returns to the MORE page | none | Back key |
| 1,2 | `COM1` | COM Radio | T4 | `K:COM_STBY_RADIO_SWAP` [SDK-RADE] | Active `(A:COM ACTIVE FREQUENCY:1, MHz)`, Standby `(A:COM STANDBY FREQUENCY:1, MHz)` [SDK-RADV] | Format `3` |
| 1,3 | `ENTRY` | Display Value | T3 | none | `X:XL24_COMPAD_ENTRY` [README 2.1.1 INTERNAL; written by the script] | the typed digits as text, e.g. `118.5__`; Format empty |
| 1,4 |  | Empty |  |  |  |  |
| 1,5 |  | Empty |  |  |  |  |
| 1,6 | `7` | Dynamic Button | T8L | `lua:XL24-COMPAD:DIGIT(7)` [README 2.1.1 LUAFUNC] | `X:XL24_COMPAD_LIT_7` [README 2.1.1 INTERNAL; written by the script] | title in the middle; image map: none at `0`, green (`Images/XL24-PadLit.png`) at `1`, for 0.25 s after the script took the digit |
| 1,7 | `8` | Dynamic Button | T8L | `lua:XL24-COMPAD:DIGIT(8)` [README 2.1.1 LUAFUNC] | `X:XL24_COMPAD_LIT_8` [README 2.1.1 INTERNAL; written by the script] | title in the middle; image map: none at `0`, green (`Images/XL24-PadLit.png`) at `1`, for 0.25 s after the script took the digit |
| 1,8 | `9` | Dynamic Button | T8L | `lua:XL24-COMPAD:DIGIT(9)` [README 2.1.1 LUAFUNC] | `X:XL24_COMPAD_LIT_9` [README 2.1.1 INTERNAL; written by the script] | title in the middle; image map: none at `0`, green (`Images/XL24-PadLit.png`) at `1`, for 0.25 s after the script took the digit |
| 2,1 |  | Empty |  |  |  |  |
| 2,2 | `STBY ID` | Display Value | T3 | none | `(A:COM STANDBY FREQ IDENT:1, String)` [SDK-RADV; PD-SRC string A-Var] | the station ident as text; Format empty |
| 2,3 |  | Empty |  |  |  |  |
| 2,4 |  | Empty |  |  |  |  |
| 2,5 |  | Empty |  |  |  |  |
| 2,6 | `4` | Dynamic Button | T8L | `lua:XL24-COMPAD:DIGIT(4)` [README 2.1.1 LUAFUNC] | `X:XL24_COMPAD_LIT_4` [README 2.1.1 INTERNAL; written by the script] | title in the middle; image map: none at `0`, green (`Images/XL24-PadLit.png`) at `1`, for 0.25 s after the script took the digit |
| 2,7 | `5` | Dynamic Button | T8L | `lua:XL24-COMPAD:DIGIT(5)` [README 2.1.1 LUAFUNC] | `X:XL24_COMPAD_LIT_5` [README 2.1.1 INTERNAL; written by the script] | title in the middle; image map: none at `0`, green (`Images/XL24-PadLit.png`) at `1`, for 0.25 s after the script took the digit |
| 2,8 | `6` | Dynamic Button | T8L | `lua:XL24-COMPAD:DIGIT(6)` [README 2.1.1 LUAFUNC] | `X:XL24_COMPAD_LIT_6` [README 2.1.1 INTERNAL; written by the script] | title in the middle; image map: none at `0`, green (`Images/XL24-PadLit.png`) at `1`, for 0.25 s after the script took the digit |
| 3,1 |  | Empty |  |  |  |  |
| 3,2 |  | Empty |  |  |  |  |
| 3,3 |  | Empty |  |  |  |  |
| 3,4 |  | Empty |  |  |  |  |
| 3,5 |  | Empty |  |  |  |  |
| 3,6 | `1` | Dynamic Button | T8L | `lua:XL24-COMPAD:DIGIT(1)` [README 2.1.1 LUAFUNC] | `X:XL24_COMPAD_LIT_1` [README 2.1.1 INTERNAL; written by the script] | title in the middle; image map: none at `0`, green (`Images/XL24-PadLit.png`) at `1`, for 0.25 s after the script took the digit |
| 3,7 | `2` | Dynamic Button | T8L | `lua:XL24-COMPAD:DIGIT(2)` [README 2.1.1 LUAFUNC] | `X:XL24_COMPAD_LIT_2` [README 2.1.1 INTERNAL; written by the script] | title in the middle; image map: none at `0`, green (`Images/XL24-PadLit.png`) at `1`, for 0.25 s after the script took the digit |
| 3,8 | `3` | Dynamic Button | T8L | `lua:XL24-COMPAD:DIGIT(3)` [README 2.1.1 LUAFUNC] | `X:XL24_COMPAD_LIT_3` [README 2.1.1 INTERNAL; written by the script] | title in the middle; image map: none at `0`, green (`Images/XL24-PadLit.png`) at `1`, for 0.25 s after the script took the digit |
| 4,1 |  | Empty |  |  |  |  |
| 4,2 |  | Empty |  |  |  |  |
| 4,3 |  | Empty |  |  |  |  |
| 4,4 |  | Empty |  |  |  |  |
| 4,5 |  | Empty |  |  |  |  |
| 4,6 | `CLR` | Dynamic Button | T8L | Main `lua:XL24-COMPAD:BACK`, Second (long press) `lua:XL24-COMPAD:CLEAR` [README 2.1.1 LUAFUNC, 2.1] | `X:XL24_COMPAD_LIT_CLR` [README 2.1.1 INTERNAL; written by the script] | title in the middle; image map: none at `0`, green (`Images/XL24-PadLit.png`) at `1`, for 0.25 s after a press that removed a digit |
| 4,7 | `0` | Dynamic Button | T8L | `lua:XL24-COMPAD:DIGIT(0)` [README 2.1.1 LUAFUNC] | `X:XL24_COMPAD_LIT_0` [README 2.1.1 INTERNAL; written by the script] | title in the middle; image map: none at `0`, green (`Images/XL24-PadLit.png`) at `1`, for 0.25 s after the script took the digit |
| 4,8 | `ENT` | Dynamic Button | T8L | Main `lua:XL24-COMPAD:ENTER`, Second (long press) `lua:XL24-COMPAD:ENTER_SWAP` [README 2.1.1 LUAFUNC, 2.1] | `X:XL24_COMPAD_LIT_ENT` [README 2.1.1 INTERNAL; written by the script] | title in the middle; image map: none at `0`, green (`Images/XL24-PadLit.png`) at `1`, for 1 s after the sim read back the sent frequency (COM1 standby; on a long press COM1 active) |

### COM pad: centered text and press feedback

The page is the VisionJet's COM pad ([visionjet-sf50.md](visionjet-sf50.md), "COM pad: centered text and
press feedback"), opened here from MORE 1,5. It has not been sim-tested on any aircraft. The ten digit keys,
CLR and ENT have their title in the middle of the key, and a key turns green for a short time when its press
took effect.

| Press | The key turns green | What the green means |
|---|---|---|
| A digit the pad takes | at once, for 0.25 s | the script added the digit to the entry (no sim value exists for it), never that a radio changed |
| A digit the pad refuses (the first digit not 1, and so on) | no | |
| CLR, short or long, with digits typed | at once, for 0.25 s | the script removed the last digit, or all; never that a radio changed |
| CLR with no digit typed | no | |
| ENT, short | when COM1 standby reads the sent frequency (within 1 kHz, at most 1.5 s later), for 1 s | the sim read back the sent frequency in COM1 standby |
| ENT, long | when COM1 active reads the sent frequency (the same limits), for 1 s | the sim read back the sent frequency in COM1 active |
| ENT with no valid frequency typed, or the sim does not read it back within 1.5 s | no | the entry stays, or the log says COM1 did not read it back |

A refused press, a press with no sim connected and a failed read-back stay dark. COM1 at 1,2 is the radio's
own state: it shows which frequency moved. A command runs when the key is released, so the green comes on
release (PD-PAD). If COM1 standby (on a long press COM1 active) already held the typed frequency, ENT turns
green at once: the sim has it, whether or not this press changed anything. A newer ENT press ends the wait
and the green of an older one.

How it is made: each of the twelve keys is a Dynamic Button whose value is its own internal variable
(`X:XL24_COMPAD_LIT_0` to `_9`, `_CLR`, `_ENT`), with Image Mapping on: `0` the empty `Images/None.png`, `1`
the package's own `Images/XL24-PadLit.png`. The shared script `XL24-COMPAD.lua` writes the variables; this
profile does not change the script, and the variables are the same as on the VisionJet (the C172's keys do
not read them). Without the script the keys do nothing; without the image they show PilotsDeck's wait image
instead of green. The package installs both.

Not proven: that the script's waits (the end of a light, the reads after ENT) don't hold up a fast next
press (the row "COM pad press feedback, fast presses (V-PAD)" in the VisionJet doc's "Fallbacks"; the
fallback is the same for both aircraft). Also a test item: whether the CJ4's COM1 takes the event the script
sends, `K:COM_STBY_RADIO_SET_HZ` ([phase2-com1-pad.md](phase2-com1-pad.md)).

## Key table: autopilot

Standard SDK mode keys (SDK-APE) with the SimVar each mode reads (SDK-APV), the step keys in rows 2 and 4
(H1) and their readouts in row 3. The CJ4's own autopilot panel may use input events instead (sim steps S-1
and S-4).

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | (Stream Deck) | Returns to the MORE page | none | Back key |
| 1,2 | `AP` | Dynamic Button | T2 | `K:AP_MASTER` [SDK-APE] | `(A:AUTOPILOT MASTER, Bool)` [SDK-APV] | On/Off image |
| 1,3 | `FD` | Dynamic Button | T2 | `K:TOGGLE_FLIGHT_DIRECTOR` [SDK-APE] | `(A:AUTOPILOT FLIGHT DIRECTOR ACTIVE, Bool)` [SDK-APV] | On/Off image |
| 1,4 | `HDG` | Dynamic Button | T2 | `K:AP_HDG_HOLD` [SDK-APE] | `(A:AUTOPILOT HEADING LOCK, Bool)` [SDK-APV] | On/Off image |
| 1,5 | `NAV` | Dynamic Button | T2 | `K:AP_NAV1_HOLD` [SDK-APE] | `(A:AUTOPILOT NAV1 LOCK, Bool)` [SDK-APV] | On/Off image |
| 1,6 | `APR` | Dynamic Button | T2 | `K:AP_APR_HOLD` [SDK-APE] | `(A:AUTOPILOT APPROACH HOLD, Bool)` [SDK-APV] | On/Off image |
| 1,7 | `BC` | Dynamic Button | T2 | `K:AP_BC_HOLD` [SDK-APE] | `(A:AUTOPILOT BACKCOURSE HOLD, Bool)` [SDK-APV] | On/Off image |
| 1,8 |  | Empty |  |  |  | VNAV: no 2024 VNAV event found (SDK-APE); its input event once S-1 lists it (docs/cj4-research.md) |
| 2,1 | `ALT` | Dynamic Button | T2 | `K:AP_ALT_HOLD` [SDK-APE] | `(A:AUTOPILOT ALTITUDE LOCK, Bool)` [SDK-APV] | On/Off image |
| 2,2 | `HDG+` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(1)` key down, `lua:XL24-CJ4:RELEASE(1)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:HEADING_BUG_INC` [SDK-APE] | none (HDG BUG at 3,2 shows the result) | fixed image |
| 2,3 | `CRS+` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(3)` key down, `lua:XL24-CJ4:RELEASE(3)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:VOR1_OBI_INC` [SDK-RADE] | none (CRS1 at 3,3 shows the result) | fixed image |
| 2,4 | `ALT+` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(5)` key down, `lua:XL24-CJ4:RELEASE(5)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:AP_ALT_VAR_INC` [SDK-APE] | none (ALT SEL at 3,4 shows the result) | fixed image |
| 2,5 | `VS+` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(7)` key down, `lua:XL24-CJ4:RELEASE(7)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:AP_VS_VAR_INC` [SDK-APE] | none (VS TGT at 3,5 shows the result) | fixed image |
| 2,6 | `SPD+` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(9)` key down, `lua:XL24-CJ4:RELEASE(9)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:AP_SPD_VAR_INC` [SDK-APE] | none (SPD TGT at 3,6 shows the result) | fixed image |
| 2,7 | `YD` | Dynamic Button | T2 | `K:YAW_DAMPER_TOGGLE` [SDK-APE; CKL 285] | `(A:AUTOPILOT YAW DAMPER, Bool)` [SDK-APV] | On/Off image |
| 2,8 | `BANK` | Display Value | T3 | Main `K:AP_MAX_BANK_INC`, Second (long press) `K:AP_MAX_BANK_DEC` [SDK-APE, README 2.1] | `(A:AUTOPILOT MAX BANK ID, number)` [SDK-APV] | Format `1.0` |
| 3,1 | `VS` | Dynamic Button | T2 | `K:AP_VS_HOLD` [SDK-APE] | `(A:AUTOPILOT VERTICAL HOLD, Bool)` [SDK-APV] | On/Off image |
| 3,2 | `HDG BUG` | Display Value | T3 | none | `(A:AUTOPILOT HEADING LOCK DIR, Degrees)` [SDK-APV] | Format `3.0:%s°` |
| 3,3 | `CRS1` | Display Value | T3 | none | `(A:NAV OBS:1, Degrees)` [SDK-RADV] | Format `3.0:%s°` |
| 3,4 | `ALT SEL` | Display Value | T3 | none | `(A:AUTOPILOT ALTITUDE LOCK VAR, Feet)` [SDK-APV] | Format `1.0` |
| 3,5 | `VS TGT` | Display Value | T3 | none | `(A:AUTOPILOT VERTICAL HOLD VAR, Feet/minute)` [SDK-APV] | Format `1.0` |
| 3,6 | `SPD TGT` | Display Value | T3 | none | `(A:AUTOPILOT AIRSPEED HOLD VAR, Knots)` [SDK-APV] | Format `1.0` |
| 3,7 | `MACH TGT` | Display Value | T3 | none | `(A:AUTOPILOT MACH HOLD VAR, number)` [SDK-APV] | Format `1.2` |
| 3,8 | `IAS/MACH` | Dynamic Button | T2 | `K:AP_MANAGED_SPEED_IN_MACH_TOGGLE` [SDK-APE] | `(A:AUTOPILOT MANAGED SPEED IN MACH, Bool)` [SDK-APV] | On/Off image |
| 4,1 | `FLC` | Dynamic Button | T2 | `K:FLIGHT_LEVEL_CHANGE` [SDK-APE] | `(A:AUTOPILOT FLIGHT LEVEL CHANGE, Bool)` [SDK-APV] | On/Off image |
| 4,2 | `HDG-` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(2)` key down, `lua:XL24-CJ4:RELEASE(2)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:HEADING_BUG_DEC` [SDK-APE] | none (HDG BUG at 3,2 shows the result) | fixed image |
| 4,3 | `CRS-` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(4)` key down, `lua:XL24-CJ4:RELEASE(4)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:VOR1_OBI_DEC` [SDK-RADE] | none (CRS1 at 3,3 shows the result) | fixed image |
| 4,4 | `ALT-` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(6)` key down, `lua:XL24-CJ4:RELEASE(6)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:AP_ALT_VAR_DEC` [SDK-APE] | none (ALT SEL at 3,4 shows the result) | fixed image |
| 4,5 | `VS-` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(8)` key down, `lua:XL24-CJ4:RELEASE(8)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:AP_VS_VAR_DEC` [SDK-APE] | none (VS TGT at 3,5 shows the result) | fixed image |
| 4,6 | `SPD-` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(10)` key down, `lua:XL24-CJ4:RELEASE(10)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:AP_SPD_VAR_DEC` [SDK-APE] | none (SPD TGT at 3,6 shows the result) | fixed image |
| 4,7 |  | Empty |  |  |  |  |
| 4,8 |  | Empty |  |  |  |  |

## Key table: xpdr

The C172's transponder page ([phase3-transponder.md](phase3-transponder.md)), including its writes to the
transponder state.

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | (Stream Deck) | Returns to the MORE page | none | Back key |
| 1,2 | `XPDR` | Display Value | T3 | none | `(A:TRANSPONDER CODE:1, Bco16)` [SDK-RADV] | Decode BCD, Format `4.0` |
| 1,3 | `ENTRY` | Display Value | T3 | none | `X:XL24_XPDRPAD_ENTRY` [README 2.1.1 INTERNAL; written by the script] | the typed digits as text, e.g. `12__`; Format empty |
| 1,4 | `MODE` | Display Value | T3 | none | `(A:TRANSPONDER STATE:1, Enum)` [SDK-RADV] | Mappings `0=OFF:1=STBY:2=TEST:3=ON:4=ALT:5=GND` |
| 1,5 |  | Empty |  |  |  |  |
| 1,6 | `7` | Simple Button | T8 | `lua:XL24-XPDRPAD:DIGIT(7)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 1,7 |  | Empty |  |  |  | no key 8 (codes use 0-7) |
| 1,8 |  | Empty |  |  |  | no key 9 (codes use 0-7) |
| 2,1 |  | Empty |  |  |  |  |
| 2,2 | `STBY` | Dynamic Button | T6 | `(A:TRANSPONDER STATE:1, Enum)`, On `$=1` / Off `` [SDK-RADV, README 2.1.1, 2.1.2] | `(A:TRANSPONDER STATE:1, Enum)` [SDK-RADV] | On/Off image: On `1`, Off `4` |
| 2,3 | `ON` | Dynamic Button | T6 | `(A:TRANSPONDER STATE:1, Enum)`, On `$=3` / Off `` [SDK-RADV, README 2.1.1, 2.1.2] | `(A:TRANSPONDER STATE:1, Enum)` [SDK-RADV] | On/Off image: On `3`, Off `1` |
| 2,4 | `ALT` | Dynamic Button | T6 | `(A:TRANSPONDER STATE:1, Enum)`, On `$=4` / Off `` [SDK-RADV, README 2.1.1, 2.1.2] | `(A:TRANSPONDER STATE:1, Enum)` [SDK-RADV] | On/Off image: On `4`, Off `1` |
| 2,5 |  | Empty |  |  |  |  |
| 2,6 | `4` | Simple Button | T8 | `lua:XL24-XPDRPAD:DIGIT(4)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 2,7 | `5` | Simple Button | T8 | `lua:XL24-XPDRPAD:DIGIT(5)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 2,8 | `6` | Simple Button | T8 | `lua:XL24-XPDRPAD:DIGIT(6)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 3,1 |  | Empty |  |  |  |  |
| 3,2 | `IDENT` | Dynamic Button | T2 | `K:XPNDR_IDENT_ON` [SDK-RADE] | `(A:TRANSPONDER IDENT:1, Bool)` [SDK-RADV] | On/Off image |
| 3,3 | `VFR` | Simple Button | T5 | `K:XPNDR_SET:4608` [SDK-RADE] | none | fixed image |
| 3,4 |  | Empty |  |  |  |  |
| 3,5 |  | Empty |  |  |  |  |
| 3,6 | `1` | Simple Button | T8 | `lua:XL24-XPDRPAD:DIGIT(1)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 3,7 | `2` | Simple Button | T8 | `lua:XL24-XPDRPAD:DIGIT(2)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 3,8 | `3` | Simple Button | T8 | `lua:XL24-XPDRPAD:DIGIT(3)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 4,1 |  | Empty |  |  |  |  |
| 4,2 |  | Empty |  |  |  |  |
| 4,3 |  | Empty |  |  |  |  |
| 4,4 |  | Empty |  |  |  |  |
| 4,5 |  | Empty |  |  |  |  |
| 4,6 | `CLR` | Simple Button | T8 | Main `lua:XL24-XPDRPAD:BACK`, Second (long press) `lua:XL24-XPDRPAD:CLEAR` [README 2.1.1 LUAFUNC, 2.1] | none | fixed image |
| 4,7 | `0` | Simple Button | T8 | `lua:XL24-XPDRPAD:DIGIT(0)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 4,8 | `ENT` | Simple Button | T8 | `lua:XL24-XPDRPAD:ENTER` [README 2.1.1 LUAFUNC] | none (XPDR at 1,2 shows the result) | fixed image |

## Key table: radios

The VisionJet's radios page from before its main page changed (V-UX): NAV1, NAV2 and COM2 with their step
keys, the BARO column and the two transmitter keys. The step keys call this profile's `XL24-CJ4.lua`. BARO
1,8 is a readout without a press (main 3,6 has the press and the long press).

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | (Stream Deck) | Returns to the MORE page | none | Back key |
| 1,2 | `NAV1` | COM Radio | T4 | `K:NAV1_RADIO_SWAP` [SDK-RADE] | Active `(A:NAV ACTIVE FREQUENCY:1, MHz)`, Standby `(A:NAV STANDBY FREQUENCY:1, MHz)` [SDK-RADV] | Format `2` |
| 1,3 | `NAV1 ID` | Display Value | T3 | none | `(A:NAV IDENT:1, String)` [SDK-RADV] | the station ident as text; Format empty |
| 1,4 | `NAV2` | COM Radio | T4 | `K:NAV2_RADIO_SWAP` [SDK-RADE] | Active `(A:NAV ACTIVE FREQUENCY:2, MHz)`, Standby `(A:NAV STANDBY FREQUENCY:2, MHz)` [SDK-RADV] | Format `2` |
| 1,5 | `NAV2 ID` | Display Value | T3 | none | `(A:NAV IDENT:2, String)` [SDK-RADV] | the station ident as text; Format empty |
| 1,6 | `COM2` | COM Radio | T4 | `K:COM2_RADIO_SWAP` [SDK-RADE] | Active `(A:COM ACTIVE FREQUENCY:2, MHz)`, Standby `(A:COM STANDBY FREQUENCY:2, MHz)` [SDK-RADV] | Format `3` |
| 1,7 | `COM2 ID` | Display Value | T3 | none | `(A:COM ACTIVE FREQ IDENT:2, String)` [SDK-RADV] | the station ident as text; Format empty |
| 1,8 | `BARO` | Display Value | T3 | none | `(A:KOHLSMAN SETTING HG:1, inHg)` [SDK-SYSV] | Format `2.2` |
| 2,1 |  | Empty |  |  |  |  |
| 2,2 | `MHZ+` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(13)` key down, `lua:XL24-CJ4:RELEASE(13)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:NAV1_RADIO_WHOLE_INC` [SDK-RADE] | none | fixed image |
| 2,3 | `KHZ+` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(14)` key down, `lua:XL24-CJ4:RELEASE(14)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:NAV1_RADIO_FRACT_INC` [SDK-RADE] | none | fixed image |
| 2,4 | `MHZ+` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(15)` key down, `lua:XL24-CJ4:RELEASE(15)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:NAV2_RADIO_WHOLE_INC` [SDK-RADE] | none | fixed image |
| 2,5 | `KHZ+` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(16)` key down, `lua:XL24-CJ4:RELEASE(16)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:NAV2_RADIO_FRACT_INC` [SDK-RADE] | none | fixed image |
| 2,6 | `MHZ+` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(17)` key down, `lua:XL24-CJ4:RELEASE(17)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:COM2_RADIO_WHOLE_INC` [SDK-RADE] | none | fixed image |
| 2,7 | `KHZ+` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(18)` key down, `lua:XL24-CJ4:RELEASE(18)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:COM2_RADIO_FRACT_INC` [SDK-RADE] | none | fixed image |
| 2,8 | `BARO+` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(11)` key down, `lua:XL24-CJ4:RELEASE(11)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:KOHLSMAN_INC` [SDK-INSTE; weak, as visionjet-sf50.md] | none (1,8 shows the result) | fixed image |
| 3,1 |  | Empty |  |  |  |  |
| 3,2 | `MHZ-` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(19)` key down, `lua:XL24-CJ4:RELEASE(19)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:NAV1_RADIO_WHOLE_DEC` [SDK-RADE] | none | fixed image |
| 3,3 | `KHZ-` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(20)` key down, `lua:XL24-CJ4:RELEASE(20)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:NAV1_RADIO_FRACT_DEC` [SDK-RADE] | none | fixed image |
| 3,4 | `MHZ-` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(21)` key down, `lua:XL24-CJ4:RELEASE(21)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:NAV2_RADIO_WHOLE_DEC` [SDK-RADE] | none | fixed image |
| 3,5 | `KHZ-` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(22)` key down, `lua:XL24-CJ4:RELEASE(22)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:NAV2_RADIO_FRACT_DEC` [SDK-RADE] | none | fixed image |
| 3,6 | `MHZ-` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(23)` key down, `lua:XL24-CJ4:RELEASE(23)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:COM2_RADIO_WHOLE_DEC` [SDK-RADE] | none | fixed image |
| 3,7 | `KHZ-` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(24)` key down, `lua:XL24-CJ4:RELEASE(24)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:COM2_RADIO_FRACT_DEC` [SDK-RADE] | none | fixed image |
| 3,8 | `BARO-` | Simple Button | H1 | `lua:XL24-CJ4:HOLD(12)` key down, `lua:XL24-CJ4:RELEASE(12)` key up (Hold Switch) [README 2.1.1 LUAFUNC, 2.1.2; PD-HOLD]; the script sends `K:KOHLSMAN_DEC` [SDK-INSTE; weak, as visionjet-sf50.md] | none (1,8 shows the result) | fixed image |
| 4,1 |  | Empty |  |  |  |  |
| 4,2 |  | Empty |  |  |  |  |
| 4,3 |  | Empty |  |  |  |  |
| 4,4 |  | Empty |  |  |  |  |
| 4,5 |  | Empty |  |  |  |  |
| 4,6 | `MIC1` | Dynamic Button | T2 | `K:PILOT_TRANSMITTER_SET:0` [SDK-RADE] | `(A:COM TRANSMIT:1, Bool)` [SDK-RADV] | On/Off image |
| 4,7 | `MIC2` | Dynamic Button | T2 | `K:PILOT_TRANSMITTER_SET:1` [SDK-RADE] | `(A:COM TRANSMIT:2, Bool)` [SDK-RADV] | On/Off image |
| 4,8 |  | Empty |  |  |  |  |

## Key table: systems

Electrical keys in row 1 (standard events), electrical and hydraulic readouts in row 2, fuel transfer and
pump readouts in row 3. No write for the fuel transfer selector: no 2024 event was found for it.

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | (Stream Deck) | Returns to the MORE page | none | Back key |
| 1,2 | `BAT` | Dynamic Button | T2 | `K:TOGGLE_MASTER_BATTERY:1` [SDK-ELECE; CKL 7] | `(A:ELECTRICAL MASTER BATTERY:1, Bool)` [SDK-ELECV] | On/Off image |
| 1,3 | `GEN L` | Dynamic Button | T2 | `K:TOGGLE_ALTERNATOR1` [SDK-ELECE] | `(A:GENERAL ENG MASTER ALTERNATOR:1, Bool)` [SDK-ENGV] | On/Off image |
| 1,4 | `GEN R` | Dynamic Button | T2 | `K:TOGGLE_ALTERNATOR2` [SDK-ELECE] | `(A:GENERAL ENG MASTER ALTERNATOR:2, Bool)` [SDK-ENGV] | On/Off image |
| 1,5 | `AVIONICS` | Display Value | T3 | none | `(A:AVIONICS MASTER SWITCH:1, Bool)` [SDK-SYSV; CKL 19] | Mappings `0=OFF:1=ON` |
| 1,6 |  | Empty |  |  |  | STBY: the standby display switch (CKL 15) has no name until S-1 |
| 1,7 |  | Empty |  |  |  | EMER LT: the emergency lights switch (CKL 11) has no name until S-1 |
| 1,8 | `EXT PWR` | Display Value | T3 | none | `(A:EXTERNAL POWER ON:1, Bool)` [SDK-ELECV; CKL 86] | Mappings `0=OFF:1=ON` |
| 2,1 |  | Empty |  |  |  |  |
| 2,2 | `BUS V` | Display Value | T3 | none | `(A:ELECTRICAL MAIN BUS VOLTAGE:1, Volts)` [SDK-ELECV] | Format `2.1` |
| 2,3 | `BATT A` | Display Value | T3 | none | `(A:ELECTRICAL BATTERY LOAD:1, Amperes)` [SDK-ELECV; CKL 231] | Format `1.1` |
| 2,4 | `HYD PSI` | Display Value | T3 | none | `(A:HYDRAULIC PRESSURE:1, psi)` [SDK-SYSV; CKL 125] | Format `1.0` |
| 2,5 |  | Empty |  |  |  |  |
| 2,6 |  | Empty |  |  |  |  |
| 2,7 |  | Empty |  |  |  |  |
| 2,8 |  | Empty |  |  |  |  |
| 3,1 |  | Empty |  |  |  |  |
| 3,2 | `XFER` | Display Value | T3 | none | `(A:FUEL CROSS FEED, Enum)` [SDK-FUELV; CKL 366] | Format `1.0` |
| 3,3 | `PUMP L` | Display Value | T3 | none | `(A:GENERAL ENG FUEL PUMP ON:1, Bool)` [SDK-ENGV] | Mappings `0=OFF:1=ON` |
| 3,4 | `PUMP R` | Display Value | T3 | none | `(A:GENERAL ENG FUEL PUMP ON:2, Bool)` [SDK-ENGV] | Mappings `0=OFF:1=ON` |
| 3,5 |  | Empty |  |  |  |  |
| 3,6 |  | Empty |  |  |  |  |
| 3,7 |  | Empty |  |  |  |  |
| 3,8 |  | Empty |  |  |  |  |
| 4,1 |  | Empty |  |  |  |  |
| 4,2 |  | Empty |  |  |  |  |
| 4,3 |  | Empty |  |  |  |  |
| 4,4 |  | Empty |  |  |  |  |
| 4,5 |  | Empty |  |  |  |  |
| 4,6 |  | Empty |  |  |  |  |
| 4,7 |  | Empty |  |  |  |  |
| 4,8 |  | Empty |  |  |  |  |

## Key table: engine

Readouts only: engine 1 (left) in rows 1 and 3, engine 2 (right) in rows 2 and 4, the fuel quantities at 3,6
to 3,8. Starter and run/stop stay cockpit controls.

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | (Stream Deck) | Returns to the MORE page | none | Back key |
| 1,2 | `N1 L` | Display Value | T3 | none | `(A:TURB ENG N1:1, Percent)` [SDK-ENGV] | Format `1.1` |
| 1,3 | `N2 L` | Display Value | T3 | none | `(A:TURB ENG N2:1, Percent)` [SDK-ENGV] | Format `1.1` |
| 1,4 | `ITT L` | Display Value | T3 | none | `(A:TURB ENG ITT:1, Celsius)` [SDK-ENGV; CKL 74] | Format `1.0` |
| 1,5 | `FF L` | Display Value | T3 | none | `(A:TURB ENG FUEL FLOW PPH:1, Pounds per hour)` [SDK-ENGV] | Format `1.0` |
| 1,6 | `OIL P L` | Display Value | T3 | none | `(A:GENERAL ENG OIL PRESSURE:1, psi)` [SDK-ENGV] | Format `1.0` |
| 1,7 | `OIL T L` | Display Value | T3 | none | `(A:GENERAL ENG OIL TEMPERATURE:1, fahrenheit)` [SDK-ENGV] | Format `1.0` |
| 1,8 |  | Empty |  |  |  |  |
| 2,1 |  | Empty |  |  |  |  |
| 2,2 | `N1 R` | Display Value | T3 | none | `(A:TURB ENG N1:2, Percent)` [SDK-ENGV] | Format `1.1` |
| 2,3 | `N2 R` | Display Value | T3 | none | `(A:TURB ENG N2:2, Percent)` [SDK-ENGV] | Format `1.1` |
| 2,4 | `ITT R` | Display Value | T3 | none | `(A:TURB ENG ITT:2, Celsius)` [SDK-ENGV; CKL 74] | Format `1.0` |
| 2,5 | `FF R` | Display Value | T3 | none | `(A:TURB ENG FUEL FLOW PPH:2, Pounds per hour)` [SDK-ENGV] | Format `1.0` |
| 2,6 | `OIL P R` | Display Value | T3 | none | `(A:GENERAL ENG OIL PRESSURE:2, psi)` [SDK-ENGV] | Format `1.0` |
| 2,7 | `OIL T R` | Display Value | T3 | none | `(A:GENERAL ENG OIL TEMPERATURE:2, fahrenheit)` [SDK-ENGV] | Format `1.0` |
| 2,8 |  | Empty |  |  |  |  |
| 3,1 |  | Empty |  |  |  |  |
| 3,2 | `START L` | Display Value | T3 | none | `(A:GENERAL ENG STARTER:1, Bool)` [SDK-ENGV; CKL 66] | Mappings `0=OFF:1=ON` |
| 3,3 | `RUN L` | Display Value | T3 | none | `(A:GENERAL ENG COMBUSTION:1, Bool)` [SDK-ENGV; CKL 70] | Mappings `0=OFF:1=RUN` |
| 3,4 | `IGN L` | Display Value | T3 | none | `(A:TURB ENG IGNITION SWITCH EX1:1, Enum)` [SDK-ENGV] | Format `1.0` |
| 3,5 |  | Empty |  |  |  |  |
| 3,6 | `FUEL L` | Display Value | T3 | none | `(A:FUEL TANK LEFT MAIN QUANTITY, Gallons)` [SDK-FUELV] | Format `1.0` |
| 3,7 | `FUEL R` | Display Value | T3 | none | `(A:FUEL TANK RIGHT MAIN QUANTITY, Gallons)` [SDK-FUELV] | Format `1.0` |
| 3,8 | `FUEL TOT` | Display Value | T3 | none | `(A:FUEL TOTAL QUANTITY, Gallons)` [SDK-FUELV] | Format `1.0` |
| 4,1 |  | Empty |  |  |  |  |
| 4,2 | `START R` | Display Value | T3 | none | `(A:GENERAL ENG STARTER:2, Bool)` [SDK-ENGV; CKL 66] | Mappings `0=OFF:1=ON` |
| 4,3 | `RUN R` | Display Value | T3 | none | `(A:GENERAL ENG COMBUSTION:2, Bool)` [SDK-ENGV; CKL 70] | Mappings `0=OFF:1=RUN` |
| 4,4 | `IGN R` | Display Value | T3 | none | `(A:TURB ENG IGNITION SWITCH EX1:2, Enum)` [SDK-ENGV] | Format `1.0` |
| 4,5 |  | Empty |  |  |  |  |
| 4,6 |  | Empty |  |  |  |  |
| 4,7 |  | Empty |  |  |  |  |
| 4,8 |  | Empty |  |  |  |  |

## Key table: iceenv

Ice protection keys in row 1 (standard events), pressurization readouts in row 3.

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | (Stream Deck) | Returns to the MORE page | none | Back key |
| 1,2 | `ENG AI L` | Dynamic Button | T2 | `K:ANTI_ICE_TOGGLE_ENG1` [SDK-ENGE; CKL 129] | `(A:ENG ANTI ICE:1, Bool)` [SDK-ENGV] | On/Off image |
| 1,3 | `ENG AI R` | Dynamic Button | T2 | `K:ANTI_ICE_TOGGLE_ENG2` [SDK-ENGE; CKL 129] | `(A:ENG ANTI ICE:2, Bool)` [SDK-ENGV] | On/Off image |
| 1,4 | `WING/STAB` | Dynamic Button | T2 | `K:TOGGLE_STRUCTURAL_DEICE` [SDK-AMISCE; CKL 191] | `(A:STRUCTURAL DEICE SWITCH, Bool)` [SDK-SYSV] | On/Off image |
| 1,5 | `WSHLD` | Dynamic Button | T2 | `K:WINDSHIELD_DEICE_TOGGLE` [SDK-AMISCE] | `(A:WINDSHIELD DEICE SWITCH, Bool)` [SDK-SYSV] | On/Off image |
| 1,6 |  | Empty |  |  |  | P/S L: the left pitot/static heat button (CKL 239) has no name until S-1 (the SDK's pitot heat has no side) |
| 1,7 |  | Empty |  |  |  | P/S R: the right pitot/static heat button (CKL 239) has no name until S-1 |
| 1,8 |  | Empty |  |  |  |  |
| 2,1 |  | Empty |  |  |  |  |
| 2,2 |  | Empty |  |  |  |  |
| 2,3 |  | Empty |  |  |  |  |
| 2,4 |  | Empty |  |  |  |  |
| 2,5 |  | Empty |  |  |  |  |
| 2,6 |  | Empty |  |  |  |  |
| 2,7 |  | Empty |  |  |  |  |
| 2,8 |  | Empty |  |  |  |  |
| 3,1 |  | Empty |  |  |  |  |
| 3,2 |  | Empty |  |  |  | CLIMATE: the climate control selector (CKL 55) has no name until S-1 |
| 3,3 | `CAB ALT` | Display Value | T3 | none | `(A:PRESSURIZATION CABIN ALTITUDE, Feet)` [SDK-SYSV; CKL 149] | Format `1.0` |
| 3,4 | `CAB RATE` | Display Value | T3 | none | `(A:PRESSURIZATION CABIN ALTITUDE RATE, Feet/minute)` [SDK-SYSV] | Format `1.0` |
| 3,5 | `DIFF` | Display Value | T3 | none | `(A:PRESSURIZATION PRESSURE DIFFERENTIAL, psi)` [SDK-SYSV] | Format `1.1` |
| 3,6 | `DUMP` | Display Value | T3 | none | `(A:PRESSURIZATION DUMP SWITCH, Bool)` [SDK-SYSV] | Mappings `0=OFF:1=ON` |
| 3,7 |  | Empty |  |  |  |  |
| 3,8 |  | Empty |  |  |  |  |
| 4,1 |  | Empty |  |  |  |  |
| 4,2 |  | Empty |  |  |  |  |
| 4,3 |  | Empty |  |  |  |  |
| 4,4 |  | Empty |  |  |  |  |
| 4,5 |  | Empty |  |  |  |  |
| 4,6 |  | Empty |  |  |  |  |
| 4,7 |  | Empty |  |  |  |  |
| 4,8 |  | Empty |  |  |  |  |

## Key table: lights

The lights that are not on the main page. Which of them the CJ4 has is not confirmed; a key whose light the
CJ4 lacks does nothing (test item).

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | (Stream Deck) | Returns to the MORE page | none | Back key |
| 1,2 | `RECOG` | Dynamic Button | T2 | `K:TOGGLE_RECOGNITION_LIGHTS` [SDK-ELECE] | `(A:LIGHT RECOGNITION, Bool)` [SDK-SYSV] | On/Off image |
| 1,3 | `WING` | Dynamic Button | T2 | `K:TOGGLE_WING_LIGHTS` [SDK-ELECE] | `(A:LIGHT WING, Bool)` [SDK-SYSV] | On/Off image |
| 1,4 |  | Empty |  |  |  |  |
| 1,5 |  | Empty |  |  |  |  |
| 1,6 |  | Empty |  |  |  |  |
| 1,7 |  | Empty |  |  |  |  |
| 1,8 |  | Empty |  |  |  |  |
| 2,1 |  | Empty |  |  |  |  |
| 2,2 | `BELTS` | Dynamic Button | T2 | `K:CABIN_SEATBELTS_ALERT_SWITCH_TOGGLE` [SDK-AMISCE] | `(A:CABIN SEATBELTS ALERT SWITCH, Bool)` [SDK-SYSV] | On/Off image |
| 2,3 | `NO SMOKE` | Dynamic Button | T2 | `K:CABIN_NO_SMOKING_ALERT_SWITCH_TOGGLE` [SDK-AMISCE] | `(A:CABIN NO SMOKING ALERT SWITCH, Bool)` [SDK-SYSV] | On/Off image |
| 2,4 |  | Empty |  |  |  | PASS SAFE: the pass lights safety button (CKL 105) has no name until S-1 |
| 2,5 |  | Empty |  |  |  |  |
| 2,6 |  | Empty |  |  |  |  |
| 2,7 |  | Empty |  |  |  |  |
| 2,8 |  | Empty |  |  |  |  |
| 3,1 |  | Empty |  |  |  |  |
| 3,2 | `CABIN` | Dynamic Button | T2 | `K:TOGGLE_CABIN_LIGHTS` [SDK-ELECE] | `(A:LIGHT CABIN, Bool)` [SDK-SYSV] | On/Off image |
| 3,3 | `PANEL` | Dynamic Button | T2 | `K:PANEL_LIGHTS_TOGGLE` [SDK-ELECE] | `(A:LIGHT PANEL, Bool)` [SDK-SYSV] | On/Off image |
| 3,4 |  | Empty |  |  |  |  |
| 3,5 |  | Empty |  |  |  |  |
| 3,6 |  | Empty |  |  |  |  |
| 3,7 |  | Empty |  |  |  |  |
| 3,8 |  | Empty |  |  |  |  |
| 4,1 |  | Empty |  |  |  |  |
| 4,2 |  | Empty |  |  |  |  |
| 4,3 |  | Empty |  |  |  |  |
| 4,4 |  | Empty |  |  |  |  |
| 4,5 |  | Empty |  |  |  |  |
| 4,6 |  | Empty |  |  |  |  |
| 4,7 |  | Empty |  |  |  |  |
| 4,8 |  | Empty |  |  |  |  |

## What the keys do

- **Main, row 1:** BAT switches the battery by the standard event, lit from the battery switch SimVar. N1
  shows the left engine's N1 in percent. PARK toggles the parking brake by the standard event, lit from the
  brake SimVar (the same event failed in the VisionJet). GEAR shows the gear handle (`UP` or `DOWN`) and
  does nothing on a press. FLAPS shows the flap handle position as a number (0 = up): a press moves it one
  step out, a long press (half a second or more) one step in.
- **Main, row 2:** AP, HDG, ALT, VS, NAV, APR, FLC and FD switch the autopilot, its modes and the flight
  director by the standard events, each lit from its own SimVar.
- **Main, row 3:** COM1 shows the active and standby frequency, a press swaps them. XPDR shows the
  transponder code. ATC and MAP open and close the sim's ATC and map windows (fixed images, a sim window has
  no state). CDI shows `GPS` or `VLOC`, a press toggles it. BARO shows the altimeter setting; a press sends
  the standard baro event (`K:BAROMETRIC`), a long press the standard pressure event
  (`K:BAROMETRIC_STD_PRESSURE`).
- **Main, row 4:** NAV LT, BCN, STRB, LDG, TAXI, PITOT and ICE send the standard events, each lit from its
  own SimVar. ICE sends the same event and reads the same SimVar as ICE/ENV 1,4 WING/STAB.
- **Trim:** TRIM UP and TRIM DN step the elevator trim, AIL L and AIL R the aileron trim, RUD L and RUD R
  the rudder trim, by the standard events; the gauges show the positions from -100 to 100 percent. The six
  keys repeat while held, at most 8 s per hold.
- **Autopilot:** the main page's mode keys again, plus BC (back course), YD (yaw damper) and IAS/MACH (the
  speed target in knots or Mach), each by its standard event and lit from its SimVar. BANK shows the bank
  limit's number: a press raises it, a long press lowers it. HDG+/-, CRS+/-, ALT+/-, VS+/- and SPD+/- step
  the heading bug, the NAV1 course, the selected altitude, the vertical speed target and the speed target
  and repeat while held; HDG BUG, CRS1, ALT SEL, VS TGT, SPD TGT and MACH TGT show them and do nothing on a
  press.
- **Radios:** NAV1, NAV2 and COM2 show active and standby, a press swaps them; the ID keys show the station
  idents. MHZ+/- and KHZ+/- step the standby frequency and BARO+/- the altimeter setting, all by standard
  events with hold to repeat. MIC1 and MIC2 pick the radio that transmits, lit from the radio's own transmit
  SimVar.
- **Systems:** BAT (as on main), GEN L and GEN R by the standard events, each lit from its SimVar. AVIONICS,
  EXT PWR, BUS V, BATT A, HYD PSI, XFER, PUMP L and PUMP R are readouts and do nothing on a press. XFER
  shows the raw number of the fuel cross feed SimVar; its words come after the test.
- **Engine:** readouts only: N1 and N2 (percent), ITT (degrees Celsius), fuel flow (pounds per hour), oil
  pressure (psi) and temperature (degrees Fahrenheit), START, RUN and IGN per engine, and the left, right
  and total fuel in gallons. IGN shows the raw number of the ignition switch SimVar; its words come after
  the test.
- **ICE/ENV:** ENG AI L, ENG AI R, WING/STAB and WSHLD by the standard events, each lit from its SimVar. CAB
  ALT, CAB RATE, DIFF and DUMP are readouts.
- **Lights:** RECOG, WING, BELTS, NO SMOKE, CABIN and PANEL by the standard events, each lit from its
  SimVar.
- **Copied pages:** views, sim rate, V-speeds and transponder work as on the C172 (their docs above), the
  COM pad as on the VisionJet (above); they use standard events, SimVars and the shared Lua scripts, nothing
  C172-specific.

## Which route each key uses

The rule: the cockpit switches of the MSFS 2024 C172 and VisionJet drive input events (B-vars), sometimes
with another index than the standard event, so a switch key takes the aircraft's input event first. The
CJ4's input event list does not exist yet (S-1). Until it does, 22 switch keys use the standard event with
the SimVar as their read, and a control with no standard event is a readout (AVIONICS) or empty. An input
event from the list replaces a standard event in a later unit.

| Keys | Event and read | Source |
|---|---|---|
| main 1,1 and systems 1,2 `BAT` | `K:TOGGLE_MASTER_BATTERY:1`, `(A:ELECTRICAL MASTER BATTERY:1, Bool)` | SDK-ELECE, SDK-ELECV |
| main 1,4 `PARK` | `K:PARKING_BRAKES`, `(A:BRAKE PARKING POSITION, Bool)` | AM; failed in the VisionJet; SDK-GEARV |
| main 4,1 `NAV LT`, 4,2 `BCN`, 4,3 `STRB`, 4,4 `LDG`, 4,5 `TAXI` | `K:TOGGLE_NAV_LIGHTS`, `K:TOGGLE_BEACON_LIGHTS`, `K:STROBES_TOGGLE`, `K:LANDING_LIGHTS_TOGGLE`, `K:TOGGLE_TAXI_LIGHTS`, each with its `LIGHT` SimVar | SDK-ELECE, SDK-SYSV |
| main 4,6 `PITOT` | `K:PITOT_HEAT_TOGGLE`, `(A:PITOT HEAT, Bool)` | SDK-AMISCE, SDK-SYSV |
| main 4,7 `ICE`, iceenv 1,4 `WING/STAB` | `K:TOGGLE_STRUCTURAL_DEICE`, `(A:STRUCTURAL DEICE SWITCH, Bool)` | SDK-AMISCE, SDK-SYSV |
| systems 1,3 `GEN L`, 1,4 `GEN R` | `K:TOGGLE_ALTERNATOR1`, `K:TOGGLE_ALTERNATOR2`, `(A:GENERAL ENG MASTER ALTERNATOR:1, Bool)` and `:2` | SDK-ELECE, SDK-ENGV |
| iceenv 1,2 `ENG AI L`, 1,3 `ENG AI R` | `K:ANTI_ICE_TOGGLE_ENG1`, `K:ANTI_ICE_TOGGLE_ENG2`, `(A:ENG ANTI ICE:1, Bool)` and `:2` | SDK-ENGE, SDK-ENGV |
| iceenv 1,5 `WSHLD` | `K:WINDSHIELD_DEICE_TOGGLE`, `(A:WINDSHIELD DEICE SWITCH, Bool)` | SDK-AMISCE, SDK-SYSV |
| lights 1,2 `RECOG`, 1,3 `WING`, 3,2 `CABIN`, 3,3 `PANEL` | `K:TOGGLE_RECOGNITION_LIGHTS`, `K:TOGGLE_WING_LIGHTS`, `K:TOGGLE_CABIN_LIGHTS`, `K:PANEL_LIGHTS_TOGGLE`, each with its `LIGHT` SimVar | SDK-ELECE, SDK-SYSV |
| lights 2,2 `BELTS`, 2,3 `NO SMOKE` | `K:CABIN_SEATBELTS_ALERT_SWITCH_TOGGLE`, `K:CABIN_NO_SMOKING_ALERT_SWITCH_TOGGLE`, each with its SimVar | SDK-AMISCE, SDK-SYSV |

Everything else uses the routes the C172 pages use: standard events and SimVars, the camera and transponder
SimVar writes, and the shared scripts. The autopilot keys use the standard events too; the CJ4's own buttons
may be input events (S-1, S-4). Every index is the pilot's or the left side's (1), with 2 for the right
engine, generator and second radios.

## Hold to repeat

The step keys repeat while held, by the route of the VisionJet profile
([visionjet-sf50.md](visionjet-sf50.md), "Hold to repeat"). PilotsDeck has no repeat for keys (PD-HOLD), so
the repeat runs in this profile's own script, `Scripts/XL24-CJ4.lua`, with the VisionJet script's code,
speed profiles and limits and its own key table of 30 codes, one code per key. The VisionJet's hold test in
the sim has not been run yet, so this is not proven there either.

**How it works.** Each step key is a Simple Button with **Hold Switch** on and the command type Lua
Function: key down runs `lua:XL24-CJ4:HOLD(n)`, key up `lua:XL24-CJ4:RELEASE(n)` (README 2.1.2). n is the
key's code (table below). PilotsDeck runs each Lua call on its own task, and `Sleep` pauses only that task
(PD-HOLD), so HOLD can wait in a loop while RELEASE runs; two calls of one script at once are a hand test.
The times below count 50 ms sleeps, so the real times can run a little longer, and the sim itself may speed
up repeated trim events (SDK-FCE).

- **A short press** sends one step at key down.
- **Held**, the key waits its delay, then sends more steps, faster the longer it is held.
- **It stops** at key up (within about 50 ms), at the key's step cap, or after about 20 s held, whichever
  comes first. If a key up never reaches the script (for example when the page changes while the key is
  held), the repeat runs on after the release until the cap or the 20 s limit ends it (trim: about 8 s); the
  next press of that key resyncs its count. Change pages only with no step key held.
- **Open point (hand test):** if the app sends the key up of a key held across a page change to the key now
  at its position, PilotsDeck runs that key's key-up command although its key down never came (PD-HOLD).
  From trim the main page's keys come under the finger: HDG (2,2), APR (2,6), FD (2,8), BARO (3,6) and BCN
  (4,2) are PilotsDeck keys there. The other way, with a main page key held while TRIM opens, the key up
  would run the RELEASE of the trim key at its position without its HOLD: nothing runs on from it, but that
  code then gives one step per press and no repeat until the script is loaded again (for example after a
  restart of the Stream Deck app).
- A key with Hold Switch can't have a long press command (README 2.1.2), so no step key has one.
- The step keys show fixed images; the readouts beside them (autopilot row 3, radios row 1, the trim gauges)
  show the sim's values, so a step the aircraft ignores shows as a readout that does not move.
- The script writes no variable and sends only the events of its key table; it does not check which aircraft
  is loaded.

| Codes | Keys | Event the script sends | Profile, cap |
|---|---|---|---|
| 1, 2 | autopilot 2,2 `HDG+`, 4,2 `HDG-` | `K:HEADING_BUG_INC`, `K:HEADING_BUG_DEC` (SDK-APE) | fast, 360 |
| 3, 4 | autopilot 2,3 `CRS+`, 4,3 `CRS-` | `K:VOR1_OBI_INC`, `K:VOR1_OBI_DEC` (SDK-RADE) | fast, 360 |
| 5, 6 | autopilot 2,4 `ALT+`, 4,4 `ALT-` | `K:AP_ALT_VAR_INC`, `K:AP_ALT_VAR_DEC` (SDK-APE) | alt, 400 |
| 7, 8 | autopilot 2,5 `VS+`, 4,5 `VS-` | `K:AP_VS_VAR_INC`, `K:AP_VS_VAR_DEC` (SDK-APE) | slow, 40 |
| 9, 10 | autopilot 2,6 `SPD+`, 4,6 `SPD-` | `K:AP_SPD_VAR_INC`, `K:AP_SPD_VAR_DEC` (SDK-APE) | fast, 200 |
| 11, 12 | radios 2,8 `BARO+`, 3,8 `BARO-` | `K:KOHLSMAN_INC`, `K:KOHLSMAN_DEC` (SDK-INSTE; weak, as visionjet-sf50.md) | baro, 200 |
| 13 to 18 | radios 2,2 to 2,7 (NAV1, NAV2, COM2 `MHZ+` / `KHZ+`) | `K:NAV1_RADIO_WHOLE_INC`, `K:NAV1_RADIO_FRACT_INC`, `K:NAV2_RADIO_WHOLE_INC`, `K:NAV2_RADIO_FRACT_INC`, `K:COM2_RADIO_WHOLE_INC`, `K:COM2_RADIO_FRACT_INC` (SDK-RADE) | MHZ slow, 30; KHZ fast, 200 |
| 19 to 24 | radios 3,2 to 3,7 (NAV1, NAV2, COM2 `MHZ-` / `KHZ-`) | the same six with `_DEC` (SDK-RADE) | MHZ slow, 30; KHZ fast, 200 |
| 25, 26 | trim 2,2 `TRIM UP`, 4,2 `TRIM DN` | `K:ELEV_TRIM_UP`, `K:ELEV_TRIM_DN` (SDK-FCE) | trim, 160 |
| 27, 28 | trim 2,6 `AIL L`, 2,8 `AIL R` | `K:AILERON_TRIM_LEFT`, `K:AILERON_TRIM_RIGHT` (SDK-FCE) | trim, 160 |
| 29, 30 | trim 3,6 `RUD L`, 3,8 `RUD R` | `K:RUDDER_TRIM_LEFT`, `K:RUDDER_TRIM_RIGHT` (SDK-FCE) | trim, 160 |

| Profile | Delay | Then (from the end of the delay) |
|---|---|---|
| fast | 400 ms | 10 steps/s to 1.5 s, 20/s to 3 s, then 60/s (3 per 50 ms) |
| alt | 400 ms | 10/s to 1.5 s, then 20/s |
| slow | 400 ms | 6.7/s (one per 150 ms) |
| baro | 400 ms | 10/s to 2 s, then 20/s |
| trim | 250 ms | 20/s, no speed-up (the cap of 160 steps comes at about 8 s) |

The cap counts the first step. Never repeated: the mode keys, FLAPS, BANK, the switches, the sim rate keys
and the pads. The times are working values: if the repeat is too slow or too fast, only the script's
`PROFILES` and `KEYS` tables change.

## What each key holds

The key kinds of [phase2-main-page.md](phase2-main-page.md), "What each key holds": every key is a copy of a
real saved key with only the listed fields changed (the generator does this).

| Kind | Action, copied from | Keys here |
|---|---|---|
| T2 K-event with SimVar read | Dynamic Button, the Phase 1 AP key (`p1:3,0`): Command Address a `K:` event, Value Address a SimVar, so the On and Off images both follow the read; PARK copies the Phase 1 PARK key (`p1:1,0`); `1X` runs a Lua Function | the mode keys and switches on main, autopilot, systems, iceenv and lights; xpdr 3,2; radios 4,6, 4,7; simrate 1,2 |
| T2 (template) | the Phase 1 AP key (`p1:3,0`) as it is | main 2,1 |
| T3 Display Value | the Phase 1 readout key (`p1:2,0`): Value Address, Format or Mappings; command none, or a press (and long press) command | every readout |
| T4 COM Radio | `com_radio` (templates.json) | main 3,1; compad 1,2; radios 1,2, 1,4, 1,6 |
| T5 Simple Button | `simple_button` with the AP key's states: a `K:` event, a fixed image, no read | main 3,3, 3,4; simrate 1,3, 1,5; xpdr 3,3 |
| T6 camera and transponder write | `avar_dynamic_button` (templates.json): writes and reads the same SimVar | views 1,2, 1,3; xpdr 2,2 to 2,4 |
| T8 pad key | Simple Button with the command type Lua Function, a fixed image, no read ([phase2-com1-pad.md](phase2-com1-pad.md), "What each key holds") | xpdr: the digits, CLR and ENT |
| T8L lit pad key | Dynamic Button, the Phase 1 AP key (`p1:3,0`): command type Lua Function (14), Value Address `X:XL24_COMPAD_LIT_<key>`, Image Mapping on, title alignment middle ([visionjet-sf50.md](visionjet-sf50.md), "What each key holds") | compad: the digits, CLR and ENT |
| T9 Display Gauge | `display_gauge` (templates.json) | trim 2,7 and 3,7 (horizontal), 3,4 (vertical), each with a center line |
| H1 hold to repeat | as T5, with the command type Lua Function (14), Command `lua:XL24-CJ4:HOLD(n)`, alternate command (`AddressActionOff`) `lua:XL24-CJ4:RELEASE(n)`, Hold Switch on and no long press (README 2.1.1, 2.1.2) | autopilot 2,2 to 2,6, 4,2 to 4,6; radios 2,2 to 2,8, 3,2 to 3,8; trim 2,2, 2,6, 2,8, 3,6, 3,8, 4,2 |

"Folder" and "Back" are the Stream Deck app's own keys. Title sizes follow [navigation.md](navigation.md),
"Rules".

## Profile Manager mapping

A package can't carry an aircraft mapping ([package.md](package.md)), and the CJ4 has **no search string
yet**: PilotsDeck logs the aircraft's string at the first CJ4 flight (S-1). Until then pick `MSFS2024 CJ4`
on the Stream Deck by hand. Once the string is known:

1. Open the Profile Manager, **Profile Mapping**, and pick `MSFS2024 CJ4`.
2. Check "StreamDeck Profile modified for Switching".
3. Type a part of the logged aircraft string that only the CJ4 has, press **Plus**, then **Save**.

A lead only, not confirmed: the CJ4's package has a folder `html_ui\airplanes\asobo_cj4`, so the aircraft
string may hold `asobo_cj4`.

## What the keys show when the CJ4 isn't there

- No sim, or no flight: PilotsDeck's own idle and waiting images, as on the other profiles.
- Another aircraft: the readouts and lit keys read standard SimVars (the two ENTRY readouts and the COM pad's
  twelve keys read internal variables), so they show that aircraft's own values (what the second engine's
  readouts show in a single-engine aircraft is not tested).
- **Keys act on any aircraft that has their event:** the switches, FLAPS, PARK, the autopilot, radio, trim
  and transponder keys are standard events and SimVar writes and move the loaded aircraft's own controls
  where it has them. Do not press them in another aircraft. The step keys act the same way and repeat while
  held (the script does not check the aircraft).
- The views, sim rate, ATC and MAP keys act on the sim itself, in any aircraft.
- If the CJ4 ignores a standard event, the key's read stays where it was and the key's image does not
  change: the hand test records it.

## Not on these pages, and why

**Kept for a later unit.** Five pages of the research page's draft layout and one checklist key use the WT21
key names, and nobody has tried those names in the default CJ4. They wait for that test (sim step S-4 of
[cj4-research.md](cj4-research.md)). Their positions are empty until then:

- MORE 1,2 DCP (the display control panel), MORE 1,3 CCP (the cursor control panel);
- MORE 2,6 FMS, 2,7 FMS ABC, 2,8 FMS 123 (the FMC's function and line select, letter and number keys);
- checklist 1,2 CKLST (the cursor control panel's checklist key, likely the key that shows the checklist).
  The page itself stays, with its back key, as on the C172.

**The eight gaps** (no name until S-1's input event list, or no function):

- main 1,3: no fuel pump key (the CJ4's pumps are readouts, systems 3,3 and 3,4);
- autopilot 1,8 VNAV: no 2024 VNAV event was found (SDK-APE);
- systems 1,6 STBY (the standby display switch, CKL 15) and 1,7 EMER LT (the emergency lights switch, CKL
  11);
- iceenv 1,6 P/S L and 1,7 P/S R (the pitot/static heat buttons, CKL 239; the SDK's pitot heat has no side,
  main 4,6 PITOT sends it) and 3,2 CLIMATE (the climate control selector, CKL 55);
- lights 2,4 PASS SAFE (the pass lights safety button, CKL 105).

The copied empty positions stay as on their pages: vspeeds 1,5 and 2,3 (Vx and Vno have no SimVar), xpdr 1,7
and 1,8 (codes use the digits 0 to 7).

**Never on these pages:** a gear key, engine start, stop and ignition keys (readouts only), fuel transfer
writes, TOGA, an autothrottle key (none found), the copilot's side. No key is guarded: no key here needs a
guard.

## Fallbacks

Use one only if the checklist shows the main route does not work, and say which one you used. None is
tested. A key that fails with no working fallback becomes a readout (command none) or Empty, and its row in
aircraft-mappings.md says "does not work".

| Key | If it fails | Fallback | Source |
|---|---|---|---|
| The 22 switch keys of "Which route each key uses" | The event does nothing, or the key does not follow the cockpit switch | The control's input event once S-1 lists it; until then a readout of the key's read (command none) | [cj4-research.md](cj4-research.md), S-1 |
| PARK | `K:PARKING_BRAKES` does nothing or the brake springs back (as in the VisionJet) | The parking brake's input event once S-1 lists it; else readout only | [visionjet-sf50.md](visionjet-sf50.md) |
| Autopilot mode keys, BC, YD, BANK, IAS/MACH | The CJ4's autopilot panel ignores the standard event | The button's input event after S-1 and S-4; else readout only | [cj4-research.md](cj4-research.md), S-4 |
| CRS+, CRS- | `K:VOR1_OBI_INC` / `_DEC` do not move the course | Readout only (CRS1); the keys Empty | SDK-RADE |
| SPD+, SPD- | The events do not move the CJ4's speed target, or SPD TGT does not show it | After a look at the control (S-3), another event in the script's key table; else Empty | SDK-APE |
| BARO press and long press | `K:BAROMETRIC` or `K:BAROMETRIC_STD_PRESSURE` does nothing | Readout only; no STD | SDK-INSTE |
| BARO+, BARO- | `K:KOHLSMAN_INC` / `_DEC` do nothing | The column's two step keys Empty, BARO 1,8 stays a readout | SDK-INSTE |
| Hold to repeat | The keys do not repeat, or a repeat runs on after release | As the VisionJet: a global script with `RunInterval`; else no repeat and a long press that sends a five-step burst (neither is built) | PD-HOLD; [visionjet-sf50.md](visionjet-sf50.md) |
| Repeat speed | Too slow or too fast | Only the script's `PROFILES` and `KEYS` values change | |
| XFER, IGN L, IGN R | The raw numbers are unclear | Mappings from the recorded numbers per selector position | SDK-FUELV, SDK-ENGV |
| FLAPS | The number per detent is unclear | Mappings after the test | SDK-CTLV |
| HYD PSI, ITT, OIL T, fuel readouts | The unit or scale does not match the cockpit | Another unit or format after the test | SDK-ENGV, SDK-FUELV, SDK-SYSV |
| COCKPIT, EXTERNAL; XPDR STBY, ON, ALT | The SimVar writes do nothing in the CJ4 | Those five keys become their readouts (command none) | SDK-CAMV, SDK-RADV |
| COM pad ENT | The CJ4's COM1 does not take `K:COM_STBY_RADIO_SET_HZ` | None yet: ENT stays dark and the result is recorded | [phase2-com1-pad.md](phase2-com1-pad.md) |
| COM pad press feedback | A fast next press is late or lost, a key stays green or shows the wait image, or ENT never turns green though COM1 shows the frequency | The VisionJet's three COM pad rows, for both aircraft | [visionjet-sf50.md](visionjet-sf50.md), "Fallbacks"; PD-PAD |

Also hand-test items: the C172's V-speed SimVars on a jet (no fallback yet), and the generators as the SDK's
alternators (fallback: the first row).

## How to test

Run [tests/manual-checklist.md](../tests/manual-checklist.md), section "Citation CJ4 profile (CJ-1)". The
sim step S-1 (the input event list and the aircraft string) comes first. As on the other profiles, check
both directions: press a key and watch the cockpit, then **work the control in the cockpit with the mouse
and check that the key follows without a key being pressed.** Never press GEAR or an engine key expecting an
action (they are readouts). Hold each step key for 1, 3 and 10 s and check that the repeat stops at once on
release and never runs on. Run the COM pad's fast press steps before its other steps. Record which keys do
nothing (their input event is the fix), the step per press of ALT and BARO+/-, the flap number per detent,
the XFER and IGN numbers per selector position and every unit that does not match the cockpit.

## When it passes

1. Any change found in the test goes into `tools/profilegen/cj4.json` and this doc; then the profile is
   regenerated (not exported from the app) and imported again.
2. Fill in the "Verified" column of the rows in aircraft-mappings.md ("Cessna Citation CJ4 (MSFS 2024
   default, CJ-1)") with the date and sim version, for each function that passed; mark a row "does not work"
   where a key failed.

## Sources

Bracket words that are remarks, not sources: "failed in the SF50", "weak", "as visionjet-sf50.md" and
"written by the script".

| Tag | Source |
|---|---|
| CKL | The default CJ4's checklist file, in its package in the sim's streamed-package cache (label texts only; cited by line), read 2026-11-18 |
| SDK-APE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-autopilot-and-flight-assistance-events/, read 2026-11-18 |
| SDK-APV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-autopilot-and-assistant-variables/, read 2026-11-18 |
| SDK-ELECE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-electrical-events/, read 2026-11-18 |
| SDK-ELECV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-electrics-variables/ (as in [visionjet-g2-research.md](visionjet-g2-research.md)) |
| SDK-AMISCE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-miscellaneous-events/, read 2026-11-18 |
| SDK-ENGE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-engine-events/, read 2026-11-18 |
| SDK-ENGV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-engine-variables/, read 2026-11-18 |
| SDK-FUELV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-fuel-variables/, read 2026-11-18 |
| SDK-SYSV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-system-variables/, read 2026-11-18 |
| SDK-FCE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-flight-control-events/, read 2026-11-18 |
| SDK-CTLV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-control-variables/, read 2026-11-18 |
| SDK-GEARV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-brake-and-landing-gear-variables/ (as in [visionjet-g2-research.md](visionjet-g2-research.md)) |
| SDK-FMV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-flight-model-variables/ (as in [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md)) |
| SDK-RADE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-radio-navigation-events/ (as in [phase2-main-page.md](phase2-main-page.md)) |
| SDK-RADV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-radio-navigation-variables/ (as in [phase2-main-page.md](phase2-main-page.md)) |
| SDK-INSTE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-instrumentation-events/ (as in [phase2-main-page.md](phase2-main-page.md)) |
| SDK-MISCE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/miscellaneous-events/ (as in [phase2-main-page.md](phase2-main-page.md)) |
| SDK-CAMV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/camera-variables/ (as in [phase2-trim-views.md](phase2-trim-views.md)) |
| SDK-UNITS | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/simulation-variable-units/ (as in [phase2-main-page.md](phase2-main-page.md)) |
| SDK-ENVV, SDK20-CTLV | The SDK pages named in [phase2-sim-rate.md](phase2-sim-rate.md) (SDK-ENVV) and [phase2-trim-views.md](phase2-trim-views.md) (SDK20-CTLV), "Sources" |
| README | PilotsDeck README, https://github.com/Fragtality/PilotsDeck/blob/master/README.md (read 2026-11-16): 2.1 (Second command on a long press, >= 500 ms), 2.1.1 (A-Var `(A:Name:Index, Unit)`, B-Var "The Name of the B-Var with preceding `B:`!", K-Var, L-Var with On and Off values, H-Var "can't be read"), 2.1.2, 3.5.1 |
| INTERNAL, LUAFUNC (after README 2.1.1) | The internal variable (`X:`) and Lua Function (`lua:`) address kinds of README 2.1.1, as [phase2-com1-pad.md](phase2-com1-pad.md) and [visionjet-sf50.md](visionjet-sf50.md), "Sources" |
| PD-HOLD | PilotsDeck README at commit 11bdf1f (https://raw.githubusercontent.com/Fragtality/PilotsDeck/11bdf1f/README.md), read 2026-11-17 (V-3): 2.1 (a Second Command when pressed 500 ms or longer, sent once), 2.1.2 (Hold Switch: the normal command on key down, the alternate command on key up; with Hold Switch no long press command), 3.5 (standard scripts in `Scripts`, their state kept while loaded), 3.5.1 (`SimCommand`, `Sleep`, `Log`), 3.5.2 (global scripts, `RunInterval`), 4.1 (`TickDelay` only between encoder ticks); and its source at 11bdf1f7daf4828f822c18919952fe5b66153e58: `Plugin/Actions/Simple/ActionBaseSimple.cs` 534 to 536, 549, 563 to 566 (a holdable command at key down, its key-up form at key up, nothing repeats), `Plugin/Simulator/SimCommand.cs` 77 to 82, 94 to 97 (a Lua Function is holdable), `Plugin/Simulator/ConnectorNone.cs` 45 to 48 (each Lua call on its own task), `Plugin/Resources/Scripts/ManagedScript.cs` 359 (`SimCommand` queues the event), 406 (`Sleep` is `Thread.Sleep`); V-UX, read 2026-11-23 at the same commit: `Plugin/Actions/ActionManager.cs` `OnKeyUp` (a key up goes to the key whose context the app names; a key no longer registered is not found), `Plugin/Actions/Simple/ActionBaseSimple.cs` `OnKeyUp` (runs the key-up command without a check that the key down came first) |
| PD-PAD | PilotsDeck README and source at commit 11bdf1f7daf4828f822c18919952fe5b66153e58 (https://github.com/Fragtality/PilotsDeck), read 2026-11-24 (V-PAD): README 2.1.1 (INTERNAL), 2.2.2 (Image Mapping), 2.3 (Dynamic Button); `Plugin/Actions/Simple/ActionSwitchDisplay.cs` `Refresh` (the background, then with Image Mapping the mapped image for the value), `Plugin/Actions/Simple/ActionSwitch.cs` `Refresh` (a Simple Button draws its background only), `Plugin/Actions/Simple/ActionBaseSimple.cs` (`DrawTitle` draws only on encoders, so the Stream Deck app draws a key's title; `OnKeyUp` sends the command), `Plugin/Actions/Simple/ValueState.cs` `GetValueMapped` (an exact entry is compared as text; no match returns the value itself, so each value needs its entry), `Plugin/Resources/Images/ImageMapping.cs`, `Plugin/Resources/Images/ManagedImage.cs` (a missing file shows the wait image), `Plugin/Resources/VariableManager.cs` and `Plugin/Resources/Variables/VariableString.cs` (an `X:` variable is a string that starts as `0`), `Plugin/Simulator/ConnectorNone.cs` (an `X:` write needs no sim and does nothing for a variable no key or script registered; each Lua call on its own task), `Plugin/Resources/ScriptManager.cs` `RunFunction` (no script call without a ready sim), `Plugin/AppConfiguration.cs` (`IntervalDeckRefresh` 50 ms, `IntervalUnusedRessources` 60 s); `Images/None.png` is the Background of the saved `avar_dynamic_button` template (`tools/profilegen/templates.json`); https://docs.elgato.com/streamdeck/sdk/references/manifest (`TitleAlignment` top, middle, bottom) |
| PD-SRC, P2-6 route ruling | As [phase2-sim-rate.md](phase2-sim-rate.md) and [phase2-com1-pad.md](phase2-com1-pad.md), "Sources" ("PD-SRC string A-Var": as [phase3-radios.md](phase3-radios.md), "Sources") |
| AM | [aircraft-mappings.md](aircraft-mappings.md): verified on the 2024 C172 (2026-11-11), not on the CJ4 |
| HH-MS | HubHop presets for "Cirrus SF50 Vision Jet (MSFS2024)" (vendor Microsoft), https://hubhop.mobiflight.com/presets/?aircraft=Cirrus+SF50+Vision+Jet+%28MSFS2024%29, read 2026-11-16, as in [visionjet-sf50.md](visionjet-sf50.md), "Sources": a source for the VisionJet, not for the CJ4 (the preset "SF50 Baro PUSH STD" sends `K:BAROMETRIC_STD_PRESSURE` and then writes an input event of the SF50, so it does not show that the event alone is enough, [visionjet-g2-research.md](visionjet-g2-research.md)) |
