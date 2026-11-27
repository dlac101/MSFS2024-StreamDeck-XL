# Vision Jet research (MSFS 2024)

## Status

Research only. Nothing here is built or sim-tested. Every name is Unverified.
When a profile is built, its names go into [aircraft-mappings.md](aircraft-mappings.md), Unverified until a
sim test passes.

The first profile built from this page: [visionjet-sf50.md](visionjet-sf50.md) (V-1; not yet sim-tested except
the A/T keys, hand-tested 2026-11-26). This page's tables and draft layout stay as researched for V-1: the
built keys, their addresses and test states are in [visionjet-sf50.md](visionjet-sf50.md) and
[aircraft-mappings.md](aircraft-mappings.md) (the A/T and PARK keys, for example, now write the SF50's own
input events).

This page collects what the public sources say about the Cirrus Vision Jet (SF50) that comes with MSFS 2024,
the default aircraft and the one target of this page: its name and edition, the variable and event names the
sources give for it, and a draft Stream Deck XL page layout. FlightFX's add-on is not the target (see
"Products"). Nothing on this page has been tried in the sim. Each name cites its source tag (listed under
"Sources", with the URL and the date it was read) and stays Unverified until the aircraft is loaded, its input
event list is read and a sim test passes.

Address forms follow the PilotsDeck README, section 2.1.1 (README). Positions are row,column, 1-based, row 1
at the top.

## Products

| Product | Maker | Where sold or included | Avionics | Version and date | Source |
|---|---|---|---|---|---|
| The MSFS 2024 default SF50: "Cirrus Vision SF50 (VisionJet)" (list name); "Cirrus SF50 Vision Jet" (official FAQ) | Open: sources conflict (see below) | Included in MSFS 2024 (default aircraft); which edition: open (the Standard Edition in a pre-release list) | G3000-type: "G3000" named by a forum user; no official source | none public | FSE-LIST https://fselite.net/content/all-aircraft-featured-in-microsoft-flight-simulator-2024/ (pre-release list, posted 2024-09-19, updated 2024-09-23), read 2026-11-16; FS-FAQ https://www.flightsimulator.com/microsoft-flight-simulator-2024-faq/ read 2026-11-16; FORUM-MAN (2024-12-15 post) |

What the sources say, and what stays open:

- **Name and variant: open.** The sources call it "Cirrus Vision SF50 (VisionJet)" (FSE-LIST), "Cirrus SF50
  Vision Jet" (FS-FAQ; the official forum's thread for it, FORUM-24) and "Cirrus SF50 Vision Jet (MSFS2024)"
  (the HubHop aircraft name, HH-MS). No official source read names a variant (G2, G2+ or another), so this
  page does not call the default a "G2". One MSFS 2024 bug report on the official forum (tagged msfs-2024, no
  mods) titles it "Cirrus Vision Jet G2" without saying where "G2" comes from (FORUM-G2, 2024-11-20): a user's
  wording, not the sim's own title. The name the sim shows settles it (open question 2).
- **Edition and ownership: open.** FSE-LIST puts it in the Standard Edition list, a list made at the
  pre-release Global Preview Event. A user list of first-party aircraft (FORUM-LIST, 2025-10-09) also puts it
  in the Standard tier and links FS-FAQ. The official FAQ (FS-FAQ) names the "Cirrus SF50 Vision Jet" under a
  2024-03-13 partnership announcement with FlightFX but has no per-edition list, and no official edition list
  was found. Which edition holds it, and whether you have it now, is open question 1.
- **Maker: open, the sources conflict.** FS-FAQ ties the aircraft to the FlightFX partnership without saying
  who built it. Forum users say FlightFX built it (FORUM-MAN, 2024-12-05; FORUM-CMP, 2025-06-18), or that
  FlightFX sold the model and the systems were reworked with Working Title (FORUM-CMP, 2025-06-18), or that
  FlightFX leaves support to Microsoft (FORUM-MAN, 2024-12-05). No verdict here.
- **Avionics.** "G3000" is a forum user's word (FORUM-MAN, 2024-12-15); HubHop's Microsoft preset reads
  `L:WT_TOGA_ACTIVE` (HH-MS). No source read names "Perspective Touch+": open.
- **Systems the sources show.** Autothrottle and VNAV work (FORUM-24, 2024-11-23). A TOGA button sits on the
  left side of the throttle and is used with the autothrottle for takeoff (FORUM-MAN, 2024-12-06). Autoland
  exists, with reports that it finds no airport (FORUM-24, 2024-11-24; FORUM-AL, 2024-11-25). The parachute
  (CAPS) deploys: users ask how to reset it and report a model gap in its compartment (FORUM-24P2, 2024-11-24
  and 2024-11-28). Users disagree whether the checklists work (FORUM-MAN, 2024-12-07 and 2024-12-16).
- **FlightFX's add-on: not the target.** FlightFX sells its own "SF50 Vision Jet G2", an MSFS 2020 add-on, on
  the MSFS Marketplace (FFX-PROD, MKT-FFX). This page does not cover it and uses none of its names.
- **Other products: none found.** One more search of flightsim.to, Orbx, SimMarket and the Marketplace
  (2026-11-16) found no other Vision Jet aircraft: only liveries and a checklist add-on for the existing
  models on flightsim.to.

## Is a Vision Jet installed

The default SF50 package is present in the sim's streamed-package cache on the development PC; no add-on
Vision Jet is installed. Whether the aircraft is in your aircraft list is open question 1. The aircraft's own
input event list (the `InputEvents.txt` that PilotsDeck writes once the aircraft is loaded) does not exist
yet, so no B-var name is known.

## Where the names come from

| Source | What it gives for the default SF50 | How it was read |
|---|---|---|
| MSFS 2024 SDK SimVars and key events (SDK-* tags) | standard names | built-in browser, the page's own search (each name below was found on the page its tag names) |
| G3000 H events for MSFS 2024 (WT-G3000H) | likely (G3000-type), not confirmed for the SF50 | web page; it names no aircraft and does not say which GTC index is which seat |
| HubHop "Cirrus SF50 Vision Jet (MSFS2024)" (HH-MS), vendor Microsoft | 3 presets (TOGA annunciator, baro STD, VNV) | built-in browser, aircraft filter, rows expanded |
| The aircraft's own input events (B-vars) | once the aircraft has been loaded with PilotsDeck running | not available yet: B-var rows below have no name |
| Developer documents | none public for the 2024 aircraft (FORUM-MAN, 2024-12-05) | - |
| The C172 G1000 page docs of this repo | the standard names those pages use (radios, transponder, views, sim rate, V-speeds), with their SDK tags | the linked doc |
| PilotsDeck README 2.1.1 (README) | address forms only | the repo's existing source |

How the tables write names:

- A HubHop preset's code is RPN, not a PilotsDeck address. The tables give the names in the code as
  candidates, with the PilotsDeck address form (README 2.1.1). A preset that needs several steps is
  "calculator code": it needs the MobiFlight WASM module (see [installation.md](installation.md)).
- A name the C172 pages already use cites that page's doc and its SDK tag ("as" the doc).

Open research points (not questions for you): whether the SF50 displays have bezel softkeys (the G3000 H event
list has PFD softkey events; no HubHop preset for the default SF50 uses them); whether its touch controllers
take the horizontal or the vertical GTC events (WT-G3000H lists both; no source ties either to the SF50);
which GTC index is the pilot's (open question 4); how many batteries and generators it has (its input event
list will show).

## Candidate names

Kind is one of SimVar, K-event, B-var, L-var, H-event, input event, calculator code. A SimVar's unit in the
PilotsDeck address is the one the repo's other pages use for that kind of value (SDK-UNITS). Every name is a
candidate for the default SF50.

### Touch controllers

The touch controllers (GTCs). WT-G3000H lists 12 events per horizontal GTC; `[index]` is the GTC's instrument
index (1, 2, 3 ...). The default SF50 uses G3000-type avionics per a forum user (FORUM-MAN), not confirmed;
whether its GTCs take these horizontal events is open.

| Control | Candidate name | Kind | PilotsDeck address | Source | Status |
|---|---|---|---|---|---|
| Top knob, outer, clockwise / counterclockwise | `AS3000_TSC_Horizontal_[index]_TopKnob_Large_INC`, `..._TopKnob_Large_DEC` | H-event | `H:AS3000_TSC_Horizontal_1_TopKnob_Large_INC` | WT-G3000H; not confirmed for the SF50 | Unverified |
| Top knob, inner, clockwise / counterclockwise | `AS3000_TSC_Horizontal_[index]_TopKnob_Small_INC`, `..._TopKnob_Small_DEC` | H-event | `H:AS3000_TSC_Horizontal_1_TopKnob_Small_INC` | WT-G3000H; not confirmed for the SF50 | Unverified |
| Top knob push | `AS3000_TSC_Horizontal_[index]_TopKnob_Push` | H-event | `H:AS3000_TSC_Horizontal_1_TopKnob_Push` | WT-G3000H; not confirmed for the SF50 | Unverified |
| Top knob long push | `AS3000_TSC_Horizontal_[index]_TopKnob_Push_Long` | H-event | `H:AS3000_TSC_Horizontal_1_TopKnob_Push_Long` | WT-G3000H; not confirmed for the SF50 | Unverified |
| Softkeys upper, middle, lower | `AS3000_TSC_Horizontal_[index]_SoftKey_1`, `..._SoftKey_2`, `..._SoftKey_3` | H-event | `H:AS3000_TSC_Horizontal_1_SoftKey_1` | WT-G3000H; not confirmed for the SF50 | Unverified |
| Lower knob, clockwise / counterclockwise | `AS3000_TSC_Horizontal_[index]_BottomKnob_Small_INC`, `..._BottomKnob_Small_DEC` | H-event | `H:AS3000_TSC_Horizontal_1_BottomKnob_Small_INC` | WT-G3000H; not confirmed for the SF50 | Unverified |
| Lower knob push | `AS3000_TSC_Horizontal_[index]_BottomKnob_Push` | H-event | `H:AS3000_TSC_Horizontal_1_BottomKnob_Push` | WT-G3000H; not confirmed for the SF50 | Unverified |

WT-G3000H also lists vertical GTC events (`AS3000_TSC_Vertical_[index]_...`); no source ties them to the SF50.
No source gives a readable state for a GTC knob or softkey: GTC keys read nothing.

### PFD and MFD

WT-G3000H events for the display units, the baro names and the V-speed readouts of the C172 pages. Whether the
SF50 displays have bezel softkeys is open; no HubHop preset for the default SF50 uses the softkey, range or
joystick events.

| Control | Candidate name | Kind | PilotsDeck address | Source | Status |
|---|---|---|---|---|---|
| PFD softkeys 1-12 (left to right) | `AS3000_PFD_1_SOFTKEYS_[index]`, `AS3000_PFD_2_SOFTKEYS_[index]` | H-event | `H:AS3000_PFD_1_SOFTKEYS_1` | WT-G3000H; open: softkeys | Unverified |
| Map range | `AS3000_PFD_[index]_RANGE_INC`, `..._RANGE_DEC` | H-event | `H:AS3000_PFD_1_RANGE_INC` | WT-G3000H; not confirmed for the SF50 | Unverified |
| Joystick up, down, left, right, push | `AS3000_PFD_[index]_JOYSTICK_UP` (`_DOWN`, `_LEFT`, `_RIGHT`, `_PUSH`) | H-event | `H:AS3000_PFD_1_JOYSTICK_PUSH` | WT-G3000H; not confirmed for the SF50 | Unverified |
| Baro knob | `AS3000_PFD_[index]_BARO_INC`, `..._BARO_DEC`, `..._BARO_PUSH` | H-event | `H:AS3000_PFD_1_BARO_PUSH` | WT-G3000H; not confirmed for the SF50 | Unverified |
| Course knob | `AS3000_PFD_[index]_CRS_INC`, `..._CRS_DEC`, `..._CRS_PUSH` | H-event | `H:AS3000_PFD_1_CRS_INC` | WT-G3000H; not confirmed for the SF50 | Unverified |
| Baro STD (HubHop preset "SF50 Baro PUSH STD") | `(>K:BAROMETRIC_STD_PRESSURE) 1 (>B:AUTOPILOT_BARO_1_SYNC)` | calculator code | calculator code (MobiFlight WASM module) | HH-MS | Unverified |
| Baro STD event in that preset | `BAROMETRIC_STD_PRESSURE` | K-event | `K:BAROMETRIC_STD_PRESSURE` | HH-MS | Unverified |
| Baro sync input event in that preset | `AUTOPILOT_BARO_1_SYNC` | input event | `B:AUTOPILOT_BARO_1_SYNC` | HH-MS | Unverified |
| Baro sync (the C172 BARO key's press) | `BAROMETRIC` | K-event | `K:BAROMETRIC` | SDK-INSTE, as [phase2-main-page.md](phase2-main-page.md) | Unverified |
| Baro setting (readout) | `KOHLSMAN SETTING HG` | SimVar | `(A:KOHLSMAN SETTING HG:1, inHg)` | SDK-SYSV, as [phase2-main-page.md](phase2-main-page.md) | Unverified |
| V-speed readouts | `DESIGN SPEED VS0`, `DESIGN SPEED VS1`, `DESIGN SPEED MIN ROTATION`, `DESIGN SPEED CLIMB`, `DESIGN SPEED VC`, `REFERENCE SPEED MAX IAS` | SimVar | `(A:DESIGN SPEED VS0, knots)` and the others there | SDK-FMV, as [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md) | Unverified |
| Flap speed limit (readout) | `FLAPS CURRENT SPEED LIMITATION` | SimVar | `(A:FLAPS CURRENT SPEED LIMITATION, knots)` | SDK-CTLV, as [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md) | Unverified |

### Autopilot

HubHop has one autopilot preset for the default SF50 (VNV, HH-MS); the standard SDK names are the candidates,
as on the C172 autopilot page. Beyond VNAV and the autothrottle (FORUM-24), no source read says which modes
the SF50's autopilot has.

| Control | Candidate name | Kind | PilotsDeck address | Source | Status |
|---|---|---|---|---|---|
| AP master | `AP_MASTER` | K-event | `K:AP_MASTER` | SDK-APE | Unverified |
| AP state | `AUTOPILOT MASTER` | SimVar | `(A:AUTOPILOT MASTER, Bool)` | SDK-APV | Unverified |
| AP disengaged state | `AUTOPILOT DISENGAGED` | SimVar | `(A:AUTOPILOT DISENGAGED, Bool)` | SDK-APV | Unverified |
| HDG mode | `AP_HDG_HOLD` | K-event | `K:AP_HDG_HOLD` | SDK-APE | Unverified |
| HDG state | `AUTOPILOT HEADING LOCK` | SimVar | `(A:AUTOPILOT HEADING LOCK, Bool)` | SDK-APV | Unverified |
| Heading bug | `AUTOPILOT HEADING LOCK DIR` | SimVar | `(A:AUTOPILOT HEADING LOCK DIR, Degrees)` (no index; `:1` is the C172 page's fallback) | SDK-APV, as [phase3-autopilot.md](phase3-autopilot.md) | Unverified |
| Heading bug step | `HEADING_BUG_INC`, `HEADING_BUG_DEC` | K-event | `K:HEADING_BUG_INC` | SDK-APE, as [phase3-autopilot.md](phase3-autopilot.md) | Unverified |
| Heading sync | `Garmin_AP_HDG_Sync` | H-event | `H:Garmin_AP_HDG_Sync` | WT-G3000H; not confirmed for the SF50 | Unverified |
| ALT mode | `AP_ALT_HOLD` | K-event | `K:AP_ALT_HOLD` | SDK-APE | Unverified |
| ALT state | `AUTOPILOT ALTITUDE LOCK` | SimVar | `(A:AUTOPILOT ALTITUDE LOCK, Bool)` | SDK-APV | Unverified |
| ALT preselect | `AUTOPILOT ALTITUDE LOCK VAR` | SimVar | `(A:AUTOPILOT ALTITUDE LOCK VAR, Feet)` | SDK-APV, as [phase3-autopilot.md](phase3-autopilot.md) | Unverified |
| ALT preselect step | `AP_ALT_VAR_INC`, `AP_ALT_VAR_DEC` | K-event | `K:AP_ALT_VAR_INC` | SDK-APE | Unverified |
| VS mode | `AP_VS_HOLD` | K-event | `K:AP_VS_HOLD` | SDK-APE, as [phase3-autopilot.md](phase3-autopilot.md) | Unverified |
| VS state | `AUTOPILOT VERTICAL HOLD` | SimVar | `(A:AUTOPILOT VERTICAL HOLD, Bool)` | SDK-APV | Unverified |
| VS target | `AUTOPILOT VERTICAL HOLD VAR` | SimVar | `(A:AUTOPILOT VERTICAL HOLD VAR, Feet/minute)` | SDK-APV | Unverified |
| VS step | `AP_VS_VAR_INC`, `AP_VS_VAR_DEC` | K-event | `K:AP_VS_VAR_INC` | SDK-APE | Unverified |
| NAV mode | `AP_NAV1_HOLD` | K-event | `K:AP_NAV1_HOLD` | SDK-APE | Unverified |
| NAV state | `AUTOPILOT NAV1 LOCK` | SimVar | `(A:AUTOPILOT NAV1 LOCK, Bool)` | SDK-APV | Unverified |
| APR mode | `AP_APR_HOLD` | K-event | `K:AP_APR_HOLD` | SDK-APE | Unverified |
| APR state | `AUTOPILOT APPROACH HOLD`, `AUTOPILOT GLIDESLOPE HOLD` | SimVar | `(A:AUTOPILOT APPROACH HOLD, Bool)` | SDK-APV | Unverified |
| FLC mode | `FLIGHT_LEVEL_CHANGE` | K-event | `K:FLIGHT_LEVEL_CHANGE` | SDK-APE, as [phase3-autopilot.md](phase3-autopilot.md) | Unverified |
| FLC state | `AUTOPILOT FLIGHT LEVEL CHANGE` | SimVar | `(A:AUTOPILOT FLIGHT LEVEL CHANGE, Bool)` | SDK-APV | Unverified |
| FLC / speed reference | `AUTOPILOT AIRSPEED HOLD VAR`, `AUTOPILOT MACH HOLD VAR` | SimVar | `(A:AUTOPILOT AIRSPEED HOLD VAR, Knots)` | SDK-APV | Unverified |
| Speed reference step | `AP_SPD_VAR_INC`, `AP_SPD_VAR_DEC` | K-event | `K:AP_SPD_VAR_INC` | SDK-APE, as [phase3-autopilot.md](phase3-autopilot.md) | Unverified |
| LVL mode | `AP_WING_LEVELER` | K-event | `K:AP_WING_LEVELER` | SDK-APE | Unverified |
| LVL state | `AUTOPILOT WING LEVELER` | SimVar | `(A:AUTOPILOT WING LEVELER, Bool)` | SDK-APV | Unverified |
| VNV mode, press and state | `XMLVAR_VNAVButtonValue` | L-var | `L:XMLVAR_VNAVButtonValue`; press as calculator code `(L:XMLVAR_VNAVButtonValue) ! (>L:XMLVAR_VNAVButtonValue)` | HH-MS | Unverified |
| Flight director | `TOGGLE_FLIGHT_DIRECTOR` | K-event | `K:TOGGLE_FLIGHT_DIRECTOR` | SDK-APE | Unverified |
| Flight director state | `AUTOPILOT FLIGHT DIRECTOR ACTIVE` | SimVar | `(A:AUTOPILOT FLIGHT DIRECTOR ACTIVE, Bool)` | SDK-APV, as [phase2-main-page.md](phase2-main-page.md) | Unverified |
| NAV1 course (readout) | `NAV OBS` | SimVar | `(A:NAV OBS:1, Degrees)` | SDK-RADV, as [phase3-autopilot.md](phase3-autopilot.md) | Unverified |

### Autothrottle and TOGA

Autothrottle and TOGA work on the default SF50 per users (FORUM-24, FORUM-MAN). No source read gives a name
for the TOGA button itself or for a manual or FMS speed reference mode.

| Control | Candidate name | Kind | PilotsDeck address | Source | Status |
|---|---|---|---|---|---|
| A/T arm | `AUTO_THROTTLE_ARM` | K-event | `K:AUTO_THROTTLE_ARM` | SDK-APE; not confirmed for the SF50 | Unverified |
| A/T armed state | `AUTOPILOT THROTTLE ARM` | SimVar | `(A:AUTOPILOT THROTTLE ARM, Bool)` | SDK-APV | Unverified |
| A/T managed state | `AUTOPILOT MANAGED THROTTLE ACTIVE` | SimVar | `(A:AUTOPILOT MANAGED THROTTLE ACTIVE, Bool)` | SDK-APV | Unverified |
| TOGA | `AUTO_THROTTLE_TO_GA` | K-event | `K:AUTO_THROTTLE_TO_GA` | SDK-APE; not confirmed for the SF50 | Unverified |
| Takeoff power state | `AUTOPILOT TAKEOFF POWER ACTIVE` | SimVar | `(A:AUTOPILOT TAKEOFF POWER ACTIVE, Bool)` | SDK-APV | Unverified |
| TOGA annunciator (green TO on the PFD) | `WT_TOGA_ACTIVE` | L-var | `L:WT_TOGA_ACTIVE` | HH-MS | Unverified |

### Lights

On the default SF50 the cockpit switches are likely input events (as on the 2024 C172, see
[aircraft-mappings.md](aircraft-mappings.md)): their names come from the aircraft's input event list. The
K-events and SimVars below are the standard SDK names the C172 main page keeps as fallbacks
([phase2-main-page.md](phase2-main-page.md)); which lights the SF50 has is not confirmed.

| Control | Candidate name | Kind | PilotsDeck address | Source | Status |
|---|---|---|---|---|---|
| Light switches | none yet: from the aircraft's InputEvents once installed | B-var | `B:<input event>` | README 2.1.1 | Unverified |
| Nav lights | `TOGGLE_NAV_LIGHTS` | K-event | `K:TOGGLE_NAV_LIGHTS` | SDK-ELECE | Unverified |
| Nav lights state | `LIGHT NAV` | SimVar | `(A:LIGHT NAV, Bool)` | SDK-SYSV | Unverified |
| Beacon | `TOGGLE_BEACON_LIGHTS` | K-event | `K:TOGGLE_BEACON_LIGHTS` | SDK-ELECE | Unverified |
| Beacon state | `LIGHT BEACON` | SimVar | `(A:LIGHT BEACON, Bool)` | SDK-SYSV | Unverified |
| Taxi lights | `TOGGLE_TAXI_LIGHTS` | K-event | `K:TOGGLE_TAXI_LIGHTS` | SDK-ELECE | Unverified |
| Taxi lights state | `LIGHT TAXI` | SimVar | `(A:LIGHT TAXI, Bool)` | SDK-SYSV | Unverified |
| Strobes | `STROBES_TOGGLE`, `STROBES_SET` | K-event | `K:STROBES_TOGGLE` | SDK-ELECE | Unverified |
| Strobes state | `LIGHT STROBE` | SimVar | `(A:LIGHT STROBE, Bool)` | SDK-SYSV | Unverified |
| Landing lights | `LANDING_LIGHTS_TOGGLE`, `LANDING_LIGHTS_SET` | K-event | `K:LANDING_LIGHTS_TOGGLE` | SDK-ELECE | Unverified |
| Landing lights state | `LIGHT LANDING` | SimVar | `(A:LIGHT LANDING, Bool)` | SDK-SYSV | Unverified |
| Wing (ice) lights | `WING_LIGHTS_SET` | K-event | `K:WING_LIGHTS_SET` | SDK-ELECE | Unverified |
| Wing lights state | `LIGHT WING` | SimVar | `(A:LIGHT WING, Bool)` | SDK-SYSV | Unverified |

### Electrical

On the 2024 C172 the battery switch drives an input event and a different battery index than the K-event (see
[aircraft-mappings.md](aircraft-mappings.md)), so the default SF50's switches are taken from its input event
list first. No source read says how many batteries and generators it has: the rows below use index 1, and that
list will show any second one.

| Control | Candidate name | Kind | PilotsDeck address | Source | Status |
|---|---|---|---|---|---|
| Battery and generator switches | none yet: from the aircraft's InputEvents once installed | B-var | `B:<input event>` | README 2.1.1 | Unverified |
| Battery toggle | `TOGGLE_MASTER_BATTERY` | K-event | `K:TOGGLE_MASTER_BATTERY:1` | SDK-ELECE | Unverified |
| Battery state | `ELECTRICAL MASTER BATTERY` | SimVar | `(A:ELECTRICAL MASTER BATTERY:1, Bool)` | SDK-ELECV | Unverified |
| Generator (alternator) switch | `ALTERNATOR_SET` | K-event | `K:ALTERNATOR_SET` | SDK-ELECE | Unverified |
| Generator (alternator) state | `GENERAL ENG MASTER ALTERNATOR` | SimVar | `(A:GENERAL ENG MASTER ALTERNATOR:1, Bool)` | SDK-ENGV | Unverified |
| Main bus volts | `ELECTRICAL MAIN BUS VOLTAGE` | SimVar | `(A:ELECTRICAL MAIN BUS VOLTAGE:1, Volts)` | SDK-ELECV | Unverified |
| External power | `EXTERNAL POWER ON` | SimVar | `(A:EXTERNAL POWER ON:1, Bool)` | SDK-ELECV | Unverified |
| Panel power | `CIRCUIT GENERAL PANEL ON` | SimVar | `(A:CIRCUIT GENERAL PANEL ON, Bool)` | SDK-ELECV | Unverified |

Avionics master: no name found (no HubHop preset; `AVIONICS_MASTER` and `AVIONICS MASTER SWITCH` were not
found on the SDK electrical pages searched). It comes from the input event list.

### Fuel

No fuel name for the default SF50 beyond the standard quantities was found; its fuel selector and any fuel
pump come from its input event list.

| Control | Candidate name | Kind | PilotsDeck address | Source | Status |
|---|---|---|---|---|---|
| Fuel selector | none yet: from the aircraft's InputEvents once installed | B-var | `B:<input event>` | README 2.1.1 | Unverified |
| Fuel quantity, total | `FUEL TOTAL QUANTITY` | SimVar | `(A:FUEL TOTAL QUANTITY, Gallons)` | SDK-FUELV | Unverified |
| Fuel quantity, left and right tank | `FUEL TANK LEFT MAIN QUANTITY`, `FUEL TANK RIGHT MAIN QUANTITY` | SimVar | `(A:FUEL TANK LEFT MAIN QUANTITY, Gallons)` | SDK-FUELV | Unverified |

### Engine

No source read names the engine model; the readouts use engine index 1. Engine start and stop stay in the
cockpit (as on the C172 main page: no irreversible engine command on the deck), so the engine names below are
readouts, and the ignition events are candidates only.

| Control | Candidate name | Kind | PilotsDeck address | Source | Status |
|---|---|---|---|---|---|
| N1 | `TURB ENG N1` | SimVar | `(A:TURB ENG N1:1, Percent)` | SDK-ENGV | Unverified |
| N2 | `TURB ENG N2` | SimVar | `(A:TURB ENG N2:1, Percent)` | SDK-ENGV | Unverified |
| ITT | `TURB ENG ITT` | SimVar | `(A:TURB ENG ITT:1, Celsius)` | SDK-ENGV | Unverified |
| Fuel flow | `TURB ENG FUEL FLOW PPH` | SimVar | `(A:TURB ENG FUEL FLOW PPH:1, Pounds per hour)` | SDK-ENGV | Unverified |
| Engine running | `GENERAL ENG COMBUSTION` | SimVar | `(A:GENERAL ENG COMBUSTION:1, Bool)` | SDK-ENGV | Unverified |
| Ignition switch state | `TURB ENG IGNITION SWITCH` | SimVar | `(A:TURB ENG IGNITION SWITCH:1, Bool)` | SDK-ENGV | Unverified |
| Ignition switch | `TURBINE_IGNITION_SWITCH_TOGGLE`, `TURBINE_IGNITION_SWITCH_SET` | K-event | `K:TURBINE_IGNITION_SWITCH_TOGGLE` | SDK-ENGE; not confirmed for the SF50 | Unverified |
| Engine switches | none yet: from the aircraft's InputEvents once installed | B-var | `B:<input event>` | README 2.1.1 | Unverified |

### Pressurization and environment

No source read gives a name for the default SF50's pressurization, bleed air, cabin temperature, fan or oxygen
controls: they come from its input event list.

| Control | Candidate name | Kind | PilotsDeck address | Source | Status |
|---|---|---|---|---|---|
| Environment switches | none yet: from the aircraft's InputEvents once installed | B-var | `B:<input event>` | README 2.1.1 | Unverified |

### Anti-ice

Standard SDK names; which of these systems the default SF50 has is not confirmed by any source read (its input
event list will show). The C172 main page keeps 4,7 for anti-ice: the draft fills it.

| Control | Candidate name | Kind | PilotsDeck address | Source | Status |
|---|---|---|---|---|---|
| Windshield de-ice | `WINDSHIELD_DEICE_TOGGLE` | K-event | `K:WINDSHIELD_DEICE_TOGGLE` | SDK-AMISCE | Unverified |
| Windshield de-ice state | `WINDSHIELD DEICE SWITCH` | SimVar | `(A:WINDSHIELD DEICE SWITCH, Bool)` | SDK-SYSV | Unverified |
| Wing and stabilizer de-ice | `TOGGLE_STRUCTURAL_DEICE` | K-event | `K:TOGGLE_STRUCTURAL_DEICE` | SDK-AMISCE | Unverified |
| Wing and stabilizer de-ice state | `STRUCTURAL DEICE SWITCH` | SimVar | `(A:STRUCTURAL DEICE SWITCH, Bool)` | SDK-SYSV | Unverified |
| Engine anti-ice | `ANTI_ICE_TOGGLE_ENG1` | K-event | `K:ANTI_ICE_TOGGLE_ENG1` | SDK-ENGE | Unverified |
| Engine anti-ice state | `ENG ANTI ICE` | SimVar | `(A:ENG ANTI ICE:1, Bool)` | SDK-ENGV | Unverified |
| Probe heat | `PITOT_HEAT_TOGGLE`, `PITOT_HEAT_SET` | K-event | `K:PITOT_HEAT_TOGGLE` | SDK-AMISCE, as [phase2-main-page.md](phase2-main-page.md) | Unverified |
| Probe heat state | `PITOT HEAT` | SimVar | `(A:PITOT HEAT, Bool)` | SDK-SYSV | Unverified |
| Anti-ice switches | none yet: from the aircraft's InputEvents once installed | B-var | `B:<input event>` | README 2.1.1 | Unverified |

### CAPS and emergency autoland

No candidate names: no source read gives a variable or event for the parachute (CAPS) or for emergency
autoland (HH-MS, WT-G3000H, the forum threads). The default SF50 has both (FORUM-24P2 for CAPS; FORUM-24 and
FORUM-AL for autoland, with reports that it finds no airport).

Working rule: no action key for either, on any page. A read-only status key only if a source gives a state.
Guard rule proposed for the case you ever ask for one: a second-level page only, never the main page; a long
press of a full second; a readout key beside it showing the state. (Open question 3.)

### Trim flaps and gear

The C172 pages' names, which are standard SimVars and events. The GEAR key reads the gear handle, and
`IS GEAR RETRACTABLE` shows whether the gear retracts. No gear event was found on the SDK flight control
events page, so the draft has no gear action key. No source names a speed brake for the SF50: none found.

| Control | Candidate name | Kind | PilotsDeck address | Source | Status |
|---|---|---|---|---|---|
| Elevator trim up, down | `ELEV_TRIM_UP`, `ELEV_TRIM_DN` | K-event | `K:ELEV_TRIM_UP` | SDK-FCE, as [phase2-trim-views.md](phase2-trim-views.md) | Unverified |
| Elevator trim readouts | `ELEVATOR TRIM PCT EX2`, `ELEVATOR TRIM POSITION` | SimVar | `(A:ELEVATOR TRIM PCT EX2, percent)` | SDK-CTLV, as [phase2-trim-views.md](phase2-trim-views.md) | Unverified |
| Flaps step | `FLAPS_INCR`, `FLAPS_DECR` | K-event | `K:FLAPS_INCR` | SDK-FCE, as [phase2-main-page.md](phase2-main-page.md) | Unverified |
| Flaps handle | `FLAPS HANDLE INDEX` | SimVar | `(A:FLAPS HANDLE INDEX, number)` | SDK-CTLV, as [phase2-main-page.md](phase2-main-page.md) | Unverified |
| Gear handle | `GEAR HANDLE POSITION` | SimVar | `(A:GEAR HANDLE POSITION, Bool)` | SDK-GEARV | Unverified |
| Gear type check | `IS GEAR RETRACTABLE` | SimVar | `(A:IS GEAR RETRACTABLE, Bool)` | SDK-GEARV | Unverified |
| Parking brake | `PARKING_BRAKES` | K-event | `K:PARKING_BRAKES` | as [phase2-main-page.md](phase2-main-page.md) | Unverified |
| Parking brake state | `BRAKE PARKING POSITION` | SimVar | `(A:BRAKE PARKING POSITION, Bool)` | SDK-GEARV | Unverified |

### Radios and transponder

The standard radio and transponder names of the C172 pages are the candidates; HubHop has no radio or
transponder preset for the default SF50. Whether its radios answer these events, and not only its touch
controllers, is not confirmed.

| Control | Candidate name | Kind | PilotsDeck address | Source | Status |
|---|---|---|---|---|---|
| COM1 swap | `COM_STBY_RADIO_SWAP` | K-event | `K:COM_STBY_RADIO_SWAP` | SDK-RADE, as [phase2-main-page.md](phase2-main-page.md) | Unverified |
| COM1 active, standby | `COM ACTIVE FREQUENCY`, `COM STANDBY FREQUENCY` | SimVar | `(A:COM ACTIVE FREQUENCY:1, MHz)` | SDK-RADV, as [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| COM1 standby ident | `COM STANDBY FREQ IDENT` | SimVar | `(A:COM STANDBY FREQ IDENT:1, String)` | SDK-RADV, as [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| NAV1, NAV2, COM2 swap and steps | `NAV1_RADIO_SWAP`, `NAV2_RADIO_SWAP`, `COM2_RADIO_SWAP`, `NAV1_RADIO_WHOLE_INC`, `NAV1_RADIO_WHOLE_DEC`, `NAV1_RADIO_FRACT_INC`, `NAV1_RADIO_FRACT_DEC`, `NAV2_RADIO_WHOLE_INC`, `NAV2_RADIO_WHOLE_DEC`, `NAV2_RADIO_FRACT_INC`, `NAV2_RADIO_FRACT_DEC`, `COM2_RADIO_WHOLE_INC`, `COM2_RADIO_WHOLE_DEC`, `COM2_RADIO_FRACT_INC`, `COM2_RADIO_FRACT_DEC` | K-event | `K:NAV1_RADIO_SWAP` and the others there | SDK-RADE, as [phase3-radios.md](phase3-radios.md) | Unverified |
| Mic select | `PILOT_TRANSMITTER_SET` | K-event | `K:PILOT_TRANSMITTER_SET:0` | SDK-RADE, as [phase3-radios.md](phase3-radios.md) | Unverified |
| NAV1, NAV2, COM2 readouts | `NAV ACTIVE FREQUENCY`, `NAV STANDBY FREQUENCY`, `NAV IDENT`, `COM ACTIVE FREQUENCY`, `COM STANDBY FREQUENCY`, `COM ACTIVE FREQ IDENT`, `COM TRANSMIT` | SimVar | `(A:NAV ACTIVE FREQUENCY:1, MHz)` and the others there | SDK-RADV, as [phase3-radios.md](phase3-radios.md) | Unverified |
| CDI source | `TOGGLE_GPS_DRIVES_NAV1` | K-event | `K:TOGGLE_GPS_DRIVES_NAV1` | SDK-RADE, as [phase2-main-page.md](phase2-main-page.md) | Unverified |
| CDI source state | `GPS DRIVES NAV1` | SimVar | `(A:GPS DRIVES NAV1, Bool)` | SDK-RADV, as [phase2-main-page.md](phase2-main-page.md) | Unverified |
| Transponder code | `TRANSPONDER CODE` | SimVar | `(A:TRANSPONDER CODE:1, Bco16)` | SDK-RADV, as [phase3-transponder.md](phase3-transponder.md) | Unverified |
| Transponder mode | `TRANSPONDER STATE` | SimVar | `(A:TRANSPONDER STATE:1, Enum)` | SDK-RADV, as [phase3-transponder.md](phase3-transponder.md) | Unverified |
| Ident | `XPNDR_IDENT_ON` | K-event | `K:XPNDR_IDENT_ON` | SDK-RADE, as [phase3-transponder.md](phase3-transponder.md) | Unverified |
| Ident state | `TRANSPONDER IDENT` | SimVar | `(A:TRANSPONDER IDENT:1, Bool)` | SDK-RADV, as [phase3-transponder.md](phase3-transponder.md) | Unverified |
| Code set (VFR key) | `XPNDR_SET` | K-event | `K:XPNDR_SET:4608` | SDK-RADE, as [phase3-transponder.md](phase3-transponder.md) | Unverified |

### Views sim rate and checklist

Views and sim rate are the C172 pages' (camera state SimVar writes, sim rate events and the sim rate script);
they are not aircraft names, and neither are the C172 main page's ATC and map window events. No checklist
event was found for the default SF50; users disagree whether its checklists work (FORUM-MAN, 2024-12-07 and
2024-12-16).

| Control | Candidate name | Kind | PilotsDeck address | Source | Status |
|---|---|---|---|---|---|
| Camera state | `CAMERA STATE` | SimVar | `(A:CAMERA STATE, Enum)` | SDK-CAMV, as [phase2-trim-views.md](phase2-trim-views.md) | Unverified |
| Camera view (readouts) | `CAMERA VIEW TYPE AND INDEX` | SimVar | `(A:CAMERA VIEW TYPE AND INDEX:0, Enum)` | SDK-CAMV, as [phase2-trim-views.md](phase2-trim-views.md) | Unverified |
| Sim rate (readout) | `SIMULATION RATE` | SimVar | `(A:SIMULATION RATE, number)` | as [phase2-sim-rate.md](phase2-sim-rate.md) | Unverified |
| Sim rate steps | `SIM_RATE_INCR`, `SIM_RATE_DECR` | K-event | `K:SIM_RATE_INCR` | SDK-MISCE, as [phase2-sim-rate.md](phase2-sim-rate.md) | Unverified |
| ATC and map windows | `SIMUI_WINDOW_HIDESHOW`, `FLIGHT_MAP` | K-event | `K:SIMUI_WINDOW_HIDESHOW` | SDK-MISCE, as [phase2-main-page.md](phase2-main-page.md) | Unverified |

## Leads from other PilotsDeck profiles

Third-party PilotsDeck profiles were looked at for ideas; none of them names a Vision Jet, SF50, G3000 or
AS3000. Nothing is taken from them beyond these ideas, and every idea stays a lead until an MSFS 2024 source
confirms it:

- A third-party PilotsDeck profile has a page of Garmin knob keys by H-event: the idea fits the GTC page
  below, but its AS1000 names do not carry over (the G3000 uses `AS3000_*` names, WT-G3000H).
- A third-party PilotsDeck package fills its `aircraft` field for profile matching: a later Vision Jet package
  can do the same (see [package.md](package.md)).
- A third-party PilotsDeck profile's view keys need extra controller bindings: this project's views must not,
  so the VIEWS page keeps the C172 method (camera state SimVar writes).
- A third-party PilotsDeck profile has a ground-service menu folder usable on any aircraft: a later folder,
  not part of this research.

## Draft layout

A draft only: nothing here is built. Rules as [navigation.md](navigation.md): one main page, child pages by
folder key, the back key at 1,1 on every child page, at most two folder levels. The main page keeps the C172
G1000 grid ([phase2-main-page.md](phase2-main-page.md)): same function, same position; a function the jet
lacks (or that no source gives yet) leaves its key empty. Every key pairs its press with the state it reads
and uses only names from the tables above.

Proposed profile name: `MSFS2024 VisionJet` (a proposal; open question 5). Pages: main; TRIM, VIEWS, SIM RATE,
CHECKLIST and MORE below it; V-SPEEDS, COM PAD, AUTOPILOT, XPDR, RADIOS, SYSTEMS, GTC, ENGINE and ICE/ENV
below MORE. MORE's PFD and MFD positions stay empty until the softkey point is settled. No CAPS or emergency
autoland action key on any page (see "CAPS and emergency autoland").

### Main page

The C172 G1000 main page grid. Changes: 1,2 shows N1 instead of RPM; 1,3 (fuel pump) stays empty, no source
gives one for the default SF50; 1,5 GEAR reads the gear handle; 4,7 fills the C172's reserved anti-ice key.

| Pos | Title | Press (candidate) | Reads (candidate) | Source | Status |
|---|---|---|---|---|---|
| 1,1 | `BAT` | B-var from the input event list; else `K:TOGGLE_MASTER_BATTERY:1` | `(A:ELECTRICAL MASTER BATTERY:1, Bool)` | SDK-ELECE; SDK-ELECV; README 2.1.1 | Unverified |
| 1,2 | `N1` | none (readout) | `(A:TURB ENG N1:1, Percent)` | SDK-ENGV | Unverified |
| 1,3 |  | Empty | none: empty (no fuel pump name for the default SF50) | - | - |
| 1,4 | `PARK` | `K:PARKING_BRAKES` | `(A:BRAKE PARKING POSITION, Bool)` | [phase2-main-page.md](phase2-main-page.md); SDK-GEARV | Unverified |
| 1,5 | `GEAR` | none (readout; the gear lever stays in the cockpit) | `(A:GEAR HANDLE POSITION, Bool)` | SDK-GEARV | Unverified |
| 1,6 | `FLAPS` | `K:FLAPS_INCR`, long press `K:FLAPS_DECR` | `(A:FLAPS HANDLE INDEX, number)` | SDK-FCE; SDK-CTLV | Unverified |
| 1,7 | `TRIM` | Folder: opens **trim** | none: folder key | [navigation.md](navigation.md) | - |
| 1,8 | `VIEWS` | Folder: opens **views** | none: folder key | [navigation.md](navigation.md) | - |
| 2,1 | `AP` | `K:AP_MASTER` | `(A:AUTOPILOT MASTER, Bool)` | SDK-APE; SDK-APV | Unverified |
| 2,2 | `HDG` | `K:AP_HDG_HOLD` | `(A:AUTOPILOT HEADING LOCK, Bool)` | SDK-APE; SDK-APV | Unverified |
| 2,3 | `ALT` | `K:AP_ALT_HOLD` | `(A:AUTOPILOT ALTITUDE LOCK, Bool)` | SDK-APE; SDK-APV | Unverified |
| 2,4 | `VS` | `K:AP_VS_HOLD` | `(A:AUTOPILOT VERTICAL HOLD, Bool)` | SDK-APE; SDK-APV | Unverified |
| 2,5 | `NAV` | `K:AP_NAV1_HOLD` | `(A:AUTOPILOT NAV1 LOCK, Bool)` | SDK-APE; SDK-APV | Unverified |
| 2,6 | `APR` | `K:AP_APR_HOLD` | `(A:AUTOPILOT APPROACH HOLD, Bool)` | SDK-APE; SDK-APV | Unverified |
| 2,7 | `FLC` | `K:FLIGHT_LEVEL_CHANGE` | `(A:AUTOPILOT FLIGHT LEVEL CHANGE, Bool)` | SDK-APE; SDK-APV | Unverified |
| 2,8 | `FD` | `K:TOGGLE_FLIGHT_DIRECTOR` | `(A:AUTOPILOT FLIGHT DIRECTOR ACTIVE, Bool)` | SDK-APE; SDK-APV | Unverified |
| 3,1 | `COM1` | `K:COM_STBY_RADIO_SWAP` | `(A:COM ACTIVE FREQUENCY:1, MHz)`, `(A:COM STANDBY FREQUENCY:1, MHz)` | [phase2-main-page.md](phase2-main-page.md) | Unverified |
| 3,2 | `XPDR` | none (readout) | `(A:TRANSPONDER CODE:1, Bco16)` | [phase2-main-page.md](phase2-main-page.md) | Unverified |
| 3,3 | `ATC` | `K:SIMUI_WINDOW_HIDESHOW` | none: no state (as the C172 main page) | [phase2-main-page.md](phase2-main-page.md) | Unverified |
| 3,4 | `MAP` | `K:FLIGHT_MAP` | none: no state (as the C172 main page) | [phase2-main-page.md](phase2-main-page.md) | Unverified |
| 3,5 | `CDI` | `K:TOGGLE_GPS_DRIVES_NAV1` | `(A:GPS DRIVES NAV1, Bool)` | [phase2-main-page.md](phase2-main-page.md) | Unverified |
| 3,6 | `BARO` | `K:BAROMETRIC` | `(A:KOHLSMAN SETTING HG:1, inHg)` | [phase2-main-page.md](phase2-main-page.md); STD: see "PFD and MFD" | Unverified |
| 3,7 | `SIM RATE` | Folder: opens **simrate** | none: folder key | [navigation.md](navigation.md) | - |
| 3,8 | `CHECKLIST` | Folder: opens **checklist** | none: folder key | [navigation.md](navigation.md) | - |
| 4,1 | `NAV LT` | B-var from the input event list; else `K:TOGGLE_NAV_LIGHTS` | `(A:LIGHT NAV, Bool)` | SDK-ELECE; SDK-SYSV; README 2.1.1 | Unverified |
| 4,2 | `BCN` | B-var from the input event list; else `K:TOGGLE_BEACON_LIGHTS` | `(A:LIGHT BEACON, Bool)` | SDK-ELECE; SDK-SYSV; README 2.1.1 | Unverified |
| 4,3 | `STRB` | B-var from the input event list; else `K:STROBES_TOGGLE` | `(A:LIGHT STROBE, Bool)` | SDK-ELECE; SDK-SYSV; README 2.1.1 | Unverified |
| 4,4 | `LDG` | B-var from the input event list; else `K:LANDING_LIGHTS_TOGGLE` | `(A:LIGHT LANDING, Bool)` | SDK-ELECE; SDK-SYSV; README 2.1.1 | Unverified |
| 4,5 | `TAXI` | B-var from the input event list; else `K:TOGGLE_TAXI_LIGHTS` | `(A:LIGHT TAXI, Bool)` | SDK-ELECE; SDK-SYSV; README 2.1.1 | Unverified |
| 4,6 | `PITOT` | B-var from the input event list; else `K:PITOT_HEAT_TOGGLE` | `(A:PITOT HEAT, Bool)` | SDK-AMISCE; SDK-SYSV; README 2.1.1 | Unverified |
| 4,7 | `A-ICE` | `K:TOGGLE_STRUCTURAL_DEICE` | `(A:STRUCTURAL DEICE SWITCH, Bool)` | SDK-AMISCE; SDK-SYSV | Unverified |
| 4,8 | `MORE` | Folder: opens **more** | none: folder key | [navigation.md](navigation.md) | - |

### TRIM

As the C172 trim page ([phase2-trim-views.md](phase2-trim-views.md)), with its trim gauge at 3,4.

| Pos | Title | Press (candidate) | Reads (candidate) | Source | Status |
|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | [navigation.md](navigation.md) | - |
| 1,2 |  | Empty | none: empty | - | - |
| 1,3 |  | Empty | none: empty | - | - |
| 1,4 |  | Empty | none: empty | - | - |
| 1,5 |  | Empty | none: empty | - | - |
| 1,6 |  | Empty | none: empty | - | - |
| 1,7 |  | Empty | none: empty | - | - |
| 1,8 |  | Empty | none: empty | - | - |
| 2,1 |  | Empty | none: empty | - | - |
| 2,2 | `TRIM UP` | `K:ELEV_TRIM_UP` | none: step key (the readouts at 3,2 to 3,4 show the result) | SDK-FCE | Unverified |
| 2,3 |  | Empty | none: empty | - | - |
| 2,4 |  | Empty | none: empty | - | - |
| 2,5 |  | Empty | none: empty | - | - |
| 2,6 |  | Empty | none: empty | - | - |
| 2,7 |  | Empty | none: empty | - | - |
| 2,8 |  | Empty | none: empty | - | - |
| 3,1 |  | Empty | none: empty | - | - |
| 3,2 | `TRIM` | none (readout) | `(A:ELEVATOR TRIM PCT EX2, percent)` | SDK-CTLV | Unverified |
| 3,3 | `TRIM DEG` | none (readout) | `(A:ELEVATOR TRIM POSITION, degrees)` | SDK-CTLV | Unverified |
| 3,4 | `TRIM` | none (a Display Gauge: a vertical bar with the number) | `(A:ELEVATOR TRIM PCT EX2, percent)` | SDK-CTLV, as [phase2-trim-views.md](phase2-trim-views.md) | Unverified |
| 3,5 |  | Empty | none: empty | - | - |
| 3,6 |  | Empty | none: empty | - | - |
| 3,7 |  | Empty | none: empty | - | - |
| 3,8 |  | Empty | none: empty | - | - |
| 4,1 |  | Empty | none: empty | - | - |
| 4,2 | `TRIM DN` | `K:ELEV_TRIM_DN` | none: step key (the readouts show the result) | SDK-FCE | Unverified |
| 4,3 |  | Empty | none: empty | - | - |
| 4,4 |  | Empty | none: empty | - | - |
| 4,5 |  | Empty | none: empty | - | - |
| 4,6 |  | Empty | none: empty | - | - |
| 4,7 |  | Empty | none: empty | - | - |
| 4,8 |  | Empty | none: empty | - | - |

### VIEWS

As the C172 views page ([phase2-trim-views.md](phase2-trim-views.md)): camera SimVar writes, no controller
bindings.

| Pos | Title | Press (candidate) | Reads (candidate) | Source | Status |
|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | [navigation.md](navigation.md) | - |
| 1,2 | `COCKPIT` | write `(A:CAMERA STATE, Enum)` = 2 | `(A:CAMERA STATE, Enum)` | SDK-CAMV | Unverified |
| 1,3 | `EXTERNAL` | write `(A:CAMERA STATE, Enum)` = 3 | `(A:CAMERA STATE, Enum)` | SDK-CAMV | Unverified |
| 1,4 | `CAMERA` | none (readout) | `(A:CAMERA STATE, Enum)` | SDK-CAMV | Unverified |
| 1,5 | `VIEW` | none (readout) | `(A:CAMERA VIEW TYPE AND INDEX:0, Enum)` | SDK-CAMV | Unverified |
| 1,6 | `VIEW NO` | none (readout) | `(A:CAMERA VIEW TYPE AND INDEX:1, number)` | SDK-CAMV | Unverified |
| 1,7 |  | Empty | none: empty | - | - |
| 1,8 |  | Empty | none: empty | - | - |
| 2,1 |  | Empty | none: empty | - | - |
| 2,2 |  | Empty | none: empty | - | - |
| 2,3 |  | Empty | none: empty | - | - |
| 2,4 |  | Empty | none: empty | - | - |
| 2,5 |  | Empty | none: empty | - | - |
| 2,6 |  | Empty | none: empty | - | - |
| 2,7 |  | Empty | none: empty | - | - |
| 2,8 |  | Empty | none: empty | - | - |
| 3,1 |  | Empty | none: empty | - | - |
| 3,2 |  | Empty | none: empty | - | - |
| 3,3 |  | Empty | none: empty | - | - |
| 3,4 |  | Empty | none: empty | - | - |
| 3,5 |  | Empty | none: empty | - | - |
| 3,6 |  | Empty | none: empty | - | - |
| 3,7 |  | Empty | none: empty | - | - |
| 3,8 |  | Empty | none: empty | - | - |
| 4,1 |  | Empty | none: empty | - | - |
| 4,2 |  | Empty | none: empty | - | - |
| 4,3 |  | Empty | none: empty | - | - |
| 4,4 |  | Empty | none: empty | - | - |
| 4,5 |  | Empty | none: empty | - | - |
| 4,6 |  | Empty | none: empty | - | - |
| 4,7 |  | Empty | none: empty | - | - |
| 4,8 |  | Empty | none: empty | - | - |

### SIM RATE

As the C172 sim rate page ([phase2-sim-rate.md](phase2-sim-rate.md)), with its Lua script.

| Pos | Title | Press (candidate) | Reads (candidate) | Source | Status |
|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | [navigation.md](navigation.md) | - |
| 1,2 | `1X` | the sim rate script, back to 1x | `(A:SIMULATION RATE, number)` | [phase2-sim-rate.md](phase2-sim-rate.md) | Unverified |
| 1,3 | `SLOWER` | `K:SIM_RATE_DECR` | none: step key (the RATE readout shows the result) | [phase2-sim-rate.md](phase2-sim-rate.md) | Unverified |
| 1,4 | `RATE` | `K:SIM_RATE_INCR`, long press `K:SIM_RATE_DECR` | `(A:SIMULATION RATE, number)` | [phase2-sim-rate.md](phase2-sim-rate.md) | Unverified |
| 1,5 | `FASTER` | `K:SIM_RATE_INCR` | none: step key (the RATE readout shows the result) | [phase2-sim-rate.md](phase2-sim-rate.md) | Unverified |
| 1,6 |  | Empty | none: empty | - | - |
| 1,7 |  | Empty | none: empty | - | - |
| 1,8 |  | Empty | none: empty | - | - |
| 2,1 |  | Empty | none: empty | - | - |
| 2,2 |  | Empty | none: empty | - | - |
| 2,3 |  | Empty | none: empty | - | - |
| 2,4 |  | Empty | none: empty | - | - |
| 2,5 |  | Empty | none: empty | - | - |
| 2,6 |  | Empty | none: empty | - | - |
| 2,7 |  | Empty | none: empty | - | - |
| 2,8 |  | Empty | none: empty | - | - |
| 3,1 |  | Empty | none: empty | - | - |
| 3,2 |  | Empty | none: empty | - | - |
| 3,3 |  | Empty | none: empty | - | - |
| 3,4 |  | Empty | none: empty | - | - |
| 3,5 |  | Empty | none: empty | - | - |
| 3,6 |  | Empty | none: empty | - | - |
| 3,7 |  | Empty | none: empty | - | - |
| 3,8 |  | Empty | none: empty | - | - |
| 4,1 |  | Empty | none: empty | - | - |
| 4,2 |  | Empty | none: empty | - | - |
| 4,3 |  | Empty | none: empty | - | - |
| 4,4 |  | Empty | none: empty | - | - |
| 4,5 |  | Empty | none: empty | - | - |
| 4,6 |  | Empty | none: empty | - | - |
| 4,7 |  | Empty | none: empty | - | - |
| 4,8 |  | Empty | none: empty | - | - |

### CHECKLIST

The C172 checklist page holds only its back key, and so does this one: no checklist event was found for the
default SF50.

| Pos | Title | Press (candidate) | Reads (candidate) | Source | Status |
|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | [navigation.md](navigation.md) | - |
| 1,2 |  | Empty | none: empty | - | - |
| 1,3 |  | Empty | none: empty | - | - |
| 1,4 |  | Empty | none: empty | - | - |
| 1,5 |  | Empty | none: empty | - | - |
| 1,6 |  | Empty | none: empty | - | - |
| 1,7 |  | Empty | none: empty | - | - |
| 1,8 |  | Empty | none: empty | - | - |
| 2,1 |  | Empty | none: empty | - | - |
| 2,2 |  | Empty | none: empty | - | - |
| 2,3 |  | Empty | none: empty | - | - |
| 2,4 |  | Empty | none: empty | - | - |
| 2,5 |  | Empty | none: empty | - | - |
| 2,6 |  | Empty | none: empty | - | - |
| 2,7 |  | Empty | none: empty | - | - |
| 2,8 |  | Empty | none: empty | - | - |
| 3,1 |  | Empty | none: empty | - | - |
| 3,2 |  | Empty | none: empty | - | - |
| 3,3 |  | Empty | none: empty | - | - |
| 3,4 |  | Empty | none: empty | - | - |
| 3,5 |  | Empty | none: empty | - | - |
| 3,6 |  | Empty | none: empty | - | - |
| 3,7 |  | Empty | none: empty | - | - |
| 3,8 |  | Empty | none: empty | - | - |
| 4,1 |  | Empty | none: empty | - | - |
| 4,2 |  | Empty | none: empty | - | - |
| 4,3 |  | Empty | none: empty | - | - |
| 4,4 |  | Empty | none: empty | - | - |
| 4,5 |  | Empty | none: empty | - | - |
| 4,6 |  | Empty | none: empty | - | - |
| 4,7 |  | Empty | none: empty | - | - |
| 4,8 |  | Empty | none: empty | - | - |

### MORE

The C172 MORE page plus three new second-level folders in row 2 (GTC, ENGINE, ICE/ENV). 1,2 PFD and 1,3 MFD
stay empty until it is known whether the SF50 displays have bezel softkeys.

| Pos | Title | Press (candidate) | Reads (candidate) | Source | Status |
|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | [navigation.md](navigation.md) | - |
| 1,2 |  | Empty | none: empty (PFD folder only if the displays have softkeys) | - | - |
| 1,3 |  | Empty | none: empty (MFD folder only if the displays have softkeys) | - | - |
| 1,4 | `V-SPEEDS` | Folder: opens **vspeeds** | none: folder key | [navigation.md](navigation.md) | - |
| 1,5 | `COM PAD` | Folder: opens **compad** | none: folder key | [navigation.md](navigation.md) | - |
| 1,6 | `AUTOPILOT` | Folder: opens **autopilot** | none: folder key | [navigation.md](navigation.md) | - |
| 1,7 | `XPDR` | Folder: opens **xpdr** | none: folder key | [navigation.md](navigation.md) | - |
| 1,8 | `RADIOS` | Folder: opens **radios** | none: folder key | [navigation.md](navigation.md) | - |
| 2,1 |  | Empty | none: empty | - | - |
| 2,2 | `SYSTEMS` | Folder: opens **systems** | none: folder key | [navigation.md](navigation.md) | - |
| 2,3 | `GTC` | Folder: opens **gtc** | none: folder key | [navigation.md](navigation.md) | - |
| 2,4 | `ENGINE` | Folder: opens **engine** | none: folder key | [navigation.md](navigation.md) | - |
| 2,5 | `ICE/ENV` | Folder: opens **iceenv** | none: folder key | [navigation.md](navigation.md) | - |
| 2,6 |  | Empty | none: empty | - | - |
| 2,7 |  | Empty | none: empty | - | - |
| 2,8 |  | Empty | none: empty | - | - |
| 3,1 |  | Empty | none: empty | - | - |
| 3,2 |  | Empty | none: empty | - | - |
| 3,3 |  | Empty | none: empty | - | - |
| 3,4 |  | Empty | none: empty | - | - |
| 3,5 |  | Empty | none: empty | - | - |
| 3,6 |  | Empty | none: empty | - | - |
| 3,7 |  | Empty | none: empty | - | - |
| 3,8 |  | Empty | none: empty | - | - |
| 4,1 |  | Empty | none: empty | - | - |
| 4,2 |  | Empty | none: empty | - | - |
| 4,3 |  | Empty | none: empty | - | - |
| 4,4 |  | Empty | none: empty | - | - |
| 4,5 |  | Empty | none: empty | - | - |
| 4,6 |  | Empty | none: empty | - | - |
| 4,7 |  | Empty | none: empty | - | - |
| 4,8 |  | Empty | none: empty | - | - |

### V-SPEEDS

As the C172 V-speeds page ([phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md)): the aircraft's design speeds.

| Pos | Title | Press (candidate) | Reads (candidate) | Source | Status |
|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | [navigation.md](navigation.md) | - |
| 1,2 | `VS0` | none (readout) | `(A:DESIGN SPEED VS0, knots)` | [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md) | Unverified |
| 1,3 | `VS1` | none (readout) | `(A:DESIGN SPEED VS1, knots)` | [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md) | Unverified |
| 1,4 | `VR` | none (readout) | `(A:DESIGN SPEED MIN ROTATION, knots)` | [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md) | Unverified |
| 1,5 |  | Empty | none: empty | - | - |
| 1,6 | `CLIMB` | none (readout) | `(A:DESIGN SPEED CLIMB, knots)` | [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md) | Unverified |
| 1,7 |  | Empty | none: empty | - | - |
| 1,8 |  | Empty | none: empty | - | - |
| 2,1 |  | Empty | none: empty | - | - |
| 2,2 | `CRUISE` | none (readout) | `(A:DESIGN SPEED VC, knots)` | [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md) | Unverified |
| 2,3 |  | Empty | none: empty | - | - |
| 2,4 | `VNE` | none (readout) | `(A:REFERENCE SPEED MAX IAS, knots)` | [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md) | Unverified |
| 2,5 | `VFE` | none (readout) | `(A:FLAPS CURRENT SPEED LIMITATION, knots)` | [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md) | Unverified |
| 2,6 |  | Empty | none: empty | - | - |
| 2,7 |  | Empty | none: empty | - | - |
| 2,8 |  | Empty | none: empty | - | - |
| 3,1 |  | Empty | none: empty | - | - |
| 3,2 |  | Empty | none: empty | - | - |
| 3,3 |  | Empty | none: empty | - | - |
| 3,4 |  | Empty | none: empty | - | - |
| 3,5 |  | Empty | none: empty | - | - |
| 3,6 |  | Empty | none: empty | - | - |
| 3,7 |  | Empty | none: empty | - | - |
| 3,8 |  | Empty | none: empty | - | - |
| 4,1 |  | Empty | none: empty | - | - |
| 4,2 |  | Empty | none: empty | - | - |
| 4,3 |  | Empty | none: empty | - | - |
| 4,4 |  | Empty | none: empty | - | - |
| 4,5 |  | Empty | none: empty | - | - |
| 4,6 |  | Empty | none: empty | - | - |
| 4,7 |  | Empty | none: empty | - | - |
| 4,8 |  | Empty | none: empty | - | - |

### COM PAD

As the C172 COM1 pad ([phase2-com1-pad.md](phase2-com1-pad.md)), with its Lua script; standard COM1 names.

| Pos | Title | Press (candidate) | Reads (candidate) | Source | Status |
|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | [navigation.md](navigation.md) | - |
| 1,2 | `COM1` | `K:COM_STBY_RADIO_SWAP` | `(A:COM ACTIVE FREQUENCY:1, MHz)`, `(A:COM STANDBY FREQUENCY:1, MHz)` | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 1,3 | `ENTRY` | none (readout of the pad script's entry) | the pad script's entry value | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 1,4 |  | Empty | none: empty | - | - |
| 1,5 |  | Empty | none: empty | - | - |
| 1,6 | `7` | the pad script: digit 7 | none: pad key (ENTRY shows the result) | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 1,7 | `8` | the pad script: digit 8 | none: pad key (ENTRY shows the result) | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 1,8 | `9` | the pad script: digit 9 | none: pad key (ENTRY shows the result) | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 2,1 |  | Empty | none: empty | - | - |
| 2,2 | `STBY ID` | none (readout) | `(A:COM STANDBY FREQ IDENT:1, String)` | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 2,3 |  | Empty | none: empty | - | - |
| 2,4 |  | Empty | none: empty | - | - |
| 2,5 |  | Empty | none: empty | - | - |
| 2,6 | `4` | the pad script: digit 4 | none: pad key (ENTRY shows the result) | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 2,7 | `5` | the pad script: digit 5 | none: pad key (ENTRY shows the result) | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 2,8 | `6` | the pad script: digit 6 | none: pad key (ENTRY shows the result) | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 3,1 |  | Empty | none: empty | - | - |
| 3,2 |  | Empty | none: empty | - | - |
| 3,3 |  | Empty | none: empty | - | - |
| 3,4 |  | Empty | none: empty | - | - |
| 3,5 |  | Empty | none: empty | - | - |
| 3,6 | `1` | the pad script: digit 1 | none: pad key (ENTRY shows the result) | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 3,7 | `2` | the pad script: digit 2 | none: pad key (ENTRY shows the result) | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 3,8 | `3` | the pad script: digit 3 | none: pad key (ENTRY shows the result) | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 4,1 |  | Empty | none: empty | - | - |
| 4,2 |  | Empty | none: empty | - | - |
| 4,3 |  | Empty | none: empty | - | - |
| 4,4 |  | Empty | none: empty | - | - |
| 4,5 |  | Empty | none: empty | - | - |
| 4,6 | `CLR` | the pad script: back, long press clear | none: pad key (ENTRY shows the result) | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 4,7 | `0` | the pad script: digit 0 | none: pad key (ENTRY shows the result) | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 4,8 | `ENT` | the pad script: enter, long press enter and swap | none: pad key (COM1 shows the result) | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |

### AUTOPILOT

The C172 autopilot page ([phase3-autopilot.md](phase3-autopilot.md)) with the jet's changes: 1,7 stays empty
(no source gives the SF50 a back-course mode); 3,7 LVL fills the position the C172 page keeps for it; 1,8 VNV
uses the L-var HubHop gives for the default SF50; course and heading sync use G3000 H events; column 8 holds
the autothrottle (A/T, TOGA, A/T MGD). 2,7 stays empty, as on the C172 page.

| Pos | Title | Press (candidate) | Reads (candidate) | Source | Status |
|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | [navigation.md](navigation.md) | - |
| 1,2 | `AP` | `K:AP_MASTER` | `(A:AUTOPILOT MASTER, Bool)` | SDK-APE; SDK-APV | Unverified |
| 1,3 | `FD` | `K:TOGGLE_FLIGHT_DIRECTOR` | `(A:AUTOPILOT FLIGHT DIRECTOR ACTIVE, Bool)` | SDK-APE; SDK-APV | Unverified |
| 1,4 | `HDG` | `K:AP_HDG_HOLD` | `(A:AUTOPILOT HEADING LOCK, Bool)` | SDK-APE; SDK-APV | Unverified |
| 1,5 | `NAV` | `K:AP_NAV1_HOLD` | `(A:AUTOPILOT NAV1 LOCK, Bool)` | SDK-APE; SDK-APV | Unverified |
| 1,6 | `APR` | `K:AP_APR_HOLD` | `(A:AUTOPILOT APPROACH HOLD, Bool)` | SDK-APE; SDK-APV | Unverified |
| 1,7 |  | Empty | none: empty (back course: no source for the SF50) | - | - |
| 1,8 | `VNV` | calculator code `(L:XMLVAR_VNAVButtonValue) ! (>L:XMLVAR_VNAVButtonValue)` | `L:XMLVAR_VNAVButtonValue` | HH-MS | Unverified |
| 2,1 | `ALT` | `K:AP_ALT_HOLD` | `(A:AUTOPILOT ALTITUDE LOCK, Bool)` | SDK-APE; SDK-APV | Unverified |
| 2,2 | `HDG+` | `K:HEADING_BUG_INC` | none: step key (HDG BUG shows the result) | SDK-APE | Unverified |
| 2,3 | `CRS+` | `H:AS3000_PFD_1_CRS_INC` | none: step key (CRS1 shows the result) | WT-G3000H | Unverified |
| 2,4 | `ALT+` | `K:AP_ALT_VAR_INC` | none: step key (ALT SEL shows the result) | SDK-APE | Unverified |
| 2,5 | `VS+` | `K:AP_VS_VAR_INC` | none: step key (VS TGT shows the result) | SDK-APE | Unverified |
| 2,6 | `SPD+` | `K:AP_SPD_VAR_INC` | none: step key (FLC SPD shows the result) | SDK-APE | Unverified |
| 2,7 |  | Empty | none: empty (as the C172 page) | - | - |
| 2,8 | `A/T` | `K:AUTO_THROTTLE_ARM` | `(A:AUTOPILOT THROTTLE ARM, Bool)` | SDK-APE; SDK-APV | Unverified |
| 3,1 | `VS` | `K:AP_VS_HOLD` | `(A:AUTOPILOT VERTICAL HOLD, Bool)` | SDK-APE; SDK-APV | Unverified |
| 3,2 | `HDG BUG` | `H:Garmin_AP_HDG_Sync` | `(A:AUTOPILOT HEADING LOCK DIR, Degrees)` | WT-G3000H; SDK-APV | Unverified |
| 3,3 | `CRS1` | `H:AS3000_PFD_1_CRS_PUSH` | `(A:NAV OBS:1, Degrees)` | WT-G3000H; as [phase3-autopilot.md](phase3-autopilot.md) | Unverified |
| 3,4 | `ALT SEL` | none (readout) | `(A:AUTOPILOT ALTITUDE LOCK VAR, Feet)` | SDK-APV | Unverified |
| 3,5 | `VS TGT` | none (readout) | `(A:AUTOPILOT VERTICAL HOLD VAR, Feet/minute)` | SDK-APV | Unverified |
| 3,6 | `FLC SPD` | none (readout) | `(A:AUTOPILOT AIRSPEED HOLD VAR, Knots)` | SDK-APV | Unverified |
| 3,7 | `LVL` | `K:AP_WING_LEVELER` | `(A:AUTOPILOT WING LEVELER, Bool)` | SDK-APE; SDK-APV | Unverified |
| 3,8 | `TOGA` | none (readout; the TOGA button stays in the cockpit) | `L:WT_TOGA_ACTIVE` | HH-MS | Unverified |
| 4,1 | `FLC` | `K:FLIGHT_LEVEL_CHANGE` | `(A:AUTOPILOT FLIGHT LEVEL CHANGE, Bool)` | SDK-APE; SDK-APV | Unverified |
| 4,2 | `HDG-` | `K:HEADING_BUG_DEC` | none: step key (HDG BUG shows the result) | SDK-APE | Unverified |
| 4,3 | `CRS-` | `H:AS3000_PFD_1_CRS_DEC` | none: step key (CRS1 shows the result) | WT-G3000H | Unverified |
| 4,4 | `ALT-` | `K:AP_ALT_VAR_DEC` | none: step key (ALT SEL shows the result) | SDK-APE | Unverified |
| 4,5 | `VS-` | `K:AP_VS_VAR_DEC` | none: step key (VS TGT shows the result) | SDK-APE | Unverified |
| 4,6 | `SPD-` | `K:AP_SPD_VAR_DEC` | none: step key (FLC SPD shows the result) | SDK-APE | Unverified |
| 4,7 |  | Empty | none: empty | - | - |
| 4,8 | `A/T MGD` | none (readout) | `(A:AUTOPILOT MANAGED THROTTLE ACTIVE, Bool)` | SDK-APV | Unverified |

### XPDR

As the C172 transponder page ([phase3-transponder.md](phase3-transponder.md)), with its Lua script.

| Pos | Title | Press (candidate) | Reads (candidate) | Source | Status |
|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | [navigation.md](navigation.md) | - |
| 1,2 | `XPDR` | none (readout) | `(A:TRANSPONDER CODE:1, Bco16)` | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 1,3 | `ENTRY` | none (readout of the pad script's entry) | the pad script's entry value | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 1,4 | `MODE` | none (readout) | `(A:TRANSPONDER STATE:1, Enum)` | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 1,5 |  | Empty | none: empty | - | - |
| 1,6 | `7` | the pad script: digit 7 | none: pad key (ENTRY shows the result) | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 1,7 |  | Empty | none: empty | - | - |
| 1,8 |  | Empty | none: empty | - | - |
| 2,1 |  | Empty | none: empty | - | - |
| 2,2 | `STBY` | write `(A:TRANSPONDER STATE:1, Enum)` = 1 | `(A:TRANSPONDER STATE:1, Enum)` | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 2,3 | `ON` | write `(A:TRANSPONDER STATE:1, Enum)` = 3 | `(A:TRANSPONDER STATE:1, Enum)` | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 2,4 | `ALT` | write `(A:TRANSPONDER STATE:1, Enum)` = 4 | `(A:TRANSPONDER STATE:1, Enum)` | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 2,5 |  | Empty | none: empty | - | - |
| 2,6 | `4` | the pad script: digit 4 | none: pad key (ENTRY shows the result) | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 2,7 | `5` | the pad script: digit 5 | none: pad key (ENTRY shows the result) | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 2,8 | `6` | the pad script: digit 6 | none: pad key (ENTRY shows the result) | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 3,1 |  | Empty | none: empty | - | - |
| 3,2 | `IDENT` | `K:XPNDR_IDENT_ON` | `(A:TRANSPONDER IDENT:1, Bool)` | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 3,3 | `VFR` | `K:XPNDR_SET:4608` | none: sets a code (XPDR shows the result) | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 3,4 |  | Empty | none: empty | - | - |
| 3,5 |  | Empty | none: empty | - | - |
| 3,6 | `1` | the pad script: digit 1 | none: pad key (ENTRY shows the result) | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 3,7 | `2` | the pad script: digit 2 | none: pad key (ENTRY shows the result) | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 3,8 | `3` | the pad script: digit 3 | none: pad key (ENTRY shows the result) | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 4,1 |  | Empty | none: empty | - | - |
| 4,2 |  | Empty | none: empty | - | - |
| 4,3 |  | Empty | none: empty | - | - |
| 4,4 |  | Empty | none: empty | - | - |
| 4,5 |  | Empty | none: empty | - | - |
| 4,6 | `CLR` | the pad script: back, long press clear | none: pad key (ENTRY shows the result) | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 4,7 | `0` | the pad script: digit 0 | none: pad key (ENTRY shows the result) | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 4,8 | `ENT` | the pad script: enter | none: pad key (XPDR shows the result) | [phase3-transponder.md](phase3-transponder.md) | Unverified |

### RADIOS

As the C172 radios page ([phase3-radios.md](phase3-radios.md)): NAV1, NAV2, COM2 and mic select by K-event.

| Pos | Title | Press (candidate) | Reads (candidate) | Source | Status |
|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | [navigation.md](navigation.md) | - |
| 1,2 | `NAV1` | `K:NAV1_RADIO_SWAP` | `(A:NAV ACTIVE FREQUENCY:1, MHz)`, `(A:NAV STANDBY FREQUENCY:1, MHz)` | [phase3-radios.md](phase3-radios.md) | Unverified |
| 1,3 | `NAV1 ID` | none (readout) | `(A:NAV IDENT:1, String)` | [phase3-radios.md](phase3-radios.md) | Unverified |
| 1,4 | `NAV2` | `K:NAV2_RADIO_SWAP` | `(A:NAV ACTIVE FREQUENCY:2, MHz)`, `(A:NAV STANDBY FREQUENCY:2, MHz)` | [phase3-radios.md](phase3-radios.md) | Unverified |
| 1,5 | `NAV2 ID` | none (readout) | `(A:NAV IDENT:2, String)` | [phase3-radios.md](phase3-radios.md) | Unverified |
| 1,6 | `COM2` | `K:COM2_RADIO_SWAP` | `(A:COM ACTIVE FREQUENCY:2, MHz)`, `(A:COM STANDBY FREQUENCY:2, MHz)` | [phase3-radios.md](phase3-radios.md) | Unverified |
| 1,7 | `COM2 ID` | none (readout) | `(A:COM ACTIVE FREQ IDENT:2, String)` | [phase3-radios.md](phase3-radios.md) | Unverified |
| 1,8 |  | Empty | none: empty | - | - |
| 2,1 |  | Empty | none: empty | - | - |
| 2,2 | `MHZ+` | `K:NAV1_RADIO_WHOLE_INC` | none: step key (NAV1 shows the result) | [phase3-radios.md](phase3-radios.md) | Unverified |
| 2,3 | `KHZ+` | `K:NAV1_RADIO_FRACT_INC` | none: step key (NAV1 shows the result) | [phase3-radios.md](phase3-radios.md) | Unverified |
| 2,4 | `MHZ+` | `K:NAV2_RADIO_WHOLE_INC` | none: step key (NAV2 shows the result) | [phase3-radios.md](phase3-radios.md) | Unverified |
| 2,5 | `KHZ+` | `K:NAV2_RADIO_FRACT_INC` | none: step key (NAV2 shows the result) | [phase3-radios.md](phase3-radios.md) | Unverified |
| 2,6 | `MHZ+` | `K:COM2_RADIO_WHOLE_INC` | none: step key (COM2 shows the result) | [phase3-radios.md](phase3-radios.md) | Unverified |
| 2,7 | `KHZ+` | `K:COM2_RADIO_FRACT_INC` | none: step key (COM2 shows the result) | [phase3-radios.md](phase3-radios.md) | Unverified |
| 2,8 |  | Empty | none: empty | - | - |
| 3,1 |  | Empty | none: empty | - | - |
| 3,2 | `MHZ-` | `K:NAV1_RADIO_WHOLE_DEC` | none: step key (NAV1 shows the result) | [phase3-radios.md](phase3-radios.md) | Unverified |
| 3,3 | `KHZ-` | `K:NAV1_RADIO_FRACT_DEC` | none: step key (NAV1 shows the result) | [phase3-radios.md](phase3-radios.md) | Unverified |
| 3,4 | `MHZ-` | `K:NAV2_RADIO_WHOLE_DEC` | none: step key (NAV2 shows the result) | [phase3-radios.md](phase3-radios.md) | Unverified |
| 3,5 | `KHZ-` | `K:NAV2_RADIO_FRACT_DEC` | none: step key (NAV2 shows the result) | [phase3-radios.md](phase3-radios.md) | Unverified |
| 3,6 | `MHZ-` | `K:COM2_RADIO_WHOLE_DEC` | none: step key (COM2 shows the result) | [phase3-radios.md](phase3-radios.md) | Unverified |
| 3,7 | `KHZ-` | `K:COM2_RADIO_FRACT_DEC` | none: step key (COM2 shows the result) | [phase3-radios.md](phase3-radios.md) | Unverified |
| 3,8 |  | Empty | none: empty | - | - |
| 4,1 |  | Empty | none: empty | - | - |
| 4,2 |  | Empty | none: empty | - | - |
| 4,3 |  | Empty | none: empty | - | - |
| 4,4 |  | Empty | none: empty | - | - |
| 4,5 |  | Empty | none: empty | - | - |
| 4,6 | `MIC1` | `K:PILOT_TRANSMITTER_SET:0` | `(A:COM TRANSMIT:1, Bool)` | [phase3-radios.md](phase3-radios.md) | Unverified |
| 4,7 | `MIC2` | `K:PILOT_TRANSMITTER_SET:1` | `(A:COM TRANSMIT:2, Bool)` | [phase3-radios.md](phase3-radios.md) | Unverified |
| 4,8 |  | Empty | none: empty | - | - |

### SYSTEMS

Replaces the C172 systems page: battery, generator, bus volts and fuel. Switches come from the input event
list where the press says so. How many batteries and generators the default SF50 has is open: 1,3 and 1,5 wait
for a second one if that list shows it. Row 2 stays empty for the interior lights and 1,7 for an avionics
master until that list is read, and row 3 for the fuel selector (no name found).

| Pos | Title | Press (candidate) | Reads (candidate) | Source | Status |
|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | [navigation.md](navigation.md) | - |
| 1,2 | `BAT` | B-var from the input event list; else `K:TOGGLE_MASTER_BATTERY:1` | `(A:ELECTRICAL MASTER BATTERY:1, Bool)` | SDK-ELECE; SDK-ELECV; README 2.1.1 | Unverified |
| 1,3 |  | Empty | none: empty (a second battery, if the input event list shows one) | - | - |
| 1,4 | `GEN` | B-var from the input event list | `(A:GENERAL ENG MASTER ALTERNATOR:1, Bool)` | SDK-ENGV; README 2.1.1 | Unverified |
| 1,5 |  | Empty | none: empty (a second generator, if the input event list shows one) | - | - |
| 1,6 | `BUS V` | none (readout) | `(A:ELECTRICAL MAIN BUS VOLTAGE:1, Volts)` | SDK-ELECV | Unverified |
| 1,7 |  | Empty | none: empty (avionics master: no name found) | - | - |
| 1,8 | `EXT PWR` | none (readout) | `(A:EXTERNAL POWER ON:1, Bool)` | SDK-ELECV | Unverified |
| 2,1 |  | Empty | none: empty | - | - |
| 2,2 |  | Empty | none: empty | - | - |
| 2,3 |  | Empty | none: empty | - | - |
| 2,4 |  | Empty | none: empty | - | - |
| 2,5 |  | Empty | none: empty | - | - |
| 2,6 |  | Empty | none: empty | - | - |
| 2,7 |  | Empty | none: empty | - | - |
| 2,8 |  | Empty | none: empty | - | - |
| 3,1 |  | Empty | none: empty | - | - |
| 3,2 |  | Empty | none: empty (fuel selector: no name found) | - | - |
| 3,3 |  | Empty | none: empty | - | - |
| 3,4 |  | Empty | none: empty | - | - |
| 3,5 |  | Empty | none: empty | - | - |
| 3,6 |  | Empty | none: empty | - | - |
| 3,7 |  | Empty | none: empty | - | - |
| 3,8 |  | Empty | none: empty | - | - |
| 4,1 |  | Empty | none: empty | - | - |
| 4,2 | `FUEL L` | none (readout) | `(A:FUEL TANK LEFT MAIN QUANTITY, Gallons)` | SDK-FUELV | Unverified |
| 4,3 | `FUEL R` | none (readout) | `(A:FUEL TANK RIGHT MAIN QUANTITY, Gallons)` | SDK-FUELV | Unverified |
| 4,4 | `FUEL TOT` | none (readout) | `(A:FUEL TOTAL QUANTITY, Gallons)` | SDK-FUELV | Unverified |
| 4,5 |  | Empty | none: empty | - | - |
| 4,6 |  | Empty | none: empty | - | - |
| 4,7 |  | Empty | none: empty | - | - |
| 4,8 |  | Empty | none: empty | - | - |

### GTC

Two touch controllers, 12 keys each: GTC 1 in columns 2-4, GTC 2 in columns 6-8 (softkeys on top, then the top
knob outer and inner rings around its push and long push, then the lower knob). Which GTC index is the pilot's
is open (open question 4), and whether the SF50's touch controllers take these horizontal GTC events is not
confirmed.

| Pos | Title | Press (candidate) | Reads (candidate) | Source | Status |
|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | [navigation.md](navigation.md) | - |
| 1,2 | `G1 SK1` | `H:AS3000_TSC_Horizontal_1_SoftKey_1` | none: no state found (a knob or softkey press) | WT-G3000H | Unverified |
| 1,3 | `G1 SK2` | `H:AS3000_TSC_Horizontal_1_SoftKey_2` | none: no state found (a knob or softkey press) | WT-G3000H | Unverified |
| 1,4 | `G1 SK3` | `H:AS3000_TSC_Horizontal_1_SoftKey_3` | none: no state found (a knob or softkey press) | WT-G3000H | Unverified |
| 1,5 |  | Empty | none: empty | - | - |
| 1,6 | `G2 SK1` | `H:AS3000_TSC_Horizontal_2_SoftKey_1` | none: no state found (a knob or softkey press) | WT-G3000H | Unverified |
| 1,7 | `G2 SK2` | `H:AS3000_TSC_Horizontal_2_SoftKey_2` | none: no state found (a knob or softkey press) | WT-G3000H | Unverified |
| 1,8 | `G2 SK3` | `H:AS3000_TSC_Horizontal_2_SoftKey_3` | none: no state found (a knob or softkey press) | WT-G3000H | Unverified |
| 2,1 |  | Empty | none: empty | - | - |
| 2,2 | `G1 TOP L-` | `H:AS3000_TSC_Horizontal_1_TopKnob_Large_DEC` | none: no state found (a knob or softkey press) | WT-G3000H | Unverified |
| 2,3 | `G1 TOP PUSH` | `H:AS3000_TSC_Horizontal_1_TopKnob_Push` | none: no state found (a knob or softkey press) | WT-G3000H | Unverified |
| 2,4 | `G1 TOP L+` | `H:AS3000_TSC_Horizontal_1_TopKnob_Large_INC` | none: no state found (a knob or softkey press) | WT-G3000H | Unverified |
| 2,5 |  | Empty | none: empty | - | - |
| 2,6 | `G2 TOP L-` | `H:AS3000_TSC_Horizontal_2_TopKnob_Large_DEC` | none: no state found (a knob or softkey press) | WT-G3000H | Unverified |
| 2,7 | `G2 TOP PUSH` | `H:AS3000_TSC_Horizontal_2_TopKnob_Push` | none: no state found (a knob or softkey press) | WT-G3000H | Unverified |
| 2,8 | `G2 TOP L+` | `H:AS3000_TSC_Horizontal_2_TopKnob_Large_INC` | none: no state found (a knob or softkey press) | WT-G3000H | Unverified |
| 3,1 |  | Empty | none: empty | - | - |
| 3,2 | `G1 TOP S-` | `H:AS3000_TSC_Horizontal_1_TopKnob_Small_DEC` | none: no state found (a knob or softkey press) | WT-G3000H | Unverified |
| 3,3 | `G1 TOP LONG` | `H:AS3000_TSC_Horizontal_1_TopKnob_Push_Long` | none: no state found (a knob or softkey press) | WT-G3000H | Unverified |
| 3,4 | `G1 TOP S+` | `H:AS3000_TSC_Horizontal_1_TopKnob_Small_INC` | none: no state found (a knob or softkey press) | WT-G3000H | Unverified |
| 3,5 |  | Empty | none: empty | - | - |
| 3,6 | `G2 TOP S-` | `H:AS3000_TSC_Horizontal_2_TopKnob_Small_DEC` | none: no state found (a knob or softkey press) | WT-G3000H | Unverified |
| 3,7 | `G2 TOP LONG` | `H:AS3000_TSC_Horizontal_2_TopKnob_Push_Long` | none: no state found (a knob or softkey press) | WT-G3000H | Unverified |
| 3,8 | `G2 TOP S+` | `H:AS3000_TSC_Horizontal_2_TopKnob_Small_INC` | none: no state found (a knob or softkey press) | WT-G3000H | Unverified |
| 4,1 |  | Empty | none: empty | - | - |
| 4,2 | `G1 LOW-` | `H:AS3000_TSC_Horizontal_1_BottomKnob_Small_DEC` | none: no state found (a knob or softkey press) | WT-G3000H | Unverified |
| 4,3 | `G1 LOW PUSH` | `H:AS3000_TSC_Horizontal_1_BottomKnob_Push` | none: no state found (a knob or softkey press) | WT-G3000H | Unverified |
| 4,4 | `G1 LOW+` | `H:AS3000_TSC_Horizontal_1_BottomKnob_Small_INC` | none: no state found (a knob or softkey press) | WT-G3000H | Unverified |
| 4,5 |  | Empty | none: empty | - | - |
| 4,6 | `G2 LOW-` | `H:AS3000_TSC_Horizontal_2_BottomKnob_Small_DEC` | none: no state found (a knob or softkey press) | WT-G3000H | Unverified |
| 4,7 | `G2 LOW PUSH` | `H:AS3000_TSC_Horizontal_2_BottomKnob_Push` | none: no state found (a knob or softkey press) | WT-G3000H | Unverified |
| 4,8 | `G2 LOW+` | `H:AS3000_TSC_Horizontal_2_BottomKnob_Small_INC` | none: no state found (a knob or softkey press) | WT-G3000H | Unverified |

### ENGINE

Readouts only: engine start, stop and ignition stay in the cockpit (no irreversible engine command on the
deck).

| Pos | Title | Press (candidate) | Reads (candidate) | Source | Status |
|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | [navigation.md](navigation.md) | - |
| 1,2 | `N1` | none (readout) | `(A:TURB ENG N1:1, Percent)` | SDK-ENGV | Unverified |
| 1,3 | `N2` | none (readout) | `(A:TURB ENG N2:1, Percent)` | SDK-ENGV | Unverified |
| 1,4 | `ITT` | none (readout) | `(A:TURB ENG ITT:1, Celsius)` | SDK-ENGV | Unverified |
| 1,5 | `FF` | none (readout) | `(A:TURB ENG FUEL FLOW PPH:1, Pounds per hour)` | SDK-ENGV | Unverified |
| 1,6 |  | Empty | none: empty | - | - |
| 1,7 |  | Empty | none: empty | - | - |
| 1,8 |  | Empty | none: empty | - | - |
| 2,1 |  | Empty | none: empty | - | - |
| 2,2 | `RUNNING` | none (readout) | `(A:GENERAL ENG COMBUSTION:1, Bool)` | SDK-ENGV | Unverified |
| 2,3 | `IGN` | none (readout) | `(A:TURB ENG IGNITION SWITCH:1, Bool)` | SDK-ENGV | Unverified |
| 2,4 |  | Empty | none: empty | - | - |
| 2,5 |  | Empty | none: empty | - | - |
| 2,6 |  | Empty | none: empty | - | - |
| 2,7 |  | Empty | none: empty | - | - |
| 2,8 |  | Empty | none: empty | - | - |
| 3,1 |  | Empty | none: empty | - | - |
| 3,2 | `FUEL TOT` | none (readout) | `(A:FUEL TOTAL QUANTITY, Gallons)` | SDK-FUELV | Unverified |
| 3,3 |  | Empty | none: empty | - | - |
| 3,4 |  | Empty | none: empty | - | - |
| 3,5 |  | Empty | none: empty | - | - |
| 3,6 |  | Empty | none: empty | - | - |
| 3,7 |  | Empty | none: empty | - | - |
| 3,8 |  | Empty | none: empty | - | - |
| 4,1 |  | Empty | none: empty | - | - |
| 4,2 |  | Empty | none: empty | - | - |
| 4,3 |  | Empty | none: empty | - | - |
| 4,4 |  | Empty | none: empty | - | - |
| 4,5 |  | Empty | none: empty | - | - |
| 4,6 |  | Empty | none: empty | - | - |
| 4,7 |  | Empty | none: empty | - | - |
| 4,8 |  | Empty | none: empty | - | - |

### ICE/ENV

Row 1: anti-ice, probe heat and the wing (ice) light by standard SDK names. Rows 2 and 3 stay empty for the
environment controls (bleed air, ECS, temperature, oxygen) until the default SF50's input event list is read:
no source gives their names.

| Pos | Title | Press (candidate) | Reads (candidate) | Source | Status |
|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | [navigation.md](navigation.md) | - |
| 1,2 | `WSHLD` | `K:WINDSHIELD_DEICE_TOGGLE` | `(A:WINDSHIELD DEICE SWITCH, Bool)` | SDK-AMISCE; SDK-SYSV | Unverified |
| 1,3 | `WING/STAB` | `K:TOGGLE_STRUCTURAL_DEICE` | `(A:STRUCTURAL DEICE SWITCH, Bool)` | SDK-AMISCE; SDK-SYSV | Unverified |
| 1,4 | `ENG A/I` | `K:ANTI_ICE_TOGGLE_ENG1` | `(A:ENG ANTI ICE:1, Bool)` | SDK-ENGE; SDK-ENGV | Unverified |
| 1,5 | `PROBE` | `K:PITOT_HEAT_TOGGLE` | `(A:PITOT HEAT, Bool)` | SDK-AMISCE; SDK-SYSV | Unverified |
| 1,6 |  | Empty | none: empty | - | - |
| 1,7 |  | Empty | none: empty | - | - |
| 1,8 | `WING LT` | B-var from the input event list; else `K:WING_LIGHTS_SET` with 1 or 0 | `(A:LIGHT WING, Bool)` | SDK-ELECE; SDK-SYSV; README 2.1.1 | Unverified |
| 2,1 |  | Empty | none: empty | - | - |
| 2,2 |  | Empty | none: empty | - | - |
| 2,3 |  | Empty | none: empty | - | - |
| 2,4 |  | Empty | none: empty | - | - |
| 2,5 |  | Empty | none: empty | - | - |
| 2,6 |  | Empty | none: empty | - | - |
| 2,7 |  | Empty | none: empty | - | - |
| 2,8 |  | Empty | none: empty | - | - |
| 3,1 |  | Empty | none: empty | - | - |
| 3,2 |  | Empty | none: empty | - | - |
| 3,3 |  | Empty | none: empty | - | - |
| 3,4 |  | Empty | none: empty | - | - |
| 3,5 |  | Empty | none: empty | - | - |
| 3,6 |  | Empty | none: empty | - | - |
| 3,7 |  | Empty | none: empty | - | - |
| 3,8 |  | Empty | none: empty | - | - |
| 4,1 |  | Empty | none: empty | - | - |
| 4,2 |  | Empty | none: empty | - | - |
| 4,3 |  | Empty | none: empty | - | - |
| 4,4 |  | Empty | none: empty | - | - |
| 4,5 |  | Empty | none: empty | - | - |
| 4,6 |  | Empty | none: empty | - | - |
| 4,7 |  | Empty | none: empty | - | - |
| 4,8 |  | Empty | none: empty | - | - |

## Open questions

1. Edition and ownership: which MSFS 2024 edition do you have, and is the default SF50 in your aircraft list
   now? A pre-release list and a user list put it in the Standard Edition (FSE-LIST, FORUM-LIST); no official
   edition list was found. Once it is in your list, loading it once with PilotsDeck running gives its input
   event list.
2. Name and variant: what does the sim call the aircraft in its aircraft selection, and does it show a variant
   such as "G2"? No official source read names one. (This changes only the wording of this page and the
   profile.)
3. CAPS and emergency autoland: confirm no action keys (the working value), or ask for a read-only status key
   only.
4. GTC page: which touch controllers matter most to you (pilot-side ones first)? The draft holds GTC 1 and GTC
   2; which index is the pilot's is open (the G3000 H event list does not say).
5. Profile name: `MSFS2024 VisionJet` or another (it must stay the same across versions).

## Sources

| Tag | Source |
|---|---|
| FSE-LIST | FSElite, all aircraft in MSFS 2024 (pre-release list from the Global Preview Event; posted 2024-09-19, updated 2024-09-23), https://fselite.net/content/all-aircraft-featured-in-microsoft-flight-simulator-2024/, read 2026-11-16 |
| FS-FAQ | Microsoft Flight Simulator 2024 FAQ (partners: FlightFX, 2024-03-13), https://www.flightsimulator.com/microsoft-flight-simulator-2024-faq/, read 2026-11-16 |
| FORUM-LIST | Official forum, user list of first-party aircraft (2025-10-09), https://forums.flightsimulator.com/t/msfs-2024-list-of-all-first-party-aircraft-with-links-to-official-info-for-each/741340, read 2026-11-16 |
| FFX-PROD | FlightFX product page, https://flightfx.io/portfolio/sf50-vision-jet, read 2026-11-16 |
| MKT-FFX | MSFS Marketplace listing, https://msfsmarket.place/aircraft/ffx-aircraft-visionjet, read 2026-11-16 |
| FORUM-24 | Official forum, MSFS2024 Cirrus SF50 Vision Jet thread, page 1, https://forums.flightsimulator.com/t/msfs2024-cirrus-sf50-vision-jet/664507, read 2026-11-16 |
| FORUM-24P2 | The same thread, page 2, https://forums.flightsimulator.com/t/msfs2024-cirrus-sf50-vision-jet/664507?page=2, read 2026-11-16 |
| FORUM-MAN | Official forum, 2024 Vision Jet aircraft manual thread, https://forums.flightsimulator.com/t/2024-vision-jet-aircraft-manual/681622, read 2026-11-16 |
| FORUM-CMP | Official forum, FlightFX 2020 versus MSFS 2024 Vision Jet thread, https://forums.flightsimulator.com/t/which-vision-jet-is-better-flightfx-ms-2020-version-or-asobos-msfs-2024-version/726660, read 2026-11-16 |
| FORUM-AL | Official forum, SF50 autoland "no airport found" thread, https://forums.flightsimulator.com/t/autoland-not-working-no-airport-found-cirrus-sf50-vision-jet/673598, read 2026-11-16 |
| FORUM-G2 | Official forum, MSFS 2024 bug report on the landing and taxi lights, titled with "Cirrus Vision Jet G2" (2024-11-20), https://forums.flightsimulator.com/t/cirrus-vision-jet-g2-landing-taxi-lights-not-producing-light/665715, read 2026-11-16 |
| WT-G3000H | MSFS Avionics Framework docs (2024), G3000 H event list, https://microsoft.github.io/msfs-avionics-mirror/2024/docs/avionics/g3000/h-event-list, read 2026-11-16 |
| HH-MS | HubHop presets, aircraft "Cirrus SF50 Vision Jet (MSFS2024)" (vendor Microsoft), https://hubhop.mobiflight.com/presets/?aircraft=Cirrus+SF50+Vision+Jet+%28MSFS2024%29, read 2026-11-16 |
| SDK-APV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-autopilot-and-assistant-variables/, read 2026-11-16 |
| SDK-APE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-autopilot-and-flight-assistance-events/, read 2026-11-16 |
| SDK-ENGV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-engine-variables/, read 2026-11-16 |
| SDK-ENGE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-engine-events/, read 2026-11-16 |
| SDK-ELECE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-electrical-events/, read 2026-11-16 |
| SDK-ELECV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-electrics-variables/, read 2026-11-16 |
| SDK-SYSV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-system-variables/, read 2026-11-16 |
| SDK-AMISCE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-miscellaneous-events/, read 2026-11-16 |
| SDK-GEARV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-brake-and-landing-gear-variables/, read 2026-11-16 |
| SDK-FCE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-flight-control-events/, read 2026-11-16 |
| SDK-FUELV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-fuel-variables/, read 2026-11-16 |
| SDK-CTLV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-control-variables/ (as in [phase2-main-page.md](phase2-main-page.md)) |
| SDK-FMV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-flight-model-variables/ (as in [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md)) |
| SDK-RADV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-radio-navigation-variables/ (as in [phase2-main-page.md](phase2-main-page.md)) |
| SDK-RADE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-radio-navigation-events/ (as in [phase2-main-page.md](phase2-main-page.md)) |
| SDK-INSTE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-instrumentation-events/ (as in [phase2-main-page.md](phase2-main-page.md)) |
| SDK-MISCE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/miscellaneous-events/ (as in [phase2-main-page.md](phase2-main-page.md)) |
| SDK-CAMV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/camera-variables/ (as in [phase2-trim-views.md](phase2-trim-views.md)) |
| SDK-UNITS | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/simulation-variable-units/ (as in [phase2-main-page.md](phase2-main-page.md)) |
| README | PilotsDeck README, https://github.com/Fragtality/PilotsDeck/blob/master/README.md (2.1.1 address syntax), as in [phase2-main-page.md](phase2-main-page.md) |
