# Phase 3: engine and fuel page, Cessna 172 G1000

**Status: generated, not yet sim-tested.** The page is in the generated profile, but nothing has been tried
in the app or the sim yet. Every new name below is recorded as "Unverified" in
[aircraft-mappings.md](aircraft-mappings.md) ("Phase 3 engine and fuel page") until the checks in
[tests/manual-checklist.md](../tests/manual-checklist.md), section "P3-5: Engine and fuel page (C172 G1000)",
pass.

Goal: the G1000 engine indication system (EIS) on the deck, read only, in the EIS order: RPM, fuel flow, oil
pressure, oil temperature, EGT and vacuum as readouts, the fuel quantity left and right as two bar gauges, and
the bus volts and battery amps as readouts. Nothing on the page writes to the sim: there is no command, no
script and no engine control (the main page's rule: no engine command on the deck).

The page is part of the generated profile `MSFS2024 C172 G1000` (same file, same name, same import as the
main page: see [phase2-main-page.md](phase2-main-page.md), "Import the profile"). It needs **no script**. The
table below is the reference for what each key holds; `tools/profilegen/check.py` compares the profile with
the "Key table: engine" section key by key.

Nothing on this page uses keyboard bindings, vJoy or anything tied to a controller: every key only reads a
SimVar, so it works the same with the Xbox Elite controller and the T.16000M + TWCS.

## Where the page sits

A second-level folder page **engine**, opened by the folder key `ENGINE` at **MORE 2,3** (next to `SYSTEMS`
at 2,2; [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md), "Key table: more"). How the pages connect:
[navigation.md](navigation.md).

## Layout: engine

Positions are **row,column**, 1-based, row 1 at the top. 1,1 is the back key (it returns to MORE), as on
every child page. Row 1 holds the EIS readouts in the EIS order, row 2 the two fuel gauges, row 3 the
electrical readouts. Column 1 below the back key stays empty, as on the systems page; row 4 is empty.

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | RPM | FFLOW | OIL PRES | OIL TEMP | EGT | VAC | |
| **Row 2** | | FUEL L | FUEL R | | | | | |
| **Row 3** | | BUS V | BATT A | | | | | |
| **Row 4** | | | | | | | | |

## Key table: engine

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to MORE | none | Back key |
| 1,2 | `RPM` | Display Value | T3 | none | `(A:GENERAL ENG RPM:1, rpm)` [SDK-ENGV; main 1,2] | Format `1.0` |
| 1,3 | `FFLOW` | Display Value | T3 | none | `(A:ENG FUEL FLOW GPH:1, gallons per hour)` [SDK-ENGV, SDK-UNITS] | Format `1.1` |
| 1,4 | `OIL PRES` | Display Value | T3 | none | `(A:GENERAL ENG OIL PRESSURE:1, psi)` [SDK-ENGV, SDK-UNITS] | Format `1.0` |
| 1,5 | `OIL TEMP` | Display Value | T3 | none | `(A:GENERAL ENG OIL TEMPERATURE:1, fahrenheit)` [SDK-ENGV, SDK-UNITS] | Format `1.0` |
| 1,6 | `EGT` | Display Value | T3 | none | `(A:GENERAL ENG EXHAUST GAS TEMPERATURE:1, fahrenheit)` [SDK-ENGV, SDK-UNITS] | Format `1.0` |
| 1,7 | `VAC` | Display Value | T3 | none | `(A:SUCTION PRESSURE, inHg)` [SDK-SYSV, SDK-UNITS] | Format `1.1` |
| 1,8 | | Empty | | | | |
| 2,1 | | Empty | | | | |
| 2,2 | `FUEL L` | Display Gauge | T9 | none | `(A:FUEL LEFT QUANTITY, Gallons)` [SDK-FUELV] | Format `1.0`; horizontal bar (Orientation Right, saved `0`), `0` to `26` gallons [GARMIN], pointer, no warning range |
| 2,3 | `FUEL R` | Display Gauge | T9 | none | `(A:FUEL RIGHT QUANTITY, Gallons)` [SDK-FUELV] | Format `1.0`; horizontal bar (Orientation Right, saved `0`), `0` to `26` gallons [GARMIN], pointer, no warning range |
| 2,4 | | Empty | | | | |
| 2,5 | | Empty | | | | |
| 2,6 | | Empty | | | | |
| 2,7 | | Empty | | | | |
| 2,8 | | Empty | | | | |
| 3,1 | | Empty | | | | |
| 3,2 | `BUS V` | Display Value | T3 | none | `(A:ELECTRICAL BUS VOLTAGE:1, Volts)` [SDK-ELECV; systems 1,6] | Format `2.1` |
| 3,3 | `BATT A` | Display Value | T3 | none | `(A:ELECTRICAL BATTERY LOAD:2, Amperes)` [SDK-ELECV; systems 1,7] | Format `1.1` |
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

**Back** = the Stream Deck app's back key (`backtoparent`), added by the generator on every child page.
"Empty" = no action on that key.

## What the keys do

- **RPM** (1,2) shows the engine RPM (`GENERAL ENG RPM:1`, "The RPM for an indexed engine.", SDK-ENGV), Format
  `1.0`. It repeats the main page's 1,2 (the same address and Format), so the EIS order is complete here (A-RPM).
- **FFLOW** (1,3) shows the fuel flow in gallons per hour (`ENG FUEL FLOW GPH:1`, "Engine fuel flow in gallons
  per hour for the indexed engine.", SDK-ENGV), Format `1.1` (e.g. `8.4`).
- **OIL PRES** (1,4) shows the oil pressure in psi (`GENERAL ENG OIL PRESSURE:1`, "The indexed engine oil
  pressure.", native unit psf; `psi` is an SDK unit name, SDK-UNITS), Format `1.0`.
- **OIL TEMP** (1,5) and **EGT** (1,6) show the oil temperature and the exhaust gas temperature in deg F
  (`GENERAL ENG OIL TEMPERATURE:1`, `GENERAL ENG EXHAUST GAS TEMPERATURE:1`, native unit rankine; `fahrenheit`
  is an SDK unit name), Format `1.0`.
- **VAC** (1,7) shows the vacuum system suction in inches of mercury (`SUCTION PRESSURE`, "Vacuum system
  suction pressure.", no index, SDK-SYSV), Format `1.1` (e.g. `5.0`).
- **FUEL L, FUEL R** (2,2, 2,3) are Display Gauges: a horizontal bar, empty at the left, full at the right,
  from `0` to `26` gallons (the G1000 EIS full scale of the 172S: "When full, the indicator displays to 35
  gallons per side (26 gallons for the Models 172R and 172S).", GARMIN), with a yellow pointer and the number
  below the bar (Format `1.0`). They read the same SimVars as the systems page's FUEL L and FUEL R readouts
  (4,2, 4,3): `FUEL LEFT QUANTITY` / `FUEL RIGHT QUANTITY`, "Current quantity in volume of _all_ the tanks on
  the left side of the aircraft." (right the same), SDK-FUELV. A value above `26` draws at the end of the bar;
  the number still shows the value.
- **BUS V** (3,2) and **BATT A** (3,3) show the bus volts and the battery amps with the systems page's
  addresses and Formats (systems 1,6 and 1,7: `ELECTRICAL BUS VOLTAGE:1`, Format `2.1`; `ELECTRICAL BATTERY
  LOAD:2`, Format `1.1`). They are taken as the EIS M BUS and M BATT values (A-IDX, A-AMPS).
- **No range or colour band on any key.** The real EIS has green, yellow and red arcs, but no source readable
  here gives them for the sim: the 2024 C172 G1000 is a streamed aircraft whose panel and engine files cannot
  be read, the SDK names none, and the Garmin manual describes the real aircraft (A-RANGES).
- **The keys read sim values only.** A press on any key sends nothing: the readouts have no command, the
  gauges have none either (PilotsDeck shows its brief alert sign on a gauge key, as on the trim gauge).
- **What the user sees.** With no sim the plugin is Idle and the keys show a static preview; with the sim but
  no flight every key shows the plugin's Wait image ([phase2-main-page.md](phase2-main-page.md)). Cold and dark
  (expected, Unverified): RPM `0`, FFLOW `0.0`, OIL PRES `0`, OIL TEMP and EGT about the outside air temperature
  in deg F, VAC `0.0`, FUEL L/R the pointer at the loaded quantity with the number, BUS V `00.0` (Format `2.1`) or
  the battery volts if the sim reports them unpowered, BATT A `0.0`. The real EIS is dark then, but the keys
  still show the sim's values (A-DARK). Battery on: BUS V about the battery volts, BATT A the load. Engine
  running: RPM, FFLOW, OIL PRES, OIL TEMP, EGT, VAC and BUS V rise to their running values.

**Open points the hand test decides (Unverified):**

- **A-IDX: the indexes.** Engine `1` (the only engine; SDK-ENGV: "a value between 1 and 16"), bus `1` taken as
  M BUS, battery `2` taken as M BATT (the systems page's indexes, its A-6). If the EIS shows otherwise, the index
  from the scmon check, on both pages.
- **A-AMPS: BATT A's sign** against the EIS M BATT. The SDK's battery load is the load while the battery
  supplies, "not when charging"; no source states the EIS sign. The key reads the value as it is (no Scalar).
  If the sign is reversed: Scalar `-1`; if it never shows charging: `ELECTRICAL BUS AMPS:n` (the systems page's
  fallback).
- **A-FUELVAR: the fuel SimVars.** SDK-FUELV says the General fuel SimVars are "only valid for legacy aircraft"
  for the most part (aircraft whose fuel is set up in the flight model's `[FUEL]` section) and that MSFS 2024
  aircraft should not use them. The 2024 C172 is expected to answer them anyway; the systems page's FUEL L/R
  read the same SimVars and are not sim-tested either. If they read `0` or wrong: `FUELSYSTEM TANK QUANTITY:n`,
  on both pages.
- **A-FUELRANGE: the gauge scale** `0` to `26` gallons (GARMIN, the real 172S EIS). The sim's tank capacity is
  not readable here. If a full tank reads another number, the Maximum becomes that number.
- **A-UNITS: the unit strings** `gallons per hour`, `psi`, `fahrenheit`, `inHg` (SDK unit names, passed as
  published, README 2.1.1). If a key shows `0` while the EIS moves: the native unit (`rankine`, `psf`) with a
  Scalar, or the `ENG ...` variants (Fallbacks).
- **A-DARK, A-RANGES, A-RPM, A-BAR:** values while the EIS is dark, no colour bands, RPM repeated, horizontal
  bars: the user says in checklist step 7 whether they suit.

## What each key holds

Every key is a copy of a template with only these fields changed (the generator does this).

- **T3** (RPM, FFLOW, OIL PRES, OIL TEMP, EGT, VAC, BUS V, BATT A): the Phase 1 HDG key's Display Value
  (`p1:2,0`), no command: Value Address and Format from the table; everything else is the template's (Scalar
  `1`, no Mappings, background `Images/Empty.png`, title size 15 at the top).
- **T9** (FUEL L, FUEL R): the Display Gauge template `display_gauge` (P3-4's; see
  [phase2-trim-views.md](phase2-trim-views.md), "What each key holds", T9, for how it was derived). Its saved
  settings, by settings panel tab ("key" = set by the key in `tools/profilegen/c172-g1000.json`, "template" =
  the template's value):

| Field (panel tab) | Saved value | From | Source |
|---|---|---|---|
| Address (Value) | `(A:FUEL LEFT QUANTITY, Gallons)` / `(A:FUEL RIGHT QUANTITY, Gallons)` | key | PD-PI; SDK-FUELV |
| Scalar / Minimum / Maximum (Value) | `1` / `0` / `26` | template / key / key | PD-PI, README 2.3; GARMIN (A-FUELRANGE) |
| Draw Arc / Orientation / Size / Offset (Gauge) | off (`DrawArc` `false`: a bar) / Right, saved `BarOrientation` `0` (a horizontal bar, empty left, full right) / `58; 10` / `0; 0` | template | PD-PI, PD-SRC defaults (A-BAR) |
| Gauge color / color switching (Gauge) | `#006400` / off | template | PD-PI, P1 |
| Center Line | off (no neutral point on a quantity) | template | PD-PI |
| Indicator color / size / flip (Indicator) | `#ffcc00` (yellow, as the trim gauge) / `10` / off | key / template / template | PD-PI |
| Warning Range | off: **no warning or critical range** (no source: the aircraft is streamed, the SDK names none) | template | PD-PI |
| Show Text / Format / Mappings / font inherit (Text) | on / `1.0` / empty / on | template / key / template / template | PD-PI |
| Draw Rectangle (Text) | `7; 45; 60; 21` (the number below the bar) | template | PD-SRC (P3-4) |
| Commands | none (`HasAction` `false`, Command Type `3`, empty address) | template | PD-PI |
| Background | `Images/Empty.png` (PilotsDeck draws everything) | template | P1 |
| Title | `FUEL L` or `FUEL R`, top, size 15 | key / template | as every key |

If you change a gauge by hand during a test, Tab out of each text field (Size, Offset, Minimum, Maximum,
Format): the settings panel saves a text field only when focus leaves it.

## Which route each key uses, and why

Every key reads a SimVar. The aircraft's input event list
([reference/InputEvents-C172-G1000.txt](reference/InputEvents-C172-G1000.txt)) was checked first: its engine
lines (176 magneto, 177 throttle, 178 mixture) are controls, and **no input event is a readout**, so there is
no B-Var to read. In MSFS 2024 aircraft a gauge may read another index (bus, battery, tank) than the default
one (the battery precedent in aircraft-mappings.md): the indexes here are open (A-IDX). The sim's own EIS
configuration cannot be read (the aircraft is streamed), so no index or range comes from it.

| Key | Route | Reason |
|---|---|---|
| RPM, FFLOW, OIL PRES, OIL TEMP, EGT | `GENERAL ENG ...:1` / `ENG FUEL FLOW GPH:1` SimVars, engine index 1 | The SDK engine SimVars; the C172 has one engine. Fuel flow: also a lead (TorontoWill's generic profile reads the same name, index and unit). |
| VAC | `SUCTION PRESSURE`, no index | The only vacuum value on SDK-SYSV (the other, `PARTIAL PANEL VACUUM`, is a fail flag). |
| FUEL L, FUEL R | `FUEL LEFT QUANTITY` / `FUEL RIGHT QUANTITY` | The systems page's reads (one source of truth for both pages); A-FUELVAR. |
| BUS V, BATT A | `ELECTRICAL BUS VOLTAGE:1` / `ELECTRICAL BATTERY LOAD:2` | The systems page's reads; A-IDX, A-AMPS. |

## Not on this page, and why

| Function | Why not now |
|---|---|
| Magnetos, starter, throttle, mixture | The main page's rule: no engine command on the deck. |
| LOAD A, FUEL TOT, the fuel selector and valve | They stay on the systems page ([phase3-systems.md](phase3-systems.md)). |
| CHT, fuel pressure, engine hours | Not in this unit's scope (the roadmap's P3-5: RPM, fuel flow, oil, EGT, vacuum, fuel, volts and amps). |
| Colour bands and warning ranges | No readable source for the sim (A-RANGES). |
| One gauge for both tanks (Display Gauge Dual) | The profile checker has no such action; a later tools unit if wanted (A-DUAL). |
| Icon pack images | Personal use only; in the local icon build ([icons.md](icons.md)). |

## Fallbacks

Use one only if the checklist shows the main address doesn't work, and say which one you used. None is
tested, and none is built.

| Key | Fallback | Source |
|---|---|---|
| OIL PRES | `(A:ENG OIL PRESSURE:1, psi)` | SDK-ENGV |
| OIL TEMP | `(A:ENG OIL TEMPERATURE:1, fahrenheit)` | SDK-ENGV |
| EGT | `(A:ENG EXHAUST GAS TEMPERATURE:1, fahrenheit)` | SDK-ENGV |
| OIL PRES, OIL TEMP, EGT show `0` while the EIS moves (A-UNITS) | the native unit (`psf`, `rankine`) with a Scalar | SDK-ENGV; SDK-UNITS |
| FFLOW shows `0` while the engine runs | `(A:ENG FUEL FLOW PPH:1, pounds per hour)`: a weight rate (SDK-UNITS), not the EIS gallons; record the numbers against the EIS | SDK-ENGV; SDK-UNITS |
| VAC shows `0` while the engine runs | none: `SUCTION PRESSURE` is the only vacuum value on SDK-SYSV (`PARTIAL PANEL VACUUM` is a fail flag); record it | SDK-SYSV |
| FUEL L / FUEL R read `0` or wrong (A-FUELVAR) | `(A:FUELSYSTEM TANK QUANTITY:n, Gallons)`, n from the scmon check; the Maximum from `(A:FUELSYSTEM TANK CAPACITY:n, Gallons)` (`FUEL LEFT CAPACITY` / `FUEL RIGHT CAPACITY` are General SimVars like the reads that failed) | SDK-FUELV |
| BUS V or BATT A differ from the EIS (A-IDX, A-AMPS) | as the systems page: another index, `(A:ELECTRICAL MAIN BUS VOLTAGE:1, Volts)` (v1.00); BATT A index 1, Scalar `-1` or `(A:ELECTRICAL BUS AMPS:1, Amperes)` | SDK-ELECV |

## How to test

Run [tests/manual-checklist.md](../tests/manual-checklist.md), section "P3-5: Engine and fuel page (C172
G1000)": cold and dark, battery on, then engine running, each key against the MFD EIS.

## When it passes

1. Any change found in the test goes into `tools/profilegen/c172-g1000.json` and this doc; then the profile
   is regenerated (not exported from the app) and imported again.
2. Fill in the "Verified" column of the engine and fuel rows in aircraft-mappings.md with the date and sim
   version, for each function that passed.

## Sources

| Tag | Source |
|---|---|
| SDK-ENGV | MSFS 2024 SDK, SimVars "Aircraft Engine Variables", https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-engine-variables/ (Engine Index "a value between 1 and 16 that signals which of the engines on the aircraft is being targeted"; `ENG FUEL FLOW GPH` gallons per hour; `ENG FUEL FLOW PPH` pounds per hour; `GENERAL ENG OIL PRESSURE` psf; `GENERAL ENG OIL TEMPERATURE` and `GENERAL ENG EXHAUST GAS TEMPERATURE` rankine; `GENERAL ENG RPM` rpm; `ENG OIL PRESSURE`, `ENG OIL TEMPERATURE`, `ENG EXHAUST GAS TEMPERATURE`), read 2026-11-16 |
| SDK-SYSV | MSFS 2024 SDK, SimVars "Aircraft System Variables", https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-system-variables/ (`SUCTION PRESSURE` "Vacuum system suction pressure.", inches of mercury, no index), read 2026-11-16 |
| SDK-FUELV | MSFS 2024 SDK, SimVars "Aircraft Fuel Variables", https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-fuel-variables/ (`FUEL LEFT QUANTITY` / `FUEL RIGHT QUANTITY` and `FUEL LEFT CAPACITY` / `FUEL RIGHT CAPACITY`, Gallons; the section note that the majority of these SimVars are only valid for legacy aircraft whose fuel is set up in the flight model's `[FUEL]` section, and that MSFS 2024 aircraft should not use them; `FUELSYSTEM TANK QUANTITY` and `FUELSYSTEM TANK CAPACITY` "Tank Name (or index)", Gallons), read 2026-11-16 |
| SDK-ELECV | MSFS 2024 SDK, SimVars "Aircraft Electrics Variables" (the systems page's source; URL in [phase3-systems.md](phase3-systems.md), "Sources") |
| SDK-UNITS | MSFS 2024 SDK, "Simulation Variable Units", https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/simulation-variable-units/ (unit names `gallons per hour`, `pounds per hour`, `psi`, `fahrenheit`, `inHg`, `rpm`, `gallons`, `volts`, `amperes`), read 2026-11-16 |
| README | PilotsDeck README, https://github.com/Fragtality/PilotsDeck/blob/master/README.md: 2.1.1 (A-Var `(Prefix:Name(:index), Unit)`, the unit "as published separated by a `,` from the Name"), 2.2.2 (Format), 2.3 (Display Gauge: Minimum and Maximum "of the configured Variable", "By Default this Action will render a Bar") |
| PD-PI | The installed plugin's settings panel `Plugin\PI\pi-DisplayGauge.html` (fields `Scalar`, `MinimumValue`, `MaximumValue`, `DrawArc`, `GaugeSize`, `GaugeColor`, `UseColorSwitching`, `BarOrientation`, `Offset`, `IndicatorColor`, `CenterLine`, `DrawWarnRange`, `ShowText`, `Format`, `ValueMappings`), read 2026-11-16 |
| PD-SRC | PilotsDeck source at commit 11bdf1f7daf4828f822c18919952fe5b66153e58, as on the trim gauge ([phase2-trim-views.md](phase2-trim-views.md), "Sources"): Orientation Right = `0`, the default bar and its text rectangle |
| P1 | The Phase 1 export (`MSFS2024 C172 POC.streamDeckProfile`): key `p1:2,0` (Display Value) and its gauge field defaults |
| GARMIN | Garmin G1000 Reference Manual, Cessna Nav III, Section 3 EIS, https://www.manualslib.com/manual/2328281/Garmin-G1000.html?page=37 and ?page=38 (labels RPM, FFLOW GPH, OIL PRES, OIL TEMP, EGT, VAC, FUEL QTY GAL L and R, M and E BUS VOLTS, M and S BATT AMPS; "When full, the indicator displays to 35 gallons per side (26 gallons for the Models 172R and 172S)."), the real aircraft, read 2026-11-16 |
| IE | [reference/InputEvents-C172-G1000.txt](reference/InputEvents-C172-G1000.txt) (IE n = line n: 176 magneto, 177 throttle, 178 mixture; no readout) |
| Leads | TorontoWill's generic PilotsDeck profile reads `(A:ENG FUEL FLOW GPH:1,Gallons per hour)`. A lead only; nothing copied. |
