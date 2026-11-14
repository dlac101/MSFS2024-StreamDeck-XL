# Phase 3: Autopilot page (GFC 700), Cessna 172 G1000

**Status: generated, not yet sim-tested.** The page is in the generated profile, but nothing on it has been
tried in the app or the sim yet. Every name below is recorded as "Unverified" in
[aircraft-mappings.md](aircraft-mappings.md) ("Phase 3 autopilot page") until the checks in
[tests/manual-checklist.md](../tests/manual-checklist.md), section "P3-1: Autopilot page (C172 G1000)", pass.

Goal: the GFC 700 autopilot on one Stream Deck page. The mode keys (AP, FD, HDG, NAV, APR, BC, VNV, ALT,
VS, FLC) are lit from the sim's own state, and the selected values (heading bug, course, selected altitude,
vertical speed target, FLC speed target) each have a readout with a step up and a step down key. The main
page's AP row (2,1 to 2,8) stays as it is; this page adds BC, VNV and the selected values.

The page is part of the generated profile `MSFS2024 C172 G1000` (same file, same name, same import as the
main page: see [phase2-main-page.md](phase2-main-page.md), "Import the profile"). No script and no image to
install. The table below is the reference for what each key holds; `tools/profilegen/check.py` compares the
profile with the "Key table: autopilot" section key by key.

Nothing on this page uses keyboard bindings, vJoy or anything tied to a controller: the keys send SimConnect
events (K-events), G1000 H-events or one input event (B-Var), and the indicators and readouts read SimVars
and one L-Var, so they work the same with the Xbox Elite controller and the T.16000M + TWCS.

## Where the page sits

A second-level folder page **autopilot**, opened by the folder key `AUTOPILOT` at **MORE 1,6** (next to
COM PAD; [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md), "Key table: more"). Position 1,6 was free in
the data file and in both local icon profiles the user runs (ProfilesV3, read 2026-11-14). How the pages
connect: [navigation.md](navigation.md).

## Layout: autopilot

Positions are **row,column**, 1-based, row 1 at the top. 1,1 is the back key (it returns to MORE), as on
every child page. Row 1 holds AP, FD and the lateral modes in GFC 700 order, then VNV; column 1 holds the
vertical modes; columns 2 to 6 hold one value each: "+" above its readout, "-" below it (a press higher up
the column raises the value).

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | AP | FD | HDG | NAV | APR | BC | VNV |
| **Row 2** | ALT | HDG+ | CRS+ | ALT+ | VS+ | SPD+ | (YD) | |
| **Row 3** | VS | HDG BUG | CRS1 | ALT SEL | VS TGT | FLC SPD | (LVL) | |
| **Row 4** | FLC | HDG- | CRS- | ALT- | VS- | SPD- | | |

(YD) and (LVL) are reserved and empty: this aircraft has neither (see "Not on this page, and why").

## Key table: autopilot

Action names and templates T1, T2, T3, T5 as in [phase2-main-page.md](phase2-main-page.md) ("What each key
holds"). **Back** = the Stream Deck app's back key (`backtoparent`), added by the generator on every child
page. "Empty" = no action on that key. Source tags: "Sources" below; "IE n" = line n of
[reference/InputEvents-C172-G1000.txt](reference/InputEvents-C172-G1000.txt).

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to the MORE page | none | Back key |
| 1,2 | `AP` | Dynamic Button | T2 | `K:AP_MASTER` [SDK-APE; AM] | `(A:AUTOPILOT MASTER, Bool)` [SDK-APV; AM] | On/Off image |
| 1,3 | `FD` | Dynamic Button | T2 | `K:TOGGLE_FLIGHT_DIRECTOR` [SDK-APE; SDK-APT] | `(A:AUTOPILOT FLIGHT DIRECTOR ACTIVE, Bool)` [SDK-APV] | On/Off image |
| 1,4 | `HDG` | Dynamic Button | T2 | `K:AP_HDG_HOLD` [SDK-APE] | `(A:AUTOPILOT HEADING LOCK, Bool)` [SDK-APV] | On/Off image |
| 1,5 | `NAV` | Dynamic Button | T2 | `K:AP_NAV1_HOLD` [SDK-APE; SDK-APT] | `(A:AUTOPILOT NAV1 LOCK, Bool)` [SDK-APV] | On/Off image |
| 1,6 | `APR` | Dynamic Button | T2 | `K:AP_APR_HOLD` [SDK-APE; SDK-APT] | `(A:AUTOPILOT APPROACH HOLD, Bool)` [SDK-APV] | On/Off image |
| 1,7 | `BC` | Dynamic Button | T2 | `K:AP_BC_HOLD` [SDK-APE; SDK-APT] | `(A:AUTOPILOT BACKCOURSE HOLD, Bool)` [SDK-APV] | On/Off image |
| 1,8 | `VNV` | Dynamic Button | T1 | `B:as1000_autopilot_vertical_navigation_pfd`, On `1` / Off `0` [IE 29; README 2.1.1] | `L:XMLVAR_VNAVButtonValue` [SDK-APT; lead: JIBLET; weak, A-6] | On/Off image, Special State |
| 2,1 | `ALT` | Dynamic Button | T2 | `K:AP_ALT_HOLD` [SDK-APE; SDK-APT] | `(A:AUTOPILOT ALTITUDE LOCK, Bool)` [SDK-APV] | On/Off image |
| 2,2 | `HDG+` | Simple Button | T5 | `K:HEADING_BUG_INC` [SDK-APE] | none | fixed image |
| 2,3 | `CRS+` | Simple Button | T5 | Main `H:AS1000_PFD_CRS_INC` [SDK-AS1000], Second (long press) `K:VOR1_OBI_FAST_INC` [SDK-RADE; README 2.1] | none | fixed image |
| 2,4 | `ALT+` | Simple Button | T5 | Main `K:AP_ALT_VAR_INC` [SDK-APE], Second (long press) `K:AP_ALT_VAR_INC:1000` [SDK-APE; SDK-AS1000; README 2.1.1, 2.1; A-4] | none | fixed image |
| 2,5 | `VS+` | Simple Button | T5 | `K:AP_VS_VAR_INC` [SDK-APE] | none | fixed image |
| 2,6 | `SPD+` | Simple Button | T5 | `K:AP_SPD_VAR_INC` [SDK-APE] | none | fixed image |
| 2,7 | | Empty | | | | YD reserved (A-7) |
| 2,8 | | Empty | | | | |
| 3,1 | `VS` | Dynamic Button | T2 | `K:AP_VS_HOLD` [SDK-APE] | `(A:AUTOPILOT VERTICAL HOLD, Bool)` [SDK-APV] | On/Off image |
| 3,2 | `HDG BUG` | Display Value | T3 | `K:AP_HDG_CURRENT_HDG_SET` [SDK-APE; lead: FORUM; A-5] | `(A:AUTOPILOT HEADING LOCK DIR, Degrees)` [SDK-APV; A-5] | Format `3.0:%s°` |
| 3,3 | `CRS1` | Display Value | T3 | `H:AS1000_PFD_CRS_PUSH` [SDK-AS1000] | `(A:NAV OBS:1, Degrees)` [SDK-RADV] | Format `3.0:%s°` |
| 3,4 | `ALT SEL` | Display Value | T3 | none | `(A:AUTOPILOT ALTITUDE LOCK VAR, Feet)` [SDK-APV; A-5] | Format `1.0` |
| 3,5 | `VS TGT` | Display Value | T3 | none | `(A:AUTOPILOT VERTICAL HOLD VAR, Feet/minute)` [SDK-APV] | Format `1.0` |
| 3,6 | `FLC SPD` | Display Value | T3 | none | `(A:AUTOPILOT AIRSPEED HOLD VAR, Knots)` [SDK-APV] | Format `1.0` |
| 3,7 | | Empty | | | | LVL reserved (A-7) |
| 3,8 | | Empty | | | | |
| 4,1 | `FLC` | Dynamic Button | T2 | `K:FLIGHT_LEVEL_CHANGE` [SDK-APE; SDK-APT; A-9] | `(A:AUTOPILOT FLIGHT LEVEL CHANGE, Bool)` [SDK-APV] | On/Off image |
| 4,2 | `HDG-` | Simple Button | T5 | `K:HEADING_BUG_DEC` [SDK-APE] | none | fixed image |
| 4,3 | `CRS-` | Simple Button | T5 | Main `H:AS1000_PFD_CRS_DEC` [SDK-AS1000], Second (long press) `K:VOR1_OBI_FAST_DEC` [SDK-RADE; README 2.1] | none | fixed image |
| 4,4 | `ALT-` | Simple Button | T5 | Main `K:AP_ALT_VAR_DEC` [SDK-APE], Second (long press) `K:AP_ALT_VAR_DEC:1000` [SDK-APE; SDK-AS1000; README 2.1.1, 2.1; A-4] | none | fixed image |
| 4,5 | `VS-` | Simple Button | T5 | `K:AP_VS_VAR_DEC` [SDK-APE] | none | fixed image |
| 4,6 | `SPD-` | Simple Button | T5 | `K:AP_SPD_VAR_DEC` [SDK-APE] | none | fixed image |
| 4,7 | | Empty | | | | |
| 4,8 | | Empty | | | | |

## What the keys do

- **Mode keys** (AP, FD, HDG, NAV, APR, BC, ALT, VS, FLC): a press sends the K-event, which toggles the
  mode in the sim. The key is lit only while its SimVar reads 1, so a press the sim refuses (APR with no
  approach loaded, NAV with no signal, a mode that needs AP on) leaves it dark. Pressing one mode can drop
  another (the GFC 700 leaves ALT when VS engages, and so on): the keys show what the sim does.
  AP, HDG, ALT, VS, NAV, APR, FLC and FD send the same events as the main page's AP row.
- **VNV** (1,8): a press writes the aircraft's VNV input event: `1` when the input event itself reads `0`,
  else `0` (PilotsDeck compares the variable it writes, not the L-Var it shows: README 2.1.2), as BAT does on
  the main page. Lit while `L:XMLVAR_VNAVButtonValue` reads 1. That L-Var is what Asobo's cockpit VNV button
  code toggles (SDK-APT, a general-path template page, not a `/msfs2024/` page) and what Jiblet's pre-2024
  profile reads (a lead). **The read is a weak source (A-6)**: if the key never lights while VNV shows on the
  PFD, see "Fallbacks".
- **HDG+ / HDG-** (2,2 / 4,2): one degree per press expected (`HEADING_BUG_INC/DEC`, no parameter; the SDK
  states no step or wrap: the checklist records both). **HDG BUG** (3,2) shows the selected heading as three
  digits with a degree sign (`005°`); a press syncs the bug to the current heading (`AP_HDG_CURRENT_HDG_SET`
  with no parameter = slot 0, which the SDK says sets every slot).
- **CRS+ / CRS-** (2,3 / 4,3): the G1000 PFD CRS knob's own H-events, one degree per press; they follow the
  CDI source like the knob. A **long press** (hold at least 0.5 s; hold a full second to be sure) steps
  10 degrees with `VOR1_OBI_FAST_INC/DEC`, which stop at 0/360 instead of wrapping (SDK-RADE).
  **CRS1** (3,3) shows the NAV1 course (`NAV OBS:1`) as `005°`; a press is the CRS knob push (centres the
  CDI on the course to the station).
- **ALT+ / ALT-** (2,4 / 4,4): `AP_ALT_VAR_INC/DEC` with no parameter, the sim's own step (100 ft
  expected). A **long press** sends the same events with the parameter `1000`, taken as a 1000 ft step
  (the AS1000 ALT knob has 100 and 1000 ft increments, SDK-AS1000). **Risk (A-4):** the SDK names that
  parameter "New reference altitude", so the long press may set the selected altitude **to** 1000 ft
  instead of stepping by 1000. That changes only the selected altitude (recoverable with the short
  presses); the checklist checks it and "Fallbacks" gives the repair. **ALT SEL** (3,4) shows the selected
  altitude in feet (`5500`); no press command.
- **VS+ / VS-** (2,5 / 4,5): `AP_VS_VAR_INC/DEC`, the sim's step (100 fpm expected). **VS TGT** (3,5) shows
  the target in ft/min with the sim's sign (`-500`; a climb has no `+`, PilotsDeck's Format has no sign
  option).
- **SPD+ / SPD-** (2,6 / 4,6): `AP_SPD_VAR_INC/DEC`, the sim's step. **FLC SPD** (3,6) shows the FLC speed
  target in knots.
- **FLC** (4,1) sends `FLIGHT_LEVEL_CHANGE` only. The cockpit FLC button also sets the speed target to the
  current airspeed (SDK-APT); the key does not, so the target may be an old value (A-9; the checklist
  checks it).
- **Readouts always show the selected value**, also while their mode is off (A-10). The G1000 PFD always
  shows the heading bug and the selected altitude; it shows the VS and FLC targets only in their modes.
- NAV and APR are lit only from the HOLD SimVars, as the sim sets them; an armed (white) mode on the PFD
  may or may not light the key (A-8, recorded in the checklist).
- With no flight loaded the keys look as phase2-main-page.md "What the keys show when the sim isn't there"
  says: with no sim running the plugin is Idle and the keys show a static preview; with the sim running but no
  flight loaded every key shows the plugin's Wait image.

## Which route each key uses, and why

The 2024 C172 lists input events (B-Vars) for every GFC 700 button and for the HDG, CRS and ALT knobs
(IE 6 to 35, 61 to 64, 79 to 82). In MSFS 2024 aircraft a cockpit control may drive a B-Var and a
different SimVar index than the standard K-event (the battery, [aircraft-mappings.md](aircraft-mappings.md),
"Battery"). Here the K-event route is used wherever one exists, because:

- PilotsDeck writes a B-Var as a value (README 2.1.1, BVAR), and the value a push button needs is not known
  (the main page's AP rows: "push value unknown").
- The mode SimVars are the autopilot's own state (SDK-APV), and the cockpit buttons change them through
  the same K-events (SDK-APT: FD, ALT, BC, NAV, APR, FLC buttons send exactly these; HDG and VS send the
  `AP_PANEL_` variants). There is no second SimVar index involved, so the battery fault does not apply.
- `AP_MASTER` with `(A:AUTOPILOT MASTER, Bool)` already passed in this aircraft both ways (2026-11-11).

| Key | Input event in IE | Route used | Reason |
|---|---|---|---|
| AP | IE 15 `as1000_autopilot_ap_pfd` | K-event | verified 2026-11-11 (aircraft-mappings.md) |
| FD | IE 21 `as1000_autopilot_fd_pfd` | K-event | the cockpit button's own event (SDK-APT); as main 2,8 |
| HDG | IE 25 `as1000_autopilot_heading_pfd` | K-event | as main 2,2; the cockpit sends `AP_PANEL_HEADING_HOLD` (fallback) |
| NAV | IE 27 `as1000_autopilot_navigation_pfd` | K-event | the cockpit button's own event; as main 2,5 |
| APR | IE 17 `as1000_autopilot_approach_pfd` | K-event | the cockpit button's own event; as main 2,6 |
| BC | IE 19 `as1000_autopilot_backcourse_pfd` | K-event | the cockpit button's own event |
| ALT | IE 13 `as1000_autopilot_altitude_pfd` | K-event | the cockpit button's own event; as main 2,3 |
| VS | IE 33 `as1000_autopilot_verticalspeed_pfd` | K-event | as main 2,4; the cockpit sends `AP_PANEL_VS_HOLD` (fallback) |
| FLC | IE 23 `as1000_autopilot_flightlevelchange_pfd` | K-event | the cockpit button's event; as main 2,7 (A-9) |
| VNV | IE 29 `as1000_autopilot_vertical_navigation_pfd` | **B-Var** | no K-event and no SimVar for VNV exist (SDK-APE, SDK-APV) |
| HDG+/- | IE 80 `as1000_heading_pfd` (knob) | K-event | `HEADING_BUG_INC/DEC` need no value |
| HDG BUG press | IE 82 `as1000_heading_sync_pfd` | K-event | `AP_HDG_CURRENT_HDG_SET` (A-5) |
| CRS+/-, CRS1 press | IE 62 `as1000_course_pfd`, IE 64 `as1000_course_push_pfd` | H-event | the CRS knob's own events; P2-4's PFD H-events from the same SDK page work in this aircraft (LR144-C4) |
| CRS long press | (as above) | K-event | no 10-degree H-event; `VOR1_OBI_FAST_*` (SDK-RADE) |
| ALT+/- | IE 7, 9 `as1000_altitude_inner/outer_pfd` | K-event | the step is a K-event parameter, no B-Var value is known (A-4) |
| VS+/- | IE 31, 35 `as1000_autopilot_verticalspeed_down/up_pfd` | K-event | `AP_VS_VAR_INC/DEC` need no value |
| SPD+/- | (the same UP/DN wheel in FLC, IE 31/35) | K-event | `AP_SPD_VAR_INC/DEC` need no value |

Command types (saved `ActionType`, as `check.py` checks them): `K:` 16, `H:` 8, `B:` 13, no command 3. A
K-event with a parameter is written `K:NAME:value` (README 2.1.1 KVAR: "positive integer" parameters); no
negative value is needed (VS uses INC/DEC, never `AP_VS_VAR_SET_ENGLISH`).

## What each key holds

Every key is a copy of a template with only these fields changed (the generator does this; never edit the
profile by hand).

- **T2** (the Phase 1 AP key, main page T2): Command `AddressAction` = the K-event, Value Address `Address`
  = the SimVar, On `1` / Off `0`. Title size 14 (the template's 10, by the rule in navigation.md "Rules").
- **T1** for VNV (the Phase 1 BAT key, main page T1): Command `B:as1000_autopilot_vertical_navigation_pfd`,
  On `1` / Off `0`; Value Address `L:XMLVAR_VNAVButtonValue`; Special State on with "any value"
  (`HasIndication`, `IndicationValueAny`), so an unexpected value shows the special image instead of no
  image. Title size 15 (the template's).
- **T3** (the Phase 1 HDG readout, main page T3): Value Address and Format as in the table; HDG BUG and
  CRS1 also have a press command (`ActionType` 16 / 8, `AddressAction`), as main CDI and BARO. Title size 15.
- **T5** (template `simple_button`, states from the Phase 1 AP key, `LinkedTitle` on, Background image
  `Images/Switch.png`, Draw Box off), as main ATC/MAP and the PFD keys: Command Type and Address from the
  table. CRS+/-, ALT+/- also have **long press** on (`HasLongPress`) with a Second Command
  (`ActionTypeLong` 16, `AddressActionLong`), as COMPAD CLR. Title size 14.
- The folder key `AUTOPILOT` on MORE and the back key: title size 12, as every folder and back key.

## Not on this page, and why

| Function | Why not |
|---|---|
| YD (2,7 reserved) | No yaw damper button on the AS1000 bezel (SDK-AS1000) and no input event in this aircraft (IE). navigation.md: a function an aircraft lacks leaves its key empty. If wanted later: `K:YAW_DAMPER_TOGGLE` / `(A:AUTOPILOT YAW DAMPER, Bool)` (SDK-APE, SDK-APV), expected to do nothing here. |
| LVL (3,7 reserved) | No LVL button on the AS1000 bezel and no input event. If wanted later: `K:AP_WING_LEVELER` / `(A:AUTOPILOT WING LEVELER, Bool)`. |
| Armed modes (NAV/APR/GS armed shown on the key) | A later unit: a Special State on `AUTOPILOT APPROACH ARM` / `GLIDESLOPE ARM` (A-8). |
| Dashes on a readout when its mode is off | Would need a Special State per key and a design call (A-10). |
| VS readout with a `+` for climbs | PilotsDeck's Format has no sign option (README 2.2.2). |
| The MFD-side input events (`..._mfd`) | The PFD side is enough; one set of keys. |

## Fallbacks

Use one only if the checklist shows the main route doesn't work, and say which one you used. None is
tested. Each is a data-file change (then regenerate); none needs a script.

| Key | If the check fails | Fallback | Source |
|---|---|---|---|
| FD | press does nothing | `B:as1000_autopilot_fd_pfd` | IE 21 |
| HDG | press does nothing | `K:AP_PANEL_HEADING_HOLD`, then `B:as1000_autopilot_heading_pfd` | SDK-APE, SDK-APT; IE 25 |
| NAV, APR, BC | press does nothing | `B:as1000_autopilot_navigation_pfd`, `..._approach_pfd`, `..._backcourse_pfd` | IE 27, 17, 19 |
| ALT | press does nothing | `K:AP_PANEL_ALTITUDE_HOLD`, then `B:as1000_autopilot_altitude_pfd` | SDK-APE; IE 13 |
| VS | press does nothing | `K:AP_PANEL_VS_HOLD`, then `B:as1000_autopilot_verticalspeed_pfd` | SDK-APE, SDK-APT; IE 33 |
| FLC | the speed target stays at an old value | a Lua script (FLC on, then `K:AP_SPD_VAR_SET` to the current IAS), or `B:as1000_autopilot_flightlevelchange_pfd`; either needs a coordinator ruling (A-9, A-12) | SDK-APE, SDK-APT; IE 23 |
| VNV | the press does nothing | an L-Var write toggling `L:XMLVAR_VNAVButtonValue` (what the cockpit code does); needs a ruling and a `check.py` change under a TOOLS LOCK (A-6, A-11); else VNV becomes Empty | SDK-APT |
| VNV | the press works but the key never lights | read the B-Var `B:as1000_autopilot_vertical_navigation_pfd` itself (README: only some B-Vars have a value), else no state (Simple Button) | README 2.1.1; IE 29 |
| VNV | only every second press works (the input event keeps the 1 of the first press, so the next press writes 0) | the Reset Switch: "UseLvarReset": true in the key's set (PilotsDeck writes On 1, then Off 0 100 ms later; settings panel "Reset Switch to Off Position after pressed") | README 2.1.2; Plugin/PI/pi-SwitchDisplay.html |
| HDG BUG readout | differs from the PFD's HDG box | add the index: `(A:AUTOPILOT HEADING LOCK DIR:1, Degrees)` | SDK-APV (slots) |
| HDG BUG press | the bug does not move | `K:AP_HDG_CURRENT_HDG_SET:1`, then `B:as1000_heading_sync_pfd` | SDK-APE; IE 82 |
| HDG+/- | the bug does not move | `B:as1000_heading_pfd` (value unknown) | IE 80 |
| CRS+/- | the course does not move | `K:VOR1_OBI_INC` / `K:VOR1_OBI_DEC` | SDK-RADE |
| CRS1 press | the CDI does not centre | `B:as1000_course_push_pfd` (value unknown) | IE 64 |
| ALT SEL readout | differs from the PFD | `(A:AUTOPILOT ALTITUDE LOCK VAR:1, Feet)` | SDK-APV (slots) |
| ALT+/- long press | **sets the selected altitude to 1000 ft** instead of stepping (A-4) | first set the selected altitude back with the short presses; then the long press becomes the README sequence form, ten single steps (`K:AP_ALT_VAR_INC:0:AP_ALT_VAR_INC:0:...`, ten times; "each K-Var in the Sequence needs exact one Parameter"), or the long press is dropped | README 2.1.1; SDK-APE |
| ALT+/- short press | steps 1000 ft instead of 100 | give the short press the parameter: `K:AP_ALT_VAR_INC:100` / `K:AP_ALT_VAR_DEC:100` (as Jiblet passes 100) | SDK-APE; lead: JIBLET |
| VS+/- | the target does not move | `B:as1000_autopilot_verticalspeed_up_pfd` / `..._down_pfd` (value unknown) | IE 35, 31 |

## Open points (ASSUMPTIONS ruled in LR418-C9; each is checked by the hand test)

- **A-4** ALT long press `:1000`: step or set? See "Fallbacks". Holds only with its hand test. Leads for the
  step reading (not proof for the 2024 C172): the MSFS avionics framework's AltitudeSelectManager treats an
  `AP_ALT_VAR_INC/DEC` value above its `inputIncrLargeThreshold` as a large increment (msfs-avionics-mirror,
  `src/sdk/autopilot/managers/AltitudeSelectManager.ts`), and Jiblet's ALT dial passes 1000 as well as 100.
- **A-5** No index on `AUTOPILOT HEADING LOCK DIR` / `AUTOPILOT ALTITUDE LOCK VAR` (the SDK lists the index
  as N/A); HDG sync with no parameter (slot 0). The same manager writes `AUTOPILOT ALTITUDE LOCK VAR:1` (slot
  1 by default), so `:1` is a likely repair for ALT SEL.
- **A-6** VNV: B-Var write, L-Var read. Weak source: the L-Var comes from a general-path SDK template page
  (not a `/msfs2024/` page) and a pre-2024 profile; no 2024 source confirms it. Stays Unverified.
- **A-8** NAV/APR lit only from the HOLD SimVars (armed may not light).
- **A-9** FLC does not set the speed target to the current IAS.
- **A-10** Readouts show the selected value always; VS with no `+`.
- The steps of HDG, CRS, ALT (short press), VS and SPD are the sim's; the checklist records each.

## How to test

Run [tests/manual-checklist.md](../tests/manual-checklist.md), section "P3-1: Autopilot page (C172 G1000)".
As on the other pages, check the reverse direction too: **work each mode button and knob in the cockpit
with the mouse and check that the keys and readouts follow without a key being pressed.** For VNV and the
readouts, `tools/scmon` (Admin account, read only; [tools/scmon/README.md](../tools/scmon/README.md)) shows
what the sim really has.

## When it passes

1. Any change found in the test goes into `tools/profilegen/c172-g1000.json` and this doc; then the profile
   is regenerated (not exported from the app) and imported again.
2. Fill in the "Verified" column of the autopilot rows in aircraft-mappings.md with the date and sim
   version, for each function that passed.

## Sources

| Tag | Source |
|---|---|
| SDK-APE | MSFS 2024 SDK, autopilot key events: https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-autopilot-and-flight-assistance-events/ (`AP_MASTER` "Toggles AP on/off", `TOGGLE_FLIGHT_DIRECTOR`, `AP_HDG_HOLD`, `AP_NAV1_HOLD`, `AP_APR_HOLD`, `AP_BC_HOLD`, `AP_ALT_HOLD`, `AP_PANEL_ALTITUDE_HOLD`, `AP_VS_HOLD`, `AP_PANEL_HEADING_HOLD`, `AP_PANEL_VS_HOLD`, `FLIGHT_LEVEL_CHANGE`, `HEADING_BUG_INC/DEC`, `AP_ALT_VAR_INC/DEC` "[0]: New reference altitude [1]: Index", `AP_VS_VAR_INC/DEC`, `AP_SPD_VAR_INC/DEC`, `AP_HDG_CURRENT_HDG_SET` "[0]: slot index"; no VNAV event), read 2026-11-14 |
| SDK-APV | MSFS 2024 SDK, autopilot SimVars: https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-autopilot-and-assistant-variables/ (the Bool mode SimVars above; `AUTOPILOT HEADING LOCK DIR` Degrees, `AUTOPILOT ALTITUDE LOCK VAR` Feet, `AUTOPILOT VERTICAL HOLD VAR` Feet/minute, `AUTOPILOT AIRSPEED HOLD VAR` Knots, index N/A; slots "slot 0 overwrites all others"; no VNAV SimVar), read 2026-11-14 |
| SDK-RADV | MSFS 2024 SDK, radio navigation SimVars: https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-radio-navigation-variables/ (`NAV OBS` "NAV Index (1-4)", Degrees), read 2026-11-14 |
| SDK-RADE | MSFS 2024 SDK, radio navigation events: https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-radio-navigation-events/ (`VOR1_OBI_INC/DEC`; `VOR1_OBI_FAST_INC/DEC` by 10 degrees, stop on 360/0), read 2026-11-14 |
| SDK-AS1000 | SDK template explorer, AS1000 glass cockpit (general `/html/` path, the page P2-4 used): https://docs.flightsimulator.com/html/Content_Configuration/Models/ModelBehaviors/TemplateExplorer/Asobo/GlassCockpit/AS1000.html (CRS knob `AS1000_PFD_CRS_INC/DEC/PUSH`; ALT knob increments 100 and 1000; nose UP = `AP_VS_VAR_INC`; no YD or LVL button) |
| SDK-APT | SDK template explorer, Asobo `Common/Autopilot.html` (general path): https://docs.flightsimulator.com/html/Content_Configuration/Models/ModelBehaviors/TemplateExplorer/Asobo/Common/Autopilot.html (the code each cockpit AP button runs; VNV toggles `L:XMLVAR_VNAVButtonValue`; FLC also sets the speed to IAS) |
| README | PilotsDeck README, https://github.com/Fragtality/PilotsDeck/blob/master/README.md: 2.1 (Second command on a long press, >= 500 ms), 2.1.1 (AVAR, KVAR with parameters and sequences, BVAR, LVAR), 2.2.2 (Format), 2.3 (Dynamic Button On/Off) |
| IE | [reference/InputEvents-C172-G1000.txt](reference/InputEvents-C172-G1000.txt) (233 input events of the 2024 C172 G1000) |
| AM | [aircraft-mappings.md](aircraft-mappings.md): AP master verified 2026-11-11, MSFS 1.9.24.0 |
| LR144-C4 | The user's report that P2-4's PFD/MFD H-events from SDK-AS1000 worked in the 2024 C172 ("Yes, they worked") |
| JIBLET | Jiblet's C172 G1000 profile (PilotsDeck 0.8, pre-2024, in `A:\FS2024 Stuff\PilotsDeck`): AP page reads `XMLVAR_VNAVBUTTONVALUE`, ALT step parameters 100 and 1000. Lead only, nothing copied. |
| FORUM | forums.flightsimulator.com reports that the MSFS 2024 binding "Set AP Current HDG" syncs the heading bug. Lead only. |
