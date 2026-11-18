# Citation CJ4 research (MSFS 2024)

## Status

Research only. Nothing here is built or sim-tested. Every name is Unverified.
When a profile is built, its names go into [aircraft-mappings.md](aircraft-mappings.md), Unverified until a
sim test passes.

This page collects what the public sources say about the Cessna Citation CJ4 that comes with MSFS 2024, the
default aircraft and the one target of this page: its name and edition, the variable and event names the
sources give for it, and a draft Stream Deck XL page layout with hold to repeat on its step keys. Add-ons and
mods for the CJ4 are not the target (see "Products"). Nothing on this page has been tried in the sim. Each name
cites its source tag (listed under "Sources", with the URL and the date it was read) and stays Unverified
until the aircraft is loaded, its input event list is read and a sim test passes.

Address forms follow the PilotsDeck README, section 2.1.1 (README). Positions are row,column, 1-based, row 1
at the top. Working values on this page (the profile name, the script name, pilot-side index 1, readouts for
the engine start controls) are proposals for the build: the build decides them, and the open questions below
may change them.

## Products

| Product | Maker | Where sold or included | Avionics | Version and date | Source |
|---|---|---|---|---|---|
| The MSFS 2024 default CJ4: "Cessna Citation CJ4" (list name and the official forum thread's title) | Asobo per a user list (FORUM-LIST); no official page read | Included in MSFS 2024 (default aircraft); the Standard Edition per a pre-release list and a user list; no official edition list found | Open: WT21-type is likely (WT21 was built to replicate the CJ4, WT21-OV), but no source read says the 2024 default runs it | none public; updated in sim update SU5 per a user list (FORUM-LIST, edit of 2026-04-30; no date given for SU5) | FSE-LIST https://fselite.net/content/all-aircraft-featured-in-microsoft-flight-simulator-2024/ (pre-release list, posted 2024-09-19, updated 2024-09-23), read 2026-11-18; FORUM-LIST read 2026-11-18; FORUM-CJ4 https://forums.flightsimulator.com/t/msfs2024-cessna-citation-cj4/664505 (first post 2024-11-18), read 2026-11-18 |
| CJ4 Plus: an add-on that extends the CJ4 (flight plan and weight import, datalink); not the target | a third party (flightsim.to) | flightsim.to, free download; says it supports MSFS 2024 and MSFS 2020 | the CJ4's own | 1.6, 2026-01-06 | CJ4P https://flightsim.to/addon/98503/cj4-plus, read 2026-11-18 |
| A realism mod for the default CJ4 (flight model, weights, engines); not the target | a third party (flightsim.to) | flightsim.to; says it is for MSFS 2020 only | the CJ4's own | 1.5.9, 2026-01-10 | CJ4RM https://flightsim.to/addon/60697/asobo-cessna-citation-cj4-realism-mod, read 2026-11-18 |
| Working Title CJ4 mod; not the target | Working Title | GitHub, free; a mod of the MSFS 2020 CJ4 | its own (the WT CJ4 avionics) | 0.10.3; repository archived 2024-05-16, before MSFS 2024 came out | WT-REL20 https://github.com/Working-Title-MSFS-Mods/fspackages/releases/tag/cj4-v0.10.3, read 2026-11-18 |

What the sources say, and what stays open:

- **Name: "Cessna Citation CJ4".** FSE-LIST, FORUM-LIST and the official forum thread (FORUM-CJ4) use it. The
  name the sim shows in its aircraft list was not read (sim step S-2).
- **Edition: the Standard Edition, not confirmed officially.** FSE-LIST is a pre-release list; FORUM-LIST is a
  user list; a search summary of another list (WC-LIST) agrees. One search of flightsimulator.com found no
  official edition page. FORUM-LIST links the official aircraft manuals page as the CJ4's guide (FS-MANUALS,
  not opened).
- **Maker: Asobo** per FORUM-LIST and the package folder name of the default CJ4 (see "Is a CJ4 installed").
- **Avionics: open.** The WT21 docs say WT21 was "initially designed to replicate" the CJ4 (WT21-OV), and its
  electronic checklist page says its default preamble is based on the CJ4 (WT21-CKL). No source read says the
  2024 default CJ4 runs WT21: the first H-event test in the sim settles it (sim step S-4).
- **Systems the sources show.** The default CJ4's checklist file names, among others: the battery switch (CKL
  7), emergency lights switch (CKL 11), standby flight display switch (CKL 15), avionics switch (CKL 19),
  climate control selector (CKL 55), an engine starter button and an engine run/stop button (CKL 66, 70),
  external power (CKL 86), a pass lights safety button (CKL 105), speed brakes and ground spoilers (CKL 117,
  436), hydraulic pressure (CKL 125), engine-only anti-ice (CKL 129), pressurization (CKL 149), the ice
  protection system (CKL 191), rudder bias (CKL 195), three trims (CKL 211), a GA button (CKL 227), battery
  amps (CKL 231), pitot/static heat buttons (CKL 239), the yaw damper (CKL 285), a landing lights button (CKL
  301) and a fuel transfer selector (CKL 366). Users of the official thread report: no engine readouts during
  the left engine's start until the avionics are on (FORUM-CJ4, 2024-11-20), no ground power (2024-11-21 and
  2024-11-29), autopilot pitch changes too abrupt on altitude capture, FLCH and VS (2024-11-22), a crash on the
  FMS POS INIT page (2024-11-22) and a flight director LNAV bar that does not move (2024-11-28).
- **Autothrottle: none found.** No source read names one for the CJ4, so the draft has no A/T key.
- **Add-ons and mods: not the target.** CJ4 Plus, the realism mod and the Working Title CJ4 mod (rows above)
  are not covered. The Working Title mod's names (WT-WIKI20) are listed below as "(MSFS 2020 mod)" candidates
  only, never alone for a 2024 key.

## Is a CJ4 installed

The default CJ4 package is present in the sim's streamed-package cache on the development PC; its systems files
are packed, only its checklist file is readable (CKL: control labels, no variable names); no add-on CJ4 is
installed. Whether the aircraft is in your aircraft list is open question 1. The aircraft's own input event
list (the `InputEvents.txt` that PilotsDeck writes once the aircraft is loaded) does not exist yet, so no B-var
name is known, and PilotsDeck's log has never seen the CJ4 (sim step S-1).

## Where the names come from

| Source | What it gives for the default CJ4 | How it was read |
|---|---|---|
| WT21 H event list for MSFS 2024 (WT21-H) | FMC, CCP, display unit, DCP and baro knob events; likely (WT21-type), not confirmed for the CJ4 | web page; it names no aircraft ("base WT21"); the names are case-sensitive |
| MSFS 2024 SDK SimVars and key events (SDK-* tags) | standard names; engine index 1 (left) and 2 (right) | web page, read from the article body (each name below was found on the page its tag names) |
| Working Title CJ4 mod wiki (WT-WIKI20) | autopilot H-events and L-vars, panel and FMC events of the MSFS 2020 mod | web page; marked "(MSFS 2020 mod)" |
| HubHop presets for the CJ4 (HH-CJ4) | open: not read (the site needs a browser) | - |
| The aircraft's own input events (B-vars) | once the aircraft has been loaded with PilotsDeck running | not available yet: B-var rows below have no name |
| The default CJ4's checklist file (CKL) | the names of its cockpit controls (labels, not variables) | the file in the sim's package cache |
| The C172 G1000 and VisionJet docs of this repo | the standard names those pages use, with their SDK tags | the linked doc |
| PilotsDeck README 2.1.1 (README) | address forms only | the repo's existing source |

How the tables write names:

- An `[index]` H-event's PilotsDeck address uses index 1, taken as the pilot side (a working value: WT21-H
  says the FMC index is "usually 1 or 2", the CCP and display unit index is the MFD's, the DCP index the PFD's,
  and does not say which is the pilot's; open question 6).
- A name the C172 or VisionJet pages already use cites that page's doc and its SDK tag ("as" the doc).
- A name only in the MSFS 2020 mod's wiki is a candidate marked "(MSFS 2020 mod)" and never fills a draft key.
- B-var rows say "none yet": the aircraft's input event list gives the names (sim step S-1). On the 2024 C172
  and the SF50 the cockpit switches drive input events, sometimes with another index than the K-event (see
  [aircraft-mappings.md](aircraft-mappings.md)), so the draft takes B-vars first and the K-events as fallbacks.

## Candidate names

Kind is one of SimVar, K-event, B-var, L-var, H-event, input event, calculator code. A SimVar's unit in the
PilotsDeck address is the one the repo's other pages use for that kind of value (SDK-UNITS). Every name is a
candidate for the default CJ4.

### FMS

The FMC (the CDU's keys). WT21-H lists 23 event rows; `[index]` is the FMC's number. No source gives a readable
state for an FMC key: FMS keys read nothing.

| Control | Candidate name | Kind | PilotsDeck address | Source | Status |
|---|---|---|---|---|---|
| Page keys IDX, FPLN, DEP ARR, LEGS | `WT21_FMC_[index]_BTN_IDX`, `..._BTN_FPLN`, `..._BTN_DEPARR`, `..._BTN_LEGS` | H-event | `H:WT21_FMC_1_BTN_FPLN` | WT21-H; not confirmed for the CJ4 | Unverified |
| Page keys DSPL MENU, MFD ADV, MFD DATA | `WT21_FMC_[index]_BTN_DSPL_MENU`, `..._BTN_MFD_ADV`, `..._BTN_MFD_DATA` | H-event | `H:WT21_FMC_1_BTN_MFD_ADV` | WT21-H; not confirmed for the CJ4 | Unverified |
| Page keys DIR, PERF, MSG, TUN | `WT21_FMC_[index]_BTN_DIR`, `..._BTN_PERF`, `..._BTN_MSG`, `..._BTN_TUN` | H-event | `H:WT21_FMC_1_BTN_DIR` | WT21-H; not confirmed for the CJ4 | Unverified |
| Line select keys L1-L6, R1-R6 | `WT21_FMC_[index]_BTN_[L\|R][1-6]` | H-event | `H:WT21_FMC_1_BTN_L1` ... `H:WT21_FMC_1_BTN_R6` | WT21-H; not confirmed for the CJ4 | Unverified |
| PREV PAGE, NEXT PAGE | `WT21_FMC_[index]_BTN_PREVPAGE`, `..._BTN_NEXTPAGE` | H-event | `H:WT21_FMC_1_BTN_NEXTPAGE` | WT21-H; not confirmed for the CJ4 | Unverified |
| Letters A-Z | `WT21_FMC_[index]_BTN_[A-Z]` | H-event | `H:WT21_FMC_1_BTN_A` | WT21-H; not confirmed for the CJ4 | Unverified |
| Digits 0-9 | `WT21_FMC_[index]_BTN_[0-9]` | H-event | `H:WT21_FMC_1_BTN_0` | WT21-H; not confirmed for the CJ4 | Unverified |
| Plus/minus, space, slash, dot | `WT21_FMC_[index]_BTN_PLUSMINUS`, `..._BTN_SP`, `..._BTN_DIV`, `..._BTN_DOT` | H-event | `H:WT21_FMC_1_BTN_DOT` | WT21-H; not confirmed for the CJ4 | Unverified |
| CLR, CLR after a long press | `WT21_FMC_[index]_BTN_CLR`, `..._BTN_CLR_LONG` | H-event | `H:WT21_FMC_1_BTN_CLR` | WT21-H; not confirmed for the CJ4 | Unverified |
| EXEC | `WT21_FMC_[index]_BTN_EXEC` | H-event | `H:WT21_FMC_1_BTN_EXEC` | WT21-H; not confirmed for the CJ4 | Unverified |
| FMC keys of the MSFS 2020 mod | `CJ4_FMC_1_BTN_*` (for example `CJ4_FMC_1_BTN_EXEC`, `CJ4_FMC_1_BTN_CLR_Long`) | H-event | `H:CJ4_FMC_1_BTN_EXEC` | WT-WIKI20 (MSFS 2020 mod) | Unverified |

### Display and cursor control panels

WT21-H's display control panel (DCP, `Generic_Upr_`, index = the PFD's) and cursor control panel (CCP,
`Generic_Lwr_`, index = the MFD's), and the display unit line select keys (index = the MFD's). No source gives
a readable state for these keys. No reversion control (display or sensor reversion) was found in WT21-H or the
other sources read.

| Control | Candidate name | Kind | PilotsDeck address | Source | Status |
|---|---|---|---|---|---|
| DCP PFD MENU, REFS MENU, ESC | `Generic_Upr_[index]_Push_PFD_MENU`, `..._Push_REFS_MENU`, `..._Push_ESC` | H-event | `H:Generic_Upr_1_Push_PFD_MENU` | WT21-H; not confirmed for the CJ4 | Unverified |
| DCP TFC, WX and TERR | `Generic_Upr_[index]_Push_TFC`, `..._Push_TERR_WX` | H-event | `H:Generic_Upr_1_Push_TFC` | WT21-H; not confirmed for the CJ4 | Unverified |
| DCP MENU ADV knob | `Generic_Upr_[index]_Push_MENU_ADV_INC`, `..._DEC` | H-event | `H:Generic_Upr_1_Push_MENU_ADV_INC` | WT21-H; not confirmed for the CJ4 | Unverified |
| DCP DATA knob | `Generic_Upr_[index]_Push_DATA_INC`, `..._DEC`, `..._PUSH` | H-event | `H:Generic_Upr_1_Push_DATA_PUSH` | WT21-H; not confirmed for the CJ4 | Unverified |
| DCP RANGE knob | `Generic_Upr_[index]_Push_RANGE_INC`, `..._DEC` | H-event | `H:Generic_Upr_1_Push_RANGE_INC` | WT21-H; not confirmed for the CJ4 | Unverified |
| DCP TILT knob | `Generic_Upr_[index]_Push_TILT_INC`, `..._DEC`, `..._PUSH` | H-event | `H:Generic_Upr_1_Push_TILT_PUSH` | WT21-H; not confirmed for the CJ4 | Unverified |
| CCP UPR MENU, LWR MENU, ESC | `Generic_Lwr_[index]_Push_UPR_MENU`, `..._Push_LWR_MENU`, `..._Push_ESC` | H-event | `H:Generic_Lwr_1_Push_UPR_MENU` | WT21-H; not confirmed for the CJ4 | Unverified |
| CCP NAV DATA, CAS PAGE, ENG, SYS | `Generic_Lwr_[index]_Push_NAV_DATA`, `..._Push_CAS_PAGE`, `..._Push_ENG`, `..._Push_SYS` | H-event | `H:Generic_Lwr_1_Push_ENG` | WT21-H; not confirmed for the CJ4 | Unverified |
| CCP TFC, WX and TERR, CKLST | `Generic_Lwr_[index]_Push_TFC`, `..._Push_TERR_WX`, `..._Push_CKLST` | H-event | `H:Generic_Lwr_1_Push_CKLST` | WT21-H; not confirmed for the CJ4 | Unverified |
| CCP MEM 1-3, push and hold | `Generic_Lwr_[index]_Push_MEM[1-3]`, `Generic_Lwr_[index]_Hold_MEM[1-3]` | H-event | `H:Generic_Lwr_1_Push_MEM1`, `H:Generic_Lwr_1_Hold_MEM1` | WT21-H; not confirmed for the CJ4 | Unverified |
| CCP ZOOM switch | `Generic_Lwr_[index]_Push_ZOOM_INC`, `..._DEC` | H-event | `H:Generic_Lwr_1_Push_ZOOM_INC` | WT21-H; not confirmed for the CJ4 | Unverified |
| CCP MENU ADV knob | `Generic_Lwr_[index]_Push_MENU_ADV_INC`, `..._DEC` | H-event | `H:Generic_Lwr_1_Push_MENU_ADV_INC` | WT21-H; not confirmed for the CJ4 | Unverified |
| CCP DATA knob | `Generic_Lwr_[index]_Push_DATA_INC`, `..._DEC`, `..._PUSH` | H-event | `H:Generic_Lwr_1_Push_DATA_PUSH` | WT21-H; not confirmed for the CJ4 | Unverified |
| CCP joystick | `Generic_Lwr_[index]_JOYSTICK_UP` (`_DOWN`, `_LEFT`, `_RIGHT`) | H-event | `H:Generic_Lwr_1_JOYSTICK_UP` | WT21-H; not confirmed for the CJ4 | Unverified |
| Display unit line select keys 1-4, left and right | `Generic_Lwr_[index]_Push_[1-4][L\|R]` | H-event | `H:Generic_Lwr_1_Push_1L` ... `H:Generic_Lwr_1_Push_4R` | WT21-H; not confirmed for the CJ4 | Unverified |
| Panel keys of the MSFS 2020 mod (no index) | `Generic_Upr_Push_PFD_MENU`, `Generic_Lwr_Push_CKLST_1`, `Generic_Lwr_DATA_PUSH_LONG` and the others there | H-event | `H:Generic_Lwr_Push_CKLST_1` | WT-WIKI20 (MSFS 2020 mod) | Unverified |

### Autopilot and flight guidance

No source read gives a name for the default CJ4's autopilot panel itself: the standard SDK names are the
candidates, as on the C172 and VisionJet autopilot pages, and the 2024 mode buttons may be input events (as the
SF50's are, [visionjet-sf50.md](visionjet-sf50.md)): sim steps S-1 and S-4 settle it. WT21-H has no autopilot
section. No 2024 VNAV event was found (SDK-APE has none); the 2020 mod's names are listed for reference only.

| Control | Candidate name | Kind | PilotsDeck address | Source | Status |
|---|---|---|---|---|---|
| Autopilot buttons | none yet: from the aircraft's InputEvents once loaded | B-var | `B:<input event>` | README 2.1.1 | Unverified |
| AP master | `AP_MASTER` | K-event | `K:AP_MASTER` | SDK-APE | Unverified |
| AP state | `AUTOPILOT MASTER` | SimVar | `(A:AUTOPILOT MASTER, Bool)` | SDK-APV, as [visionjet-g2-research.md](visionjet-g2-research.md) | Unverified |
| Flight director | `TOGGLE_FLIGHT_DIRECTOR` | K-event | `K:TOGGLE_FLIGHT_DIRECTOR` | SDK-APE | Unverified |
| Flight director state | `AUTOPILOT FLIGHT DIRECTOR ACTIVE` | SimVar | `(A:AUTOPILOT FLIGHT DIRECTOR ACTIVE, Bool)` | SDK-APV | Unverified |
| HDG mode and state | `AP_HDG_HOLD`; `AUTOPILOT HEADING LOCK` | K-event, SimVar | `K:AP_HDG_HOLD`; `(A:AUTOPILOT HEADING LOCK, Bool)` | SDK-APE; SDK-APV, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| Heading bug and step | `AUTOPILOT HEADING LOCK DIR`; `HEADING_BUG_INC`, `HEADING_BUG_DEC`, `HEADING_BUG_SET` | SimVar, K-event | `(A:AUTOPILOT HEADING LOCK DIR, Degrees)`; `K:HEADING_BUG_INC` | SDK-APV; SDK-APE, as [phase3-autopilot.md](phase3-autopilot.md) | Unverified |
| HSI needle bearing (for a heading sync key) | `HSI BEARING` | SimVar | `(A:HSI BEARING, Degrees)` | SDK-RADV | Unverified |
| NAV mode and state | `AP_NAV1_HOLD`; `AUTOPILOT NAV1 LOCK` | K-event, SimVar | `K:AP_NAV1_HOLD`; `(A:AUTOPILOT NAV1 LOCK, Bool)` | SDK-APE; SDK-APV, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| NAV source for the nav modes | `AP_NAV_SELECT_SET`; `AUTOPILOT NAV SELECTED` | K-event, SimVar | `K:AP_NAV_SELECT_SET`; `(A:AUTOPILOT NAV SELECTED, number)` | SDK-APE; SDK-APV | Unverified |
| APR mode and state | `AP_APR_HOLD`; `AUTOPILOT APPROACH HOLD` | K-event, SimVar | `K:AP_APR_HOLD`; `(A:AUTOPILOT APPROACH HOLD, Bool)` | SDK-APE; SDK-APV, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| Back course mode and state | `AP_BC_HOLD`; `AUTOPILOT BACKCOURSE HOLD` | K-event, SimVar | `K:AP_BC_HOLD`; `(A:AUTOPILOT BACKCOURSE HOLD, Bool)` | SDK-APE; SDK-APV, as [phase3-autopilot.md](phase3-autopilot.md) | Unverified |
| ALT mode, state, preselect, step | `AP_ALT_HOLD`; `AUTOPILOT ALTITUDE LOCK`; `AUTOPILOT ALTITUDE LOCK VAR`; `AP_ALT_VAR_INC`, `AP_ALT_VAR_DEC` | K-event, SimVar | `K:AP_ALT_HOLD`; `(A:AUTOPILOT ALTITUDE LOCK VAR, Feet)`; `K:AP_ALT_VAR_INC` | SDK-APE; SDK-APV, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| VS mode, state, target, step | `AP_VS_HOLD`; `AUTOPILOT VERTICAL HOLD`; `AUTOPILOT VERTICAL HOLD VAR`; `AP_VS_VAR_INC`, `AP_VS_VAR_DEC` | K-event, SimVar | `K:AP_VS_HOLD`; `(A:AUTOPILOT VERTICAL HOLD VAR, Feet/minute)`; `K:AP_VS_VAR_INC` | SDK-APE; SDK-APV, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| FLC mode and state | `FLIGHT_LEVEL_CHANGE`; `AUTOPILOT FLIGHT LEVEL CHANGE` | K-event, SimVar | `K:FLIGHT_LEVEL_CHANGE`; `(A:AUTOPILOT FLIGHT LEVEL CHANGE, Bool)` | SDK-APE; SDK-APV, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| Speed reference and step | `AUTOPILOT AIRSPEED HOLD VAR`; `AP_SPD_VAR_INC`, `AP_SPD_VAR_DEC` | SimVar, K-event | `(A:AUTOPILOT AIRSPEED HOLD VAR, Knots)`; `K:AP_SPD_VAR_INC` | SDK-APV; SDK-APE, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| IAS / Mach reference toggle and state | `AP_MANAGED_SPEED_IN_MACH_TOGGLE`; `AUTOPILOT MANAGED SPEED IN MACH` | K-event, SimVar | `K:AP_MANAGED_SPEED_IN_MACH_TOGGLE`; `(A:AUTOPILOT MANAGED SPEED IN MACH, Bool)` | SDK-APE; SDK-APV | Unverified |
| Mach hold, Mach reference and step | `AP_MACH_HOLD`, `AP_PANEL_MACH_HOLD`; `AUTOPILOT MACH HOLD`; `AUTOPILOT MACH HOLD VAR`; `AP_MACH_VAR_INC`, `AP_MACH_VAR_DEC` | K-event, SimVar | `K:AP_MACH_HOLD`; `(A:AUTOPILOT MACH HOLD VAR, number)` | SDK-APE; SDK-APV | Unverified |
| Bank limit (low bank) | `AP_MAX_BANK_INC`, `AP_MAX_BANK_DEC`, `AP_MAX_BANK_SET`; `AUTOPILOT MAX BANK ID`, `AUTOPILOT MAX BANK` | K-event, SimVar | `K:AP_MAX_BANK_INC`; `(A:AUTOPILOT MAX BANK ID, number)` | SDK-APE; SDK-APV | Unverified |
| Bank hold | `AP_BANK_HOLD`; `AUTOPILOT BANK HOLD` | K-event, SimVar | `K:AP_BANK_HOLD`; `(A:AUTOPILOT BANK HOLD, Bool)` | SDK-APE; SDK-APV | Unverified |
| Yaw damper and state | `YAW_DAMPER_TOGGLE`, `YAW_DAMPER_SET`; `AUTOPILOT YAW DAMPER` | K-event, SimVar | `K:YAW_DAMPER_TOGGLE`; `(A:AUTOPILOT YAW DAMPER, Bool)` | SDK-APE; SDK-APV, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| Course knob (NAV1) | `VOR1_OBI_INC`, `VOR1_OBI_DEC`; `NAV OBS` | K-event, SimVar | `K:VOR1_OBI_INC`; `(A:NAV OBS:1, Degrees)` | SDK-RADE, SDK-RADV, as [phase3-autopilot.md](phase3-autopilot.md) | Unverified |
| GA button (CKL 227) | `AUTO_THROTTLE_TO_GA`; `AUTOPILOT TAKEOFF POWER ACTIVE` | K-event, SimVar | `K:AUTO_THROTTLE_TO_GA`; `(A:AUTOPILOT TAKEOFF POWER ACTIVE, Bool)` | SDK-APE; SDK-APV; not confirmed for the CJ4 | Unverified |
| Autopilot mode buttons of the MSFS 2020 mod | `WT_CJ4_AP_HDG_PRESSED`, `WT_CJ4_AP_NAV_PRESSED`, `WT_CJ4_AP_APPR_PRESSED`, `WT_CJ4_AP_VNAV_PRESSED`, `WT_CJ4_AP_VS_PRESSED`, `WT_CJ4_AP_FLC_PRESSED`, `WT_CJ4_AP_ALT_PRESSED`, `WT_CJ4_AP_FD_TOGGLE` | H-event | `H:WT_CJ4_AP_VNAV_PRESSED` | WT-WIKI20 (MSFS 2020 mod) | Unverified |
| Autopilot mode lights of the MSFS 2020 mod | `WT_CJ4_HDG_ON`, `WT_CJ4_NAV_ON`, `WT_CJ4_VNAV_ON`, `WT_CJ4_VS_ON`, `WT_CJ4_FLC_ON`, `WT_CJ4_ALT_HOLD` | L-var | `L:WT_CJ4_VNAV_ON` | WT-WIKI20 (MSFS 2020 mod) | Unverified |

The baro knob is under "Views sim rate and checklist" with the other main-page names. Autothrottle: none found
(see "Products").

### Lights

On the default CJ4 the cockpit switches are likely input events (as on the 2024 C172 and the SF50): their names
come from the aircraft's input event list. The K-events and SimVars below are the standard SDK names, kept as
fallbacks. The light SimVars take a circuit index (SDK-SYSV); the rows give none, as the C172 main page does.
Which exterior lights the CJ4 has beyond "exterior lights" and a landing lights button (CKL 43, 301) is not
confirmed.

| Control | Candidate name | Kind | PilotsDeck address | Source | Status |
|---|---|---|---|---|---|
| Light switches | none yet: from the aircraft's InputEvents once loaded | B-var | `B:<input event>` | README 2.1.1 | Unverified |
| Nav lights and state | `TOGGLE_NAV_LIGHTS`; `LIGHT NAV` | K-event, SimVar | `K:TOGGLE_NAV_LIGHTS`; `(A:LIGHT NAV, Bool)` | SDK-ELECE; SDK-SYSV | Unverified |
| Beacon and state | `TOGGLE_BEACON_LIGHTS`; `LIGHT BEACON` | K-event, SimVar | `K:TOGGLE_BEACON_LIGHTS`; `(A:LIGHT BEACON, Bool)` | SDK-ELECE; SDK-SYSV | Unverified |
| Strobes and state | `STROBES_TOGGLE`; `LIGHT STROBE` | K-event, SimVar | `K:STROBES_TOGGLE`; `(A:LIGHT STROBE, Bool)` | SDK-ELECE; SDK-SYSV | Unverified |
| Landing lights and state (CKL 301) | `LANDING_LIGHTS_TOGGLE`; `LIGHT LANDING` | K-event, SimVar | `K:LANDING_LIGHTS_TOGGLE`; `(A:LIGHT LANDING, Bool)` | SDK-ELECE; SDK-SYSV | Unverified |
| Taxi lights and state | `TOGGLE_TAXI_LIGHTS`; `LIGHT TAXI` | K-event, SimVar | `K:TOGGLE_TAXI_LIGHTS`; `(A:LIGHT TAXI, Bool)` | SDK-ELECE; SDK-SYSV | Unverified |
| Recognition lights and state | `TOGGLE_RECOGNITION_LIGHTS`; `LIGHT RECOGNITION` | K-event, SimVar | `K:TOGGLE_RECOGNITION_LIGHTS`; `(A:LIGHT RECOGNITION, Bool)` | SDK-ELECE; SDK-SYSV | Unverified |
| Wing (ice) lights and state | `TOGGLE_WING_LIGHTS`, `WING_LIGHTS_SET`; `LIGHT WING` | K-event, SimVar | `K:TOGGLE_WING_LIGHTS`; `(A:LIGHT WING, Bool)` | SDK-ELECE; SDK-SYSV | Unverified |
| Logo lights and state | `TOGGLE_LOGO_LIGHTS`; `LIGHT LOGO` | K-event, SimVar | `K:TOGGLE_LOGO_LIGHTS`; `(A:LIGHT LOGO, Bool)` | SDK-ELECE; SDK-SYSV; no source says the CJ4 has one | Unverified |
| Cabin lights and state | `TOGGLE_CABIN_LIGHTS`; `LIGHT CABIN` | K-event, SimVar | `K:TOGGLE_CABIN_LIGHTS`; `(A:LIGHT CABIN, Bool)` | SDK-ELECE; SDK-SYSV | Unverified |
| Panel lights and state | `PANEL_LIGHTS_TOGGLE`; `LIGHT PANEL` | K-event, SimVar | `K:PANEL_LIGHTS_TOGGLE`; `(A:LIGHT PANEL, Bool)` | SDK-ELECE; SDK-SYSV | Unverified |
| Seat belt sign and state | `CABIN_SEATBELTS_ALERT_SWITCH_TOGGLE`; `CABIN SEATBELTS ALERT SWITCH` | K-event, SimVar | `K:CABIN_SEATBELTS_ALERT_SWITCH_TOGGLE`; `(A:CABIN SEATBELTS ALERT SWITCH, Bool)` | SDK-AMISCE; SDK-SYSV | Unverified |
| No smoking sign and state | `CABIN_NO_SMOKING_ALERT_SWITCH_TOGGLE`; `CABIN NO SMOKING ALERT SWITCH` | K-event, SimVar | `K:CABIN_NO_SMOKING_ALERT_SWITCH_TOGGLE`; `(A:CABIN NO SMOKING ALERT SWITCH, Bool)` | SDK-AMISCE; SDK-SYSV | Unverified |
| Emergency lights switch (CKL 11), pass lights safety button (CKL 105) | none yet: from the aircraft's InputEvents once loaded | B-var | `B:<input event>` | README 2.1.1 | Unverified |
| Panel lighting knob of the MSFS 2020 mod | `LIGHTING_Knob_Master` | L-var | `L:LIGHTING_Knob_Master` | WT-WIKI20 (MSFS 2020 mod) | Unverified |

### Electrical

On the 2024 C172 the battery switch drives an input event and another battery index than the K-event (see
[aircraft-mappings.md](aircraft-mappings.md)), so the CJ4's switches are taken from its input event list
first. The rows use index 1 for the battery and the left generator, 2 for the right (sim step S-3 settles the
indexes). No SDK event for the avionics switch was found (as the C172 systems page found,
[phase3-systems.md](phase3-systems.md)).

| Control | Candidate name | Kind | PilotsDeck address | Source | Status |
|---|---|---|---|---|---|
| Battery, generator, avionics, standby display and external power switches | none yet: from the aircraft's InputEvents once loaded | B-var | `B:<input event>` | README 2.1.1 | Unverified |
| Battery toggle | `TOGGLE_MASTER_BATTERY` | K-event | `K:TOGGLE_MASTER_BATTERY:1` | SDK-ELECE | Unverified |
| Battery state | `ELECTRICAL MASTER BATTERY` | SimVar | `(A:ELECTRICAL MASTER BATTERY:1, Bool)` | SDK-ELECV, as [visionjet-g2-research.md](visionjet-g2-research.md) | Unverified |
| Generator left, right | `TOGGLE_ALTERNATOR1`, `TOGGLE_ALTERNATOR2`, `ALTERNATOR_SET` | K-event | `K:TOGGLE_ALTERNATOR1` | SDK-ELECE | Unverified |
| Generator state left, right | `GENERAL ENG MASTER ALTERNATOR` | SimVar | `(A:GENERAL ENG MASTER ALTERNATOR:1, Bool)`, `:2` | SDK-ENGV | Unverified |
| Avionics state | `AVIONICS MASTER SWITCH` | SimVar | `(A:AVIONICS MASTER SWITCH:1, Bool)` | SDK-SYSV, as [phase3-systems.md](phase3-systems.md) | Unverified |
| External power switch | `TOGGLE_EXTERNAL_POWER`, `SET_EXTERNAL_POWER` | K-event | `K:TOGGLE_EXTERNAL_POWER` | SDK-ELECE; users report no ground power (FORUM-CJ4) | Unverified |
| External power state | `EXTERNAL POWER ON` | SimVar | `(A:EXTERNAL POWER ON:1, Bool)` | SDK-ELECV, as [visionjet-g2-research.md](visionjet-g2-research.md) | Unverified |
| Main bus volts | `ELECTRICAL MAIN BUS VOLTAGE` | SimVar | `(A:ELECTRICAL MAIN BUS VOLTAGE:1, Volts)` | SDK-ELECV, as [phase3-systems.md](phase3-systems.md) | Unverified |
| Battery amps (CKL 231) | `ELECTRICAL BATTERY LOAD` | SimVar | `(A:ELECTRICAL BATTERY LOAD:1, Amperes)` | SDK-ELECV, as [phase3-systems.md](phase3-systems.md) | Unverified |
| Hydraulic pressure (CKL 125) | `HYDRAULIC PRESSURE` | SimVar | `(A:HYDRAULIC PRESSURE:1, psi)` (SDK-SYSV gives psf; psi as the oil pressure readout of [phase3-engine-fuel.md](phase3-engine-fuel.md)) | SDK-SYSV | Unverified |

### Fuel

The CJ4 has a fuel transfer selector (CKL 366); no 2024 event for it was found (no crossfeed event on SDK-ENGE),
so it is a readout. Its SimVars below are standard names; which one follows the CJ4's selector is open (sim
steps S-1, S-3).

| Control | Candidate name | Kind | PilotsDeck address | Source | Status |
|---|---|---|---|---|---|
| Fuel transfer selector, fuel pumps | none yet: from the aircraft's InputEvents once loaded | B-var | `B:<input event>` | README 2.1.1 | Unverified |
| Crossfeed and transfer state | `FUEL CROSS FEED`, `FUEL SELECTED TRANSFER MODE`, `FUEL TRANSFER PUMP ON` | SimVar | `(A:FUEL CROSS FEED, Enum)` | SDK-FUELV | Unverified |
| Fuel quantity left, right, total | `FUEL TANK LEFT MAIN QUANTITY`, `FUEL TANK RIGHT MAIN QUANTITY`, `FUEL TOTAL QUANTITY` | SimVar | `(A:FUEL TANK LEFT MAIN QUANTITY, Gallons)` | SDK-FUELV, as [visionjet-g2-research.md](visionjet-g2-research.md) | Unverified |
| Fuel quantity by weight | `FUEL TOTAL QUANTITY WEIGHT`, `FUEL WEIGHT PER GALLON` | SimVar | `(A:FUEL TOTAL QUANTITY WEIGHT, Pounds)` | SDK-FUELV | Unverified |
| Engine fuel pump switch and state | `TOGGLE_ELECT_FUEL_PUMP1`, `TOGGLE_ELECT_FUEL_PUMP2`; `GENERAL ENG FUEL PUMP SWITCH`, `GENERAL ENG FUEL PUMP ON` | K-event, SimVar | `K:TOGGLE_ELECT_FUEL_PUMP1`; `(A:GENERAL ENG FUEL PUMP ON:1, Bool)` | SDK-ENGE; SDK-ENGV | Unverified |
| Engine fuel valve and state | `TOGGLE_FUEL_VALVE_ENG1`, `TOGGLE_FUEL_VALVE_ENG2`; `GENERAL ENG FUEL VALVE` | K-event, SimVar | `K:TOGGLE_FUEL_VALVE_ENG1`; `(A:GENERAL ENG FUEL VALVE:1, Bool)` | SDK-ENGE; SDK-ENGV | Unverified |
| Fuel system pumps (fuel system model) | `FUELSYSTEM PUMP SWITCH`, `FUELSYSTEM PUMP ACTIVE` | SimVar | `(A:FUELSYSTEM PUMP SWITCH:1, Bool)` | SDK-FUELV | Unverified |

### Engines

Two engines, index 1 (left) and 2 (right); no source read names the engine model. Engine start and stop stay in
the cockpit (as on the C172 and VisionJet pages: no irreversible engine command on the deck), so the starter and
run/stop controls (CKL 66, 70) are readouts in the draft and their events are candidates only.

| Control | Candidate name | Kind | PilotsDeck address | Source | Status |
|---|---|---|---|---|---|
| N1 | `TURB ENG N1`, `TURB ENG CORRECTED N1` | SimVar | `(A:TURB ENG N1:1, Percent)`, `:2` | SDK-ENGV, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| N2 | `TURB ENG N2`, `TURB ENG CORRECTED N2` | SimVar | `(A:TURB ENG N2:1, Percent)`, `:2` | SDK-ENGV, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| ITT (CKL 74) | `TURB ENG ITT` | SimVar | `(A:TURB ENG ITT:1, Celsius)`, `:2` | SDK-ENGV, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| Fuel flow | `TURB ENG FUEL FLOW PPH` | SimVar | `(A:TURB ENG FUEL FLOW PPH:1, Pounds per hour)`, `:2` | SDK-ENGV, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| Oil pressure, temperature | `GENERAL ENG OIL PRESSURE`, `GENERAL ENG OIL TEMPERATURE` | SimVar | `(A:GENERAL ENG OIL PRESSURE:1, psi)`, `(A:GENERAL ENG OIL TEMPERATURE:1, fahrenheit)` | SDK-ENGV, as [phase3-engine-fuel.md](phase3-engine-fuel.md) | Unverified |
| Engine running | `GENERAL ENG COMBUSTION` | SimVar | `(A:GENERAL ENG COMBUSTION:1, Bool)`, `:2` | SDK-ENGV | Unverified |
| Starter state | `GENERAL ENG STARTER`, `GENERAL ENG STARTER ACTIVE` | SimVar | `(A:GENERAL ENG STARTER:1, Bool)`, `:2` | SDK-ENGV | Unverified |
| Starter events | `TOGGLE_STARTER1`, `TOGGLE_STARTER2`, `STARTER1_SET`, `SET_STARTER1_HELD` | K-event | `K:TOGGLE_STARTER1` | SDK-ENGE; not used in the draft | Unverified |
| Ignition state | `TURB ENG IGNITION SWITCH`, `TURB ENG IGNITION SWITCH EX1` | SimVar | `(A:TURB ENG IGNITION SWITCH EX1:1, Enum)` | SDK-ENGV | Unverified |
| Ignition events | `TURBINE_IGNITION_SWITCH_TOGGLE`, `TURBINE_IGNITION_SWITCH_SET` | K-event | `K:TURBINE_IGNITION_SWITCH_TOGGLE` | SDK-ENGE; not used in the draft | Unverified |
| Engine starter and run/stop buttons | none yet: from the aircraft's InputEvents once loaded | B-var | `B:<input event>` | README 2.1.1 | Unverified |

### Pressurization and environment

The CJ4 has a climate control selector and pressurization (CKL 55, 149); no source read names their controls.
The SDK gives standard pressurization readouts and events.

| Control | Candidate name | Kind | PilotsDeck address | Source | Status |
|---|---|---|---|---|---|
| Climate and pressurization controls | none yet: from the aircraft's InputEvents once loaded | B-var | `B:<input event>` | README 2.1.1 | Unverified |
| Cabin altitude | `PRESSURIZATION CABIN ALTITUDE`, `PRESSURIZATION CABIN ALTITUDE GOAL` | SimVar | `(A:PRESSURIZATION CABIN ALTITUDE, Feet)` | SDK-SYSV | Unverified |
| Cabin rate | `PRESSURIZATION CABIN ALTITUDE RATE` | SimVar | `(A:PRESSURIZATION CABIN ALTITUDE RATE, Feet/minute)` (SDK-SYSV gives feet per second) | SDK-SYSV | Unverified |
| Differential pressure | `PRESSURIZATION PRESSURE DIFFERENTIAL` | SimVar | `(A:PRESSURIZATION PRESSURE DIFFERENTIAL, psi)` (SDK-SYSV gives psf) | SDK-SYSV | Unverified |
| Dump switch state | `PRESSURIZATION DUMP SWITCH` | SimVar | `(A:PRESSURIZATION DUMP SWITCH, Bool)` | SDK-SYSV | Unverified |
| Pressurization events | `PRESSURIZATION_PRESSURE_ALT_INC`, `PRESSURIZATION_PRESSURE_ALT_DEC`, `PRESSURIZATION_CLIMB_RATE_INC`, `PRESSURIZATION_CLIMB_RATE_DEC`, `PRESSURIZATION_PRESSURE_DUMP_SWITCH` | K-event | `K:PRESSURIZATION_PRESSURE_DUMP_SWITCH` | SDK-AMISCE; not used in the draft | Unverified |

### Anti-ice

The CJ4 has engine-only anti-ice, an ice protection system and pitot/static heat buttons (CKL 129, 191, 239).
Standard SDK names; which the CJ4 answers is open (its input event list will show). The pitot/static heat
buttons are two (left and right) per CKL 239; the SDK's pitot heat event and SimVar have no side.

| Control | Candidate name | Kind | PilotsDeck address | Source | Status |
|---|---|---|---|---|---|
| Anti-ice switches | none yet: from the aircraft's InputEvents once loaded | B-var | `B:<input event>` | README 2.1.1 | Unverified |
| Engine anti-ice left, right | `ANTI_ICE_TOGGLE_ENG1`, `ANTI_ICE_TOGGLE_ENG2`, `ANTI_ICE_SET_ENG1`, `ANTI_ICE_SET_ENG2` | K-event | `K:ANTI_ICE_TOGGLE_ENG1` | SDK-ENGE | Unverified |
| Engine anti-ice state | `ENG ANTI ICE`, `GENERAL ENG ANTI ICE POSITION` | SimVar | `(A:ENG ANTI ICE:1, Bool)`, `:2` | SDK-ENGV | Unverified |
| Wing and stabilizer de-ice and state | `TOGGLE_STRUCTURAL_DEICE`; `STRUCTURAL DEICE SWITCH` | K-event, SimVar | `K:TOGGLE_STRUCTURAL_DEICE`; `(A:STRUCTURAL DEICE SWITCH, Bool)` | SDK-AMISCE; SDK-SYSV | Unverified |
| Windshield heat and state | `WINDSHIELD_DEICE_TOGGLE`, `WINDSHIELD_DEICE_SET`; `WINDSHIELD DEICE SWITCH` | K-event, SimVar | `K:WINDSHIELD_DEICE_TOGGLE`; `(A:WINDSHIELD DEICE SWITCH, Bool)` | SDK-AMISCE; SDK-SYSV | Unverified |
| Pitot/static heat and state | `PITOT_HEAT_TOGGLE`, `PITOT_HEAT_SET`; `PITOT HEAT` | K-event, SimVar | `K:PITOT_HEAT_TOGGLE`; `(A:PITOT HEAT, Bool)` | SDK-AMISCE; SDK-SYSV, as [phase2-main-page.md](phase2-main-page.md) | Unverified |

### Trim flaps gear and speed brakes

Three trims (CKL 211): elevator, aileron and rudder, with the C172 trim page's names. The gear is a readout (as on
the SF50 pages; no gear event was found on SDK-FCE). The parking brake's `K:PARKING_BRAKES` failed in the SF50
(see [visionjet-sf50.md](visionjet-sf50.md)), so the CJ4's parking brake comes from its input event list first.

| Control | Candidate name | Kind | PilotsDeck address | Source | Status |
|---|---|---|---|---|---|
| Elevator trim up, down | `ELEV_TRIM_UP`, `ELEV_TRIM_DN` | K-event | `K:ELEV_TRIM_UP` | SDK-FCE, as [phase2-trim-views.md](phase2-trim-views.md) | Unverified |
| Elevator trim readout | `ELEVATOR TRIM PCT EX2`, `ELEVATOR TRIM PCT` | SimVar | `(A:ELEVATOR TRIM PCT EX2, percent)` | SDK-CTLV, as [phase2-trim-views.md](phase2-trim-views.md) | Unverified |
| Aileron trim left, right and readout | `AILERON_TRIM_LEFT`, `AILERON_TRIM_RIGHT`; `AILERON TRIM PCT` | K-event, SimVar | `K:AILERON_TRIM_LEFT`; `(A:AILERON TRIM PCT, percent)` | SDK-FCE; SDK-CTLV, as [phase2-trim-views.md](phase2-trim-views.md) | Unverified |
| Rudder trim left, right and readout | `RUDDER_TRIM_LEFT`, `RUDDER_TRIM_RIGHT`; `RUDDER TRIM PCT` | K-event, SimVar | `K:RUDDER_TRIM_LEFT`; `(A:RUDDER TRIM PCT, percent)` | SDK-FCE; SDK-CTLV, as [phase2-trim-views.md](phase2-trim-views.md) | Unverified |
| Flaps step and handle | `FLAPS_INCR`, `FLAPS_DECR`; `FLAPS HANDLE INDEX`, `FLAPS HANDLE PERCENT` | K-event, SimVar | `K:FLAPS_INCR`; `(A:FLAPS HANDLE INDEX, number)` | SDK-FCE; SDK-CTLV, as [phase2-main-page.md](phase2-main-page.md) | Unverified |
| Speed brakes (CKL 117) | `SPOILERS_TOGGLE`, `SPOILERS_ON`, `SPOILERS_OFF`, `SPOILERS_SET` | K-event | `K:SPOILERS_TOGGLE` | SDK-FCE | Unverified |
| Ground spoilers armed (CKL 436) | `SPOILERS_ARM_TOGGLE`, `SPOILERS_ARM_SET`; `SPOILERS ARMED` | K-event, SimVar | `K:SPOILERS_ARM_TOGGLE`; `(A:SPOILERS ARMED, Bool)` | SDK-FCE; SDK-CTLV | Unverified |
| Speed brake handle | `SPOILERS HANDLE POSITION` | SimVar | `(A:SPOILERS HANDLE POSITION, percent)` | SDK-CTLV | Unverified |
| Gear handle | `GEAR HANDLE POSITION` | SimVar | `(A:GEAR HANDLE POSITION, Bool)` | SDK-GEARV, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| Parking brake (fallback) | `PARKING_BRAKES` | K-event | `K:PARKING_BRAKES` | as [phase2-main-page.md](phase2-main-page.md); failed in the SF50 | Unverified |
| Parking brake state | `BRAKE PARKING POSITION` | SimVar | `(A:BRAKE PARKING POSITION, Bool)` | SDK-GEARV, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| Parking brake light | `BRAKE PARKING INDICATOR` | SimVar | `(A:BRAKE PARKING INDICATOR, Bool)` | SDK-GEARV | Unverified |
| Parking brake, rudder bias, nosewheel steering | none yet: from the aircraft's InputEvents once loaded | B-var | `B:<input event>` | README 2.1.1; MF-IE24 (the C172's parking brake input events, as an example of the form) | Unverified |

### Radios and transponder

The standard radio and transponder names of the C172 pages are the candidates. WT21-H has an FMC TUN key
(above); whether the CJ4's radios also answer these K-events is not confirmed.

| Control | Candidate name | Kind | PilotsDeck address | Source | Status |
|---|---|---|---|---|---|
| COM1 swap | `COM_STBY_RADIO_SWAP` | K-event | `K:COM_STBY_RADIO_SWAP` | SDK-RADE, as [phase2-main-page.md](phase2-main-page.md) | Unverified |
| COM1 active, standby | `COM ACTIVE FREQUENCY`, `COM STANDBY FREQUENCY` | SimVar | `(A:COM ACTIVE FREQUENCY:1, MHz)` | SDK-RADV, as [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| COM1 standby ident | `COM STANDBY FREQ IDENT` | SimVar | `(A:COM STANDBY FREQ IDENT:1, String)` | SDK-RADV, as [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| NAV1, NAV2, COM2 swap and steps | `NAV1_RADIO_SWAP`, `NAV2_RADIO_SWAP`, `COM2_RADIO_SWAP`, `NAV1_RADIO_WHOLE_INC`, `NAV1_RADIO_WHOLE_DEC`, `NAV1_RADIO_FRACT_INC`, `NAV1_RADIO_FRACT_DEC`, `NAV2_RADIO_WHOLE_INC`, `NAV2_RADIO_WHOLE_DEC`, `NAV2_RADIO_FRACT_INC`, `NAV2_RADIO_FRACT_DEC`, `COM2_RADIO_WHOLE_INC`, `COM2_RADIO_WHOLE_DEC`, `COM2_RADIO_FRACT_INC`, `COM2_RADIO_FRACT_DEC` | K-event | `K:NAV1_RADIO_SWAP` and the others there | SDK-RADE, as [phase3-radios.md](phase3-radios.md) | Unverified |
| Mic select | `PILOT_TRANSMITTER_SET` | K-event | `K:PILOT_TRANSMITTER_SET:0` | SDK-RADE, as [phase3-radios.md](phase3-radios.md) | Unverified |
| NAV1, NAV2, COM2 readouts | `NAV ACTIVE FREQUENCY`, `NAV STANDBY FREQUENCY`, `NAV IDENT`, `COM ACTIVE FREQUENCY`, `COM STANDBY FREQUENCY`, `COM ACTIVE FREQ IDENT`, `COM TRANSMIT` | SimVar | `(A:NAV ACTIVE FREQUENCY:1, MHz)` and the others there | SDK-RADV, as [phase3-radios.md](phase3-radios.md) | Unverified |
| CDI source | `TOGGLE_GPS_DRIVES_NAV1`; `GPS DRIVES NAV1` | K-event, SimVar | `K:TOGGLE_GPS_DRIVES_NAV1`; `(A:GPS DRIVES NAV1, Bool)` | SDK-RADE; SDK-RADV, as [phase2-main-page.md](phase2-main-page.md) | Unverified |
| Transponder code, mode, ident | `TRANSPONDER CODE`, `TRANSPONDER STATE`, `TRANSPONDER IDENT`; `XPNDR_IDENT_ON`, `XPNDR_SET` | SimVar, K-event | `(A:TRANSPONDER CODE:1, Bco16)`; `K:XPNDR_IDENT_ON` | SDK-RADV; SDK-RADE, as [phase3-transponder.md](phase3-transponder.md) | Unverified |

### Views sim rate and checklist

Views and sim rate are the C172 pages' (camera state SimVar writes, sim rate events and the sim rate script);
they are not aircraft names, and neither are the C172 main page's ATC and map window events. The checklist: the
CCP's CKLST key (WT21-H) likely shows it: a WT21 aircraft shows its checklists on the MFD (WT21-CKL), but no
source read says which key opens them. The default CJ4 has a checklist file (CKL). The baro names are here
because the main page holds BARO.

| Control | Candidate name | Kind | PilotsDeck address | Source | Status |
|---|---|---|---|---|---|
| Camera state | `CAMERA STATE` | SimVar | `(A:CAMERA STATE, Enum)` | SDK-CAMV, as [phase2-trim-views.md](phase2-trim-views.md) | Unverified |
| Camera view (readouts) | `CAMERA VIEW TYPE AND INDEX` | SimVar | `(A:CAMERA VIEW TYPE AND INDEX:0, Enum)` | SDK-CAMV, as [phase2-trim-views.md](phase2-trim-views.md) | Unverified |
| Sim rate (readout) | `SIMULATION RATE` | SimVar | `(A:SIMULATION RATE, number)` | as [phase2-sim-rate.md](phase2-sim-rate.md) | Unverified |
| Sim rate steps | `SIM_RATE_INCR`, `SIM_RATE_DECR` | K-event | `K:SIM_RATE_INCR` | SDK-MISCE, as [phase2-sim-rate.md](phase2-sim-rate.md) | Unverified |
| ATC and map windows | `SIMUI_WINDOW_HIDESHOW`, `FLIGHT_MAP` | K-event | `K:SIMUI_WINDOW_HIDESHOW` | SDK-MISCE, as [phase2-main-page.md](phase2-main-page.md) | Unverified |
| Checklist key (CCP) | `Generic_Lwr_[index]_Push_CKLST` | H-event | `H:Generic_Lwr_1_Push_CKLST` | WT21-H; WT21-CKL; not confirmed for the CJ4 | Unverified |
| Baro knob (WT21) | `AP_BARO_Up`, `AP_BARO_Down` | H-event | `H:AP_BARO_Up` | WT21-H; not confirmed for the CJ4 | Unverified |
| Baro knob (SDK) | `KOHLSMAN_INC`, `KOHLSMAN_DEC` | K-event | `K:KOHLSMAN_INC` | SDK-INSTE, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| Baro sync and standard | `BAROMETRIC`, `BAROMETRIC_STD_PRESSURE` | K-event | `K:BAROMETRIC` | SDK-INSTE, as [phase2-main-page.md](phase2-main-page.md) and [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| Baro setting (readout) | `KOHLSMAN SETTING HG` | SimVar | `(A:KOHLSMAN SETTING HG:1, inHg)` | SDK-SYSV, as [phase2-main-page.md](phase2-main-page.md) | Unverified |
| V-speed readouts | `DESIGN SPEED VS0`, `DESIGN SPEED VS1`, `DESIGN SPEED MIN ROTATION`, `DESIGN SPEED CLIMB`, `DESIGN SPEED VC`, `REFERENCE SPEED MAX IAS` | SimVar | `(A:DESIGN SPEED VS0, knots)` and the others there | SDK-FMV, as [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md) | Unverified |
| Flap speed limit (readout) | `FLAPS CURRENT SPEED LIMITATION` | SimVar | `(A:FLAPS CURRENT SPEED LIMITATION, knots)` | SDK-CTLV, as [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md) | Unverified |

## Leads from other Stream Deck profiles

A third-party CJ4 profile for another Stream Deck plugin (a 15-key deck) and third-party PilotsDeck profiles
were looked at for ideas. Ideas taken (in this page's own words): a full FMS set (function keys, line select
keys, a letter and digit keyboard on their own pages); left and right engine pairs on one page; flaps, fuel and
trim readouts near the main page; autopilot targets shown beside the mode keys; index-2 radio readouts; a
cursor or joystick block. The third-party CJ4 profile has data errors on some keys, so it is never a source.

Names seen only in those profiles stay leads until an MSFS 2024 source confirms them. Names they use that an SDK
page confirmed (for example `AP_MASTER`, `TURB ENG CORRECTED N1`, `GENERAL ENG ANTI ICE POSITION`,
`CABIN_NO_SMOKING_ALERT_SWITCH_TOGGLE`, `TOGGLE_RECOGNITION_LIGHTS`) are in the candidate tables above with their
SDK tags, not here. The CJ4 profile's FMC keys are confirmed only as an idea, under the WT21 names (WT21-H).

| Control | Lead name | Kind | Seen in | Status |
|---|---|---|---|---|
| FMC keys (function keys, line select keys, letters, digits) | `MOBIFLIGHT_CJ4_FMC_1_BTN_*` (for example `MOBIFLIGHT_CJ4_FMC_1_BTN_EXEC`) | event of the MobiFlight event module (MSFS 2020 era) | a third-party CJ4 profile for another Stream Deck plugin | lead, needs a source |
| Gear | `GEAR_TOGGLE` | K-event | a third-party CJ4 profile for another Stream Deck plugin | lead, needs a source (not on SDK-FCE) |
| Flaps, fuel and trim gauges | gauge names written with underscores (for example `FLAPS_HANDLE_PERCENT`, `ELEVATOR_TRIM_PCT`) | the other plugin's own forms | a third-party CJ4 profile for another Stream Deck plugin | lead, needs a source (the SDK spellings are in the tables above) |
| Engine pairs | engine items named per engine (left and right) | B-var with an index | a third-party PilotsDeck profile | lead, needs a source |

## Hold to repeat

The CJ4 profile is built with hold to repeat on its step keys from its first build, by the route of the SF50
profile ([visionjet-sf50.md](visionjet-sf50.md), "Hold to repeat"): each step key is a Simple Button with Hold
Switch on; key down runs `lua:XL24-CJ4:HOLD(n)`, key up `lua:XL24-CJ4:RELEASE(n)`; per-key caps and speed
profiles; 50 ms ticks; the repeat stops at key up, at the key's cap or after about 20 s.

- **Script (working value):** a new script `Scripts/XL24-CJ4.lua` with its own key table; the SF50's script
  stays as it is. If one shared script is chosen instead, the SF50 script, its doc and its hold test change in
  the build.
- **Keys (30 codes, working list):** autopilot HDG+/-, CRS+/-, ALT+/-, VS+/-, SPD+/- (codes 1-10); BARO+/- (11,
  12); radios MHZ and KHZ +/- for NAV1, NAV2 and COM2 (13-24); trim elevator UP/DN, aileron L/R, rudder L/R
  (25-30). The draft gives each key's code and its profile and cap (the SF50's profile names: fast, alt, slow,
  baro, trim).
- **Never repeated:** mode keys, flaps, gear, sim rate, B-var switches, FMS, DCP and CCP keys, the pads, PARK.
- **Input events:** if the CJ4's knobs answer only input events (sim steps S-1, S-4), the build decides whether
  the script may send them.
- **Waits on:** the SF50's hold test in the sim. If that test fails, the CJ4 build takes the SF50 profile's
  fallbacks ([visionjet-sf50.md](visionjet-sf50.md), "Fallbacks"). The build that adds the script also names it
  in the package notes ([package.md](package.md)).

| Profile | Keys | Cap per hold |
|---|---|---|
| fast | HDG, CRS, SPD, the KHZ keys | HDG, CRS 360; SPD, KHZ 200 |
| alt | ALT | 400 |
| slow | VS, the MHZ keys | VS 40, MHZ 30 |
| baro | BARO+, BARO- | 200 |
| trim | the six trim keys | 160 |

The times and speeds of each profile are the SF50's ([visionjet-sf50.md](visionjet-sf50.md), "Hold to repeat").

## Draft layout

A draft only: nothing here is built. Rules as [navigation.md](navigation.md): one main page, child pages by
folder key, the back key at 1,1 on every child page, at most two folder levels. The main page keeps the SF50
and C172 G1000 grid: same function, same position; a function the jet lacks (or that no source gives yet)
leaves its key empty. Every key pairs its press with the state it reads, a state key's On and Off images both
follow its own read (never an image for a state), and every key uses only names from the tables above.

Proposed profile name: `MSFS2024 CJ4` (a working value; open question 4). Pages: main; TRIM, VIEWS, SIM RATE,
CHECKLIST and MORE below it; DCP, CCP, V-SPEEDS, COM PAD, AUTOPILOT, XPDR, RADIOS, SYSTEMS, ENGINE, ICE/ENV,
LIGHTS, FMS, FMS ABC and FMS 123 below MORE (20 pages). "Hold to repeat" is `yes (<profile>, <cap>)` with the
SF50 profile names (see "Hold to repeat"), or `-`. "B-var from the input event list (S-1)" means the switch's
input event, once that list exists; the K-event after "else" is the fallback.

### Main page

The SF50 main page grid ([visionjet-sf50.md](visionjet-sf50.md), "Layouts"): same function, same position. Changes:
1,3 stays empty (no fuel pump key; the pumps are readouts on SYSTEMS); 4,2 is the beacon (the SF50 has none; the
CJ4's recognition lights are on LIGHTS); BARO gets the SF50's long press for standard pressure. No key on the main
page repeats.

| Pos | Title | Press (candidate) | Reads (candidate) | Hold to repeat | Source | Status |
|---|---|---|---|---|---|---|
| 1,1 | `BAT` | B-var from the input event list (S-1); else `K:TOGGLE_MASTER_BATTERY:1` | `(A:ELECTRICAL MASTER BATTERY:1, Bool)` | - | SDK-ELECE; SDK-ELECV; README 2.1.1; CKL 7 | Unverified |
| 1,2 | `N1` | none (readout) | `(A:TURB ENG N1:1, Percent)` (left; right on ENGINE) | - | SDK-ENGV | Unverified |
| 1,3 |  | Empty | none: empty | - | - | - |
| 1,4 | `PARK` | B-var from the input event list (S-1); else `K:PARKING_BRAKES` | `(A:BRAKE PARKING POSITION, Bool)` | - | [phase2-main-page.md](phase2-main-page.md); SDK-GEARV; README 2.1.1 | Unverified |
| 1,5 | `GEAR` | none (readout; the gear lever stays in the cockpit) | `(A:GEAR HANDLE POSITION, Bool)` | - | SDK-GEARV | Unverified |
| 1,6 | `FLAPS` | `K:FLAPS_INCR`, long press `K:FLAPS_DECR` | `(A:FLAPS HANDLE INDEX, number)` | - | SDK-FCE; SDK-CTLV | Unverified |
| 1,7 | `TRIM` | Folder: opens **trim** | none: folder key | - | [navigation.md](navigation.md) | - |
| 1,8 | `VIEWS` | Folder: opens **views** | none: folder key | - | [navigation.md](navigation.md) | - |
| 2,1 | `AP` | `K:AP_MASTER` | `(A:AUTOPILOT MASTER, Bool)` | - | SDK-APE; SDK-APV | Unverified |
| 2,2 | `HDG` | `K:AP_HDG_HOLD` | `(A:AUTOPILOT HEADING LOCK, Bool)` | - | SDK-APE; SDK-APV | Unverified |
| 2,3 | `ALT` | `K:AP_ALT_HOLD` | `(A:AUTOPILOT ALTITUDE LOCK, Bool)` | - | SDK-APE; SDK-APV | Unverified |
| 2,4 | `VS` | `K:AP_VS_HOLD` | `(A:AUTOPILOT VERTICAL HOLD, Bool)` | - | SDK-APE; SDK-APV | Unverified |
| 2,5 | `NAV` | `K:AP_NAV1_HOLD` | `(A:AUTOPILOT NAV1 LOCK, Bool)` | - | SDK-APE; SDK-APV | Unverified |
| 2,6 | `APR` | `K:AP_APR_HOLD` | `(A:AUTOPILOT APPROACH HOLD, Bool)` | - | SDK-APE; SDK-APV | Unverified |
| 2,7 | `FLC` | `K:FLIGHT_LEVEL_CHANGE` | `(A:AUTOPILOT FLIGHT LEVEL CHANGE, Bool)` | - | SDK-APE; SDK-APV | Unverified |
| 2,8 | `FD` | `K:TOGGLE_FLIGHT_DIRECTOR` | `(A:AUTOPILOT FLIGHT DIRECTOR ACTIVE, Bool)` | - | SDK-APE; SDK-APV | Unverified |
| 3,1 | `COM1` | `K:COM_STBY_RADIO_SWAP` | `(A:COM ACTIVE FREQUENCY:1, MHz)`, `(A:COM STANDBY FREQUENCY:1, MHz)` | - | [phase2-main-page.md](phase2-main-page.md) | Unverified |
| 3,2 | `XPDR` | none (readout) | `(A:TRANSPONDER CODE:1, Bco16)` | - | [phase2-main-page.md](phase2-main-page.md) | Unverified |
| 3,3 | `ATC` | `K:SIMUI_WINDOW_HIDESHOW` | none: no state (as the C172 main page) | - | [phase2-main-page.md](phase2-main-page.md) | Unverified |
| 3,4 | `MAP` | `K:FLIGHT_MAP` | none: no state (as the C172 main page) | - | [phase2-main-page.md](phase2-main-page.md) | Unverified |
| 3,5 | `CDI` | `K:TOGGLE_GPS_DRIVES_NAV1` | `(A:GPS DRIVES NAV1, Bool)` | - | [phase2-main-page.md](phase2-main-page.md); the CJ4's NAV source: S-4 | Unverified |
| 3,6 | `BARO` | `K:BAROMETRIC`, long press `K:BAROMETRIC_STD_PRESSURE` | `(A:KOHLSMAN SETTING HG:1, inHg)` | - | [phase2-main-page.md](phase2-main-page.md); [visionjet-sf50.md](visionjet-sf50.md); CKL 145 | Unverified |
| 3,7 | `SIM RATE` | Folder: opens **simrate** | none: folder key | - | [navigation.md](navigation.md) | - |
| 3,8 | `CHECKLIST` | Folder: opens **checklist** | none: folder key | - | [navigation.md](navigation.md) | - |
| 4,1 | `NAV LT` | B-var from the input event list (S-1); else `K:TOGGLE_NAV_LIGHTS` | `(A:LIGHT NAV, Bool)` | - | SDK-ELECE; SDK-SYSV; README 2.1.1 | Unverified |
| 4,2 | `BCN` | B-var from the input event list (S-1); else `K:TOGGLE_BEACON_LIGHTS` | `(A:LIGHT BEACON, Bool)` | - | SDK-ELECE; SDK-SYSV; README 2.1.1 | Unverified |
| 4,3 | `STRB` | B-var from the input event list (S-1); else `K:STROBES_TOGGLE` | `(A:LIGHT STROBE, Bool)` | - | SDK-ELECE; SDK-SYSV; README 2.1.1 | Unverified |
| 4,4 | `LDG` | B-var from the input event list (S-1); else `K:LANDING_LIGHTS_TOGGLE` | `(A:LIGHT LANDING, Bool)` | - | SDK-ELECE; SDK-SYSV; README 2.1.1; CKL 301 | Unverified |
| 4,5 | `TAXI` | B-var from the input event list (S-1); else `K:TOGGLE_TAXI_LIGHTS` | `(A:LIGHT TAXI, Bool)` | - | SDK-ELECE; SDK-SYSV; README 2.1.1 | Unverified |
| 4,6 | `PITOT` | B-var from the input event list (S-1); else `K:PITOT_HEAT_TOGGLE` | `(A:PITOT HEAT, Bool)` | - | SDK-AMISCE; SDK-SYSV; README 2.1.1; CKL 239 | Unverified |
| 4,7 | `ICE` | B-var from the input event list (S-1); else `K:TOGGLE_STRUCTURAL_DEICE` | `(A:STRUCTURAL DEICE SWITCH, Bool)` | - | SDK-AMISCE; SDK-SYSV; README 2.1.1; CKL 191 | Unverified |
| 4,8 | `MORE` | Folder: opens **more** | none: folder key | - | [navigation.md](navigation.md) | - |

### TRIM

Opened by main 1,7. The C172's current trim page ([phase2-trim-views.md](phase2-trim-views.md)) with its aileron
trim keys kept (the CJ4 has three trims, CKL 211); all six trim keys hold to repeat.

| Pos | Title | Press (candidate) | Reads (candidate) | Hold to repeat | Source | Status |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | - | [navigation.md](navigation.md) | - |
| 1,2 |  | Empty | none: empty | - | - | - |
| 1,3 |  | Empty | none: empty | - | - | - |
| 1,4 |  | Empty | none: empty | - | - | - |
| 1,5 |  | Empty | none: empty | - | - | - |
| 1,6 |  | Empty | none: empty | - | - | - |
| 1,7 |  | Empty | none: empty | - | - | - |
| 1,8 |  | Empty | none: empty | - | - | - |
| 2,1 |  | Empty | none: empty | - | - | - |
| 2,2 | `TRIM UP` | `lua:XL24-CJ4:HOLD(25)` key down, `lua:XL24-CJ4:RELEASE(25)` key up; the script sends `K:ELEV_TRIM_UP` | none: step key (the gauge at 3,4 shows the result) | yes (trim, 160) | SDK-FCE, as [phase2-trim-views.md](phase2-trim-views.md); README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 2,3 |  | Empty | none: empty | - | - | - |
| 2,4 |  | Empty | none: empty | - | - | - |
| 2,5 |  | Empty | none: empty | - | - | - |
| 2,6 | `AIL L` | `lua:XL24-CJ4:HOLD(27)` key down, `lua:XL24-CJ4:RELEASE(27)` key up; the script sends `K:AILERON_TRIM_LEFT` | none: step key (the gauge at 2,7 shows the result) | yes (trim, 160) | SDK-FCE, as [phase2-trim-views.md](phase2-trim-views.md); README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 2,7 | `AIL TRIM` | none (a Display Gauge, as the C172's) | `(A:AILERON TRIM PCT, percent)` | - | SDK-CTLV, as [phase2-trim-views.md](phase2-trim-views.md) | Unverified |
| 2,8 | `AIL R` | `lua:XL24-CJ4:HOLD(28)` key down, `lua:XL24-CJ4:RELEASE(28)` key up; the script sends `K:AILERON_TRIM_RIGHT` | none: step key (the gauge at 2,7 shows the result) | yes (trim, 160) | SDK-FCE, as [phase2-trim-views.md](phase2-trim-views.md); README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 3,1 |  | Empty | none: empty | - | - | - |
| 3,2 |  | Empty | none: empty | - | - | - |
| 3,3 |  | Empty | none: empty | - | - | - |
| 3,4 | `TRIM` | none (a Display Gauge, as the C172's) | `(A:ELEVATOR TRIM PCT EX2, percent)` | - | SDK-CTLV, as [phase2-trim-views.md](phase2-trim-views.md) | Unverified |
| 3,5 |  | Empty | none: empty | - | - | - |
| 3,6 | `RUD L` | `lua:XL24-CJ4:HOLD(29)` key down, `lua:XL24-CJ4:RELEASE(29)` key up; the script sends `K:RUDDER_TRIM_LEFT` | none: step key (the gauge at 3,7 shows the result) | yes (trim, 160) | SDK-FCE, as [phase2-trim-views.md](phase2-trim-views.md); README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 3,7 | `RUD TRIM` | none (a Display Gauge, as the C172's) | `(A:RUDDER TRIM PCT, percent)` | - | SDK-CTLV, as [phase2-trim-views.md](phase2-trim-views.md) | Unverified |
| 3,8 | `RUD R` | `lua:XL24-CJ4:HOLD(30)` key down, `lua:XL24-CJ4:RELEASE(30)` key up; the script sends `K:RUDDER_TRIM_RIGHT` | none: step key (the gauge at 3,7 shows the result) | yes (trim, 160) | SDK-FCE, as [phase2-trim-views.md](phase2-trim-views.md); README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 4,1 |  | Empty | none: empty | - | - | - |
| 4,2 | `TRIM DN` | `lua:XL24-CJ4:HOLD(26)` key down, `lua:XL24-CJ4:RELEASE(26)` key up; the script sends `K:ELEV_TRIM_DN` | none: step key (the gauge at 3,4 shows the result) | yes (trim, 160) | SDK-FCE, as [phase2-trim-views.md](phase2-trim-views.md); README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 4,3 |  | Empty | none: empty | - | - | - |
| 4,4 |  | Empty | none: empty | - | - | - |
| 4,5 |  | Empty | none: empty | - | - | - |
| 4,6 |  | Empty | none: empty | - | - | - |
| 4,7 |  | Empty | none: empty | - | - | - |
| 4,8 |  | Empty | none: empty | - | - | - |

### VIEWS

Opened by main 1,8. The C172's views page as it is ([phase2-trim-views.md](phase2-trim-views.md)): camera SimVar
writes, no controller bindings.

| Pos | Title | Press (candidate) | Reads (candidate) | Hold to repeat | Source | Status |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | - | [navigation.md](navigation.md) | - |
| 1,2 | `COCKPIT` | write `(A:CAMERA STATE, Enum)` = 2 | `(A:CAMERA STATE, Enum)` | - | SDK-CAMV | Unverified |
| 1,3 | `EXTERNAL` | write `(A:CAMERA STATE, Enum)` = 3 | `(A:CAMERA STATE, Enum)` | - | SDK-CAMV | Unverified |
| 1,4 | `CAMERA` | none (readout) | `(A:CAMERA STATE, Enum)` | - | SDK-CAMV | Unverified |
| 1,5 | `VIEW` | none (readout) | `(A:CAMERA VIEW TYPE AND INDEX:0, Enum)` | - | SDK-CAMV | Unverified |
| 1,6 | `VIEW NO` | none (readout) | `(A:CAMERA VIEW TYPE AND INDEX:1, number)` | - | SDK-CAMV | Unverified |
| 1,7 |  | Empty | none: empty | - | - | - |
| 1,8 |  | Empty | none: empty | - | - | - |
| 2,1 |  | Empty | none: empty | - | - | - |
| 2,2 |  | Empty | none: empty | - | - | - |
| 2,3 |  | Empty | none: empty | - | - | - |
| 2,4 |  | Empty | none: empty | - | - | - |
| 2,5 |  | Empty | none: empty | - | - | - |
| 2,6 |  | Empty | none: empty | - | - | - |
| 2,7 |  | Empty | none: empty | - | - | - |
| 2,8 |  | Empty | none: empty | - | - | - |
| 3,1 |  | Empty | none: empty | - | - | - |
| 3,2 |  | Empty | none: empty | - | - | - |
| 3,3 |  | Empty | none: empty | - | - | - |
| 3,4 |  | Empty | none: empty | - | - | - |
| 3,5 |  | Empty | none: empty | - | - | - |
| 3,6 |  | Empty | none: empty | - | - | - |
| 3,7 |  | Empty | none: empty | - | - | - |
| 3,8 |  | Empty | none: empty | - | - | - |
| 4,1 |  | Empty | none: empty | - | - | - |
| 4,2 |  | Empty | none: empty | - | - | - |
| 4,3 |  | Empty | none: empty | - | - | - |
| 4,4 |  | Empty | none: empty | - | - | - |
| 4,5 |  | Empty | none: empty | - | - | - |
| 4,6 |  | Empty | none: empty | - | - | - |
| 4,7 |  | Empty | none: empty | - | - | - |
| 4,8 |  | Empty | none: empty | - | - | - |

### SIM RATE

Opened by main 3,7. The C172's sim rate page as it is ([phase2-sim-rate.md](phase2-sim-rate.md)), with its Lua
script. Its step keys do not repeat.

| Pos | Title | Press (candidate) | Reads (candidate) | Hold to repeat | Source | Status |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | - | [navigation.md](navigation.md) | - |
| 1,2 | `1X` | the sim rate script, back to 1x | `(A:SIMULATION RATE, number)` | - | [phase2-sim-rate.md](phase2-sim-rate.md) | Unverified |
| 1,3 | `SLOWER` | `K:SIM_RATE_DECR` | none: step key (the RATE readout shows the result) | - | [phase2-sim-rate.md](phase2-sim-rate.md) | Unverified |
| 1,4 | `RATE` | `K:SIM_RATE_INCR`, long press `K:SIM_RATE_DECR` | `(A:SIMULATION RATE, number)` | - | [phase2-sim-rate.md](phase2-sim-rate.md) | Unverified |
| 1,5 | `FASTER` | `K:SIM_RATE_INCR` | none: step key (the RATE readout shows the result) | - | [phase2-sim-rate.md](phase2-sim-rate.md) | Unverified |
| 1,6 |  | Empty | none: empty | - | - | - |
| 1,7 |  | Empty | none: empty | - | - | - |
| 1,8 |  | Empty | none: empty | - | - | - |
| 2,1 |  | Empty | none: empty | - | - | - |
| 2,2 |  | Empty | none: empty | - | - | - |
| 2,3 |  | Empty | none: empty | - | - | - |
| 2,4 |  | Empty | none: empty | - | - | - |
| 2,5 |  | Empty | none: empty | - | - | - |
| 2,6 |  | Empty | none: empty | - | - | - |
| 2,7 |  | Empty | none: empty | - | - | - |
| 2,8 |  | Empty | none: empty | - | - | - |
| 3,1 |  | Empty | none: empty | - | - | - |
| 3,2 |  | Empty | none: empty | - | - | - |
| 3,3 |  | Empty | none: empty | - | - | - |
| 3,4 |  | Empty | none: empty | - | - | - |
| 3,5 |  | Empty | none: empty | - | - | - |
| 3,6 |  | Empty | none: empty | - | - | - |
| 3,7 |  | Empty | none: empty | - | - | - |
| 3,8 |  | Empty | none: empty | - | - | - |
| 4,1 |  | Empty | none: empty | - | - | - |
| 4,2 |  | Empty | none: empty | - | - | - |
| 4,3 |  | Empty | none: empty | - | - | - |
| 4,4 |  | Empty | none: empty | - | - | - |
| 4,5 |  | Empty | none: empty | - | - | - |
| 4,6 |  | Empty | none: empty | - | - | - |
| 4,7 |  | Empty | none: empty | - | - | - |
| 4,8 |  | Empty | none: empty | - | - | - |

### CHECKLIST

Opened by main 3,8. One key, the CCP's CKLST key (index 1), likely the key that shows the electronic checklist on
the MFD (no source read says so); the CCP page holds the knobs and joystick. If the default CJ4 does not answer
it (S-4), the page keeps only its back key, as the C172's.

| Pos | Title | Press (candidate) | Reads (candidate) | Hold to repeat | Source | Status |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | - | [navigation.md](navigation.md) | - |
| 1,2 | `CKLST` | `H:Generic_Lwr_1_Push_CKLST` | none: no readable state (WT21 H-event) | - | WT21-H; WT21-CKL; CKL | Unverified |
| 1,3 |  | Empty | none: empty | - | - | - |
| 1,4 |  | Empty | none: empty | - | - | - |
| 1,5 |  | Empty | none: empty | - | - | - |
| 1,6 |  | Empty | none: empty | - | - | - |
| 1,7 |  | Empty | none: empty | - | - | - |
| 1,8 |  | Empty | none: empty | - | - | - |
| 2,1 |  | Empty | none: empty | - | - | - |
| 2,2 |  | Empty | none: empty | - | - | - |
| 2,3 |  | Empty | none: empty | - | - | - |
| 2,4 |  | Empty | none: empty | - | - | - |
| 2,5 |  | Empty | none: empty | - | - | - |
| 2,6 |  | Empty | none: empty | - | - | - |
| 2,7 |  | Empty | none: empty | - | - | - |
| 2,8 |  | Empty | none: empty | - | - | - |
| 3,1 |  | Empty | none: empty | - | - | - |
| 3,2 |  | Empty | none: empty | - | - | - |
| 3,3 |  | Empty | none: empty | - | - | - |
| 3,4 |  | Empty | none: empty | - | - | - |
| 3,5 |  | Empty | none: empty | - | - | - |
| 3,6 |  | Empty | none: empty | - | - | - |
| 3,7 |  | Empty | none: empty | - | - | - |
| 3,8 |  | Empty | none: empty | - | - | - |
| 4,1 |  | Empty | none: empty | - | - | - |
| 4,2 |  | Empty | none: empty | - | - | - |
| 4,3 |  | Empty | none: empty | - | - | - |
| 4,4 |  | Empty | none: empty | - | - | - |
| 4,5 |  | Empty | none: empty | - | - | - |
| 4,6 |  | Empty | none: empty | - | - | - |
| 4,7 |  | Empty | none: empty | - | - | - |
| 4,8 |  | Empty | none: empty | - | - | - |

### MORE

Opened by main 4,8. Row 1 as the SF50's, with DCP and CCP at 1,2 and 1,3 (the C172's PFD and MFD bezel positions);
row 2 adds LIGHTS and the three FMS pages. All pages below MORE are second level.

| Pos | Title | Press (candidate) | Reads (candidate) | Hold to repeat | Source | Status |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | - | [navigation.md](navigation.md) | - |
| 1,2 | `DCP` | Folder: opens **dcp** | none: folder key | - | [navigation.md](navigation.md) | - |
| 1,3 | `CCP` | Folder: opens **ccp** | none: folder key | - | [navigation.md](navigation.md) | - |
| 1,4 | `V-SPEEDS` | Folder: opens **vspeeds** | none: folder key | - | [navigation.md](navigation.md) | - |
| 1,5 | `COM PAD` | Folder: opens **compad** | none: folder key | - | [navigation.md](navigation.md) | - |
| 1,6 | `AUTOPILOT` | Folder: opens **autopilot** | none: folder key | - | [navigation.md](navigation.md) | - |
| 1,7 | `XPDR` | Folder: opens **xpdr** | none: folder key | - | [navigation.md](navigation.md) | - |
| 1,8 | `RADIOS` | Folder: opens **radios** | none: folder key | - | [navigation.md](navigation.md) | - |
| 2,1 |  | Empty | none: empty | - | - | - |
| 2,2 | `SYSTEMS` | Folder: opens **systems** | none: folder key | - | [navigation.md](navigation.md) | - |
| 2,3 | `ENGINE` | Folder: opens **engine** | none: folder key | - | [navigation.md](navigation.md) | - |
| 2,4 | `ICE/ENV` | Folder: opens **iceenv** | none: folder key | - | [navigation.md](navigation.md) | - |
| 2,5 | `LIGHTS` | Folder: opens **lights** | none: folder key | - | [navigation.md](navigation.md) | - |
| 2,6 | `FMS` | Folder: opens **fms** | none: folder key | - | [navigation.md](navigation.md) | - |
| 2,7 | `FMS ABC` | Folder: opens **fmsabc** | none: folder key | - | [navigation.md](navigation.md) | - |
| 2,8 | `FMS 123` | Folder: opens **fms123** | none: folder key | - | [navigation.md](navigation.md) | - |
| 3,1 |  | Empty | none: empty | - | - | - |
| 3,2 |  | Empty | none: empty | - | - | - |
| 3,3 |  | Empty | none: empty | - | - | - |
| 3,4 |  | Empty | none: empty | - | - | - |
| 3,5 |  | Empty | none: empty | - | - | - |
| 3,6 |  | Empty | none: empty | - | - | - |
| 3,7 |  | Empty | none: empty | - | - | - |
| 3,8 |  | Empty | none: empty | - | - | - |
| 4,1 |  | Empty | none: empty | - | - | - |
| 4,2 |  | Empty | none: empty | - | - | - |
| 4,3 |  | Empty | none: empty | - | - | - |
| 4,4 |  | Empty | none: empty | - | - | - |
| 4,5 |  | Empty | none: empty | - | - | - |
| 4,6 |  | Empty | none: empty | - | - | - |
| 4,7 |  | Empty | none: empty | - | - | - |
| 4,8 |  | Empty | none: empty | - | - | - |

### V-SPEEDS

Opened by more 1,4. The C172's V-speeds page as it is ([phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md)).

| Pos | Title | Press (candidate) | Reads (candidate) | Hold to repeat | Source | Status |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | - | [navigation.md](navigation.md) | - |
| 1,2 | `VS0` | none (readout) | `(A:DESIGN SPEED VS0, knots)` | - | [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md) | Unverified |
| 1,3 | `VS1` | none (readout) | `(A:DESIGN SPEED VS1, knots)` | - | [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md) | Unverified |
| 1,4 | `VR` | none (readout) | `(A:DESIGN SPEED MIN ROTATION, knots)` | - | [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md) | Unverified |
| 1,5 |  | Empty | none: empty | - | - | - |
| 1,6 | `CLIMB` | none (readout) | `(A:DESIGN SPEED CLIMB, knots)` | - | [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md) | Unverified |
| 1,7 |  | Empty | none: empty | - | - | - |
| 1,8 |  | Empty | none: empty | - | - | - |
| 2,1 |  | Empty | none: empty | - | - | - |
| 2,2 | `CRUISE` | none (readout) | `(A:DESIGN SPEED VC, knots)` | - | [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md) | Unverified |
| 2,3 |  | Empty | none: empty | - | - | - |
| 2,4 | `VNE` | none (readout) | `(A:REFERENCE SPEED MAX IAS, knots)` | - | [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md) | Unverified |
| 2,5 | `VFE` | none (readout) | `(A:FLAPS CURRENT SPEED LIMITATION, knots)` | - | [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md) | Unverified |
| 2,6 |  | Empty | none: empty | - | - | - |
| 2,7 |  | Empty | none: empty | - | - | - |
| 2,8 |  | Empty | none: empty | - | - | - |
| 3,1 |  | Empty | none: empty | - | - | - |
| 3,2 |  | Empty | none: empty | - | - | - |
| 3,3 |  | Empty | none: empty | - | - | - |
| 3,4 |  | Empty | none: empty | - | - | - |
| 3,5 |  | Empty | none: empty | - | - | - |
| 3,6 |  | Empty | none: empty | - | - | - |
| 3,7 |  | Empty | none: empty | - | - | - |
| 3,8 |  | Empty | none: empty | - | - | - |
| 4,1 |  | Empty | none: empty | - | - | - |
| 4,2 |  | Empty | none: empty | - | - | - |
| 4,3 |  | Empty | none: empty | - | - | - |
| 4,4 |  | Empty | none: empty | - | - | - |
| 4,5 |  | Empty | none: empty | - | - | - |
| 4,6 |  | Empty | none: empty | - | - | - |
| 4,7 |  | Empty | none: empty | - | - | - |
| 4,8 |  | Empty | none: empty | - | - | - |

### COM PAD

Opened by more 1,5. The C172's COM1 pad as it is ([phase2-com1-pad.md](phase2-com1-pad.md)). The pad keys do not
repeat.

| Pos | Title | Press (candidate) | Reads (candidate) | Hold to repeat | Source | Status |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | - | [navigation.md](navigation.md) | - |
| 1,2 | `COM1` | `K:COM_STBY_RADIO_SWAP` | `(A:COM ACTIVE FREQUENCY:1, MHz)`, `(A:COM STANDBY FREQUENCY:1, MHz)` | - | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 1,3 | `ENTRY` | none (readout of the pad script's entry) | the pad script's entry value | - | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 1,4 |  | Empty | none: empty | - | - | - |
| 1,5 |  | Empty | none: empty | - | - | - |
| 1,6 | `7` | the pad script: digit 7 | none: pad key (ENTRY shows the result) | - | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 1,7 | `8` | the pad script: digit 8 | none: pad key (ENTRY shows the result) | - | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 1,8 | `9` | the pad script: digit 9 | none: pad key (ENTRY shows the result) | - | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 2,1 |  | Empty | none: empty | - | - | - |
| 2,2 | `STBY ID` | none (readout) | `(A:COM STANDBY FREQ IDENT:1, String)` | - | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 2,3 |  | Empty | none: empty | - | - | - |
| 2,4 |  | Empty | none: empty | - | - | - |
| 2,5 |  | Empty | none: empty | - | - | - |
| 2,6 | `4` | the pad script: digit 4 | none: pad key (ENTRY shows the result) | - | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 2,7 | `5` | the pad script: digit 5 | none: pad key (ENTRY shows the result) | - | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 2,8 | `6` | the pad script: digit 6 | none: pad key (ENTRY shows the result) | - | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 3,1 |  | Empty | none: empty | - | - | - |
| 3,2 |  | Empty | none: empty | - | - | - |
| 3,3 |  | Empty | none: empty | - | - | - |
| 3,4 |  | Empty | none: empty | - | - | - |
| 3,5 |  | Empty | none: empty | - | - | - |
| 3,6 | `1` | the pad script: digit 1 | none: pad key (ENTRY shows the result) | - | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 3,7 | `2` | the pad script: digit 2 | none: pad key (ENTRY shows the result) | - | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 3,8 | `3` | the pad script: digit 3 | none: pad key (ENTRY shows the result) | - | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 4,1 |  | Empty | none: empty | - | - | - |
| 4,2 |  | Empty | none: empty | - | - | - |
| 4,3 |  | Empty | none: empty | - | - | - |
| 4,4 |  | Empty | none: empty | - | - | - |
| 4,5 |  | Empty | none: empty | - | - | - |
| 4,6 | `CLR` | the pad script: back, long press clear | none: pad key (ENTRY shows the result) | - | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 4,7 | `0` | the pad script: digit 0 | none: pad key (ENTRY shows the result) | - | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |
| 4,8 | `ENT` | the pad script: enter, long press enter and swap | none: pad key (COM1 shows the result) | - | [phase2-com1-pad.md](phase2-com1-pad.md) | Unverified |

### AUTOPILOT

Opened by more 1,6. The SF50 autopilot grid ([visionjet-sf50.md](visionjet-sf50.md)): mode keys in rows 1 and the
first column, step keys in rows 2 and 4, readouts between them in row 3. No A/T, TOGA, FMS SPD or MAN SPD key (no
source gives them for the CJ4); BC, VNAV, BANK and IAS/MACH take their places. If the CJ4's mode buttons are input
events (S-1, S-4), the build swaps the presses and reads.

| Pos | Title | Press (candidate) | Reads (candidate) | Hold to repeat | Source | Status |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | - | [navigation.md](navigation.md) | - |
| 1,2 | `AP` | `K:AP_MASTER` | `(A:AUTOPILOT MASTER, Bool)` | - | SDK-APE; SDK-APV | Unverified |
| 1,3 | `FD` | `K:TOGGLE_FLIGHT_DIRECTOR` | `(A:AUTOPILOT FLIGHT DIRECTOR ACTIVE, Bool)` | - | SDK-APE; SDK-APV | Unverified |
| 1,4 | `HDG` | `K:AP_HDG_HOLD` | `(A:AUTOPILOT HEADING LOCK, Bool)` | - | SDK-APE; SDK-APV | Unverified |
| 1,5 | `NAV` | `K:AP_NAV1_HOLD` | `(A:AUTOPILOT NAV1 LOCK, Bool)` | - | SDK-APE; SDK-APV | Unverified |
| 1,6 | `APR` | `K:AP_APR_HOLD` | `(A:AUTOPILOT APPROACH HOLD, Bool)` | - | SDK-APE; SDK-APV | Unverified |
| 1,7 | `BC` | `K:AP_BC_HOLD` | `(A:AUTOPILOT BACKCOURSE HOLD, Bool)` | - | SDK-APE; SDK-APV, as [phase3-autopilot.md](phase3-autopilot.md) | Unverified |
| 1,8 | `VNAV` | B-var from the input event list (S-1) (no 2024 VNAV event found) | the same B-var (S-1) | - | README 2.1.1 | Unverified |
| 2,1 | `ALT` | `K:AP_ALT_HOLD` | `(A:AUTOPILOT ALTITUDE LOCK, Bool)` | - | SDK-APE; SDK-APV | Unverified |
| 2,2 | `HDG+` | `lua:XL24-CJ4:HOLD(1)` key down, `lua:XL24-CJ4:RELEASE(1)` key up; the script sends `K:HEADING_BUG_INC` | none: step key (HDG BUG at 3,2 shows the result) | yes (fast, 360) | SDK-APE; README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 2,3 | `CRS+` | `lua:XL24-CJ4:HOLD(3)` key down, `lua:XL24-CJ4:RELEASE(3)` key up; the script sends `K:VOR1_OBI_INC` | none: step key (CRS1 at 3,3 shows the result) | yes (fast, 360) | SDK-RADE, as [phase3-autopilot.md](phase3-autopilot.md); README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 2,4 | `ALT+` | `lua:XL24-CJ4:HOLD(5)` key down, `lua:XL24-CJ4:RELEASE(5)` key up; the script sends `K:AP_ALT_VAR_INC` | none: step key (ALT SEL at 3,4 shows the result) | yes (alt, 400) | SDK-APE; README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 2,5 | `VS+` | `lua:XL24-CJ4:HOLD(7)` key down, `lua:XL24-CJ4:RELEASE(7)` key up; the script sends `K:AP_VS_VAR_INC` | none: step key (VS TGT at 3,5 shows the result) | yes (slow, 40) | SDK-APE; README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 2,6 | `SPD+` | `lua:XL24-CJ4:HOLD(9)` key down, `lua:XL24-CJ4:RELEASE(9)` key up; the script sends `K:AP_SPD_VAR_INC` | none: step key (SPD TGT at 3,6 shows the result) | yes (fast, 200) | SDK-APE; README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 2,7 | `YD` | `K:YAW_DAMPER_TOGGLE` | `(A:AUTOPILOT YAW DAMPER, Bool)` | - | SDK-APE; SDK-APV; CKL 285 | Unverified |
| 2,8 | `BANK` | `K:AP_MAX_BANK_INC`, long press `K:AP_MAX_BANK_DEC` | `(A:AUTOPILOT MAX BANK ID, number)` | - | SDK-APE; SDK-APV | Unverified |
| 3,1 | `VS` | `K:AP_VS_HOLD` | `(A:AUTOPILOT VERTICAL HOLD, Bool)` | - | SDK-APE; SDK-APV | Unverified |
| 3,2 | `HDG BUG` | none (readout) | `(A:AUTOPILOT HEADING LOCK DIR, Degrees)` | - | SDK-APV | Unverified |
| 3,3 | `CRS1` | none (readout) | `(A:NAV OBS:1, Degrees)` | - | SDK-RADV, as [phase3-autopilot.md](phase3-autopilot.md) | Unverified |
| 3,4 | `ALT SEL` | none (readout) | `(A:AUTOPILOT ALTITUDE LOCK VAR, Feet)` | - | SDK-APV | Unverified |
| 3,5 | `VS TGT` | none (readout) | `(A:AUTOPILOT VERTICAL HOLD VAR, Feet/minute)` | - | SDK-APV | Unverified |
| 3,6 | `SPD TGT` | none (readout) | `(A:AUTOPILOT AIRSPEED HOLD VAR, Knots)` | - | SDK-APV | Unverified |
| 3,7 | `MACH TGT` | none (readout) | `(A:AUTOPILOT MACH HOLD VAR, number)` | - | SDK-APV | Unverified |
| 3,8 | `IAS/MACH` | `K:AP_MANAGED_SPEED_IN_MACH_TOGGLE` | `(A:AUTOPILOT MANAGED SPEED IN MACH, Bool)` | - | SDK-APE; SDK-APV | Unverified |
| 4,1 | `FLC` | `K:FLIGHT_LEVEL_CHANGE` | `(A:AUTOPILOT FLIGHT LEVEL CHANGE, Bool)` | - | SDK-APE; SDK-APV | Unverified |
| 4,2 | `HDG-` | `lua:XL24-CJ4:HOLD(2)` key down, `lua:XL24-CJ4:RELEASE(2)` key up; the script sends `K:HEADING_BUG_DEC` | none: step key (HDG BUG at 3,2 shows the result) | yes (fast, 360) | SDK-APE; README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 4,3 | `CRS-` | `lua:XL24-CJ4:HOLD(4)` key down, `lua:XL24-CJ4:RELEASE(4)` key up; the script sends `K:VOR1_OBI_DEC` | none: step key (CRS1 at 3,3 shows the result) | yes (fast, 360) | SDK-RADE, as [phase3-autopilot.md](phase3-autopilot.md); README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 4,4 | `ALT-` | `lua:XL24-CJ4:HOLD(6)` key down, `lua:XL24-CJ4:RELEASE(6)` key up; the script sends `K:AP_ALT_VAR_DEC` | none: step key (ALT SEL at 3,4 shows the result) | yes (alt, 400) | SDK-APE; README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 4,5 | `VS-` | `lua:XL24-CJ4:HOLD(8)` key down, `lua:XL24-CJ4:RELEASE(8)` key up; the script sends `K:AP_VS_VAR_DEC` | none: step key (VS TGT at 3,5 shows the result) | yes (slow, 40) | SDK-APE; README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 4,6 | `SPD-` | `lua:XL24-CJ4:HOLD(10)` key down, `lua:XL24-CJ4:RELEASE(10)` key up; the script sends `K:AP_SPD_VAR_DEC` | none: step key (SPD TGT at 3,6 shows the result) | yes (fast, 200) | SDK-APE; README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 4,7 |  | Empty | none: empty | - | - | - |
| 4,8 |  | Empty | none: empty | - | - | - |

### XPDR

Opened by more 1,7. The C172's transponder page as it is ([phase3-transponder.md](phase3-transponder.md)). The pad
keys do not repeat.

| Pos | Title | Press (candidate) | Reads (candidate) | Hold to repeat | Source | Status |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | - | [navigation.md](navigation.md) | - |
| 1,2 | `XPDR` | none (readout) | `(A:TRANSPONDER CODE:1, Bco16)` | - | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 1,3 | `ENTRY` | none (readout of the pad script's entry) | the pad script's entry value | - | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 1,4 | `MODE` | none (readout) | `(A:TRANSPONDER STATE:1, Enum)` | - | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 1,5 |  | Empty | none: empty | - | - | - |
| 1,6 | `7` | the pad script: digit 7 | none: pad key (ENTRY shows the result) | - | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 1,7 |  | Empty | none: empty | - | - | - |
| 1,8 |  | Empty | none: empty | - | - | - |
| 2,1 |  | Empty | none: empty | - | - | - |
| 2,2 | `STBY` | write `(A:TRANSPONDER STATE:1, Enum)` = 1 | `(A:TRANSPONDER STATE:1, Enum)` | - | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 2,3 | `ON` | write `(A:TRANSPONDER STATE:1, Enum)` = 3 | `(A:TRANSPONDER STATE:1, Enum)` | - | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 2,4 | `ALT` | write `(A:TRANSPONDER STATE:1, Enum)` = 4 | `(A:TRANSPONDER STATE:1, Enum)` | - | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 2,5 |  | Empty | none: empty | - | - | - |
| 2,6 | `4` | the pad script: digit 4 | none: pad key (ENTRY shows the result) | - | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 2,7 | `5` | the pad script: digit 5 | none: pad key (ENTRY shows the result) | - | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 2,8 | `6` | the pad script: digit 6 | none: pad key (ENTRY shows the result) | - | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 3,1 |  | Empty | none: empty | - | - | - |
| 3,2 | `IDENT` | `K:XPNDR_IDENT_ON` | `(A:TRANSPONDER IDENT:1, Bool)` | - | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 3,3 | `VFR` | `K:XPNDR_SET:4608` | none: sets a code (XPDR shows the result) | - | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 3,4 |  | Empty | none: empty | - | - | - |
| 3,5 |  | Empty | none: empty | - | - | - |
| 3,6 | `1` | the pad script: digit 1 | none: pad key (ENTRY shows the result) | - | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 3,7 | `2` | the pad script: digit 2 | none: pad key (ENTRY shows the result) | - | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 3,8 | `3` | the pad script: digit 3 | none: pad key (ENTRY shows the result) | - | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 4,1 |  | Empty | none: empty | - | - | - |
| 4,2 |  | Empty | none: empty | - | - | - |
| 4,3 |  | Empty | none: empty | - | - | - |
| 4,4 |  | Empty | none: empty | - | - | - |
| 4,5 |  | Empty | none: empty | - | - | - |
| 4,6 | `CLR` | the pad script: back, long press clear | none: pad key (ENTRY shows the result) | - | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 4,7 | `0` | the pad script: digit 0 | none: pad key (ENTRY shows the result) | - | [phase3-transponder.md](phase3-transponder.md) | Unverified |
| 4,8 | `ENT` | the pad script: enter | none: pad key (XPDR shows the result) | - | [phase3-transponder.md](phase3-transponder.md) | Unverified |

### RADIOS

Opened by more 1,8. The SF50's radios page ([visionjet-sf50.md](visionjet-sf50.md)): the C172's radios page with
its BARO column; every step key holds to repeat.

| Pos | Title | Press (candidate) | Reads (candidate) | Hold to repeat | Source | Status |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | - | [navigation.md](navigation.md) | - |
| 1,2 | `NAV1` | `K:NAV1_RADIO_SWAP` | `(A:NAV ACTIVE FREQUENCY:1, MHz)`, `(A:NAV STANDBY FREQUENCY:1, MHz)` | - | SDK-RADE, as [phase3-radios.md](phase3-radios.md); SDK-RADV, as [phase3-radios.md](phase3-radios.md) | Unverified |
| 1,3 | `NAV1 ID` | none (readout) | `(A:NAV IDENT:1, String)` | - | SDK-RADV, as [phase3-radios.md](phase3-radios.md) | Unverified |
| 1,4 | `NAV2` | `K:NAV2_RADIO_SWAP` | `(A:NAV ACTIVE FREQUENCY:2, MHz)`, `(A:NAV STANDBY FREQUENCY:2, MHz)` | - | SDK-RADE, as [phase3-radios.md](phase3-radios.md); SDK-RADV, as [phase3-radios.md](phase3-radios.md) | Unverified |
| 1,5 | `NAV2 ID` | none (readout) | `(A:NAV IDENT:2, String)` | - | SDK-RADV, as [phase3-radios.md](phase3-radios.md) | Unverified |
| 1,6 | `COM2` | `K:COM2_RADIO_SWAP` | `(A:COM ACTIVE FREQUENCY:2, MHz)`, `(A:COM STANDBY FREQUENCY:2, MHz)` | - | SDK-RADE, as [phase3-radios.md](phase3-radios.md); SDK-RADV, as [phase3-radios.md](phase3-radios.md) | Unverified |
| 1,7 | `COM2 ID` | none (readout) | `(A:COM ACTIVE FREQ IDENT:2, String)` | - | SDK-RADV, as [phase3-radios.md](phase3-radios.md) | Unverified |
| 1,8 | `BARO` | none (readout) | `(A:KOHLSMAN SETTING HG:1, inHg)` | - | SDK-SYSV, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 2,1 |  | Empty | none: empty | - | - | - |
| 2,2 | `MHZ+` | `lua:XL24-CJ4:HOLD(13)` key down, `lua:XL24-CJ4:RELEASE(13)` key up; the script sends `K:NAV1_RADIO_WHOLE_INC` | none: step key (1,2 shows the result) | yes (slow, 30) | SDK-RADE, as [phase3-radios.md](phase3-radios.md); README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 2,3 | `KHZ+` | `lua:XL24-CJ4:HOLD(14)` key down, `lua:XL24-CJ4:RELEASE(14)` key up; the script sends `K:NAV1_RADIO_FRACT_INC` | none: step key (1,2 shows the result) | yes (fast, 200) | SDK-RADE, as [phase3-radios.md](phase3-radios.md); README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 2,4 | `MHZ+` | `lua:XL24-CJ4:HOLD(15)` key down, `lua:XL24-CJ4:RELEASE(15)` key up; the script sends `K:NAV2_RADIO_WHOLE_INC` | none: step key (1,4 shows the result) | yes (slow, 30) | SDK-RADE, as [phase3-radios.md](phase3-radios.md); README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 2,5 | `KHZ+` | `lua:XL24-CJ4:HOLD(16)` key down, `lua:XL24-CJ4:RELEASE(16)` key up; the script sends `K:NAV2_RADIO_FRACT_INC` | none: step key (1,4 shows the result) | yes (fast, 200) | SDK-RADE, as [phase3-radios.md](phase3-radios.md); README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 2,6 | `MHZ+` | `lua:XL24-CJ4:HOLD(17)` key down, `lua:XL24-CJ4:RELEASE(17)` key up; the script sends `K:COM2_RADIO_WHOLE_INC` | none: step key (1,6 shows the result) | yes (slow, 30) | SDK-RADE, as [phase3-radios.md](phase3-radios.md); README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 2,7 | `KHZ+` | `lua:XL24-CJ4:HOLD(18)` key down, `lua:XL24-CJ4:RELEASE(18)` key up; the script sends `K:COM2_RADIO_FRACT_INC` | none: step key (1,6 shows the result) | yes (fast, 200) | SDK-RADE, as [phase3-radios.md](phase3-radios.md); README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 2,8 | `BARO+` | `lua:XL24-CJ4:HOLD(11)` key down, `lua:XL24-CJ4:RELEASE(11)` key up; the script sends `K:KOHLSMAN_INC` | none: step key (1,8 shows the result) | yes (baro, 200) | SDK-INSTE (WT21-H `AP_BARO_Up` as fallback); README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 3,1 |  | Empty | none: empty | - | - | - |
| 3,2 | `MHZ-` | `lua:XL24-CJ4:HOLD(19)` key down, `lua:XL24-CJ4:RELEASE(19)` key up; the script sends `K:NAV1_RADIO_WHOLE_DEC` | none: step key (1,2 shows the result) | yes (slow, 30) | SDK-RADE, as [phase3-radios.md](phase3-radios.md); README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 3,3 | `KHZ-` | `lua:XL24-CJ4:HOLD(20)` key down, `lua:XL24-CJ4:RELEASE(20)` key up; the script sends `K:NAV1_RADIO_FRACT_DEC` | none: step key (1,2 shows the result) | yes (fast, 200) | SDK-RADE, as [phase3-radios.md](phase3-radios.md); README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 3,4 | `MHZ-` | `lua:XL24-CJ4:HOLD(21)` key down, `lua:XL24-CJ4:RELEASE(21)` key up; the script sends `K:NAV2_RADIO_WHOLE_DEC` | none: step key (1,4 shows the result) | yes (slow, 30) | SDK-RADE, as [phase3-radios.md](phase3-radios.md); README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 3,5 | `KHZ-` | `lua:XL24-CJ4:HOLD(22)` key down, `lua:XL24-CJ4:RELEASE(22)` key up; the script sends `K:NAV2_RADIO_FRACT_DEC` | none: step key (1,4 shows the result) | yes (fast, 200) | SDK-RADE, as [phase3-radios.md](phase3-radios.md); README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 3,6 | `MHZ-` | `lua:XL24-CJ4:HOLD(23)` key down, `lua:XL24-CJ4:RELEASE(23)` key up; the script sends `K:COM2_RADIO_WHOLE_DEC` | none: step key (1,6 shows the result) | yes (slow, 30) | SDK-RADE, as [phase3-radios.md](phase3-radios.md); README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 3,7 | `KHZ-` | `lua:XL24-CJ4:HOLD(24)` key down, `lua:XL24-CJ4:RELEASE(24)` key up; the script sends `K:COM2_RADIO_FRACT_DEC` | none: step key (1,6 shows the result) | yes (fast, 200) | SDK-RADE, as [phase3-radios.md](phase3-radios.md); README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 3,8 | `BARO-` | `lua:XL24-CJ4:HOLD(12)` key down, `lua:XL24-CJ4:RELEASE(12)` key up; the script sends `K:KOHLSMAN_DEC` | none: step key (1,8 shows the result) | yes (baro, 200) | SDK-INSTE (WT21-H `AP_BARO_Down` as fallback); README 2.1.1, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 4,1 |  | Empty | none: empty | - | - | - |
| 4,2 |  | Empty | none: empty | - | - | - |
| 4,3 |  | Empty | none: empty | - | - | - |
| 4,4 |  | Empty | none: empty | - | - | - |
| 4,5 |  | Empty | none: empty | - | - | - |
| 4,6 | `MIC1` | `K:PILOT_TRANSMITTER_SET:0` | `(A:COM TRANSMIT:1, Bool)` | - | SDK-RADE, as [phase3-radios.md](phase3-radios.md); SDK-RADV, as [phase3-radios.md](phase3-radios.md) | Unverified |
| 4,7 | `MIC2` | `K:PILOT_TRANSMITTER_SET:1` | `(A:COM TRANSMIT:2, Bool)` | - | SDK-RADE, as [phase3-radios.md](phase3-radios.md); SDK-RADV, as [phase3-radios.md](phase3-radios.md) | Unverified |
| 4,8 |  | Empty | none: empty | - | - | - |

### DCP

Opened by more 1,2. New. The 15 DCP events of WT21-H (index 1, the PFD), plain presses (RANGE and TILT do not
repeat), a baro readout, and in columns 7 and 8 the eight display unit line select keys (index 1, the MFD; on this
page because the CCP page has no room left).

| Pos | Title | Press (candidate) | Reads (candidate) | Hold to repeat | Source | Status |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | - | [navigation.md](navigation.md) | - |
| 1,2 | `PFD MENU` | `H:Generic_Upr_1_Push_PFD_MENU` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 1,3 | `REFS MENU` | `H:Generic_Upr_1_Push_REFS_MENU` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 1,4 | `ESC` | `H:Generic_Upr_1_Push_ESC` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 1,5 | `TFC` | `H:Generic_Upr_1_Push_TFC` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 1,6 | `TERR/WX` | `H:Generic_Upr_1_Push_TERR_WX` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 1,7 | `DU 1L` | `H:Generic_Lwr_1_Push_1L` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 1,8 | `DU 1R` | `H:Generic_Lwr_1_Push_1R` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 2,1 |  | Empty | none: empty | - | - | - |
| 2,2 | `MENU ADV+` | `H:Generic_Upr_1_Push_MENU_ADV_INC` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 2,3 | `DATA+` | `H:Generic_Upr_1_Push_DATA_INC` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 2,4 | `RANGE+` | `H:Generic_Upr_1_Push_RANGE_INC` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 2,5 | `TILT+` | `H:Generic_Upr_1_Push_TILT_INC` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 2,6 | `BARO` | none (readout) | `(A:KOHLSMAN SETTING HG:1, inHg)` | - | SDK-SYSV, as [phase2-main-page.md](phase2-main-page.md) | Unverified |
| 2,7 | `DU 2L` | `H:Generic_Lwr_1_Push_2L` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 2,8 | `DU 2R` | `H:Generic_Lwr_1_Push_2R` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 3,1 |  | Empty | none: empty | - | - | - |
| 3,2 |  | Empty | none: empty | - | - | - |
| 3,3 | `DATA PUSH` | `H:Generic_Upr_1_Push_DATA_PUSH` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 3,4 |  | Empty | none: empty | - | - | - |
| 3,5 | `TILT PUSH` | `H:Generic_Upr_1_Push_TILT_PUSH` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 3,6 |  | Empty | none: empty | - | - | - |
| 3,7 | `DU 3L` | `H:Generic_Lwr_1_Push_3L` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 3,8 | `DU 3R` | `H:Generic_Lwr_1_Push_3R` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 4,1 |  | Empty | none: empty | - | - | - |
| 4,2 | `MENU ADV-` | `H:Generic_Upr_1_Push_MENU_ADV_DEC` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 4,3 | `DATA-` | `H:Generic_Upr_1_Push_DATA_DEC` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 4,4 | `RANGE-` | `H:Generic_Upr_1_Push_RANGE_DEC` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 4,5 | `TILT-` | `H:Generic_Upr_1_Push_TILT_DEC` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 4,6 |  | Empty | none: empty | - | - | - |
| 4,7 | `DU 4L` | `H:Generic_Lwr_1_Push_4L` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 4,8 | `DU 4R` | `H:Generic_Lwr_1_Push_4R` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |

### CCP

Opened by more 1,3. New. The 23 CCP events of WT21-H (index 1, the MFD): MEM 1-3 push on a press and hold on a long
press; the joystick as a cross around 3,6; nothing repeats.

| Pos | Title | Press (candidate) | Reads (candidate) | Hold to repeat | Source | Status |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | - | [navigation.md](navigation.md) | - |
| 1,2 | `UPR MENU` | `H:Generic_Lwr_1_Push_UPR_MENU` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 1,3 | `LWR MENU` | `H:Generic_Lwr_1_Push_LWR_MENU` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 1,4 | `ESC` | `H:Generic_Lwr_1_Push_ESC` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 1,5 | `NAV DATA` | `H:Generic_Lwr_1_Push_NAV_DATA` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 1,6 | `CAS` | `H:Generic_Lwr_1_Push_CAS_PAGE` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 1,7 | `ENG` | `H:Generic_Lwr_1_Push_ENG` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 1,8 | `SYS` | `H:Generic_Lwr_1_Push_SYS` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 2,1 | `TFC` | `H:Generic_Lwr_1_Push_TFC` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 2,2 | `MENU ADV+` | `H:Generic_Lwr_1_Push_MENU_ADV_INC` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 2,3 | `DATA+` | `H:Generic_Lwr_1_Push_DATA_INC` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 2,4 | `ZOOM+` | `H:Generic_Lwr_1_Push_ZOOM_INC` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 2,5 |  | Empty | none: empty | - | - | - |
| 2,6 | `JOY UP` | `H:Generic_Lwr_1_JOYSTICK_UP` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 2,7 |  | Empty | none: empty | - | - | - |
| 2,8 | `MEM1` | `H:Generic_Lwr_1_Push_MEM1`, long press `H:Generic_Lwr_1_Hold_MEM1` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 3,1 | `TERR/WX` | `H:Generic_Lwr_1_Push_TERR_WX` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 3,2 | `CKLST` | `H:Generic_Lwr_1_Push_CKLST` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 3,3 | `DATA PUSH` | `H:Generic_Lwr_1_Push_DATA_PUSH` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 3,4 |  | Empty | none: empty | - | - | - |
| 3,5 | `JOY LEFT` | `H:Generic_Lwr_1_JOYSTICK_LEFT` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 3,6 |  | Empty | none: empty | - | - | - |
| 3,7 | `JOY RIGHT` | `H:Generic_Lwr_1_JOYSTICK_RIGHT` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 3,8 | `MEM2` | `H:Generic_Lwr_1_Push_MEM2`, long press `H:Generic_Lwr_1_Hold_MEM2` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 4,1 |  | Empty | none: empty | - | - | - |
| 4,2 | `MENU ADV-` | `H:Generic_Lwr_1_Push_MENU_ADV_DEC` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 4,3 | `DATA-` | `H:Generic_Lwr_1_Push_DATA_DEC` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 4,4 | `ZOOM-` | `H:Generic_Lwr_1_Push_ZOOM_DEC` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 4,5 |  | Empty | none: empty | - | - | - |
| 4,6 | `JOY DOWN` | `H:Generic_Lwr_1_JOYSTICK_DOWN` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |
| 4,7 |  | Empty | none: empty | - | - | - |
| 4,8 | `MEM3` | `H:Generic_Lwr_1_Push_MEM3`, long press `H:Generic_Lwr_1_Hold_MEM3` | none: no readable state (WT21 H-event) | - | WT21-H | Unverified |

### SYSTEMS

Opened by more 2,2. Electrical switches in row 1 (B-vars first, K-events as fallbacks), electrical and hydraulic
readouts in row 2, fuel transfer and pump readouts in row 3 (no write: no 2024 event was found for the transfer
selector).

| Pos | Title | Press (candidate) | Reads (candidate) | Hold to repeat | Source | Status |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | - | [navigation.md](navigation.md) | - |
| 1,2 | `BAT` | B-var from the input event list (S-1); else `K:TOGGLE_MASTER_BATTERY:1` | `(A:ELECTRICAL MASTER BATTERY:1, Bool)` | - | SDK-ELECE; SDK-ELECV; README 2.1.1; CKL 7 | Unverified |
| 1,3 | `GEN L` | B-var from the input event list (S-1); else `K:TOGGLE_ALTERNATOR1` | `(A:GENERAL ENG MASTER ALTERNATOR:1, Bool)` | - | SDK-ELECE; SDK-ENGV; README 2.1.1 | Unverified |
| 1,4 | `GEN R` | B-var from the input event list (S-1); else `K:TOGGLE_ALTERNATOR2` | `(A:GENERAL ENG MASTER ALTERNATOR:2, Bool)` | - | SDK-ELECE; SDK-ENGV; README 2.1.1 | Unverified |
| 1,5 | `AVIONICS` | B-var from the input event list (S-1) (no SDK event found) | `(A:AVIONICS MASTER SWITCH:1, Bool)` | - | SDK-SYSV, as [phase3-systems.md](phase3-systems.md); README 2.1.1; CKL 19 | Unverified |
| 1,6 | `STBY` | B-var from the input event list (S-1) | the same B-var (S-1) | - | README 2.1.1; CKL 15 | Unverified |
| 1,7 | `EMER LT` | B-var from the input event list (S-1) | the same B-var (S-1) | - | README 2.1.1; CKL 11 | Unverified |
| 1,8 | `EXT PWR` | none (readout) | `(A:EXTERNAL POWER ON:1, Bool)` | - | SDK-ELECV, as [visionjet-g2-research.md](visionjet-g2-research.md); CKL 86 | Unverified |
| 2,1 |  | Empty | none: empty | - | - | - |
| 2,2 | `BUS V` | none (readout) | `(A:ELECTRICAL MAIN BUS VOLTAGE:1, Volts)` | - | SDK-ELECV, as [phase3-systems.md](phase3-systems.md) | Unverified |
| 2,3 | `BATT A` | none (readout) | `(A:ELECTRICAL BATTERY LOAD:1, Amperes)` | - | SDK-ELECV, as [phase3-systems.md](phase3-systems.md); CKL 231 | Unverified |
| 2,4 | `HYD PSI` | none (readout) | `(A:HYDRAULIC PRESSURE:1, psi)` | - | SDK-SYSV; CKL 125 | Unverified |
| 2,5 |  | Empty | none: empty | - | - | - |
| 2,6 |  | Empty | none: empty | - | - | - |
| 2,7 |  | Empty | none: empty | - | - | - |
| 2,8 |  | Empty | none: empty | - | - | - |
| 3,1 |  | Empty | none: empty | - | - | - |
| 3,2 | `XFER` | none (readout) | B-var from the input event list (S-1); else `(A:FUEL CROSS FEED, Enum)` | - | SDK-FUELV; README 2.1.1; CKL 366 | Unverified |
| 3,3 | `PUMP L` | none (readout) | `(A:GENERAL ENG FUEL PUMP ON:1, Bool)` | - | SDK-ENGV | Unverified |
| 3,4 | `PUMP R` | none (readout) | `(A:GENERAL ENG FUEL PUMP ON:2, Bool)` | - | SDK-ENGV | Unverified |
| 3,5 |  | Empty | none: empty | - | - | - |
| 3,6 |  | Empty | none: empty | - | - | - |
| 3,7 |  | Empty | none: empty | - | - | - |
| 3,8 |  | Empty | none: empty | - | - | - |
| 4,1 |  | Empty | none: empty | - | - | - |
| 4,2 |  | Empty | none: empty | - | - | - |
| 4,3 |  | Empty | none: empty | - | - | - |
| 4,4 |  | Empty | none: empty | - | - | - |
| 4,5 |  | Empty | none: empty | - | - | - |
| 4,6 |  | Empty | none: empty | - | - | - |
| 4,7 |  | Empty | none: empty | - | - | - |
| 4,8 |  | Empty | none: empty | - | - | - |

### ENGINE

Opened by more 2,3. Changed for two engines: the left engine in row 1, the right in row 2 (N1, N2, ITT, fuel flow,
oil); starter, running and ignition readouts in rows 3 (left) and 4 (right); fuel quantities at 3,6 to 3,8. The
starter and run/stop controls are readouts (open question 5).

| Pos | Title | Press (candidate) | Reads (candidate) | Hold to repeat | Source | Status |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | - | [navigation.md](navigation.md) | - |
| 1,2 | `N1 L` | none (readout) | `(A:TURB ENG N1:1, Percent)` | - | SDK-ENGV, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 1,3 | `N2 L` | none (readout) | `(A:TURB ENG N2:1, Percent)` | - | SDK-ENGV, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 1,4 | `ITT L` | none (readout) | `(A:TURB ENG ITT:1, Celsius)` | - | SDK-ENGV, as [visionjet-sf50.md](visionjet-sf50.md); CKL 74 | Unverified |
| 1,5 | `FF L` | none (readout) | `(A:TURB ENG FUEL FLOW PPH:1, Pounds per hour)` | - | SDK-ENGV, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 1,6 | `OIL P L` | none (readout) | `(A:GENERAL ENG OIL PRESSURE:1, psi)` | - | SDK-ENGV, as [phase3-engine-fuel.md](phase3-engine-fuel.md) | Unverified |
| 1,7 | `OIL T L` | none (readout) | `(A:GENERAL ENG OIL TEMPERATURE:1, fahrenheit)` | - | SDK-ENGV, as [phase3-engine-fuel.md](phase3-engine-fuel.md) | Unverified |
| 1,8 |  | Empty | none: empty | - | - | - |
| 2,1 |  | Empty | none: empty | - | - | - |
| 2,2 | `N1 R` | none (readout) | `(A:TURB ENG N1:2, Percent)` | - | SDK-ENGV, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 2,3 | `N2 R` | none (readout) | `(A:TURB ENG N2:2, Percent)` | - | SDK-ENGV, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 2,4 | `ITT R` | none (readout) | `(A:TURB ENG ITT:2, Celsius)` | - | SDK-ENGV, as [visionjet-sf50.md](visionjet-sf50.md); CKL 74 | Unverified |
| 2,5 | `FF R` | none (readout) | `(A:TURB ENG FUEL FLOW PPH:2, Pounds per hour)` | - | SDK-ENGV, as [visionjet-sf50.md](visionjet-sf50.md) | Unverified |
| 2,6 | `OIL P R` | none (readout) | `(A:GENERAL ENG OIL PRESSURE:2, psi)` | - | SDK-ENGV, as [phase3-engine-fuel.md](phase3-engine-fuel.md) | Unverified |
| 2,7 | `OIL T R` | none (readout) | `(A:GENERAL ENG OIL TEMPERATURE:2, fahrenheit)` | - | SDK-ENGV, as [phase3-engine-fuel.md](phase3-engine-fuel.md) | Unverified |
| 2,8 |  | Empty | none: empty | - | - | - |
| 3,1 |  | Empty | none: empty | - | - | - |
| 3,2 | `START L` | none (readout) | `(A:GENERAL ENG STARTER:1, Bool)` | - | SDK-ENGV; CKL 66 | Unverified |
| 3,3 | `RUN L` | none (readout) | `(A:GENERAL ENG COMBUSTION:1, Bool)` (the engine runs; not the button) | - | SDK-ENGV; CKL 70 | Unverified |
| 3,4 | `IGN L` | none (readout) | `(A:TURB ENG IGNITION SWITCH EX1:1, Enum)` | - | SDK-ENGV | Unverified |
| 3,5 |  | Empty | none: empty | - | - | - |
| 3,6 | `FUEL L` | none (readout) | `(A:FUEL TANK LEFT MAIN QUANTITY, Gallons)` | - | SDK-FUELV | Unverified |
| 3,7 | `FUEL R` | none (readout) | `(A:FUEL TANK RIGHT MAIN QUANTITY, Gallons)` | - | SDK-FUELV | Unverified |
| 3,8 | `FUEL TOT` | none (readout) | `(A:FUEL TOTAL QUANTITY, Gallons)` | - | SDK-FUELV | Unverified |
| 4,1 |  | Empty | none: empty | - | - | - |
| 4,2 | `START R` | none (readout) | `(A:GENERAL ENG STARTER:2, Bool)` | - | SDK-ENGV; CKL 66 | Unverified |
| 4,3 | `RUN R` | none (readout) | `(A:GENERAL ENG COMBUSTION:2, Bool)` (the engine runs; not the button) | - | SDK-ENGV; CKL 70 | Unverified |
| 4,4 | `IGN R` | none (readout) | `(A:TURB ENG IGNITION SWITCH EX1:2, Enum)` | - | SDK-ENGV | Unverified |
| 4,5 |  | Empty | none: empty | - | - | - |
| 4,6 |  | Empty | none: empty | - | - | - |
| 4,7 |  | Empty | none: empty | - | - | - |
| 4,8 |  | Empty | none: empty | - | - | - |

### ICE/ENV

Opened by more 2,4. Anti-ice switches in row 1 (B-vars first; the two pitot/static heat buttons only by B-var,
since the SDK's pitot heat names have no side; main 4,6 keeps the SDK pitot key); climate and pressurization
readouts in row 3 (no write until the input event list names the controls).

| Pos | Title | Press (candidate) | Reads (candidate) | Hold to repeat | Source | Status |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | - | [navigation.md](navigation.md) | - |
| 1,2 | `ENG AI L` | B-var from the input event list (S-1); else `K:ANTI_ICE_TOGGLE_ENG1` | `(A:ENG ANTI ICE:1, Bool)` | - | SDK-ENGE; SDK-ENGV; README 2.1.1; CKL 129 | Unverified |
| 1,3 | `ENG AI R` | B-var from the input event list (S-1); else `K:ANTI_ICE_TOGGLE_ENG2` | `(A:ENG ANTI ICE:2, Bool)` | - | SDK-ENGE; SDK-ENGV; README 2.1.1; CKL 129 | Unverified |
| 1,4 | `WING/STAB` | B-var from the input event list (S-1); else `K:TOGGLE_STRUCTURAL_DEICE` | `(A:STRUCTURAL DEICE SWITCH, Bool)` | - | SDK-AMISCE; SDK-SYSV; README 2.1.1; CKL 191 | Unverified |
| 1,5 | `WSHLD` | B-var from the input event list (S-1); else `K:WINDSHIELD_DEICE_TOGGLE` | `(A:WINDSHIELD DEICE SWITCH, Bool)` | - | SDK-AMISCE; SDK-SYSV; README 2.1.1 | Unverified |
| 1,6 | `P/S L` | B-var from the input event list (S-1) | the same B-var (S-1) | - | README 2.1.1; CKL 239 | Unverified |
| 1,7 | `P/S R` | B-var from the input event list (S-1) | the same B-var (S-1) | - | README 2.1.1; CKL 239 | Unverified |
| 1,8 |  | Empty | none: empty | - | - | - |
| 2,1 |  | Empty | none: empty | - | - | - |
| 2,2 |  | Empty | none: empty | - | - | - |
| 2,3 |  | Empty | none: empty | - | - | - |
| 2,4 |  | Empty | none: empty | - | - | - |
| 2,5 |  | Empty | none: empty | - | - | - |
| 2,6 |  | Empty | none: empty | - | - | - |
| 2,7 |  | Empty | none: empty | - | - | - |
| 2,8 |  | Empty | none: empty | - | - | - |
| 3,1 |  | Empty | none: empty | - | - | - |
| 3,2 | `CLIMATE` | none (readout) | B-var from the input event list (S-1) | - | README 2.1.1; CKL 55 | Unverified |
| 3,3 | `CAB ALT` | none (readout) | `(A:PRESSURIZATION CABIN ALTITUDE, Feet)` | - | SDK-SYSV; CKL 149 | Unverified |
| 3,4 | `CAB RATE` | none (readout) | `(A:PRESSURIZATION CABIN ALTITUDE RATE, Feet/minute)` | - | SDK-SYSV | Unverified |
| 3,5 | `DIFF` | none (readout) | `(A:PRESSURIZATION PRESSURE DIFFERENTIAL, psi)` | - | SDK-SYSV | Unverified |
| 3,6 | `DUMP` | none (readout) | `(A:PRESSURIZATION DUMP SWITCH, Bool)` | - | SDK-SYSV | Unverified |
| 3,7 |  | Empty | none: empty | - | - | - |
| 3,8 |  | Empty | none: empty | - | - | - |
| 4,1 |  | Empty | none: empty | - | - | - |
| 4,2 |  | Empty | none: empty | - | - | - |
| 4,3 |  | Empty | none: empty | - | - | - |
| 4,4 |  | Empty | none: empty | - | - | - |
| 4,5 |  | Empty | none: empty | - | - | - |
| 4,6 |  | Empty | none: empty | - | - | - |
| 4,7 |  | Empty | none: empty | - | - | - |
| 4,8 |  | Empty | none: empty | - | - | - |

### LIGHTS

Opened by more 2,5. New. Exterior lights not on the main page in row 1, cabin signs and the pass lights safety
button in row 2, interior lights in row 3. The emergency lights switch is on SYSTEMS. The light K-events take a
circuit index that is unknown (as on the C172 systems page), so the B-vars come first.

| Pos | Title | Press (candidate) | Reads (candidate) | Hold to repeat | Source | Status |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | - | [navigation.md](navigation.md) | - |
| 1,2 | `RECOG` | B-var from the input event list (S-1); else `K:TOGGLE_RECOGNITION_LIGHTS` | `(A:LIGHT RECOGNITION, Bool)` | - | SDK-ELECE; SDK-SYSV; README 2.1.1 | Unverified |
| 1,3 | `WING` | B-var from the input event list (S-1); else `K:TOGGLE_WING_LIGHTS` | `(A:LIGHT WING, Bool)` | - | SDK-ELECE; SDK-SYSV; README 2.1.1 | Unverified |
| 1,4 |  | Empty | none: empty | - | - | - |
| 1,5 |  | Empty | none: empty | - | - | - |
| 1,6 |  | Empty | none: empty | - | - | - |
| 1,7 |  | Empty | none: empty | - | - | - |
| 1,8 |  | Empty | none: empty | - | - | - |
| 2,1 |  | Empty | none: empty | - | - | - |
| 2,2 | `BELTS` | B-var from the input event list (S-1); else `K:CABIN_SEATBELTS_ALERT_SWITCH_TOGGLE` | `(A:CABIN SEATBELTS ALERT SWITCH, Bool)` | - | SDK-AMISCE; SDK-SYSV; README 2.1.1 | Unverified |
| 2,3 | `NO SMOKE` | B-var from the input event list (S-1); else `K:CABIN_NO_SMOKING_ALERT_SWITCH_TOGGLE` | `(A:CABIN NO SMOKING ALERT SWITCH, Bool)` | - | SDK-AMISCE; SDK-SYSV; README 2.1.1 | Unverified |
| 2,4 | `PASS SAFE` | B-var from the input event list (S-1) | the same B-var (S-1) | - | README 2.1.1; CKL 105 | Unverified |
| 2,5 |  | Empty | none: empty | - | - | - |
| 2,6 |  | Empty | none: empty | - | - | - |
| 2,7 |  | Empty | none: empty | - | - | - |
| 2,8 |  | Empty | none: empty | - | - | - |
| 3,1 |  | Empty | none: empty | - | - | - |
| 3,2 | `CABIN` | B-var from the input event list (S-1); else `K:TOGGLE_CABIN_LIGHTS` | `(A:LIGHT CABIN, Bool)` | - | SDK-ELECE; SDK-SYSV; README 2.1.1 | Unverified |
| 3,3 | `PANEL` | B-var from the input event list (S-1); else `K:PANEL_LIGHTS_TOGGLE` | `(A:LIGHT PANEL, Bool)` | - | SDK-ELECE; SDK-SYSV; README 2.1.1 | Unverified |
| 3,4 |  | Empty | none: empty | - | - | - |
| 3,5 |  | Empty | none: empty | - | - | - |
| 3,6 |  | Empty | none: empty | - | - | - |
| 3,7 |  | Empty | none: empty | - | - | - |
| 3,8 |  | Empty | none: empty | - | - | - |
| 4,1 |  | Empty | none: empty | - | - | - |
| 4,2 |  | Empty | none: empty | - | - | - |
| 4,3 |  | Empty | none: empty | - | - | - |
| 4,4 |  | Empty | none: empty | - | - | - |
| 4,5 |  | Empty | none: empty | - | - | - |
| 4,6 |  | Empty | none: empty | - | - | - |
| 4,7 |  | Empty | none: empty | - | - | - |
| 4,8 |  | Empty | none: empty | - | - | - |

### FMS

Opened by more 2,6. New. The FMC's function keys (index 1) and its twelve line select keys: L1-L3 and R1-R3 in row
2, L4-L6 and R4-R6 in row 3. CLR sends `CLR_LONG` on a long press. No FMS key reads a state; the CDU screen stays
in the sim.

| Pos | Title | Press (candidate) | Reads (candidate) | Hold to repeat | Source | Status |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | - | [navigation.md](navigation.md) | - |
| 1,2 | `IDX` | `H:WT21_FMC_1_BTN_IDX` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 1,3 | `FPLN` | `H:WT21_FMC_1_BTN_FPLN` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 1,4 | `LEGS` | `H:WT21_FMC_1_BTN_LEGS` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 1,5 | `DEP ARR` | `H:WT21_FMC_1_BTN_DEPARR` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 1,6 | `PERF` | `H:WT21_FMC_1_BTN_PERF` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 1,7 | `DIR` | `H:WT21_FMC_1_BTN_DIR` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 1,8 | `EXEC` | `H:WT21_FMC_1_BTN_EXEC` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 2,1 | `L1` | `H:WT21_FMC_1_BTN_L1` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 2,2 | `L2` | `H:WT21_FMC_1_BTN_L2` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 2,3 | `L3` | `H:WT21_FMC_1_BTN_L3` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 2,4 | `MFD ADV` | `H:WT21_FMC_1_BTN_MFD_ADV` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 2,5 | `MFD DATA` | `H:WT21_FMC_1_BTN_MFD_DATA` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 2,6 | `R1` | `H:WT21_FMC_1_BTN_R1` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 2,7 | `R2` | `H:WT21_FMC_1_BTN_R2` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 2,8 | `R3` | `H:WT21_FMC_1_BTN_R3` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 3,1 | `L4` | `H:WT21_FMC_1_BTN_L4` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 3,2 | `L5` | `H:WT21_FMC_1_BTN_L5` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 3,3 | `L6` | `H:WT21_FMC_1_BTN_L6` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 3,4 | `DSPL MENU` | `H:WT21_FMC_1_BTN_DSPL_MENU` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 3,5 | `TUN` | `H:WT21_FMC_1_BTN_TUN` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 3,6 | `R4` | `H:WT21_FMC_1_BTN_R4` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 3,7 | `R5` | `H:WT21_FMC_1_BTN_R5` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 3,8 | `R6` | `H:WT21_FMC_1_BTN_R6` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 4,1 | `MSG` | `H:WT21_FMC_1_BTN_MSG` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 4,2 | `PREV` | `H:WT21_FMC_1_BTN_PREVPAGE` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 4,3 | `NEXT` | `H:WT21_FMC_1_BTN_NEXTPAGE` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 4,4 | `CLR` | `H:WT21_FMC_1_BTN_CLR`, long press `H:WT21_FMC_1_BTN_CLR_LONG` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 4,5 |  | Empty | none: empty | - | - | - |
| 4,6 |  | Empty | none: empty | - | - | - |
| 4,7 |  | Empty | none: empty | - | - | - |
| 4,8 |  | Empty | none: empty | - | - | - |

### FMS ABC

Opened by more 2,7. New. The FMC letters A-Z in reading order, then space, slash, CLR and EXEC (index 1).

| Pos | Title | Press (candidate) | Reads (candidate) | Hold to repeat | Source | Status |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | - | [navigation.md](navigation.md) | - |
| 1,2 | `A` | `H:WT21_FMC_1_BTN_A` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 1,3 | `B` | `H:WT21_FMC_1_BTN_B` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 1,4 | `C` | `H:WT21_FMC_1_BTN_C` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 1,5 | `D` | `H:WT21_FMC_1_BTN_D` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 1,6 | `E` | `H:WT21_FMC_1_BTN_E` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 1,7 | `F` | `H:WT21_FMC_1_BTN_F` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 1,8 | `G` | `H:WT21_FMC_1_BTN_G` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 2,1 | `H` | `H:WT21_FMC_1_BTN_H` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 2,2 | `I` | `H:WT21_FMC_1_BTN_I` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 2,3 | `J` | `H:WT21_FMC_1_BTN_J` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 2,4 | `K` | `H:WT21_FMC_1_BTN_K` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 2,5 | `L` | `H:WT21_FMC_1_BTN_L` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 2,6 | `M` | `H:WT21_FMC_1_BTN_M` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 2,7 | `N` | `H:WT21_FMC_1_BTN_N` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 2,8 | `O` | `H:WT21_FMC_1_BTN_O` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 3,1 | `P` | `H:WT21_FMC_1_BTN_P` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 3,2 | `Q` | `H:WT21_FMC_1_BTN_Q` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 3,3 | `R` | `H:WT21_FMC_1_BTN_R` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 3,4 | `S` | `H:WT21_FMC_1_BTN_S` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 3,5 | `T` | `H:WT21_FMC_1_BTN_T` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 3,6 | `U` | `H:WT21_FMC_1_BTN_U` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 3,7 | `V` | `H:WT21_FMC_1_BTN_V` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 3,8 | `W` | `H:WT21_FMC_1_BTN_W` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 4,1 | `X` | `H:WT21_FMC_1_BTN_X` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 4,2 | `Y` | `H:WT21_FMC_1_BTN_Y` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 4,3 | `Z` | `H:WT21_FMC_1_BTN_Z` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 4,4 | `SP` | `H:WT21_FMC_1_BTN_SP` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 4,5 | `/` | `H:WT21_FMC_1_BTN_DIV` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 4,6 | `CLR` | `H:WT21_FMC_1_BTN_CLR`, long press `H:WT21_FMC_1_BTN_CLR_LONG` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 4,7 |  | Empty | none: empty | - | - | - |
| 4,8 | `EXEC` | `H:WT21_FMC_1_BTN_EXEC` | none: FMS key (no readable state) | - | WT21-H | Unverified |

### FMS 123

Opened by more 2,8. New. The FMC digits as a keypad, dot and plus/minus, CLR and EXEC (index 1).

| Pos | Title | Press (candidate) | Reads (candidate) | Hold to repeat | Source | Status |
|---|---|---|---|---|---|---|
| 1,1 |  | Back | none: back key | - | [navigation.md](navigation.md) | - |
| 1,2 | `1` | `H:WT21_FMC_1_BTN_1` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 1,3 | `2` | `H:WT21_FMC_1_BTN_2` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 1,4 | `3` | `H:WT21_FMC_1_BTN_3` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 1,5 |  | Empty | none: empty | - | - | - |
| 1,6 |  | Empty | none: empty | - | - | - |
| 1,7 |  | Empty | none: empty | - | - | - |
| 1,8 |  | Empty | none: empty | - | - | - |
| 2,1 |  | Empty | none: empty | - | - | - |
| 2,2 | `4` | `H:WT21_FMC_1_BTN_4` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 2,3 | `5` | `H:WT21_FMC_1_BTN_5` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 2,4 | `6` | `H:WT21_FMC_1_BTN_6` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 2,5 |  | Empty | none: empty | - | - | - |
| 2,6 |  | Empty | none: empty | - | - | - |
| 2,7 |  | Empty | none: empty | - | - | - |
| 2,8 | `CLR` | `H:WT21_FMC_1_BTN_CLR`, long press `H:WT21_FMC_1_BTN_CLR_LONG` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 3,1 |  | Empty | none: empty | - | - | - |
| 3,2 | `7` | `H:WT21_FMC_1_BTN_7` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 3,3 | `8` | `H:WT21_FMC_1_BTN_8` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 3,4 | `9` | `H:WT21_FMC_1_BTN_9` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 3,5 |  | Empty | none: empty | - | - | - |
| 3,6 |  | Empty | none: empty | - | - | - |
| 3,7 |  | Empty | none: empty | - | - | - |
| 3,8 |  | Empty | none: empty | - | - | - |
| 4,1 |  | Empty | none: empty | - | - | - |
| 4,2 | `.` | `H:WT21_FMC_1_BTN_DOT` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 4,3 | `0` | `H:WT21_FMC_1_BTN_0` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 4,4 | `+/-` | `H:WT21_FMC_1_BTN_PLUSMINUS` | none: FMS key (no readable state) | - | WT21-H | Unverified |
| 4,5 |  | Empty | none: empty | - | - | - |
| 4,6 |  | Empty | none: empty | - | - | - |
| 4,7 |  | Empty | none: empty | - | - | - |
| 4,8 | `EXEC` | `H:WT21_FMC_1_BTN_EXEC` | none: FMS key (no readable state) | - | WT21-H | Unverified |

## Steps in the sim

None of these blocks the build: without them the build uses the SDK and WT21 names above, B-var rows without a
name, everything Unverified.

- **S-1: the input event list.** Start the Stream Deck app with PilotsDeck, load a CJ4 flight, wait about 30 s
  after it loads, then quit. PilotsDeck writes the CJ4's `InputEvents.txt` (every B-var), which the build copies
  into `docs/reference/` (as it did for the SF50), and its log shows the aircraft string that the Profile
  Manager mapping needs ([package.md](package.md)). Settles every "none yet" row.
- **S-2: the name.** Note the name the aircraft list shows for the CJ4 and any variants. Settles this page's
  name line. Without it: "Cessna Citation CJ4" (FSE-LIST).
- **S-3: which variable each control drives.** A capture with the repo's read-only SimConnect monitor while you
  work, with the mouse: the battery, generator, avionics and light switches, engine anti-ice, the parking
  brake, the HDG, ALT and baro knobs and the autopilot mode buttons. Settles which SimVar index each control
  drives. Without it: SDK index 1 (left) and 2 (right).
- **S-4: input events or H-events.** In developer mode, press CTRL+G over one FMS key and one autopilot button
  (MF-IE24) and note whether it lists an input event. Settles input events against the WT21 H-events. Without
  it: WT21 H-events for the FMS, DCP and CCP keys, SDK K-events for the autopilot.

## Open questions

These wait for you; each has a working value the draft uses until you answer.

1. Which CJ4: the MSFS 2024 default (in the sim's streamed-package cache now) or an add-on or mod such as CJ4
   Plus? Working value: the default. Another answer adds that product's sources; the default rows stay.
2. Order: build the CJ4 profile before or after the next VisionJet unit (its touch controller page, which waits
   for your captures)? Working value: whichever inputs arrive first, and the CJ4 build after the VisionJet hold
   test. This changes only the order of work.
3. Which pages matter most to you (the FMS keyboard pages, the DCP and CCP pages)? Working value: all draft
   pages. Another answer drops pages.
4. Profile name: `MSFS2024 CJ4`? Working value: yes; it stays the same across versions once built.
5. Engine starter and run/stop: readouts (the working value) or guarded keys (a long press, on a second-level
   page)?
6. Pilot side only (index 1) for the FMC, DCP and CCP keys? Working value: yes. Another answer: a copilot page
   later.

## Sources

| Tag | Source |
|---|---|
| FSE-LIST | FSElite, all aircraft in MSFS 2024 (pre-release list; posted 2024-09-19, updated 2024-09-23), https://fselite.net/content/all-aircraft-featured-in-microsoft-flight-simulator-2024/, read 2026-11-18 |
| FORUM-LIST | Official forum, user list of first-party aircraft (2025-10-09, edited to 2026-04-30), https://forums.flightsimulator.com/t/msfs-2024-list-of-all-first-party-aircraft-with-links-to-official-info-for-each/741340, read 2026-11-18 |
| FORUM-CJ4 | Official forum, "[MSFS2024] Cessna Citation CJ4" thread, page 1 (first post 2024-11-18), https://forums.flightsimulator.com/t/msfs2024-cessna-citation-cj4/664505, read 2026-11-18 |
| WC-LIST | Windows Central, MSFS 2024 list of every aircraft, https://www.windowscentral.com/gaming/xbox/microsoft-flight-simulator-2024-list-of-every-aircraft (search result summary only, 2026-11-18) |
| FS-MANUALS | Official aircraft manuals page, https://www.flightsimulator.com/aircraft-manuals/ (linked by FORUM-LIST; not opened) |
| WT21-OV | MSFS Avionics Framework docs (2024), WT21 overview, https://microsoft.github.io/msfs-avionics-mirror/2024/docs/avionics/wt21/overview, read 2026-11-18 |
| WT21-H | MSFS Avionics Framework docs (2024), WT21 H event list, https://microsoft.github.io/msfs-avionics-mirror/2024/docs/avionics/wt21/h-event-list, read 2026-11-18 |
| WT21-CKL | MSFS Avionics Framework docs (2024), WT21 electronic checklists, https://microsoft.github.io/msfs-avionics-mirror/2024/docs/avionics/wt21/electronic-checklists, read 2026-11-18 |
| WT-WIKI20 | Working Title CJ4 mod (MSFS 2020) wiki, Sim Variables, https://github.com/Working-Title-MSFS-Mods/fspackages/wiki/Sim-Variables, read 2026-11-18 |
| WT-REL20 | Working Title CJ4 v0.10.3 release (repository archived 2024-05-16), https://github.com/Working-Title-MSFS-Mods/fspackages/releases/tag/cj4-v0.10.3, read 2026-11-18 |
| CJ4P | flightsim.to, CJ4 Plus, https://flightsim.to/addon/98503/cj4-plus, read 2026-11-18 |
| CJ4RM | flightsim.to, Asobo Cessna Citation CJ4 realism mod, https://flightsim.to/addon/60697/asobo-cessna-citation-cj4-realism-mod, read 2026-11-18 |
| MF-IE24 | MobiFlight docs, input events in MSFS 2024, https://docs.mobiflight.com/guides/input-events-2024/, read 2026-11-18 |
| HH-CJ4 | HubHop presets for the CJ4, https://hubhop.mobiflight.com/presets/?aircraft=Cessna+Citation+CJ4 (not read: the page needs a browser; preset counts open) |
| CKL | The default CJ4's checklist file, in its package in the sim's streamed-package cache (label texts only; cited by line), read 2026-11-18 |
| SDK-APE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-autopilot-and-flight-assistance-events/, read 2026-11-18 |
| SDK-APV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-autopilot-and-assistant-variables/, read 2026-11-18 |
| SDK-ELECE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-electrical-events/, read 2026-11-18 |
| SDK-AMISCE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-miscellaneous-events/, read 2026-11-18 |
| SDK-ENGE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-engine-events/, read 2026-11-18 |
| SDK-ENGV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-engine-variables/, read 2026-11-18 |
| SDK-FUELV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-fuel-variables/, read 2026-11-18 |
| SDK-SYSV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-system-variables/, read 2026-11-18 |
| SDK-FCE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-flight-control-events/, read 2026-11-18 |
| SDK-CTLV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-control-variables/, read 2026-11-18 |
| SDK-ELECV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-electrics-variables/ (as in [visionjet-g2-research.md](visionjet-g2-research.md)) |
| SDK-GEARV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-brake-and-landing-gear-variables/ (as in [visionjet-g2-research.md](visionjet-g2-research.md)) |
| SDK-FMV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-flight-model-variables/ (as in [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md)) |
| SDK-RADV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-radio-navigation-variables/ (as in [phase2-main-page.md](phase2-main-page.md)) |
| SDK-RADE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-radio-navigation-events/ (as in [phase2-main-page.md](phase2-main-page.md)) |
| SDK-INSTE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-instrumentation-events/ (as in [phase2-main-page.md](phase2-main-page.md)) |
| SDK-MISCE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/miscellaneous-events/ (as in [phase2-main-page.md](phase2-main-page.md)) |
| SDK-CAMV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/camera-variables/ (as in [phase2-trim-views.md](phase2-trim-views.md)) |
| SDK-UNITS | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/simulation-variable-units/ (as in [phase2-main-page.md](phase2-main-page.md)) |
| README | PilotsDeck README, section 2.1.1 (address forms), as in [installation.md](installation.md) |
