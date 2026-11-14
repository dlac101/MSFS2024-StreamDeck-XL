# Phase 2: Sim rate page, Cessna 172 G1000

**Status: repaired (P2-6R), not yet sim-tested.** The first sim test (2026-11-12) found two faults: the
1X/2X/4X keys (`K:SIM_RATE_SET:1/2/4`) did not change the rate ("the simrate buttons arent changing sim
rate in game", LR259-C5), and `RATE` stepped the rate up to 128x but never back down ("rate button worked,
took me all the way to 128x but never back down", LR263-C5). After that the user asked for a new layout
(LR298-C5): a faster and a slower key, the RATE readout, and "a dedicated 1x button, to try to return to
normal speed in one press, if possible". This version, left to right:

- **1X** (1,2) runs a Lua script, `XL24-SIMRATE.lua`, that steps the rate with `K:SIM_RATE_INCR` /
  `K:SIM_RATE_DECR` until the rate read from the sim is 1x (see "What the keys do").
  The script must be **installed once** (see "Install the script").
- **SLOWER** (1,3): one press = one step down (`K:SIM_RATE_DECR`), so the way down never depends on hold
  timing or on the script.
- **RATE** (1,4) is unchanged. Its long press was set up right, but no press was held long enough: PilotsDeck
  runs the long press only after **0.5 s**, and every press in the plugin log was held 0.06 to 0.25 s.
  **Hold RATE a full second** to step down.
- **FASTER** (1,5): one press = one step up (`K:SIM_RATE_INCR`).
- The **2X** and **4X** keys are removed (the user lists only faster, slower, rate and 1x,
  LR298-C5). 1,6 is empty.

The first checks are the hand test **HT-C** at the start of the checklist section "Phase 2: Sim rate page
(C172 G1000)" (HT-A, the step size, is answered by the user's report: steps of x2 up to 128x, LR298-C5).
Every name below is recorded as "Unverified" in [aircraft-mappings.md](aircraft-mappings.md) until the sim
rate checks pass.

Goal: a **1X** key that sets the simulation rate back to **1x (normal)** in one press, lit only when the
sim's actual rate (read from the sim) is 1x, **SLOWER** and **FASTER** keys that step the rate down and up,
and a **RATE** readout that also steps the rate up and down. The user first asked for "2x, 4x, normal" as
easy toggles (P2-6); the layout above is the user's own after the first sim test (LR298-C5). The keys sit on
a child page **simrate**, opened by the main page's folder key `SIM RATE` at 3,7 (that position was reserved
for a timer; see [navigation.md](navigation.md), "Pages", the note on reserved positions below the table).

The page is part of the generated profile `MSFS2024 C172 G1000` (same file, same name, same import as
the main page: see [phase2-main-page.md](phase2-main-page.md), "Import the profile"), plus **one script file
to install** (below). The table below is the reference for what each key holds; `tools/profilegen/check.py`
compares the profile with the "Key table: simrate" section key by key. How the pages connect:
[navigation.md](navigation.md).

Positions are **row,column**, 1-based, row 1 at the top. **1,1 is the back key** (it returns to the main
page), as on every child page. Templates T2, T3 and T5 are the main page's (see
[phase2-main-page.md](phase2-main-page.md), "What each key holds"); no new template.

Nothing on this page uses keyboard bindings, vJoy or anything tied to a controller: the keys send
SimConnect events (K-events), directly or from the Lua script, and read a sim variable, so they work the
same with the Xbox Elite controller and the T.16000M + TWCS.

## Install the script (once)

The 1X key calls the function `SET` of the standard script
`pilotsdeck/MSFS2024-XL/_Package/Scripts/XL24-SIMRATE.lua`. PilotsDeck reads scripts from its own Scripts
folder (README 3.5), so the file must be there before this key can work. Signed in as Admin, either:

- copy the file into `%APPDATA%\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\Scripts\`
  (the plugin loads new and changed scripts while it runs; no restart needed, README 3.5) (if the sim
  rate page was open while you copied it, go back and open the page again), or
- build and install the package with the Profile Manager (README.md, "Building the package"), which puts
  `Scripts/` files in the same place.

After any change to the script in the repo, copy it again. Without the file, 1X does nothing and the
plugin log says the script is not registered ("The Script ... is not registered or running", PD-SRC
`ScriptManager.cs`). RATE, SLOWER and FASTER don't need the script.

## Layout: simrate

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | < back | 1X | SLOWER | RATE | FASTER | | | |
| **Row 2** | | | | | | | | |
| **Row 3** | | | | | | | | |
| **Row 4** | | | | | | | | |

## Key table: simrate

Action names as in phase2-main-page.md. **Back** = the Stream Deck app's back key (`backtoparent`), added
by the generator on every child page. "Empty" = no action on that key. Commands starting `lua:` are
command type **Lua Function** (saved as `14`; PD-SRC `SimCommand.cs`, PD-PI line 227).

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | | Back | (Stream Deck) | Returns to the main page | none | Back key |
| 1,2 | `1X` | Dynamic Button | T2 | `lua:XL24-SIMRATE:SET(1)` (steps `K:SIM_RATE_INCR` / `K:SIM_RATE_DECR`) [README 2.1.1 LUAFUNC, 3.5.1; SDK-MISCE; LR153-C4] | `(A:SIMULATION RATE, number)` [SDK-ENVV, PD-SRC] | On/Off image: On `1`, Off `2` |
| 1,3 | `SLOWER` | Simple Button | T5 | `K:SIM_RATE_DECR` [SDK-MISCE] | none | fixed image |
| 1,4 | `RATE` | Display Value | T3 | Main `K:SIM_RATE_INCR`, Second (long press) `K:SIM_RATE_DECR` [SDK-MISCE, README 2.1] | `(A:SIMULATION RATE, number)` [SDK-ENVV, PD-SRC] | Format `1.2` |
| 1,5 | `FASTER` | Simple Button | T5 | `K:SIM_RATE_INCR` [SDK-MISCE] | none | fixed image |
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

- **1X** runs `SET(1)` in `XL24-SIMRATE.lua`. PilotsDeck runs the command `lua:XL24-SIMRATE:SET(1)` as the
  Lua code `SET(1)` (PD-SRC `ScriptManager.cs` `RunFunction`; it runs only while the sim is connected).
  `SET` reads the rate, sends **one** `K:SIM_RATE_DECR` (rate above 1x) or `K:SIM_RATE_INCR` (rate below
  1x), waits until the read rate changes, and repeats until the rate is 1x. Both events take no parameter
  ("Increase the simulation rate ...", "Decreases the simulation rate ...", SDK-MISCE). Each step is one
  step of the sim's own rate series: the sim steps by **x2** up to 128x (the user's report, "constantly
  doubling from 2x till then", LR298-C5; SDK-ENVV lists the rates 0.0625, 0.125, ... 128), so 128x to 1x
  is 7 steps and the slowest rate, 0.0625x, to 1x is 4. Limits (the script never runs away):
  - at most **8 events per press** (128x to 1x is 7 steps of x2);
  - the next event only after the read rate changed; if it doesn't change within **2 s**, the script stops;
  - it stops when the rate passes 1x (it should not, with steps of x2), when no rate is read (a press at the
    moment the page opens, `RATE` still blank: press again), or after 8 steps;
  - a press while a run is still going is ignored (two quick presses don't run twice);
  - each stop writes one line to the plugin's `lua.log` (`XL24-SIMRATE: ... stopped`).
- **SLOWER** sends `K:SIM_RATE_DECR` on every press: one step down, no hold needed, no script. It is the
  safe way down (press it until RATE shows `1.00`, or press 1X). It is a Simple Button with a fixed
  image, like the main page's ATC key (T5), the form of the sim-tested TRIM UP/DN keys (LR97-C2).
- **RATE** shows the sim's rate with two decimals (Format `1.2`: `1.00`, `2.00`, `0.50`, `0.06` for
  0.0625). A press sends `K:SIM_RATE_INCR` ("Increase the simulation rate"), a long press
  `K:SIM_RATE_DECR` ("Decreases the simulation rate") (SDK-MISCE). **Hold RATE a full second** for the
  long press: PilotsDeck runs the Second command only when the key was held at least `LongPressTime`,
  500 ms by default (README 2.1: "when pressed longer (>= 500ms)"; PD-SRC `ActionBaseSimple.cs` OnKeyUp,
  `ActionCommand.cs`, `AppConfiguration.cs`; the installed `PluginConfig.json` holds `"LongPressTime":
  500`). On 2026-11-12 every RATE press was held 0.06 to 0.25 s, so the long press never ran and the rate
  only went up (plugin log: "Key TimeDiff" lines, no "Build Long Command").
- **FASTER** sends `K:SIM_RATE_INCR` on every press: one step up, no script. It is SLOWER's twin (the same
  Simple Button T5, only the event and the title differ). Up to 128x (SDK-ENVV: "clamped between 0.0625
  and 128"); press SLOWER or 1X to come back.
- **Every rate indicator reads the sim.** 1X and RATE read the environment variable `SIMULATION RATE`
  (SDK-ENVV: "clamped between 0.0625 and 128", "a value of 1 means that 1 second of game time is the same
  as 1 second of "real" time", values 0.0625, 0.125, 0.25, 0.5, 1, 2, 4, ... 128). The address is the A:
  form `(A:SIMULATION RATE, number)`: README 2.1.1 names `E:` for environment variables; PilotsDeck treats
  `A:` and `E:` alike (PD-SRC `TypeMatching.cs`, one pattern for both) and subscribes the variable by its
  bare name (PD-SRC `SubManager.cs`), so it is the same request as `(E:SIMULATION RATE, number)`, and
  `E:` is the fallback (LR161-C4, A-6). 1X lights because the sim reports 1x, not because it was pressed
  or because the script ran. The script reads the same variable (README 3.5.1 `SimVar`, `SimRead`).
  SLOWER and FASTER read nothing: RATE shows what they did.

What the keys show:

| Sim rate | 1X | RATE |
|---|---|---|
| 1x | On | `1.00` |
| 2x | Off | `2.00` |
| 4x, 8x, ... 128x; 0.5x, 0.25x, 0.125x, 0.0625x | neither image | `4.00`, `8.00`, ... `128.00`; `0.50`, `0.25`, ... `0.06` |
| paused | not in the sources (the SDK says nothing about the rate while paused): the checklist records it | |

SLOWER and FASTER always show their fixed image.

"Neither image" = the key shows only its background and its title, no On or Off image: a Dynamic Button
whose read value matches neither its On nor its Off value, with Special State off, draws no On/Off image
(PD-SRC `ActionSwitchDisplay.cs`, `Refresh()`: the On image when the value matches On, else the Off image
when it matches Off, else the Special State image only when Special State is on, else no image; as on the
views page COCKPIT and EXTERNAL keys, [phase2-trim-views.md](phase2-trim-views.md)). It is not an error
image. So 1X is lit only at 1x; at 2x it shows its Off image, at every other rate no image. 1X keeps the
first build's On `1` / Off `2`.

**When the sim refuses.** If a script run stops short of 1x, 1X is not lit and RATE shows the real rate;
`lua.log` has one line saying why. If a run ever ends in a
Lua error, the script clears its "run going" flag anyway (it calls the stepping inside `pcall`, the Lua
base function, which PilotsDeck's NeoLua engine provides: PD-SRC `Plugin/Plugin.csproj` references NeoLua
1.3.20-beta.1, and NeoLua `NeoLua/LuaGlobal.cs` v1.3.19 line 517 declares `[LuaMember("pcall")]`; the
installed build carries it, PD-LUA) and writes `XL24-SIMRATE: error, stopped: ...` to `lua.log`; the next
press works again.

## The script

[`pilotsdeck/MSFS2024-XL/_Package/Scripts/XL24-SIMRATE.lua`](../pilotsdeck/MSFS2024-XL/_Package/Scripts/XL24-SIMRATE.lua),
a standard script (README 3.5.1). The `XL24-` prefix keeps it apart from other packages' scripts in the
plugin's shared Scripts folder. It uses only `SimVar`, `SimRead`, `SimCommand`, `Sleep` and `Log` (README
3.5.1) and the Lua base calls `tonumber`, `tostring`, `math.abs` and `pcall`. Its one function is
`SET(n)` (any rate the SDK lists, 0.0625 to 128); the page uses only `SET(1)`. The only events it sends are
`K:SIM_RATE_INCR` and `K:SIM_RATE_DECR`; it writes no variable.

Why the waits should not hold up other keys (from the sources; the sim test confirms it): PilotsDeck
runs a Lua Function command on its own task (PD-SRC `ConnectorNone.cs`: `Task.Run(() => RunScript(command))`),
and `SimCommand` only queues the event for the plugin's command loop (PD-SRC `ManagedScript.cs`; README
3.5/3.5.1: "The execution won't block anything."), so the events the script queues are sent while it sleeps (`Sleep` is `Thread.Sleep`, PD-SRC
`ManagedScript.cs`). `SimRead` returns the plugin's current copy of the variable, which the plugin
updates each time the sim sends a new value (PD-SRC `SubMapping.cs`, OnReceived), on another thread than
the script's. PilotsDeck loads the script when a key that uses it appears and unloads it when none
is left (README 3.5; PD-SRC `RessourceStore.cs`).

## What each key holds

Every key is a copy of a template with only these fields changed (the generator does this; by hand only
when you change a key during a test, see phase2-main-page.md "Changing a key by hand").

**T2 Dynamic Button with a Lua Function command** (copy of the Phase 1 AP key, as HDG on the main page):
Commands tab Command Type **All Sims: Lua Function** (`ActionType` 14), Command Address as below, On/Off
Value empty, Toggle Switch unchecked; Value tab Address `(A:SIMULATION RATE, number)`; On/Off States On
Value / Off Value as below, On/Off images `Images/KorryOnBlueTop.png` / `Images/KorryOffWhiteBottom.png`
(as AP).

| Pos | Commands: Command Address | Value: Address | On/Off States: On Value / Off Value | Title |
|---|---|---|---|---|
| simrate 1,2 | `lua:XL24-SIMRATE:SET(1)` | `(A:SIMULATION RATE, number)` | `1` / `2` | `1X` |

The settings panel accepts these addresses (PD-PI line 196 `regLuaFunc`: `lua:` + file name + `:` +
function, optional `(...)`). A real saved Dynamic Button with a Lua Function command and a read Address
exists in the Fenix XL reference profile (REF-FNX; the saved form only, not copied).

**T3 Display Value with a Main and a Second command** (copy of the Phase 1 HDG key, the same fields as
FLAPS on the main page): Value tab Address `(A:SIMULATION RATE, number)`, Format `1.2`, Mappings empty,
Decode BCD unchecked; Main Command MSFS: K-Var (SimEvent) `K:SIM_RATE_INCR`; long press (`HasLongPress`)
enabled; Second Command MSFS: K-Var (SimEvent) `K:SIM_RATE_DECR`; On/Off Values empty; Title `RATE`
(simrate 1,4). Unchanged in P2-6R apart from its position (1,5 in the first build).

**T5 Simple Button with a K-event** (the main page's ATC key at 3,3: template `simple_button`, states from
the Phase 1 AP key, `LinkedTitle` on, Background image `Images/Switch.png`, Draw Box off): Command Type
MSFS: K-Var (SimEvent) (`ActionType` 16), Command Address `K:SIM_RATE_DECR`, Title `SLOWER` (simrate 1,3);
Command Address `K:SIM_RATE_INCR`, Title `FASTER` (simrate 1,5).

## Not on this page, and why

| Function | Why not | Source |
|---|---|---|
| `2X` and `4X` keys (`lua:XL24-SIMRATE:SET(2)`, `SET(4)`; the P2-6R build, before that `K:SIM_RATE_SET:2/4`) | Removed in P2-6R: the user's layout lists only a faster and a slower key, the rate readout and a 1x key. FASTER and SLOWER reach every rate in steps of x2. | LR298-C5 |
| `K:SIM_RATE_SET:1/2/4` (the first build of 1X/2X/4X) | Does not work as sent: every press was logged as sent with no error, and the rate did not change (2026-11-12, LR259-C5). Why is not known: the sim may ignore the event, the value may be scaled, or the parameter may not arrive. | plugin log 2026-11-12; SDK-MISCE; PD-SRC `ToolsMSFS.cs` |
| `K:SIM_RATE_SET` with the x256 scale (`:256` = 1x) | Untested, a lead only (the FSUIPC offset 0x0C1A stores the rate x256). Not tried: the hand test for it was dropped with the 2X key in P2-6R; 1X steps instead. | lead only (FSUIPC offset; a saved reference profile, not copied); LR298-C5 |
| `K:SIM_RATE` | "Selects the simulation rate. Use the PLUS and MINUS events to increment/decrement the value": a select mode plus a second event; `K:SIM_RATE_INCR` / `_DECR` step the rate directly. | SDK-MISCE |
| Pause (`K:PAUSE_TOGGLE`, `K:PAUSE_ON`, `K:PAUSE_OFF`, `K:PAUSE_SET`) | Not asked for. | SDK-MISCE |
| Writing `SIMULATION RATE` directly (an E-Var / A-Var write) | The SDK marks it get/set, but this page uses no A-Var or E-Var write for the sim rate (LR153-C4). | SDK-ENVV; LR153-C4 |
| A Toggle Switch form (press again = back to 1x) | No real saved key with Toggle Switch on and a K-event command exists on this PC, so there is no example to copy. | brief scan (P2-6 research) |

## Sources

| Tag | Source |
|---|---|
| SDK-MISCE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/miscellaneous-events/ ("Sim Rate": `SIM_RATE`, `SIM_RATE_DECR`, `SIM_RATE_INCR` (no parameter), `SIM_RATE_SET` "[0] Value"), read 2026-11-13 |
| SDK-ENVV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/environment-variables/ (`SIMULATION RATE`, unit Number; not on any SimVar page) |
| README | PilotsDeck README, https://github.com/Fragtality/PilotsDeck/blob/master/README.md (2.1 Main and Second (long press, ">= 500ms") command; 2.1.1 K-Var address `(K:)Name(:Parameter)`, A-Var/E-Var address form, LUAFUNC `lua:File:Function(Parameter)`; 3.5 standard scripts: Scripts folder, loaded on demand, reloaded when changed; 3.5.1 `SimVar`, `SimRead`, `SimCommand`, `Sleep`, `Log`; "The execution won't block anything."; Display Value Format `Zeros.Fraction`) |
| PD-SRC | PilotsDeck source, https://github.com/Fragtality/PilotsDeck/blob/11bdf1f7daf4828f822c18919952fe5b66153e58/ `Plugin/Tools/TypeMatching.cs` (A: and E: read alike), `Plugin/Simulator/MSFS/SubManager.cs` (subscribed by the bare name), `Plugin/Simulator/MSFS/SubMapping.cs` (OnReceived: updates the variable `SimRead` returns each time the sim sends a new value), `Plugin/Simulator/MSFS/ToolsMSFS.cs` (WriteKvar: each parameter sent as an unsigned whole number), `Plugin/Actions/Simple/ActionSwitchDisplay.cs` (which image a Dynamic Button shows: `Refresh()`, On, else Off, else the Special State image only with Special State on, else none), `Plugin/Actions/Simple/ActionBaseSimple.cs` (OnKeyUp: the long command only when held >= LongPressTime), `Plugin/Actions/Simple/ActionCommand.cs` and `Plugin/AppConfiguration.cs` (LongPressTime, default 500), `Plugin/Simulator/SimCommand.cs` (`LUAFUNC = 14`), `Plugin/Simulator/ConnectorNone.cs` (a Lua Function command runs on its own task), `Plugin/Resources/Scripts/ManagedScript.cs` (`SimVar`, `SimRead`, `SimCommand`, `Sleep` = `Thread.Sleep`, `Log`; the engine is NeoLua `LuaGlobal`), `Plugin/Resources/ScriptManager.cs` (`RunFunction`; "not registered or running"), `Plugin/Actions/Simple/RessourceStore.cs` (a script loads with the key that uses it) |
| PD-PI | The installed plugin's settings panel, `%APPDATA%\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\Plugin\PI\js\pi-Common.js` lines 195 (`rxKvarCmd`), 196 (`regLuaFunc`), 227 (`type == 14 //LuaFunc`) |
| PD-LUA | PilotsDeck's Lua engine is NeoLua: PD-SRC `Plugin/Plugin.csproj` `<PackageReference Include="NeoLua" Version="1.3.20-beta.1" />` (commit 11bdf1f7). NeoLua's own source declares `pcall` in its global table: `NeoLua/LuaGlobal.cs` at tag v1.3.19 (the newest tag, https://github.com/neolithos/neolua/tags), line 517 `[LuaMember("pcall")]`, https://raw.githubusercontent.com/neolithos/neolua/v1.3.19/NeoLua/LuaGlobal.cs. The installed build carries it: the installed `PilotsDeck.exe` (0.9.7 local build, sha256 909f7af7...) holds NeoLua (`Neo.Lua.dll`) and the Lua base functions `pcall`, `tonumber`, `tostring` and others (byte search, read only, 2026-11-13) |
| REF-FNX | The Fenix XL reference profile installed in ProfilesV3, key 6,3: a Dynamic Button with command type 14 `lua:FNX-A320:INIT_AIRCRAFT` and a read Address. A lead for the saved form only, not copied. |
| LOG | The plugin log `PilotsDeck20261112.log` (read only, searched): the first build's 1X/2X/4X presses as "Running Command (Type: KVAR \| Address: K:SIM_RATE_SET:2 ...)" with no error; RATE "Key TimeDiff" 0.06 to 0.25 s; no "Build Long Command" |
| S7 leads | Not confirmed, recorded only: AVSIM topic 673460 (the set event broken in MSFS 2024, step instead); simFlight topic 91807 (FSUIPC offset 0x0C1A, rate x256); MSFS forum topic 768093 (one step may be x4 in MSFS 2024; the user's report says x2, LR298-C5) |
| LR161-C4 | The coordinator's ruling in the project's chain ledger (2026-11-12): build 1X/2X/4X on `K:SIM_RATE_SET:1/2/4`, Unverified (the first build; replaced in P2-6R). |
| LR97-C2 | The trim keys' sim test (2026-11-11): the K-Var command type (16) works from the deck (`K:ELEV_TRIM_UP` / `_DN`). |
| LR153-C4 | The coordinator's ruling: no A-Var or E-Var write for the sim rate; K-events from the SDK; every indicator reads the rate; stepping with the increment/decrement events against the read rate (Lua allowed) as a named ASSUMPTION, ruled for P2-6R in LR277-C5. |
| LR259-C5, LR263-C5 | The user's sim test reports (2026-11-12): 1X/2X/4X did not change the rate; RATE went up to 128x but never back down. |
| LR298-C5 | The user's layout for this page (2026-11-13): faster, slower, the rate readout and a dedicated 1x key; the sim steps by x2 up to 128x and "also supports very slow rates". Rulings: SLOWER stays, 2X and 4X removed, FASTER added. |

## Fallbacks

Use one only if the checklist shows the main route doesn't work, and say which one you used. None is
tested; they are recorded in aircraft-mappings.md too. The repair after the test rules which one is built.

| Key | Fallback | Source |
|---|---|---|
| 1X: the script does nothing or stops at once, RATE, SLOWER and FASTER work | RATE, SLOWER and FASTER only; 1X stays as a readout until a repair. Check `lua.log` and that the script is installed first. | this page |
| All rate keys: the read shows nothing, `0` or a stuck value while the rate visibly changes | `(E:SIMULATION RATE, number)` in the Value Address and in the script (the same request per PD-SRC, so if it fails too, report it). The script needs the read: without it, it stops at once ("no rate read"). | README 2.1.1; SDK-ENVV |
| All: the sim ignores `K:SIM_RATE_DECR` (log shows the sends, nothing changes) | None left under LR153-C4 (no E-Var write, no FSUIPC offset); use the sim's own sim rate controls and report it: the coordinator decides. | LR153-C4 |

## How to test

Run [tests/manual-checklist.md](../tests/manual-checklist.md), section "Phase 2: Sim rate page (C172
G1000)": install the script, the hand test HT-C first, then the import and the page checks. As on the
other pages, the important direction is the reverse one: **change the rate with the sim's own control and
check that RATE and 1X follow without a key being pressed.**

## When it passes

1. Any change found in the test (the step size, the read address, a saved address form) goes into
   `tools/profilegen/c172-g1000.json`, the script and this doc; then the profile is regenerated (not
   exported from the app) and imported again, and the script copied again.
2. Fill in the "Verified" column of the sim rate rows in aircraft-mappings.md with the date and sim
   version, for each key that passed. Mark an event "does not work" if the sim ignored it.
