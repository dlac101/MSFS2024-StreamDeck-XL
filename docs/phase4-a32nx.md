# Phase 4: FlyByWire A32NX profile (main, FCU and OVHD pages)

**Status: generated, not yet sim-tested.** The profile `MSFS2024 A32NX` and its Lua script are in the
package, but nothing has been tried in the app or the sim yet, and the A32NX is not yet installed on this PC
(see "Install status"). Every name below is recorded as "Unverified" in
[aircraft-mappings.md](aircraft-mappings.md) ("FlyByWire A32NX (MSFS 2024)") until the checks in
[tests/manual-checklist.md](../tests/manual-checklist.md), section "Phase 4: A32NX profile (P4-1)", pass.

Goal: a second profile, for the **FlyByWire A32NX** (the Phase 4 airliner), generated the same way as the
C172 G1000 profile: a main page and two child pages, **FCU** (the autopilot panel) and **OVHD** (exterior
lights, signs, batteries, external power, APU). Every readout and every key light reads the aircraft's own
state; no key assumes its press worked.

The profile is the file `pilotsdeck/MSFS2024-XL/_Package/Profiles/MSFS2024 A32NX.streamDeckProfile`,
generated in the repo by `tools/profilegen/generate.py` from `tools/profilegen/a32nx.json`. The tables below
are the reference for what each key holds; `tools/profilegen/check.py tools/profilegen/a32nx.json` compares
the profile with the "Key table", "Key table: fcu" and "Key table: ovhd" sections key by key.

Nothing on these pages uses keyboard bindings, vJoy or anything tied to a controller: the keys send
SimConnect events (K-events, including FlyByWire's `A32NX.*` custom events), write L-Vars or one input event
(B-Var), and read L-Vars and SimVars, so they work the same with the Xbox Elite controller and the
T.16000M + TWCS.

## Install status

- **The A32NX is not installed on this PC yet** (checked 2026-11-14, read only): the MSFS 2024 package
  folders hold no FlyByWire package, and PilotsDeck has never seen an A32NX flight. The FlyByWire Installer
  is in `A:\FS2024 Stuff`; you run it yourself (Stable, v2024.1.0 or later, MSFS 2024 selected in its
  header).
- **FlyByWire supports MSFS 2024** (FBW-REL, "FS2024 A32NX Stable Release v2024.1.0"): "The aircraft is now
  officially compatible with MSFS 2024." and "Please note that this is not yet a native 2024 package."
  FlyByWire ships separate MSFS 2020 and MSFS 2024 releases (FBW-NOTAM).
- **Which API:** FlyByWire calls input events "the stable cockpit API" and asks for them where one exists
  (FBW-REL). Only the ECAM control panel and the NAV & LOGO switch have input events (FBW-IE); everything else
  here uses FlyByWire's L-Vars and custom events (FBW-SIMVARS, FBW-EVENTS, FBW-API). The FCU keys use the
  `A32NX_FCU_AFS_DISPLAY_*`, `A32NX_FCU_*_LIGHT_ON` and `A32NX_FCU_EFIS_*` L-Vars, not the legacy FCU L-Vars
  that FlyByWire lists as deprecated (FBW-SIMVARS, FBW-REL).
- The FCU and EFIS keys are the **Captain's side** (`EFIS_L`): FD, LS, baro and ND.

## Layout: main

Positions are **row,column**, 1-based, row 1 at the top. Folder keys end in `>`. Reserved keys are in brackets.

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | AP1 | AP2 | A/THR | LOC | APPR | FD | LS | FCU > |
| **Row 2** | SPD | HDG | ALT | V/S | BARO | ND MODE | ND RNG | OVHD > |
| **Row 3** | WARN | CAUT | PARK | FLAPS | GND SPLR | BRK LO | BRK MED | BRK MAX |
| **Row 4** | STROBE | BEACON | NAV LOGO | LAND L | LAND R | NOSE | SEAT BELT | [CHECKLIST] |

29 keys, 2 folder keys (FCU, OVHD), 1 reserved. The main page has no back key.

## Key table

Action names are the PilotsDeck README's: **Dynamic Button**, **Display Value**, **Simple Button**.
**Folder** = the Stream Deck app's own folder action, which opens a child page. "Empty" = no action on that
key. The kinds K1 to K9 are explained under "What each key holds"; source tags under "Sources". Command
types: `K:` = K-Var (saved as 16), `L:` = L-Var (3; the key writes its On or Off value), `B:` = B-Var (13),
`lua:` = Lua Function (14).

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | `AP1` | Dynamic Button | K1 | `K:A32NX.FCU_AP_1_PUSH` [FBW-EVENTS] | `L:A32NX_FCU_AP_1_LIGHT_ON` [FBW-SIMVARS] | On/Off image |
| 1,2 | `AP2` | Dynamic Button | K1 | `K:A32NX.FCU_AP_2_PUSH` [FBW-EVENTS] | `L:A32NX_FCU_AP_2_LIGHT_ON` [FBW-SIMVARS] | On/Off image |
| 1,3 | `A/THR` | Dynamic Button | K1 | `K:A32NX.FCU_ATHR_PUSH` [FBW-EVENTS] | `L:A32NX_FCU_ATHR_LIGHT_ON` [FBW-SIMVARS] | On/Off image |
| 1,4 | `LOC` | Dynamic Button | K1 | `K:A32NX.FCU_LOC_PUSH` [FBW-EVENTS] | `L:A32NX_FCU_LOC_LIGHT_ON` [FBW-SIMVARS] | On/Off image |
| 1,5 | `APPR` | Dynamic Button | K1 | `K:A32NX.FCU_APPR_PUSH` [FBW-EVENTS] | `L:A32NX_FCU_APPR_LIGHT_ON` [FBW-SIMVARS] | On/Off image |
| 1,6 | `FD` | Dynamic Button | K1 | `K:A32NX.FCU_EFIS_L_FD_PUSH` [FBW-EVENTS] | `L:A32NX_FCU_EFIS_L_FD_LIGHT_ON` [FBW-SIMVARS] | On/Off image |
| 1,7 | `LS` | Dynamic Button | K1 | `K:A32NX.FCU_EFIS_L_LS_PUSH` [FBW-EVENTS] | `L:A32NX_FCU_EFIS_L_LS_LIGHT_ON` [FBW-SIMVARS] | On/Off image |
| 1,8 | `FCU` | Folder | (Stream Deck) | Opens the child page **fcu** | none | Folder; the page's keys: "Key table: fcu" below |
| 2,1 | `SPD` | Display Value | K3 | `K:A32NX.FCU_SPD_PUSH` (knob push) [FBW-EVENTS] | `lua:XL24-A32NX:SPD` (the script) [README 2.1.1 LUAFUNC; FBW-SIMVARS] | Lua text: the FCU SPD/MACH window |
| 2,2 | `HDG` | Display Value | K3 | `K:A32NX.FCU_HDG_PUSH` (knob push) [FBW-EVENTS] | `lua:XL24-A32NX:HDG` (the script) [README 2.1.1 LUAFUNC; FBW-SIMVARS] | Lua text: the FCU HDG/TRK window |
| 2,3 | `ALT` | Display Value | K3 | `K:A32NX.FCU_ALT_PUSH` (knob push) [FBW-EVENTS] | `lua:XL24-A32NX:ALT` (the script) [README 2.1.1 LUAFUNC; FBW-SIMVARS] | Lua text: the FCU ALT window |
| 2,4 | `V/S` | Display Value | K3 | `K:A32NX.FCU_VS_PUSH` (knob push) [FBW-EVENTS] | `lua:XL24-A32NX:VS` (the script) [README 2.1.1 LUAFUNC; FBW-SIMVARS] | Lua text: the FCU V/S-FPA window |
| 2,5 | `BARO` | Display Value | K3 | Main `K:A32NX.FCU_EFIS_L_BARO_PUSH` (QNH), Second (long press) `K:A32NX.FCU_EFIS_L_BARO_PULL` (STD) [FBW-EVENTS, FBW-API] | `lua:XL24-A32NX:BARO` (the script) [README 2.1.1 LUAFUNC; FBW-SIMVARS, FBW-API] | Lua text: the Captain's baro window |
| 2,6 | `ND MODE` | Display Value | K7 | Main `lua:XL24-A32NX:NDMODE(1)`, Second (long press) `lua:XL24-A32NX:NDMODE(-1)` (the script writes the L-Var) [README 2.1.1 LUAFUNC, 3.5.1] | `L:A32NX_FCU_EFIS_L_EFIS_MODE` [FBW-API, FBW-SIMVARS] | Mappings `0=ILS:1=VOR:2=NAV:3=ARC:4=PLAN` |
| 2,7 | `ND RNG` | Display Value | K7 | Main `lua:XL24-A32NX:NDRANGE(1)`, Second (long press) `lua:XL24-A32NX:NDRANGE(-1)` (the script writes the L-Var) [README 2.1.1 LUAFUNC, 3.5.1] | `L:A32NX_FCU_EFIS_L_EFIS_RANGE` [FBW-API, FBW-SIMVARS] | Mappings `0=10:1=20:2=40:3=80:4=160:5=320` |
| 2,8 | `OVHD` | Folder | (Stream Deck) | Opens the child page **ovhd** | none | Folder; the page's keys: "Key table: ovhd" below |
| 3,1 | `WARN` | Dynamic Button | K2 | `L:A32NX_MASTER_WARNING`, On `0` / Off `0` (always writes 0) [FBW-API] | `L:A32NX_MASTER_WARNING` [FBW-API] | On/Off image, Special State |
| 3,2 | `CAUT` | Dynamic Button | K2 | `L:A32NX_MASTER_CAUTION`, On `0` / Off `0` (always writes 0) [FBW-API] | `L:A32NX_MASTER_CAUTION` [FBW-API] | On/Off image, Special State |
| 3,3 | `PARK` | Dynamic Button | K2 | `L:A32NX_PARK_BRAKE_LEVER_POS`, On `1` / Off `0` [FBW-API] | `L:A32NX_PARK_BRAKE_LEVER_POS` [FBW-API, FBW-SIMVARS] | On/Off image, Special State |
| 3,4 | `FLAPS` | Display Value | T3 (FLAPS form) | Main `K:FLAPS_INCR`, Second (long press) `K:FLAPS_DECR` [FBW-API] | `L:A32NX_FLAPS_HANDLE_INDEX` [FBW-API, FBW-SIMVARS] | Mappings `0=UP:1=1:2=2:3=3:4=FULL` |
| 3,5 | `GND SPLR` | Dynamic Button | K1 | `K:SPOILERS_ARM_TOGGLE` [FBW-API] | `L:A32NX_SPOILERS_ARMED` [FBW-API, FBW-SIMVARS] | On/Off image |
| 3,6 | `BRK LO` | Dynamic Button | K1 | `K:A32NX.AUTOBRAKE_BUTTON_LO` [FBW-EVENTS, FBW-API] | `L:A32NX_AUTOBRAKES_ARMED_MODE` [FBW-API] | On/Off image: On `1`, Off `0` |
| 3,7 | `BRK MED` | Dynamic Button | K1 | `K:A32NX.AUTOBRAKE_BUTTON_MED` [FBW-EVENTS, FBW-API] | `L:A32NX_AUTOBRAKES_ARMED_MODE` [FBW-API] | On/Off image: On `2`, Off `0` |
| 3,8 | `BRK MAX` | Dynamic Button | K1 | `K:A32NX.AUTOBRAKE_BUTTON_MAX` [FBW-EVENTS, FBW-API] | `L:A32NX_AUTOBRAKES_ARMED_MODE` [FBW-API] | On/Off image: On `3`, Off `0` |
| 4,1 | `STROBE` | Display Value | K5 | `L:LIGHTING_STROBE_0`, On `0` / Off `1` (ON / AUTO) [FBW-API] | `L:LIGHTING_STROBE_0` [FBW-API] | Mappings `0=ON:1=AUTO:2=OFF` |
| 4,2 | `BEACON` | Dynamic Button | K1 | `K:TOGGLE_BEACON_LIGHTS` [SDK-ELECE] | `(A:LIGHT BEACON, Bool)` [FBW-API] | On/Off image |
| 4,3 | `NAV LOGO` | Display Value | K8 | `B:A32NX_OVH_LIGHTS_NAV_LOGO_SW`, On `1` / Off `0` (SYS 1 / OFF) [FBW-IE, FBW-REL; README 2.1.1 BVAR] | `B:A32NX_OVH_LIGHTS_NAV_LOGO_SW` [FBW-IE] | Mappings `0=OFF:1=SYS 1:2=SYS 2` |
| 4,4 | `LAND L` | Display Value | K5 | `L:LIGHTING_LANDING_2`, On `0` / Off `2` (ON / RETRACT) [FBW-API] | `L:LIGHTING_LANDING_2` [FBW-API] | Mappings `0=ON:1=OFF:2=RETR` |
| 4,5 | `LAND R` | Display Value | K5 | `L:LIGHTING_LANDING_3`, On `0` / Off `2` (ON / RETRACT) [FBW-API] | `L:LIGHTING_LANDING_3` [FBW-API] | Mappings `0=ON:1=OFF:2=RETR` |
| 4,6 | `NOSE` | Display Value | K5 | `L:LIGHTING_LANDING_1`, On `0` / Off `1` (T.O. / TAXI) [FBW-API] | `L:LIGHTING_LANDING_1` [FBW-API] | Mappings `0=T.O.:1=TAXI:2=OFF` |
| 4,7 | `SEAT BELT` | Dynamic Button | K1 | `K:CABIN_SEATBELTS_ALERT_SWITCH_TOGGLE` [FBW-API] | `(A:CABIN SEATBELTS ALERT SWITCH, Bool)` [FBW-API] | On/Off image |
| 4,8 | | Empty | | | | Reserved: CHECKLIST (Phase 5) |

What the main page keys do:
- **AP1, AP2, A/THR, LOC, APPR, FD, LS** press the FCU and EFIS buttons and light from the button's own light
  L-Var.
- **SPD, HDG, ALT, V/S, BARO** show the FCU windows as text (see "The script"). A press pushes the knob
  (managed mode; for BARO: QNH); a **long press** on BARO (hold at least 0.5 s) pulls it (STD). The FCU page
  has the turn and pull keys.
- **ND MODE, ND RNG**: press = one step clockwise (ILS > VOR > NAV > ARC > PLAN; 10 > 20 > ... > 320), long
  press = one step back. They stop at the ends. The key shows the ND setting the aircraft reads.
- **WARN, CAUT** light while the MASTER WARNING or MASTER CAUTION light is on; a press writes 0 to clear it
  (FlyByWire documents no press event for these lights: FBW-API lists the L-Vars as read/write).
- **PARK** sets or releases the parking brake lever; **FLAPS**: press = one notch down (`K:FLAPS_INCR`),
  long press = one notch up (`K:FLAPS_DECR`), as on the C172 profile.
- **BRK LO, BRK MED, BRK MAX** press the autobrake buttons; each lights when that mode is armed.
- **STROBE** toggles ON and AUTO, **LAND L/R** ON and RETRACT, **NOSE** T.O. and TAXI; each shows all three
  positions (the switch's third position is set in the cockpit). **NAV LOGO** toggles SYS 1 and OFF and
  shows OFF, SYS 1 or SYS 2.

## Layout: fcu

1,1 is the back key (it returns to the main page), as on every child page. The knobs are columns: a `+` key
above the readout above a `-` key, and the knob's PULL key at the bottom: SPD column 2, HDG column 3, ALT
column 6, V/S column 7, baro column 8.

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | SPD+ | HDG+ | SPD/MACH | TRK/FPA | ALT+ | V/S+ | BARO+ |
| **Row 2** | FD | SPD | HDG | AP1 | AP2 | ALT | V/S | BARO |
| **Row 3** | LS | SPD- | HDG- | A/THR | EXPED | ALT- | V/S- | BARO- |
| **Row 4** | ALT STEP | SPD PULL | HDG PULL | LOC | APPR | ALT PULL | V/S PULL | hPa/inHg |

31 keys and the back key; no empty position.

## Key table: fcu

Forms as in "Key table". **Back** = the Stream Deck app's back key (`backtoparent`), added by the generator.

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to the main page | none | Back key |
| 1,2 | `SPD+` | Simple Button | K6 | `K:A32NX.FCU_SPD_INC` [FBW-EVENTS] | none (SPD at 2,2 shows the result) | fixed image |
| 1,3 | `HDG+` | Simple Button | K6 | `K:A32NX.FCU_HDG_INC` [FBW-EVENTS] | none (HDG at 2,3 shows the result) | fixed image |
| 1,4 | `SPD/MACH` | Display Value | K4 | `K:A32NX.FCU_SPD_MACH_TOGGLE_PUSH` [FBW-EVENTS] | `L:A32NX_FCU_AFS_DISPLAY_MACH_MODE` [FBW-SIMVARS] | Mappings `0=SPD:1=MACH` |
| 1,5 | `TRK/FPA` | Display Value | K4 | `K:A32NX.FCU_TRK_FPA_TOGGLE_PUSH` [FBW-EVENTS] | `L:A32NX_FCU_AFS_DISPLAY_TRK_FPA_MODE` [FBW-SIMVARS] | Mappings `0=HDG VS:1=TRK FPA` |
| 1,6 | `ALT+` | Simple Button | K6 | `K:A32NX.FCU_ALT_INC` (no parameter: the ALT STEP setting) [FBW-EVENTS] | none (ALT at 2,6 shows the result) | fixed image |
| 1,7 | `V/S+` | Simple Button | K6 | `K:A32NX.FCU_VS_INC` [FBW-EVENTS] | none (V/S at 2,7 shows the result) | fixed image |
| 1,8 | `BARO+` | Simple Button | K6 | `K:A32NX.FCU_EFIS_L_BARO_INC` [FBW-EVENTS, FBW-API] | none (BARO at 2,8 shows the result) | fixed image |
| 2,1 | `FD` | Dynamic Button | K1 | `K:A32NX.FCU_EFIS_L_FD_PUSH` [FBW-EVENTS] | `L:A32NX_FCU_EFIS_L_FD_LIGHT_ON` [FBW-SIMVARS] | On/Off image |
| 2,2 | `SPD` | Display Value | K3 | `K:A32NX.FCU_SPD_PUSH` (knob push) [FBW-EVENTS] | `lua:XL24-A32NX:SPD` (the script) [README 2.1.1 LUAFUNC; FBW-SIMVARS] | Lua text: the FCU SPD/MACH window |
| 2,3 | `HDG` | Display Value | K3 | `K:A32NX.FCU_HDG_PUSH` (knob push) [FBW-EVENTS] | `lua:XL24-A32NX:HDG` (the script) [README 2.1.1 LUAFUNC; FBW-SIMVARS] | Lua text: the FCU HDG/TRK window |
| 2,4 | `AP1` | Dynamic Button | K1 | `K:A32NX.FCU_AP_1_PUSH` [FBW-EVENTS] | `L:A32NX_FCU_AP_1_LIGHT_ON` [FBW-SIMVARS] | On/Off image |
| 2,5 | `AP2` | Dynamic Button | K1 | `K:A32NX.FCU_AP_2_PUSH` [FBW-EVENTS] | `L:A32NX_FCU_AP_2_LIGHT_ON` [FBW-SIMVARS] | On/Off image |
| 2,6 | `ALT` | Display Value | K3 | `K:A32NX.FCU_ALT_PUSH` (knob push) [FBW-EVENTS] | `lua:XL24-A32NX:ALT` (the script) [README 2.1.1 LUAFUNC; FBW-SIMVARS] | Lua text: the FCU ALT window |
| 2,7 | `V/S` | Display Value | K3 | `K:A32NX.FCU_VS_PUSH` (knob push) [FBW-EVENTS] | `lua:XL24-A32NX:VS` (the script) [README 2.1.1 LUAFUNC; FBW-SIMVARS] | Lua text: the FCU V/S-FPA window |
| 2,8 | `BARO` | Display Value | K3 | Main `K:A32NX.FCU_EFIS_L_BARO_PUSH` (QNH), Second (long press) `K:A32NX.FCU_EFIS_L_BARO_PULL` (STD) [FBW-EVENTS, FBW-API] | `lua:XL24-A32NX:BARO` (the script) [README 2.1.1 LUAFUNC; FBW-SIMVARS, FBW-API] | Lua text: the Captain's baro window |
| 3,1 | `LS` | Dynamic Button | K1 | `K:A32NX.FCU_EFIS_L_LS_PUSH` [FBW-EVENTS] | `L:A32NX_FCU_EFIS_L_LS_LIGHT_ON` [FBW-SIMVARS] | On/Off image |
| 3,2 | `SPD-` | Simple Button | K6 | `K:A32NX.FCU_SPD_DEC` [FBW-EVENTS] | none (SPD at 2,2 shows the result) | fixed image |
| 3,3 | `HDG-` | Simple Button | K6 | `K:A32NX.FCU_HDG_DEC` [FBW-EVENTS] | none (HDG at 2,3 shows the result) | fixed image |
| 3,4 | `A/THR` | Dynamic Button | K1 | `K:A32NX.FCU_ATHR_PUSH` [FBW-EVENTS] | `L:A32NX_FCU_ATHR_LIGHT_ON` [FBW-SIMVARS] | On/Off image |
| 3,5 | `EXPED` | Dynamic Button | K1 | `K:A32NX.FCU_EXPED_PUSH` [FBW-EVENTS] | `L:A32NX_FCU_EXPED_LIGHT_ON` [FBW-SIMVARS] | On/Off image |
| 3,6 | `ALT-` | Simple Button | K6 | `K:A32NX.FCU_ALT_DEC` (no parameter: the ALT STEP setting) [FBW-EVENTS] | none (ALT at 2,6 shows the result) | fixed image |
| 3,7 | `V/S-` | Simple Button | K6 | `K:A32NX.FCU_VS_DEC` [FBW-EVENTS] | none (V/S at 2,7 shows the result) | fixed image |
| 3,8 | `BARO-` | Simple Button | K6 | `K:A32NX.FCU_EFIS_L_BARO_DEC` [FBW-EVENTS, FBW-API] | none (BARO at 2,8 shows the result) | fixed image |
| 4,1 | `ALT STEP` | Display Value | K4 | `K:A32NX.FCU_ALT_INCREMENT_TOGGLE` [FBW-EVENTS] | `L:A32NX_FCU_ALT_INCREMENT_1000` [FBW-SIMVARS] | Mappings `0=100:1=1000` |
| 4,2 | `SPD PULL` | Simple Button | K6 | `K:A32NX.FCU_SPD_PULL` [FBW-EVENTS] | none (SPD at 2,2 shows the result) | fixed image |
| 4,3 | `HDG PULL` | Simple Button | K6 | `K:A32NX.FCU_HDG_PULL` [FBW-EVENTS] | none (HDG at 2,3 shows the result) | fixed image |
| 4,4 | `LOC` | Dynamic Button | K1 | `K:A32NX.FCU_LOC_PUSH` [FBW-EVENTS] | `L:A32NX_FCU_LOC_LIGHT_ON` [FBW-SIMVARS] | On/Off image |
| 4,5 | `APPR` | Dynamic Button | K1 | `K:A32NX.FCU_APPR_PUSH` [FBW-EVENTS] | `L:A32NX_FCU_APPR_LIGHT_ON` [FBW-SIMVARS] | On/Off image |
| 4,6 | `ALT PULL` | Simple Button | K6 | `K:A32NX.FCU_ALT_PULL` [FBW-EVENTS] | none (ALT at 2,6 shows the result) | fixed image |
| 4,7 | `V/S PULL` | Simple Button | K6 | `K:A32NX.FCU_VS_PULL` [FBW-EVENTS] | none (V/S at 2,7 shows the result) | fixed image |
| 4,8 | `hPa/inHg` | Display Value | K5 | `L:A32NX_FCU_EFIS_L_BARO_IS_INHG`, On `1` / Off `0` (inHg / hPa) [FBW-API] | `L:A32NX_FCU_EFIS_L_BARO_IS_INHG` [FBW-API, FBW-SIMVARS] | Mappings `0=hPa:1=inHg` |

What the FCU page keys do: each `+` / `-` key is one knob detent per press (ALT by 100 or 1000 ft, as ALT
STEP shows); each PULL key pulls its knob (selected mode); SPD/MACH, TRK/FPA and ALT STEP press the FCU's own
buttons and show the mode the aircraft reads; hPa/inHg writes the unit selector (inHg / hPa) and shows it.
The other keys are the main page's.

## Layout: ovhd

1,1 is the back key (it returns to the main page).

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | STROBE | BEACON | WING | NAV LOGO | RWY TURN | LAND L | LAND R |
| **Row 2** | NOSE | SEAT BELT | NO SMOKE | | | | | |
| **Row 3** | BAT 1 | BAT 2 | EXT PWR | APU MSTR | APU START | APU AVAIL | | |
| **Row 4** | | | | | | | | |

16 keys, the back key and 15 empty positions (reserved for a later unit: transponder and TCAS, EMER EXIT
lights and others).

## Key table: ovhd

Forms as in "Key table".

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
| 2,4 | | Empty | | | | Reserved (a later unit) |
| 2,5 | | Empty | | | | Reserved (a later unit) |
| 2,6 | | Empty | | | | Reserved (a later unit) |
| 2,7 | | Empty | | | | Reserved (a later unit) |
| 2,8 | | Empty | | | | Reserved (a later unit) |
| 3,1 | `BAT 1` | Dynamic Button | K2 | `L:A32NX_OVHD_ELEC_BAT_1_PB_IS_AUTO`, On `1` / Off `0` (AUTO / OFF) [FBW-API] | `L:A32NX_OVHD_ELEC_BAT_1_PB_IS_AUTO` [FBW-API, FBW-SIMVARS] | On/Off image, Special State |
| 3,2 | `BAT 2` | Dynamic Button | K2 | `L:A32NX_OVHD_ELEC_BAT_2_PB_IS_AUTO`, On `1` / Off `0` (AUTO / OFF) [FBW-API] | `L:A32NX_OVHD_ELEC_BAT_2_PB_IS_AUTO` [FBW-API, FBW-SIMVARS] | On/Off image, Special State |
| 3,3 | `EXT PWR` | Dynamic Button | K2 | `L:A32NX_OVHD_ELEC_EXT_PWR_PB_IS_ON`, On `1` / Off `0` [FBW-API] | `L:A32NX_OVHD_ELEC_EXT_PWR_PB_IS_ON` [FBW-API] | On/Off image, Special State |
| 3,4 | `APU MSTR` | Dynamic Button | K2 | `L:A32NX_OVHD_APU_MASTER_SW_PB_IS_ON`, On `1` / Off `0` [FBW-API] | `L:A32NX_OVHD_APU_MASTER_SW_PB_IS_ON` [FBW-API, FBW-SIMVARS] | On/Off image, Special State |
| 3,5 | `APU START` | Dynamic Button | K2 | `L:A32NX_OVHD_APU_START_PB_IS_ON`, On `1` / Off `1` (always writes 1) [FBW-API] | `L:A32NX_OVHD_APU_START_PB_IS_ON` [FBW-API, FBW-SIMVARS] | On/Off image, Special State |
| 3,6 | `APU AVAIL` | Display Value | K9 | none | `L:A32NX_OVHD_APU_START_PB_IS_AVAILABLE` [FBW-API, FBW-SIMVARS] | Mappings `0=---:1=AVAIL` |
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

What the OVHD page keys do: STROBE, BEACON, NAV LOGO, LAND L/R, NOSE and SEAT BELT are the main page's keys.
**WING** toggles the wing lights; **RWY TURN** toggles both runway turn-off light circuits (21 left, 22 right)
and lights from the left one; **NO SMOKE** toggles ON and AUTO and shows all three positions; **BAT 1, BAT 2**
switch the battery pushbuttons between AUTO (lit) and OFF; **EXT PWR** and **APU MSTR** switch their
pushbuttons; **APU START** always writes 1 (start) and lights while the START pushbutton is on; **APU AVAIL**
shows `AVAIL` when the APU is available.

## The script

[`pilotsdeck/MSFS2024-XL/_Package/Scripts/XL24-A32NX.lua`](../pilotsdeck/MSFS2024-XL/_Package/Scripts/XL24-A32NX.lua),
a standard script (README 3.5.1). It uses only `SimVar`, `SimRead` and `SimWrite`. PilotsDeck runs a Lua
function used as a key's Value Address on every process cycle and shows what it returns (README 2.1.1
LUAFUNC: functions can be used "as Variable or Command"); `lua:XL24-A32NX:SPD` runs `SPD()` (PilotsDeck adds
the `()`).

| Function | Returns (text) or does | Reads |
|---|---|---|
| `SPD()` | `---` when dashed; Mach mode: `.78` (two decimals, no leading 0); else the speed as `250`; ` *` appended when the managed dot is on | `L:A32NX_FCU_AFS_DISPLAY_SPD_MACH_VALUE`, `_SPD_MACH_DASHES`, `_SPD_MACH_MANAGED`, `L:A32NX_FCU_AFS_DISPLAY_MACH_MODE` |
| `HDG()` | `---` when dashed, else `090`; ` *` when the managed dot is on | `L:A32NX_FCU_AFS_DISPLAY_HDG_TRK_VALUE`, `_HDG_TRK_DASHES`, `_HDG_TRK_MANAGED` |
| `ALT()` | `05000`; ` *` when the level change managed dot is on | `L:A32NX_FCU_AFS_DISPLAY_ALT_VALUE`, `L:A32NX_FCU_AFS_DISPLAY_LVL_CH_MANAGED` |
| `VS()` | dashed: `-----` (V/S mode) or `--.-` (FPA mode); V/S mode `+0700` / `-1500` (ft/min); FPA mode `-3.0` (degrees) | `L:A32NX_FCU_AFS_DISPLAY_VS_FPA_VALUE`, `_VS_FPA_DASHES`, `L:A32NX_FCU_AFS_DISPLAY_TRK_FPA_MODE` |
| `BARO()` | `STD`, or `1013` (hPa), or `29.92` (inHg), as the baro value mode says | `L:A32NX_FCU_EFIS_L_DISPLAY_BARO_VALUE`, `L:A32NX_FCU_EFIS_L_DISPLAY_BARO_VALUE_MODE` (0 STD, 1 hPa, 2 inHg) |
| `NDMODE(step)` | reads the ND mode, adds `step` (1 or -1), keeps it in 0..4 and writes it | `L:A32NX_FCU_EFIS_L_EFIS_MODE` |
| `NDRANGE(step)` | the same for the ND range, 0..5 | `L:A32NX_FCU_EFIS_L_EFIS_RANGE` |

- All five readouts return an empty text when `L:A32NX_FCU_HEALTHY` is not 1 ("If the FCU is healthy in one or
  more channels", FBW-SIMVARS): with no A32NX loaded, or the FCU unpowered, the readout keys are blank, as the
  real FCU windows. `NDMODE` and `NDRANGE` do nothing then.
- The managed marker is ` *` (plain ASCII; the real FCU shows a dot).
- Units (FBW-API ranges, not yet seen in the sim): speed in knots, Mach as a decimal (0.1..0.99); V/S in
  ft/min, FPA in degrees (-9.9..9.9); altitude in feet (100..49000); baro in hPa or inHg.

## What each key holds

Every key is a copy of a real saved key with only these fields changed (the generator does this). `p1:c,r` =
that key of the Phase 1 export; `simple_button` = the templates.json entry, as on the C172 profile
([phase2-main-page.md](phase2-main-page.md), "What each key holds", T1 to T5).

| Kind | Action, copied from | Fields set |
|---|---|---|
| K1 K-event button | Dynamic Button, the Phase 1 AP key (`p1:3,0`, T2) | Command Address (`K:`), Value Address; On State only where it is not `1` (BRK MED `2`, BRK MAX `3`) |
| K2 L-Var switch | Dynamic Button, the Phase 1 BAT key (`p1:0,0`, T1) | Command Type L-Var (`ActionType` 3), Value and Command Address (the same `L:`), On / Off Value where not `1` / `0`, Special State on (any value) |
| K3 FCU readout | Display Value, the Phase 1 HDG key (`p1:2,0`, T3) | Value Address `lua:XL24-A32NX:<function>`, Format empty, Command Type K-Var, Command Address (the knob push); BARO also long press on with a K-Var Second Command (the pull) |
| K4 mode readout | Display Value (`p1:2,0`) | Value Address (`L:`), Format empty, Mappings, Command Type K-Var, Command Address |
| K5 L-Var selector | Display Value (`p1:2,0`) | Value Address and Command Address (the same `L:`; the template's command type is already L-Var, 3), Format empty, Mappings, On and Off Value |
| K6 K-event press | Simple Button (`simple_button`, states from `p1:3,0`, T5) | Command Type K-Var, Command Address, Background `Images/Switch.png`, Draw Box off, `LinkedTitle` on |
| K7 Lua step | Display Value (`p1:2,0`) | Value Address (`L:`), Format empty, Mappings, Command Type Lua Function (14), Command Address `...(1)`, long press on, Second Command `...(-1)` |
| K8 B-Var selector | Display Value (`p1:2,0`) | Value and Command Address (the same `B:`), Command Type B-Var (13), On `1` / Off `0`, "Do not request B-Var" off, Format empty, Mappings |
| K9 readout only | Display Value (`p1:2,0`) | Value Address (`L:`), Format empty, Mappings |
| T3 (FLAPS form) | Display Value (`p1:2,0`), as the C172 FLAPS key | Value Address, Format empty, Mappings, K-Var press and long press |

Title sizes ([navigation.md](navigation.md), "Rules"): Dynamic and Simple Buttons copied from the AP key draw
their titles at 14, the ones copied from the BAT key keep 15; titles of 8 or more characters on Dynamic and
Simple Buttons are set to 13 (`GND SPLR`, `SEAT BELT`, `RWY TURN`, `APU MSTR`, `APU START`, `SPD PULL`,
`HDG PULL`, `ALT PULL`, `V/S PULL`); Display Values keep their template size (15).

PilotsDeck forms (README 2.1.1): an L-Var "with or without preceding `L:`", read as a Number; as a command
"The Plugin will toggle between these two Values" (On and Off Value). A K-Var takes up to five parameters, or
a sequence `K:A:n:K:B:m` (PD-PI line 195), as RWY TURN uses. FlyByWire's `A32NX.*` custom events are
SimConnect client events (FBW-SCI: `SimConnect_MapClientEventToSimEvent`), and PilotsDeck sends a K-Var name
unchanged to its SimConnect event manager (PD-SRC `ToolsMSFS.cs`), so `K:A32NX.FCU_SPD_PUSH` is sent as a
K-Var (type 16); the PilotsDeck README's own calculator example names `A32NX.FCU_SPD_DEC` as a custom event.
That the events arrive is an inference until the sim test.

## Import the profile

1. Install the A32NX (see "Install status") and load it once, so PilotsDeck sees it.
2. **Copy the script:** copy `pilotsdeck/MSFS2024-XL/_Package/Scripts/XL24-A32NX.lua` into the PilotsDeck
   plugin's Scripts folder,
   `%APPDATA%\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\Scripts\` (or build and install the
   package with the Profile Manager, which puts `Scripts/` files there). Without it the readouts stay blank
   and ND MODE / ND RNG do nothing. Copy it again after any change to it in the repo.
3. Back up your Stream Deck profiles ([installation.md](installation.md#back-up-existing-profiles)). A profile
   already named `MSFS2024 A32NX`: export it to the backup folder and delete it before you import (the
   Profile Manager finds profiles by name).
4. With the Stream Deck app running, double-click the file
   `pilotsdeck/MSFS2024-XL/_Package/Profiles/MSFS2024 A32NX.streamDeckProfile` (or Preferences > Profiles >
   Import), pick the **Stream Deck XL**, choose **Install**, then select **`MSFS2024 A32NX`**.
5. In PilotsDeck's Profile Manager, map the profile to the A32NX's aircraft string (from the PilotsDeck log
   after the A32NX flight loads) and record that string in aircraft-mappings.md.

The C172 profiles (`MSFS2024 C172 G1000`, `MSFS2024 C172 POC`) are not changed by this profile.

### Regenerating the profile

From the repo root (Python 3, standard library only):

```powershell
python tools/profilegen/generate.py tools/profilegen/a32nx.json
python tools/profilegen/check.py tools/profilegen/a32nx.json
```

`check.py` compares the profile with this doc's three key tables, the Phase 1 export, the templates and a
fresh build, and checks every `lua:` key against `XL24-A32NX.lua`. `--sources` adds the provenance check (as
for the C172 profile, phase2-main-page.md). The data file sets `"phase1_keys": []`: the A32NX main page holds
none of the Phase 1 keys (BAT, PARK, AP) that check.py's phase1 check compares on the C172 main page. A change
to a key goes into `tools/profilegen/a32nx.json` and this doc together; then regenerate, check and import the
new file.

## What the keys show when the A32NX isn't there

- No sim, or no flight: PilotsDeck's own idle and waiting images, as on the C172 profile.
- Another aircraft (or the A32NX not powered): the FCU readouts (SPD, HDG, ALT, V/S, BARO) are **blank**, and
  ND MODE / ND RNG presses do nothing. Every other key shows what its variable reads: an L-Var the aircraft
  doesn't have reads 0, so the AP, FD, LS, BRK, WARN, CAUT, PARK and BAT keys show off, **STROBE shows `ON`,
  LAND L/R `ON`, NOSE `T.O.`, NO SMOKE `ON`**, ND MODE `ILS`, ND RNG `10`, FLAPS `UP`, APU AVAIL `---`. That is
  the 0 of a missing variable, not the aircraft's state.
- A command the sim refuses shows PilotsDeck's alert sign on the key.
- BRK LO, MED and MAX all read the same L-Var: a key whose value is neither its On nor its Off value (for
  example BRK LO while MED is armed) draws no On or Off image, only the key background and its title
  (PilotsDeck source, `ActionSwitchDisplay.cs`); the hand test confirms it.

## Fallbacks

Use one only if the checklist shows the main route does not work, and say which one you used. None is tested.
A key that fails with no working fallback becomes readout-only (command none) or Empty, and its row in
aircraft-mappings.md says "does not work".

| Key | If it fails | Fallback | Source |
|---|---|---|---|
| Every `K:A32NX.*` key | The plugin log shows the command, the cockpit doesn't move | A Lua function per key that sends the event as calculator code, `SimCalculator("(>K:A32NX.FCU_SPD_PUSH)")` (command type Lua Function) | FBW-SCI; README 2.1.1 CALCULATOR, 3.5.1 |
| WARN, CAUT | Writing 0 doesn't clear the light (or the aural goes on) | Readout only (command none) | FBW-API, FBW-WARN |
| STROBE, LAND L/R, NOSE, NO SMOKE | Writing the `LIGHTING_*` / `XMLVAR_*` L-Var doesn't move the switch in the MSFS 2024 build | STROBE: `K:STROBES_TOGGLE` (FBW-API: ON and OFF only, no AUTO; FBW-API also lists `STROBES_SET`, `STROBES_ON`, `STROBES_OFF`); the others readout only | FBW-API |
| NAV LOGO | The B-Var command does nothing, or the key does not follow the switch (FlyByWire names `_Set`, `_Inc`, `_Dec` forms) | Record what `InputEvents.txt` lists for it, then use that form; for the readout, FlyByWire's state L-Var `L:A32NX_LIGHTS_NAV_LOGO` (FBW-REL; values not documented there) | FBW-IE, FBW-REL; README 2.1.1 BVAR |
| RWY TURN | The circuit toggles don't move the switch or the lights | Readout only | SDK-ELECE, FBW-API |
| PARK | Writing the lever L-Var doesn't move the lever | `K:PARKING_BRAKES` (the C172's verified event) | FBW-REL; aircraft-mappings.md |
| SPD/HDG/ALT/V/S/BARO show wrong scale or nothing | Mach not a decimal, FPA not in degrees, baro value mode differs | Change the format in `XL24-A32NX.lua` only (no profile change) | FBW-SIMVARS, FBW-API |

## How to test

Run [tests/manual-checklist.md](../tests/manual-checklist.md), section "Phase 4: A32NX profile (P4-1)". As on
the C172 pages, check both directions: press a key and watch the cockpit, then **move the control in the
cockpit with the mouse and check that the key follows without a key being pressed.**

## When it passes

1. Any change found in the test goes into `tools/profilegen/a32nx.json`, the script and this doc; then the
   profile is regenerated (not exported from the app) and imported again, and the script copied again.
2. Fill in the "Verified" column of the A32NX rows in aircraft-mappings.md with the date, sim version and
   A32NX version, for each function that passed; mark a row "does not work" where a key failed.

## Sources

| Tag | Source |
|---|---|
| FBW-SIMVARS | FlyByWire `fbw-a32nx/docs/a320-simvars.md`, https://github.com/flybywiresim/aircraft/blob/master/fbw-a32nx/docs/a320-simvars.md (file commit 57e2517, 2026-11-02): FCU AFS display L-Vars (`A32NX_FCU_AFS_DISPLAY_{name}_VALUE`, dashes, managed dot, Mach and TRK/FPA mode), `A32NX_FCU_{button}_LIGHT_ON`, `A32NX_FCU_EFIS_{side}_{button}_LIGHT_ON`, baro display L-Vars, `A32NX_FCU_HEALTHY`, `A32NX_FCU_ALT_INCREMENT_1000`, flaps, spoilers, APU, BAT; the Deprecated section |
| FBW-EVENTS | FlyByWire `fbw-a32nx/docs/a320-events.md`, https://github.com/flybywiresim/aircraft/blob/master/fbw-a32nx/docs/a320-events.md (file commit 0cc8a75): the `A32NX.FCU_*`, `A32NX.FCU_EFIS_L_*` and `A32NX.AUTOBRAKE_BUTTON_*` custom events |
| FBW-IE | FlyByWire `fbw-a32nx/docs/a32nx-input-events.md`, https://github.com/flybywiresim/aircraft/blob/master/fbw-a32nx/docs/a32nx-input-events.md (file commit 0296560): `A32NX_OVH_LIGHTS_NAV_LOGO_SW` ("the NAV & LOGO light switch on the overhead") |
| FBW-API | FlyByWire Flight Deck API, https://docs.flybywiresim.com/aircraft/a32nx/a32nx-api/a32nx-flightdeck-api/ (read 2026-11-14; "The below table might lag behind the current developments of the A32NX."): R/W L-Vars and their values for the lights, signs, MASTER WARNING/CAUTION, parking brake, flaps, spoilers, autobrake, BAT, EXT PWR, APU, baro and ND; `LIGHT BEACON`, `LIGHT WING`, `CIRCUIT SWITCH ON:21/22`, `CABIN SEATBELTS ALERT SWITCH`; `SPOILERS_ARM_TOGGLE`, `FLAPS_INCR`, `FLAPS_DECR`, `CABIN_SEATBELTS_ALERT_SWITCH_TOGGLE` |
| FBW-REL | https://docs.flybywiresim.com/release-notes/a32nx/v2024010/ ("FS2024 A32NX Stable Release v2024.1.0"): MSFS 2024 support, input events as the stable cockpit API, the three-position NAV/LOGO switch, legacy FCU L-Vars not stable API |
| FBW-NOTAM | https://flybywiresim.com/notams/development-update-sim-specific-releases-for-msfs-2020-and-2024/ (2026-05-13): separate MSFS 2020 and 2024 releases |
| FBW-SCI | FlyByWire `fbw-a32nx/src/wasm/fbw_a320/src/interface/SimConnectInterface.cpp` (master): the `A32NX.*` events are SimConnect client events (`SimConnect_MapClientEventToSimEvent`) |
| FBW-WARN | https://docs.flybywiresim.com/pilots-corner/a32nx/a32nx-briefing/flight-deck/glareshield/warning/ (what pressing MASTER WARN/CAUT does) |
| SDK-ELECE | MSFS 2024 SDK, Aircraft Electrical Events, https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-electrical-events/: `TOGGLE_BEACON_LIGHTS`, `TOGGLE_WING_LIGHTS`, `ELECTRICAL_CIRCUIT_TOGGLE` ("Toggle the named (or indexed) circuit switch state.") |
| README | PilotsDeck README, https://github.com/Fragtality/PilotsDeck/blob/master/README.md: 2.1 (long press, Second command), 2.1.1 (LVAR, KVAR, BVAR, LUAFUNC, CALCULATOR address forms), 2.1.2 (toggle between On and Off Value), 3.5.1 (standard scripts: `SimVar`, `SimRead`, `SimWrite`, `SimCalculator`) |
| PD-SRC | PilotsDeck source, https://github.com/Fragtality/PilotsDeck (tree 11bdf1f7): `Plugin/Simulator/SimCommand.cs` (`LVAR = 3`, `BVAR = 13`, `LUAFUNC = 14`, `KVAR = 16`), `Plugin/Simulator/ConnectorMSFS.cs` (L-Var command: write the value), `Plugin/Simulator/MSFS/ToolsMSFS.cs` (`WriteKvar`: the event name sent unchanged), `Plugin/Actions/Simple/ActionSwitchDisplay.cs` (no value image when neither value matches) |
| PD-PI | The installed plugin's settings panel, `Plugin\PI\js\pi-Common.js`: line 179 (`validNameKvar` takes `.` in K-Var names), 182 (`regLvar`), 195 (`rxKvarCmd`: one event with up to five parameters, or a sequence), 196 (`regLuaFunc`), 205 (`type == 3 //lvar`) |
| REF-FENIX | The Fenix A320 XL reference profile the user keeps in `A:\FS2024 Stuff\PilotsDeck` (read only, nothing copied): page layout ideas (FCU knob columns), and a real saved L-Var command (Display Gauge, command type 3, On and Off Value set) |
