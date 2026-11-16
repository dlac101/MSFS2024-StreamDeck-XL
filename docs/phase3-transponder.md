# Phase 3: transponder page, Cessna 172 G1000

**Status: generated, not yet sim-tested.** The page is in the generated profile and its Lua script is in
the package, but nothing has been tried in the app or the sim yet. Every new name below is recorded as
"Unverified" in [aircraft-mappings.md](aircraft-mappings.md) ("Phase 3 transponder page") until the checks
in [tests/manual-checklist.md](../tests/manual-checklist.md), section "P3-2: Transponder page (C172 G1000)",
pass.

Goal: set the squawk code from the Stream Deck and see the transponder as the sim has it: a number pad
for the four code digits (one press per digit, ENT sends the code once), a code readout, a mode readout,
STBY / ON / ALT mode keys, IDENT and a one-press VFR code (1200). The main page's `XPDR` key (3,2) only
shows the code; this page sets it.

The page is part of the generated profile `MSFS2024 C172 G1000` (same file, same name, same import as the
main page: see [phase2-main-page.md](phase2-main-page.md), "Import the profile"), plus **one script file to
install** (below). The table below is the reference for what each key holds; `tools/profilegen/check.py`
compares the profile with the "Key table: xpdr" section key by key.

Nothing on this page uses keyboard bindings, vJoy or anything tied to a controller: the keys run a
PilotsDeck Lua script that sends a SimConnect event (K-event), send K-events, or write a SimVar, and the
readouts read SimVars, so they work the same with the Xbox Elite controller and the T.16000M + TWCS.

## Where the page sits

A second-level folder page **xpdr**, opened by the folder key `XPDR` at **MORE 1,7** (next to AUTOPILOT at
1,6; [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md), "Key table: more"). MORE 1,8 `RADIOS` opens the
radios page ([phase3-radios.md](phase3-radios.md)). How the pages connect: [navigation.md](navigation.md).

## Install the script (once)

The pad keys call functions of the standard script
`pilotsdeck/MSFS2024-XL/_Package/Scripts/XL24-XPDRPAD.lua`. PilotsDeck reads scripts from its own Scripts
folder (README 3.5), so the file must be there before the pad can work. Signed in as Admin:

- main route: install the package with the Profile Manager ([package.md](package.md), "Install"; not yet tested
  with the Profile Manager). It copies every script of the package into the plugin's `Scripts` folder.
- by hand (fallback): copy the file into `%APPDATA%\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\Scripts\`
  (the plugin loads new and changed scripts while it runs; no restart needed, README 3.5).

This is the same step as for the COM1 pad ([phase2-com1-pad.md](phase2-com1-pad.md), "Install the script").
After any change to the script in the repo, install the new package or copy it again. Without the file, the
digit, CLR and ENT keys do nothing and the plugin log says the script is not registered. The other keys
(readouts, STBY / ON / ALT, IDENT, VFR) don't need the script.

## Layout: xpdr

Positions are **row,column**, 1-based, row 1 at the top. 1,1 is the back key (it returns to MORE), as on
every child page. The digits keep the COM PAD's places (calculator order) so the hand learns one pad; 8 and
9 (1,7 and 1,8) are Empty, because transponder codes use the digits 0 to 7 only. Readouts on row 1, mode
keys on row 2, IDENT and VFR on row 3.

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | XPDR | ENTRY | MODE | | 7 | | |
| **Row 2** | | STBY | ON | ALT | | 4 | 5 | 6 |
| **Row 3** | | IDENT | VFR | | | 1 | 2 | 3 |
| **Row 4** | | | | | | CLR | 0 | ENT |

## Key table: xpdr

Action names as in phase2-main-page.md. **Back** = the Stream Deck app's back key (`backtoparent`), added
by the generator on every child page. "Empty" = no action on that key. Commands starting `lua:` are
command type **Lua Function** (saved as `14`), `K:` commands **K-Var** (`16`), and the STBY / ON / ALT
commands **A-Var** (`12`) (PD-SRC `SimCommand.cs`; PD-PI lines 221, 227, 231).

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to MORE | none | Back key |
| 1,2 | `XPDR` | Display Value | T3 | none | `(A:TRANSPONDER CODE:1, Bco16)` [SDK-RADV] | Decode BCD, Format `4.0` |
| 1,3 | `ENTRY` | Display Value | T3 | none | `X:XL24_XPDRPAD_ENTRY` [README 2.1.1 INTERNAL; written by the script] | the typed digits as text, e.g. `12__`; Format empty |
| 1,4 | `MODE` | Display Value | T3 | none | `(A:TRANSPONDER STATE:1, Enum)` [SDK-RADV] | Mappings `0=OFF:1=STBY:2=TEST:3=ON:4=ALT:5=GND` |
| 1,5 | | Empty | | | | |
| 1,6 | `7` | Simple Button | T8 | `lua:XL24-XPDRPAD:DIGIT(7)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 1,7 | | Empty | | | | no key 8 (codes use 0-7) |
| 1,8 | | Empty | | | | no key 9 (codes use 0-7) |
| 2,1 | | Empty | | | | |
| 2,2 | `STBY` | Dynamic Button | T6 | `(A:TRANSPONDER STATE:1, Enum)`, On `$=1` / Off `` [SDK-RADV, README 2.1.1, 2.1.2] | `(A:TRANSPONDER STATE:1, Enum)` [SDK-RADV] | On/Off image: On `1`, Off `4` |
| 2,3 | `ON` | Dynamic Button | T6 | `(A:TRANSPONDER STATE:1, Enum)`, On `$=3` / Off `` [SDK-RADV, README 2.1.1, 2.1.2] | `(A:TRANSPONDER STATE:1, Enum)` [SDK-RADV] | On/Off image: On `3`, Off `1` |
| 2,4 | `ALT` | Dynamic Button | T6 | `(A:TRANSPONDER STATE:1, Enum)`, On `$=4` / Off `` [SDK-RADV, README 2.1.1, 2.1.2] | `(A:TRANSPONDER STATE:1, Enum)` [SDK-RADV] | On/Off image: On `4`, Off `1` |
| 2,5 | | Empty | | | | |
| 2,6 | `4` | Simple Button | T8 | `lua:XL24-XPDRPAD:DIGIT(4)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 2,7 | `5` | Simple Button | T8 | `lua:XL24-XPDRPAD:DIGIT(5)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 2,8 | `6` | Simple Button | T8 | `lua:XL24-XPDRPAD:DIGIT(6)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 3,1 | | Empty | | | | |
| 3,2 | `IDENT` | Dynamic Button | T2 | `K:XPNDR_IDENT_ON` [SDK-RADE] | `(A:TRANSPONDER IDENT:1, Bool)` [SDK-RADV] | On/Off image |
| 3,3 | `VFR` | Simple Button | T5 | `K:XPNDR_SET:4608` [SDK-RADE] | none | fixed image |
| 3,4 | | Empty | | | | |
| 3,5 | | Empty | | | | |
| 3,6 | `1` | Simple Button | T8 | `lua:XL24-XPDRPAD:DIGIT(1)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 3,7 | `2` | Simple Button | T8 | `lua:XL24-XPDRPAD:DIGIT(2)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 3,8 | `3` | Simple Button | T8 | `lua:XL24-XPDRPAD:DIGIT(3)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 4,1 | | Empty | | | | |
| 4,2 | | Empty | | | | |
| 4,3 | | Empty | | | | |
| 4,4 | | Empty | | | | |
| 4,5 | | Empty | | | | |
| 4,6 | `CLR` | Simple Button | T8 | Main `lua:XL24-XPDRPAD:BACK`, Second (long press) `lua:XL24-XPDRPAD:CLEAR` [README 2.1.1 LUAFUNC, 2.1] | none | fixed image |
| 4,7 | `0` | Simple Button | T8 | `lua:XL24-XPDRPAD:DIGIT(0)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 4,8 | `ENT` | Simple Button | T8 | `lua:XL24-XPDRPAD:ENTER` [README 2.1.1 LUAFUNC] | none (XPDR at 1,2 shows the result) | fixed image |

## What the keys do

- **XPDR** (1,2) shows the squawk code the sim has, exactly as the main page's 3,2: the SimVar unit is
  Bco16 (each of the four octal digits is one hex nibble, so code 1200 is 0x1200 = 4608), the key decodes
  it with **Decode BCD** and shows it with Format `4.0` (four digits with leading zeros, e.g. `0400`).
- **ENTRY** (1,3) shows the digits typed so far, written by the script into `X:XL24_XPDRPAD_ENTRY`:
  `____`, `7___`, `70__`, `700_`, `7000`.
- **MODE** (1,4) shows the transponder mode the sim has, through Mappings
  `0=OFF:1=STBY:2=TEST:3=ON:4=ALT:5=GND` (the SDK's enum, SDK-RADV).
- **Digits 0 to 7**: add one digit (at most four). There are no keys 8 and 9.
- **CLR** deletes the last digit; a **long press** (>= 500 ms, README 2.1) clears the entry.
- **ENT** needs exactly four digits; with fewer, nothing is sent, the entry stays and `lua.log` says why.
  With four it sends `K:XPNDR_SET` with the code (below), logs it and clears the entry. The deck never
  assumes it worked: XPDR at 1,2 shows what the sim has.
- **STBY / ON / ALT** (2,2 to 2,4) write the transponder mode SimVar `TRANSPONDER STATE` (index 1): STBY
  writes 1, ON writes 3, ALT writes 4 (On Value `$=1` / `$=3` / `$=4`: "always moved to" that value,
  README 2.1.2). Each key is lit (On image) only while MODE is its value; STBY shows its Off image at ALT
  (4), ON and ALT at STBY (1); for any other mode the key shows only its background (views precedent,
  [phase2-trim-views.md](phase2-trim-views.md), PilotsDeck `ActionSwitchDisplay.cs`). So the keys are lit
  from the read side only, never from the press.
- **IDENT** (3,2) sends `K:XPNDR_IDENT_ON`; the sim turns ident off by itself after 18 seconds (SDK-RADE,
  SDK-RADV). The key is lit while `TRANSPONDER IDENT` is 1.
- **VFR** (3,3) sets code 1200 in one press: `K:XPNDR_SET:4608` (4608 = 0x1200).
- **Leaving the page clears the entry.** PilotsDeck registers a standard script when a key whose command
  uses it appears, and unregisters it when no such key is left (PD-SRC `RessourceStore.cs`); the script's
  top level runs on each load and writes the empty entry (README 3.5), as on the COM1 pad.
- With no sim the plugin is Idle and the keys show a static preview; with the sim but no flight every key
  shows the plugin's Wait image ([phase2-main-page.md](phase2-main-page.md)).

## The script

[`pilotsdeck/MSFS2024-XL/_Package/Scripts/XL24-XPDRPAD.lua`](../pilotsdeck/MSFS2024-XL/_Package/Scripts/XL24-XPDRPAD.lua),
a standard script (README 3.5.1). The `XL24-` prefix keeps it apart from other packages' scripts in the
plugin's shared Scripts folder. It uses only `SimWrite`, `SimCommand` and `Log` (README 3.5.1). Functions:
`DIGIT(n)`, `BACK`, `CLEAR`, `ENTER`. PilotsDeck runs a command `lua:XL24-XPDRPAD:DIGIT(7)` as the Lua code
`DIGIT(7)` (PD-SRC `ScriptManager.cs` `RunFunction`), so the digit arrives as a number; the script ignores
anything but a whole number 0 to 7, and any digit past the fourth.

**The code it sends.** `K:XPNDR_SET` takes the code Bco16 encoded (SDK-RADE: "[0]: Frequency value (Bco16
encoded)"), and a K-event parameter is a positive whole number (README 2.1.1 KVAR). So ENT reads the four
typed digits as one hex number and sends it in decimal: `7000` = 0x7000 = `K:XPNDR_SET:28672`, `1200` =
0x1200 = `4608` (the VFR key's value). The `lua.log` line says "XL24-XPDRPAD: squawk set to 7000
(K:XPNDR_SET 28672)". It runs only while the sim is connected (PD-SRC `SimController.IsReadyProcess`).

## What each key holds

Every key is a copy of a template with only these fields changed (the generator does this).

- **T3** (XPDR, ENTRY, MODE): the main page's Display Value ([phase2-main-page.md](phase2-main-page.md),
  "What each key holds"), no command: Value Address, Format, Decode BCD (XPDR only) and Mappings (MODE only)
  as in the table.
- **T8** (digits, CLR, ENT): the COM1 pad's Simple Button with a Lua Function command
  ([phase2-com1-pad.md](phase2-com1-pad.md), "What each key holds"): `ActionType` 14, Command Address from
  the table, Background image `Images/Switch.png`, Draw Box off. CLR also has long press on
  (`HasLongPress`) with a Second Command of the same type (`ActionTypeLong` 14, `AddressActionLong`
  `lua:XL24-XPDRPAD:CLEAR`). ENT has no long press.
- **T5** (VFR): the main page's Simple Button with a K-event command (`ActionType` 16).
- **T2** (IDENT): the Phase 1 AP key's Dynamic Button (K-event command, On `1` / Off `0` states) with the
  command and Value Address from the table.
- **T6** (STBY, ON, ALT): the views page's Dynamic Button with an A-Var command (template
  `avar_dynamic_button`, a copy of the user's sim-tested EXTERNAL key, [phase2-trim-views.md](phase2-trim-views.md),
  "T6"): Command Type A-Var (`ActionType` 12), Command Address and Value Address
  `(A:TRANSPONDER STATE:1, Enum)`, On Value `$=1` / `$=3` / `$=4`, Off Value empty, On/Off States as in the
  table.

## Which route each key uses, and why

In MSFS 2024 aircraft a cockpit control may drive an input event (B-Var) and a different SimVar index than
the standard K-event (the battery precedent, [aircraft-mappings.md](aircraft-mappings.md)). For the
transponder, **the 2024 C172 G1000 exposes no input event**: its input-event list
([reference/InputEvents-C172-G1000.txt](reference/InputEvents-C172-G1000.txt)) has only the transponder
breaker `B:electrical_breaker_btn_breaker_xpndr` (IE 172). So every key uses the SDK's K-events or
SimVars, and the readouts (XPDR, MODE, IDENT's light) show whether the cockpit follows.

| Key | Route | Reason |
|---|---|---|
| Digits, CLR, ENT | Lua script, then `K:XPNDR_SET` | A plain key sends one fixed command and can't hold typed digits; the script collects four and sends the code once (the COM1 pad's reason). |
| XPDR, MODE | SimVar reads | `TRANSPONDER CODE` and `TRANSPONDER STATE`, index 1 ("Index should always be 1", SDK-RADV). |
| STBY / ON / ALT | A-Var write (`ActionType` 12) to `TRANSPONDER STATE:1` | The SDK's radio events have **no transponder mode event** (only `XPNDR`, `XPNDR_1000/100/10/1_INC/DEC`, `XPNDR_INC/DEC_CARRY`, `XPNDR_IDENT_*` and `XPNDR_SET`, SDK-RADE), and the aircraft has no transponder input event. The MSFS 2024 SDK marks `TRANSPONDER STATE` **settable** (SDK-RADV, rechecked 2026-11-14: the Settable cell of its row holds the green tick, while `TRANSPONDER CODE` holds the red cross). The coordinator's ruling for P3-2 (A-4) allows an A-Var write for these three keys only, as a narrow widening of the views page's rule (an A-Var write to a SimVar the SDK marks settable). |
| IDENT | `K:XPNDR_IDENT_ON` | SDK-RADE: "After 18 seconds it will disable automatically"; ON (not TOGGLE) so a second press never cancels an ident. |
| VFR | `K:XPNDR_SET:4608` | One press for 1200; the same event as ENT. |

**The hand test decides STBY / ON / ALT.** The G1000 can hold its own transponder mode and set the SimVar
back, so a key that changes `TRANSPONDER STATE` (MODE follows) but **not the PFD's own XPDR mode display**
counts as a failed hand test. Then the repair empties the three keys (with that reason), keeps the MODE
readout, and this doc names the PFD softkeys for the mode (XPDR, then STBY / ON / ALT). The checklist step
for these keys checks the PFD's mode display, not only MODE.

## Not on this page, and why

| Function | Why not now |
|---|---|
| Keys 8 and 9 | Squawk codes are octal: digits 0 to 7 only. |
| OFF, TEST and GND mode keys | Not built (this page has the three flying modes STBY / ON / ALT); MODE still shows these modes when the sim has them. |
| NAV1/NAV2 and COM2 tuning, COM1/COM2 mic select | The radios page (MORE 1,8 `RADIOS`, [phase3-radios.md](phase3-radios.md)). |
| Code entry by the G1000 softkeys (`H:` events) | The pad sets the code in one step; the PFD's XPDR softkeys stay usable by hand. |
| Digit and ENT images from the icon pack | Personal use only; in the local icon build ([icons.md](icons.md)). |

## Fallbacks

Use one only if the checklist shows the main route doesn't work, and say which one you used. None is
tested.

| Key | Fallback | Source |
|---|---|---|
| Digits / ENT (no Lua, or `K:XPNDR_SET` does nothing) | Per-digit keys: four keys `K:XPNDR_1000_INC`, `K:XPNDR_100_INC`, `K:XPNDR_10_INC`, `K:XPNDR_1_INC` with long press `_DEC` ("Increments the first digit of the transponder.", and so on); ENTRY, digits, CLR and ENT then Empty | SDK-RADE |
| ENTRY shows nothing, `0` or the last value while digits are typed | The key reads the entry from the script instead: Value Address `lua:XL24-XPDRPAD:...` with a function that returns the same string (as the COM1 pad's ENTRY fallback). Not built. | README 2.1.1 |
| XPDR shows a wrong number | `(A:TRANSPONDER CODE:1, number)`, Decode BCD unchecked (the main page 3,2 fallback) | SDK-RADV, SDK-UNITS |
| STBY / ON / ALT: the PFD's mode doesn't change (MODE may or may not follow) | The three keys go Empty with the reason; MODE stays; set the mode with the PFD softkeys (XPDR, then STBY / ON / ALT) by hand (the pfd page's softkeys reach them) | A-4 ruling |
| IDENT doesn't ident | `K:XPNDR_IDENT_TOGGLE`, then `K:XPNDR_IDENT_SET:1` | SDK-RADE |
| VFR | `K:XPNDR_SET:0x1200` (the same value as hex, README 2.1.1 KVAR) | SDK-RADE; README 2.1.1 |
| Nothing on the pad works, plugin log: the script is not registered | The script file is not in the plugin's Scripts folder: see "Install the script" | PD-SRC `ScriptManager.cs` |

## How to test

Run [tests/manual-checklist.md](../tests/manual-checklist.md), section "P3-2: Transponder page (C172
G1000)". As on the other pages, check the reverse direction too: **change the code and the mode with the
PFD's own softkeys and check that XPDR, MODE and the mode keys follow without a key being pressed.**

## When it passes

1. Any change found in the test goes into `tools/profilegen/c172-g1000.json`, the script and this doc;
   then the profile is regenerated (not exported from the app) and imported again, and the script copied
   again.
2. Fill in the "Verified" column of the transponder rows in aircraft-mappings.md with the date and sim
   version, for each function that passed.

## Sources

| Tag | Source |
|---|---|
| SDK-RADE | MSFS 2024 SDK, Key events "Aircraft Radio Navigation Events", https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-radio-navigation-events/ (`XPNDR_SET` "[0]: Frequency value (Bco16 encoded)"; `XPNDR_IDENT_ON` "After 18 seconds it will disable automatically."; `XPNDR_IDENT_TOGGLE`, `XPNDR_IDENT_SET`; `XPNDR_1000_INC` ... `XPNDR_1_DEC`; no transponder mode event), read 2026-11-14 |
| SDK-RADV | MSFS 2024 SDK, SimVars "Radio Navigation Variables", https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-radio-navigation-variables/ (`TRANSPONDER CODE` "4-digit code. Index should always be 1", Bco16; `TRANSPONDER STATE` "Enum: 0 = Off, 1 = Standby, 2 = Test, 3 = On, 4 = Alt, 5 = Ground"; `TRANSPONDER IDENT` "When set to TRUE, it will automatically turn FALSE after 18 seconds.", Bool), read 2026-11-14. The Settable column is drawn, not written: in the page source the `TRANSPONDER STATE` cell holds a `checkmark_circle` tick (green, `#00e331` in the site's stylesheet) and the `TRANSPONDER CODE` cell a `checkmark_circle_red` cross (rechecked 2026-11-14 for P3-2). The page's Markdown source (the same URL followed by `index.md`) writes the marks as text: `{{< check/good >}}` for `TRANSPONDER STATE` and `TRANSPONDER IDENT`, `{{< check/bad >}}` for `TRANSPONDER CODE` (16 good and 261 bad on the page; checked 2026-11-14 in the P3-2 review). |
| SDK-UNITS | MSFS 2024 SDK, "Simulation Variable Units" (Bco16), as in phase2-main-page.md |
| README | PilotsDeck README, https://github.com/Fragtality/PilotsDeck/blob/master/README.md: 2.1 (Main and Second command, long press >= 500 ms); 2.1.1 KVAR (up to five positive whole-number parameters, "can be given as Hexnumber prefixed with 0x"), AVAR ("make sure that it is writeable"), LUAFUNC (`lua:File:Function(Parameter)`), INTERNAL (`X:Name`); 2.1.2 (`$=4` "always moved to Position 4"); 2.2.2 (Format, Decode BCD); 3.5 and 3.5.1 (standard scripts; `SimWrite`, `SimCommand`, `Log`) |
| PD-SRC | PilotsDeck source, https://github.com/Fragtality/PilotsDeck (master): `SimCommand.cs` (AVAR = 12, LUAFUNC = 14), `RessourceStore.cs`, `ScriptManager.cs` (`RunFunction`), `ActionSwitchDisplay.cs` (no image when the value matches neither On nor Off), as cited in phase2-com1-pad.md and phase2-trim-views.md |
| PD-PI | The installed plugin's settings panel, `%APPDATA%\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\Plugin\PI\js\pi-Common.js` (line 189 `regAvar`, 195 `rxKvarCmd` accepts `K:XPNDR_SET:4608`, 196 `regLuaFunc`, 197 `regInternal`; 221 type 12, 227 type 14, 231 type 16), read 2026-11-14 |
| IE | [reference/InputEvents-C172-G1000.txt](reference/InputEvents-C172-G1000.txt) (no transponder input event; IE 172 is the transponder breaker) |
| Leads | Jiblet's C172 G1000 profile for the SD+XL (pre-2024: per-digit `XPNDR_1000/100/10/1_INC/DEC` keys reading `(A:TRANSPONDER STATE:1,Enum)`); TorontoWill's generic profile (`(A:TRANSPONDER CODE:1,number)`). Leads only; every name above is confirmed in the SDK; nothing copied. |
