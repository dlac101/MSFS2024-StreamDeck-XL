# Phase 2: G1000 bezel and V-speeds pages, Cessna 172 G1000

**Status: untested.** Nothing on these pages has been tried in the sim yet. Every new name below is
recorded as "Unverified" in [aircraft-mappings.md](aircraft-mappings.md) until the Phase 2 G1000 and
V-speeds checks pass.

Goal: three pages under the main page's **MORE** folder (key 4,8) for the default MSFS 2024 **Cessna 172
Skyhawk G1000**: the **PFD** bezel keys, the **MFD** bezel keys and a **V-speeds** display. They are the
first second-level pages of the profile (main > MORE > page, [navigation.md](navigation.md) "Rules": at
most two levels). The MORE page itself now holds three folder keys that open them.

The pages are part of the generated profile `MSFS2024 C172 G1000` (same file, same name, same import as
the main page: see [phase2-main-page.md](phase2-main-page.md), "Import the profile"). The tables below are
the reference for what each key holds; `tools/profilegen/check.py` compares the profile with the four
"Key table" sections key by key.

Positions are **row,column**, 1-based, row 1 at the top. On every page **1,1 is the back key**: on MORE it
returns to the main page, on PFD, MFD and V-SPEEDS it returns to MORE. Template T3 is the main page's (see
[phase2-main-page.md](phase2-main-page.md), "What each key holds"); T7 (Simple Button with an H-event
command) is new here (see "What each key holds" below).

Nothing on these pages uses keyboard bindings, vJoy or anything tied to a controller: the bezel keys send
H-events through PilotsDeck and the MobiFlight WASM module (PD-SRC), the readouts read SimVars. They work the same
with the Xbox Elite controller and the T.16000M + TWCS.

## MORE page

A menu of further pages. Five folder keys now (the fourth, `COM PAD` at 1,5, opens the COM1 number pad:
[phase2-com1-pad.md](phase2-com1-pad.md); the fifth, `AUTOPILOT` at 1,6, opens the autopilot page:
[phase3-autopilot.md](phase3-autopilot.md)); the other positions stay free for later folders (radios:
[navigation.md](navigation.md), "Pages").

### Layout: more

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | PFD > | MFD > | V-SPEEDS > | COM PAD > | AUTOPILOT > | | |
| **Row 2** | | | | | | | | |
| **Row 3** | | | | | | | | |
| **Row 4** | | | | | | | | |

## Key table: more

**Back** = the Stream Deck app's back key (`backtoparent`), added by the generator on every child page.
**Folder** = the Stream Deck app's folder action ("Create Folder"), as on the main page. "Empty" = no
action on that key.

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to the main page | none | Back key |
| 1,2 | `PFD` | Folder | (Stream Deck) | Opens the child page **pfd** | none | Folder; the page's keys: "Key table: pfd" below |
| 1,3 | `MFD` | Folder | (Stream Deck) | Opens the child page **mfd** | none | Folder; the page's keys: "Key table: mfd" below |
| 1,4 | `V-SPEEDS` | Folder | (Stream Deck) | Opens the child page **vspeeds** | none | Folder; the page's keys: "Key table: vspeeds" below |
| 1,5 | `COM PAD` | Folder | (Stream Deck) | Opens the child page **compad** | none | Folder; the page's keys: "Key table: compad" in [phase2-com1-pad.md](phase2-com1-pad.md) |
| 1,6 | `AUTOPILOT` | Folder | (Stream Deck) | Opens the child page **autopilot** | none | Folder; the page's keys: "Key table: autopilot" in [phase3-autopilot.md](phase3-autopilot.md) |
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

The PFD, MFD and V-SPEEDS pages are second-level pages: they hold no folder keys (no third level).

## PFD and MFD pages (G1000 bezel)

One page per display, with the same layout: the PFD page sends the PFD's events, the MFD page the MFD's.
The keys are the G1000 bezel buttons and knobs that the 2024 C172 G1000 lists as cockpit controls (its
input events, IE 39 to 137): the 12 softkeys, MENU, PROC, ENT, CLR, FPL, Direct-To, the FMS knob (inner
and outer ring, inner push) and the range knob (turn and push).

### Layout: pfd and mfd

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | DIRECT | MENU | FPL | PROC | CLR | CLR HOLD | ENT |
| **Row 2** | FMS PUSH | FMS OUT- | FMS OUT+ | FMS IN- | FMS IN+ | RANGE- | RANGE+ | RNG PUSH |
| **Row 3** | SK 1 | SK 2 | SK 3 | SK 4 | SK 5 | SK 6 | | |
| **Row 4** | SK 7 | SK 8 | SK 9 | SK 10 | SK 11 | SK 12 | | |

Rows 3 and 4 hold the softkeys left to right in two halves (SK 1 to SK 6 above SK 7 to SK 12), so the
softkey numbers read like the bezel's row. Row 1 holds the buttons of the bezel's right side, row 2 the
two knobs.

**How the keys send (command route).** Every bezel key is a Simple Button that sends one **H-event**, the
event name the G1000's own cockpit buttons fire, PilotsDeck command type **HVAR** (8):
- **Names:** the SDK's AS1000 template (SDK-AS1000) builds the bezel events as `H:<prefix>_<function>`
  with the prefix `AS1000_PFD` on the PFD and `AS1000_MFD` on the MFD: `_SOFTKEYS_1` to `_SOFTKEYS_12`,
  `_DIRECTTO`, `_ENT_Push`, `_CLR` (and `_CLR_Long` for a long press), `_MENU_Push`, `_FPL_Push`,
  `_PROC_Push`, `_FMS_Upper_INC` / `_DEC` / `_PUSH` (inner knob), `_FMS_Lower_INC` / `_DEC` (outer
  knob, no push), `_RANGE_INC` / `_DEC` and the range joystick's `_JOYSTICK_PUSH`. That page is in the
  SDK documentation's general section (no MSFS 2024 copy of it was found). For MSFS 2024: the SDK's RPN
  page says every MSFS 2024 cockpit panel "sends a number of cockpit specific `H:` events" (SDK-RPN), and
  the aircraft is the AS1000 one (the plugin log names its package `fs24-asobo-aircraft-c172sp-as1000`;
  its input events are the `as1000_*` list, IE). Whether the 2024 G1000 still reacts to these names is
  what the sim test shows.
- **Key type (sources):** command type 8 is HVAR in the installed 0.9.7 settings panel (PD-PI:
  `Plugin/PI/js/pi-Common.js` line 215, `type == 8 //HVar`) and in the PilotsDeck source (PD-SRC:
  `Plugin/Simulator/SimCommand.cs`, `HVAR = 8`). T7 is the main page's T5 Simple Button (template
  `simple_button`, a real key saved by PilotsDeck 0.9.7, BUILD_VERSION 11, in the user's MSFS-Fenix320-XL
  profile) with only the command type and address changed. No type-8 key saved by PilotsDeck 0.9.x exists
  on this PC; the coordinator's ruling LR144-C4 (route C) accepts these sources in its place. The plugin log
  showed the generated keys sent as HVAR and the user reported they worked (LR143-C4, LR144-C4).
- **Address form (EX-G1000):** the user's installed profile `G1000` (ProfilesV3) holds six keys of the
  Generic package (TorontoWill v1.3, zip dated 2025-01-26, profile format 2.0), saved with a pre-0.8.9
  PilotsDeck (BUILD_VERSION 7, no Plugin block) and imported 2026-11-11 02:35, when the Stream Deck app
  wrote the 0.9.7.0 Plugin block. They send `H:AS1000_MFD_DIRECTTO`, `H:AS1000_MFD_MENU_Push`,
  `H:AS1000_MFD_FPL_Push`, `H:AS1000_MFD_PROC_Push`, `H:AS1000_MFD_CLR` and `H:AS1000_MFD_ENT_Push`:
  command type 8, DoNotRequestBvar true as saved (the B-Var "Run as Command" box; no effect on an H-Var),
  no box, background `Images/Switch.png` (five of them; the Direct-To one has `Images/A-GearLocked.png`).
  They show the address form only and were never pressed on this PC.
- **Address syntax:** README 2.1.1, HVAR: the H-Var name "with or without preceding `H:`", command only
  ("they trigger an Event but can't be read"). The plugin sends H-events through the MobiFlight WASM
  module (PD-SRC: `ConnectorMSFS.cs`, `ToolsMSFS.cs`; README 1.4 says only that the installer installs it); the plugin log of 2026-11-11 shows the module connected
  ("MobiFlight WASM Client Connection opened").
- **Why not the input events or the G1000 K-events:** see "Command choice" below.

**Indicators: none.** No key on these pages shows sim state, because there is none to read: H-events
"can't be read" (README 2.1.1), the softkey labels change with the G1000 page and no SimVar in the MSFS
2024 SDK gives them, and the bezel buttons have no on/off state. So every bezel key is a Simple Button
with a fixed image and a neutral title (`SK 1`, `MENU`, ...). What a press did shows on the G1000 itself.

## Key table: pfd

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to the MORE page | none | Back key |
| 1,2 | `DIRECT` | Simple Button | T7 | `H:AS1000_PFD_DIRECTTO` [SDK-AS1000, EX-G1000, IE 66] | none (H-events can't be read) | fixed image |
| 1,3 | `MENU` | Simple Button | T7 | `H:AS1000_PFD_MENU_Push` [SDK-AS1000, EX-G1000, IE 89] | none (H-events can't be read) | fixed image |
| 1,4 | `FPL` | Simple Button | T7 | `H:AS1000_PFD_FPL_Push` [SDK-AS1000, EX-G1000, IE 78] | none (H-events can't be read) | fixed image |
| 1,5 | `PROC` | Simple Button | T7 | `H:AS1000_PFD_PROC_Push` [SDK-AS1000, EX-G1000, IE 107] | none (H-events can't be read) | fixed image |
| 1,6 | `CLR` | Simple Button | T7 | `H:AS1000_PFD_CLR` [SDK-AS1000, EX-G1000, IE 40] | none (H-events can't be read) | fixed image |
| 1,7 | `CLR HOLD` | Simple Button | T7 | `H:AS1000_PFD_CLR_Long` [SDK-AS1000, IE 40] | none (H-events can't be read) | fixed image |
| 1,8 | `ENT` | Simple Button | T7 | `H:AS1000_PFD_ENT_Push` [SDK-AS1000, EX-G1000, IE 70] | none (H-events can't be read) | fixed image |
| 2,1 | `FMS PUSH` | Simple Button | T7 | `H:AS1000_PFD_FMS_Upper_PUSH` [SDK-AS1000, IE 76] | none (H-events can't be read) | fixed image |
| 2,2 | `FMS OUT-` | Simple Button | T7 | `H:AS1000_PFD_FMS_Lower_DEC` [SDK-AS1000, IE 72] | none (H-events can't be read) | fixed image |
| 2,3 | `FMS OUT+` | Simple Button | T7 | `H:AS1000_PFD_FMS_Lower_INC` [SDK-AS1000, IE 72] | none (H-events can't be read) | fixed image |
| 2,4 | `FMS IN-` | Simple Button | T7 | `H:AS1000_PFD_FMS_Upper_DEC` [SDK-AS1000, IE 74] | none (H-events can't be read) | fixed image |
| 2,5 | `FMS IN+` | Simple Button | T7 | `H:AS1000_PFD_FMS_Upper_INC` [SDK-AS1000, IE 74] | none (H-events can't be read) | fixed image |
| 2,6 | `RANGE-` | Simple Button | T7 | `H:AS1000_PFD_RANGE_DEC` [SDK-AS1000, IE 113 likely, IE 109 the other candidate] | none (H-events can't be read) | fixed image |
| 2,7 | `RANGE+` | Simple Button | T7 | `H:AS1000_PFD_RANGE_INC` [SDK-AS1000, IE 113 likely, IE 109 the other candidate] | none (H-events can't be read) | fixed image |
| 2,8 | `RNG PUSH` | Simple Button | T7 | `H:AS1000_PFD_JOYSTICK_PUSH` [SDK-AS1000, IE 111] | none (H-events can't be read) | fixed image |
| 3,1 | `SK 1` | Simple Button | T7 | `H:AS1000_PFD_SOFTKEYS_1` [SDK-AS1000, IE 115] | none (labels change with the page; no SimVar) | fixed image |
| 3,2 | `SK 2` | Simple Button | T7 | `H:AS1000_PFD_SOFTKEYS_2` [SDK-AS1000, IE 123] | none (labels change with the page; no SimVar) | fixed image |
| 3,3 | `SK 3` | Simple Button | T7 | `H:AS1000_PFD_SOFTKEYS_3` [SDK-AS1000, IE 125] | none (labels change with the page; no SimVar) | fixed image |
| 3,4 | `SK 4` | Simple Button | T7 | `H:AS1000_PFD_SOFTKEYS_4` [SDK-AS1000, IE 127] | none (labels change with the page; no SimVar) | fixed image |
| 3,5 | `SK 5` | Simple Button | T7 | `H:AS1000_PFD_SOFTKEYS_5` [SDK-AS1000, IE 129] | none (labels change with the page; no SimVar) | fixed image |
| 3,6 | `SK 6` | Simple Button | T7 | `H:AS1000_PFD_SOFTKEYS_6` [SDK-AS1000, IE 131] | none (labels change with the page; no SimVar) | fixed image |
| 3,7 | | Empty | | | | |
| 3,8 | | Empty | | | | |
| 4,1 | `SK 7` | Simple Button | T7 | `H:AS1000_PFD_SOFTKEYS_7` [SDK-AS1000, IE 133] | none (labels change with the page; no SimVar) | fixed image |
| 4,2 | `SK 8` | Simple Button | T7 | `H:AS1000_PFD_SOFTKEYS_8` [SDK-AS1000, IE 135] | none (labels change with the page; no SimVar) | fixed image |
| 4,3 | `SK 9` | Simple Button | T7 | `H:AS1000_PFD_SOFTKEYS_9` [SDK-AS1000, IE 137] | none (labels change with the page; no SimVar) | fixed image |
| 4,4 | `SK 10` | Simple Button | T7 | `H:AS1000_PFD_SOFTKEYS_10` [SDK-AS1000, IE 117] | none (labels change with the page; no SimVar) | fixed image |
| 4,5 | `SK 11` | Simple Button | T7 | `H:AS1000_PFD_SOFTKEYS_11` [SDK-AS1000, IE 119] | none (labels change with the page; no SimVar) | fixed image |
| 4,6 | `SK 12` | Simple Button | T7 | `H:AS1000_PFD_SOFTKEYS_12` [SDK-AS1000, IE 121] | none (labels change with the page; no SimVar) | fixed image |
| 4,7 | | Empty | | | | |
| 4,8 | | Empty | | | | |

## Key table: mfd

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to the MORE page | none | Back key |
| 1,2 | `DIRECT` | Simple Button | T7 | `H:AS1000_MFD_DIRECTTO` [SDK-AS1000, EX-G1000, IE 65] | none (H-events can't be read) | fixed image |
| 1,3 | `MENU` | Simple Button | T7 | `H:AS1000_MFD_MENU_Push` [SDK-AS1000, EX-G1000, IE 88] | none (H-events can't be read) | fixed image |
| 1,4 | `FPL` | Simple Button | T7 | `H:AS1000_MFD_FPL_Push` [SDK-AS1000, EX-G1000, IE 77] | none (H-events can't be read) | fixed image |
| 1,5 | `PROC` | Simple Button | T7 | `H:AS1000_MFD_PROC_Push` [SDK-AS1000, EX-G1000, IE 106] | none (H-events can't be read) | fixed image |
| 1,6 | `CLR` | Simple Button | T7 | `H:AS1000_MFD_CLR` [SDK-AS1000, EX-G1000, IE 39] | none (H-events can't be read) | fixed image |
| 1,7 | `CLR HOLD` | Simple Button | T7 | `H:AS1000_MFD_CLR_Long` [SDK-AS1000, IE 39] | none (H-events can't be read) | fixed image |
| 1,8 | `ENT` | Simple Button | T7 | `H:AS1000_MFD_ENT_Push` [SDK-AS1000, EX-G1000, IE 69] | none (H-events can't be read) | fixed image |
| 2,1 | `FMS PUSH` | Simple Button | T7 | `H:AS1000_MFD_FMS_Upper_PUSH` [SDK-AS1000, IE 75] | none (H-events can't be read) | fixed image |
| 2,2 | `FMS OUT-` | Simple Button | T7 | `H:AS1000_MFD_FMS_Lower_DEC` [SDK-AS1000, IE 71] | none (H-events can't be read) | fixed image |
| 2,3 | `FMS OUT+` | Simple Button | T7 | `H:AS1000_MFD_FMS_Lower_INC` [SDK-AS1000, IE 71] | none (H-events can't be read) | fixed image |
| 2,4 | `FMS IN-` | Simple Button | T7 | `H:AS1000_MFD_FMS_Upper_DEC` [SDK-AS1000, IE 73] | none (H-events can't be read) | fixed image |
| 2,5 | `FMS IN+` | Simple Button | T7 | `H:AS1000_MFD_FMS_Upper_INC` [SDK-AS1000, IE 73] | none (H-events can't be read) | fixed image |
| 2,6 | `RANGE-` | Simple Button | T7 | `H:AS1000_MFD_RANGE_DEC` [SDK-AS1000, IE 112 likely, IE 108 the other candidate] | none (H-events can't be read) | fixed image |
| 2,7 | `RANGE+` | Simple Button | T7 | `H:AS1000_MFD_RANGE_INC` [SDK-AS1000, IE 112 likely, IE 108 the other candidate] | none (H-events can't be read) | fixed image |
| 2,8 | `RNG PUSH` | Simple Button | T7 | `H:AS1000_MFD_JOYSTICK_PUSH` [SDK-AS1000, IE 110] | none (H-events can't be read) | fixed image |
| 3,1 | `SK 1` | Simple Button | T7 | `H:AS1000_MFD_SOFTKEYS_1` [SDK-AS1000, IE 114] | none (labels change with the page; no SimVar) | fixed image |
| 3,2 | `SK 2` | Simple Button | T7 | `H:AS1000_MFD_SOFTKEYS_2` [SDK-AS1000, IE 122] | none (labels change with the page; no SimVar) | fixed image |
| 3,3 | `SK 3` | Simple Button | T7 | `H:AS1000_MFD_SOFTKEYS_3` [SDK-AS1000, IE 124] | none (labels change with the page; no SimVar) | fixed image |
| 3,4 | `SK 4` | Simple Button | T7 | `H:AS1000_MFD_SOFTKEYS_4` [SDK-AS1000, IE 126] | none (labels change with the page; no SimVar) | fixed image |
| 3,5 | `SK 5` | Simple Button | T7 | `H:AS1000_MFD_SOFTKEYS_5` [SDK-AS1000, IE 128] | none (labels change with the page; no SimVar) | fixed image |
| 3,6 | `SK 6` | Simple Button | T7 | `H:AS1000_MFD_SOFTKEYS_6` [SDK-AS1000, IE 130] | none (labels change with the page; no SimVar) | fixed image |
| 3,7 | | Empty | | | | |
| 3,8 | | Empty | | | | |
| 4,1 | `SK 7` | Simple Button | T7 | `H:AS1000_MFD_SOFTKEYS_7` [SDK-AS1000, IE 132] | none (labels change with the page; no SimVar) | fixed image |
| 4,2 | `SK 8` | Simple Button | T7 | `H:AS1000_MFD_SOFTKEYS_8` [SDK-AS1000, IE 134] | none (labels change with the page; no SimVar) | fixed image |
| 4,3 | `SK 9` | Simple Button | T7 | `H:AS1000_MFD_SOFTKEYS_9` [SDK-AS1000, IE 136] | none (labels change with the page; no SimVar) | fixed image |
| 4,4 | `SK 10` | Simple Button | T7 | `H:AS1000_MFD_SOFTKEYS_10` [SDK-AS1000, IE 116] | none (labels change with the page; no SimVar) | fixed image |
| 4,5 | `SK 11` | Simple Button | T7 | `H:AS1000_MFD_SOFTKEYS_11` [SDK-AS1000, IE 118] | none (labels change with the page; no SimVar) | fixed image |
| 4,6 | `SK 12` | Simple Button | T7 | `H:AS1000_MFD_SOFTKEYS_12` [SDK-AS1000, IE 120] | none (labels change with the page; no SimVar) | fixed image |
| 4,7 | | Empty | | | | |
| 4,8 | | Empty | | | | |

### What the bezel keys do

- **One press is one event.** A Simple Button sends its command once per press (README 2.1); there is no
  auto-repeat. A knob key is one detent per press (INC = one step clockwise, DEC = one step
  anticlockwise, if the SDK's names mean what they say; the test records the direction).
- **CLR HOLD** sends the long-press event of CLR (SDK-AS1000: `_CLR_Long`, which the cockpit button sends
  after a 2 s hold). It is a separate key, not a long press on CLR, so each key sends exactly one event.
  What the G1000 does with it the test records.
- **RNG PUSH** sends the range joystick's push (`_JOYSTICK_PUSH` in SDK-AS1000), for the cockpit control
  the input events call `as1000_range_push_*` (IE 110, 111). What it does on the G1000 the test records.
- **Softkeys:** `SK n` presses softkey n, counted from the left. Its function is whatever the G1000 shows
  above that softkey at that moment (the label changes with the page): look at the G1000, not the deck.
- **If a key does nothing** (the sim test of each key below): the plugin log shows "Running Command (Type:
  HVAR ...)" for the press. With that line and no reaction on the G1000, the name or the route is wrong
  for MSFS 2024; without it, the press never left the plugin. Either way the key is recorded as "does not
  work" and becomes Empty, or gets the fallback below once a hand test has given it a real example.

**Command choice (H-event, input event or K-event).** For each function there are three candidates:

| Candidate | Example (PFD softkey 1) | Source | Used? |
|---|---|---|---|
| H-event (HVAR, 8) | `H:AS1000_PFD_SOFTKEYS_1` | SDK-AS1000 (names), SDK-RPN (H-events in MSFS 2024 panels), PD-PI and PD-SRC (command type 8), EX-G1000 (the address form, in keys saved with a pre-0.8.9 PilotsDeck), Jiblet (leads, PilotsDeck 0.8) | **Yes**: a named source for every name and for the command type, on a real 0.9.7 key template (LR144-C4). |
| Input event (B-Var, 13) | `B:as1000_softkey_1_pfd` | IE 115 | No: the value that presses a bezel button is documented nowhere this project has (the README 2.1.1 B-Var command form `B:name:value` needs it; IE lists names only). Phase 1 found a B-Var sent with no value did nothing (phase2-main-page.md, "Fallbacks"). It is the fallback, after a hand test (below). |
| K-event (KVAR, 16) | `K:G1000_PFD_SOFTKEY1` | MSFS 2024 SDK key events list (SDK-KE) | No: a Working Title developer wrote that the G1000 key events in the SDK are deprecated (WT-FORUM, a lead only), and P2-3 found the legacy view K-events ignored by MSFS 2024 (LR95-C2). |

In MSFS 2024 aircraft a cockpit control may drive an input event rather than the legacy event (the
battery case in aircraft-mappings.md). An H-event bypasses the input event: it is what the cockpit button
fires itself (SDK-AS1000), so the G1000 should react to it the same way. If it doesn't, the input event
is the fallback.

**Not on these pages, and why:**

| Function | Why not | Source |
|---|---|---|
| Range joystick pan (`_JOYSTICK_UP`, `_DOWN`, `_LEFT`, `_RIGHT`) | Named in SDK-AS1000 (the range knob's pan, `_Range_Pan_X` / `_Y`). The 2024 C172's input event `as1000_range_*` may be that control (the input events list names only; `as1000_range_zoom_*` is likely the range knob, `as1000_range_push_*` its push). Left Empty (3,7, 3,8, 4,7, 4,8) in this unit, until a test or source shows it. | SDK-AS1000; IE 108 to 113 |
| FMS outer knob push | SDK-AS1000 names no push for the outer ring. | SDK-AS1000 |
| COM, NAV, heading, course, baro, altitude knobs; autopilot keys; volume | Other bezel controls with their own input events (the other `as1000_*` lines of IE): planned for the autopilot-values and radio pages (navigation.md, MORE row). The autopilot mode keys are on the main page (2,1 to 2,8). | IE; navigation.md |
| Softkey labels, the active G1000 page | No SimVar in the MSFS 2024 SDK gives them (labels only through third-party bridges, not installed). | README 2.1.1 (H-events can't be read) |

## V-speeds page

Readouts only: each key shows one speed the sim gives for the loaded aircraft, in whole knots. **Pressing a
readout does nothing** (the plugin log shows a warning, as for the views page readouts). No key shows a
typed number: a speed the sim gives no variable for stays Empty.

The SimVars are on the MSFS 2024 SDK's "Aircraft Flight Model Variables" page (SDK-FMV) and, for the flap
limit, "Aircraft Control Variables" (SDK-CTLV). All are read only (`check/bad` in the SDK). They are read
in the unit `knots` (SDK-UNITS, speed: knots and feet/second are both speed units; SimConnect converts),
whatever unit the SDK lists for them (`kias`, `Feet (ft) per second` or `knots`), and shown with Format
`1.0` (no decimals, e.g. `48`).

### Layout: vspeeds

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | VS0 | VS1 | VR | [Vx] | CLIMB | | |
| **Row 2** | | CRUISE | [Vno] | VNE | VFE | | | |
| **Row 3** | | | | | | | | |
| **Row 4** | | | | | | | | |

Low speeds in row 1, high speeds in row 2; [Vx] and [Vno] mark positions kept Empty (no SimVar), so the
order stays the usual one if a later sim version adds them.

## Key table: vspeeds

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to the MORE page | none | Back key |
| 1,2 | `VS0` | Display Value | T3 | none | `(A:DESIGN SPEED VS0, knots)` [SDK-FMV, SDK-UNITS] | Format `1.0` |
| 1,3 | `VS1` | Display Value | T3 | none | `(A:DESIGN SPEED VS1, knots)` [SDK-FMV, SDK-UNITS] | Format `1.0` |
| 1,4 | `VR` | Display Value | T3 | none | `(A:DESIGN SPEED MIN ROTATION, knots)` [SDK-FMV, SDK-UNITS] | Format `1.0` |
| 1,5 | | Empty | | | | Vx: no SimVar in the MSFS 2024 SDK |
| 1,6 | `CLIMB` | Display Value | T3 | none | `(A:DESIGN SPEED CLIMB, knots)` [SDK-FMV, SDK-UNITS] | Format `1.0` |
| 1,7 | | Empty | | | | |
| 1,8 | | Empty | | | | |
| 2,1 | | Empty | | | | |
| 2,2 | `CRUISE` | Display Value | T3 | none | `(A:DESIGN SPEED VC, knots)` [SDK-FMV, SDK-UNITS] | Format `1.0` |
| 2,3 | | Empty | | | | Vno: no SimVar in the MSFS 2024 SDK |
| 2,4 | `VNE` | Display Value | T3 | none | `(A:REFERENCE SPEED MAX IAS, knots)` [SDK-FMV, SDK-UNITS] | Format `1.0` |
| 2,5 | `VFE` | Display Value | T3 | none | `(A:FLAPS CURRENT SPEED LIMITATION, knots)` [SDK-CTLV, SDK-UNITS] | Format `1.0` |
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

### What each readout shows

| Key | SimVar | What the SDK says (SDK-FMV, SDK-CTLV) | Constant? | What the test should show |
|---|---|---|---|---|
| VS0 | `DESIGN SPEED VS0` | "the stall speed when flaps are fully extended" (unit `kias`) | Design constant | A whole number of knots, below VS1; the same on the ground and in flight |
| VS1 | `DESIGN SPEED VS1` | "the stall speed when flaps are fully retracted" (unit `kias`) | Design constant | Above VS0; never changes |
| VR | `DESIGN SPEED MIN ROTATION` | "the minimum speed required for aircraft rotation" (unit ft/s) | Design constant | Above VS1; never changes |
| CLIMB | `DESIGN SPEED CLIMB` | "the optimal climb speed for the aircraft" (unit ft/s); in the aircraft's flight_model.cfg it is `climb_speed`, "The aircraft climb speed, in knots" (SDK-CFG) | Design constant | Above VR; never changes. The sim's climb speed, not defined as Vy (best rate) or Vx (best angle): so the title is CLIMB, not VY; the checklist records the number |
| CRUISE | `DESIGN SPEED VC` | "the aircraft ideal cruising speed" (unit ft/s); in flight_model.cfg it is `cruise_speed`, "in ktas" (SDK-CFG): a true airspeed, where the other keys show indicated speeds | Design constant | A whole number of knots; never changes. The sim's design cruise speed (the SDK's Vc) as a true airspeed, not Vno and not the POH Vc: so the title is CRUISE, not VC |
| VNE | `REFERENCE SPEED MAX IAS` | "The maximum IAS that the aircraft can fly at" (unit knots) | Reference speed; doesn't change in flight | The highest number on the page; never changes |
| VFE | `FLAPS CURRENT SPEED LIMITATION` | "The maximum allowed speed with the current flaps position" (unit knots) | **Not constant**: changes with the flap handle | A number that changes when the flaps move (the checklist records it at each flap position, including UP) |

SDK-FMV describes the SimVars of VS0, VS1, VR, CLIMB and CRUISE each as a "design constant" of the aircraft: they are the
loaded aircraft's own values, not POH numbers. No POH value is listed here (none from a source at hand).
If a readout shows about 1.7 times the expected number (1 knot is about 1.69 feet per second), the
conversion from the SDK's unit didn't happen: record it (see "Fallbacks").

**Not on this page, and why:**

| Speed or SimVar | Why not | Source |
|---|---|---|
| Vx (best angle of climb) | No SimVar for it in the MSFS 2024 SDK's flight model variables. The aircraft's flight_model.cfg holds it (`best_angle_climb_speed`), but no SimVar reads it. Position 1,5 stays Empty. | SDK-FMV; SDK-CFG |
| Vno (maximum structural cruising speed) | No SimVar for it: flight_model.cfg holds it (`normal_operating_speed`), but no SimVar reads it. `ESTIMATED CRUISE SPEED` ("Estimated cruise speed") is not Vno (a lead from Jiblet's package used it as Vno: dropped). Position 2,3 stays Empty. | SDK-FMV; SDK-CFG; Jiblet |
| `DESIGN TAKEOFF SPEED` | "the aircraft ideal takoff speed": not one of the speeds this page lists. | SDK-FMV |
| `REFERENCE SPEED MAX IAS GEAR DOWN` | Gear-down limit: the C172 has fixed gear (main page GEAR key). | SDK-FMV |
| A fixed Vfe for full flaps | No SimVar (flight_model.cfg holds it, `max_flaps_extended`, but no SimVar reads it); VFE shows the limit for the current flap position instead. | SDK-CTLV; SDK-CFG |

## Sources

| Tag | Source |
|---|---|
| README | PilotsDeck README, https://github.com/Fragtality/PilotsDeck/blob/master/README.md (1.2 HVAR "Trigger any HTML Event", command only; 1.4 the installer installs or updates the MobiFlight WASM module; 2.1 Main Command; 2.1.1 HVAR address syntax, "with or without preceding `H:`", "can't be read") |
| PD-SRC | PilotsDeck source, https://github.com/Fragtality/PilotsDeck (master branch; it may be newer than the installed 0.9.7 build): `Plugin/Simulator/SimCommand.cs` (command type `HVAR = 8`); `Plugin/Simulator/ConnectorMSFS.cs` (an HVAR command goes to `WriteHtmlVariable`, which calls `ToolsMSFS.WriteHvar(command, MobiModule)`); `Plugin/Simulator/MSFS/ToolsMSFS.cs` (`WriteSingleHvar` adds `H:` if missing, then runs it through the MobiFlight module's `ExecuteCode`) |
| PD-PI | The installed plugin's settings panel, `%APPDATA%\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\Plugin\PI\js\pi-Common.js` (line 215 `type == 8 //HVar`: command type 8 is HVar; address pattern `regHvar`) |
| SDK-AS1000 | MSFS SDK Template Explorer, `Asobo\GlassCockpit\AS1000.xml`, https://docs.flightsimulator.com/html/Content_Configuration/Models/ModelBehaviors/TemplateExplorer/Asobo/GlassCockpit/AS1000.html (KEY_PREFIX `#AS1000#_#FUNCTION#` with FUNCTION `PFD` / `MFD`; softkeys `(>H:#KEY_PREFIX#_SOFTKEYS_#KEY_ID#)` for 1 to 12; `_DIRECTTO`, `_ENT_Push`, `_CLR`, `_CLR_Long`, `_MENU_Push`, `_FPL_Push`, `_PROC_Push`, `_FMS_Upper_PUSH`/`_INC`/`_DEC`, `_FMS_Lower_INC`/`_DEC`, `_RANGE_INC`/`_DEC`, `_JOYSTICK_*`). Served under the SDK documentation's general `/html/` path; no `/msfs2024/` copy was found |
| SDK-RPN | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/reverse-polish-notation/ (H: events: "Each cockpit panel in Microsoft Flight Simulator 2024 sends a number of cockpit specific `H:` events"; "not required to be defined ahead of time") |
| SDK-FMV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-flight-model-variables/ (DESIGN SPEED VS0, VS1, MIN ROTATION, CLIMB, VC; REFERENCE SPEED MAX IAS; ESTIMATED CRUISE SPEED; DESIGN TAKEOFF SPEED; all `check/bad`) |
| SDK-CTLV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-control-variables/ (Flaps: FLAPS CURRENT SPEED LIMITATION, knots, not settable) |
| SDK-CFG | MSFS 2024 SDK, flight_model.cfg, section [REFERENCE SPEEDS], https://docs.flightsimulator.com/msfs2024/retail/content-configuration/cfg-files/flight_model.cfg/ (`climb_speed` "The aircraft climb speed, in knots"; `cruise_speed` "The aircraft cruise speed, in ktas"; it also holds `best_angle_climb_speed` (Vx), `normal_operating_speed` (Vno) and `max_flaps_extended` (Vfe), which no SimVar in SDK-FMV or SDK-CTLV reads) |
| SDK-UNITS | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/simulation-variable-units/ (speed: `knots`, `feet/second`) |
| SDK-KE | MSFS 2024 SDK key events list (`G1000_PFD_SOFTKEY1` to `12` and the other G1000 events), https://docs.flightsimulator.com/msfs2024/html/6_Programming_APIs/Key_Events/Key_Events.htm (found through a web search; candidates only, not used) |
| WT-FORUM | https://forums.flightsimulator.com/t/working-title-g1000-nxi-eventids/551265 (2022, a lead only: "We use the same H events as the original AS1000 did"; "The G1000 key events listed in the SDK docs are deprecated") |
| IE n | [reference/InputEvents-C172-G1000.txt](reference/InputEvents-C172-G1000.txt), line n (identical to the plugin's live `InputEvents.txt`) |
| EX-G1000 | The user's installed profile `G1000`: `%APPDATA%\Elgato\StreamDeck\ProfilesV3\4A4C2DB1-197F-46F2-A005-C378BBEF630A.sdProfile\Profiles\EC7CA592-CE1E-4EBD-BB2C-39FB1055BAA4\manifest.json`, actions `1,0` to `3,1`: six keys of the Generic package (TorontoWill v1.3, zip dated 2025-01-26, profile format 2.0, in `A:\FS2024 Stuff\PilotsDeck`), saved with a pre-0.8.9 PilotsDeck (BUILD_VERSION 7, no Plugin block) and imported 2026-11-11 02:35, when the Stream Deck app wrote the 0.9.7.0 Plugin block; command type 8 with `H:AS1000_MFD_*` addresses. They show the address form only and were never pressed on this PC (read only; the settings equal the package file's) |
| Jiblet | Jiblet's "Cessna 172 G1000 SD Plus XL v1.1" package in `A:\FS2024 Stuff\PilotsDeck` (PilotsDeck 0.8 format, pre-2024): leads only, each confirmed above or dropped |
| LR95-C2 | Sim test row in the project's chain ledger (2026-11-11): the legacy view K-events did nothing in MSFS 2024 |

## What each key holds

Every key is a copy of a template with only these fields changed (the generator does this; by hand only
when you change a key during a test, see phase2-main-page.md "Changing a key by hand").

**T7 Simple Button with an H-event command** (new; built by the generator from the template
`simple_button` in `tools/profilegen/templates.json`, the same as T5): Commands tab Command Type **H-Var**
(type 8; the settings panel's exact label for it was not checked), Command Address as in the Key table, On/Off Value empty, Toggle Switch and Hold Switch
unchecked, no long press; background `Images/Switch.png`, no box; Title as in the table. These are also the
values of the six pre-0.8.9 keys in EX-G1000 (command type 8, no box, linked title, `Images/Switch.png` on five
of the six; the background is the same on every bezel key here, as on ATC and MAP);
the generator changes the T5 template in exactly the fields ATC and MAP change, with command type 8 in
place of 16. PFD and MFD: every key but 1,1 and the Empty positions.

**T3 Display Value** (as RPM on the main page): Value tab Address and Format as in the Key table, no
Mappings, Decode BCD unchecked, no command. V-speeds: 1,2, 1,3, 1,4, 1,6, 2,2, 2,4, 2,5.

**Folder keys** (MORE 1,2, 1,3, 1,4): the Stream Deck app's "Create Folder", as on the main page.

## Fallbacks

Use one only if the checklist shows the main address doesn't work, and say which one you used. None is
tested; they are recorded in aircraft-mappings.md too.

| Key | Fallback | Source |
|---|---|---|
| Any PFD/MFD key | The cockpit control's input event as a B-Var command with a value, for example `B:as1000_softkey_1_pfd:1` (README 2.1.1 B-Var command form). The value is unknown: first the one-key hand test below, then (if it works) the generator gets the form from the saved key. | IE; README 2.1.1 |
| Any PFD/MFD key, no "Running Command (Type: HVAR" line in the log | The press never left the plugin: check that the plugin log shows the MobiFlight WASM connection after the flight loaded. The bezel keys need the MobiFlight WASM module (installation.md follow-up). | PD-SRC; README 1.4 |
| V-speeds readout shows about 1.7 times the expected value | No fallback address: record the number and the key; a later unit decides (for example a scale factor on the key). | SDK-FMV, SDK-UNITS |
| V-speeds readout shows nothing, 0, or -1 or another negative number (the SDK default when the aircraft's flight_model.cfg does not set it) | The SimVar isn't filled for this aircraft: record it; the key becomes Empty. | SDK-FMV |

**One-key hand test for the input-event fallback** (only if the H-event keys fail; the LR101-C2 form): in
the imported profile, on the PFD page, select key **3,1 `SK 1`**; Commands tab: Command Type **MSFS: B-Var
(InputEvent)**, **Run as Command** checked, Command Address `B:as1000_softkey_1_pfd:1`, press Tab to save.
In the sim, with the PFD showing its softkey row, press the key once: the PFD's softkey 1 function should
happen (as a mouse click on the bezel's first softkey). Then a session in Admin reads the saved key from
ProfilesV3: it is the real example for the fallback route.

## How to test

Run [tests/manual-checklist.md](../tests/manual-checklist.md), section "Phase 2: G1000 and V-speeds pages
(C172 G1000)", after the earlier Phase 2 blocks. The bezel keys have no state to read, so their test is
the G1000's own reaction: **press each key and watch the PFD or MFD; then click the same bezel button with
the mouse and check it does the same.** The readouts are checked against each other (VS0 < VS1 < VR ...)
and against the flap handle (VFE).

## When it passes

1. Any change found in the test goes into `tools/profilegen/c172-g1000.json` and this doc; then the profile
   is regenerated (not exported from the app) and imported again.
2. Fill in the "Verified" column of the G1000 and V-speeds rows in aircraft-mappings.md with the date and
   sim version, for each key that passed. Mark a key "does not work" if it did nothing; it becomes Empty.
