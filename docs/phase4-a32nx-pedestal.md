# Phase 4: A32NX pedestal page (ECAM control panel, speed brake, gear, engines)

**Status: generated, not yet sim-tested.** The page is in the generated profile `MSFS2024 A32NX`, but nothing
on it has been tried in the app or the sim yet, and the A32NX is not yet installed on this PC (see "Install
status"). Every name below is recorded as "Unverified" in [aircraft-mappings.md](aircraft-mappings.md)
("FlyByWire A32NX pedestal page (P4-6)") until the checks in
[tests/manual-checklist.md](../tests/manual-checklist.md), section "Phase 4: A32NX pedestal page (P4-6)",
pass.

Goal: the pedestal and the ECAM controls on one page, **ped**, opened from the EFIS page by the folder key
`PED` at **efis 3,6**. It holds the **ECAM control panel** (the eleven system page keys, CLR and STS lit from
their own lamps; ALL, RCL and T.O CONFIG, which have no lamp), the **speed brake** lever, **GND SPLR**,
**FLAPS** and **PARK** (the same keys as on the main page), the **gear lever** and the **LDG GEAR** lights,
the **autobrake** state, the **ENG 1** and **ENG 2** master switches and the **ENG MODE** selector, **rudder
trim** (left, right, the trim readout with its reset), **A/SKID & N/W STRG** (readout) and the **brake
pressure** needles. Every key lights or reads from the aircraft; no key assumes its press worked.

The page is part of the profile `MSFS2024 A32NX` (same file, same name, same import as the main page: see
[phase4-a32nx.md](phase4-a32nx.md), "Import the profile"), and its SPD BRK, LDG GEAR, A/BRK, ENG MODE, RUD
TRIM and BRK PSI keys use the same Lua script `XL24-A32NX.lua`, which must be installed again (P4-6 added six
functions). The key table below is the reference for what each key holds; `tools/profilegen/check.py
tools/profilegen/a32nx.json` compares the profile with "Key table: ped" key by key. No existing key moved or
changed; only efis 3,6, empty before, became the folder key.

Nothing on this page uses keyboard bindings, vJoy or anything tied to a controller: the keys send the
cockpit's own H-events (through the MobiFlight WASM module, see "The MobiFlight WASM module"), standard
SimConnect events, write an L-Var or run the Lua script, and read L-Vars and SimVars, so they work the same
with the Xbox Elite controller and the T.16000M + TWCS.

## Install status

- **The A32NX is not installed on this PC yet** (checked 2026-11-16, read only, as for P4-1 to P4-4): the
  MSFS 2024 package folders hold no FlyByWire package, and PilotsDeck has never seen an A32NX flight (its
  `InputEvents.txt` is not in the plugin folder now, no `A32NX` L-Var in its `L-Vars.txt`, no A32NX aircraft
  line in its newest log).
- FlyByWire's MSFS 2024 support is as in [phase4-a32nx.md](phase4-a32nx.md), "Install status" (Stable
  v2024.1.0, "officially compatible with MSFS 2024", FBW-REL). FlyByWire's input events cover the ECAM
  control panel (FBW-IE), but PilotsDeck reaches only the `_Set` input events over SimConnect (README 2.1.1
  BVAR), and FlyByWire marks the ECP keys' `_Set` "meaningless": the ECAM keys use the H-events the cockpit's
  own buttons send (ASSUMPTION A-5).
- The FlyByWire sources are read at the tag **v2024.1.0** (the MSFS 2024 Stable release). Where FlyByWire's
  documents differ from the cockpit's code (the Flight Deck API's older `A32NX_BTN_*` ECAM L-Vars, the
  autobrake values), the code wins.

## Where the page sits

**ped** is a second-level page, opened by the folder key `PED` at **efis 3,6** (the EFIS page is opened by
main 4,8). Its back key (1,1) returns to the EFIS page, so the page is two back presses from the main page
(the most [navigation.md](navigation.md) allows; the page holds no folder key). The main page has no free
position, and efis 3,6 and 3,7 were reserved for a later unit; row 3 of the EFIS page already holds RADIO
and XPDR, two other pedestal panels. How the pages connect: [navigation.md](navigation.md), "MSFS2024 A32NX
pages".

## Layout: ped

Positions are **row,column**, 1-based, row 1 at the top. Rows 1 and 2 hold the ECAM control panel in the
panel's own order, row 3 the speed brake, flaps, park brake, gear and autobrake, row 4 the engines, the
rudder trim, A/SKID and the brake pressure.

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | ENG | BLEED | PRESS | ELEC | HYD | FUEL | TO CONF |
| **Row 2** | CLR | APU | COND | DOOR | WHEEL | F/CTL | ALL | STS |
| **Row 3** | RCL | SPD BRK | GND SPLR | FLAPS | PARK | GEAR | LDG GEAR | A/BRK |
| **Row 4** | ENG 1 | ENG 2 | ENG MODE | RUD L | RUD TRIM | RUD R | A/SKID | BRK PSI |

31 keys and the back key, no empty position. 28 keys are new functions; GND SPLR, FLAPS and PARK repeat the
main page's keys 3,5, 3,4 and 3,3 with the same settings (ASSUMPTION A-3), so the pedestal controls are on
one page.

## Key table: ped

Action names are the PilotsDeck README's: **Dynamic Button**, **Display Value**, **Simple Button**. **Back**
= the Stream Deck app's back key (`backtoparent`), added by the generator. The kinds K1 to K10 and T3 are
explained in [phase4-a32nx.md](phase4-a32nx.md), "What each key holds", K12 to K14 in
[phase4-a32nx-radios.md](phase4-a32nx-radios.md), "What each key holds", K16 under "What each key holds"
below; source tags under "Sources" below. Command types: `H:` = H-Var (saved as 8; here a sequence of two),
`K:` = K-Var (16), `L:` = L-Var (3; the key writes its On or Off value), `lua:` = Lua Function (14).

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to the EFIS page | none | Back key |
| 1,2 | `ENG` | Dynamic Button | K13 | `H:A32NX_ECP_ENG_PRESSED:A32NX_ECP_ENG_RELEASED` [FBW-ECP-XML, FBW-ECP-TS] | `L:A32NX_ECP_LIGHT_ENG` [FBW-ECP-TS, FBW-ECP-XML] | On/Off image |
| 1,3 | `BLEED` | Dynamic Button | K13 | `H:A32NX_ECP_BLEED_PRESSED:A32NX_ECP_BLEED_RELEASED` [FBW-ECP-XML, FBW-ECP-TS] | `L:A32NX_ECP_LIGHT_BLEED` [FBW-ECP-TS, FBW-ECP-XML] | On/Off image |
| 1,4 | `PRESS` | Dynamic Button | K13 | `H:A32NX_ECP_PRESS_PRESSED:A32NX_ECP_PRESS_RELEASED` [FBW-ECP-XML, FBW-ECP-TS] | `L:A32NX_ECP_LIGHT_PRESS` [FBW-ECP-TS, FBW-ECP-XML] | On/Off image |
| 1,5 | `ELEC` | Dynamic Button | K13 | `H:A32NX_ECP_ELEC_PRESSED:A32NX_ECP_ELEC_RELEASED` [FBW-ECP-XML, FBW-ECP-TS] | `L:A32NX_ECP_LIGHT_ELEC` [FBW-ECP-TS, FBW-ECP-XML] | On/Off image |
| 1,6 | `HYD` | Dynamic Button | K13 | `H:A32NX_ECP_HYD_PRESSED:A32NX_ECP_HYD_RELEASED` [FBW-ECP-XML, FBW-ECP-TS] | `L:A32NX_ECP_LIGHT_HYD` [FBW-ECP-TS, FBW-ECP-XML] | On/Off image |
| 1,7 | `FUEL` | Dynamic Button | K13 | `H:A32NX_ECP_FUEL_PRESSED:A32NX_ECP_FUEL_RELEASED` [FBW-ECP-XML, FBW-ECP-TS] | `L:A32NX_ECP_LIGHT_FUEL` [FBW-ECP-TS, FBW-ECP-XML] | On/Off image |
| 1,8 | `TO CONF` | Simple Button | K12 | `H:A32NX_ECP_TO_CONF_TEST_PRESSED:A32NX_ECP_TO_CONF_TEST_RELEASED` [FBW-ECP-XML, FBW-ECP-TS] | none (no lamp; the E/WD shows the result) | fixed image |
| 2,1 | `CLR` | Dynamic Button | K13 | `H:A32NX_ECP_CLR_1_PRESSED:A32NX_ECP_CLR_1_RELEASED` [FBW-ECP-XML, FBW-ECP-TS] | `L:A32NX_ECP_LIGHT_CLR_1` [FBW-ECP-TS, FBW-ECP-XML] | On/Off image |
| 2,2 | `APU` | Dynamic Button | K13 | `H:A32NX_ECP_APU_PRESSED:A32NX_ECP_APU_RELEASED` [FBW-ECP-XML, FBW-ECP-TS] | `L:A32NX_ECP_LIGHT_APU` [FBW-ECP-TS, FBW-ECP-XML] | On/Off image |
| 2,3 | `COND` | Dynamic Button | K13 | `H:A32NX_ECP_COND_PRESSED:A32NX_ECP_COND_RELEASED` [FBW-ECP-XML, FBW-ECP-TS] | `L:A32NX_ECP_LIGHT_COND` [FBW-ECP-TS, FBW-ECP-XML] | On/Off image |
| 2,4 | `DOOR` | Dynamic Button | K13 | `H:A32NX_ECP_DOOR_PRESSED:A32NX_ECP_DOOR_RELEASED` [FBW-ECP-XML, FBW-ECP-TS] | `L:A32NX_ECP_LIGHT_DOOR` [FBW-ECP-TS, FBW-ECP-XML] | On/Off image |
| 2,5 | `WHEEL` | Dynamic Button | K13 | `H:A32NX_ECP_BRAKES_PRESSED:A32NX_ECP_BRAKES_RELEASED` [FBW-ECP-XML, FBW-ECP-TS] | `L:A32NX_ECP_LIGHT_BRAKES` [FBW-ECP-TS, FBW-ECP-XML] | On/Off image |
| 2,6 | `F/CTL` | Dynamic Button | K13 | `H:A32NX_ECP_FLT_CTL_PRESSED:A32NX_ECP_FLT_CTL_RELEASED` [FBW-ECP-XML, FBW-ECP-TS] | `L:A32NX_ECP_LIGHT_FLT_CTL` [FBW-ECP-TS, FBW-ECP-XML] | On/Off image |
| 2,7 | `ALL` | Simple Button | K12 | `H:A32NX_ECP_ALL_PRESSED:A32NX_ECP_ALL_RELEASED` [FBW-ECP-XML, FBW-ECP-TS] | none (no lamp; the SD shows the page) | fixed image |
| 2,8 | `STS` | Dynamic Button | K13 | `H:A32NX_ECP_STS_PRESSED:A32NX_ECP_STS_RELEASED` [FBW-ECP-XML, FBW-ECP-TS] | `L:A32NX_ECP_LIGHT_STS` [FBW-ECP-TS, FBW-ECP-XML] | On/Off image |
| 3,1 | `RCL` | Simple Button | K12 | `H:A32NX_ECP_RCL_PRESSED:A32NX_ECP_RCL_RELEASED` [FBW-ECP-XML, FBW-ECP-TS] | none (no lamp; the E/WD shows the result) | fixed image |
| 3,2 | `SPD BRK` | Display Value | K3 | Main `K:SPOILERS_TOGGLE`, Second (long press) `K:SPOILERS_SET:8192` [FBW-SCI, FBW-SPLR] | `lua:XL24-A32NX:SPDBRK` (the script) [README 2.1.1 LUAFUNC; FBW-SIMVARS, FBW-SPLR] | Lua text: RET, ARM, 50%, FULL |
| 3,3 | `GND SPLR` | Dynamic Button | K1 | `K:SPOILERS_ARM_TOGGLE` [FBW-API] | `L:A32NX_SPOILERS_ARMED` [FBW-API, FBW-SIMVARS] | On/Off image |
| 3,4 | `FLAPS` | Display Value | T3 (FLAPS form) | Main `K:FLAPS_INCR`, Second (long press) `K:FLAPS_DECR` [FBW-API] | `L:A32NX_FLAPS_HANDLE_INDEX` [FBW-API, FBW-SIMVARS] | Mappings `0=UP:1=1:2=2:3=3:4=FULL` |
| 3,5 | `PARK` | Dynamic Button | K2 | `L:A32NX_PARK_BRAKE_LEVER_POS`, On `1` / Off `0` [FBW-API] | `L:A32NX_PARK_BRAKE_LEVER_POS` [FBW-API, FBW-SIMVARS] | On/Off image, Special State |
| 3,6 | `GEAR` | Display Value | T3 (FLAPS form) | Main `K:GEAR_DOWN`, Second (long press) `K:GEAR_UP` [FBW-HANDLING, FBW-GEAR-RS] | `L:A32NX_GEAR_HANDLE_POSITION` [FBW-SIMVARS, FBW-HANDLING] | Mappings `0=UP:1=DOWN` |
| 3,7 | `LDG GEAR` | Display Value | K14 | none | `lua:XL24-A32NX:GEARIND` (the script) [README 2.1.1 LUAFUNC; FBW-SIMVARS, FBW-MISC] | Lua text: 3 GRN, UNLK, UP |
| 3,8 | `A/BRK` | Display Value | K14 | none | `lua:XL24-A32NX:ABRK` (the script) [README 2.1.1 LUAFUNC; FBW-SIMVARS, FBW-API] | Lua text: OFF, LO, MED, MAX, DECEL |
| 4,1 | `ENG 1` | Dynamic Button | K16 | Main `K:FUELSYSTEM_VALVE_OPEN:1` (ON), Second (long press) `K:FUELSYSTEM_VALVE_CLOSE:1` (OFF) [FBW-MISC, FBW-API] | `(A:FUELSYSTEM VALVE SWITCH:1, Bool)` [FBW-MISC, FBW-API] | On/Off image |
| 4,2 | `ENG 2` | Dynamic Button | K16 | Main `K:FUELSYSTEM_VALVE_OPEN:2` (ON), Second (long press) `K:FUELSYSTEM_VALVE_CLOSE:2` (OFF) [FBW-MISC, FBW-API] | `(A:FUELSYSTEM VALVE SWITCH:2, Bool)` [FBW-MISC, FBW-API] | On/Off image |
| 4,3 | `ENG MODE` | Display Value | K7 | Main `lua:XL24-A32NX:ENGMODE(1)` (one position clockwise), Second (long press) `lua:XL24-A32NX:ENGMODE(-1)` (the script runs the selector's own code) [README 2.1.1 LUAFUNC, 3.5.1; FBW-AIRBUS] | `L:XMLVAR_ENG_MODE_SEL` [FBW-AIRBUS] | Mappings `0=CRANK:1=NORM:2=IGN` |
| 4,4 | `RUD L` | Simple Button | K6 | `K:RUDDER_TRIM_LEFT` [FBW-HANDLING, FBW-SCI] | none (RUD TRIM at 4,5 shows the result) | fixed image |
| 4,5 | `RUD TRIM` | Display Value | K3 | `K:RUDDER_TRIM_RESET` [FBW-HANDLING, FBW-API] | `lua:XL24-A32NX:RUDTRIM` (the script) [README 2.1.1 LUAFUNC; FBW-SIMVARS, FBW-RTPI, FBW-FBI] | Lua text: L 2.5, R 1.0, 0.0 |
| 4,6 | `RUD R` | Simple Button | K6 | `K:RUDDER_TRIM_RIGHT` [FBW-HANDLING, FBW-SCI] | none (RUD TRIM at 4,5 shows the result) | fixed image |
| 4,7 | `A/SKID` | Display Value | K9 | none (readout only, A-4) | `(A:ANTISKID BRAKES ACTIVE, Bool)` [FBW-HANDLING, FBW-API] | Mappings `0=OFF:1=ON` |
| 4,8 | `BRK PSI` | Display Value | K14 | none | `lua:XL24-A32NX:BRKPSI` (the script) [README 2.1.1 LUAFUNC; FBW-INTERIOR-BRK] | Lua text: left and right brake pressure, in 1000 psi |

## What the keys do

ECAM control panel:
- **ENG, BLEED, PRESS, ELEC, HYD, FUEL, APU, COND, DOOR, WHEEL, F/CTL** press the panel's system page key:
  the key sends the cockpit button's own pair of H-events, pressed then released (FBW-ECP-XML), and the
  System Display shows that page. A page key is lit while the SD shows its page (FlyByWire's display
  management sets the lamp from the page it shows, FBW-ECP-TS). What a second press of a lit key does is the
  aircraft's own logic (not read in the source; the test records it).
- **CLR** is lit while there is something to clear (FBW-ECP-TS: the lamp follows the warning computer's light
  word); a press clears the shown message. **STS** shows the STATUS page and is lit while it is shown.
- **ALL** steps the SD through its pages, **RCL** recalls the messages, **TO CONF** runs the T.O CONFIG test.
  The three have no lamp (`<NO_SEQ2/>` in FBW-ECP-XML): their keys show a fixed image and the E/WD or the SD
  shows the result.
- The pressed and released events go out one right after the other. FlyByWire's panel still holds a key
  pressed for its minimum hold time, about 281 ms (`MIN_HOLD_TIME_MS = 8.5 * 33`, FBW-ECP-TS), so a short
  press counts as a press.

Speed brake, flaps, park brake, gear:
- **SPD BRK** shows the speed brake lever: `RET` (retracted), `FULL`, a step in between as `50%`, and `ARM`
  while the ground spoilers are armed. A press sends `K:SPOILERS_TOGGLE`: the lever goes to RET if it is out,
  else to FULL; a long press (0.5 s or more) sends `K:SPOILERS_SET:8192`, the lever at 1/2 (8192 / 16384).
  Both disarm the ground spoilers (FBW-SPLR).
- **GND SPLR** arms and disarms the ground spoilers and is lit while they are armed; **FLAPS** steps the
  flaps lever (press one step down, long press one step up) and shows its position; **PARK** sets and
  releases the park brake and is lit while it is set. The three are the main page's keys 3,5, 3,4 and 3,3
  with the same settings (ASSUMPTION A-3): a press on either page moves the same lever.
- **GEAR** shows the gear lever as the aircraft has it (`UP`, `DOWN`; a value between 0 and 1 while it moves
  shows as a number). A press sends `K:GEAR_DOWN` (lever down); **only a long press** sends `K:GEAR_UP`
  (ASSUMPTION A-4). FlyByWire maps both events to its own lever request (FBW-GEAR-RS).
- **LDG GEAR** shows the LDG GEAR panel as landing gear computer 1 drives it: `3 GRN` (or `1 GRN`, `2 GRN`)
  counts the gears locked down, `UNLK` while any gear disagrees with the lever, `UP` when none is down;
  blank while the panel's bus (DC 2) is unpowered (FBW-MISC).
- **A/BRK** shows the armed autobrake mode (`OFF`, `LO`, `MED`, `MAX`) and `DECEL` while the DECEL light is
  on. The autobrake buttons stay on the main page (BRK LO, MED, MAX; ASSUMPTION A-3).

Engines, rudder trim, brakes:
- **ENG 1, ENG 2**: a press switches the engine master ON (`K:FUELSYSTEM_VALVE_OPEN`), **only a long press**
  switches it OFF (`K:FUELSYSTEM_VALVE_CLOSE`), as the cockpit switch's own code sends them (FBW-MISC;
  ASSUMPTION A-4). The key is lit while the sim's fuel valve switch reads on.
- **ENG MODE** moves the ENG MODE selector: a press one position clockwise (CRANK, NORM, IGN), a long press
  one position back; it stops at the ends. The script writes the selector's L-Var and runs the selector's own
  code (ASSUMPTION A-8). The key shows the position the aircraft reads.
- **RUD L, RUD R** move the rudder trim one step left or right; **RUD TRIM** shows the trim in degrees
  (`L 2.5`, `R 1.0`, `0.0`) and a press resets it to 0; blank while the trim display's bus (DC 2) is
  unpowered (FBW-RTPI).
- **A/SKID** shows the A/SKID & N/W STRG switch (`ON`, `OFF`); a press does nothing (ASSUMPTION A-4).
- **BRK PSI** shows the left and right needles of the triple brake indicator in thousands of psi (`2.0 2.0`
  is 2000 psi on each); blank while its bus (DC ESS) is unpowered (FBW-INTERIOR-BRK).

## Guarded keys

ASSUMPTION A-4. A key whose wrong press could hurt the flight sends that command only on a long press (0.5 s
or more) or not at all:

| Key | Short press | Long press | Why |
|---|---|---|---|
| GEAR | lever down | lever up | gear up on the ground; never long-press GEAR on the ground (ASSUMPTION A-13) |
| ENG 1, ENG 2 | master ON | master OFF | an engine shut down by a stray press |
| A/SKID | nothing (readout) | nothing | a press would switch off anti-skid and nose wheel steering |
| EMER CANC | not on the page | | it cancels a warning's aural for the rest of the flight |

The ECAM keys, SPD BRK, the rudder trim keys, ENG MODE, GND SPLR, FLAPS and PARK are plain, as their cockpit
controls (PARK as on the main page, P4-1).

## What each key holds

The kinds of [phase4-a32nx.md](phase4-a32nx.md), "What each key holds": every key is a copy of a real saved
key with only the listed fields changed (the generator does this). On this page: K1 (GND SPLR), K2 (PARK), K3
(SPD BRK, RUD TRIM), K6 (RUD L, RUD R), K7 (ENG MODE), K9 (A/SKID), T3 (FLAPS, GEAR), K12 (TO CONF, ALL, RCL),
K13 (the 13 lit ECAM keys), K14 (LDG GEAR, A/BRK, BRK PSI; K12 to K14 in
[phase4-a32nx-radios.md](phase4-a32nx-radios.md)) and one new kind:

| Kind | Action, copied from | Fields set |
|---|---|---|
| K16 K-event button with long press | Dynamic Button, the Phase 1 AP key (`p1:3,0`, T2), as K1 | Command Address (`K:`, the template's command type K-Var), Value Address; long press on, Second Command Type K-Var (`ActionTypeLong` 16), Second Command Address (`K:`) |

The K12 and K13 keys here send an H-Var **sequence**: README 2.1.1, "You can activate multiple H-Vars in a
Sequence if you separate them with a `:` Sign." (its example names the second H-Var without `H:`), so
`H:A32NX_ECP_ENG_PRESSED:A32NX_ECP_ENG_RELEASED` sends the pressed event, then the released one. The long
press fields (README 2.1, Second command) are in the saved Phase 1 AP key and already set on the Display Value
keys BARO and FLAPS (ASSUMPTION A-13). An A-Var is read as `(A:Name:Index, Unit)` (README 2.1.1). The data
file is `tools/profilegen/a32nx.json`, page `ped` (`"parent": "efis"`, `"spec":
"docs/phase4-a32nx-pedestal.md"`), and the efis key 3,6.

Title sizes ([navigation.md](navigation.md), "Rules"): Dynamic and Simple Buttons copied from the AP key draw
their titles at 14 (the ECAM keys, `TO CONF` included, ENG 1, ENG 2, RUD L, RUD R); GND SPLR keeps the main
page's 13; Display Values keep their template size (15).

## The script

[`pilotsdeck/MSFS2024-XL/_Package/Scripts/XL24-A32NX.lua`](../pilotsdeck/MSFS2024-XL/_Package/Scripts/XL24-A32NX.lua)
(the main page's script, [phase4-a32nx.md](phase4-a32nx.md), "The script"). P4-6 added six functions at the
end and one header comment line; nothing that was there changed. The fifteen new addresses are registered
with `SimVar(...)` at the top level of the file, as the others.

| Function | Returns (text) or does | Reads / writes |
|---|---|---|
| `SPDBRK()` | `ARM` while the ground spoilers are armed; else `RET` below 0.01, `FULL` above 0.99, otherwise the lever position as `50%` | reads `L:A32NX_SPOILERS_ARMED`, `L:A32NX_SPOILERS_HANDLE_POSITION` (0 retracted .. 1 full) |
| `GEARIND()` | `""` while DC 2 is unpowered; `UNLK` while any gear is unlocked; else `3 GRN` (the number of gears locked down), `UP` for none | reads `L:A32NX_ELEC_DC_2_BUS_IS_POWERED`, `L:A32NX_LGCIU_1_NOSE_GEAR_DOWNLOCKED`, `_LEFT_`, `_RIGHT_`, `L:A32NX_LGCIU_1_NOSE_GEAR_UNLOCKED`, `_LEFT_`, `_RIGHT_` |
| `ABRK()` | `DECEL` while the DECEL light is on; else `LO`, `MED`, `MAX` for the armed mode 1 to 3, `OFF` | reads `L:A32NX_AUTOBRAKES_DECEL_LIGHT`, `L:A32NX_AUTOBRAKES_ARMED_MODE` |
| `RUDTRIM()` | `""` while DC 2 is unpowered; else the trim in degrees: `0.0` below 0.05, else `L 2.5` or `R 1.0` | reads `L:A32NX_ELEC_DC_2_BUS_IS_POWERED`, `L:A32NX_HYD_RUDDER_TRIM_FEEDBACK_ANGLE` (degrees, negative = left) |
| `BRKPSI()` | `""` while DC ESS is unpowered; else the left and right pressure / 1000 as `2.0 2.0` | reads `L:A32NX_ELEC_DC_ESS_BUS_IS_POWERED`, `L:A32NX_HYD_BRAKE_ALTN_LEFT_PRESS`, `L:A32NX_HYD_BRAKE_ALTN_RIGHT_PRESS` (psi) |
| `ENGMODE(step)` | nothing unless `L:A32NX_TOTAL_FUEL_QUANTITY` reads more than 0 (the A32NX check of `FUELMODE`); reads the selector, adds `step` (1 or -1), keeps it in 0..2, writes it and runs the selector's code for that position by `SimCalculator` | reads and writes `L:XMLVAR_ENG_MODE_SEL` (0 CRANK, 1 NORM, 2 IGN); sends the code below |

The ENG MODE selector's code, as FlyByWire's knob runs it for each position (FBW-AIRBUS,
`A32NX_ENGINE_MODE_SELECTOR_TEMPLATE`), in the script's own function `eng_mode_code`:
- 2 (IGN): `2 (>K:TURBINE_IGNITION_SWITCH_SET1) 2 (>K:TURBINE_IGNITION_SWITCH_SET2)`, then
  `(>H:A320_Neo_EICAS_2_Ignition_Start)` (one string)
- 1 (NORM): `1 (>K:TURBINE_IGNITION_SWITCH_SET1) 1 (>K:TURBINE_IGNITION_SWITCH_SET2)`
- 0 (CRANK): `0 (>K:TURBINE_IGNITION_SWITCH_SET)`

- The readouts follow FlyByWire's own panels: LDG GEAR the panel's template (landing gear computer 1, DC 2,
  FBW-MISC), BRK PSI the indicator's needles (value / 1000, DC ESS, FBW-INTERIOR-BRK), RUD TRIM the rudder
  trim display (DC 2, FBW-RTPI). That display shows the flight augmentation computer's copy of the trim
  unit's feedback angle `L:A32NX_HYD_RUDDER_TRIM_FEEDBACK_ANGLE` (degrees, FBW-SIMVARS); the computer takes
  the angle with its sign turned (FBW-FBI) and the display writes `L` for a value of 0 or more, so a
  negative angle is left. The Flight Deck API's `RUDDER TRIM PCT` row (FBW-API) is not used: FlyByWire
  takes the trim events itself, and its code at v2024.1.0 does not write that SimVar (FBW-SCI, FBW-FBI).
- `BRKPSI` uses the DC ESS check the RADIO page added (`RMP_POWER`, the same L-Var); `ENGMODE` uses the fuel
  L-Var `FUELMODE` added (`FUEL_TOTAL`). In another aircraft the fuel L-Var reads 0, so ENG MODE does nothing.

## The MobiFlight WASM module

Every `H:` command on this page (the 16 ECAM keys) and the calculator code of ENG MODE (`SimCalculator`) go
through the MobiFlight WASM module: "PilotsDeck sends every H-event and all calculator code through the
MobiFlight WASM module" ([troubleshooting.md](troubleshooting.md#the-mobiflight-wasm-module)). It is installed
on this PC ([installation.md](installation.md), "MobiFlight WASM module (which keys need it)"; that section
and troubleshooting.md do not list this page's keys yet, ASSUMPTION A-17). Without it the 16 ECAM keys do
nothing, most likely with no alert sign on the key, and ENG MODE writes the selector's L-Var but its code does
not run. The K-event keys, PARK (an L-Var write) and every read do not need the module.

## What the keys show when the A32NX isn't there

- No sim, or no flight: PilotsDeck's own idle and waiting images, as on the other pages.
- Another aircraft: the ECAM keys dark (their lamp L-Vars read 0), A/BRK `OFF`, SPD BRK `RET`, GEAR `UP`,
  LDG GEAR and RUD TRIM blank (the DC 2 L-Var reads 0), BRK PSI blank, ENG MODE `CRANK`, FLAPS `UP`, PARK
  and GND SPLR off. That is the 0 of a missing L-Var, not the aircraft's state.
- The A32NX not powered: the ECAM keys dark, LDG GEAR, RUD TRIM and BRK PSI blank (their buses are off);
  the other keys show what their variables read.
- ENG 1, ENG 2 and A/SKID read standard SimVars, so they show the other aircraft's own values.
- **The standard events act on any aircraft:** GEAR, ENG 1, ENG 2, RUD L, RUD R, the RUD TRIM reset, SPD BRK,
  FLAPS and GND SPLR move the loaded aircraft's own controls where it has them. Keep the profile on the A32NX
  with the Profile Manager's aircraft mapping, and do not press those keys in another aircraft.
- The ECAM H-events have no listener in other aircraft; ENG MODE does nothing (the A32NX fuel L-Var reads 0).
- A command the sim refuses shows PilotsDeck's alert sign on the key.

## Not on this page

- **EMER CANC**: it cancels a warning's aural for the rest of the flight (ASSUMPTION A-4).
- **CLR 2**: the First Officer's copy of CLR.
- **The autobrake buttons** BRK LO, MED, MAX: on the main page (A/BRK here shows the armed mode).
- **ACCU** pressure and **BRK FAN**: no room; a second page would be ASSUMPTION A-2.
- **Elevator trim** and the ECAM panel's DIM knobs: not part of this page's controls.

## Fallbacks

Use one only if the checklist shows the main route does not work, and say which one you used. None is tested.
A key that fails with no working fallback becomes readout-only (command none) or Empty, and its row in
aircraft-mappings.md says "does not work".

| Key | If it fails | Fallback | Source |
|---|---|---|---|
| Any ECAM key (A-5) | The press does nothing (check first: the MobiFlight WASM module is installed and the plugin log shows "MobiFlight WASM Client Connection opened"; the plugin log shows the command) | (1) Use Delay on (`UseControlDelay`: 25 ms between the two events, README 2.1.2); (2) a Lua function `ECP(name)` that sends `(>H:A32NX_ECP_<N>_PRESSED)`, waits 100 ms (`Sleep`) and sends `_RELEASED` by `SimCalculator` (command type Lua Function); not built | README 2.1.2, 3.5.1; FBW-ECP-TS |
| ECAM keys look (A-16) | With ANN LT on DIM a lit key shows no image (the lamp reads 0.1, neither On `1` nor Off `0`) | A Lua function returning 1 or 0 as the key's read (a later change) | FBW-OVHD-DISC |
| ENG MODE (A-8) | The selector does not follow the L-Var write, or the ignition does not follow | ENG MODE becomes a readout (command none), same read | FBW-AIRBUS, FBW-API |
| ENG 1, ENG 2 (A-13) | The long press does not send the OFF command | The T3 form, as GEAR: a Display Value with the same commands and read, Mappings `0=OFF:1=ON`; else readout only | README 2.1 |
| SPD BRK (A-13) | The long press does not put the lever at 1/2 | Record the lever position; the parameter of `K:SPOILERS_SET` is the only change | FBW-SPLR, PD-SRC |
| GEAR, ENG 1, ENG 2 (A-4) | A stronger guard is wanted | Readout only (command none) | |
| RUD TRIM | The readout does not follow the cockpit's rudder trim display | `RUDTRIM` reads `(A:RUDDER TRIM PCT, Percent over 100)` x 20 (the Flight Deck API's row) | FBW-API |

## How to test

Run [tests/manual-checklist.md](../tests/manual-checklist.md), section "Phase 4: A32NX pedestal page (P4-6)",
after the P4-1 section's "Before you start" and "Import" steps. As on the other pages, check both directions:
press a key and watch the cockpit, then **work the control in the cockpit with the mouse and check that the
key follows without a key being pressed.** Never long-press GEAR on the ground. Record what a second press of
a lit ECAM key does, what ALL does per press, the lit ECAM keys with ANN LT on DIM, the brake pressures, the
ENG MODE result and the rudder trim step.

## When it passes

1. Any change found in the test goes into `tools/profilegen/a32nx.json`, the script and this doc; then the
   profile is regenerated (not exported from the app) and imported again, and the script installed again.
2. Fill in the "Verified" column of the rows in aircraft-mappings.md ("FlyByWire A32NX pedestal page (P4-6)")
   with the date, sim version and A32NX version, for each function that passed; mark a row "does not work"
   where a key failed.

## Sources

FlyByWire sources: the flybywiresim/aircraft repository at the tag v2024.1.0 (the MSFS 2024 Stable release),
`https://raw.githubusercontent.com/flybywiresim/aircraft/v2024.1.0/<path>`, and FlyByWire's docs site, read
2026-11-16. The tags FBW-REL, FBW-EVENTS and PD-SRC are the ones of [phase4-a32nx.md](phase4-a32nx.md),
"Sources".

| Tag | Source |
|---|---|
| FBW-ECP-XML | `fbw-a32nx/src/base/flybywire-aircraft-a320-neo/ModelBehaviorDefs/A32NX/Interior/Pedestal/A32NX_ECP.xml`, https://raw.githubusercontent.com/flybywiresim/aircraft/v2024.1.0/fbw-a32nx/src/base/flybywire-aircraft-a320-neo/ModelBehaviorDefs/A32NX/Interior/Pedestal/A32NX_ECP.xml: each ECAM button's H-event `A32NX_ECP_#BUTTON_NAME#`, sent as `_PRESSED` on press and `_RELEASED` on release, and its lamp `(L:A32NX_ECP_LIGHT_#BUTTON_NAME#)`; the button names (CLR_1, STS, RCL, TO_CONF_TEST, ENG, BLEED, APU, HYD, ELEC, COND, PRESS, FUEL, FLT_CTL, DOOR, BRAKES, ALL); RCL, TO_CONF_TEST and ALL have no lamp (`<NO_SEQ2/>`) |
| FBW-ECP-TS | `fbw-a32nx/src/systems/systems-host/systems/ECP/Ecp.ts`, https://raw.githubusercontent.com/flybywiresim/aircraft/v2024.1.0/fbw-a32nx/src/systems/systems-host/systems/ECP/Ecp.ts: the panel takes the H-events `/^A32NX_ECP_([\w\d_]+)_(PRESSED\|RELEASED)$/`, holds a key at least `MIN_HOLD_TIME_MS = 8.5 * 33`, and writes each lamp `L:A32NX_ECP_LIGHT_${this.name}` (bright, dim or 0) from the page request and the warning computer's light word; DC ESS bus |
| FBW-OVHD-DISC | `fbw-a32nx/src/systems/shared/src/publishers/A32NXOverheadDiscretePublisher.ts`, https://raw.githubusercontent.com/flybywiresim/aircraft/v2024.1.0/fbw-a32nx/src/systems/shared/src/publishers/A32NXOverheadDiscretePublisher.ts: `ANN_LIGHT_BRIGHT_BRIGHTNESS = 1`, `ANN_LIGHT_DIM_BRIGHTNESS = 0.1` |
| FBW-ECP-PR | FlyByWire pull request #9840 "feat(a32nx): ecam control panel (ecp)", file list https://api.github.com/repos/flybywiresim/aircraft/pulls/9840/files (lead): FlyByWire's own procedure presses T.O CONFIG by `(>H:A32NX_ECP_TO_CONF_TEST_PRESSED)` |
| FBW-HANDLING | `fbw-a32nx/src/behavior/src/A32NX_Interior_Handling.xml`, https://raw.githubusercontent.com/flybywiresim/aircraft/v2024.1.0/fbw-a32nx/src/behavior/src/A32NX_Interior_Handling.xml: the flaps lever (`K:FLAPS_INCR`, `K:FLAPS_DECR`), the speed brake lever, the park brake lever (`K:PARKING_BRAKES`), the rudder trim knob (`K:RUDDER_TRIM_LEFT`, `K:RUDDER_TRIM_RIGHT`, reset `K:RUDDER_TRIM_RESET`, reads `A:RUDDER TRIM PCT`), the gear lever (`L:A32NX_GEAR_HANDLE_POSITION`, `K:GEAR_UP`, `K:GEAR_DOWN`, the lever lock `L:A32NX_GEAR_LEVER_LOCKED`), the A/SKID switch (`K:ANTISKID_BRAKES_TOGGLE`, `A:ANTISKID BRAKES ACTIVE`) |
| FBW-MISC | `fbw-a32nx/src/behavior/src/A32NX_Interior_Misc.xml`, https://raw.githubusercontent.com/flybywiresim/aircraft/v2024.1.0/fbw-a32nx/src/behavior/src/A32NX_Interior_Misc.xml: the engine master switch (`A:FUELSYSTEM VALVE SWITCH:#VALVE_ID#`, `K:FUELSYSTEM_VALVE_OPEN`, `K:FUELSYSTEM_VALVE_CLOSE`), the LDG GEAR lights (`L:A32NX_LGCIU_1_#GEAR_ID#_GEAR_UNLOCKED`, `_DOWNLOCKED`, `L:A32NX_ELEC_DC_2_BUS_IS_POWERED`) |
| FBW-AIRBUS | `fbw-a32nx/src/base/flybywire-aircraft-a320-neo/ModelBehaviorDefs/A32NX/Airbus.xml`, https://raw.githubusercontent.com/flybywiresim/aircraft/v2024.1.0/fbw-a32nx/src/base/flybywire-aircraft-a320-neo/ModelBehaviorDefs/A32NX/Airbus.xml: `A32NX_ENGINE_MODE_SELECTOR_TEMPLATE`, the knob position `XMLVAR_ENG_MODE_SEL` (type L) and the code for each position (`K:TURBINE_IGNITION_SWITCH_SET1`, `_SET2`, `_SET`, `H:A320_Neo_EICAS_2_Ignition_Start`) |
| FBW-GEAR-RS | `fbw-a32nx/src/wasm/systems/a320_systems_wasm/src/gear.rs`, https://raw.githubusercontent.com/flybywiresim/aircraft/v2024.1.0/fbw-a32nx/src/wasm/systems/a320_systems_wasm/src/gear.rs: `GEAR_UP` (0) and `GEAR_DOWN` (1) mapped to the lever request `GEAR_LEVER_POSITION_REQUEST`, masked |
| FBW-SPLR | `fbw-a32nx/src/wasm/fbw_a320/src/SpoilersHandler.cpp`, https://raw.githubusercontent.com/flybywiresim/aircraft/v2024.1.0/fbw-a32nx/src/wasm/fbw_a320/src/SpoilersHandler.cpp: the toggle ("handlePosition = handlePosition > 0 ? POSITION_RETRACTED : POSITION_FULL;"), the set ("fmin(1.0, fmax(0.0, value / 16384.0))"), the arm toggle ("isArmed = !isArmed;"); both lever commands disarm |
| FBW-SCI | `fbw-a32nx/src/wasm/fbw_a320/src/interface/SimConnectInterface.cpp`, https://raw.githubusercontent.com/flybywiresim/aircraft/v2024.1.0/fbw-a32nx/src/wasm/fbw_a320/src/interface/SimConnectInterface.cpp: FlyByWire takes `SPOILERS_TOGGLE`, `SPOILERS_SET`, `SPOILERS_ARM_TOGGLE`, `RUDDER_TRIM_LEFT`, `RUDDER_TRIM_RIGHT`, `RUDDER_TRIM_RESET` (`RUDDER_TRIM_SET` only logged) |
| FBW-FBI | `fbw-a32nx/src/wasm/fbw_a320/src/FlyByWireInterface.cpp`, https://raw.githubusercontent.com/flybywiresim/aircraft/v2024.1.0/fbw-a32nx/src/wasm/fbw_a320/src/FlyByWireInterface.cpp: the rudder trim switches and reset go to the flight augmentation computers (`rudder_trim_switch_left = trimInput.rudderTrimSwitchLeft`), which take the trim position with its sign turned (`rudder_trim_position_deg = -idRudderTrimPosition->get()`, from `A32NX_HYD_RUDDER_TRIM_FEEDBACK_ANGLE`) and give `A32NX_FAC_<n>_RUDDER_TRIM_POS`; no write of `RUDDER TRIM PCT` |
| FBW-RTPI | `fbw-a32nx/src/systems/instruments/src/RTPI/instrument.tsx`, https://raw.githubusercontent.com/flybywiresim/aircraft/v2024.1.0/fbw-a32nx/src/systems/instruments/src/RTPI/instrument.tsx: the rudder trim display reads `L:A32NX_FAC_1_RUDDER_TRIM_POS` (or FAC 2's), shows `L` for a value of 0 or more, else `R`, and the value to one decimal; blank without `L:A32NX_ELEC_DC_2_BUS_IS_POWERED` |
| FBW-INTERIOR | `fbw-a32nx/src/base/flybywire-aircraft-a320-neo/SimObjects/AirPlanes/FlyByWire_A320_NEO/model/A320_NEO_INTERIOR.xml`, https://raw.githubusercontent.com/flybywiresim/aircraft/v2024.1.0/fbw-a32nx/src/base/flybywire-aircraft-a320-neo/SimObjects/AirPlanes/FlyByWire_A320_NEO/model/A320_NEO_INTERIOR.xml: the engine masters (VALVE_ID 1 and 2), the ENG MODE knob, the rudder trim knob, the gear lever, the autobrake buttons and lights, the A/SKID switch, the ECAM control panel |
| FBW-INTERIOR-BRK | the same file, component `Airbus_BRK`: the brake needles `(L:A32NX_ELEC_DC_ESS_BUS_IS_POWERED, Bool) if{ (L:A32NX_HYD_BRAKE_ALTN_LEFT_PRESS, number) 1000 / }` and the right one, 0 to 3 (3000 psi) |
| FBW-SIMVARS | `fbw-a32nx/docs/a320-simvars.md`, https://raw.githubusercontent.com/flybywiresim/aircraft/v2024.1.0/fbw-a32nx/docs/a320-simvars.md: `A32NX_SPOILERS_ARMED`, `A32NX_SPOILERS_HANDLE_POSITION`, `A32NX_FLAPS_HANDLE_INDEX`, `A32NX_PARK_BRAKE_LEVER_POS`, `A32NX_AUTOBRAKES_ARMED_MODE` (0 to 3), `A32NX_AUTOBRAKES_DECEL_LIGHT`, `A32NX_LGCIU_{number}_{gear}_GEAR_DOWNLOCKED` / `_UNLOCKED`, `A32NX_GEAR_HANDLE_POSITION`, `A32NX_HYD_RUDDER_TRIM_FEEDBACK_ANGLE` (Degree, "Rudder trim unit position feedback"); the ECAM lamp L-Vars are not listed (code only) |
| FBW-IE | `fbw-a32nx/docs/a32nx-input-events.md`, https://raw.githubusercontent.com/flybywiresim/aircraft/v2024.1.0/fbw-a32nx/docs/a32nx-input-events.md: the ECAM input events `B:A32NX_PED_ECP_<NAME>_PB` (`_Push`, `_Release`; `_Set` "meaningless") |
| FBW-API | FlyByWire Flight Deck API, https://docs.flybywiresim.com/aircraft/a32nx/a32nx-api/a32nx-flightdeck-api/: ENG 1+2 MASTER (`FUELSYSTEM_VALVE_OPEN` "Activates the switch", `FUELSYSTEM_VALVE_CLOSE`, `FUELSYSTEM VALVE SWITCH:1`), ENG MODE (0 CRANK, 1 NORM, 2 IGN), the speed brake, GND SPOILER ARM, flaps, rudder trim (`RUDDER TRIM PCT`, -1.0 for 20 degrees left to 1.0 for 20 degrees right, not used: see "The script"; `RUDDER_TRIM_RESET`), gear, autobrake (`A32NX_AUTOBRAKES_DECEL_LIGHT`), A/SKID & N/W STRG (`ANTISKID BRAKES ACTIVE`), the older ECAM `A32NX_BTN_*` L-Vars |
| README | PilotsDeck README, https://github.com/Fragtality/PilotsDeck/blob/master/README.md: 2.1 (long press, Second command), 2.1.1 (HVAR `Name(:Parameter)(:Name(:Parameter))*` and the sequence sentence; KVAR; LVAR; AVAR `(A:Name:Index, Unit)`; BVAR, only the `_Set` input events over SimConnect; LUAFUNC), 2.1.2 (Use Delay), 3.5.1 (`SimVar`, `SimRead`, `SimWrite`, `SimCalculator`, `Sleep`) |
