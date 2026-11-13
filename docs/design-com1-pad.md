# Design: COM1 frequency pad, Cessna 172 G1000

**Status: design only. Nothing is built, generated or sim-tested.** This doc is the brief for the build
unit. Every new name below is recorded as "Unverified" in [aircraft-mappings.md](aircraft-mappings.md)
("Planned: COM1 pad").

Goal: type a COM1 frequency on a number pad on the Stream Deck and send it to COM1
standby (or straight to active). Today the main page's `COM1` key (3,1) can only swap active and standby;
tuning stays on the G1000 knobs. The idea comes from the Flight Tracker Stream Deck plugin (FT-SD), whose
radio key opens a numpad page on a long press. That plugin is not used here (it has no input-event support
and PilotsDeck already covers it); only the idea is taken.

## Where the page sits

A second-level folder page **compad**, opened by a new folder key `COM PAD` at **MORE 1,5** (next to
PFD, MFD and V-SPEEDS). That is the place [navigation.md](navigation.md) already plans for radio tuning
("radios (COM/NAV tuning, transponder code and IDENT)"), and it keeps the two-level limit.

Why not a long press on the main page `COM1` key, as in FT-SD: FT-SD switches to a numpad *profile* that
the plugin itself ships. A PilotsDeck key can't open a Stream Deck folder; only a folder key can. So the pad
is reached the normal way: `MORE`, then `COM PAD`.

Alternative, if two presses are too many: put the folder key on the main page at **4,7** (now reserved for
Anti-ice; the C172 has only pitot heat, which is already at 4,6). That makes compad a first-level page.
The user decides; the layout below is the same either way.

## Layout: compad

Positions are **row,column**, 1-based, row 1 at the top. 1,1 is the back key, as on every child page.
The digits sit on the right in calculator order (7-8-9 on top, 0 at the bottom between CLR and ENT), as on
a PC number pad.

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | COM1 | ENTRY | | | 7 | 8 | 9 |
| **Row 2** | | STBY ID | | | | 4 | 5 | 6 |
| **Row 3** | | | | | | 1 | 2 | 3 |
| **Row 4** | | | | | | CLR | 0 | ENT |

| Pos | Title | Action | Command | Read | Display |
|---|---|---|---|---|---|
| 1,2 | `COM1` | COM Radio (template T4, the same key as main 3,1) | `K:COM_STBY_RADIO_SWAP` [SDK-RADE] | `(A:COM ACTIVE FREQUENCY:1, MHz)`, `(A:COM STANDBY FREQUENCY:1, MHz)` [SDK-RADV] | Format `3`. This is the read-back: it shows what the sim really has after ENT. |
| 1,3 | `ENTRY` | Display Value, no command | none | `X:XL24_COMPAD_ENTRY` (internal variable, written by the script) [README 2.1.1 INTERNAL] | The typed digits, e.g. `118.5__`; `___.___` when empty |
| 2,2 | `STBY ID` | Display Value, no command | none | `(A:COM STANDBY FREQ IDENT:1, String)` [SDK-RADV] | Station ident of the standby frequency (e.g. the ATIS station). Optional: drop it if it reads nothing. |
| 1,6 to 3,8, 4,7 | `7` `8` `9` `4` `5` `6` `1` `2` `3` `0` | Simple Button (template T5), command type Lua Function | `lua:XL24-COMPAD:DIGIT(n)` with n = the key's digit [README 2.1.1 LUAFUNC] | none (ENTRY shows the result) | Fixed image, title = the digit |
| 4,6 | `CLR` | Simple Button with long press | Press `lua:XL24-COMPAD:BACK`, long press `lua:XL24-COMPAD:CLEAR` | none | Fixed image |
| 4,8 | `ENT` | Simple Button with long press | Press `lua:XL24-COMPAD:ENTER` (set standby), long press `lua:XL24-COMPAD:ENTER_SWAP` (set standby, then swap it to active) | none (COM1 at 1,2 shows the result) | Fixed image |

All other positions are Empty.

**Proven pattern this copies.** The GSX Pro reference profile the user downloaded (installed in
ProfilesV3) already does "Lua writes a string into an `X:` variable, a key shows it, other keys call Lua
functions": its menu keys read `X:GSX_MENU_LINE10` and send `lua:GSX:SELECT(10)` (saved command type
`14` = Lua Function; type `15` = Internal). That is a lead for the saved form only (REF-GSX); its files are
not copied.

## How typing works

The script keeps the typed digits (at most 6) and writes them to `X:XL24_COMPAD_ENTRY` after every key,
with the decimal point fixed after the third digit: `1__.___`, `11_.___`, `118.___`, `118.5__`,
`118.52_`, `118.525`.

**Digits that can't make a COM frequency are ignored** (COM is 118.000 to 136.990 MHz):

| Digit position | Allowed |
|---|---|
| 1st | `1` only |
| 2nd | `1`, `2`, `3` |
| 3rd | after `11`: `8`, `9`; after `13`: `0` to `6`; after `12`: any |
| 4th to 6th | any (a 7th digit is ignored) |

**ENT** needs at least 3 digits. Missing decimals are zeros (`118` = 118.000, `1185` = 118.500). Then:

- **25 kHz radio shorthand.** If the radio is in 25 kHz mode (`(A:COM SPACING MODE:1, Enum)` = 0
  [SDK-RADV]) and exactly two decimals were typed ending in 2 or 7, a 5 is added: `118.52` = 118.525,
  `118.57` = 118.575. That is how 25 kHz frequencies are usually written and said. In 8.33 kHz mode
  nothing is added.
- **Range check.** Below 118.000 or above 136.990: nothing is sent and the entry stays, so it can be fixed
  with CLR.
- **Send.** `K:COM_STBY_RADIO_SET_HZ` with the frequency in Hz (118.525 MHz = `118525000`) [SDK-RADE:
  "[0]: Frequency value (Hz) Sets COM 1/2/3 standby frequency in Hz"]. The number fits the unsigned whole
  number a K-event parameter takes (README 2.1.1 KVAR). The Hz form is used instead of `COM_STBY_RADIO_SET`
  (BCD16) because BCD16 can't hold the third decimal.
- The entry clears. **Long press ENT** also sends `K:COM_STBY_RADIO_SWAP` 100 ms later, so the new
  frequency becomes active.

The deck never assumes it worked: the `COM1` key at 1,2 reads both frequencies from the sim.

**Leaving the page clears the entry.** PilotsDeck loads a standard script while keys use it and unloads it
when none do; the script's top level runs on every load and writes the empty entry (README 3.5).

## Script (draft)

`pilotsdeck/MSFS2024-XL/_Package/Scripts/XL24-COMPAD.lua`, a standard script (README 3.5.1). The
`XL24-` prefix keeps it apart from other packages' scripts in the shared Scripts folder. Not written to the
package yet; this draft is for the build unit.

```lua
-- XL24-COMPAD.lua: COM1 frequency pad (MSFS2024-XL). DRAFT, untested.
local ENTRY   = "X:XL24_COMPAD_ENTRY"
local SPACING = "(A:COM SPACING MODE:1, Enum)"
SimVar(SPACING)

local digits = ""

local function show()
    local s = digits .. string.rep("_", 6 - #digits)
    SimWrite(ENTRY, string.sub(s, 1, 3) .. "." .. string.sub(s, 4, 6))
end

local function allowed(d)
    local n = #digits
    if n == 0 then return d == 1 end
    if n == 1 then return d >= 1 and d <= 3 end
    if n == 2 then
        local second = string.sub(digits, 2, 2)
        if second == "1" then return d >= 8 end
        if second == "3" then return d <= 6 end
        return true
    end
    return n < 6
end

function DIGIT(d)
    d = tonumber(d)
    if d == nil or d < 0 or d > 9 or not allowed(d) then return end
    digits = digits .. tostring(math.floor(d))
    show()
end

function BACK()
    digits = string.sub(digits, 1, -2)
    show()
end

function CLEAR()
    digits = ""
    show()
end

local function frequencyHz()
    if #digits < 3 then return nil end
    local s = digits
    if #s == 5 and SimRead(SPACING) == 0 then
        local last = string.sub(s, 5, 5)
        if last == "2" or last == "7" then s = s .. "5" end
    end
    s = s .. string.rep("0", 6 - #s)
    local khz = tonumber(s)
    if khz < 118000 or khz > 136990 then return nil end
    return khz * 1000
end

local function send(swap)
    local hz = frequencyHz()
    if hz == nil then
        Log("COMPAD: not a COM frequency: " .. digits)
        return
    end
    SimCommand("K:COM_STBY_RADIO_SET_HZ:" .. string.format("%d", math.floor(hz)))
    if swap then
        Sleep(100)
        SimCommand("K:COM_STBY_RADIO_SWAP")
    end
    Log("COMPAD: sent " .. hz .. (swap and " and swapped" or ""))
    CLEAR()
end

function ENTER()      send(false) end
function ENTER_SWAP() send(true)  end

show()
```

Points for the build unit to check (not in the sources): that NeoLua's `string.format("%d", ...)` prints
the whole number without a decimal or exponent (else use `SharpFormat("{0:0}", hz)`, README 3.5.1); that a
`DIGIT(7)` parameter arrives as a number or a string (the script handles both); that a Display Value shows
an `X:` string (GSX does it on a Display Value with a command; if the plain Display Value shows nothing, use
that form).

## Not in this design, and why

| Function | Why not now |
|---|---|
| COM2, NAV1/2 | Same script with an index; first prove COM1. NAV uses `NAV1_STBY_SET_HZ` [SDK-RADE] and 108.000 to 117.950. |
| Transponder code entry | Natural next use of the same pad (4 octal digits, `K:XPNDR_SET`); planned in phase2-main-page.md. A later unit. |
| Opening the pad from a long press on main 3,1 | Not possible with a folder (see "Where the page sits"). |
| The G1000's own COM knobs (`B:as1000_com_large_pfd` and so on, IE 47-52) | Turning knobs digit by digit is what the pad replaces; the K-event sets the frequency in one step. |

## How to test (goes into tests/manual-checklist.md when built)

1. Open MORE > COM PAD. ENTRY shows `___.___`; `lua.log` in the plugin's log folder shows no error.
2. Type `1 1 8 5`: ENTRY shows `118.5__`. Press ENT: COM1 standby (1,2 and the PFD) becomes 118.500.
3. Type `1 2 1 5 2`, press ENT: standby 121.525 if the radio is in 25 kHz mode (record the mode shown
   by the PFD or the sim's value of `COM SPACING MODE:1`).
4. Type `1 4`: the 4 is ignored (ENTRY stays `1__.___`). CLR deletes one digit; long CLR clears all.
5. Type `1 2 4 3 5`, long press ENT: 124.350 becomes **active** and the old active goes to standby.
6. Set a frequency with the G1000 knob: the COM1 key at 1,2 follows (read-back, reverse direction).
7. Leave the page and come back: ENTRY is empty again.
8. Plugin log: each ENT shows `Running Command` for `lua:XL24-COMPAD:ENTER`; `lua.log` shows
   `COMPAD: sent ...`.
9. If 8.33 kHz mode is available on the G1000, set it and enter 118.005: record what the radio shows
   (the SDK does not say whether the Hz value is the channel name or the real frequency).

## Sources

| Tag | Source |
|---|---|
| SDK-RADE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-radio-navigation-events/ (`COM_STBY_RADIO_SET_HZ` "[0]: Frequency value (Hz)", `COM_STBY_RADIO_SET` BCD16, `COM_STBY_RADIO_SWAP`), read 2026-11-12 |
| SDK-RADV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-radio-navigation-variables/ (`COM SPACING MODE` "Enum: 0 = 25kHz 1 = 8.33kHz"; `COM STANDBY FREQ IDENT` String; `COM STANDBY FREQUENCY`), read 2026-11-12 |
| README | PilotsDeck README, https://github.com/Fragtality/PilotsDeck/blob/master/README.md: 2.1.1 KVAR (parameters are positive whole numbers), LUAFUNC (`lua:File:Function(Parameter)`), INTERNAL (`X:Name`); 3.5 (standard scripts: loaded on demand, state kept while loaded, top level runs on load); 3.5.1 (`SimVar`, `SimRead`, `SimWrite`, `SimCommand`, `Sleep`, `Log`, `SharpFormat`) |
| REF-GSX | The GSX Pro reference profile installed in ProfilesV3 (display key with Address `X:GSX_MENU_LINE10`, command type 14 `lua:GSX:SELECT(10)`); the Fenix XL profile has a type 14 long press (`lua:fnx-a320:MCDU_AOC2`). Leads for the saved form only, not copied. |
| FT-SD | https://github.com/nguyenquyhy/Flight-Tracker-StreamDeck (GPL-3.0), docs/USERGUIDE.md "NAV & COM": hold the radio key to open a numpad. Idea only; no code or images taken. |
| IE | [reference/InputEvents-C172-G1000.txt](reference/InputEvents-C172-G1000.txt) |
