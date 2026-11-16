# Phase 4: A32NX radio and transponder pages (RMP 1 and ATC/TCAS panel)

**Status: generated, not yet sim-tested.** Both pages are in the generated profile `MSFS2024 A32NX`, but
nothing on them has been tried in the app or the sim yet, and the A32NX is not yet installed on this PC (see
"Install status"). Every name below is recorded as "Unverified" in
[aircraft-mappings.md](aircraft-mappings.md) ("FlyByWire A32NX radio and transponder pages (P4-4)") until the
checks in [tests/manual-checklist.md](../tests/manual-checklist.md), section "Phase 4: A32NX radio and
transponder pages (P4-4)", pass.

Goal: the Captain's radio management panel (**RMP 1**) and the **ATC/TCAS panel** on two pages opened from the
EFIS page. **radio** (efis 3,4 `RADIO`) has the RMP's VHF1 and VHF2 keys, its ON/OFF switch, its ACTIVE and
STBY windows, the transfer key and the two tuning knobs as four step keys, and the active frequencies of COM1
and COM2. **xpdr** (efis 3,5 `XPDR`) has the transponder code, the panel's own keypad (0 to 7 and CLR), the
transponder state, IDENT, the mode selector (STBY/AUTO/ON), ALT RPTG, and the TCAS mode and traffic
selectors. Every key lights or reads from the aircraft; no key assumes its press worked.

The pages are part of the profile `MSFS2024 A32NX` (same file, same name, same import as the main page: see
[phase4-a32nx.md](phase4-a32nx.md), "Import the profile"), and their ACTIVE, STBY, MODE, TCAS and TRAFFIC keys
use the same Lua script `XL24-A32NX.lua`, which must be installed again (P4-4 added five functions). The two
key tables below are the reference for what each key holds; `tools/profilegen/check.py
tools/profilegen/a32nx.json` compares the profile with "Key table: radio" and "Key table: xpdr" key by key. No
existing key moved or changed; only efis 3,4 and 3,5, empty before, became the two folder keys.

Nothing on these pages uses keyboard bindings, vJoy or anything tied to a controller: the keys send the
cockpit's own H-events (through the MobiFlight WASM module, see "The MobiFlight WASM module"), one standard
SimConnect event (IDENT), write L-Vars or run the Lua script, and read L-Vars and SimVars, so they work the
same with the Xbox Elite controller and the T.16000M + TWCS.

## Install status

- **The A32NX is not installed on this PC yet** (checked 2026-11-16, read only, as for P4-1 to P4-3): the
  MSFS 2024 package folders hold no FlyByWire package, and PilotsDeck has never seen an A32NX flight (its
  `InputEvents.txt` holds only the C172 G1000's events, no `A32NX` L-Var in its `L-Vars.txt`, no A32NX
  aircraft line in its newest logs).
- FlyByWire's MSFS 2024 support is as in [phase4-a32nx.md](phase4-a32nx.md), "Install status" (Stable
  v2024.1.0, "officially compatible with MSFS 2024", FBW-REL). FlyByWire's input events still cover only the
  ECAM control panel and the NAV & LOGO switch (FBW-IE): the RMP and the ATC/TCAS panel have none, so these
  pages use the H-events and L-Vars of the cockpit's own behaviour files and gauges, and standard SimVars for
  the reads.
- The FlyByWire sources are read at the tag **v2024.1.0** (the MSFS 2024 Stable release), the a320-simvars
  list at master. Where FlyByWire's documents differ from the cockpit's code (the VHF2 standby L-Var's name,
  the RMP mode values above 3, the TCAS row labels of the Flight Deck API), the code wins.

## Where the pages sit

**radio** and **xpdr** are second-level pages, opened by the folder keys `RADIO` at **efis 3,4** and `XPDR` at
**efis 3,5** (the EFIS page is opened by main 4,8). Each page's back key (1,1) returns to the EFIS page, so
these pages are two back presses from the main page (the most [navigation.md](navigation.md) allows; neither
page holds a folder key). The main page and the FCU page have no free position, and efis 3,4 to 3,7 were
reserved for a later unit. How the pages connect: [navigation.md](navigation.md), "MSFS2024 A32NX pages".

## Layout: radio

Positions are **row,column**, 1-based, row 1 at the top. Reserved keys are in brackets. Row 1 holds the RMP's
radio keys, its ON/OFF switch and the knob steps up, row 2 the COM readouts, the RMP windows with XFER between
them, and the knob steps down.

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | VHF1 | VHF2 | [VHF3] | | RMP ON | MHz+ | kHz+ |
| **Row 2** | COM1 | COM2 | | ACTIVE | XFER | STBY | MHz- | kHz- |
| **Row 3** | | | | | | | | |
| **Row 4** | | | | | | | | |

12 keys, the back key and 19 empty positions: 1,4 reserved for VHF3 (a later unit), 1,5, 2,3 and rows 3 and
4 reserved for a later unit.

## Key table: radio

Action names are the PilotsDeck README's: **Dynamic Button**, **Display Value**, **Simple Button**. **Back**
= the Stream Deck app's back key (`backtoparent`), added by the generator. "Empty" = no action on that key.
The kinds K1 to K11 are explained in [phase4-a32nx.md](phase4-a32nx.md), "What each key holds" (K11 in
[phase4-a32nx-overhead.md](phase4-a32nx-overhead.md)), K12 to K15 under "What each key holds" below; source
tags under "Sources" below. Command types: `H:` = H-Var (saved as 8), `K:` = K-Var (16), `L:` = L-Var (3; the
key writes its On or Off value), `lua:` = Lua Function (14).

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to the EFIS page | none | Back key |
| 1,2 | `VHF1` | Dynamic Button | K13 | `H:A32NX_RMP_L_VHF1_BUTTON_PRESSED` [FBW-RMP-XML, FBW-RMP-BASE] | `L:A32NX_RMP_L_SELECTED_MODE` [FBW-RMP-BASE, FBW-API] | On/Off image |
| 1,3 | `VHF2` | Dynamic Button | K13 | `H:A32NX_RMP_L_VHF2_BUTTON_PRESSED` [FBW-RMP-XML, FBW-RMP-BASE] | `L:A32NX_RMP_L_SELECTED_MODE` [FBW-RMP-BASE, FBW-API] | On/Off image: On `2`, Off `0` |
| 1,4 | | Empty | | | | Reserved: VHF3 (data link; a later unit) |
| 1,5 | | Empty | | | | Reserved (a later unit) |
| 1,6 | `RMP ON` | Dynamic Button | K2 | `L:A32NX_RMP_L_TOGGLE_SWITCH`, On `1` / Off `0` [FBW-API, FBW-RMP-XML, FBW-REACT] | `L:A32NX_RMP_L_TOGGLE_SWITCH` [FBW-SIMVARS, FBW-API, FBW-RMP-BASE] | On/Off image, Special State |
| 1,7 | `MHz+` | Simple Button | K12 | `H:A32NX_RMP_L_OUTER_KNOB_TURNED_CLOCKWISE` [FBW-RMP-XML, FBW-RMP-STBY] | none (STBY at 2,6 shows the result) | fixed image |
| 1,8 | `kHz+` | Simple Button | K12 | `H:A32NX_RMP_L_INNER_KNOB_TURNED_CLOCKWISE` [FBW-RMP-XML, FBW-RMP-STBY] | none (STBY at 2,6 shows the result) | fixed image |
| 2,1 | `COM1` | Display Value | K11 | none | `(A:COM ACTIVE FREQUENCY:1, MHz)` [SDK-RADV, FBW-API, FBW-RMP-VHF] | Format `1.3` |
| 2,2 | `COM2` | Display Value | K11 | none | `(A:COM ACTIVE FREQUENCY:2, MHz)` [SDK-RADV, FBW-API, FBW-RMP-VHF] | Format `1.3` |
| 2,3 | | Empty | | | | Reserved (a later unit) |
| 2,4 | `ACTIVE` | Display Value | K14 | none | `lua:XL24-A32NX:RMPACT` (the script) [README 2.1.1 LUAFUNC; FBW-RMP-VHF, FBW-RMP-BASE] | Lua text: RMP 1's active window |
| 2,5 | `XFER` | Simple Button | K12 | `H:A32NX_RMP_L_TRANSFER_BUTTON_PRESSED` [FBW-RMP-XML, FBW-RMP-VHF] | none (ACTIVE and STBY show the result) | fixed image |
| 2,6 | `STBY` | Display Value | K14 | none | `lua:XL24-A32NX:RMPSTBY` (the script) [README 2.1.1 LUAFUNC; FBW-RMP-VHF, FBW-RMP-BASE] | Lua text: RMP 1's standby window |
| 2,7 | `MHz-` | Simple Button | K12 | `H:A32NX_RMP_L_OUTER_KNOB_TURNED_ANTICLOCKWISE` [FBW-RMP-XML, FBW-RMP-STBY] | none (STBY at 2,6 shows the result) | fixed image |
| 2,8 | `kHz-` | Simple Button | K12 | `H:A32NX_RMP_L_INNER_KNOB_TURNED_ANTICLOCKWISE` [FBW-RMP-XML, FBW-RMP-STBY] | none (STBY at 2,6 shows the result) | fixed image |
| 3,1 | | Empty | | | | Reserved (a later unit) |
| 3,2 | | Empty | | | | Reserved (a later unit) |
| 3,3 | | Empty | | | | Reserved (a later unit) |
| 3,4 | | Empty | | | | Reserved (a later unit) |
| 3,5 | | Empty | | | | Reserved (a later unit) |
| 3,6 | | Empty | | | | Reserved (a later unit) |
| 3,7 | | Empty | | | | Reserved (a later unit) |
| 3,8 | | Empty | | | | Reserved (a later unit) |
| 4,1 | | Empty | | | | Reserved (a later unit) |
| 4,2 | | Empty | | | | Reserved (a later unit) |
| 4,3 | | Empty | | | | Reserved (a later unit) |
| 4,4 | | Empty | | | | Reserved (a later unit) |
| 4,5 | | Empty | | | | Reserved (a later unit) |
| 4,6 | | Empty | | | | Reserved (a later unit) |
| 4,7 | | Empty | | | | Reserved (a later unit) |
| 4,8 | | Empty | | | | Reserved (a later unit) |

## Layout: xpdr

The keypad sits in the places of the C172 profile's pads (7 at 1,6; 4 5 6; 1 2 3; CLR 0), with no 8, 9 or
ENT key: the panel's keypad has only the digits 0 to 7 and takes the code on the fourth digit. Column 2 and 3
hold the readouts and selectors.

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | XPDR | STATE | IDENT | | 7 | | |
| **Row 2** | | MODE | ALT RPTG | [SYS] | | 4 | 5 | 6 |
| **Row 3** | | TCAS | TRAFFIC | | | 1 | 2 | 3 |
| **Row 4** | | | | | | CLR | 0 | |

16 keys, the back key and 15 empty positions: 2,4 reserved for the XPDR SYS 1/2 selector (a later unit), the
others reserved for a later unit.

## Key table: xpdr

Forms as in "Key table: radio".

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to the EFIS page | none | Back key |
| 1,2 | `XPDR` | Display Value | K15 | none | `(A:TRANSPONDER CODE:1, Bco16)` [SDK-RADV, FBW-API, FBW-ATC-GAUGE] | Decode BCD, Format `4.0` |
| 1,3 | `STATE` | Display Value | K9 | none | `(A:TRANSPONDER STATE:1, Enum)` [SDK-RADV, FBW-ATC-XML] | Mappings `0=OFF:1=STBY:2=TEST:3=ON:4=ALT:5=GND` |
| 1,4 | `IDENT` | Dynamic Button | K1 | `K:XPNDR_IDENT_ON` [FBW-API, FBW-ATC-XML, SDK-RADE] | `(A:TRANSPONDER IDENT:1, Bool)` [SDK-RADV] | On/Off image |
| 1,5 | | Empty | | | | Reserved (a later unit) |
| 1,6 | `7` | Simple Button | K12 | `H:A320_Neo_ATC_BTN_7` [FBW-ATC-XML, FBW-ATC-GAUGE] | none (XPDR at 1,2 shows the code after the 4th digit) | fixed image |
| 1,7 | | Empty | | | | Reserved (a later unit) |
| 1,8 | | Empty | | | | Reserved (a later unit) |
| 2,1 | | Empty | | | | Reserved (a later unit) |
| 2,2 | `MODE` | Display Value | K7 | Main `lua:XL24-A32NX:XPDRMODE(1)` (one position clockwise), Second (long press) `lua:XL24-A32NX:XPDRMODE(-1)` (the script writes the L-Var) [README 2.1.1 LUAFUNC, 3.5.1] | `L:A32NX_TRANSPONDER_MODE` [FBW-SIMVARS, FBW-API, FBW-ATC-XML] | Mappings `0=STBY:1=AUTO:2=ON` |
| 2,3 | `ALT RPTG` | Dynamic Button | K2 | `L:A32NX_SWITCH_ATC_ALT`, On `1` / Off `0` [FBW-API, FBW-ATC-XML] | `L:A32NX_SWITCH_ATC_ALT` [FBW-SIMVARS, FBW-ATC-XML] | On/Off image, Special State |
| 2,4 | | Empty | | | | Reserved: XPDR SYS 1/2 (a later unit) |
| 2,5 | | Empty | | | | Reserved (a later unit) |
| 2,6 | `4` | Simple Button | K12 | `H:A320_Neo_ATC_BTN_4` [FBW-ATC-XML, FBW-ATC-GAUGE] | none (XPDR at 1,2 shows the code after the 4th digit) | fixed image |
| 2,7 | `5` | Simple Button | K12 | `H:A320_Neo_ATC_BTN_5` [FBW-ATC-XML, FBW-ATC-GAUGE] | none (XPDR at 1,2 shows the code after the 4th digit) | fixed image |
| 2,8 | `6` | Simple Button | K12 | `H:A320_Neo_ATC_BTN_6` [FBW-ATC-XML, FBW-ATC-GAUGE] | none (XPDR at 1,2 shows the code after the 4th digit) | fixed image |
| 3,1 | | Empty | | | | Reserved (a later unit) |
| 3,2 | `TCAS` | Display Value | K7 | Main `lua:XL24-A32NX:TCASMODE(1)` (one position clockwise), Second (long press) `lua:XL24-A32NX:TCASMODE(-1)` (the script writes the L-Var) [README 2.1.1 LUAFUNC, 3.5.1] | `L:A32NX_SWITCH_TCAS_Position` [FBW-SIMVARS, FBW-API, FBW-ATC-XML] | Mappings `0=STBY:1=TA:2=TA/RA` |
| 3,3 | `TRAFFIC` | Display Value | K7 | Main `lua:XL24-A32NX:TCASTRAF(1)` (one position clockwise), Second (long press) `lua:XL24-A32NX:TCASTRAF(-1)` (the script writes the L-Var) [README 2.1.1 LUAFUNC, 3.5.1] | `L:A32NX_SWITCH_TCAS_Traffic_Position` [FBW-SIMVARS, FBW-API, FBW-ATC-XML] | Mappings `0=THRT:1=ALL:2=ABV:3=BLW` |
| 3,4 | | Empty | | | | Reserved (a later unit) |
| 3,5 | | Empty | | | | Reserved (a later unit) |
| 3,6 | `1` | Simple Button | K12 | `H:A320_Neo_ATC_BTN_1` [FBW-ATC-XML, FBW-ATC-GAUGE] | none (XPDR at 1,2 shows the code after the 4th digit) | fixed image |
| 3,7 | `2` | Simple Button | K12 | `H:A320_Neo_ATC_BTN_2` [FBW-ATC-XML, FBW-ATC-GAUGE] | none (XPDR at 1,2 shows the code after the 4th digit) | fixed image |
| 3,8 | `3` | Simple Button | K12 | `H:A320_Neo_ATC_BTN_3` [FBW-ATC-XML, FBW-ATC-GAUGE] | none (XPDR at 1,2 shows the code after the 4th digit) | fixed image |
| 4,1 | | Empty | | | | Reserved (a later unit) |
| 4,2 | | Empty | | | | Reserved (a later unit) |
| 4,3 | | Empty | | | | Reserved (a later unit) |
| 4,4 | | Empty | | | | Reserved (a later unit) |
| 4,5 | | Empty | | | | Reserved (a later unit) |
| 4,6 | `CLR` | Simple Button | K12 | `H:A320_Neo_ATC_BTN_CLR` [FBW-ATC-XML, FBW-ATC-GAUGE] | none (XPDR at 1,2 shows the code) | fixed image |
| 4,7 | `0` | Simple Button | K12 | `H:A320_Neo_ATC_BTN_0` [FBW-ATC-XML, FBW-ATC-GAUGE] | none (XPDR at 1,2 shows the code after the 4th digit) | fixed image |
| 4,8 | | Empty | | | | Reserved (a later unit) |

## What the keys do

RADIO page:
- **VHF1, VHF2** press the RMP's own VHF1 / VHF2 key, so RMP 1 shows and tunes that radio. Each is lit while
  RMP 1 has its radio selected (`L:A32NX_RMP_L_SELECTED_MODE` 1 or 2; the cockpit key's green light also needs
  the RMP switched on). While VHF2 is selected the VHF1 key shows no image, and the reverse; in a NAV mode or
  VHF3 both keys show no image: the mode value matches neither key's On value nor its Off value (as the main
  page's BRK keys). They show their Off image only while the mode reads 0 (no A32NX). ASSUMPTION A-15.
- **RMP ON** works the RMP's ON/OFF switch by writing the switch's L-Var, as the cockpit switch does, and is
  lit while the switch is on. The RMP reads the L-Var again within half a second (FBW-REACT); the switch's
  H-event only tells the RMP that the cockpit switch moved, so the key does not send it.
- **MHz+, MHz-** turn the RMP's outer knob one step (MHz), **kHz+, kHz-** the inner knob one channel (kHz).
  FlyByWire's knob code keeps the standby frequency in 118 to 136 MHz and steps at the channel spacing the
  aircraft is set to (8.33 or 25 kHz, FBW-RMP-STBY), for whichever radio RMP 1 has selected. STBY shows the
  result.
- **XFER** presses the transfer key: the active and standby frequencies swap. ACTIVE and STBY show the result.
- **ACTIVE, STBY** show what RMP 1's two windows show, as `118.700`, from the script (`RMPACT`, `RMPSTBY`, see
  "The script"). They are blank when RMP 1 is switched off, its bus (DC ESS) is unpowered or it is in a NAV
  mode; ACTIVE shows `DATA` for VHF3 when VHF3 has no active frequency (FlyByWire sets VHF3 to data at start).
- **COM1, COM2** show the active frequencies of the sim's radios 1 and 2 (what you hear), whatever RMP 1
  shows, as `118.700`.

XPDR page:
- **XPDR** shows the transponder code the sim has (four digits).
- **7, 4, 5, 6, 1, 2, 3, 0** and **CLR** press the ATC panel's own keypad keys. The panel takes digits only
  while an entry is open, so **press CLR twice first** ("To clear the current code, double press the CLR
  button.", FBW-BEGIN): the first CLR opens an entry with the shown code's last digit removed, the second
  clears it (FBW-ATC-GAUGE). Digits pressed with no entry open do nothing. Then type the four digits: the old
  code stays until the fourth digit is in (FBW-PILOT-ATC), then the panel sets the new code itself
  (`K:XPNDR_SET`, FBW-ATC-GAUGE), and XPDR shows it. An open entry is dropped 7 seconds after the last key
  press (FBW-ATC-GAUGE).
- **STATE** shows the transponder state FlyByWire computes from the mode selector, ALT RPTG, the gear and the
  power (`OFF`, `STBY`, `ON`, `ALT` or `GND`; AUTO on the ground shows `GND`; `TEST` is the sim's value 2,
  which FlyByWire does not set). Read only: FlyByWire writes this SimVar itself, so a key that wrote it would
  be overwritten.
- **IDENT** sends the standard ident event the cockpit's IDENT button sends, and is lit while the sim's ident
  is on (it ends by itself after 18 seconds, SDK-RADE). ASSUMPTION A-18.
- **MODE, TCAS, TRAFFIC** move the mode selector (STBY, AUTO, ON), the TCAS mode selector (STBY, TA, TA/RA)
  and the traffic selector (THRT, ALL, ABV, BLW): a press moves one position clockwise, a long press (0.5 s
  or more) one position back; they stop at the ends. Each shows the position the aircraft reads. The script
  writes the selector's L-Var; FlyByWire's transponder update then sets STATE (ASSUMPTION A-7).
- **ALT RPTG** switches altitude reporting on and off and is lit while it is on; FlyByWire's transponder
  update uses it, so STATE shows `ALT` rather than `ON` while it is on (the test records when).

## What each key holds

The kinds of [phase4-a32nx.md](phase4-a32nx.md), "What each key holds": every key is a copy of a real saved
key with only the listed fields changed (the generator does this). On these pages: K1 (IDENT), K2 (RMP
ON, ALT RPTG), K7 (MODE, TCAS, TRAFFIC), K9 (STATE), K11 (COM1, COM2;
[phase4-a32nx-overhead.md](phase4-a32nx-overhead.md)) and four new kinds:

| Kind | Action, copied from | Fields set |
|---|---|---|
| K12 H-event press | Simple Button (`simple_button`, states from `p1:3,0`), the form of the C172 PFD and MFD bezel keys ([phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md), T7) | Command Type H-Var (`ActionType` 8), Command Address (`H:`), Background `Images/Switch.png`, Draw Box off, `LinkedTitle` on |
| K13 H-event button, lit | Dynamic Button, the Phase 1 AP key (`p1:3,0`, T2), as K10 with command type 8 | Command Type H-Var (`ActionType` 8), Command Address (`H:`), Value Address (`L:`); On State only where it is not `1` (VHF2 `2`) |
| K14 Lua readout | Display Value, the Phase 1 HDG key (`p1:2,0`, T3) | Value Address `lua:XL24-A32NX:<function>`, Format empty; no command (the template's L-Var type 3 with an empty Command Address) |
| K15 code readout | Display Value (`p1:2,0`), as the C172 main page's XPDR key | Value Address (`A:`, Bco16), Decode BCD on, Format `4.0`; no command |

PilotsDeck forms (README 2.1.1): an H-Var is "The Name of the H-Var with or without preceding `H:`", and
H-Vars "trigger an Event but can't be read", so each H-event key reads another variable or none; command type 8 is
the settings panel's H-Var type (PD-PI, as [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md), "Sources"). An
A-Var is read as `(A:Name:Index, Unit)`. Decode BCD (README 2.2.2): "If the Value is a binary coded decimal
(BCD), the Plugin can decode it for you with that Checkbox!". The data file is `tools/profilegen/a32nx.json`,
pages `radio` and `xpdr` (`"parent": "efis"`, `"spec": "docs/phase4-a32nx-radios.md"`), and the efis keys 3,4
and 3,5.

Title sizes ([navigation.md](navigation.md), "Rules"): Dynamic and Simple Buttons copied from the AP key draw
their titles at 14 (VHF1, VHF2, IDENT, the knob, XFER and keypad keys); of the two copied from the BAT key,
RMP ON keeps 15 and ALT RPTG (8 characters) is set to 13; Display Values keep their template size (15),
`TRAFFIC` included.

## The script

[`pilotsdeck/MSFS2024-XL/_Package/Scripts/XL24-A32NX.lua`](../pilotsdeck/MSFS2024-XL/_Package/Scripts/XL24-A32NX.lua)
(the main page's script, [phase4-a32nx.md](phase4-a32nx.md), "The script"). P4-4 added five functions at the
end and one header comment line; nothing that was there changed. The twelve new addresses are registered with
`SimVar(...)` at the top level of the file, as the others. The C172 profile's pad scripts `XL24-COMPAD.lua`
and `XL24-XPDRPAD.lua` are not used: the A32NX RMP 1 keeps its VHF2 standby frequency in its own L-Var, and
FlyByWire's panel takes the code from its own keypad.

| Function | Returns (text) or does | Reads / writes |
|---|---|---|
| `RMPACT()` | RMP 1's active window: the active frequency of the radio RMP 1 has selected (VHF1, VHF2 or VHF3), as `118.700`; `""` when RMP 1 is off, unpowered or in a NAV mode, or the frequency is 0; `DATA` for VHF3 with no frequency | reads `L:A32NX_RMP_L_TOGGLE_SWITCH`, `L:A32NX_ELEC_DC_ESS_BUS_IS_POWERED`, `L:A32NX_RMP_L_SELECTED_MODE`, `(A:COM ACTIVE FREQUENCY:1, Hz)`, `:2`, `:3` |
| `RMPSTBY()` | RMP 1's standby window, the same way: VHF1 the sim's COM 1 standby, VHF2 and VHF3 RMP 1's own standby L-Vars (FBW-RMP-VHF); `""` as above | reads the same three L-Vars, `(A:COM STANDBY FREQUENCY:1, Hz)`, `L:A32NX_RMP_L_VHF2_STANDBY_FREQUENCY`, `L:A32NX_RMP_L_VHF3_STANDBY_FREQUENCY` (Hz) |
| `XPDRMODE(step)` | reads the mode selector, adds `step` (1 or -1), keeps it in 0..2 (STBY, AUTO, ON) and writes it | `L:A32NX_TRANSPONDER_MODE` |
| `TCASMODE(step)` | the same for the TCAS mode selector, 0..2 (STBY, TA, TA/RA) | `L:A32NX_SWITCH_TCAS_Position` |
| `TCASTRAF(step)` | the same for the traffic selector, 0..3 (THRT, ALL, ABV, BLW) | `L:A32NX_SWITCH_TCAS_Traffic_Position` |

- The windows follow FlyByWire's RMP code: VHF1 on RMP 1 reads the sim's COM 1 active and standby
  frequencies; VHF2 and VHF3 read the sim's active frequency and RMP 1's own standby L-Var ("if ((side === 'L'
  && transceiver !== 1) ...", FBW-RMP-VHF); the panel shows nothing unless its bus is powered and its switch
  is on (FBW-RMP-BASE). The frequency is shown from whole kHz (`%d.%03d`), so no rounding shows. FlyByWire's
  a320-simvars list names the VHF2 standby L-Var `A32NX_RMP_L_VHF2_STANDBY`; the code's name, with
  `_FREQUENCY`, is used.
- The three selector functions have no FCU check (unlike `NDMODE`): the ATC/TCAS panel is not part of the
  FCU. In another aircraft the L-Var reads 0, so a press writes 0 + 1 to an L-Var nothing reads.

## The MobiFlight WASM module

Every `H:` command on these pages (VHF1, VHF2, XFER, the four knob keys, the eight digits and CLR: 16
keys) goes through the MobiFlight WASM module: "PilotsDeck sends every H-event and all calculator code
through the MobiFlight WASM module" ([troubleshooting.md](troubleshooting.md#the-mobiflight-wasm-module)). It
is installed on this PC ([installation.md](installation.md), "MobiFlight WASM module (which keys need it)").
Without it those 16 keys do nothing, most likely with no alert sign on the key. The Lua keys (`SimRead`,
`SimWrite`), IDENT (a K-event), RMP ON and ALT RPTG (L-Var writes) and every read do not need the module.

## What the keys show when the A32NX isn't there

- No sim, or no flight: PilotsDeck's own idle and waiting images, as on the other pages.
- Another aircraft (or the A32NX not powered): VHF1, VHF2 and RMP ON dark, ACTIVE and STBY blank (the RMP
  switch L-Var reads 0); MODE `STBY`, TCAS `STBY`, TRAFFIC `THRT` and ALT RPTG off. That is the 0 of a missing
  L-Var, not the aircraft's state; MODE, TCAS and TRAFFIC presses change only the key's text.
- COM1, COM2, XPDR, STATE and IDENT read standard SimVars, so they show the other aircraft's own values.
- The H-event keys: most aircraft have no listener for them, but the sim's own A320neo may answer the keypad
  events `A320_Neo_ATC_BTN_*` (an Asobo name, ASSUMPTION A-19). **IDENT idents any aircraft** (a standard
  event, harmless): keep the profile on the A32NX with the Profile Manager's aircraft mapping.
- A command the sim refuses shows PilotsDeck's alert sign on the key.

## Not on these pages

- **VHF3** (reserved at radio 1,4): FlyByWire sets it to data at start (`0 (>K:COM3_RADIO_SET_HZ)`, the
  window shows DATA, FBW-RMP-XML); ACTIVE and STBY still show it when it is selected in the cockpit.
- **The SEL light**: it depends on both RMPs, and FlyByWire marks its code `@todo` (FBW-RMP-XML).
- **The NAV backup keys** (NAV, VOR, ILS, ADF): a later NAV unit.
- **RMP 2** (the First Officer's side) and the **ACP** audio panel: out of this unit's scope.
- **XPDR SYS 1/2** (reserved at xpdr 2,4): "only 1 is available in the FBW A32NX" (FBW-PILOT-ATC).
- **A typed COM frequency pad**: the knob keys tune any radio RMP 1 has selected (VHF2 included, whose
  standby is an L-Var) within FlyByWire's range and spacing; a typed pad would need a third page below RADIO,
  which [navigation.md](navigation.md) does not allow at the second level (ASSUMPTION A-9).

## Fallbacks

Use one only if the checklist shows the main route does not work, and say which one you used. None is tested.
A key that fails with no working fallback becomes readout-only (command none) or Empty, and its row in
aircraft-mappings.md says "does not work".

| Key | If it fails | Fallback | Source |
|---|---|---|---|
| Any H-event key | The press does nothing (check first: the MobiFlight WASM module is installed and the plugin log shows "MobiFlight WASM Client Connection opened"; the plugin log shows the command) | See the rows below; else readout only or Empty | troubleshooting.md |
| RMP ON (A-20) | Writing the L-Var does not move the switch | The key becomes a readout (command none), same read; the switch's H-event `H:A32NX_RMP_L_TOGGLE_SWITCH` is no fallback: it only makes the RMP read the L-Var again (FBW-REACT) | FBW-API, FBW-RMP-XML, FBW-REACT |
| Keypad 0-7, CLR (A-8) | The digits do not reach the panel (typed after CLR, CLR) | A code pad of the script's own in `XL24-A32NX.lua`, in the C172 pads' pattern: digit, back, clear and enter functions that send `K:XPNDR_SET` with the Bco16 code (the event the panel itself uses), an entry readout (`X:` internal variable) and an ENT key at xpdr 4,8; not built | FBW-ATC-GAUGE, SDK-RADE; README 2.1.1 |
| MODE (A-7) | The selector moves but STATE does not follow | MODE becomes a readout (command none); record what STATE shows | FBW-ATC-XML |
| TCAS, TRAFFIC (A-14) | The key reads 0 while the cockpit knob is moved | Read (and write) the upper-case names `L:A32NX_SWITCH_TCAS_POSITION` / `L:A32NX_SWITCH_TCAS_TRAFFIC_POSITION` of the Flight Deck API; if a write does not move the knob: readout only | FBW-API, FBW-ATC-XML |
| IDENT (A-18) | The key never lights | A K6 Simple Button with the same command (no light) | SDK-RADV, FBW-ATC-XML |
| ALT RPTG, MODE, TCAS, TRAFFIC (A-5) | Writing the L-Var does not move the switch or knob | That key becomes a readout (command none), same read | FBW-API, FBW-ATC-XML |
| VHF1 / VHF2 look (A-15) | A key with no image looks wrong while the other radio is selected | A Lua function per key returning 1 or 0 as its read (a later change) | FBW-RMP-BASE |

## How to test

Run [tests/manual-checklist.md](../tests/manual-checklist.md), section "Phase 4: A32NX radio and transponder
pages (P4-4)", after the P4-1 section's "Before you start" and "Import" steps. As on the other pages, check
both directions: press a key and watch the cockpit, then **work the control in the cockpit with the mouse and
check that the key follows without a key being pressed.** Record the knob step (8.33 or 25 kHz), what VHF1
shows while VHF2 is selected, what STATE shows in each mode, how long IDENT stays lit, and whether the TCAS
keys follow the cockpit knobs.

## When it passes

1. Any change found in the test goes into `tools/profilegen/a32nx.json`, the script and this doc; then the
   profile is regenerated (not exported from the app) and imported again, and the script installed again.
2. Fill in the "Verified" column of the rows in aircraft-mappings.md ("FlyByWire A32NX radio and transponder
   pages (P4-4)") with the date, sim version and A32NX version, for each function that passed; mark a row
   "does not work" where a key failed.

## Sources

FlyByWire sources: the flybywiresim/aircraft repository at the tag v2024.1.0 (the MSFS 2024 Stable release)
unless master is named, and FlyByWire's docs site, read 2026-11-15 and 2026-11-16. The tags FBW-IE and
FBW-REL are the ones of [phase4-a32nx.md](phase4-a32nx.md), "Sources"; SDK-RADE and SDK-RADV the ones of
[phase3-transponder.md](phase3-transponder.md) and [phase2-com1-pad.md](phase2-com1-pad.md), "Sources".

| Tag | Source |
|---|---|
| FBW-RMP-VHF | `fbw-a32nx/src/systems/instruments/src/RMP/Components/VhfRadioPanel.tsx`, https://raw.githubusercontent.com/flybywiresim/aircraft/v2024.1.0/fbw-a32nx/src/systems/instruments/src/RMP/Components/VhfRadioPanel.tsx (also read at master, same lines): each window reads `COM ACTIVE FREQUENCY:${transceiver}` (Hz) and `COM STANDBY FREQUENCY:${transceiver}`, except RMP L with VHF2 or VHF3 (and RMP R with VHF1 or VHF3), whose standby is `L:A32NX_RMP_${side}_VHF${transceiver}_STANDBY_FREQUENCY`; the transfer press `A32NX_RMP_${props.side}_TRANSFER_BUTTON_PRESSED` |
| FBW-RMP-STBY | `.../RMP/Components/StandbyFrequency.tsx`, https://raw.githubusercontent.com/flybywiresim/aircraft/v2024.1.0/fbw-a32nx/src/systems/instruments/src/RMP/Components/StandbyFrequency.tsx: the four knob events `A32NX_RMP_${props.side}_OUTER_KNOB_TURNED_CLOCKWISE` (and `_ANTICLOCKWISE`, `INNER_...`), "newInteger = Utils.Clamp(integer, 118, 136);", spacing 8.33 or 25 from `RMP_VHF_SPACING_25KHZ` |
| FBW-RMP-BASE | `.../RMP/Components/BaseRadioPanels.tsx`, https://raw.githubusercontent.com/flybywiresim/aircraft/v2024.1.0/fbw-a32nx/src/systems/instruments/src/RMP/Components/BaseRadioPanels.tsx: `L:A32NX_RMP_${props.side}_SELECTED_MODE` (1 VHF1, 2 VHF2, 3 VHF3, 6 to 10 the NAV modes), the power condition `L:A32NX_ELEC_DC_ESS_BUS_IS_POWERED` (side L) and the toggle switch, the VHF1/VHF2/VHF3 press events |
| FBW-RMP-XML | `fbw-a32nx/src/behavior/src/A32NX_Interior_RMP.xml`, https://raw.githubusercontent.com/flybywiresim/aircraft/v2024.1.0/fbw-a32nx/src/behavior/src/A32NX_Interior_RMP.xml: what the cockpit's RMP controls send (`(>H:A32NX_RMP_#SIDE#_#BASE_NAME#_BUTTON_PRESSED)`, `_TRANSFER_BUTTON_PRESSED`, `_OUTER_KNOB_TURNED_CLOCKWISE` and the others, `(>H:A32NX_RMP_#SIDE#_TOGGLE_SWITCH)`), the switch L-Var `A32NX_RMP_#SIDE#_TOGGLE_SWITCH`, the VHF key light, VHF3 set to data at start, the SEL light (`@todo`) |
| FBW-ATC-XML | `fbw-a32nx/src/behavior/src/A32NX_Interior_ATC.xml`, https://raw.githubusercontent.com/flybywiresim/aircraft/v2024.1.0/fbw-a32nx/src/behavior/src/A32NX_Interior_ATC.xml: the mode selector writes `L:A32NX_TRANSPONDER_MODE` (0 STBY, 1 AUTO, 2 ON) and runs `UPDATE_TRANSPONDER_STATE`, which writes `(A:TRANSPONDER STATE:1, number)` (also from `ASOBO_GT_Update`); ALT RPTG writes `L:A32NX_SWITCH_ATC_ALT`; IDENT `(K:XPNDR_IDENT_ON, number)`; the keypad `(>H:#EVENT_NAME#)` with `A320_Neo_ATC` and `_BTN_0` to `_BTN_7`, `_BTN_CLR`; the TCAS knobs `A32NX_SWITCH_TCAS_Position` (3 positions) and `A32NX_SWITCH_TCAS_Traffic_Position` (4) |
| FBW-ATC-GAUGE | `fbw-a32nx/src/systems/instruments/src/ATC/index.tsx`, https://raw.githubusercontent.com/flybywiresim/aircraft/v2024.1.0/fbw-a32nx/src/systems/instruments/src/ATC/index.tsx: "useSplitSimVar('TRANSPONDER CODE:1', 'Bco16', 'K:XPNDR_SET', 'Bco16')"; the keypad events; the code set on the fourth digit; CLR; "setDisplayResetTimer(7);"; XPDR 1 powered by the AC ESS SHED bus |
| FBW-PILOT-RMP | FlyByWire pilot's corner, RMP, https://docs.flybywiresim.com/pilots-corner/a32nx/a32nx-briefing/flight-deck/pedestal/rmp/: "The selected key shows a green monitor light."; only VHF1 to VHF3 available |
| FBW-PILOT-ATC | FlyByWire pilot's corner, ATC-TCAS, https://docs.flybywiresim.com/pilots-corner/a32nx/a32nx-briefing/flight-deck/pedestal/atc-tcas/: "As long as the four figures of the new code are not entirely written, the previous code remains."; only XPDR 1 available |
| FBW-BEGIN | FlyByWire beginner guide, "Preparing the MCDU", section "Entering Squawk Code", https://docs.flybywiresim.com/pilots-corner/a32nx/a32nx-beginner-guide/preparing-mcdu/: "To clear the current code, double press the CLR button.", then "Enter your assigned code using the keypad." (FBW-ATC-GAUGE: the panel takes digits only while an entry is open) |
| FBW-REACT | `fbw-common/src/systems/instruments/src/react/simVars.tsx`, https://raw.githubusercontent.com/flybywiresim/aircraft/v2024.1.0/fbw-common/src/systems/instruments/src/react/simVars.tsx: `useInteractionSimVar`, which the RMP uses for its ON/OFF switch (FBW-RMP-BASE), is for a SimVar that "the XML updates" and then "emits an H event" (its own example is the RMP toggle switch); on that H-event it only reads the SimVar again, and it reads it every 500 ms "To handle the SimVar change itself through some external means, like third-party plugin or cockpit hardware" |
| FBW-SIMVARS | `fbw-a32nx/docs/a320-simvars.md`, https://raw.githubusercontent.com/flybywiresim/aircraft/master/fbw-a32nx/docs/a320-simvars.md (master): "ATC (ATA 34)" (`A32NX_TRANSPONDER_MODE`, `A32NX_SWITCH_ATC_ALT`, `A32NX_SWITCH_TCAS_Position` and `A32NX_SWITCH_TCAS_Traffic_Position`, both "Read-Only"), the RMP entries (`A32NX_RMP_L_TOGGLE_SWITCH`, `A32NX_RMP_L_SELECTED_MODE`, `A32NX_RMP_L_VHF2_STANDBY`) |
| FBW-API | FlyByWire Flight Deck API, https://docs.flybywiresim.com/aircraft/a32nx/a32nx-api/a32nx-flightdeck-api/: "Pedestal > RMP" (COM active and standby frequency, RMP MODE 0..3, RMP ON/OFF R/W) and "Pedestal > ATC-TCAS" (ATC MODE, ALT RPTG R/W, SQUAWK `TRANSPONDER CODE:1`, IDENT `XPNDR_IDENT_ON`, the TCAS rows with their labels swapped and upper-case names) |
| FBW-IE | as phase4-a32nx.md: FlyByWire input events only for the ECAM control panel and NAV & LOGO |
| FBW-REL | as phase4-a32nx.md (https://docs.flybywiresim.com/release-notes/a32nx/v2024010/) |
| SDK-RADE | MSFS 2024 SDK, Aircraft Radio Navigation Events, https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-radio-navigation-events/: `XPNDR_IDENT_ON` "After 18 seconds it will disable automatically.", `XPNDR_SET` "[0]: Frequency value (Bco16 encoded)" |
| SDK-RADV | MSFS 2024 SDK, Radio Navigation Variables, https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-radio-navigation-variables/: `TRANSPONDER CODE` (Bco16), `TRANSPONDER STATE` (0 Off, 1 Standby, 2 Test, 3 On, 4 Alt, 5 Ground), `TRANSPONDER IDENT` (Bool), `COM ACTIVE FREQUENCY` |
| README | PilotsDeck README, https://github.com/Fragtality/PilotsDeck/blob/master/README.md: 2.1 (long press, Second command), 2.1.1 (HVAR "with or without preceding `H:`", "can't be read"; AVAR `(A:Name:Index, Unit)`; LVAR; LUAFUNC "When you use a Lua Function as Variable Address, the Plugin will use the Value returned"), 2.2.2 (Format, Decode BCD), 3.5.1 (`SimVar`, `SimRead`, `SimWrite`) |
| PD-PI | as [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md), "Sources": the installed plugin's `Plugin\PI\js\pi-Common.js`, `type == 8 //HVar` (command type 8 is H-Var) |
