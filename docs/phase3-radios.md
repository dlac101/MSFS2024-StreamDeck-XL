# Phase 3: radios page, Cessna 172 G1000

**Status: generated, not yet sim-tested.** The page is in the generated profile, but nothing has been tried
in the app or the sim yet. Every new name below is recorded as "Unverified" in
[aircraft-mappings.md](aircraft-mappings.md) ("Phase 3 radios page") until the checks in
[tests/manual-checklist.md](../tests/manual-checklist.md), section "P3-2b: Radios page (C172 G1000)", pass.

Goal: tune and read the radios the deck had no keys for, each read from sim state: NAV1, NAV2 and COM2 with
their active and standby frequencies on one key (a press swaps them), MHz and kHz steps of the standby
frequency, the station idents, and COM1 / COM2 mic select. COM1 already has the main page's `COM1` key (3,1)
and the COM1 pad (MORE 1,5, [phase2-com1-pad.md](phase2-com1-pad.md)), so this page adds only its MIC1 key.

The page is part of the generated profile `MSFS2024 C172 G1000` (same file, same name, same import as the
main page: see [phase2-main-page.md](phase2-main-page.md), "Import the profile"). It needs **no script**. The
table below is the reference for what each key holds; `tools/profilegen/check.py` compares the profile with
the "Key table: radios" section key by key.

Nothing on this page uses keyboard bindings, vJoy or anything tied to a controller: the keys send SimConnect
events (K-events) and the readouts read SimVars, so they work the same with the Xbox Elite controller and the
T.16000M + TWCS.

## Where the page sits

A second-level folder page **radios**, opened by the folder key `RADIOS` at **MORE 1,8** (next to XPDR at
1,7; [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md), "Key table: more"). How the pages connect:
[navigation.md](navigation.md).

## Layout: radios

Positions are **row,column**, 1-based, row 1 at the top. 1,1 is the back key (it returns to MORE), as on
every child page. One two-column block per radio: the readout and its ident on top, its MHz and kHz steps
below, "+" above "-" as on the AUTOPILOT page. The steps are meant to act on the standby frequency (A-7,
below), and a press on the readout swaps active and standby.

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | NAV1 | NAV1 ID | NAV2 | NAV2 ID | COM2 | COM2 ID | |
| **Row 2** | | MHZ+ | KHZ+ | MHZ+ | KHZ+ | MHZ+ | KHZ+ | |
| **Row 3** | | MHZ- | KHZ- | MHZ- | KHZ- | MHZ- | KHZ- | |
| **Row 4** | | | | | | MIC1 | MIC2 | |

## Key table: radios

Action names as in phase2-main-page.md. **Back** = the Stream Deck app's back key (`backtoparent`), added
by the generator on every child page. "Empty" = no action on that key. Every command on this page is a
K-event, command type **K-Var** (saved as `16`) (PD-PI line 231).

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to MORE | none | Back key |
| 1,2 | `NAV1` | COM Radio | T4 | `K:NAV1_RADIO_SWAP` [SDK-RADE] | Active `(A:NAV ACTIVE FREQUENCY:1, MHz)`, Standby `(A:NAV STANDBY FREQUENCY:1, MHz)` [SDK-RADV] | Format `2` |
| 1,3 | `NAV1 ID` | Display Value | T3 | none | `(A:NAV IDENT:1, String)` [SDK-RADV] | the station ident as text; Format empty |
| 1,4 | `NAV2` | COM Radio | T4 | `K:NAV2_RADIO_SWAP` [SDK-RADE] | Active `(A:NAV ACTIVE FREQUENCY:2, MHz)`, Standby `(A:NAV STANDBY FREQUENCY:2, MHz)` [SDK-RADV] | Format `2` |
| 1,5 | `NAV2 ID` | Display Value | T3 | none | `(A:NAV IDENT:2, String)` [SDK-RADV] | the station ident as text; Format empty |
| 1,6 | `COM2` | COM Radio | T4 | `K:COM2_RADIO_SWAP` [SDK-RADE] | Active `(A:COM ACTIVE FREQUENCY:2, MHz)`, Standby `(A:COM STANDBY FREQUENCY:2, MHz)` [SDK-RADV] | Format `3` |
| 1,7 | `COM2 ID` | Display Value | T3 | none | `(A:COM ACTIVE FREQ IDENT:2, String)` [SDK-RADV] | the station ident as text; Format empty |
| 1,8 | | Empty | | | | |
| 2,1 | | Empty | | | | |
| 2,2 | `MHZ+` | Simple Button | T5 | `K:NAV1_RADIO_WHOLE_INC` [SDK-RADE] | none | fixed image |
| 2,3 | `KHZ+` | Simple Button | T5 | `K:NAV1_RADIO_FRACT_INC` [SDK-RADE] | none | fixed image |
| 2,4 | `MHZ+` | Simple Button | T5 | `K:NAV2_RADIO_WHOLE_INC` [SDK-RADE] | none | fixed image |
| 2,5 | `KHZ+` | Simple Button | T5 | `K:NAV2_RADIO_FRACT_INC` [SDK-RADE] | none | fixed image |
| 2,6 | `MHZ+` | Simple Button | T5 | `K:COM2_RADIO_WHOLE_INC` [SDK-RADE] | none | fixed image |
| 2,7 | `KHZ+` | Simple Button | T5 | `K:COM2_RADIO_FRACT_INC` [SDK-RADE] | none | fixed image |
| 2,8 | | Empty | | | | |
| 3,1 | | Empty | | | | |
| 3,2 | `MHZ-` | Simple Button | T5 | `K:NAV1_RADIO_WHOLE_DEC` [SDK-RADE] | none | fixed image |
| 3,3 | `KHZ-` | Simple Button | T5 | `K:NAV1_RADIO_FRACT_DEC` [SDK-RADE] | none | fixed image |
| 3,4 | `MHZ-` | Simple Button | T5 | `K:NAV2_RADIO_WHOLE_DEC` [SDK-RADE] | none | fixed image |
| 3,5 | `KHZ-` | Simple Button | T5 | `K:NAV2_RADIO_FRACT_DEC` [SDK-RADE] | none | fixed image |
| 3,6 | `MHZ-` | Simple Button | T5 | `K:COM2_RADIO_WHOLE_DEC` [SDK-RADE] | none | fixed image |
| 3,7 | `KHZ-` | Simple Button | T5 | `K:COM2_RADIO_FRACT_DEC` [SDK-RADE] | none | fixed image |
| 3,8 | | Empty | | | | |
| 4,1 | | Empty | | | | |
| 4,2 | | Empty | | | | |
| 4,3 | | Empty | | | | |
| 4,4 | | Empty | | | | |
| 4,5 | | Empty | | | | |
| 4,6 | `MIC1` | Dynamic Button | T2 | `K:PILOT_TRANSMITTER_SET:0` [SDK-RADE] | `(A:COM TRANSMIT:1, Bool)` [SDK-RADV] | On/Off image |
| 4,7 | `MIC2` | Dynamic Button | T2 | `K:PILOT_TRANSMITTER_SET:1` [SDK-RADE] | `(A:COM TRANSMIT:2, Bool)` [SDK-RADV] | On/Off image |
| 4,8 | | Empty | | | | |

## What the keys do

- **NAV1, NAV2** (1,2, 1,4) show the active frequency of their NAV radio on top (bold) and the standby
  frequency below (a COM Radio key, README 2.3), in MHz with Format `2` (two decimals, e.g. `110.50`: NAV
  channels run 108.00 to 117.95 in 50 kHz steps, so two decimals are exact). A press sends
  `K:NAV1_RADIO_SWAP` / `K:NAV2_RADIO_SWAP` ("Swap between the chosen NAV frequency and the corresponding
  standby frequency.", SDK-RADE).
- **COM2** (1,6) the same for COM2, Format `3` as the COM1 keys (`118.000`; this shows 25 kHz and 8.33 kHz
  channels). A press sends `K:COM2_RADIO_SWAP` ("Swaps COM 1/2/3 frequency with the standby frequency.").
- **NAV1 ID, NAV2 ID** (1,3, 1,5) show the ident of the station tuned on that NAV radio (`NAV IDENT`, "ICAO
  code.", a String SimVar shown as text, as the COM1 pad's STBY ID). **COM2 ID** (1,7) shows `COM ACTIVE FREQ
  IDENT` of COM2 ("The identity of the station that is tuned on the indexed active COM radio."). They may stay
  empty where the sim has no ident.
- **MHZ+ / MHZ-** (rows 2 and 3, the left column of each block) step the radio by 1 MHz: `NAVn_RADIO_WHOLE_INC`
  / `_DEC` ("by one MHz"), `COM2_RADIO_WHOLE_INC` / `_DEC` ("by 1 MHz. Values are from 118 to 137, and this will
  wrap if the values go under 118.").
- **KHZ+ / KHZ-** (the right column of each block) step the kHz part: `NAVn_RADIO_FRACT_INC` / `_DEC`
  ("by 25 KHz"; only the `_CARRY` variants say they carry, so no carry into the MHz is expected) and
  `COM2_RADIO_FRACT_INC` / `_DEC` ("by 25 KHz, with no carry when digit wraps"). The real step is open (A-8).
- **MIC1 / MIC2** (4,6, 4,7) select the COM radio the pilot transmits on: `K:PILOT_TRANSMITTER_SET:0` (COM1)
  and `:1` (COM2) ("0: Com1", "1: Com2", SDK-RADE). Each key is lit while `COM TRANSMIT` of its COM is 1
  ("Audio panel transmit status of the indexed COM.", SDK-RADV), so the lit key is the one the sim
  transmits on, whichever way it was selected.
- **The keys are lit and read from the sim only.** The readouts show sim values; a refused or ignored press
  changes nothing on them (the deck never assumes it worked).
- With no sim the plugin is Idle and the keys show a static preview; with the sim but no flight every key
  shows the plugin's Wait image ([phase2-main-page.md](phase2-main-page.md)).

**Open points the hand test decides (Unverified):**

- **A-7: which frequency the steps change.** The SDK says only "the chosen NAV frequency" for
  `NAVn_RADIO_WHOLE/FRACT_*` and "COM 1/2/3 frequency" for `COM2_RADIO_WHOLE/FRACT_*`; no source says whether
  that is the active or the standby one. This page expects the **standby** (the working value).
  Checklist step 2 records which frequency changes.
- **A-8: the kHz step.** The SDK text for `FRACT_INC` / `_DEC` is "by 25 KHz" (NAV and COM); for the NAV
  `_CARRY` variant it is "by 50 KHz, and will carry when the value wraps". NAV channels are 50 kHz apart, so
  a 50 kHz NAV step is expected; COM2 is expected to step 25 kHz in 25 kHz mode. The step the sim really
  takes is what checklist step 2 records. **8.33 kHz COM spacing is not handled** (see "Not on this page").

## What each key holds

Every key is a copy of a template with only these fields changed (the generator does this).

- **T4** (NAV1, NAV2, COM2): the main page's COM Radio key (COM1 at 3,1; template `com_radio`,
  [phase2-main-page.md](phase2-main-page.md), "T4: COM Radio"): Active and Standby addresses and Format from
  the table, Command Type K-Var (`ActionType` 16) with the swap event as Command Address.
- **T3** (NAV1 ID, NAV2 ID, COM2 ID): the main page's Display Value, no command: Value Address from the table,
  Format empty (the value is a string).
- **T5** (MHZ+/-, KHZ+/-): the main page's Simple Button with a K-event command (`ActionType` 16), Background
  image `Images/Switch.png`, Draw Box off.
- **T2** (MIC1, MIC2): the Phase 1 AP key's Dynamic Button (K-event command, On `1` / Off `0` states) with the
  command and Value Address from the table.

## Which route each key uses, and why

In MSFS 2024 aircraft a cockpit control may drive an input event (B-Var) and a different SimVar index than
the standard K-event (the battery precedent, [aircraft-mappings.md](aircraft-mappings.md)). The 2024 C172
G1000's input events for the radios ([reference/InputEvents-C172-G1000.txt](reference/InputEvents-C172-G1000.txt))
are the G1000 knobs and buttons: `B:as1000_nav_large_pfd` (IE 95), `B:as1000_nav_small_pfd` (IE 99),
`B:as1000_nav_switch_pfd` (IE 101), `B:as1000_com_large_pfd` (IE 48), `B:as1000_com_small_pfd` (IE 52),
`B:as1000_com_switch_pfd` (IE 57), and the audio panel's `B:as1000_com_1_mic_midcom` / `B:as1000_com_2_mic_midcom`
(IE 41, 43). The knobs and the swap button act on **whichever radio the cyan tuning box has selected** (one NAV
knob for NAV1 and NAV2, one COM knob for COM1 and COM2), so they can't target NAV2 or COM2 on their own, and
the value a push needs is unknown ("push value unknown", aircraft-mappings.md). The K-events name the radio
index directly, so every key uses a K-event and reads the indexed SimVars.

| Key | Route | Reason |
|---|---|---|
| NAV1, NAV2, COM2 (swap) | `K:NAV1_RADIO_SWAP`, `K:NAV2_RADIO_SWAP`, `K:COM2_RADIO_SWAP` | The event names its radio; the B-Var swap (IE 101, 57) acts on the selected radio and needs an unknown value. |
| MHZ+/-, KHZ+/- | `K:NAVn_RADIO_WHOLE/FRACT_INC/DEC`, `K:COM2_RADIO_WHOLE/FRACT_INC/DEC` | The same reason: the knob input events (IE 95, 99, 48, 52) tune the selected radio. Open: A-7 (standby or active) and A-8 (step). |
| Readouts and idents | SimVar reads, NAV index 1 and 2, COM index 2 | `NAV ACTIVE/STANDBY FREQUENCY` and `NAV IDENT` take "NAV Index (1-4)", the COM SimVars a "Com Index" of 1 to 3 (SDK-RADV); COM1 already reads index 1 (main 3,1). **A-6:** that index 1 / 2 are the PFD's NAV1 / NAV2 and index 2 its COM2 is Unverified; the readouts show it (checklist step 1). |
| MIC1, MIC2 | `K:PILOT_TRANSMITTER_SET:0` / `:1`, lit from `COM TRANSMIT:1` / `:2` | SDK-RADE says of `COM1_TRANSMIT_SELECT` / `COM2_TRANSMIT_SELECT` "See PILOT_TRANSMITTER_SET instead."; the audio panel's input events (IE 41, 43) need an unknown value. **A-9**, Unverified. |

## Not on this page, and why

| Function | Why not now |
|---|---|
| COM1 tuning and swap | Already on the main page (`COM1` 3,1) and the COM1 pad (MORE 1,5 `COM PAD`, [phase2-com1-pad.md](phase2-com1-pad.md)); this page adds only MIC1. |
| 8.33 kHz COM steps | `COM2_RADIO_FRACT_*` steps 25 kHz (SDK-RADE); the 8.33 kHz mode (`COM SPACING MODE`, SDK-RADV) is not handled. The COM2 readout still shows an 8.33 kHz channel (Format `3`). |
| NAV3/NAV4, ADF, DME | The SDK allows NAV index 1 to 4, but the aircraft's audio panel lists NAV1 and NAV2 only (IE 90, 91); ADF and DME keys are not built. |
| Frequency entry by number for COM2, NAV1/2 | The COM1 pad's script would need an index; not built (the steps tune them). |
| Audio panel receive and NAV audio keys | Not built (`COM1_RECEIVE_SELECT` and the audio panel input events, IE 42, 44, 90, 91, are not used). |
| Knob and swap images from the icon pack | Personal use only; in the local icon build ([icons.md](icons.md)). |

## Fallbacks

Use one only if the checklist shows the main route doesn't work, and say which one you used. None is tested,
and none is built.

| Key | Fallback | Source |
|---|---|---|
| NAV1/NAV2/COM2 show another radio's frequencies (or none) | Change the SimVar and event index in `tools/profilegen/c172-g1000.json` and in this doc (A-6) | SDK-RADV |
| MHZ/KHZ keys change the **active** frequency (A-7) | A new script `XL24-RADIOSTEP.lua` that reads the standby and sends `K:NAVn_STBY_SET_HZ` / `K:COM2_STBY_RADIO_SET_HZ` ("Sets the chosen NAV standby frequency (Hz).", "Sets COM 1/2/3 standby frequency in Hz."), with its own ruling; else the step keys go Empty | SDK-RADE |
| KHZ keys step the wrong amount (A-8) | The `_CARRY` variants (`K:NAVn_RADIO_FRACT_INC_CARRY` / `_DEC_CARRY`, "by 50 KHz, and will carry when the value wraps"; `K:COM2_RADIO_FRACT_INC_CARRY` / `_DEC_CARRY`), or a note in this doc | SDK-RADE |
| COM2 readout wrong | Read it as BCD16, as the COM1 keys' fallback (phase2-main-page.md) | SDK-RADV, SDK-UNITS |
| An ident key stays empty | The key goes Empty in a repair | SDK-RADV |
| MIC1/MIC2 don't select (A-9) | First `K:COM1_TRANSMIT_SELECT` / `K:COM2_TRANSMIT_SELECT`; then the input events `B:as1000_com_1_mic_midcom` / `B:as1000_com_2_mic_midcom` (IE 41, 43), after the scmon check in the checklist shows a readable value; if the `COM TRANSMIT` read fails, Simple Buttons (no light) | SDK-RADE; IE; tools/scmon |

## How to test

Run [tests/manual-checklist.md](../tests/manual-checklist.md), section "P3-2b: Radios page (C172 G1000)". As
on the other pages, check the reverse direction too: **turn the G1000's NAV and COM knobs and press the audio
panel's MIC buttons with the mouse, and check that the readouts and the MIC keys follow without a key being
pressed.**

## When it passes

1. Any change found in the test goes into `tools/profilegen/c172-g1000.json` and this doc; then the profile
   is regenerated (not exported from the app) and imported again.
2. Fill in the "Verified" column of the radios rows in aircraft-mappings.md with the date and sim version,
   for each function that passed.

## Sources

| Tag | Source |
|---|---|
| SDK-RADE | MSFS 2024 SDK, Key events "Aircraft Radio Navigation Events", https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-radio-navigation-events/ (`NAV1_RADIO_SWAP` "Swap between the chosen NAV frequency and the corresponding standby frequency."; `NAV1_RADIO_WHOLE_INC` "Increments the chosen NAV frequency by one MHz."; `NAV1_RADIO_FRACT_INC` "by 25 KHz"; `NAV1_RADIO_FRACT_INC_CARRY` "by 50 KHz, and will carry when the value wraps"; NAV2 the same; `NAV1_STBY_SET_HZ`; `COM2_RADIO_SWAP` "Swaps COM 1/2/3 frequency with the standby frequency."; `COM2_RADIO_WHOLE_INC` "by 1 MHz. Values are from 118 to 137"; `COM2_RADIO_FRACT_INC` "by 25 KHz, with no carry when digit wraps"; `COM2_RADIO_FRACT_INC_CARRY` / `_DEC_CARRY` "by 25 KHz, and carry when digit wraps" and `NAV1_RADIO_FRACT_DEC_CARRY` "Decrement the chosen NAV frequency by 50 KHz" (the `_CARRY` names rechecked 2026-11-14 for P3-2b); `COM2_STBY_RADIO_SET_HZ`; `COM1_TRANSMIT_SELECT` / `COM2_TRANSMIT_SELECT` "See PILOT_TRANSMITTER_SET instead."; `PILOT_TRANSMITTER_SET` "[0]: The Com channel to select.", "0: Com1", "1: Com2"), read 2026-11-14 |
| SDK-RADV | MSFS 2024 SDK, SimVars "Radio Navigation Variables", https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-radio-navigation-variables/ (`NAV ACTIVE FREQUENCY` / `NAV STANDBY FREQUENCY` "NAV Index (1-4)", MHz; `NAV IDENT` "ICAO code.", String; `COM ACTIVE FREQUENCY` / `COM STANDBY FREQUENCY` "Com Index", "Frequency BCD16", read in MHz as the COM1 keys; `COM TRANSMIT` "Audio panel transmit status of the indexed COM.", Bool; `COM ACTIVE FREQ IDENT` "The identity of the station that is tuned on the indexed active COM radio.", String; `COM SPACING MODE` "Enum: 0 = 25kHz, 1 = 8.33kHz"), read 2026-11-14 |
| SDK-UNITS | MSFS 2024 SDK, "Simulation Variable Units", as in phase2-main-page.md |
| README | PilotsDeck README, https://github.com/Fragtality/PilotsDeck/blob/master/README.md: 2.1.1 (address forms: A-Var `(Prefix:Name(:index), Unit)`, KVAR with up to five positive whole-number parameters), 2.2.2 (Format), 2.3 (COM Radio: Active on top, Standby below) |
| PD-SRC | PilotsDeck source, https://github.com/Fragtality/PilotsDeck/blob/11bdf1f7daf4828f822c18919952fe5b66153e58/Plugin/Simulator/MSFS/SubMapping.cs (`OnReceived`: a value that is not numeric is stored as text with `GetString()`; the file does not say which units count as not numeric, so a `String` A-Var shown as text is Unverified, as the COM1 pad's STBY ID); `Plugin/Tools/TypeMatching.cs` in the same commit (`rxAvar` accepts any unit word) |
| PD-PI | The installed plugin's settings panel, `%APPDATA%\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\Plugin\PI\js\pi-Common.js` (line 189 `regAvar`, 195 `rxKvarCmd` accepts `K:PILOT_TRANSMITTER_SET:0`, 231 type 16), read 2026-11-14 |
| IE | [reference/InputEvents-C172-G1000.txt](reference/InputEvents-C172-G1000.txt) (IE n = line n: 41, 43 the audio panel MIC buttons; 48, 52, 57 the PFD COM knobs and swap; 95, 99, 101 the PFD NAV knobs and swap) |
| Leads | Jiblet's C172 G1000 profile for the SD+XL (pre-2024: NAV/COM dials on `NAVn_RADIO_WHOLE/FRACT_*`, `COM2_RADIO_WHOLE/FRACT_*` and `_SWAP`); TorontoWill's generic profile (`NAV1_RADIO_SWAP`). Leads only; every name above is confirmed in the SDK; nothing copied. |
