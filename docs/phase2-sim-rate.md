# Phase 2: Sim rate page, Cessna 172 G1000

**Status: untested (not yet sim-tested).** Nothing on this page has been tried in the sim yet. The first
test is **HT-1**, the short hand test at the start of the checklist section "Phase 2: Sim rate page (C172
G1000)": it checks that `K:SIM_RATE_SET` with a parameter sets the rate and that the rate can be read.
Every new name below is recorded as "Unverified" in [aircraft-mappings.md](aircraft-mappings.md) until
HT-1 and the sim rate checks pass.

Goal: keys that set the simulation rate to **1x (normal), 2x and 4x**, each lit only when the sim's actual
rate (read from the sim) is its rate, plus a **RATE** readout that also steps the rate up and down. The
user asked for "2x, 4x, normal" as easy toggles. The keys sit on a new child page **simrate**, opened by
the main page's folder key `SIM RATE` at 3,7 (that position was reserved for a timer; see
[navigation.md](navigation.md), "Pages", the note on reserved positions below the table).

The page is part of the generated profile `MSFS2024 C172 G1000` (same file, same name, same import as
the main page: see [phase2-main-page.md](phase2-main-page.md), "Import the profile"). The table below is
the reference for what each key holds; `tools/profilegen/check.py` compares the profile with the
"Key table: simrate" section key by key. How the pages connect: [navigation.md](navigation.md).

Positions are **row,column**, 1-based, row 1 at the top. **1,1 is the back key** (it returns to the main
page), as on every child page. Templates T2 and T3 are the main page's (see
[phase2-main-page.md](phase2-main-page.md), "What each key holds"); no new template.

Nothing on this page uses keyboard bindings, vJoy or anything tied to a controller: the keys send
SimConnect events (K-events) and read a sim variable, so they work the same with the Xbox Elite controller
and the T.16000M + TWCS.

## Layout: simrate

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | 1X | 2X | 4X | RATE | | | |
| **Row 2** | | | | | | | | |
| **Row 3** | | | | | | | | |
| **Row 4** | | | | | | | | |

## Key table: simrate

Action names as in phase2-main-page.md. **Back** = the Stream Deck app's back key (`backtoparent`), added
by the generator on every child page. "Empty" = no action on that key.

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to the main page | none | Back key |
| 1,2 | `1X` | Dynamic Button | T2 | `K:SIM_RATE_SET:1` [SDK-MISCE, README 2.1.1, LR161-C4] | `(A:SIMULATION RATE, number)` [SDK-ENVV, PD-SRC] | On/Off image: On `1`, Off `2` |
| 1,3 | `2X` | Dynamic Button | T2 | `K:SIM_RATE_SET:2` [SDK-MISCE, README 2.1.1, LR161-C4] | `(A:SIMULATION RATE, number)` [SDK-ENVV, PD-SRC] | On/Off image: On `2`, Off `1` |
| 1,4 | `4X` | Dynamic Button | T2 | `K:SIM_RATE_SET:4` [SDK-MISCE, README 2.1.1, LR161-C4] | `(A:SIMULATION RATE, number)` [SDK-ENVV, PD-SRC] | On/Off image: On `4`, Off `1` |
| 1,5 | `RATE` | Display Value | T3 | Main `K:SIM_RATE_INCR`, Second (long press) `K:SIM_RATE_DECR` [SDK-MISCE, README 2.1] | `(A:SIMULATION RATE, number)` [SDK-ENVV, PD-SRC] | Format `1.2` |
| 1,6 | | Empty | | | | |
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

### What the keys do

- **1X, 2X, 4X** send `K:SIM_RATE_SET` with the rate as its parameter: `K:SIM_RATE_SET:1`, `:2`, `:4`.
  The SDK lists the event with one parameter, "[0] Value", and the description "Set the simulation rate."
  (SDK-MISCE); it does **not** say what the value means (the rate itself or a scaled value) or its range.
  Parameter = the rate is the working value, ruled for an Unverified build (LR161-C4); HT-1 checks it.
  PilotsDeck sends the part after the second colon as an unsigned whole number (README 2.1.1 K-Var form
  `(K:)Name(:Parameter)`, "positive integer Value"; PD-SRC `ToolsMSFS.cs` WriteKvar), so 1, 2 and 4 can be
  sent, fractions such as 0.5 can't.
- **RATE** shows the sim's rate with two decimals (Format `1.2`: `1.00`, `2.00`, `0.50`, `0.06` for
  0.0625). A press sends `K:SIM_RATE_INCR` ("Increase the simulation rate"), a long press (>= 500 ms)
  `K:SIM_RATE_DECR` ("Decreases the simulation rate") (SDK-MISCE). One press is one step of the sim's
  own rate series. RATE is the hedge if `K:SIM_RATE_SET`'s value turns out not to be the rate: the rate
  can still be stepped from the deck.
- **Every key reads the sim.** All four read the environment variable `SIMULATION RATE` (SDK-ENVV: "clamped
  between 0.0625 and 128", "a value of 1 means that 1 second of game time is the same as 1 second of
  "real" time", values 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, ... 128). The address is the A: form
  `(A:SIMULATION RATE, number)`: README 2.1.1 names `E:` for environment variables; PilotsDeck treats
  `A:` and `E:` alike (PD-SRC `TypeMatching.cs`, one pattern for both) and subscribes the variable by its
  bare name (PD-SRC `SubManager.cs`), so it is the same request as `(E:SIMULATION RATE, number)`, and
  `E:` is the fallback (LR161-C4, A-6). A key lights because the sim reports the rate, not because it
  was pressed.

What the keys show:

| Sim rate | 1X | 2X | 4X | RATE |
|---|---|---|---|---|
| 1x | On | Off | Off | `1.00` |
| 2x | Off | On | neither image | `2.00` |
| 4x | neither image | neither image | On | `4.00` |
| 0.5x, 0.25x, 8x, 16x ... | neither image | neither image | neither image | `0.50`, `0.25`, `8.00`, `16.00` |
| paused | not in the sources (the SDK says nothing about the rate while paused): the checklist records it | | | |

"Neither image" = the key shows only its background: a Dynamic Button whose read value matches neither
its On nor its Off value, with Special State off, draws no On/Off image (PD-SRC `ActionSwitchDisplay.cs`,
`Refresh()`; as on the views page COCKPIT and EXTERNAL keys, [phase2-trim-views.md](phase2-trim-views.md)).
So exactly one of 1X, 2X and 4X is lit at 1x, 2x or 4x, and none at any other rate.

**Not on this page, and why:**

| Function | Why not | Source |
|---|---|---|
| `K:SIM_RATE` | "Selects the simulation rate. Use the PLUS and MINUS events to increment/decrement the value": a select mode plus a second event; `K:SIM_RATE_INCR` / `_DECR` step the rate directly. | SDK-MISCE |
| Pause (`K:PAUSE_TOGGLE`, `K:PAUSE_ON`, `K:PAUSE_OFF`, `K:PAUSE_SET`) | Not asked for. | SDK-MISCE |
| Writing `SIMULATION RATE` directly (an E-Var / A-Var write) | The SDK marks it get/set, but this unit uses no A-Var or E-Var write for the sim rate (LR153-C4). | SDK-ENVV; LR153-C4 |
| The FSUIPC offset `0x0C1A` (rate x 256; a reference profile writes 256 for 1x and 1024 for 4x) | Not a K-event: ruled out (LR153-C4). Recorded only, and used as a lead for HT-1's 512 / 1024 step. | lead only (a saved reference profile, not copied) |
| A Toggle Switch form (press again = back to 1x) | No real saved key with Toggle Switch on and a K-event command exists on this PC, so there is no example to copy. | brief scan (P2-6 research) |

## Sources

| Tag | Source |
|---|---|
| SDK-MISCE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/miscellaneous-events/ ("Sim Rate": `SIM_RATE`, `SIM_RATE_DECR`, `SIM_RATE_INCR`, `SIM_RATE_SET` "[0] Value") |
| SDK-ENVV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/environment-variables/ (`SIMULATION RATE`, unit Number; not on any SimVar page) |
| README | PilotsDeck README, https://github.com/Fragtality/PilotsDeck/blob/master/README.md (2.1.1 K-Var address `(K:)Name(:Parameter)` with the example `K:FUELSYSTEM_PUMP_TOGGLE:3`, A-Var/E-Var address form; 2.1 Main and Second (long press) command; Display Value Format `Zeros.Fraction`) |
| PD-SRC | PilotsDeck source, https://github.com/Fragtality/PilotsDeck/blob/11bdf1f7daf4828f822c18919952fe5b66153e58/ `Plugin/Tools/TypeMatching.cs` (A: and E: read alike), `Plugin/Simulator/MSFS/SubManager.cs` (subscribed by the bare name), `Plugin/Simulator/MSFS/ToolsMSFS.cs` (WriteKvar: each parameter sent as an unsigned whole number), `Plugin/Actions/Simple/ActionSwitchDisplay.cs` (which image a Dynamic Button shows) |
| PD-PI | The installed plugin's settings panel, `%APPDATA%\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\Plugin\PI\js\pi-Common.js` line 195 (`rxKvarCmd`: a K-Var command address may carry up to five numeric parameters) |
| LR161-C4 | The coordinator's ruling in the project's chain ledger (2026-11-12): build 1X/2X/4X on `K:SIM_RATE_SET:1/2/4` now, Unverified, with HT-1 as the first checklist item. No saved key with a K-event parameter exists yet; HT-1 (a user hand test) is still to run. |
| LR97-C2 | The trim keys' sim test (2026-11-11): the K-Var command type (16) works from the deck (`K:ELEV_TRIM_UP` / `_DN`). |
| LR153-C4 | The coordinator's ruling: no A-Var or E-Var write for the sim rate; K-events from the SDK; every indicator reads the rate. |

## What each key holds

Every key is a copy of a template with only these fields changed (the generator does this; by hand only
when you change a key during a test, see phase2-main-page.md "Changing a key by hand").

**T2 Dynamic Button with a K-event** (copy of the Phase 1 AP key, as HDG on the main page): Commands tab
Command Type MSFS: K-Var (SimEvent), Command Address as below, On/Off Value empty, Toggle Switch unchecked;
Value tab Address `(A:SIMULATION RATE, number)`; On/Off States On Value / Off Value as below, On/Off images
`Images/KorryOnBlueTop.png` / `Images/KorryOffWhiteBottom.png` (as AP).

| Pos | Commands: Command Address | Value: Address | On/Off States: On Value / Off Value | Title |
|---|---|---|---|---|
| simrate 1,2 | `K:SIM_RATE_SET:1` | `(A:SIMULATION RATE, number)` | `1` / `2` | `1X` |
| simrate 1,3 | `K:SIM_RATE_SET:2` | `(A:SIMULATION RATE, number)` | `2` / `1` | `2X` |
| simrate 1,4 | `K:SIM_RATE_SET:4` | `(A:SIMULATION RATE, number)` | `4` / `1` | `4X` |

The K-Var command type is the one the committed AP, trim and FLAPS keys use (sim-tested on the trim keys,
LR97-C2). The parameter after the event name is address syntax (README 2.1.1; the settings panel accepts it,
PD-PI line 195). There is no real saved key with a K-event parameter on this PC yet; HT-1 makes one by hand.
If the settings panel shows or saves the address in another form than `K:SIM_RATE_SET:2`, record it: the
data file then uses the saved form.

**T3 Display Value with a Main and a Second command** (copy of the Phase 1 HDG key, the same fields as
FLAPS on the main page): Value tab Address `(A:SIMULATION RATE, number)`, Format `1.2`, Mappings empty,
Decode BCD unchecked; Main Command MSFS: K-Var (SimEvent) `K:SIM_RATE_INCR`; long press (`HasLongPress`)
enabled; Second Command MSFS: K-Var (SimEvent) `K:SIM_RATE_DECR`; On/Off Values empty; Title `RATE`
(simrate 1,5).

## Fallbacks

Use one only if the checklist shows the main route doesn't work, and say which one you used. None is
tested; they are recorded in aircraft-mappings.md too. The repair after the test rules which one is built.

| Key | Fallback | Source |
|---|---|---|
| 1X / 2X / 4X: no change or a wrong rate | HT-1's scale step: the value x256 (`K:SIM_RATE_SET:512` for 2x, `:1024` for 4x), as the FSUIPC offset 0x0C1A stores the rate. A lead only; nothing in the build uses it. | LR161-C4; lead (FSUIPC offset) |
| 1X / 2X / 4X: `K:SIM_RATE_SET` ignored, RATE's press and long press work | Stepping: a Lua key script that reads the rate and sends `K:SIM_RATE_INCR` / `_DECR` until it equals the target (PilotsDeck LUAFUNC command, `lua:File:Function(...)`). Not built (LR161-C4: only if HT-1 fails both scales). | README 2.1.1, Lua section; SDK-MISCE |
| All four keys: the read shows nothing, `0` or a stuck value while the rate visibly changes | `(E:SIMULATION RATE, number)` in the Value Address (the same request per PD-SRC, so if it fails too, report it: the calculator form is untested here) | README 2.1.1; SDK-ENVV |
| All: the sim ignores every sim rate K-event (log shows the sends, nothing changes) | None left under LR153-C4 (no E-Var write, no FSUIPC offset); RATE stays as a readout and the coordinator decides. | LR153-C4 |

## How to test

Run [tests/manual-checklist.md](../tests/manual-checklist.md), section "Phase 2: Sim rate page (C172
G1000)": HT-1 first, then the import and the page checks. As on the other pages, the important direction is
the reverse one: **change the rate with the sim's own control and check that RATE and the lit key follow
without a key being pressed.**

## When it passes

1. Any change found in the test (the parameter scale, the read address, a saved address form) goes into
   `tools/profilegen/c172-g1000.json` and this doc; then the profile is regenerated (not exported from the
   app) and imported again.
2. Fill in the "Verified" column of the sim rate rows in aircraft-mappings.md with the date and sim
   version, for each key that passed. Mark an event "does not work" if the sim ignored it.
