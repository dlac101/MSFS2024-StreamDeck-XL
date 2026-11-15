# Phase 4: A32NX overhead pages (OVHD and SYSTEMS)

**Status: generated, not yet sim-tested.** Both pages are in the generated profile `MSFS2024 A32NX`, but
nothing on them has been tried in the app or the sim yet, and the A32NX is not yet installed on this PC (see
"Install status"). Every name below is recorded as "Unverified" in [aircraft-mappings.md](aircraft-mappings.md)
("FlyByWire A32NX (MSFS 2024)" for P4-1's keys, "FlyByWire A32NX overhead pages (P4-3)" for the new ones) until
the checks in [tests/manual-checklist.md](../tests/manual-checklist.md), sections "Phase 4: A32NX profile
(P4-1)" and "Phase 4: A32NX overhead pages (P4-3)", pass.

Goal: the A32NX overhead on two pages. **ovhd** (main 2,8 `OVHD`) is the power-up page: exterior lights and
signs, batteries and their voltages, external power, the engine and APU generators, BUS TIE and the APU. Its
folder key `SYSTEMS` (ovhd 2,8) opens **ovhdsys**, the panels set once per flight: the fuel panel (six pumps,
MODE SEL, X FEED and its valve), ADIRS (three IR knobs, ON BAT, alignment time), engine bleeds and packs, the
other ELEC pushbuttons (AC ESS FEED, GALY & CAB, COMMERCIAL) and anti-ice (WING, ENG 1, ENG 2, PROBE/WINDOW
HEAT). Every key lights or reads from the aircraft; no key assumes its press worked.

The pages are part of the profile `MSFS2024 A32NX` (same file, same name, same import as the main page: see
[phase4-a32nx.md](phase4-a32nx.md), "Import the profile"), and the SYSTEMS page's MODE SEL key uses the same
Lua script `XL24-A32NX.lua`, which must be copied into the plugin's Scripts folder again (P4-3 added
`FUELMODE`). The two key tables below are the reference for what each key holds;
`tools/profilegen/check.py tools/profilegen/a32nx.json` compares the profile with "Key table: ovhd" and "Key
table: ovhdsys" key by key. P4-1's 16 OVHD keys did not move or change; their rows, layout and description
moved here from phase4-a32nx.md.

Nothing on these pages uses keyboard bindings, vJoy or anything tied to a controller: the keys send SimConnect
events (standard K-events), write L-Vars or one input event (B-Var), run the Lua script, and read L-Vars and
SimVars, so they work the same with the Xbox Elite controller and the T.16000M + TWCS.

## Install status

- **The A32NX is not installed on this PC yet** (checked 2026-11-14, read only, as for P4-1 and P4-2): the
  MSFS 2024 package folders hold no FlyByWire package, and PilotsDeck has never seen an A32NX flight (no
  `InputEvents.txt` for it, no `A32NX` L-Var in its `L-Vars.txt`, no A32NX line in its newest log).
- FlyByWire's MSFS 2024 support is as in [phase4-a32nx.md](phase4-a32nx.md), "Install status" (Stable
  v2024.1.0, "not yet a native 2024 package"). FlyByWire's input events still cover only the ECAM control
  panel and the NAV & LOGO switch (FBW-IE), so the overhead uses the cockpit's own L-Vars and standard sim
  events.
- The sources are FlyByWire's master branch (no release tag pinned). The Flight Deck API page says "The below
  table might lag behind the current developments of the A32NX." (FBW-API): where it differs from the
  cockpit's own XML (COMMERCIAL `_PB_IS_ON`, APU GEN, anti-ice, engine bleeds), the XML wins.

## Where the pages sit

**ovhd** is a first-level folder page, opened by the folder key `OVHD` at **main 2,8**; its back key (1,1)
returns to the main page. **ovhdsys** is a second-level page, opened by the folder key `SYSTEMS` at **ovhd
2,8**; its back key (1,1) returns to the OVHD page, so the SYSTEMS page is two back presses from the main page
(the most [navigation.md](navigation.md) allows; ovhdsys holds no folder key). How the pages connect:
[navigation.md](navigation.md), "MSFS2024 A32NX pages".

## Layout: ovhd

Positions are **row,column**, 1-based, row 1 at the top. Folder keys end in `>`. Rows 1 and 2 are P4-1's
lights and signs (plus EMER EXIT and ANN LT), row 3 batteries, external power and the APU, row 4 the voltages,
EXT AVAIL and the generators.

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | STROBE | BEACON | WING | NAV LOGO | RWY TURN | LAND L | LAND R |
| **Row 2** | NOSE | SEAT BELT | NO SMOKE | EMER EXIT | ANN LT | | | SYSTEMS > |
| **Row 3** | BAT 1 | BAT 2 | EXT PWR | APU MSTR | APU START | APU AVAIL | APU BLEED | APU N |
| **Row 4** | BAT1 V | BAT2 V | EXT AVAIL | GEN 1 | GEN 2 | APU GEN | BUS TIE | |

28 keys (P4-1's 16, unchanged, and 12 new: EMER EXIT, ANN LT, APU BLEED, APU N, BAT1 V, BAT2 V, EXT AVAIL,
GEN 1, GEN 2, APU GEN, BUS TIE and the folder key SYSTEMS), the back key and 3 empty positions (2,6, 2,7,
4,8) reserved for a later unit.

## Key table: ovhd

Action names are the PilotsDeck README's: **Dynamic Button**, **Display Value**. **Folder** = the Stream Deck
app's own folder action, which opens a child page; **Back** = the Stream Deck app's back key (`backtoparent`),
added by the generator. "Empty" = no action on that key. The kinds K1 to K10 are explained in
[phase4-a32nx.md](phase4-a32nx.md), "What each key holds", K11 under "What each key holds" below; source tags
under "Sources" below. Command types: `K:` = K-Var (saved as 16), `L:` = L-Var (3; the key writes its On or Off
value), `B:` = B-Var (13), `lua:` = Lua Function (14).

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to the main page | none | Back key |
| 1,2 | `STROBE` | Display Value | K5 | `L:LIGHTING_STROBE_0`, On `0` / Off `1` (ON / AUTO) [FBW-API] | `L:LIGHTING_STROBE_0` [FBW-API] | Mappings `0=ON:1=AUTO:2=OFF` |
| 1,3 | `BEACON` | Dynamic Button | K1 | `K:TOGGLE_BEACON_LIGHTS` [SDK-ELECE] | `(A:LIGHT BEACON, Bool)` [FBW-API] | On/Off image |
| 1,4 | `WING` | Dynamic Button | K1 | `K:TOGGLE_WING_LIGHTS` [SDK-ELECE] | `(A:LIGHT WING, Bool)` [FBW-API] | On/Off image |
| 1,5 | `NAV LOGO` | Display Value | K8 | `B:A32NX_OVH_LIGHTS_NAV_LOGO_SW`, On `1` / Off `0` (SYS 1 / OFF) [FBW-IE, FBW-REL; README 2.1.1 BVAR] | `B:A32NX_OVH_LIGHTS_NAV_LOGO_SW` [FBW-IE] | Mappings `0=OFF:1=SYS 1:2=SYS 2` |
| 1,6 | `RWY TURN` | Dynamic Button | K1 | `K:ELECTRICAL_CIRCUIT_TOGGLE:21:K:ELECTRICAL_CIRCUIT_TOGGLE:22` (left and right light circuits) [SDK-ELECE, FBW-API; README 2.1.1 KVAR, PD-PI line 195] | `(A:CIRCUIT SWITCH ON:21, Bool)` [FBW-API] | On/Off image |
| 1,7 | `LAND L` | Display Value | K5 | `L:LIGHTING_LANDING_2`, On `0` / Off `2` (ON / RETRACT) [FBW-API] | `L:LIGHTING_LANDING_2` [FBW-API] | Mappings `0=ON:1=OFF:2=RETR` |
| 1,8 | `LAND R` | Display Value | K5 | `L:LIGHTING_LANDING_3`, On `0` / Off `2` (ON / RETRACT) [FBW-API] | `L:LIGHTING_LANDING_3` [FBW-API] | Mappings `0=ON:1=OFF:2=RETR` |
| 2,1 | `NOSE` | Display Value | K5 | `L:LIGHTING_LANDING_1`, On `0` / Off `1` (T.O. / TAXI) [FBW-API] | `L:LIGHTING_LANDING_1` [FBW-API] | Mappings `0=T.O.:1=TAXI:2=OFF` |
| 2,2 | `SEAT BELT` | Dynamic Button | K1 | `K:CABIN_SEATBELTS_ALERT_SWITCH_TOGGLE` [FBW-API] | `(A:CABIN SEATBELTS ALERT SWITCH, Bool)` [FBW-API] | On/Off image |
| 2,3 | `NO SMOKE` | Display Value | K5 | `L:XMLVAR_SWITCH_OVHD_INTLT_NOSMOKING_POSITION`, On `0` / Off `1` (ON / AUTO) [FBW-API] | `L:XMLVAR_SWITCH_OVHD_INTLT_NOSMOKING_POSITION` [FBW-API] | Mappings `0=ON:1=AUTO:2=OFF` |
| 2,4 | `EMER EXIT` | Display Value | K5 | `L:XMLVAR_SWITCH_OVHD_INTLT_EMEREXIT_POSITION`, On `1` / Off `2` (ARM / OFF) [FBW-API] | `L:XMLVAR_SWITCH_OVHD_INTLT_EMEREXIT_POSITION` [FBW-API] | Mappings `0=ON:1=ARM:2=OFF` |
| 2,5 | `ANN LT` | Display Value | K5 | `L:A32NX_OVHD_INTLT_ANN`, On `0` / Off `1` (TEST / BRT) [FBW-API, FBW-SIMVARS] | `L:A32NX_OVHD_INTLT_ANN` [FBW-API, FBW-SIMVARS] | Mappings `0=TEST:1=BRT:2=DIM` |
| 2,6 | | Empty | | | | Reserved (a later unit) |
| 2,7 | | Empty | | | | Reserved (a later unit) |
| 2,8 | `SYSTEMS` | Folder | (Stream Deck) | Opens the child page **ovhdsys** | none | Folder; the page's keys: "Key table: ovhdsys" below |
| 3,1 | `BAT 1` | Dynamic Button | K2 | `L:A32NX_OVHD_ELEC_BAT_1_PB_IS_AUTO`, On `1` / Off `0` (AUTO / OFF) [FBW-API] | `L:A32NX_OVHD_ELEC_BAT_1_PB_IS_AUTO` [FBW-API, FBW-SIMVARS] | On/Off image, Special State |
| 3,2 | `BAT 2` | Dynamic Button | K2 | `L:A32NX_OVHD_ELEC_BAT_2_PB_IS_AUTO`, On `1` / Off `0` (AUTO / OFF) [FBW-API] | `L:A32NX_OVHD_ELEC_BAT_2_PB_IS_AUTO` [FBW-API, FBW-SIMVARS] | On/Off image, Special State |
| 3,3 | `EXT PWR` | Dynamic Button | K2 | `L:A32NX_OVHD_ELEC_EXT_PWR_PB_IS_ON`, On `1` / Off `0` [FBW-API] | `L:A32NX_OVHD_ELEC_EXT_PWR_PB_IS_ON` [FBW-API] | On/Off image, Special State |
| 3,4 | `APU MSTR` | Dynamic Button | K2 | `L:A32NX_OVHD_APU_MASTER_SW_PB_IS_ON`, On `1` / Off `0` [FBW-API] | `L:A32NX_OVHD_APU_MASTER_SW_PB_IS_ON` [FBW-API, FBW-SIMVARS] | On/Off image, Special State |
| 3,5 | `APU START` | Dynamic Button | K2 | `L:A32NX_OVHD_APU_START_PB_IS_ON`, On `1` / Off `1` (always writes 1) [FBW-API] | `L:A32NX_OVHD_APU_START_PB_IS_ON` [FBW-API, FBW-SIMVARS] | On/Off image, Special State |
| 3,6 | `APU AVAIL` | Display Value | K9 | none | `L:A32NX_OVHD_APU_START_PB_IS_AVAILABLE` [FBW-API, FBW-SIMVARS] | Mappings `0=---:1=AVAIL` |
| 3,7 | `APU BLEED` | Dynamic Button | K2 | `L:A32NX_OVHD_PNEU_APU_BLEED_PB_IS_ON`, On `1` / Off `0` [FBW-API, FBW-MISC] | `L:A32NX_OVHD_PNEU_APU_BLEED_PB_IS_ON` [FBW-API, FBW-MISC] | On/Off image, Special State |
| 3,8 | `APU N` | Display Value | K11 | none | `L:A32NX_APU_N_RAW` [FBW-SIMVARS] | Format `1.0` |
| 4,1 | `BAT1 V` | Display Value | K11 | none | `L:A32NX_ELEC_BAT_1_POTENTIAL` [FBW-API, FBW-SIMVARS] | Format `1.1` |
| 4,2 | `BAT2 V` | Display Value | K11 | none | `L:A32NX_ELEC_BAT_2_POTENTIAL` [FBW-API, FBW-SIMVARS] | Format `1.1` |
| 4,3 | `EXT AVAIL` | Display Value | K9 | none | `L:A32NX_EXT_PWR_AVAIL:1` [FBW-API, FBW-SIMVARS, FBW-ELEC; PD-PI line 181] | Mappings `0=---:1=AVAIL` |
| 4,4 | `GEN 1` | Dynamic Button | K1 | `K:TOGGLE_ALTERNATOR1` [FBW-ELEC, SDK-ELECE] | `(A:GENERAL ENG MASTER ALTERNATOR:1, Bool)` [FBW-ELEC, FBW-API] | On/Off image |
| 4,5 | `GEN 2` | Dynamic Button | K1 | `K:TOGGLE_ALTERNATOR2` [FBW-ELEC, SDK-ELECE] | `(A:GENERAL ENG MASTER ALTERNATOR:2, Bool)` [FBW-ELEC, FBW-API] | On/Off image |
| 4,6 | `APU GEN` | Dynamic Button | K1 | `K:APU_GENERATOR_SWITCH_TOGGLE:1` [FBW-ELEC, SDK-ELECE; README 3.5.1] | `(A:APU GENERATOR SWITCH:1, Bool)` [FBW-ELEC] | On/Off image |
| 4,7 | `BUS TIE` | Dynamic Button | K2 | `L:A32NX_OVHD_ELEC_BUS_TIE_PB_IS_AUTO`, On `1` / Off `0` [FBW-API, FBW-INTERIOR] | `L:A32NX_OVHD_ELEC_BUS_TIE_PB_IS_AUTO` [FBW-API, FBW-INTERIOR] | On/Off image, Special State |
| 4,8 | | Empty | | | | Reserved (a later unit) |

## Layout: ovhdsys

Row 1 is the fuel panel's pumps left to right (left tank, centre tank, right tank) and MODE SEL; row 2 X FEED,
its valve and ADIRS (the IR knobs in the cockpit's left-to-right order 1, 3, 2), row 3 the engine bleeds, the
packs and the ELEC pushbuttons, row 4 anti-ice and probe heat.

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | L TK 1 | L TK 2 | CTR TK 1 | CTR TK 2 | R TK 1 | R TK 2 | MODE SEL |
| **Row 2** | X FEED | XFEED VLV | IR 1 | IR 3 | IR 2 | ON BAT | ALIGN | |
| **Row 3** | BLEED 1 | BLEED 2 | PACK 1 | PACK 2 | ESS FEED | GALY CAB | COMML | |
| **Row 4** | WING A/I | ENG1 A/I | ENG2 A/I | PROBE HT | | | | |

25 keys, the back key and 6 empty positions (2,8, 3,8, 4,5 to 4,8) reserved for a later unit.

## Key table: ovhdsys

Forms as in "Key table: ovhd".

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to the OVHD page | none | Back key |
| 1,2 | `L TK 1` | Dynamic Button | K1 | `K:FUELSYSTEM_PUMP_TOGGLE:2` [FBW-MISC, FBW-INTERIOR, SDK-FUELE] | `(A:FUELSYSTEM PUMP SWITCH:2, Enum)` [FBW-MISC] | On/Off image |
| 1,3 | `L TK 2` | Dynamic Button | K1 | `K:FUELSYSTEM_PUMP_TOGGLE:5` [FBW-MISC, FBW-INTERIOR, SDK-FUELE] | `(A:FUELSYSTEM PUMP SWITCH:5, Enum)` [FBW-MISC] | On/Off image |
| 1,4 | `CTR TK 1` | Dynamic Button | K1 | `K:FUELSYSTEM_VALVE_TOGGLE:9` [FBW-MISC, FBW-INTERIOR, SDK-FUELE] | `(A:FUELSYSTEM VALVE SWITCH:9, Enum)` [FBW-MISC] | On/Off image |
| 1,5 | `CTR TK 2` | Dynamic Button | K1 | `K:FUELSYSTEM_VALVE_TOGGLE:10` [FBW-MISC, FBW-INTERIOR, SDK-FUELE] | `(A:FUELSYSTEM VALVE SWITCH:10, Enum)` [FBW-MISC] | On/Off image |
| 1,6 | `R TK 1` | Dynamic Button | K1 | `K:FUELSYSTEM_PUMP_TOGGLE:3` [FBW-MISC, FBW-INTERIOR, SDK-FUELE] | `(A:FUELSYSTEM PUMP SWITCH:3, Enum)` [FBW-MISC] | On/Off image |
| 1,7 | `R TK 2` | Dynamic Button | K1 | `K:FUELSYSTEM_PUMP_TOGGLE:6` [FBW-MISC, FBW-INTERIOR, SDK-FUELE] | `(A:FUELSYSTEM PUMP SWITCH:6, Enum)` [FBW-MISC] | On/Off image |
| 1,8 | `MODE SEL` | Dynamic Button | K10 | `lua:XL24-A32NX:FUELMODE` (the script runs the cockpit's MODE SEL code) [FBW-INTERIOR, SDK-FUELE; README 3.5.1] | `L:A32NX_OVHD_FUEL_MODESEL_MANUAL` [FBW-INTERIOR] | On/Off image (lit = MAN) |
| 2,1 | `X FEED` | Dynamic Button | K1 | `K:FUELSYSTEM_VALVE_TOGGLE:3` [FBW-MISC, FBW-INTERIOR, SDK-FUELE] | `(A:FUELSYSTEM VALVE SWITCH:3, Bool)` [FBW-MISC] | On/Off image |
| 2,2 | `XFEED VLV` | Display Value | K9 | none | `(A:FUELSYSTEM VALVE OPEN:3, Bool)` [FBW-MISC, FBW-API] | Mappings `0=SHUT:1=OPEN` |
| 2,3 | `IR 1` | Display Value | K5 | `L:A32NX_OVHD_ADIRS_IR_1_MODE_SELECTOR_KNOB`, On `1` / Off `0` (NAV / OFF) [FBW-API, FBW-SIMVARS, FBW-ADIRS] | `L:A32NX_OVHD_ADIRS_IR_1_MODE_SELECTOR_KNOB` [FBW-API, FBW-SIMVARS, FBW-ADIRS] | Mappings `0=OFF:1=NAV:2=ATT` |
| 2,4 | `IR 3` | Display Value | K5 | `L:A32NX_OVHD_ADIRS_IR_3_MODE_SELECTOR_KNOB`, On `1` / Off `0` (NAV / OFF) [FBW-API, FBW-SIMVARS, FBW-ADIRS] | `L:A32NX_OVHD_ADIRS_IR_3_MODE_SELECTOR_KNOB` [FBW-API, FBW-SIMVARS, FBW-ADIRS] | Mappings `0=OFF:1=NAV:2=ATT` |
| 2,5 | `IR 2` | Display Value | K5 | `L:A32NX_OVHD_ADIRS_IR_2_MODE_SELECTOR_KNOB`, On `1` / Off `0` (NAV / OFF) [FBW-API, FBW-SIMVARS, FBW-ADIRS] | `L:A32NX_OVHD_ADIRS_IR_2_MODE_SELECTOR_KNOB` [FBW-API, FBW-SIMVARS, FBW-ADIRS] | Mappings `0=OFF:1=NAV:2=ATT` |
| 2,6 | `ON BAT` | Display Value | K9 | none | `L:A32NX_OVHD_ADIRS_ON_BAT_IS_ILLUMINATED` [FBW-API, FBW-INTERIOR] | Mappings `0=---:1=ON BAT` |
| 2,7 | `ALIGN` | Display Value | K11 | none | `L:A32NX_ADIRS_REMAINING_IR_ALIGNMENT_TIME` [FBW-API, FBW-SIMVARS] | Format `1.0` |
| 2,8 | | Empty | | | | Reserved (a later unit) |
| 3,1 | `BLEED 1` | Dynamic Button | K2 | `L:A32NX_OVHD_PNEU_ENG_1_BLEED_PB_IS_AUTO`, On `1` / Off `0` [FBW-SIMVARS, FBW-MISC] | `L:A32NX_OVHD_PNEU_ENG_1_BLEED_PB_IS_AUTO` [FBW-SIMVARS, FBW-MISC] | On/Off image, Special State |
| 3,2 | `BLEED 2` | Dynamic Button | K2 | `L:A32NX_OVHD_PNEU_ENG_2_BLEED_PB_IS_AUTO`, On `1` / Off `0` [FBW-SIMVARS, FBW-MISC] | `L:A32NX_OVHD_PNEU_ENG_2_BLEED_PB_IS_AUTO` [FBW-SIMVARS, FBW-MISC] | On/Off image, Special State |
| 3,3 | `PACK 1` | Dynamic Button | K2 | `L:A32NX_OVHD_COND_PACK_1_PB_IS_ON`, On `1` / Off `0` [FBW-API, FBW-SIMVARS, FBW-INTERIOR] | `L:A32NX_OVHD_COND_PACK_1_PB_IS_ON` [FBW-API, FBW-SIMVARS, FBW-INTERIOR] | On/Off image, Special State |
| 3,4 | `PACK 2` | Dynamic Button | K2 | `L:A32NX_OVHD_COND_PACK_2_PB_IS_ON`, On `1` / Off `0` [FBW-API, FBW-SIMVARS, FBW-INTERIOR] | `L:A32NX_OVHD_COND_PACK_2_PB_IS_ON` [FBW-API, FBW-SIMVARS, FBW-INTERIOR] | On/Off image, Special State |
| 3,5 | `ESS FEED` | Dynamic Button | K2 | `L:A32NX_OVHD_ELEC_AC_ESS_FEED_PB_IS_NORMAL`, On `1` / Off `0` [FBW-API, FBW-SIMVARS, FBW-INTERIOR] | `L:A32NX_OVHD_ELEC_AC_ESS_FEED_PB_IS_NORMAL` [FBW-API, FBW-SIMVARS, FBW-INTERIOR] | On/Off image, Special State |
| 3,6 | `GALY CAB` | Dynamic Button | K2 | `L:A32NX_OVHD_ELEC_GALY_AND_CAB_PB_IS_AUTO`, On `1` / Off `0` [FBW-API, FBW-SIMVARS, FBW-INTERIOR] | `L:A32NX_OVHD_ELEC_GALY_AND_CAB_PB_IS_AUTO` [FBW-API, FBW-SIMVARS, FBW-INTERIOR] | On/Off image, Special State |
| 3,7 | `COMML` | Dynamic Button | K2 | `L:A32NX_OVHD_ELEC_COMMERCIAL_PB_IS_ON`, On `1` / Off `0` [FBW-SIMVARS, FBW-INTERIOR] | `L:A32NX_OVHD_ELEC_COMMERCIAL_PB_IS_ON` [FBW-SIMVARS, FBW-INTERIOR] | On/Off image, Special State |
| 3,8 | | Empty | | | | Reserved (a later unit) |
| 4,1 | `WING A/I` | Dynamic Button | K2 | `L:A32NX_BUTTON_OVHD_ANTI_ICE_WING_POSITION`, On `1` / Off `0` [FBW-MISC] | `L:A32NX_BUTTON_OVHD_ANTI_ICE_WING_POSITION` [FBW-MISC] | On/Off image, Special State |
| 4,2 | `ENG1 A/I` | Dynamic Button | K2 | `L:A32NX_BUTTON_OVHD_ANTI_ICE_ENG_1_POSITION`, On `1` / Off `0` [FBW-MISC, FBW-SIMVARS] | `L:A32NX_BUTTON_OVHD_ANTI_ICE_ENG_1_POSITION` [FBW-MISC, FBW-SIMVARS] | On/Off image, Special State |
| 4,3 | `ENG2 A/I` | Dynamic Button | K2 | `L:A32NX_BUTTON_OVHD_ANTI_ICE_ENG_2_POSITION`, On `1` / Off `0` [FBW-MISC, FBW-SIMVARS] | `L:A32NX_BUTTON_OVHD_ANTI_ICE_ENG_2_POSITION` [FBW-MISC, FBW-SIMVARS] | On/Off image, Special State |
| 4,4 | `PROBE HT` | Dynamic Button | K2 | `L:A32NX_MAN_PITOT_HEAT`, On `1` / Off `0` [FBW-API, FBW-MISC] | `L:A32NX_MAN_PITOT_HEAT` [FBW-API, FBW-MISC] | On/Off image, Special State |
| 4,5 | | Empty | | | | Reserved (a later unit) |
| 4,6 | | Empty | | | | Reserved (a later unit) |
| 4,7 | | Empty | | | | Reserved (a later unit) |
| 4,8 | | Empty | | | | Reserved (a later unit) |

## What the keys do

OVHD page, P4-1's keys (unchanged): STROBE, BEACON, NAV LOGO, LAND L/R, NOSE and SEAT BELT are the main page's
keys. **WING** toggles the wing lights; **RWY TURN** toggles both runway turn-off light circuits (21 left, 22
right) and lights from the left one; **NO SMOKE** toggles ON and AUTO and shows all three positions; **BAT 1,
BAT 2** switch the battery pushbuttons between AUTO (lit) and OFF; **EXT PWR** and **APU MSTR** switch their
pushbuttons; **APU START** always writes 1 (start) and lights while the START pushbutton is on; **APU AVAIL**
shows `AVAIL` when the APU is available.

OVHD page, new keys:
- **EMER EXIT** toggles the EMER EXIT LT switch between ARM and OFF and shows all three positions (`ON`, `ARM`,
  `OFF`; ON is set in the cockpit). FlyByWire's API names the middle value AUTO; the cockpit labels it ARM.
- **ANN LT** toggles the ANN LT switch between TEST (every annunciator lit: each FlyByWire pushbutton light
  reads `(L:A32NX_OVHD_INTLT_ANN) 0 ==`, FBW-GEN) and BRT, and shows `TEST`, `BRT` or `DIM` (DIM is set in the
  cockpit).
- **APU BLEED** switches the APU BLEED pushbutton (lit = ON).
- **APU N** shows the APU speed in percent (`0` to about `100`), **BAT1 V / BAT2 V** the battery voltages
  (`25.4`), from the L-Vars; read only.
- **EXT AVAIL** shows `AVAIL` while ground power is available, `---` otherwise; read only. The cockpit's
  EXT PWR AVAIL light is lit only while ground power is available and EXT PWR is off; once EXT PWR is on,
  the pushbutton shows ON instead (FBW-ELEC), and the key still shows `AVAIL`.
- **GEN 1, GEN 2, APU GEN** send the cockpit's own events (the engine generator and APU generator
  pushbuttons) and are lit while the generator switch is on (the cockpit's OFF light is out).
- **BUS TIE** switches the BUS TIE pushbutton (lit = AUTO).
- **SYSTEMS** opens the SYSTEMS page.

SYSTEMS page:
- **L TK 1, L TK 2, R TK 1, R TK 2** toggle the wing tank pumps (fuel pump indexes 2, 5, 3, 6) and **CTR TK 1,
  CTR TK 2** the centre tank jet pump valves (valve indexes 9, 10), with the events the cockpit pushbuttons send;
  each is lit while its pump or valve switch is on (the cockpit's OFF light is out).
- **MODE SEL** runs the script's `FUELMODE`, which runs the cockpit pushbutton's own code (see "The script");
  lit while the mode is MAN.
- **X FEED** toggles the crossfeed valve switch (valve index 3) and is lit while the switch is on (the
  cockpit's ON light); **XFEED VLV** shows the valve itself, `OPEN` or `SHUT` (the cockpit's OPEN light; the
  valve takes a moment to move).
- **IR 1, IR 3, IR 2** toggle the IR mode knobs between NAV and OFF and show `OFF`, `NAV` or `ATT`; ATT is set
  in the cockpit, and a press from ATT writes OFF. A press from NAV or ATT turns that IR off, and it must
  align again (ALIGN): press these keys on the ground only.
- **ON BAT** shows `ON BAT` while the ADIRS ON BAT light is on, `---` otherwise; **ALIGN** the remaining IR
  alignment time in seconds (`0` when aligned or not aligning); read only.
- **BLEED 1, BLEED 2** switch the engine bleed pushbuttons (lit = AUTO), **PACK 1, PACK 2** the packs (lit =
  ON), **ESS FEED** the AC ESS FEED pushbutton (lit = NORMAL), **GALY CAB** GALY & CAB (lit = AUTO), **COMML**
  COMMERCIAL (lit = ON).
- **WING A/I, ENG1 A/I, ENG2 A/I** switch the anti-ice pushbuttons, **PROBE HT** PROBE/WINDOW HEAT (lit = ON,
  manual on).

Which variable lights a pushbutton key: the switch position (the variable the cockpit's ON / OFF / AUTO legend
reads, or the L-Var its click toggles), because the key is that button and shows where it was left. System
state the cockpit shows on a separate light has its own readout where a flow needs it: EXT AVAIL, APU AVAIL,
XFEED VLV, ON BAT. FAULT lights (`*_PB_HAS_FAULT`, the fuel LO PR lights) are not shown; the ECAM shows them.
WING A/I reads the button L-Var its click writes, not `L:A32NX_PNEU_WING_ANTI_ICE_SYSTEM_SELECTED` (the
cockpit's ON light), so the key reads and writes one variable as every K2 key (PilotsDeck compares the current
value with the Off Value, README 2.1.2).

## What each key holds

The kinds K1 to K10 of [phase4-a32nx.md](phase4-a32nx.md), "What each key holds": every key is a copy of a
real saved key with only the listed fields changed (the generator does this). On these pages: K1 (BEACON, WING,
RWY TURN, SEAT BELT, GEN 1, GEN 2, APU GEN, the six tank keys, X FEED), K2 (BAT 1, BAT 2, EXT PWR, APU MSTR, APU
START, APU BLEED, BUS TIE, BLEED 1/2, PACK 1/2, ESS FEED, GALY CAB, COMML, WING A/I, ENG1/ENG2 A/I, PROBE HT),
K5 (STROBE, LAND L/R, NOSE, NO SMOKE, EMER EXIT, ANN LT, IR 1/3/2), K8 (NAV LOGO), K9 (APU AVAIL, EXT AVAIL,
XFEED VLV, ON BAT), K10 (MODE SEL) and one new kind:

| Kind | Action, copied from | Fields set |
|---|---|---|
| K11 numeric readout | Display Value, the Phase 1 HDG key (`p1:2,0`, T3) | Value Address (`L:`), Format (README 2.2.2, "Syntax: `Zeros.Fraction:Text %s Text`": `1.0` = no decimal, `1.1` = one decimal); no command (the template's L-Var type 3 with an empty Command Address), no mappings |

APU N, BAT1 V, BAT2 V and ALIGN are K11. The data file is `tools/profilegen/a32nx.json`, pages `ovhd` and
`ovhdsys` (`"spec": "docs/phase4-a32nx-overhead.md"`; ovhdsys has `"parent": "ovhd"`).

Title sizes ([navigation.md](navigation.md), "Rules"): Dynamic Buttons copied from the AP key draw their titles
at 14, the ones copied from the BAT key keep 15; titles of 8 or more characters on Dynamic Buttons are set to
13 (P4-1's `SEAT BELT`, `RWY TURN`, `APU MSTR`, `APU START`; new `APU BLEED`, `CTR TK 1`, `CTR TK 2`,
`MODE SEL`, `ESS FEED`, `GALY CAB`, `WING A/I`, `ENG1 A/I`, `ENG2 A/I`, `PROBE HT`); Display Values keep their
template size (15), `EMER EXIT`, `EXT AVAIL` and `XFEED VLV` included.

## The script

[`pilotsdeck/MSFS2024-XL/_Package/Scripts/XL24-A32NX.lua`](../pilotsdeck/MSFS2024-XL/_Package/Scripts/XL24-A32NX.lua)
(the main page's script, [phase4-a32nx.md](phase4-a32nx.md), "The script"). P4-3 added one function at the end
and one header comment line; nothing that was there changed. The new L-Var is registered with `SimVar(...)` at
the top level of the file, as the others.

| Function | Does | Reads / writes |
|---|---|---|
| `FUELMODE()` | does nothing unless `L:A32NX_TOTAL_FUEL_QUANTITY` reads more than 0; then runs, with `SimCalculator` (README 3.5.1: "Run Calculator Code in the Sim."), the code the cockpit's MODE SEL pushbutton runs on a click: `(L:A32NX_OVHD_FUEL_MODESEL_MANUAL) ! s0 (>L:A32NX_OVHD_FUEL_MODESEL_MANUAL) 1 l0 + sp0 l0 4 (>K:2:FUELSYSTEM_JUNCTION_SET) l0 5 (>K:2:FUELSYSTEM_JUNCTION_SET)` (FBW-INTERIOR, `PUSH_OVHD_FUEL_MODESEL`, `LEFT_SINGLE_CODE`): it flips the MAN L-Var and sets fuel junctions 4 and 5 to option 1 (AUTO) or 2 (MAN) (SDK-FUELE: `FUELSYSTEM_JUNCTION_SET` "[0]: Junction Index[1]: Option index") | reads `L:A32NX_TOTAL_FUEL_QUANTITY`; the code reads and writes `L:A32NX_OVHD_FUEL_MODESEL_MANUAL` and sends `FUELSYSTEM_JUNCTION_SET` |

- The guard: `A32NX_TOTAL_FUEL_QUANTITY` is FlyByWire's L-Var for "The total physical quantity of fuel in the
  tanks" (kg, FBW-SIMVARS). Another aircraft has no such L-Var (it reads 0), so the junction events never reach
  it. An A32NX with empty tanks also reads 0: then MODE SEL does nothing (nothing to select).
- **The MobiFlight WASM module.** PilotsDeck sends a script's `SimCalculator` code through the MobiFlight WASM
  module (PilotsDeck source at `11bdf1f`, PD-SRC; line numbers as a fetch tool counted them on GitHub, which
  may be one or two off):
  `Plugin/Resources/Scripts/ManagedScript.cs` line 98 registers the Lua function
  (`_env.SimCalculator = new Func<string, bool>(SimCalculator);`), and its method `SimCalculator(string code)`
  (lines 393-402) puts a command of type `SimCommandType.CALCULATOR` on `SimController.CommandChannel`;
  `Plugin/Simulator/SimController.cs` reads that channel (line 274) and passes each command to the connector's
  `RunCommand` (line 303); `Plugin/Simulator/ConnectorMSFS.cs` `RunCommand` sends a CALCULATOR command to
  `ExecuteCalculatorCode` (lines 369-370), which calls `MobiModule.ExecuteCode(command.Address.Name)` (lines
  551-569, the call at line 559); `MobiModule` is the MobiFlight module of CFIT.SimConnectLib (line 6
  `using CFIT.SimConnectLib.Modules.MobiFlight;`, line 57). So **MODE SEL needs the MobiFlight WASM module
  installed** (see [installation.md](installation.md), "MobiFlight WASM module"; it is installed on this PC,
  1.0.1). CFIT.SimConnectLib's own source (CFIT-SRC) shows why: `MobiModule.ExecuteCode` sends the code as
  the MobiFlight command `MF.SimVars.Set.<code>` on the client command channel that the MobiFlight WASM
  module creates and reads, and it does not check that the module is connected. Without the module the
  press does nothing, most likely with no alert sign on the key (`ExecuteCode` returns true unless an
  exception is thrown). Which library version the installed plugin build contains was not checked. Every
  other key on these pages is a K-Var, L-Var, A-Var read or B-Var: no other key needs the module.

## What the keys show when the A32NX isn't there

- No sim, or no flight: PilotsDeck's own idle and waiting images, as on the other pages.
- Another aircraft (or the A32NX not powered): every key shows what its variable reads. An L-Var the aircraft
  doesn't have reads 0, so the K2 pushbutton keys (BAT, EXT PWR, APU, APU BLEED, BUS TIE, BLEED, PACK, ESS
  FEED, GALY CAB, COMML, anti-ice, PROBE HT) and MODE SEL show off, STROBE, LAND L/R and NO SMOKE `ON`, NOSE
  `T.O.`, **EMER EXIT `ON`, ANN LT `TEST`**, IR 1/3/2 `OFF`, APU AVAIL, EXT AVAIL and ON BAT `---`, BAT1 V and
  BAT2 V `0.0`, APU N and ALIGN `0`. That is the 0 of a missing variable, not the aircraft's state.
- The standard SimVars (BEACON, WING, RWY TURN, SEAT BELT, GEN 1/2, APU GEN, the six tank keys, X FEED, XFEED
  VLV) read the other aircraft's own state, and **their presses act on any aircraft that has those indexes**
  (they are standard sim events, as P4-1's BEACON): keep the profile on the A32NX with the Profile Manager's
  aircraft mapping, and don't press them in another aircraft.
- MODE SEL does nothing in another aircraft (the guard, see "The script").
- A command the sim refuses shows PilotsDeck's alert sign on the key.

## Fallbacks

Use one only if the checklist shows the main route does not work, and say which one you used. None is tested.
A key that fails with no working fallback becomes readout-only (command none) or Empty, and its row in
aircraft-mappings.md says "does not work". The fallbacks of P4-1's OVHD keys (STROBE, LAND L/R, NOSE, NO
SMOKE, NAV LOGO, RWY TURN) are in [phase4-a32nx.md](phase4-a32nx.md), "Fallbacks".

| Key | If it fails | Fallback | Source |
|---|---|---|---|
| MODE SEL (A-6) | The press does nothing (check first: the MobiFlight WASM module is installed and the plugin log shows "MobiFlight WASM Client Connection opened"; the plugin log shows the command) | In `FUELMODE`: `SimWrite` the MAN L-Var (`L:A32NX_OVHD_FUEL_MODESEL_MANUAL`, 1 or 0), then `SimCommand("K:FUELSYSTEM_JUNCTION_SET:4:<1\|2>")` and the same with `:5:` (K-Var with parameters, README 2.1.1; order "[0]: Junction Index[1]: Option index", SDK-FUELE; 1 = AUTO, 2 = MAN as the cockpit code); this route does not use the MobiFlight module. If that fails: readout only (command none) | FBW-INTERIOR, SDK-FUELE; README 2.1.1, 3.5.1; PD-SRC |
| EXT AVAIL (A-7) | It reads `---` while the cockpit's EXT PWR AVAIL light is on | Read `L:A32NX_ELEC_EXT_PWR_POTENTIAL_NORMAL` ("Indicates if the potential is within the normal range", FBW-SIMVARS) instead | FBW-SIMVARS, FBW-API |
| APU N (A-8) | It does not match the ECAM's APU N | The key becomes Empty (the ECAM value, `A32NX_APU_N`, is an Arinc429 word, which the script does not decode) | FBW-SIMVARS |
| ALIGN (A-9) | It stays `0` while the IRs align (FlyByWire lists the L-Var as deprecated: "use A32NX_ADIRS_IR_{number}_MAINT_WORD instead") | The key becomes Empty | FBW-SIMVARS, FBW-API |
| Any new L-Var key (A-4) | Writing the L-Var doesn't move the pushbutton or knob | That key becomes a readout (command none), same read | FBW-API, FBW-INTERIOR, FBW-MISC |
| IR 1, IR 3, IR 2 (A-14) | The keys are not in the cockpit's left-to-right order | Swap the positions in the data file and this doc only | aircraft knowledge |

## How to test

Run [tests/manual-checklist.md](../tests/manual-checklist.md), section "Phase 4: A32NX overhead pages (P4-3)",
after the P4-1 section's "Before you start" and "Import" steps. As on the other pages, check both directions:
press a key and watch the cockpit, then **move the control in the cockpit with the mouse and check that the
key follows without a key being pressed.** Record whether EXT AVAIL follows the cockpit's AVAIL light, whether
APU N matches the ECAM, whether ALIGN counts down, and what MODE SEL does.

## When it passes

1. Any change found in the test goes into `tools/profilegen/a32nx.json`, the script and this doc; then the
   profile is regenerated (not exported from the app) and imported again, and the script copied again.
2. Fill in the "Verified" column of the rows in aircraft-mappings.md ("FlyByWire A32NX overhead pages (P4-3)",
   and P4-1's OVHD rows in "FlyByWire A32NX (MSFS 2024)") with the date, sim version and A32NX version, for each
   function that passed; mark a row "does not work" where a key failed.

## Sources

FlyByWire sources: the flybywiresim/aircraft repository (master) or FlyByWire's docs site, read 2026-11-14.
The tags FBW-API, FBW-IE, FBW-REL, SDK-ELECE, README and PD-PI of P4-1's rows are the ones of
[phase4-a32nx.md](phase4-a32nx.md), "Sources".

| Tag | Source |
|---|---|
| FBW-API | FlyByWire Flight Deck API, https://docs.flybywiresim.com/aircraft/a32nx/a32nx-api/a32nx-flightdeck-api/ ("The below table might lag behind the current developments of the A32NX."), "Overhead Forward": ELEC (BAT 1/2 display `A32NX_ELEC_BAT_1_POTENTIAL` "0.0..99.9", `A32NX_EXT_PWR_AVAIL:1`, BUS TIE, AC ESS FEED, GALY & CAB R/W), Fuel (pump indexes "L1=2, L2=5, C1=9, C2=10, R1=3, R2=6", X FEED valve 3, `FUELSYSTEM VALVE OPEN`, "MODE SEL \| N/A"), ADIRS (knobs "0=OFF, 1=NAV, 2=ATT", "Replace `1` with `2` or `3`", ON BAT light, remaining alignment time), Air Condition (APU BLEED, PACK 1/2 R/W), Anti Ice (PROBE/WINDOW HEAT `A32NX_MAN_PITOT_HEAT` R/W), Interior Lights (EMER EXIT LT "0=ON, 1=AUTO, 2=OFF", ANN LT "2=DIM, 1=BRT, 0=TEST"); and P4-1's rows |
| FBW-SIMVARS | `fbw-a32nx/docs/a320-simvars.md`, https://raw.githubusercontent.com/flybywiresim/aircraft/master/fbw-a32nx/docs/a320-simvars.md (master): `A32NX_ELEC_{name}_POTENTIAL` (Volts), `_POTENTIAL_NORMAL`, `L:A32NX_EXT_PWR_AVAIL:{number}`, `A32NX_OVHD_ELEC_AC_ESS_FEED_PB_IS_NORMAL`, the `_PB_IS_AUTO` and `_PB_IS_ON` lists (COMMERCIAL `_PB_IS_ON`), `A32NX_APU_N_RAW` ("This raw value should only be used for sounds and effects."), `A32NX_APU_N` (Arinc429), the ADIRS knob values, `A32NX_ADIRS_REMAINING_IR_ALIGNMENT_TIME` (deprecated), `A32NX_OVHD_PNEU_ENG_{number}_BLEED_PB_IS_AUTO`, `A32NX_OVHD_COND_PACK_{1,2}_PB_IS_ON`, `A32NX_BUTTON_OVHD_ANTI_ICE_ENG_1_POSITION`, `A32NX_OVHD_INTLT_ANN`, `A32NX_TOTAL_FUEL_QUANTITY` |
| FBW-INTERIOR | `A320_NEO_INTERIOR.xml`, https://raw.githubusercontent.com/flybywiresim/aircraft/master/fbw-a32nx/src/base/flybywire-aircraft-a320-neo/SimObjects/AirPlanes/FlyByWire_A320_NEO/model/A320_NEO_INTERIOR.xml (master): the overhead `UseTemplate` blocks: `TOGGLE_SIMVAR` of BUS TIE, AC ESS FEED, GALY & CAB, COMMERCIAL, PACK 1/2; the fuel pushbuttons' `ID`s (LTKPUMPS1 2, LTKPUMPS2 5, RTKPUMPS1 3, RTKPUMPS2 6, PUMP1 9, PUMP2 10, XFEED 3); `PUSH_OVHD_FUEL_MODESEL` (`SEQ2_CODE`, `LEFT_SINGLE_CODE`); the ADIRS ON BAT annunciator |
| FBW-ELEC | `fbw-a32nx/src/behavior/src/A32NX_Interior_Elec.xml`, https://raw.githubusercontent.com/flybywiresim/aircraft/master/fbw-a32nx/src/behavior/src/A32NX_Interior_Elec.xml (master): GEN click `(>K:TOGGLE_ALTERNATOR#ID#)` and OFF light `(A:GENERAL ENG MASTER ALTERNATOR:#ID#, Bool) !`; APU GEN click `#ID# (>K:APU_GENERATOR_SWITCH_TOGGLE)` and OFF light `(A:APU GENERATOR SWITCH:#ID#, Bool) !`; EXT PWR AVAIL light `(L:A32NX_EXT_PWR_AVAIL:#ID#, Bool) (L:A32NX_OVHD_ELEC_EXT_PWR_PB_IS_ON, Bool) ! and` (lit only while EXT PWR is off) |
| FBW-MISC | `fbw-a32nx/src/behavior/src/A32NX_Interior_Misc.xml`, https://raw.githubusercontent.com/flybywiresim/aircraft/master/fbw-a32nx/src/behavior/src/A32NX_Interior_Misc.xml (master): fuel pump click `#ID# (>K:FUELSYSTEM_PUMP_TOGGLE)` and OFF light `(A:FUELSYSTEM PUMP SWITCH:#ID#, Enum) 0 ==`; jet pump and crossfeed click `#ID# (>K:FUELSYSTEM_VALVE_TOGGLE)`, `(A:FUELSYSTEM VALVE SWITCH:#ID#, ...)`, crossfeed OPEN light `(A:FUELSYSTEM VALVE OPEN:#ID#, Bool)`; APU BLEED and engine bleed `TOGGLE_SIMVAR`; WING and ENG anti-ice and PROBE/WINDOW HEAT click code |
| FBW-GEN | `fbw-a32nx/src/behavior/src/A32NX_Interior_Generics.xml`, https://raw.githubusercontent.com/flybywiresim/aircraft/master/fbw-a32nx/src/behavior/src/A32NX_Interior_Generics.xml (master): `FBW_Push_Toggle` click `(#TOGGLE_SIMVAR#, Bool) ! (>#TOGGLE_SIMVAR#)` (the cockpit itself writes the L-Var); the ANN LT TEST term in the pushbutton lights |
| FBW-ADIRS | `fbw-a32nx/src/behavior/src/A32NX_Interior_ADIRS.xml`, https://raw.githubusercontent.com/flybywiresim/aircraft/master/fbw-a32nx/src/behavior/src/A32NX_Interior_ADIRS.xml (master): `<KNOB_POSITION_VAR>A32NX_OVHD_ADIRS_IR_#ID#_MODE_SELECTOR_KNOB</KNOB_POSITION_VAR>` (the knob's position is that L-Var) |
| FBW-IE | as phase4-a32nx.md (`fbw-a32nx/docs/a32nx-input-events.md`, master): input events only for the ECAM control panel and NAV & LOGO |
| FBW-REL | as phase4-a32nx.md (https://docs.flybywiresim.com/release-notes/a32nx/v2024010/) |
| SDK-ELECE | MSFS 2024 SDK, Aircraft Electrical Events, https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-electrical-events/: `TOGGLE_ALTERNATOR1` / `TOGGLE_ALTERNATOR2` ("Toggles alternator/generator 1/2/3/4 switch."), `APU_GENERATOR_SWITCH_TOGGLE` ("[0]: Generator switch index (1-4)"); and P4-1's rows |
| SDK-FUELE | MSFS 2024 SDK, Aircraft Fuel System Events, https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-fuel-system-events/: `FUELSYSTEM_PUMP_TOGGLE` ("Toggle a fuel pump on/off."), `FUELSYSTEM_VALVE_TOGGLE` ("Toggle a valve open/closed."), `FUELSYSTEM_JUNCTION_SET` ("[0]: Junction Index[1]: Option index") |
| README | PilotsDeck README, https://github.com/Fragtality/PilotsDeck/blob/master/README.md: 2.1.1 (address forms), 2.1.2 (toggle between On and Off Value), 2.2.2 (Format "Syntax: `Zeros.Fraction:Text %s Text`"), 3.5.1 (`SimVar`, `SimRead`, `SimCalculator` "Run Calculator Code in the Sim.", `SimCommand` example `SimCommand("K:APU_GENERATOR_SWITCH_TOGGLE:1")`) |
| PD-PI | The installed plugin's settings panel, `Plugin\PI\js\pi-Common.js`: line 181 (an L-Var name may end in `:<digits>`, so `L:A32NX_EXT_PWR_AVAIL:1` is a valid address), 189 (A-Var form with an index), 195 (K-Var with up to five parameters, or a sequence) |
| PD-SRC | PilotsDeck source, https://github.com/Fragtality/PilotsDeck (tree `11bdf1f`), read 2026-11-14: `Plugin/Resources/Scripts/ManagedScript.cs` (lines 98, 393-402: Lua `SimCalculator` -> a CALCULATOR command), `Plugin/Simulator/SimController.cs` (lines 18, 274, 303: the command channel to the connector), `Plugin/Simulator/ConnectorMSFS.cs` (lines 6, 57, 369-370, 551-569: CALCULATOR -> `MobiModule.ExecuteCode`) |
| CFIT-SRC | CFIT.SimConnectLib, the library of PilotsDeck's `MobiModule`: https://github.com/Fragtality/CFIT (commit `8c06162cdac66c08389d097bbc22615474529b92`), read 2026-11-14: `SimConnectLib/Modules/MobiFlight/MobiModule.cs` (`ExecuteCode` sends `MF.SimVars.Set.<code>` with `SendClientWasmCmd`, with no check that the module is connected; the client registers with `MF.Clients.Add.<name>`); the MobiFlight WASM module README, https://github.com/MobiFlight/MobiFlight-WASM-Module (branch main): `MF.Clients.Add.MyClientName` creates the client's channels, example `MF.SimVars.Set.5 (>L:MyVar)` |
