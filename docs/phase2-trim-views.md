# Phase 2: Trim and Views pages, Cessna 172 G1000

**Status: partly tested.** An early import was tried in the sim on 2026-11-11: the view K-events did
nothing (LR95-C2) and are off the page now; the EXTERNAL key's A-Var write passed a hand test (LR101-C2).
Every other new name below is recorded as "Unverified" in [aircraft-mappings.md](aircraft-mappings.md)
until the Phase 2 trim and views checks pass.

Goal: fill the two child pages that the main page's folder keys open, for the default MSFS 2024
**Cessna 172 Skyhawk G1000**: **trim** (main page key 1,7 `TRIM`) and **views** (main page key 1,8
`VIEWS`). The content comes from [navigation.md](navigation.md) ("Pages") and the Phase 2 concept layout
in [original-plan.md](original-plan.md) ("Trim page", "views"). Every indicator reads actual sim state;
a key with nothing to read shows a fixed image and says so.

The pages are part of the generated profile `MSFS2024 C172 G1000` (same file, same name, same import as
the main page: see [phase2-main-page.md](phase2-main-page.md), "Import the profile"). The tables below are
the reference for what each key holds; `tools/profilegen/check.py` compares the profile with the two
"Key table" sections key by key. How the pages connect: [navigation.md](navigation.md).

Positions are **row,column**, 1-based, row 1 at the top. On both pages **1,1 is the back key** (it
returns to the main page), as on every child page. The templates T3 and T5 are the main page's (see
[phase2-main-page.md](phase2-main-page.md), "What each key holds"); T6 (Dynamic Button with an A-Var
command) is new, copied from the user's saved key (see "What each key holds" below).

## Trim page

Trim controls and a trim position readout, for the trim the C172 actually has: **elevator trim only**.
The C172 G1000's input events list an elevator trim wheel, a yoke trim switch and a trim disconnect, and
no rudder or aileron trim (IE 182, 183, 185; nothing else with "trim" in the list), so no rudder or aileron
trim key is on the page. The trim keys send SimConnect events: no keyboard binding, no vJoy, nothing tied to
the connected flight controls.

### Layout: trim

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | | | | | | | |
| **Row 2** | | TRIM UP | | | | | | |
| **Row 3** | | TRIM | TRIM DEG | | | | | |
| **Row 4** | | TRIM DN | | | | | | |

The up key sits above the readout and the down key below it. Column 2, so the back key (1,1) is not
directly above the up key.

## Key table: trim

Action names as in phase2-main-page.md. **Back** = the Stream Deck app's back key (`backtoparent`), added
by the generator on every child page. "Empty" = no action on that key.

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to the main page | none | Back key |
| 1,2 | | Empty | | | | |
| 1,3 | | Empty | | | | |
| 1,4 | | Empty | | | | |
| 1,5 | | Empty | | | | |
| 1,6 | | Empty | | | | |
| 1,7 | | Empty | | | | |
| 1,8 | | Empty | | | | |
| 2,1 | | Empty | | | | |
| 2,2 | `TRIM UP` | Simple Button | T5 | `K:ELEV_TRIM_UP` [SDK-FCE] | none (the readouts 3,2 and 3,3 show the result) | fixed image |
| 2,3 | | Empty | | | | |
| 2,4 | | Empty | | | | |
| 2,5 | | Empty | | | | |
| 2,6 | | Empty | | | | |
| 2,7 | | Empty | | | | |
| 2,8 | | Empty | | | | |
| 3,1 | | Empty | | | | |
| 3,2 | `TRIM` | Display Value | T3 | none | `(A:ELEVATOR TRIM PCT EX2, percent)` [SDK-CTLV, SDK-UNITS] | Format `1.1` |
| 3,3 | `TRIM DEG` | Display Value | T3 | none | `(A:ELEVATOR TRIM POSITION, degrees)` [SDK-CTLV, SDK-UNITS] | Format `1.1` |
| 3,4 | | Empty | | | | |
| 3,5 | | Empty | | | | |
| 3,6 | | Empty | | | | |
| 3,7 | | Empty | | | | |
| 3,8 | | Empty | | | | |
| 4,1 | | Empty | | | | |
| 4,2 | `TRIM DN` | Simple Button | T5 | `K:ELEV_TRIM_DN` [SDK-FCE] | none (the readouts 3,2 and 3,3 show the result) | fixed image |
| 4,3 | | Empty | | | | |
| 4,4 | | Empty | | | | |
| 4,5 | | Empty | | | | |
| 4,6 | | Empty | | | | |
| 4,7 | | Empty | | | | |
| 4,8 | | Empty | | | | |

### What the trim keys do

- **TRIM UP / TRIM DN** send `K:ELEV_TRIM_UP` / `K:ELEV_TRIM_DN`. SDK-FCE: they increment / decrement
  "the elevator trim by 0.0005", and "holding down the key will cause the trim to increment faster over
  time" (the sim's own key repeat; a Stream Deck key sends one event per press). **One press is one small
  step.** How many presses a visible change takes is not known; the checklist records it. Whether "up"
  is nose up is not stated in the SDK: the up key should raise both readouts (SDK-CTLV: for `ELEVATOR TRIM
  PCT EX2`, 1 is the up limit), and the checklist records which way the cockpit trim wheel turns.
- **TRIM** shows the trim position in percent, from -100 (down limit) through 0 (neutral, always 0°) to
  100 (up limit) (SDK-CTLV, `ELEVATOR TRIM PCT EX2`, "asymmetrical +/-Percent Over 100"; read in the unit
  `percent`, SDK-UNITS). Format `1.1` = one decimal, e.g. `-12.5`.
- **TRIM DEG** shows the trim deflection in degrees (SDK-CTLV, `ELEVATOR TRIM POSITION`, "Elevator trim
  deflection", read in `degrees`, SDK-UNITS). It is the cross-check for TRIM: if TRIM shows nothing or
  `0` while TRIM DEG moves, the EX2 SimVar is the problem (see "Fallbacks").
- No hold-to-repeat and no long press: the PilotsDeck README documents no auto-repeat; its **Hold
  Switch** sends the command on key down and a second one on key up (no repeat), and the long press
  (>= 500 ms) sends one Second Command. If one step per press turns out too small, that is recorded and a
  later unit decides (for example the README's K-Var sequence form on a long press); nothing is guessed now.

**Command choice (K-event or input event).** In MSFS 2024 aircraft a cockpit control can drive an input
event and a different SimVar index than the standard K-event (the battery case in aircraft-mappings.md).
For the elevator trim there is the K-event pair above and the input event `B:handling_elevatortrim_wheel`
(IE 182). The keys use the K-events: they are documented with a direction and a step (SDK-FCE), while the
input event's values are not documented anywhere this project has (the PilotsDeck README's B-Var form
`B:name:value` needs a value, and the value for one wheel step is unknown). Trim has no index (one
elevator trim), so the battery's index problem can't occur in the same way. **If the choice is wrong**,
the checklist shows it like this: the readouts move when you press the keys, but the cockpit trim wheel
doesn't turn (or turns back), or the wheel moved with the mouse doesn't move the readouts. Then record it;
the input event is the fallback to investigate with `tools/scmon` (the user and a session in Admin).

**Not on this page, and why** (all positions not in the table are Empty):

| Function | Why not | Source |
|---|---|---|
| Rudder trim, aileron trim | The C172 G1000 lists no rudder or aileron trim control (only elevator trim input events). The K-events exist (`K:RUDDER_TRIM_LEFT`/`RIGHT`, `K:AILERON_TRIM_LEFT`/`RIGHT`) but there is no cockpit control to follow. | IE (no such entry); SDK-FCE |
| Yoke trim switch (electric trim) | Input event `B:handling_elevatortrim_yoke` exists; its values are unknown. | IE 183 |
| Trim disconnect | Input event `B:handling_trim_disconnect` exists; its values are unknown. | IE 185 |
| Takeoff trim (set to a fixed position) | `K:ELEVATOR_TRIM_SET` (-16383 to 16384) exists, but no source gives the C172's takeoff trim value. | SDK-FCE |

## Views page

Camera views through SimConnect only: **no keyboard bindings, no vJoy, nothing tied to a controller or
a controller profile.** (The installed MSFS-Fenix320-XL profile's view page uses vJoy for all 12 of its
view keys; this page doesn't.) The aircraft lists no camera input events.

**The view K-events don't work in MSFS 2024.** The first build had 20 view keys, each sending a K-event
from the SDK's "View And Camera Events" page (SDK-VCE). In the sim test of 2026-11-11 (LR95-C2) the plugin
sent every press (plugin log, no error) and the camera did not change. So those keys are Empty now, and
the events are listed under "Not on this page".

**COCKPIT and EXTERNAL write the camera SimVar instead.** They write `CAMERA STATE`, which the MSFS 2024
SDK marks settable (SDK-CAMV), as an A-Var command: PilotsDeck command type 12, "A-Var" (README 2.1.1
lists AVAR as a command type, "make sure the A-Var is writeable"; PD-SRC `SimCommand.cs`: AVAR = 12; the
installed plugin's settings panel accepts type 12, PD-PI). The rule for this page (LR99-C2): an A-Var write
to a SimVar the MSFS 2024 SDK marks settable is allowed here; it needs no controller and has a named
source. The key settings are a copy of the user's own saved EXTERNAL key (T6), which passed a hand test in
the sim on 2026-11-11 (LR101-C2: the plugin wrote 3, 2, 3 and the camera state followed).

**Indicator.** The MSFS 2024 SDK documents readable camera SimVars (SDK-CAMV): `CAMERA STATE` (2 =
Cockpit, 3 = Chase Plane Drone, ...; in the sim, 2 = cockpit, 3 = external, seen in the sim 2026-11-11
(LR95-C2)) and `CAMERA VIEW TYPE AND INDEX` (index 0 = the view type: 1 = Pilot View, 2 = Instruments,
3 = Quickview, ...; index 1 = the option number within that type). So:
- **COCKPIT** and **EXTERNAL** are Dynamic Buttons that read `CAMERA STATE`: On image when their camera is
  active, Off image when the other one is. For any other camera state (drone, showcase, ...) PilotsDeck
  shows neither image, only the key's background (PilotsDeck `ActionSwitchDisplay.cs`, `Refresh()`: no
  image when the value matches neither On nor Off and Special State is off).
- **CAMERA**, **VIEW** and **VIEW NO** are readouts of those SimVars: they show the camera state whatever
  changed it (the deck or the sim's own controls). Pressing a readout does nothing (the plugin log shows a
  warning).

### Layout: views

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | COCKPIT | EXTERNAL | CAMERA | VIEW | VIEW NO | | |
| **Row 2** | | | | | | | | |
| **Row 3** | | | | | | | | |
| **Row 4** | | | | | | | | |

## Key table: views

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to the main page | none | Back key |
| 1,2 | `COCKPIT` | Dynamic Button | T6 | `(A:CAMERA STATE, Enum)`, On `$=2` / Off `` [SDK-CAMV, README 2.1.1, 2.1.2] | `(A:CAMERA STATE, Enum)` [SDK-CAMV, SDK-UNITS] | On/Off image: On `2`, Off `3` |
| 1,3 | `EXTERNAL` | Dynamic Button | T6 | `(A:CAMERA STATE, Enum)`, On `$2,=3<` / Off `` [SDK-CAMV, README 2.1.1, 2.1.2] | `(A:CAMERA STATE, Enum)` [SDK-CAMV, SDK-UNITS] | On/Off image: On `3`, Off `2` |
| 1,4 | `CAMERA` | Display Value | T3 | none | `(A:CAMERA STATE, Enum)` [SDK-CAMV, SDK-UNITS] | Mappings `2=COCKPIT:3=CHASE:4=FIXED:5=ENV:7=SHOWCASE:8=DRONE` |
| 1,5 | `VIEW` | Display Value | T3 | none | `(A:CAMERA VIEW TYPE AND INDEX:0, Enum)` [SDK-CAMV, SDK-UNITS] | Mappings `0=OTHER:1=PILOT:2=INSTR:3=QUICK:4=QV EXT:5=VIEW` |
| 1,6 | `VIEW NO` | Display Value | T3 | none | `(A:CAMERA VIEW TYPE AND INDEX:1, number)` [SDK-CAMV, SDK-UNITS] | Format `1.0` |
| 1,7 | | Empty | | | | |
| 1,8 | | Empty | | | | |
| 2,1 | | Empty | | | | |
| 2,2 | | Empty | | | | |
| 2,3 | | Empty | | | | |
| 2,4 | | Empty | | | | |
| 2,5 | | Empty | | | | |
| 2,6 | | Empty | | | | |
| 2,7 | | Empty | | | | |
| 2,8 | | Empty | | | | |
| 3,1 | | Empty | | | | |
| 3,2 | | Empty | | | | |
| 3,3 | | Empty | | | | |
| 3,4 | | Empty | | | | |
| 3,5 | | Empty | | | | |
| 3,6 | | Empty | | | | |
| 3,7 | | Empty | | | | |
| 3,8 | | Empty | | | | |
| 4,1 | | Empty | | | | |
| 4,2 | | Empty | | | | |
| 4,3 | | Empty | | | | |
| 4,4 | | Empty | | | | |
| 4,5 | | Empty | | | | |
| 4,6 | | Empty | | | | |
| 4,7 | | Empty | | | | |
| 4,8 | | Empty | | | | |

### What the view keys do

| Key | Command | What it writes (README 2.1.2, Value Manipulations in the On Value) | Tested |
|---|---|---|---|
| COCKPIT | A-Var `(A:CAMERA STATE, Enum)`, On Value `$=2`, Off Value empty | Always writes 2 (cockpit). | Not yet: the Phase 2 checklist tests it. |
| EXTERNAL | A-Var `(A:CAMERA STATE, Enum)`, On Value `$2,=3<`, Off Value empty | Toggles: 2 (cockpit) -> 3 (external), 3 -> 2, any other state -> 3. | Hand test passed 2026-11-11 (LR101-C2): log "Running Command (Type: AVAR ...)" with values 3, 2, 3 and "Received Camera State" 3, 2, 3. |

Both keys read `CAMERA STATE` for their image, so the image shows whether a press really changed the camera.
Values other than 2 and 3 (4 Fixed On Plane, 5 Environment, 7 Showcase, 8 Drone Plane, SDK-CAMV) are not
written by any key: untested.

**Readouts.** `CAMERA` maps these camera states from SDK-CAMV: 2 Cockpit, 3 Chase Plane Drone, 4 Fixed
On Plane, 5 Environment 6DOF, 7 Showcase, 8 Drone Plane. Any other state shows as its number (SDK-CAMV
lists 1 to 33; some "belong to legacy systems"). SDK-CAMV is not consistent about 3: its state table says
"Chase Plane Drone", its `CHASE CAMERA HEADLOOK` entry calls state 3 the external/chase camera. Settled
in the sim: 2 = cockpit, 3 = external, seen in the sim 2026-11-11 (LR95-C2); `CAMERA` keeps the label
`CHASE` for 3. `VIEW` maps the view types of
`CAMERA VIEW TYPE AND INDEX:0` (0 "Unknown / default", 1 "Pilot View", 2 "Instruments", 3 "Quickview",
4 "Quickview External", 5 "View"). `VIEW NO` shows `CAMERA VIEW TYPE AND INDEX:1`, the option within the
type; SDK-CAMV says the Pilot View options are 1, 2, 4 and 5 (Close, Pilot, Landing, Copilot) by default.

**Not on this page, and why:**

| Function | Why not | Source |
|---|---|---|
| The view K-events of the first build: `K:VIEW_VIRTUAL_COCKPIT_FORWARD` (was COCKPIT), `K:CHASE_VIEW_TOGGLE` (was EXTERNAL), `K:PREV_SUB_VIEW`, `K:NEXT_SUB_VIEW`, `K:VIEW_RESET` | Sent by the plugin, ignored by MSFS 2024 (sim test 2026-11-11, LR95-C2). | SDK-VCE; LR95-C2 |
| `K:VIEW_MODE`, `K:VIEW_MODE_REV` (categories), `K:ZOOM_MINUS`, `K:ZOOM_PLUS`, `K:VIEW_PREVIOUS_TOGGLE` (last view), `K:VIEW_CAMERA_SELECT_0`, `K:VIEW_CAMERA_SELECT_1`, `K:VIEW_CAMERA_SELECT_2`, `K:VIEW_CAMERA_SELECT_3`, `K:VIEW_CAMERA_SELECT_4`, `K:VIEW_CAMERA_SELECT_5`, `K:VIEW_CAMERA_SELECT_6`, `K:VIEW_CAMERA_SELECT_7`, `K:VIEW_CAMERA_SELECT_8`, `K:VIEW_CAMERA_SELECT_9` (custom cameras); `K:VIEW_COCKPIT_FORWARD` (was COCKPIT's fallback) | Not tested, left out with the K-event view family (LR95-C2). | SDK-VCE; LR95-C2 |
| Pilot view options (Close, Pilot, Landing, Copilot), instrument views by number | No K-event selects them. The SDK documents writing `CAMERA VIEW TYPE AND INDEX` (settable) for this; an A-Var write is allowed on this page (LR99-C2) but this one is not built or tested: a later unit. | SDK-CAMV |
| Drone, showcase, fixed cameras directly | Only by writing other `CAMERA STATE` values (settable; untested): a later unit. | SDK-CAMV |
| Look left / right / rear (`K:VIEW_LEFT`, `K:VIEW_RIGHT`, `K:VIEW_REAR`, ...) | Listed and not marked obsolete ("Sets view direction to the left." etc.). Never on the page and not tested; they are K-events of the view family that MSFS 2024 ignored (LR95-C2). | SDK-VCE |
| `K:CHASE_VIEW`, `K:CHASE_VIEW_NEXT`, `K:CHASE_VIEW_PREV`, `K:VIEW_TYPE`, `K:VIEW_TYPE_REV`, `K:TOGGLE_PADLOCK` | Marked "Deprecated, do not use". | SDK-VCE |

## Sources

| Tag | Source |
|---|---|
| README | PilotsDeck README, https://github.com/Fragtality/PilotsDeck/blob/master/README.md (2.1.1 address syntax, and AVAR as a command type; 2.1.2 command options: Hold Switch, Long Press; Value Manipulations such as `$=2` and `$2,=3<`) |
| SDK-FCE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-flight-control-events/ (Elevator trim events) |
| SDK-CTLV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-control-variables/ (Elevator: trim SimVars) |
| SDK-UNITS | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/simulation-variable-units/ (`percent`, `degrees`, `Enum`, `number`) |
| SDK-VCE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/view-and-camera-events/ |
| SDK-CAMV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/camera-variables/ |
| IE n | [reference/InputEvents-C172-G1000.txt](reference/InputEvents-C172-G1000.txt), line n (identical to the plugin's live `InputEvents.txt` on 2026-11-11) |
| PD-SRC | PilotsDeck source, https://github.com/Fragtality/PilotsDeck/blob/11bdf1f7daf4828f822c18919952fe5b66153e58/Plugin/Actions/Simple/ActionSwitchDisplay.cs (which image a Dynamic Button shows); `Plugin/Simulator/SimCommand.cs` in the same commit (command type AVAR = 12) |
| PD-PI | The installed plugin's settings panel, `%APPDATA%\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\Plugin\PI\js\pi-Common.js` line 221 (command type 12, "Avar") |
| LR95-C2, LR101-C2 | Sim test rows in the project's chain ledger (2026-11-11): the view K-events did nothing; the EXTERNAL A-Var key worked |

Address syntax is the README's section 2.1.1 (A: SimVars with index and unit in brackets, K: events; an
A: SimVar can also be a command, AVAR, which writes it).

## What each key holds

Every key is a copy of a template with only these fields changed (the generator does this; by hand only
when you change a key during a test, see phase2-main-page.md "Changing a key by hand").

**T5 Simple Button** (as ATC on the main page): Commands tab Command Type MSFS: K-Var (SimEvent), Command
Address as in the Key table, On/Off Value empty, Toggle Switch unchecked; background `Images/Switch.png`;
Title as in the table. Trim: 2,2, 4,2.

**T3 Display Value** (as RPM on the main page): Value tab Address, Format and Mappings as in the Key table
(empty where the table names none), Decode BCD unchecked, no command. Trim: 3,2, 3,3. Views: 1,4, 1,5, 1,6.

**T6 Dynamic Button with an A-Var command** (new; template `avar_dynamic_button` in
`tools/profilegen/templates.json`): a verbatim copy of the user's own saved EXTERNAL key, set by hand in
the Stream Deck app and sim-tested (LR101-C2). Source, read only: the imported profile the app named
`MSFS2024 C172 G1000 copy`,
`%APPDATA%\Elgato\StreamDeck\ProfilesV3\5CFD6707-1DA1-41C0-9FE9-3B84184E1367.sdProfile\Profiles\1FA3B762-6445-4CBC-953D-326F021FFAF4\manifest.json`
(sha256 c8174d8e... when copied), action `2,0`. Commands tab Command Type A-Var (12), On Value as below, Off
Value empty, Toggle Switch unchecked; On/Off images `Images/KorryOnBlueTop.png` /
`Images/KorryOffWhiteBottom.png`.

| Pos | Commands: Command Address | Commands: On Value / Off Value | Value: Address | On/Off States: On Value / Off Value | Title |
|---|---|---|---|---|---|
| views 1,2 | `(A:CAMERA STATE, Enum)` | `$=2` / empty | `(A:CAMERA STATE, Enum)` | `2` / `3` | `COCKPIT` |
| views 1,3 | `(A:CAMERA STATE, Enum)` | `$2,=3<` / empty | `(A:CAMERA STATE, Enum)` | `3` / `2` | `EXTERNAL` |

EXTERNAL equals the saved key in every field (the generator gives it a new ActionID). COCKPIT differs from it
only in the On Value and the On/Off States values. The settings panel saves a text field only when focus
leaves it: after a hand change, Tab out of the field.

## Fallbacks

Use one only if the checklist shows the main address doesn't work, and say which one you used. None is
tested; they are recorded in aircraft-mappings.md too.

| Key | Fallback | Source |
|---|---|---|
| trim 3,2 TRIM | `(A:ELEVATOR TRIM PCT, percent)` (marked legacy in the SDK; 0 to 100 or -100 to 100 is not stated) | SDK-CTLV, SDK-UNITS |
| trim 2,2 / 4,2 | Input event `B:handling_elevatortrim_wheel`: values unknown, needs a `tools/scmon` session first | IE 182 |
| views 1,2 COCKPIT | If `$=2` does nothing: EXTERNAL (`$2,=3<`, hand-tested) also goes back to the cockpit from the external view; COCKPIT then becomes Empty. No K-event fallback: the view K-events are ignored (LR95-C2). | README 2.1.2; LR101-C2 |
| views 1,3 EXTERNAL | none needed (hand test passed, LR101-C2) | LR101-C2 |
| views 1,2 / 1,3 values | 2 = cockpit, 3 = external, seen in the sim 2026-11-11 (LR95-C2). If CAMERA shows other numbers in a later sim version, the On Value and On/Off values change to them | SDK-CAMV; LR95-C2 |

## How to test

Run [tests/manual-checklist.md](../tests/manual-checklist.md), section "Phase 2: Trim and Views pages
(C172 G1000)", after the main page's import step. As on the main page, the important direction is the
reverse one: **move the trim wheel or change the view with the mouse or keyboard, and check that the
readouts and the COCKPIT/EXTERNAL keys follow without being pressed.**

## When it passes

1. Any change found in the test goes into `tools/profilegen/c172-g1000.json` and this doc; then the profile
   is regenerated (not exported from the app) and imported again.
2. Fill in the "Verified" column of the trim and views rows in aircraft-mappings.md with the date and sim
   version, for each key that passed. Mark a view key "does not work" if it did nothing; it becomes Empty.
