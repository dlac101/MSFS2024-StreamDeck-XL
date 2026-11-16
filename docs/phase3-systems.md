# Phase 3: systems page, Cessna 172 G1000

**Status: generated, not yet sim-tested.** The page is in the generated profile, but nothing has been tried
in the app or the sim yet. Every new name below is recorded as "Unverified" in
[aircraft-mappings.md](aircraft-mappings.md) ("Phase 3 systems page") until the checks in
[tests/manual-checklist.md](../tests/manual-checklist.md), section "P3-3: Systems page (C172 G1000)", pass.

Goal: the start-up and shut-down switches the main page lacks, each lit from sim state, with the readouts that
check them: the alternator, avionics bus 1 and 2 and the standby battery with the bus volts, battery amps and
total load amps; the interior lights with a dimmer readout; the fuel selector (LEFT, BOTH, RIGHT) with a selector
readout, the fuel shutoff valve and the fuel quantity left, right and total. The main page already has BAT (1,1),
FUEL PMP (1,3), the exterior lights and PITOT (4,1-4,6) and RPM (1,2); they are not repeated here.

The page is part of the generated profile `MSFS2024 C172 G1000` (same file, same name, same import as the
main page: see [phase2-main-page.md](phase2-main-page.md), "Import the profile"). It needs **no script**. The
table below is the reference for what each key holds; `tools/profilegen/check.py` compares the profile with
the "Key table: systems" section key by key.

Nothing on this page uses keyboard bindings, vJoy or anything tied to a controller: the switch keys read and
write the aircraft's own input events (B-Vars) and the readouts read SimVars, so they work the same with the
Xbox Elite controller and the T.16000M + TWCS.

## Where the page sits

A second-level folder page **systems**, opened by the folder key `SYSTEMS` at **MORE 2,2** (the first key of
the More page's second row; row 1 is full: [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md), "Key table:
more"). How the pages connect: [navigation.md](navigation.md).

## Layout: systems

Positions are **row,column**, 1-based, row 1 at the top. 1,1 is the back key (it returns to MORE), as on
every child page. One row per system: electrical (the cockpit's switch order ALT, AVIONICS BUS 1 and 2, STBY
BATT, then the EIS readouts), interior lights, fuel selector and valve, fuel quantity. Column 1 below the back
key stays empty, as on the XPDR and radios pages. An engine start reads row 1 left to right after BAT on the
main page.

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | ALT | AVN 1 | AVN 2 | STBY BAT | BUS V | BATT A | LOAD A |
| **Row 2** | | CABIN 1 | CABIN 2 | PANEL 1 | PANEL 2 | PED LT | DIMMER | |
| **Row 3** | | LEFT | BOTH | RIGHT | FUEL SEL | FUEL VLV | | |
| **Row 4** | | FUEL L | FUEL R | FUEL TOT | | | | |

## Key table: systems

Action names as in phase2-main-page.md. **Back** = the Stream Deck app's back key (`backtoparent`), added
by the generator on every child page. "Empty" = no action on that key. Every switch command on this page is
an input event, command type **B-Var** (saved as `13`, "Run as Command" unchecked, so the key's On and Off
values are written; PD-PI lines 225-226, 237-239); the readouts send no command.

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to MORE | none | Back key |
| 1,2 | `ALT` | Dynamic Button | T1 | `B:electrical_alternator_1`, On `1` / Off `0` [IE 140] | `B:electrical_alternator_1` [IE 140] | On/Off image, Special State |
| 1,3 | `AVN 1` | Dynamic Button | T1 | `B:electrical_line_bus_1_to_avionics_bus_1`, On `1` / Off `0` [IE 174] | `B:electrical_line_bus_1_to_avionics_bus_1` [IE 174] | On/Off image, Special State |
| 1,4 | `AVN 2` | Dynamic Button | T1 | `B:electrical_line_bus_2_to_avionics_bus_2`, On `1` / Off `0` [IE 175] | `B:electrical_line_bus_2_to_avionics_bus_2` [IE 175] | On/Off image, Special State |
| 1,5 | `STBY BAT` | Dynamic Button | T1 | `B:electrical_battery_stby_2`, On `1` / Off `0` [IE 142] | `B:electrical_battery_stby_2` [IE 142] | On/Off image, Special State |
| 1,6 | `BUS V` | Display Value | T3 | none | `(A:ELECTRICAL BUS VOLTAGE:1, Volts)` [SDK-ELECV] | Format `2.1` |
| 1,7 | `BATT A` | Display Value | T3 | none | `(A:ELECTRICAL BATTERY LOAD:2, Amperes)` [SDK-ELECV] | Format `1.1` |
| 1,8 | `LOAD A` | Display Value | T3 | none | `(A:ELECTRICAL TOTAL LOAD AMPS, Amperes)` [SDK-ELECV] | Format `1.1` |
| 2,1 | | Empty | | | | |
| 2,2 | `CABIN 1` | Dynamic Button | T1 | `B:lighting_cabin_1`, On `1` / Off `0` [IE 194] | `B:lighting_cabin_1` [IE 194] | On/Off image, Special State |
| 2,3 | `CABIN 2` | Dynamic Button | T1 | `B:lighting_cabin_2`, On `1` / Off `0` [IE 195] | `B:lighting_cabin_2` [IE 195] | On/Off image, Special State |
| 2,4 | `PANEL 1` | Dynamic Button | T1 | `B:lighting_panel_1`, On `1` / Off `0` [IE 198] | `B:lighting_panel_1` [IE 198] | On/Off image, Special State |
| 2,5 | `PANEL 2` | Dynamic Button | T1 | `B:lighting_panel_2`, On `1` / Off `0` [IE 199] | `B:lighting_panel_2` [IE 199] | On/Off image, Special State |
| 2,6 | `PED LT` | Dynamic Button | T1 | `B:lighting_pedestral_1`, On `1` / Off `0` [IE 200] | `B:lighting_pedestral_1` [IE 200] | On/Off image, Special State |
| 2,7 | `DIMMER` | Display Value | T3 | none | `(A:LIGHT POTENTIOMETER:5, Percent)` [SDK-SYSV; IE 201] | Format `1.0` |
| 2,8 | | Empty | | | | |
| 3,1 | | Empty | | | | |
| 3,2 | `LEFT` | Dynamic Button | T1 | `B:fuel_selector_1`, On `1` / Off `1` [IE 180] | `B:fuel_selector_1` [IE 180] | On/Off image: On `1`, Off `2` |
| 3,3 | `BOTH` | Dynamic Button | T1 | `B:fuel_selector_1`, On `2` / Off `2` [IE 180] | `B:fuel_selector_1` [IE 180] | On/Off image: On `2`, Off `1` |
| 3,4 | `RIGHT` | Dynamic Button | T1 | `B:fuel_selector_1`, On `3` / Off `3` [IE 180] | `B:fuel_selector_1` [IE 180] | On/Off image: On `3`, Off `2` |
| 3,5 | `FUEL SEL` | Display Value | T3 | none | `(A:FUELSYSTEM JUNCTION SETTING:1, Number)` [SDK-FUELV] | Mappings `1=LEFT:2=BOTH:3=RIGHT` |
| 3,6 | `FUEL VLV` | Dynamic Button | T1 | `B:fuel_valve_shutoffvalve`, On `1` / Off `0` [IE 181] | `B:fuel_valve_shutoffvalve` [IE 181] | On/Off image, Special State |
| 3,7 | | Empty | | | | |
| 3,8 | | Empty | | | | |
| 4,1 | | Empty | | | | |
| 4,2 | `FUEL L` | Display Value | T3 | none | `(A:FUEL LEFT QUANTITY, Gallons)` [SDK-FUELV] | Format `1.1` |
| 4,3 | `FUEL R` | Display Value | T3 | none | `(A:FUEL RIGHT QUANTITY, Gallons)` [SDK-FUELV] | Format `1.1` |
| 4,4 | `FUEL TOT` | Display Value | T3 | none | `(A:FUEL TOTAL QUANTITY, Gallons)` [SDK-FUELV] | Format `1.1` |
| 4,5 | | Empty | | | | |
| 4,6 | | Empty | | | | |
| 4,7 | | Empty | | | | |
| 4,8 | | Empty | | | | |

## What the keys do

- **ALT, AVN 1, AVN 2, STBY BAT** (1,2-1,5) are the alternator, avionics bus 1, avionics bus 2 and standby
  battery switches. A press writes the key's input event with its On value `1` or its Off value `0` (README
  2.1.1 BVAR, "you can send/activate them with an optional Parameter"): the plugin sends the On value while
  the key reads its Off value, else the Off value (PD-SRC, `ToolsValueState.cs` `Toggle`), so at any third
  value (a TEST position, a dimmer step) a press sends Off `0`. Whether the aircraft takes the write is
  Unverified (checklist step 3). Each key is lit from the same input event read back.
- **BUS V** (1,6) shows the volts of bus 1 (`ELECTRICAL BUS VOLTAGE:1`, "Returns the tension going through the
  named (or indexed) Bus, in volts.", SDK-ELECV), Format `2.1` (e.g. `28.0`). **BATT A** (1,7) shows the load
  of battery 2 in amperes (`ELECTRICAL BATTERY LOAD:2`, index 2 because the cockpit BAT switch drives battery
  index 2, [aircraft-mappings.md](aircraft-mappings.md)), Format `1.1` (e.g. `2.4`; the SDK calls it
  "the load drawn from the Battery when it is used as a supplier, and will not return the supplied tension
  when charging, or when the battery is not a supplier": so no charge current is expected on it; whether it
  carries the EIS M BATT sign is open, A-6).
  **LOAD A** (1,8) shows the total load of the whole electrical system (`ELECTRICAL TOTAL LOAD AMPS`, no index),
  Format `1.1`. Compare them with the G1000 EIS "M BUS" and "M BATT" values.
- **CABIN 1, CABIN 2, PANEL 1, PANEL 2, PED LT** (2,2-2,6) write and read the aircraft's interior light input
  events (`lighting_cabin_1` / `_2`, `lighting_panel_1` / `_2`, `lighting_pedestral_1`, the aircraft's own
  spelling), On `1` / Off `0` as the electrical switches. The titles are neutral: which light each one drives is
  open (A-8).
- **DIMMER** (2,7) shows `LIGHT POTENTIOMETER:5` in percent, Format `1.0` (e.g. `75`; "Adjust the potentiometer
  of the indexed lighting.", SDK-SYSV; the aircraft lists `lighting_potentiometer_5`, IE 201). Read only (A-7).
- **LEFT, BOTH, RIGHT** (3,2-3,4) set the fuel selector (`fuel_selector_1`, IE 180). Each key writes the same
  value as its On and its Off value (`1`, `2`, `3`), so every press sets its own position, whatever the key
  shows (PD-SRC: `Toggle` returns either the On or the Off value, the same value here). Each key is lit while
  the selector reads its value.
- **FUEL SEL** (3,5) shows the fuel system's junction option (`FUELSYSTEM JUNCTION SETTING:1`, "This will
  return the current _Option_ for the indexed junction.", SDK-FUELV) as a word: Mappings `1=LEFT:2=BOTH:3=RIGHT`;
  any other number shows as the number. It is a second, SimVar view of the selector, next to the lit key.
- **FUEL VLV** (3,6) opens and closes the fuel shutoff valve (`fuel_valve_shutoffvalve`, IE 181): On `1`
  (open, fuel on) / Off `0` (closed, fuel off). **Ground only, never in flight**: a press in flight can stop
  the engine. The press is reversible and the key reads the valve back (A-5).
- **FUEL L, FUEL R, FUEL TOT** (4,2-4,4) show the fuel quantity left, right and total in gallons, Format `1.1`
  (e.g. `24.5`; `FUEL LEFT QUANTITY`: "Current quantity in volume of _all_ the tanks on the left side of the
  aircraft.", SDK-FUELV). Whether these SimVars count unusable fuel too (the EIS shows
  usable fuel) is open: checklist step 1 compares them with the EIS gauges.
- **What a switch key shows.** The On image only while its input event reads `1`, the Off image at `0`, and the
  Fault image for any other value (Special State with Any Value): a dimmer knob or a three-way switch shows up
  as Fault, never as a wrong "off".
- **What a selector key shows at the third value** (W-5). LEFT has On `1` / Off `2`, BOTH On `2` / Off `1`,
  RIGHT On `3` / Off `2`, and no Special State. The plugin draws a Dynamic Button's image in this order: the On
  image if the value matches On, else the Off image if it matches Off, else the Special State image if one is
  set; if none of these matches, it draws no state image, only the key's background (PD-SRC,
  `ActionSwitchDisplay.cs` `Refresh()`). So with the selector at RIGHT (`3`), LEFT and BOTH show neither
  image; at LEFT (`1`), RIGHT shows neither image; at BOTH (`2`), LEFT and RIGHT show their Off image. Only the
  lit key matters. What this looks like on the deck is **Unverified**: checklist step 5 records it.
- **The keys are lit and read from the sim only.** A press the aircraft refuses changes nothing on the key (it
  reads the input event back; the deck never assumes it worked). The readouts show sim values only.
- With no sim the plugin is Idle and the keys show a static preview; with the sim but no flight every key
  shows the plugin's Wait image ([phase2-main-page.md](phase2-main-page.md)). Input event keys work only after
  the aircraft's input event list has arrived.

**Open points the hand test decides (Unverified):**

- **A-3: the switch values.** ALT and AVN 1/2 are expected to be `1` / `0` (a lead writes them so). The real
  STBY BATT switch has three positions (ARM / OFF / TEST, the value of TEST unknown), and CABIN, PANEL and PED
  may be dimmer knobs (a 0-100 or 0-1 range). Any value other than `1` or `0` shows the Fault image. Checklist
  steps 3 and 4 record the values; a dimmer key that fails becomes a Display Value of its input event (repair).
- **A-4: the fuel selector values** `1` = LEFT, `2` = BOTH, `3` = RIGHT (weak: from a lead's junction option
  numbers, not from a source for the input event), and that a write of the value moves the selector. The scmon
  check of `B:fuel_selector_1`, the first in-sim step of the checklist, settles the values before step 5.
- **A-5: FUEL VLV is a plain press toggle**, ground only (see above).
- **A-6: the readout indexes.** BUS V reads bus `1` (a global index; no source names the C172's bus), BATT A
  battery `2` (the BAT precedent), and whether BATT A has the EIS M BATT sign. Checklist step 2 compares them
  with the EIS.
- **A-7: DIMMER is read only.** No source says what potentiometer 5 dims, nor the scale of
  `LIGHT_POTENTIOMETER_5_SET`; checklist step 4 records which knob it follows.
- **A-8: the light titles** CABIN 1/2 and PANEL 1/2 are neutral; checklist step 4 records what each one drives.

## What each key holds

Every key is a copy of a template with only these fields changed (the generator does this).

- **T1** (ALT, AVN 1, AVN 2, STBY BAT, CABIN 1, CABIN 2, PANEL 1, PANEL 2, PED LT, FUEL VLV): the Phase 1 BAT
  key's Dynamic Button (`p1:0,0`, command type B-Var `13`, On `1` / Off `0`, image states On `1` / Off `0`),
  with Command Address and Value Address the input event from the table, and **Special State** on with **Any
  Value** (the Fault image for any other value), as the main page's BAT and FUEL PMP. Title size 14 on STBY BAT,
  CABIN 1, CABIN 2, PANEL 1, PANEL 2 and FUEL VLV (7 or 8 letters, as the main page's FUEL PMP); 15 (the
  template's size) on the others.
- **T1, selector form** (LEFT, BOTH, RIGHT): the same Dynamic Button with Command Address and Value Address
  `B:fuel_selector_1`, the key's position value as both the On and the Off value (`1`, `2`, `3`), the image
  states On = that value and Off = the value named in the table, and **no** Special State (the third position
  is a normal value, not a fault).
- **T3** (BUS V, BATT A, LOAD A, DIMMER, FUEL SEL, FUEL L, FUEL R, FUEL TOT): the Phase 1 HDG key's Display
  Value (`p1:2,0`), no command: Value Address and Format from the table; FUEL SEL with Format empty and the
  Mappings `1=LEFT:2=BOTH:3=RIGHT`.

## Which route each key uses, and why

In MSFS 2024 aircraft a cockpit control may drive an input event (B-Var) and a different SimVar index than
the standard K-event (the battery precedent, [aircraft-mappings.md](aircraft-mappings.md): the cockpit BAT
switch drives battery index 2, so the index-1 SimVar and `K:TOGGLE_MASTER_BATTERY` don't stay in sync). The
aircraft's input event list ([reference/InputEvents-C172-G1000.txt](reference/InputEvents-C172-G1000.txt)) was
checked first for every switch: **every switch on this page is in it, so every switch key reads and writes its
input event**. The SDK K-event and SimVar pairs are fallbacks only, and weak for this aircraft twice over: the
alternator events are documented for the v1.00 electrical system only ("only viable for aircraft using the
v1.00 electrical system", SDK-ELECE) while the C172's own names are the modular system's line and circuit
terms, and the indexes the cockpit drives (bus, line, circuit and junction names live in the aircraft's
systems.cfg, which this unit did not open) are unknown. Readouts read SimVars: no input event is a readout.

| Key | Route | Reason |
|---|---|---|
| ALT | `B:electrical_alternator_1` (IE 140), read and write | In the input event list; a lead writes it `1` / `0`. The K-event `TOGGLE_ALTERNATOR1` is for the v1.00 electrical system only. |
| AVN 1, AVN 2 | `B:electrical_line_bus_1_to_avionics_bus_1` / `_2_to_avionics_bus_2` (IE 174, 175) | In the list; a lead writes them `1` / `0`. The SDK has no AVIONICS_MASTER event on SDK-ELECE; `K:ELECTRICAL_LINE_CONNECTION_TOGGLE` needs a line index nobody has given. |
| STBY BAT | `B:electrical_battery_stby_2` (IE 142) | In the list; the battery index a SimVar would need is unknown (the main BAT drives index 2). Three-position switch: A-3. |
| CABIN 1/2, PANEL 1/2, PED LT | `B:lighting_cabin_1` / `_2`, `B:lighting_panel_1` / `_2`, `B:lighting_pedestral_1` (IE 194, 195, 198, 199, 200) | In the list; the light K-events take a circuit name or index that is unknown. A-3, A-8. |
| LEFT, BOTH, RIGHT | `B:fuel_selector_1` (IE 180), one value per position | In the list; a selector needs one value per position, which the B-Var takes (A-4). |
| FUEL VLV | `B:fuel_valve_shutoffvalve` (IE 181) | In the list; `K:FUELSYSTEM_VALVE_TOGGLE` needs a valve index that is unknown. Ground only (A-5). |
| Readouts | SimVar reads (bus 1, battery 2, total load, potentiometer 5, junction 1, fuel left/right/total) | No input event is a readout. A-6 (indexes), A-7 (dimmer). |

## Not on this page, and why

| Function | Why not now |
|---|---|
| BAT, FUEL PMP, exterior lights, PITOT, RPM | Already on the main page (1,1, 1,3, 4,1-4,6, 1,2); not repeated. |
| Magnetos, starter, mixture | The main page's rule: no engine command on the deck. |
| The 30 circuit breakers and the 12 V power switch (IE 143-173) | A later unit (roadmap C.3). |
| Alternate static air (IE 207) | Not lights, electrical or fuel. |
| Fuel flow, oil, EGT, vacuum, fuel gauges | On the engine and fuel page (MORE 2,3, P3-5, [phase3-engine-fuel.md](phase3-engine-fuel.md)), which reuses this page's bus volts, battery amps and fuel quantity addresses. |
| Primer, glareshield, wing, logo or recognition light, external power | The 2024 C172 G1000 has no input event for them (A-9). |
| Dimmer steps | No source says what potentiometer 5 dims or the scale of its set event (A-7). |
| Icon pack images | Personal use only; in the local icon build ([icons.md](icons.md)). |

## Fallbacks

Use one only if the checklist shows the main route doesn't work, and say which one you used. None is tested,
and none is built.

| Key | Fallback | Source |
|---|---|---|
| ALT doesn't move the switch or doesn't follow | read `(A:GENERAL ENG MASTER ALTERNATOR:1, Bool)` ("true if the switch is ON"), write `K:TOGGLE_ALTERNATOR1` (v1.00 electrical system only) | SDK-ELECV; SDK-ELECE |
| AVN 1 / AVN 2 | read `(A:LINE CONNECTION ON:n, Bool)` or `(A:AVIONICS MASTER SWITCH:n, Bool)`, write `K:ELECTRICAL_LINE_CONNECTION_TOGGLE:n` ("line.N name (or index)"); n unknown | SDK-ELECV; SDK-SYSV; SDK-ELECE |
| STBY BAT | read `(A:ELECTRICAL MASTER BATTERY:n, Bool)`; n unknown; for a third value (TEST), new On/Off values from the scmon check (A-3) | SDK-ELECV; tools/scmon |
| BUS V or BATT A differ from the EIS (A-6) | another index, or `(A:ELECTRICAL MAIN BUS VOLTAGE:1, Volts)` (v1.00); BATT A index 1 or `(A:ELECTRICAL BUS AMPS:1, Amperes)` | SDK-ELECV |
| CABIN 1/2 | `K:TOGGLE_CABIN_LIGHTS`, read `(A:LIGHT CABIN, Bool)` | SDK-ELECE; SDK-SYSV |
| PANEL 1/2 | `K:PANEL_LIGHTS_TOGGLE`, read `(A:LIGHT PANEL, Bool)`; a dimmer knob becomes a Display Value of its input event (A-3) | SDK-ELECE; SDK-SYSV |
| PED LT | `K:PEDESTRAL_LIGHTS_TOGGLE`, read `(A:LIGHT PEDESTRAL, Bool)` | SDK-ELECE; SDK-SYSV |
| DIMMER shows `0` or `1` only, or nothing | read `B:lighting_potentiometer_5` (IE 201); a `0`/`1` reading means the sim gives 0..1 (A-7) | IE; SDK-SYSV |
| LEFT / BOTH / RIGHT light for the wrong position (A-4) | the three keys' values and FUEL SEL's mapping from the scmon check | tools/scmon |
| LEFT / BOTH / RIGHT don't move the selector (A-4) | `K:FUEL_SELECTOR_LEFT` / `K:FUEL_SELECTOR_ALL` / `K:FUEL_SELECTOR_RIGHT` ("selector 1") as Simple Buttons, the lit state kept on the B-Var read | SDK-FUELE |
| FUEL SEL | `(A:FUEL TANK SELECTOR:1, Enum)` (legacy fuel system only) | SDK-FUELV |
| FUEL VLV | `K:FUELSYSTEM_VALVE_TOGGLE:n` ("[0]: Valve Index"), read `(A:FUELSYSTEM VALVE SWITCH:n, Bool)`; n unknown | SDK-FUELE; SDK-FUELV |
| FUEL L / R / TOT | `(A:FUELSYSTEM TANK QUANTITY:n, Gallons)` | SDK-FUELV |

## How to test

Run [tests/manual-checklist.md](../tests/manual-checklist.md), section "P3-3: Systems page (C172 G1000)". As
on the other pages, check the reverse direction too: **work each cockpit switch, the light switches and the
fuel selector with the mouse, and check that the keys and readouts follow without a key being pressed.** FUEL
VLV only on the ground with the engine off.

## When it passes

1. Any change found in the test goes into `tools/profilegen/c172-g1000.json` and this doc; then the profile
   is regenerated (not exported from the app) and imported again.
2. Fill in the "Verified" column of the systems rows in aircraft-mappings.md with the date and sim version,
   for each function that passed.

## Sources

| Tag | Source |
|---|---|
| SDK-ELECE | MSFS 2024 SDK, Key events "Aircraft Electrical Events", https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-electrical-events/ (alternator events: "only viable for aircraft using the v1.00 electrical system", `TOGGLE_ALTERNATOR1` "Toggles alternator/generator 1/2/3/4 switch."; `ELECTRICAL_LINE_CONNECTION_TOGGLE` "[0]: line.N name (or index)"; `TOGGLE_CABIN_LIGHTS`, `PANEL_LIGHTS_TOGGLE`, `PEDESTRAL_LIGHTS_TOGGLE` with a circuit name or index; `LIGHT_POTENTIOMETER_n_SET` "[0]: Potentiometer value."; no AVIONICS_MASTER event), read 2026-11-14 |
| SDK-ELECV | MSFS 2024 SDK, SimVars "Aircraft Electrics Variables", https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-electrics-variables/ (`ELECTRICAL BUS VOLTAGE` v2+ "Bus name (or index)", "if you supply an index it is the global index", Volts; `ELECTRICAL BATTERY LOAD` Amperes; `ELECTRICAL TOTAL LOAD AMPS` no index, Amperes; `ELECTRICAL MAIN BUS VOLTAGE` v1.00; `ELECTRICAL BUS AMPS`; `ELECTRICAL MASTER BATTERY`; `LINE CONNECTION ON`; `GENERAL ENG MASTER ALTERNATOR` "true if the switch is ON"), read 2026-11-14 |
| SDK-SYSV | MSFS 2024 SDK, SimVars "Aircraft System Variables", https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-system-variables/ (`LIGHT POTENTIOMETER` "Potentiometer Index", "Adjust the potentiometer of the indexed lighting."; `LIGHT CABIN`, `LIGHT PANEL`, `LIGHT PEDESTRAL` Bool; `AVIONICS MASTER SWITCH`), read 2026-11-14 |
| SDK-FUELV | MSFS 2024 SDK, SimVars "Aircraft Fuel Variables", https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-fuel-variables/ (`FUEL LEFT QUANTITY` / `FUEL RIGHT QUANTITY` "Current quantity in volume of _all_ the tanks on the left side of the aircraft." (right the same), `FUEL TOTAL QUANTITY`, Gallons; `FUELSYSTEM JUNCTION SETTING` "This will return the current _Option_ for the indexed junction."; `FUEL TANK SELECTOR` legacy only; `FUELSYSTEM VALVE SWITCH`; `FUELSYSTEM TANK QUANTITY`), read 2026-11-14 |
| SDK-FUELE | MSFS 2024 SDK, Key events "Aircraft Fuel System Events", https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-fuel-system-events/ (`FUEL_SELECTOR_LEFT` "Turns selector 1 to LEFT position", `FUEL_SELECTOR_ALL`, `FUEL_SELECTOR_RIGHT`; `FUELSYSTEM_VALVE_TOGGLE` "[0]: Valve Index"), read 2026-11-14 |
| README | PilotsDeck README, https://github.com/Fragtality/PilotsDeck/blob/master/README.md: 2.1.1 (BVAR: "you can send/activate them with an optional Parameter", the variable "with preceding `B:`"; A-Var `(A:Name(:index), Unit)`), 2.2.2 (Format), 2.3 (Dynamic Button: the Special State with Any Value "for any Value which is not On or Off"; the value matching order On, Off, Special; read again 2026-11-15) |
| PD-SRC | PilotsDeck source at commit 11bdf1f7daf4828f822c18919952fe5b66153e58: https://github.com/Fragtality/PilotsDeck/blob/11bdf1f7daf4828f822c18919952fe5b66153e58/Plugin/Actions/Simple/ActionSwitchDisplay.cs (`Refresh()`: On image if the value compares to On, else Off image if it compares to Off, else the Indication image if `HasIndication` and the indication value or `IndicationValueAny`; otherwise no state image is drawn over the background) and `Plugin/Actions/Simple/ActionBaseSimple.cs` in the same commit (`CreateInstance`: the action `.action.switch.display`, the Dynamic Button, is `ActionSwitchDisplay`); `Plugin/Actions/Simple/ActionCommand.cs` (a B-Var with "Run as Command" unchecked is a value command; its state reads the Command Address), `Plugin/Actions/Simple/ValueState.cs` `GetSwitchValue` (calls `Toggle` with the key's On and Off values), `Plugin/Actions/ToolsValueState.cs` `Toggle` (the On value if the value read equals the Off value, else the Off value) and `Plugin/Simulator/ConnectorMSFS.cs` `SendInputEvent` (the value goes to the input event by `InputManager.SendEvent`), all in the same commit, read 2026-11-15 |
| PD-PI | The installed plugin's settings panel, `%APPDATA%\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\Plugin\PI\js\pi-Common.js` (sha256 e357a74d...: line 189 `regAvar`, 190 `regBvarValue`, 225-226 type 13 as a value, 237-239 `isValueCommand` "bvar requested" with lvar and avar), read 2026-11-15 |
| IE | [reference/InputEvents-C172-G1000.txt](reference/InputEvents-C172-G1000.txt) (IE n = line n: 140 alternator, 142 standby battery, 174, 175 avionics buses, 180 fuel selector, 181 fuel shutoff valve, 194, 195 cabin, 198, 199 panel, 200 pedestal, 201 potentiometer 5); the plugin's own `InputEvents.txt` for the C172 G1000 is byte-identical (sha256 4ea5f1ae..., 2026-11-14) |
| P1 | The Phase 1 export (`MSFS2024 C172 POC.streamDeckProfile`): key `p1:0,0` (BAT, Dynamic Button, B-Var `13`, On/Off `1`/`0`) and `p1:2,0` (Display Value) |
| Leads | Jiblet's C172 G1000 profile for the SD+XL (ALT on the alternator input event, BUS 1 / BUS 2 on the two line input events, written `1` / `0`; the fuel selector read as `(A:FUELSYSTEM JUNCTION SETTING:1, Number)` 1 = left, 2 = both, 3 = right). Leads only; every name above is confirmed in the SDK or the input event list; nothing copied. |
