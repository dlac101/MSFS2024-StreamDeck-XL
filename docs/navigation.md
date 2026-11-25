# Page navigation

How the pages of a profile connect. Built so far: the C172 G1000 main page, three filled child pages (Trim,
Views: [phase2-trim-views.md](phase2-trim-views.md); Sim rate: [phase2-sim-rate.md](phase2-sim-rate.md)), the More page with nine second-level pages (PFD, MFD,
V-speeds: [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md); COM pad: [phase2-com1-pad.md](phase2-com1-pad.md); Autopilot: [phase3-autopilot.md](phase3-autopilot.md); Transponder: [phase3-transponder.md](phase3-transponder.md); Radios: [phase3-radios.md](phase3-radios.md); Systems: [phase3-systems.md](phase3-systems.md); Engine: [phase3-engine-fuel.md](phase3-engine-fuel.md)) and one empty child page, Checklist (see [phase2-main-page.md](phase2-main-page.md)). Everything marked **plan** is not built yet; the
page ideas come from [original-plan.md](original-plan.md).

## Rules

- **One main page per profile.** It is the page the profile opens on (the profile's only listed page).
  Every other page is a Stream Deck **folder**: a child page opened by a folder key ("Create Folder").
  Stream Deck's own page switching (several listed pages, "Go to page") is not used.
- **Back key at 1,1 (top left) on every child page**, the Stream Deck app's back key (`backtoparent`;
  named "Parent Folder" or "Open Folder" in saved profiles). It
  returns to the page the folder key sits on. The position never changes, so position 1,1 on a child
  page never holds a function. This is the form of the installed MSFS-Fenix320-XL profile: all 43 of its
  child pages have their back key at 1,1.
- **At most two levels below the main page** (main > folder > sub-folder), so any page is at most two
  back presses from the main page. The Fenix XL profile goes five levels deep; this project keeps it
  shallow on purpose.
- **Folder keys keep their positions** on the main page across versions of a profile, so the grid stays
  familiar. A function that doesn't exist on an aircraft leaves its key empty instead of moving others.
  A profile for another aircraft type may have its own main-page grid ("MSFS2024 A32NX pages" below).
- Nothing on any page depends on the connected flight controls (Xbox Elite or T.16000M/TWCS).
- **Key titles at 14 by default** (`tools/profilegen/generate.py`: on Simple and Dynamic Buttons a template
  title size of 10 becomes 14; keys at 15 and folder and back keys at 12 stay). Readout keys (COM Radio,
  Display Value) keep their template size, because they draw their values with the title font: COM1 stays 10.
  Where a title does not fit at 14, the key's `title_size` in the data file sets another size (10 to 15).
  Every key keeps its template's title alignment (folder and back keys at the bottom), except the main page
  folder keys VIEWS, CHECKLIST and MORE (the user's own saved edit; on the VisionJet CHECKLIST is at MORE 1,5)
  and, on the VisionJet and the CJ4, the folder keys SYSTEMS and ICE/ENV and the COM pad's digit, CLR and ENT
  keys (V-PAD): their `title_align` in the data file is `"middle"` (it takes the Elgato manifest State
  `TitleAlignment` values `"top"`, `"middle"`, `"bottom"`).

## Pages

| Main page key | Child page | Holds now | Plan (not built) | Source |
|---|---|---|---|---|
| 1,7 `TRIM` | trim | back key, elevator trim up/down and the elevator trim gauge; aileron and rudder trim left/right keys, each pair with a horizontal trim gauge (P3-TRIM2) ([phase2-trim-views.md](phase2-trim-views.md), untested) | Trim controls and trim position readout | original-plan.md, Phase 2 concept layout ("Trim page") |
| 1,8 `VIEWS` | views | back key, 2 view keys (COCKPIT, EXTERNAL: A-Var writes to CAMERA STATE), 3 camera readouts ([phase2-trim-views.md](phase2-trim-views.md), EXTERNAL hand-tested, rest untested) | Camera views. Must work without vJoy or controller bindings (to be researched) | original-plan.md, Phase 2 concept layout and "Universal" level ("views") |
| 3,7 `SIM RATE` | simrate | back key, 1,2 `1X` (the Lua script XL24-SIMRATE.lua steps the rate back to 1x; lit at 1x), 1,3 `SLOWER` (one step down), 1,4 the RATE readout (press one step up, long press of a full second one step down) and 1,5 `FASTER` (one step up) ([phase2-sim-rate.md](phase2-sim-rate.md), repaired P2-6R, not yet sim-tested) | Sim rate: back to 1x, slower, faster and the rate readout (the user's layout, 2026-11-13) | the user's request (P2-6, layout 2026-11-13); position 3,7 was the Timer reservation |
| 3,8 `CHECKLIST` | checklist | back key only | Optional checklists and startup aids | original-plan.md, Phase 5 |
| 4,8 `MORE` | more | back key and nine folder keys (second level, [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md), untested): 1,2 `PFD` > pfd (G1000 PFD bezel: 12 softkeys, MENU, PROC, ENT, CLR, FPL, Direct-To, FMS and range knobs by H-event), 1,3 `MFD` > mfd (the same for the MFD), 1,4 `V-SPEEDS` > vspeeds (7 V-speed readouts), 1,5 `COM PAD` > compad (COM1 number pad: digits, CLR, ENT by the Lua script XL24-COMPAD.lua, a COM1 key and two readouts; [phase2-com1-pad.md](phase2-com1-pad.md), untested; position chosen by the user 2026-11-12), 1,6 `AUTOPILOT` > autopilot (GFC 700: 10 mode keys lit from sim state, HDG, CRS, ALT, VS and FLC speed readouts with +/- step keys; [phase3-autopilot.md](phase3-autopilot.md), not yet sim-tested), 1,7 `XPDR` > xpdr (transponder: code pad by the Lua script XL24-XPDRPAD.lua, code and mode readouts, STBY/ON/ALT by A-Var write, IDENT, VFR 1200; [phase3-transponder.md](phase3-transponder.md), not yet sim-tested), 1,8 `RADIOS` > radios (NAV1, NAV2 and COM2: active and standby readouts that swap on a press, MHz and kHz steps, station idents, COM1/COM2 mic select, all by K-event; [phase3-radios.md](phase3-radios.md), not yet sim-tested), 2,2 `SYSTEMS` > systems (alternator, avionics bus 1 and 2 and standby battery switches with bus volts and amps; interior lights and a dimmer readout; fuel selector LEFT/BOTH/RIGHT, fuel shutoff valve and fuel quantity; switches by the aircraft's input events, lit from sim state; [phase3-systems.md](phase3-systems.md), not yet sim-tested), 2,3 `ENGINE` > engine (read only, in the G1000 EIS order: RPM, fuel flow, oil pressure and temperature, EGT and vacuum readouts, fuel left/right bar gauges, bus volts and battery amps; [phase3-engine-fuel.md](phase3-engine-fuel.md), not yet sim-tested) | Further folders (second level) | original-plan.md, Phase 3 and "aircraft-class" level (Garmin avionics); phase2-main-page.md (XPDR code entry, radio page, Phase 3 selected values) |

Main page position 4,7 (Anti-ice) stays a reserved key, not a folder. (3,7 was reserved for a timer; it
is the `SIM RATE` folder now, and a later timer unit takes a free position.)

Other aircraft (Phase 4): each gets its own profile with its own permanent name. The A32NX profile has its
own main-page grid ("MSFS2024 A32NX pages"); a later aircraft uses this grid and these folder positions
where the function applies, unless its own grid is decided for it.

- **Page levels (plan):** original-plan.md sorts functions into three levels: universal (parking brake,
  gear, flaps, lights, ATC, maps, views, page navigation), aircraft-class (GA autopilot and Garmin avionics,
  airliner flight guidance and radios) and aircraft-specific (the C172 G1000 first).
- **Aircraft switching (plan):** original-plan.md asks for automatic switching by aircraft where PilotsDeck
  supports it (the Profile Manager's aircraft mappings), with safe fallback pages. Not built or tested yet.

## Adding a page

1. Add the page to the data file (`tools/profilegen/c172-g1000.json`): a page entry with its `id` and
   `parent`, and on the parent page a key with `"folder": "<id>"` and a title. The back key is added
   automatically at `back_key_pos`.
2. Add the page's keys and document them in the page's own doc, in the form of phase2-main-page.md.
3. Regenerate and check (`python tools/profilegen/generate.py`, then `python tools/profilegen/check.py`),
   then import the new file as phase2-main-page.md describes. `check.py` checks a child page against its
   doc when the page's entry in the data file names the doc (`"spec": "docs/<page doc>.md"`) and the doc has
   a table under the heading `## Key table: <page id>` in the main page's Key table form, listing all 32
   positions (`Back` at 1,1, `Empty` rows included); it then checks the page's keys key by key against
   that table. A child page with no `spec` must hold only its back key.
4. A second-level page (a folder key on a child page, as MORE's): give the first-level page a `spec` and a
   `## Key table: <page id>` with `Folder` rows, and give the new page `"parent": "<first-level page id>"`.
   `check.py` checks folder keys on every page (each opens the child page the data file and the doc's row
   name, and no page is opened twice), the back key at 1,1 on every child page, and at most two folder
   levels below the main page: a folder key on a second-level page fails the check.

## MSFS2024 A32NX pages

The FlyByWire A32NX profile `MSFS2024 A32NX` ([phase4-a32nx.md](phase4-a32nx.md), generated, not yet
sim-tested) follows the same rules: one main page (no back key), child pages opened by folder keys, the back
key at 1,1 on every child page, at most two folder levels (OVHD > SYSTEMS and EFIS > RADIO / XPDR / PED are
the second level).

| Main page key | Child page | Holds now |
|---|---|---|
| 1,8 `FCU` | fcu | back key; the FCU knobs as columns (`+` above the readout above `-`, PULL at the bottom: SPD, HDG, ALT, V/S, baro), SPD/MACH, TRK/FPA, ALT STEP, hPa/inHg, AP1, AP2, A/THR, LOC, APPR, EXPED, FD, LS; no empty position |
| 2,8 `OVHD` | ovhd | back key; exterior lights (STROBE, BEACON, WING, NAV LOGO, RWY TURN, LAND L/R, NOSE), SEAT BELT, NO SMOKE, EMER EXIT, ANN LT, BAT 1/2 and their voltages, EXT PWR, EXT AVAIL, GEN 1/2, APU GEN, BUS TIE, APU MSTR, APU START, APU AVAIL, APU BLEED, APU N, the folder key 2,8 `SYSTEMS` ([phase4-a32nx-overhead.md](phase4-a32nx-overhead.md)); 3 empty positions reserved for a later unit |
| ovhd 2,8 `SYSTEMS` | ovhdsys (second level) | back key (to OVHD); fuel pumps L TK 1/2, CTR TK 1/2, R TK 1/2, MODE SEL, X FEED and XFEED VLV, ADIRS IR 1/3/2, ON BAT, ALIGN, BLEED 1/2, PACK 1/2, ESS FEED, GALY CAB, COMML, WING/ENG1/ENG2 A/I, PROBE HT ([phase4-a32nx-overhead.md](phase4-a32nx-overhead.md), not yet sim-tested); 6 empty positions reserved for a later unit |
| 4,8 `EFIS` | efis | back key; the Captain's EFIS control panel and glareshield lamps ([phase4-a32nx-efis.md](phase4-a32nx-efis.md)): baro column (BARO+, BARO, BARO-), QNH, STD, hPa/inHg, FD, LS, CSTR, WPT, VOR.D, NDB, ARPT, ND MODE, ND RNG, ADF/VOR1, ADF/VOR2, CHRONO, AUTOLAND, WARN, CAUT, the folder keys 3,4 `RADIO` and 3,5 `XPDR` ([phase4-a32nx-radios.md](phase4-a32nx-radios.md)) and 3,6 `PED` ([phase4-a32nx-pedestal.md](phase4-a32nx-pedestal.md)); 7 empty positions (3,7 for a later unit, 4,3 to 4,8 for the F/O side EFIS) |
| efis 3,4 `RADIO`, 3,5 `XPDR` | radio, xpdr (second level) | back key (to EFIS) on each; radio: the Captain's RMP 1 (VHF1, VHF2, RMP ON, the ACTIVE and STBY windows, XFER, MHz+/-, kHz+/-) and the COM1 and COM2 active frequencies; xpdr: the ATC/TCAS panel (XPDR code, STATE, IDENT, keypad 0 to 7 and CLR, MODE, ALT RPTG, TCAS, TRAFFIC) ([phase4-a32nx-radios.md](phase4-a32nx-radios.md), not yet sim-tested); 19 (radio) and 15 (xpdr) empty positions reserved for a later unit |
| efis 3,6 `PED` | ped (second level) | back key (to EFIS); the ECAM control panel (ENG, BLEED, PRESS, ELEC, HYD, FUEL, APU, COND, DOOR, WHEEL, F/CTL, CLR, STS lit from their lamps; ALL, RCL, TO CONF), SPD BRK, GND SPLR, FLAPS, PARK (main's keys repeated), GEAR, LDG GEAR, A/BRK, ENG 1, ENG 2, ENG MODE, RUD L, RUD TRIM, RUD R, A/SKID, BRK PSI ([phase4-a32nx-pedestal.md](phase4-a32nx-pedestal.md), not yet sim-tested); no empty position |

Main page position 4,8 is the EFIS folder (P4-2); CHECKLIST (Phase 5) has no position on the A32NX main page
yet. The A32NX main page has its own
grid (FCU buttons, readouts, flight controls, lights): the C172 profile's VIEWS, SIM RATE and MORE folders are
not on it (the C172 has CHECKLIST at 3,8).

## MSFS2024 VisionJet pages

The Cirrus Vision SF50 profile `MSFS2024 VisionJet` ([visionjet-sf50.md](visionjet-sf50.md), generated, not
yet sim-tested) has its own main grid since V-UX, built around the autopilot and the autothrottle
([visionjet-sf50.md](visionjet-sf50.md), "The main page (V-UX)"); up to V-3 it used the C172 G1000 profile's
grid. It keeps the C172's folder positions TRIM 1,7, VIEWS 1,8, SIM RATE 3,7 and MORE 4,8, and the same rules:
one main page (no back key), the back key at 1,1 on every child page, at most two folder levels. COM PAD sits
at main 3,8 and CHECKLIST at MORE 1,5: a deviation from "Folder keys keep their positions" (Rules), so that
the COM pad is one press nearer while the checklist page (Phase 5) is still empty. Each folder key keeps its
title alignment where it moved (VIEWS, MORE, SYSTEMS, CHECKLIST and ICE/ENV middle, the others bottom).

| Main page key | Child page | Holds now |
|---|---|---|
| 1,7 `TRIM` | trim | the C172's current trim page (elevator trim keys and gauge, rudder trim keys and gauge) without its aileron trim keys (V-2) |
| 1,8 `VIEWS` | views | the C172's views page, plus MAP at 1,7 (V-UX) |
| 2,7 `AUTOPILOT` | autopilot | the C172's page with the G3000 course keys, HDG sync, VNV by the SF50's input event, LVL, A/T, TOGA and A/T MGD; V-2 adds FMS SPD, YD and MAN SPD; V-3: the step keys hold to repeat (under MORE 1,6 until V-UX) |
| 2,8 `RADIOS` | radios | the C172's page plus a BARO column (V-3); COM1, CDI and the BARO press and long press from main (V-UX; under MORE 1,8 until then) |
| 3,7 `SIM RATE` | simrate | the C172's sim rate page as it is (`XL24-SIMRATE.lua`) |
| 3,8 `COM PAD` | compad | the C172's COM1 pad with centered titles and press feedback (`XL24-COMPAD.lua`; under MORE 1,5 until V-UX) |
| 4,7 `SYSTEMS` | systems | V-2: BAT 2, GEN 1 and GEN 2 guarded switches; bus volts, load, engine knob, starter and fuel control readouts; V-UX: BAT, PARK, GEAR, N1 and the light, pitot and ICE switches from main (under MORE 2,2 until V-UX) |
| 4,8 `MORE` | more | back key and five folder keys (second level): 1,4 `V-SPEEDS` > vspeeds, 1,7 `XPDR` > xpdr (the C172's pages as they are), 1,5 `CHECKLIST` > checklist (back key only; main 3,8 until V-UX), 2,3 `ENGINE` > engine (N1, N2, ITT, fuel flow, engine run, ignition and fuel readouts), 2,4 `ICE/ENV` > iceenv (V-2: ice protection, wing light, oxygen and ECS switches; ice protection, bleed air and ECS readouts) |

MORE 1,2 and 1,3 (the C172's PFD and MFD pages) are empty: the SF50's PFD and MFD have no softkeys, and a GTC
page is left for the VisionJet's V-4 (with the checklist wheel, the ECS and knob writes, IE-SF50 82,
windshield MAX and battery amps). MORE 1,6, 1,8 and 2,2 are empty since V-UX.

## MSFS2024 CJ4 pages

The Citation CJ4 profile `MSFS2024 CJ4` ([cj4.md](cj4.md), generated, not yet sim-tested) keeps the C172
G1000 profile's main grid and folder positions, and the same rules: one main page (no back key), the back
key at 1,1 on every child page, at most two folder levels. 15 pages: main, the five pages its folder keys
open, and nine under MORE.

| Main page key | Child page | Holds now |
|---|---|---|
| 1,7 `TRIM` | trim | the C172's trim page: elevator, aileron and rudder trim keys (hold to repeat) and gauges |
| 1,8 `VIEWS` | views | the C172's views page as it is |
| 3,7 `SIM RATE` | simrate | the C172's sim rate page as it is (`XL24-SIMRATE.lua`) |
| 3,8 `CHECKLIST` | checklist | the back key only; 1,2 is kept empty for the cursor control panel's checklist key |
| 4,8 `MORE` | more | back key and nine folder keys (second level): 1,4 `V-SPEEDS` > vspeeds, 1,5 `COM PAD` > compad (the VisionJet's COM pad page), 1,6 `AUTOPILOT` > autopilot, 1,7 `XPDR` > xpdr, 1,8 `RADIOS` > radios, 2,2 `SYSTEMS` > systems, 2,3 `ENGINE` > engine, 2,4 `ICE/ENV` > iceenv, 2,5 `LIGHTS` > lights |

MORE 1,2, 1,3 and 2,6 to 2,8 are empty: they are kept for the display control, cursor control and three FMS
pages of a later unit, which use the WT21 key names and wait for a test of those names in the default CJ4
([cj4.md](cj4.md), "Not on these pages, and why").
