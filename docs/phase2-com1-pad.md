# Phase 2: COM1 pad, Cessna 172 G1000

**Status: generated, not yet sim-tested.** The page is in the generated profile and its Lua script is in
the package, but nothing has been tried in the app or the sim yet. Every new name below is recorded as
"Unverified" in [aircraft-mappings.md](aircraft-mappings.md) ("Phase 2 COM1 pad") until the checks in
[tests/manual-checklist.md](../tests/manual-checklist.md), section "Phase 2: COM1 pad (C172 G1000)", pass.

Goal: type a COM1 frequency on a number pad on the Stream Deck and send it to COM1 standby, or straight to
active. The main page's `COM1` key (3,1) can only swap active and standby. The idea comes from the Flight
Tracker Stream Deck plugin (FT-SD), whose radio key opens a numpad page on a long press. That plugin is not
used here (it has no input-event support, and PilotsDeck already does what it does); only the idea is
taken, no code or images.

The page is part of the generated profile `MSFS2024 C172 G1000` (same file, same name, same import as the
main page: see [phase2-main-page.md](phase2-main-page.md), "Import the profile"), plus **one script file to
install** (below). The table below is the reference for what each key holds; `tools/profilegen/check.py`
compares the profile with the "Key table: compad" section key by key.

Nothing on this page uses keyboard bindings, vJoy or anything tied to a controller: the keys run a
PilotsDeck Lua script that sends SimConnect events (K-events), and the readouts read SimVars, so they work
the same with the Xbox Elite controller and the T.16000M + TWCS.

## Where the page sits

A second-level folder page **compad**, opened by the folder key `COM PAD` at **MORE 1,5** (next to PFD,
MFD and V-SPEEDS; [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md), "Key table: more"). Position chosen
by the user (2026-11-12); main page 4,7 stays reserved for Anti-ice. How the pages connect:
[navigation.md](navigation.md).

Why not a long press on the main page `COM1` key, as in FT-SD: FT-SD switches to a numpad *profile* that
the plugin itself ships. A PilotsDeck key can't open a Stream Deck folder; only a folder key can.

## Install the script (once)

The pad keys call functions of the standard script
`pilotsdeck/MSFS2024-XL/_Package/Scripts/XL24-COMPAD.lua`. PilotsDeck reads scripts from its own Scripts
folder (README 3.5), so the file must be there before the page can work. Signed in as Admin, either:

- copy the file into `%APPDATA%\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\Scripts\`
  (the plugin loads new and changed scripts while it runs; no restart needed, README 3.5), or
- build and install the package with the Profile Manager (README.md, "Building the package"), which puts
  `Scripts/` files in the same place.

After any change to the script in the repo, copy it again. Without the file, the digit keys do nothing and
the plugin log says the script is not registered.

## Layout: compad

Positions are **row,column**, 1-based, row 1 at the top. 1,1 is the back key (it returns to MORE), as on
every child page. The digits sit on the right in calculator order (7-8-9 on top, 0 at the bottom between
CLR and ENT), as on a PC number pad.

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | COM1 | ENTRY | | | 7 | 8 | 9 |
| **Row 2** | | STBY ID | | | | 4 | 5 | 6 |
| **Row 3** | | | | | | 1 | 2 | 3 |
| **Row 4** | | | | | | CLR | 0 | ENT |

## Key table: compad

Action names as in phase2-main-page.md. **Back** = the Stream Deck app's back key (`backtoparent`), added
by the generator on every child page. "Empty" = no action on that key. Commands starting `lua:` are
command type **Lua Function** (saved as `14`; PD-SRC `SimCommand.cs`, PD-PI line 227).

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to MORE | none | Back key |
| 1,2 | `COM1` | COM Radio | T4 | `K:COM_STBY_RADIO_SWAP` [SDK-RADE] | Active `(A:COM ACTIVE FREQUENCY:1, MHz)`, Standby `(A:COM STANDBY FREQUENCY:1, MHz)` [SDK-RADV] | Format `3` |
| 1,3 | `ENTRY` | Display Value | T3 | none | `X:XL24_COMPAD_ENTRY` [README 2.1.1 INTERNAL; written by the script] | the typed digits as text, e.g. `118.5__`; Format empty |
| 1,4 | | Empty | | | | |
| 1,5 | | Empty | | | | |
| 1,6 | `7` | Simple Button | T8 | `lua:XL24-COMPAD:DIGIT(7)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 1,7 | `8` | Simple Button | T8 | `lua:XL24-COMPAD:DIGIT(8)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 1,8 | `9` | Simple Button | T8 | `lua:XL24-COMPAD:DIGIT(9)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 2,1 | | Empty | | | | |
| 2,2 | `STBY ID` | Display Value | T3 | none | `(A:COM STANDBY FREQ IDENT:1, String)` [SDK-RADV; PD-SRC string A-Var] | the station ident as text; Format empty |
| 2,3 | | Empty | | | | |
| 2,4 | | Empty | | | | |
| 2,5 | | Empty | | | | |
| 2,6 | `4` | Simple Button | T8 | `lua:XL24-COMPAD:DIGIT(4)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 2,7 | `5` | Simple Button | T8 | `lua:XL24-COMPAD:DIGIT(5)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 2,8 | `6` | Simple Button | T8 | `lua:XL24-COMPAD:DIGIT(6)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 3,1 | | Empty | | | | |
| 3,2 | | Empty | | | | |
| 3,3 | | Empty | | | | |
| 3,4 | | Empty | | | | |
| 3,5 | | Empty | | | | |
| 3,6 | `1` | Simple Button | T8 | `lua:XL24-COMPAD:DIGIT(1)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 3,7 | `2` | Simple Button | T8 | `lua:XL24-COMPAD:DIGIT(2)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 3,8 | `3` | Simple Button | T8 | `lua:XL24-COMPAD:DIGIT(3)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 4,1 | | Empty | | | | |
| 4,2 | | Empty | | | | |
| 4,3 | | Empty | | | | |
| 4,4 | | Empty | | | | |
| 4,5 | | Empty | | | | |
| 4,6 | `CLR` | Simple Button | T8 | Main `lua:XL24-COMPAD:BACK`, Second (long press) `lua:XL24-COMPAD:CLEAR` [README 2.1.1 LUAFUNC, 2.1] | none | fixed image |
| 4,7 | `0` | Simple Button | T8 | `lua:XL24-COMPAD:DIGIT(0)` [README 2.1.1 LUAFUNC] | none | fixed image |
| 4,8 | `ENT` | Simple Button | T8 | Main `lua:XL24-COMPAD:ENTER`, Second (long press) `lua:XL24-COMPAD:ENTER_SWAP` [README 2.1.1 LUAFUNC, 2.1] | none (COM1 at 1,2 shows the result) | fixed image |

**The pattern is a proven one.** The GSX Pro reference profile the user installed does the same thing:
a Lua script writes a string into an `X:` variable, a Display Value key shows it, and other keys run script
functions (its menu keys read `X:GSX_MENU_LINE10` and send `lua:GSX:SELECT(10)`, saved command type 14).
That is a lead for the saved form only (REF-GSX); its files are not copied.

## What the keys do

The script keeps the typed digits (at most 6) and writes them to `X:XL24_COMPAD_ENTRY` after every key,
with the decimal point fixed after the third digit: `___.___`, `1__.___`, `11_.___`, `118.___`,
`118.5__`, `118.52_`, `118.525`.

- **Digits that can't make a COM frequency are ignored** (COM runs from 118.000 to 136.990 MHz):

  | Digit position | Allowed |
  |---|---|
  | 1st | `1` only |
  | 2nd | `1`, `2`, `3` |
  | 3rd | after `11`: `8`, `9`; after `13`: `0` to `6`; after `12`: any |
  | 4th to 6th | any (a 7th digit is ignored) |

- **CLR** deletes the last digit; a **long press** (>= 500 ms) clears the entry.
- **ENT** needs at least 3 digits. Missing decimals are zeros (`118` = 118.000, `1185` = 118.500). Then:
  - **25 kHz shorthand.** If the radio is in 25 kHz mode (`(A:COM SPACING MODE:1, Enum)` = 0, SDK-RADV)
    and exactly two decimals were typed ending in 2 or 7, a 5 is added: `118.52` = 118.525, `118.57` =
    118.575. That is how 25 kHz frequencies are usually written and said. In 8.33 kHz mode nothing is
    added.
  - **Range check.** Below 118.000 or above 136.990: nothing is sent, the entry stays (fix it with CLR),
    and `lua.log` says why.
  - **Send.** `K:COM_STBY_RADIO_SET_HZ` with the frequency in Hz (118.525 MHz = `118525000`) (SDK-RADE:
    "[0]: Frequency value (Hz) Sets COM 1/2/3 standby frequency in Hz"). The script builds the number as
    text (the kHz digits followed by `000`), so no number formatting is involved; it fits the unsigned whole
    number a K-event parameter takes (README 2.1.1 KVAR). The Hz form is used instead of
    `COM_STBY_RADIO_SET` (BCD16) because BCD16 can't hold the third decimal.
  - The entry clears.
- **Long press ENT** does the same and then, 100 ms later, sends `K:COM_STBY_RADIO_SWAP`, so the new
  frequency becomes active.
- **COM1** (1,2) is the same key as the main page's 3,1: it reads both frequencies from the sim, and a
  press swaps them. The deck never assumes ENT worked: this key shows what the sim has.
- **STBY ID** (2,2) shows the station ident the sim gives for the standby frequency (for example the
  ATIS station), read as a string A-Var (PilotsDeck reads an A-Var as text when its unit is `String`,
  PD-SRC). Optional: if it shows nothing in the sim test, it becomes Empty.
- **Leaving the page clears the entry.** PilotsDeck registers a standard script when a key whose command
  uses it appears, and unregisters it when no such key is left (PD-SRC `RessourceStore.cs`); the
  script's top level runs on each load and writes the empty entry (README 3.5).

## The script

[`pilotsdeck/MSFS2024-XL/_Package/Scripts/XL24-COMPAD.lua`](../pilotsdeck/MSFS2024-XL/_Package/Scripts/XL24-COMPAD.lua),
a standard script (README 3.5.1). The `XL24-` prefix keeps it apart from other packages' scripts in the
plugin's shared Scripts folder. It uses only `SimVar`, `SimRead`, `SimWrite`, `SimCommand`, `Sleep` and
`Log` (README 3.5.1). Functions: `DIGIT(n)`, `BACK`, `CLEAR`, `ENTER`, `ENTER_SWAP`. PilotsDeck runs a
command `lua:XL24-COMPAD:DIGIT(7)` as the Lua code `DIGIT(7)`, and `lua:XL24-COMPAD:BACK` as `BACK()`
(PD-SRC `ScriptManager.cs` `RunFunction`), so the digit arrives as a number. It runs only while the sim is
connected (same place: `SimController.IsReadyProcess`).

## What each key holds

Every key is a copy of a template with only these fields changed (the generator does this).

- **T3** and **T4** are the main page's (see [phase2-main-page.md](phase2-main-page.md), "What each key
  holds"). ENTRY and STBY ID are T3 with no command: Value Address as in the table, Format empty, no
  Mappings.
- **T8 Simple Button with a Lua Function command** (new here): the main page's T5 (template
  `simple_button`, states from the Phase 1 AP key, `LinkedTitle` on, Background image `Images/Switch.png`,
  Draw Box off) with Command Type **All Sims: Lua Function** (`ActionType` 14) and the Command Address
  from the table. CLR and ENT also have **long press** on (`HasLongPress`) with a Second Command of the
  same type (`ActionTypeLong` 14, `AddressActionLong`). The settings panel accepts these addresses (PD-PI
  line 196 `regLuaFunc`: `lua:` + file name + `:` + function, optional `(...)`).

## Not on this page, and why

| Function | Why not now |
|---|---|
| COM2, NAV1/2 | Same script with an index; first prove COM1. NAV would use `NAV1_STBY_SET_HZ` (SDK-RADE) and 108.000 to 117.950. |
| Transponder code entry | Natural next use of the same pad (4 octal digits, `K:XPNDR_SET`); planned in phase2-main-page.md. A later unit. |
| Opening the pad from a long press on main 3,1 | Not possible with a folder (see "Where the page sits"). |
| The G1000's own COM knobs (`B:as1000_com_large_pfd` and so on, IE 47-52) | Turning knobs digit by digit is what the pad replaces; the K-event sets the frequency in one step. |
| Digit and ENT images from the icon pack | Personal use only; possible later in the local icon build ([icons.md](icons.md)). |

## Fallbacks

Use one only if the checklist shows the main route doesn't work, and say which one you used. None is
tested.

| Key | Fallback | Source |
|---|---|---|
| ENTRY shows nothing, `0` or the last value while digits are typed (the log shows the DIGIT commands) | Make the key read the entry from the script instead: Value Address `lua:XL24-COMPAD:ENTRY_TEXT` with a function `ENTRY_TEXT()` that returns the same string (a Lua function used as a variable, README 2.1.1 LUAFUNC). Not built. | README 2.1.1 |
| ENT: standby doesn't change, `lua.log` says "COM1 standby set to ..." | `K:COM_STBY_RADIO_SET` with the BCD16 value (two decimals only; 118.52 = `0x1852`), or report it: the K-event route may not reach the G1000 radio | SDK-RADE |
| STBY ID shows nothing | Empty the key | SDK-RADV |
| Nothing works, plugin log: the script is not registered | The script file is not in the plugin's Scripts folder: see "Install the script" | PD-SRC `ScriptManager.cs` |

## How to test

Run [tests/manual-checklist.md](../tests/manual-checklist.md), section "Phase 2: COM1 pad (C172 G1000)". As
on the other pages, check the reverse direction too: **change COM1 with the G1000 knob and check that the
COM1 key on the pad follows without a key being pressed.**

## When it passes

1. Any change found in the test goes into `tools/profilegen/c172-g1000.json`, the script and this doc;
   then the profile is regenerated (not exported from the app) and imported again, and the script copied
   again.
2. Fill in the "Verified" column of the COM1 pad rows in aircraft-mappings.md with the date and sim
   version, for each function that passed.

## Sources

| Tag | Source |
|---|---|
| SDK-RADE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-radio-navigation-events/ (`COM_STBY_RADIO_SET_HZ` "[0]: Frequency value (Hz)", `COM_STBY_RADIO_SET` BCD16, `COM_STBY_RADIO_SWAP`), read 2026-11-12 |
| SDK-RADV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-radio-navigation-variables/ (`COM SPACING MODE` "Enum: 0 = 25kHz 1 = 8.33kHz"; `COM STANDBY FREQ IDENT` String; `COM STANDBY FREQUENCY`), read 2026-11-12 |
| README | PilotsDeck README, https://github.com/Fragtality/PilotsDeck/blob/master/README.md: 2.1 (Main and Second, long press, command); 2.1.1 KVAR (parameters are positive whole numbers), LUAFUNC (`lua:File:Function(Parameter)`), INTERNAL (`X:Name`); 3.5 (standard scripts: Scripts folder, loaded on demand, reloaded when changed, state kept while loaded, top level runs on load); 3.5.1 (`SimVar`, `SimRead`, `SimWrite`, `SimCommand`, `Sleep`, `Log`) |
| PD-SRC | PilotsDeck source, https://github.com/Fragtality/PilotsDeck (master, read 2026-11-12): `Plugin/Simulator/SimCommand.cs` (`LUAFUNC = 14`), `Plugin/Actions/Simple/RessourceStore.cs` (a Lua Function command registers its script when the key's resources register, and unregisters it), `Plugin/Resources/ScriptManager.cs` (`RunFunction`: `()` appended when missing, the call run as Lua code; needs the sim connected), `Plugin/Resources/Variables/ManagedAddress.cs` and `VariableManager.cs` (an A-Var with unit `String` is read as a string) |
| PD-PI | The installed plugin's settings panel, `%APPDATA%\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\Plugin\PI\js\pi-Common.js` lines 196-197 (`regLuaFunc`, `regInternal`) and 227 (`type == 14 //LuaFunc`) |
| REF-GSX | The GSX Pro reference profile installed in ProfilesV3 (Display Value key with Address `X:GSX_MENU_LINE10` and command type 14 `lua:GSX:SELECT(10)`); the Fenix XL profile has a type 14 long press (`lua:fnx-a320:MCDU_AOC2`). Leads for the saved form only, not copied. |
| FT-SD | https://github.com/nguyenquyhy/Flight-Tracker-StreamDeck (GPL-3.0), docs/USERGUIDE.md "NAV & COM": hold the radio key to open a numpad. Idea only; no code or images taken. |
| IE | [reference/InputEvents-C172-G1000.txt](reference/InputEvents-C172-G1000.txt) |
