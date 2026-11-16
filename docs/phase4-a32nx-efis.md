# Phase 4: A32NX EFIS page (EFIS control panel and glareshield, Captain side)

**Status: generated, not yet sim-tested.** The page is in the generated profile `MSFS2024 A32NX`, but nothing
on it has been tried in the app or the sim yet, and the A32NX is not yet installed on this PC (see "Install
status"). Every name below is recorded as "Unverified" in [aircraft-mappings.md](aircraft-mappings.md)
("FlyByWire A32NX EFIS page (P4-2)") until the checks in
[tests/manual-checklist.md](../tests/manual-checklist.md), section "Phase 4: A32NX EFIS page (P4-2)", pass.

Goal: the Captain's whole EFIS control panel and the glareshield lamps on one page: baro (value, QNH, STD,
hPa/inHg, + and -), FD, LS, ND mode and range, the five ND option buttons (CSTR, WPT, VOR.D, NDB, ARPT), both
ADF/VOR switches, CHRONO, the AUTOLAND lamp, MASTER WARN and MASTER CAUT. Every lamp and readout reads the
aircraft's own state; no key assumes its press worked.

The page is part of the profile `MSFS2024 A32NX` (same file, same name, same import as the main page: see
[phase4-a32nx.md](phase4-a32nx.md), "Import the profile"), and it uses the same Lua script `XL24-A32NX.lua`,
which must be copied into the plugin's Scripts folder again (P4-2 added four functions to it). The table
below is the reference for what each key holds; `tools/profilegen/check.py tools/profilegen/a32nx.json`
compares the profile with the "Key table: efis" section key by key.

Nothing on this page uses keyboard bindings, vJoy or anything tied to a controller: the keys send SimConnect
events (FlyByWire's `A32NX.*` custom events as K-Vars), run the Lua script (which writes L-Vars), or write
one L-Var, and read L-Vars, so they work the same with the Xbox Elite controller and the T.16000M + TWCS.

## Install status

- **The A32NX is not installed on this PC yet** (checked 2026-11-14, read only, as for P4-1): the MSFS 2024
  package folders hold no FlyByWire package, and PilotsDeck has never seen an A32NX flight (no
  `InputEvents.txt` for it, no `A32NX` L-Var in its `L-Vars.txt`, no A32NX line in its newest log).
- FlyByWire's MSFS 2024 support is as in [phase4-a32nx.md](phase4-a32nx.md), "Install status" (Stable
  v2024.1.0, "not yet a native 2024 package"). FlyByWire still lists input events only for the ECAM control
  panel and the NAV & LOGO switch (FBW-IE): nothing for the FCU, the EFIS control panel, the master lights or
  the chrono, so this page uses FlyByWire's L-Vars and custom events.
- The sources are FlyByWire's master branch; `A32NX_Interior_EFIS.xml` and `PseudoFWC.ts` were also read at
  the tag v2024.1.0 (same lines).

## Where the page sits

A first-level folder page **efis**, opened by the folder key `EFIS` at **main 4,8** (the main page's only
free position; P4-1 had it reserved for CHECKLIST, which has no position on the A32NX main page yet).
1,1 is the back key (it returns to the main page), as on every child page. How the pages connect:
[navigation.md](navigation.md), "MSFS2024 A32NX pages".

## Layout: efis

Positions are **row,column**, 1-based, row 1 at the top. Column 2 is the baro knob, as on the FCU page: `+`
above the readout above `-`; QNH and STD (the knob's push and pull) sit left of it. Row 1 holds FD and the
five ND option buttons, row 2 LS, the ND knobs, the ADF/VOR switches and CHRONO. Reserved keys are in
brackets.

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | BARO+ | FD | CSTR | WPT | VOR.D | NDB | ARPT |
| **Row 2** | QNH | BARO | LS | ND MODE | ND RNG | ADF/VOR1 | ADF/VOR2 | CHRONO |
| **Row 3** | STD | BARO- | hPa/inHg | RADIO > | XPDR > | PED > | | AUTOLAND |
| **Row 4** | WARN | CAUT | [F/O EFIS] | [F/O EFIS] | [F/O EFIS] | [F/O EFIS] | [F/O EFIS] | [F/O EFIS] |

21 keys, the 3 folder keys `RADIO`, `XPDR` (P4-4, [phase4-a32nx-radios.md](phase4-a32nx-radios.md)) and `PED`
(P4-6, [phase4-a32nx-pedestal.md](phase4-a32nx-pedestal.md)), the back key and 7 empty positions: 3,7 reserved
for a later unit, 4,3 to 4,8 reserved for the First Officer's EFIS control panel (a later unit). 11 keys are
new functions (CSTR, WPT, VOR.D, NDB, ARPT, QNH, STD, ADF/VOR1, ADF/VOR2, CHRONO, AUTOLAND); 10 repeat a P4-1
key (FD, LS, BARO+, BARO, BARO-, hPa/inHg, ND MODE, ND RNG, WARN, CAUT) with the same settings, so the whole
panel is on one page.

## Key table: efis

Action names are the PilotsDeck README's: **Dynamic Button**, **Display Value**, **Simple Button**. **Back**
= the Stream Deck app's back key (`backtoparent`), added by the generator. "Empty" = no action on that key.
The kinds K1 to K10 are explained in [phase4-a32nx.md](phase4-a32nx.md), "What each key holds"; source tags
under "Sources" below. Command types: `K:` = K-Var (saved as 16), `L:` = L-Var (3; the key writes its On or
Off value), `lua:` = Lua Function (14).

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to the main page | none | Back key |
| 1,2 | `BARO+` | Simple Button | K6 | `K:A32NX.FCU_EFIS_L_BARO_INC` [FBW-EVENTS, FBW-API] | none (BARO at 2,2 shows the result) | fixed image |
| 1,3 | `FD` | Dynamic Button | K1 | `K:A32NX.FCU_EFIS_L_FD_PUSH` [FBW-EVENTS] | `L:A32NX_FCU_EFIS_L_FD_LIGHT_ON` [FBW-SIMVARS] | On/Off image |
| 1,4 | `CSTR` | Dynamic Button | K1 | `K:A32NX.FCU_EFIS_L_CSTR_PUSH` [FBW-EVENTS, FBW-EFIS-XML] | `L:A32NX_FCU_EFIS_L_CSTR_LIGHT_ON` [FBW-SIMVARS, FBW-API, FBW-EFIS-XML] | On/Off image |
| 1,5 | `WPT` | Dynamic Button | K1 | `K:A32NX.FCU_EFIS_L_WPT_PUSH` [FBW-EVENTS, FBW-EFIS-XML] | `L:A32NX_FCU_EFIS_L_WPT_LIGHT_ON` [FBW-SIMVARS, FBW-API, FBW-EFIS-XML] | On/Off image |
| 1,6 | `VOR.D` | Dynamic Button | K1 | `K:A32NX.FCU_EFIS_L_VORD_PUSH` [FBW-EVENTS, FBW-EFIS-XML] | `L:A32NX_FCU_EFIS_L_VORD_LIGHT_ON` [FBW-SIMVARS, FBW-API, FBW-EFIS-XML] | On/Off image |
| 1,7 | `NDB` | Dynamic Button | K1 | `K:A32NX.FCU_EFIS_L_NDB_PUSH` [FBW-EVENTS, FBW-EFIS-XML] | `L:A32NX_FCU_EFIS_L_NDB_LIGHT_ON` [FBW-SIMVARS, FBW-API, FBW-EFIS-XML] | On/Off image |
| 1,8 | `ARPT` | Dynamic Button | K1 | `K:A32NX.FCU_EFIS_L_ARPT_PUSH` [FBW-EVENTS, FBW-EFIS-XML] | `L:A32NX_FCU_EFIS_L_ARPT_LIGHT_ON` [FBW-SIMVARS, FBW-API, FBW-EFIS-XML] | On/Off image |
| 2,1 | `QNH` | Dynamic Button | K1 | `K:A32NX.FCU_EFIS_L_BARO_PUSH` (baro knob push) [FBW-EVENTS, FBW-EFIS-PILOT] | `L:A32NX_FCU_EFIS_L_DISPLAY_BARO_MODE` (0 STD, 1 QNH, 2 QFE) [FBW-SIMVARS, FBW-API] | On/Off image: On `1`, Off `0` (the template's; lit in QNH) |
| 2,2 | `BARO` | Display Value | K3 | Main `K:A32NX.FCU_EFIS_L_BARO_PUSH` (QNH), Second (long press) `K:A32NX.FCU_EFIS_L_BARO_PULL` (STD) [FBW-EVENTS, FBW-API] | `lua:XL24-A32NX:BARO` (the script) [README 2.1.1 LUAFUNC; FBW-SIMVARS, FBW-API] | Lua text: the Captain's baro window |
| 2,3 | `LS` | Dynamic Button | K1 | `K:A32NX.FCU_EFIS_L_LS_PUSH` [FBW-EVENTS] | `L:A32NX_FCU_EFIS_L_LS_LIGHT_ON` [FBW-SIMVARS] | On/Off image |
| 2,4 | `ND MODE` | Display Value | K7 | Main `lua:XL24-A32NX:NDMODE(1)`, Second (long press) `lua:XL24-A32NX:NDMODE(-1)` (the script writes the L-Var) [README 2.1.1 LUAFUNC, 3.5.1] | `L:A32NX_FCU_EFIS_L_EFIS_MODE` [FBW-API, FBW-SIMVARS, FBW-EFIS-XML] | Mappings `0=ILS:1=VOR:2=NAV:3=ARC:4=PLAN` |
| 2,5 | `ND RNG` | Display Value | K7 | Main `lua:XL24-A32NX:NDRANGE(1)`, Second (long press) `lua:XL24-A32NX:NDRANGE(-1)` (the script writes the L-Var) [README 2.1.1 LUAFUNC, 3.5.1] | `L:A32NX_FCU_EFIS_L_EFIS_RANGE` [FBW-API, FBW-SIMVARS, FBW-EFIS-XML] | Mappings `0=10:1=20:2=40:3=80:4=160:5=320` |
| 2,6 | `ADF/VOR1` | Display Value | K7 | Main `lua:XL24-A32NX:NAV1(1)` (one position toward VOR), Second (long press) `lua:XL24-A32NX:NAV1(-1)` (toward ADF) (the script writes the L-Var) [README 2.1.1 LUAFUNC, 3.5.1] | `L:A32NX_FCU_EFIS_L_NAVAID_1_MODE` [FBW-API, FBW-EFIS-XML] | Mappings `0=OFF:1=ADF:2=VOR` |
| 2,7 | `ADF/VOR2` | Display Value | K7 | Main `lua:XL24-A32NX:NAV2(1)` (one position toward VOR), Second (long press) `lua:XL24-A32NX:NAV2(-1)` (toward ADF) (the script writes the L-Var) [README 2.1.1 LUAFUNC, 3.5.1] | `L:A32NX_FCU_EFIS_L_NAVAID_2_MODE` [FBW-API, FBW-EFIS-XML] | Mappings `0=OFF:1=ADF:2=VOR` |
| 2,8 | `CHRONO` | Simple Button | K6 | `K:A32NX.EFIS_L_CHRONO_PUSHED` [FBW-EVENTS] | none (the left ND shows the chrono time) | fixed image |
| 3,1 | `STD` | Dynamic Button | K1 | `K:A32NX.FCU_EFIS_L_BARO_PULL` (baro knob pull) [FBW-EVENTS, FBW-EFIS-PILOT] | `L:A32NX_FCU_EFIS_L_DISPLAY_BARO_MODE` (0 STD, 1 QNH, 2 QFE) [FBW-SIMVARS, FBW-API] | On/Off image: On `0`, Off `1` (lit in STD) |
| 3,2 | `BARO-` | Simple Button | K6 | `K:A32NX.FCU_EFIS_L_BARO_DEC` [FBW-EVENTS, FBW-API] | none (BARO at 2,2 shows the result) | fixed image |
| 3,3 | `hPa/inHg` | Display Value | K5 | `L:A32NX_FCU_EFIS_L_BARO_IS_INHG`, On `1` / Off `0` (inHg / hPa) [FBW-API, FBW-EFIS-XML] | `L:A32NX_FCU_EFIS_L_BARO_IS_INHG` [FBW-API, FBW-SIMVARS] | Mappings `0=hPa:1=inHg` |
| 3,4 | `RADIO` | Folder | (Stream Deck) | Opens the child page **radio** | none | Folder; the page's keys: "Key table: radio" in [phase4-a32nx-radios.md](phase4-a32nx-radios.md) |
| 3,5 | `XPDR` | Folder | (Stream Deck) | Opens the child page **xpdr** | none | Folder; the page's keys: "Key table: xpdr" in [phase4-a32nx-radios.md](phase4-a32nx-radios.md) |
| 3,6 | `PED` | Folder | (Stream Deck) | Opens the child page **ped** | none | Folder; the page's keys: "Key table: ped" in [phase4-a32nx-pedestal.md](phase4-a32nx-pedestal.md) |
| 3,7 | | Empty | | | | Reserved (a later unit) |
| 3,8 | `AUTOLAND` | Display Value | K9 | none | `L:A32NX_AUTOPILOT_AUTOLAND_WARNING` [FBW-API, FBW-FCU-XML; FBW-SIMVARS lists it as deprecated] | Mappings `0=---:1=ON` |
| 4,1 | `WARN` | Dynamic Button | K10 | `lua:XL24-A32NX:MWARN` (the script presses the MASTER WARN button: its push L-Var 1, 200 ms, 0) [FBW-INTERIOR, FBW-FWC; README 2.1.1 LUAFUNC, 3.5.1] | `L:A32NX_MASTER_WARNING` [FBW-API, FBW-FWC] | On/Off image |
| 4,2 | `CAUT` | Dynamic Button | K10 | `lua:XL24-A32NX:MCAUT` (the script presses the MASTER CAUT button: its push L-Var 1, 200 ms, 0) [FBW-INTERIOR, FBW-FWC; README 2.1.1 LUAFUNC, 3.5.1] | `L:A32NX_MASTER_CAUTION` [FBW-API, FBW-FWC] | On/Off image |
| 4,3 | | Empty | | | | Reserved: F/O side EFIS (a later unit) |
| 4,4 | | Empty | | | | Reserved: F/O side EFIS (a later unit) |
| 4,5 | | Empty | | | | Reserved: F/O side EFIS (a later unit) |
| 4,6 | | Empty | | | | Reserved: F/O side EFIS (a later unit) |
| 4,7 | | Empty | | | | Reserved: F/O side EFIS (a later unit) |
| 4,8 | | Empty | | | | Reserved: F/O side EFIS (a later unit) |

Title sizes ([navigation.md](navigation.md), "Rules"): the Dynamic and Simple Buttons are copied from the AP
key and draw their titles at 14 (no title on them has 8 or more characters); the Display Values keep their
template size (15), `ADF/VOR1`, `ADF/VOR2`, `AUTOLAND` and `hPa/inHg` included (as P4-1's `SPD/MACH`).

## What the keys do

- **FD, LS** press the Captain's FD and LS buttons and light from the button's own light L-Var (as main 1,6
  and 1,7).
- **CSTR, WPT, VOR.D, NDB, ARPT** press the ND option buttons; each lights from its own light L-Var.
  FlyByWire: "Only one selection can be active at a time." (FBW-EFIS-PILOT), so pressing one puts the lit one
  out; the keys show it because each reads its own light.
- **BARO+ / BARO-** turn the baro knob one step; **BARO** shows the baro window (`STD`, `1013` or `29.92`;
  blank when the FCU is not healthy). A BARO press pushes the knob, a long press (hold at least 0.5 s) pulls
  it, as on the main and FCU pages.
- **QNH** pushes the baro knob and is lit while the baro mode is QNH; **STD** pulls the knob and is lit while
  the mode is STD. FlyByWire: pulling selects the standard setting; in STD a push "makes the last selected QFE
  or QNH setting available", and once off STD a push changes between QNH and QFE (FBW-EFIS-PILOT). So QNH is
  the knob's push, not a "select QNH": in QFE (mode 2) a press goes to QNH, but a press while QNH is lit goes
  to QFE where the aircraft offers QFE (the hand test records it). In QFE neither key shows its On or Off
  image, only the key background and its title (PilotsDeck draws no image for a value that is neither the On
  nor the Off value; see phase4-a32nx.md, the BRK note).
- **hPa/inHg** writes the baro unit selector (inHg / hPa) and shows it (as fcu 4,8).
- **ND MODE, ND RNG** step the ND mode and range knobs (as main 2,6 and 2,7).
- **ADF/VOR1, ADF/VOR2**: press = the switch one position to the right, toward VOR (ADF > OFF > VOR); long
  press = one position to the left, toward ADF. They stop at the ends. The key shows `ADF`, `OFF` or `VOR`
  from the switch L-Var the aircraft reads. The values are FlyByWire's Flight Deck API's (0 OFF, 1 ADF,
  2 VOR) and the cockpit switch's own (it writes 1 left, 0 middle, 2 right; tooltips ADF, OFF, VOR:
  FBW-EFIS-XML); FlyByWire's `a320-simvars.md` says VOR 1, ADF 2 instead (see "Fallbacks").
- **CHRONO** presses the left chrono button, which starts the chrono on the Captain's ND ("When triggered
  presses the left chrono button (to start the clock on the left ND)", FBW-EVENTS); the hand test records
  what a second and third press do. No L-Var for the ND chrono is documented, so the key shows no state:
  the ND shows the time.
- **AUTOLAND** shows `ON` while the AUTOLAND warning lamp is lit (the cockpit lamp reads this L-Var and flashes
  from it, FBW-FCU-XML), `---` otherwise. Read only.
- **WARN, CAUT** are the main page's 3,1 and 3,2 keys: lit while the MASTER WARNING / MASTER CAUTION lamp is
  on; a press presses the Captain's MASTER WARN / MASTER CAUT button the way the cockpit does (see "The
  script").

## The script

[`pilotsdeck/MSFS2024-XL/_Package/Scripts/XL24-A32NX.lua`](../pilotsdeck/MSFS2024-XL/_Package/Scripts/XL24-A32NX.lua)
(the main page's script, [phase4-a32nx.md](phase4-a32nx.md), "The script"). P4-2 added four functions at the
end; nothing that was there changed. The new L-Vars are registered with `SimVar(...)` at the top level of the
file, as the others.

| Function | Does | Reads / writes |
|---|---|---|
| `NAV1(step)` | reads ADF/VOR switch 1, moves it `step` positions (`1` = toward VOR, `-1` = toward ADF; positions left to right ADF = value 1, OFF = 0, VOR = 2), keeps it on the switch and writes the value; an unknown value counts as OFF; does nothing when `L:A32NX_FCU_HEALTHY` is not 1 | `L:A32NX_FCU_EFIS_L_NAVAID_1_MODE` |
| `NAV2(step)` | the same for ADF/VOR switch 2 | `L:A32NX_FCU_EFIS_L_NAVAID_2_MODE` |
| `MWARN()` | presses the Captain's MASTER WARN button: `SimWrite` 1, `Sleep(200)`, `SimWrite` 0; no FCU check | writes `L:PUSH_AUTOPILOT_MASTERAWARN_L` |
| `MCAUT()` | the same for MASTER CAUT | writes `L:PUSH_AUTOPILOT_MASTERCAUT_L` |

Why WARN and CAUT press the button instead of writing the lamp: in the cockpit, the glareshield MASTER WARN
button writes `L:PUSH_AUTOPILOT_MASTERAWARN_L` 1 when pressed and 0 when released (MASTER CAUT the same with
`L:PUSH_AUTOPILOT_MASTERCAUT_L`), and lights from `L:A32NX_MASTER_WARNING` / `L:A32NX_MASTER_CAUTION`
(FBW-INTERIOR). The flight warning computer reads the push L-Var, makes a pulse on its 0 -> 1 edge, and writes
the lamp L-Var itself (FBW-FWC). So the key does what the cockpit button does. A PilotsDeck L-Var toggle
cannot do that (it would leave the button "held" every other press), so the script writes 1, waits 200 ms
and writes 0 (README 3.5.1: `SimWrite`, `Sleep`; 3.5: in a command, Sleep blocks nothing). P4-1's key wrote 0 to
the lamp L-Var (FBW-API lists it as read/write), which bypasses the FWC; P4-2 changed main 3,1 and 3,2 to the
press as well.

## What each key holds

The kinds K1 to K10 of [phase4-a32nx.md](phase4-a32nx.md), "What each key holds": every key is a copy of a
real saved key with only the listed fields changed (the generator does this). On this page: K1 (FD, LS, the
option buttons, QNH, STD; STD sets On State `0` and Off State `1`), K3 (BARO, as main 2,5), K5 (hPa/inHg, as
fcu 4,8), K6 (BARO+, BARO-, CHRONO, as fcu 1,8 and 3,8), K7 (ND MODE, ND RNG, ADF/VOR1, ADF/VOR2, as main 2,6),
K9 (AUTOLAND) and K10 (WARN, CAUT: the Phase 1 AP key with a Lua Function command, as the C172 sim rate `1X`
key). The data file is `tools/profilegen/a32nx.json`, page `efis` (`"spec": "docs/phase4-a32nx-efis.md"`).

## What the keys show when the A32NX isn't there

- No sim, or no flight: PilotsDeck's own idle and waiting images, as on the other pages.
- Another aircraft (or the A32NX not powered): BARO is **blank**, and ND MODE, ND RNG, ADF/VOR1 and ADF/VOR2
  presses do nothing (the FCU is not healthy). Every other key shows what its variable reads: an L-Var the
  aircraft doesn't have reads 0, so FD, LS, the option buttons, WARN and CAUT show off, **QNH shows off and
  STD lit**, ND MODE `ILS`, ND RNG `10`, ADF/VOR1 and 2 `OFF`, hPa/inHg `hPa`, AUTOLAND `---`. That is the 0
  of a missing variable, not the aircraft's state.
- WARN and CAUT presses write the A32NX's push L-Vars 1 then 0 in any aircraft; another aircraft does not read
  them, so nothing moves.
- A command the sim refuses shows PilotsDeck's alert sign on the key.

## Not on this page, and why

- **The First Officer's EFIS panel**: every name exists with `_R_` (FBW-SIMVARS `{side} = L or R`, FBW-EVENTS
  `side = L, R`), but a single pilot uses the Captain's side; row 4 columns 3 to 8 are reserved for it.
- **Sidestick priority lights**: no Flight Deck API row (FBW-API "N/A"); they need two FCDC L-Vars and light
  only when a takeover button is pressed.
- **The centre clock**: `A32NX_CHRONO_*` is the clock instrument's CHR display (FBW-SIMVARS), not the ND chrono.

## Fallbacks

Use one only if the checklist shows the main route does not work, and say which one you used. None is tested.
A key that fails with no working fallback becomes readout-only (command none) or Empty, and its row in
aircraft-mappings.md says "does not work".

| Key | If it fails | Fallback | Source |
|---|---|---|---|
| WARN, CAUT (here and main 3,1 / 3,2) | The press (push L-Var 1, 200 ms, 0) doesn't put the lamp out or stop the aural | First a longer press: only the `Sleep` value in `MWARN` / `MCAUT` changes. If the press does not work at all: P4-1's form on both pages, a K2 key that writes 0 to the lamp L-Var (`L:A32NX_MASTER_WARNING` / `L:A32NX_MASTER_CAUTION`, On `0` / Off `0`); then readout only | FBW-INTERIOR, FBW-FWC, FBW-API |
| ADF/VOR1, ADF/VOR2 | The key shows `ADF` while the cockpit switch is on VOR (or the other way round) | The values are FlyByWire's `a320-simvars.md` ones (VOR 1, ADF 2): swap `1=ADF:2=VOR` to `1=VOR:2=ADF` in both mappings and swap the values 1 and 2 in the two helper functions in `XL24-A32NX.lua` (`navaid_pos`, `navaid_value`), nothing else | FBW-SIMVARS, FBW-API, FBW-EFIS-XML |
| ADF/VOR1, ADF/VOR2 | Writing the L-Var doesn't move the switch | Readout only (command none) | FBW-API |
| CHRONO | The plugin log shows the command, the chrono doesn't start | The H-event `H:A32NX_EFIS_L_CHRONO_PUSHED` (FBW-API lists it as an "HTML Event"): a Simple Button with command type H-Var (`ActionType` 8), as the C172 PFD H-event keys | FBW-API |
| AUTOLAND | It stays `---` while the cockpit's AUTOLAND lamp is lit (FlyByWire lists the L-Var as deprecated) | The key becomes Empty | FBW-SIMVARS, FBW-FCU-XML |
| CSTR, WPT, VOR.D, NDB, ARPT, QNH, STD, CHRONO (every `K:A32NX.*` key) | The plugin log shows the command, the cockpit doesn't move | As phase4-a32nx.md: a Lua function per key that sends the event as calculator code (`SimCalculator`) | FBW-SCI (phase4-a32nx.md); README 2.1.1 CALCULATOR, 3.5.1 |

## How to test

Run [tests/manual-checklist.md](../tests/manual-checklist.md), section "Phase 4: A32NX EFIS page (P4-2)",
after the P4-1 section's "Before you start" and "Import" steps. As on the other pages, check both directions:
press a key and watch the cockpit, then **move the control in the cockpit with the mouse and check that the
key follows without a key being pressed.** Record the values the cockpit writes for ADF and VOR, whether
CHRONO starts the ND chrono, whether AUTOLAND ever shows `ON`, and whether the 200 ms WARN/CAUT press is
long enough.

## When it passes

1. Any change found in the test goes into `tools/profilegen/a32nx.json`, the script and this doc; then the
   profile is regenerated (not exported from the app) and imported again, and the script copied again.
2. Fill in the "Verified" column of the rows in aircraft-mappings.md ("FlyByWire A32NX EFIS page (P4-2)") with
   the date, sim version and A32NX version, for each function that passed; mark a row "does not work" where a
   key failed.

## Sources

All FlyByWire sources are in the flybywiresim/aircraft repository or FlyByWire's docs site, read 2026-11-14.
The tags FBW-SIMVARS, FBW-EVENTS, FBW-IE, FBW-API, FBW-SCI and README are the ones of
[phase4-a32nx.md](phase4-a32nx.md), "Sources".

| Tag | Source |
|---|---|
| FBW-SIMVARS | `fbw-a32nx/docs/a320-simvars.md`, https://raw.githubusercontent.com/flybywiresim/aircraft/master/fbw-a32nx/docs/a320-simvars.md (master), "#### FCU EFIS CP": `A32NX_FCU_EFIS_{side}_{button}_LIGHT_ON` with `{button}` = FD, LS, CSTR, WPT, VORD, NDB, ARPT; `..._DISPLAY_BARO_MODE` (STD 0, QNH 1, QFE 2); `..._NAVAID_{number}_MODE` (here NONE 0, VOR 1, ADF 2); `..._EFIS_MODE`, `..._EFIS_RANGE`; Deprecated: `A32NX_AUTOPILOT_AUTOLAND_WARNING` |
| FBW-EVENTS | `fbw-a32nx/docs/a320-events.md`, https://raw.githubusercontent.com/flybywiresim/aircraft/master/fbw-a32nx/docs/a320-events.md (master), "### EFIS CP": `A32NX.FCU_EFIS_{side}_{FD,LS,CSTR,WPT,VORD,NDB,ARPT}_PUSH`, `..._BARO_INC`, `..._BARO_DEC`, `..._BARO_PUSH`, `..._BARO_PULL`; `A32NX.EFIS_L_CHRONO_PUSHED` |
| FBW-IE | `fbw-a32nx/docs/a32nx-input-events.md` (master): input events only for the ECAM control panel and NAV & LOGO |
| FBW-API | FlyByWire Flight Deck API, https://docs.flybywiresim.com/aircraft/a32nx/a32nx-api/a32nx-flightdeck-api/ ("might lag behind"): Glareshield "Warning Panel" (MASTER WARNING / MASTER CAUTION L-Vars, CHRONO as `H:A32NX_EFIS_L_CHRONO_PUSHED`, AUTOLAND WARNING) and "EFIS Control Panel" (the option light L-Vars, `A32NX_FCU_EFIS_L_NAVAID_1_MODE` / `_2_MODE` "R/W" with 0=OFF, 1=ADF, 2=VOR, the baro mode and unit L-Vars) |
| FBW-EFIS-XML | `fbw-a32nx/src/behavior/src/A32NX_Interior_EFIS.xml`, https://raw.githubusercontent.com/flybywiresim/aircraft/master/fbw-a32nx/src/behavior/src/A32NX_Interior_EFIS.xml (master and tag v2024.1.0): the cockpit's EFIS control panel: the option buttons send `A32NX.FCU_EFIS_#SIDE#_#BASE_NAME#_PUSH` and light from `..._LIGHT_ON`; the NAV AID switch writes 1 / 0 / 2 (tooltips ADF / OFF / VOR); the baro selector toggles `BARO_IS_INHG`; the ND knobs drive `EFIS_MODE` / `EFIS_RANGE` |
| FBW-INTERIOR | `A320_NEO_INTERIOR.xml`, https://raw.githubusercontent.com/flybywiresim/aircraft/master/fbw-a32nx/src/base/flybywire-aircraft-a320-neo/SimObjects/AirPlanes/FlyByWire_A320_NEO/model/A320_NEO_INTERIOR.xml (master): `A32NX_PUSH_WARN_L` / `A32NX_PUSH_CAUTION_L` write `PUSH_AUTOPILOT_MASTERAWARN_L` / `PUSH_AUTOPILOT_MASTERCAUT_L` 1 on press, 0 on release, and light from `A32NX_MASTER_WARNING` / `A32NX_MASTER_CAUTION`; the EFIS_L option, ADF switch, chrono and autoland lamp instances |
| FBW-FCU-XML | `fbw-a32nx/src/behavior/src/A32NX_Interior_FCU.xml` (master): the autoland lamp template reads `L:A32NX_AUTOPILOT_AUTOLAND_WARNING` (and flashes), no write |
| FBW-FWC | `PseudoFWC.ts`, https://raw.githubusercontent.com/flybywiresim/aircraft/master/fbw-a32nx/src/systems/systems-host/systems/FWC/PseudoFWC.ts (master and tag v2024.1.0): the FWC reads `L:PUSH_AUTOPILOT_MASTERAWARN_L` (and the caution push L-Var), makes a pulse on its rising edge, and writes `L:A32NX_MASTER_WARNING` / `L:A32NX_MASTER_CAUTION` itself |
| FBW-EFIS-PILOT | FlyByWire pilot's guide, EFIS Control Panel, https://docs.flybywiresim.com/pilots-corner/a32nx/a32nx-briefing/flight-deck/glareshield/efis_control/: pull = STD, push changes between QNH and QFE once off STD; "Only one selection can be active at a time." |
| README | PilotsDeck README, https://github.com/Fragtality/PilotsDeck/blob/master/README.md: 2.1.1 (address forms: L-Var, K-Var, Lua Function), 3.5 (Lua scripts: Sleep in a command blocks nothing), 3.5.1 (standard scripts: `SimVar`, `SimRead`, `SimWrite`, `Sleep`) |
