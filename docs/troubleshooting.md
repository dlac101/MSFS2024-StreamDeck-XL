# Troubleshooting

Use this page when the deck, a key, a script or an image doesn't do what its page doc says. Each section
gives what you see, the likely causes, the checks in order, the fix and the source, and links to the doc
with the full steps. Do every check on the PC where the sim and the Stream Deck app run: the plugin, its
log and its `Scripts` and `Images` folders are under that Windows account's `%APPDATA%`.

## Where to look

PilotsDeck writes its logs to the plugin's log folder,
`%APPDATA%\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\log\` (README 4.2.1, 3.5):
`PilotsDeck<YYYYMMDD>.log` is the main log (one file per day), `startup.log` covers the plugin's start,
and `lua.log` holds the Lua scripts' messages and errors. The Stream Deck app keeps its own log,
`StreamDeck0.log`, in `%APPDATA%\Elgato\StreamDeck\logs` (README 4.2.1).

The main log can grow by tens of MB in a day. Search it instead of opening it whole, for example in
PowerShell (put the day's date in place of `<YYYYMMDD>`):

```powershell
$dir = "$env:APPDATA\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\log"
Select-String -Path "$dir\PilotsDeck<YYYYMMDD>.log" -Pattern 'Plugin changed to'
```

Each line reads `<date> <time> [LVL] [ Class:Method ] <message>`, with a level such as `INF`, `WRN`, `ERR`
or `DBG` (plugin log on this PC, 2026-11-14). Search for the message part. Make a verbose log only when
someone asks you for one (README 4.2.2): close the Stream Deck app, set `LogLevel` to `0` in the plugin's
`PluginConfig.json`, reproduce the problem, close the app again and set `LogLevel` back to `1`.

## What the keys show: the plugin's states

| State | When | What the keys show |
|---|---|---|
| Idle | No sim running | A static preview of each key's own setup |
| Waiting | Sim running, no flight loaded | Every key shows the plugin's Wait image, a dark square with three dots ([icons.md](icons.md)) |
| Ready | A flight is loaded | Each key is drawn from its settings and the sim's live values |

The states are from README 3.1 (the page docs say the same, for example
[phase2-main-page.md](phase2-main-page.md#what-the-keys-show-when-the-sim-isnt-there)). The main log marks
each change with `--- Plugin changed to IDLE ---`, `--- Plugin changed to WAIT ---` or
`--- Plugin changed to READY ---`, and the sim's own state with `--- Sim changed to LOADING ---`, `SESSION`
or `RUNNING` (plugin log on this PC, 2026-11-14). While the plugin can't reach the sim it logs
`SimConnect not connected - Retry in <n>s` (`Plugin/Simulator/ConnectorMSFS.cs` at `11bdf1f`).

- **Every key shows the Wait image.** Likely cause: the flight hasn't finished loading. Check: wait until
  you are in the cockpit; if the image stays, search the main log for `Plugin changed to READY`. Fix: with
  a READY line after the flight started, a key that still shows the Wait image is missing its image
  ([missing image](#a-key-shows-the-wait-image-while-the-plugin-is-ready)). With none, gather what
  README 4.2.1 asks for in a support request (the plugin version and the logs above).
- **The keys stay static previews while the sim runs.** Likely cause: the plugin hasn't connected to the
  sim and is still Idle. Check: is the sim fully started? Then search the main log for
  `SimConnect not connected`: the plugin retries by itself. Fix: wait for the retry; if it never connects,
  see the known connection issue in [installation.md](installation.md#pilotsdeck-rules-worth-knowing).
- **The PilotsDeck actions are missing in the Stream Deck app, or their dropdowns are empty.** Likely
  cause: Windows or antivirus software blocks the plugin's files (README 4.2.1). Fix: the `Unblock-File`
  command in ["PilotsDeck rules worth knowing"](installation.md#pilotsdeck-rules-worth-knowing).
- **The plugin stops about 1 s after it starts.** See
  [the patched plugin build](#the-patched-plugin-build-what-not-to-do).

## A key does nothing

What you see: you press a key and nothing moves in the cockpit. A command that could not be executed
shows a yellow alert sign on the key for a moment (README 2.1).

1. Check the plugin state first (above): a command can't run while the sim isn't connected (README 2.1).
2. Search the main log for `Running Command` at the time of the press. A line ending
   `Running Command (...) on Connector MSFS` means the plugin sent the command to the sim (plugin log on
   this PC, 2026-11-14; written by `Plugin/Simulator/SimController.cs` at `11bdf1f`). With no line for the
   press, compare the key's settings in the Stream Deck app with the page doc's "What each key holds".
3. If the command was sent and the cockpit doesn't move, the address may be wrong for this aircraft or
   sim version. Check the page doc's "Fallbacks" and the key's row in
   [aircraft-mappings.md](aircraft-mappings.md): most rows are still "Unverified".
4. If the key sends an H-event or runs a script's `SimCalculator` call (the A32NX fuel MODE SEL key), the
   MobiFlight WASM module must be working ([the MobiFlight WASM module](#the-mobiflight-wasm-module)).

A key that lights or shows a value but doesn't follow the cockpit reads another variable than the cockpit
control drives (example: the C172's battery switch drives an input event, not the standard battery SimVar,
[aircraft-mappings.md](aircraft-mappings.md)). Fix: report it with the page doc's "How to test" steps.

## A script key does nothing

These keys run a Lua script from the package; without it they do nothing (the page docs' install steps):

| Script | Keys that need it | Page doc |
|---|---|---|
| `XL24-SIMRATE.lua` | Sim rate `1X` | [phase2-sim-rate.md](phase2-sim-rate.md) |
| `XL24-COMPAD.lua` | COM pad digits, CLR, ENT | [phase2-com1-pad.md](phase2-com1-pad.md) |
| `XL24-XPDRPAD.lua` | Transponder pad digits, CLR, ENT | [phase3-transponder.md](phase3-transponder.md) |
| `XL24-A32NX.lua` | A32NX FCU and baro readouts, ND MODE, ND RNG, WARN, CAUT, the EFIS page's script keys, the fuel MODE SEL key | [phase4-a32nx.md](phase4-a32nx.md), [phase4-a32nx-efis.md](phase4-a32nx-efis.md), [phase4-a32nx-overhead.md](phase4-a32nx-overhead.md) |

PilotsDeck logs two warnings for a missing script (`Plugin/Resources/ScriptManager.cs` at `11bdf1f`):
`Script File '<file>' does not exist!` when a key that uses it is loaded, and
`The Script '<file>' is not registered or running` when such a key is pressed. The log names the file in
lower case, for example `xl24-simrate.lua` (plugin log on this PC, 2026-11-14). A script runs only once the
plugin has connected to the sim (it may still be Waiting, not yet Ready): before that a press runs nothing
(same file, `RunFunction`, and `Plugin/Simulator/ConnectorMSFS.cs`). A press whose script call fails, for
example before the connection, logs `Failed Script Execution for (...)` (`Plugin/Simulator/ConnectorNone.cs`
at `11bdf1f`).

1. Check the plugin state (above), then in File Explorer that the plugin's `Scripts` folder,
   `%APPDATA%\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\Scripts\`, holds the file.
2. Search the main log for `does not exist`, `not registered or running` and `Failed Script Execution`.
3. Open `lua.log` for the script's own lines, which start with `XL24-SIMRATE:`, `XL24-COMPAD:` or
   `XL24-XPDRPAD:`, and for script errors (README 3.5).

Fix: install the package ([package.md](package.md#install)), which copies every script into the `Scripts`
folder, or copy the file by hand as the page doc's install step says. A changed script is reloaded by
itself while the plugin runs; no restart needed (README 3.5).

## A key shows the Wait image while the plugin is Ready

What you see: the plugin is Ready and most keys are drawn, but some keys show the Wait image. PilotsDeck
shows the Wait image in place of an image file it can't find, and logs nothing about it at the normal log
level (`Plugin/Resources/Images/ManagedImage.cs` at `11bdf1f`).

1. Check the plugin state first (above): while it is Waiting, every key shows this image.
2. The usual cause here is the optional local icon build, whose images the local icon package (or a hand
   copy) puts into the plugin's `Images` folder
   ([icons.md](icons.md#2-install-with-the-profile-manager-your-own-step)). In
   File Explorer, check that `%APPDATA%\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\Images\`
   holds it. Images must be PNG files and square (README 3.3).

Fix: install the local icon package again (or copy the images by hand) and restart the Stream Deck app,
as icons.md says. Never re-run the PilotsDeck installer to fix images (see
[the patched plugin build](#the-patched-plugin-build-what-not-to-do)).

## The MobiFlight WASM module

PilotsDeck sends every H-event and all calculator code through the MobiFlight WASM module. In this repo the
H-event keys are the C172 G1000 PFD and MFD bezel keys and the autopilot page's CRS+, CRS1 and CRS- presses:
without the module they do nothing. A Lua script's `SimCalculator` call is calculator code too, so the A32NX
fuel MODE SEL key (ovhdsys 1,8, [phase4-a32nx-overhead.md](phase4-a32nx-overhead.md)) needs the module as
well: without it the press does nothing (CFIT.SimConnectLib at `8c06162c`: `MobiModule.ExecuteCode` sends the
code with no check that the module is connected). The other address kinds don't use it
(installation.md, linked below).

1. In File Explorer, check that the sim's Community folder ([installation.md](installation.md#this-pc))
   holds the `mobiflight-event-module` folder.
2. After a flight has loaded, search the main log for `MobiFlight WASM`. A working module gives
   `Sending Ping to MobiFlight WASM Module.`, then
   `MobiFlight WASM Ping acknowledged - opening Client Connection.` and
   `MobiFlight WASM Client Connection opened.` (plugin log on this PC, 2026-11-14).

Fix, and why reinstalling the module is blocked on this PC: installation.md, "MobiFlight WASM module
(which keys need it)"
([link](installation.md#mobiflight-wasm-module-which-keys-need-it)).

## The patched plugin build: what not to do

The plugin on this PC is a locally patched build of PilotsDeck 0.9.7, because the official build crashes
at startup ([installation.md](installation.md)). That crash looks like this: the plugin stops about 1 s
after every start, the Stream Deck app disables it as unstable, and `startup.log` ends with
`COMException ... Incorrect function. (0x80070001)`.

While [Fragtality/PilotsDeck#176](https://github.com/Fragtality/PilotsDeck/issues/176) is open (still open
on 2026-11-14), don't:

- re-run the PilotsDeck installer or update the plugin (either brings the crash back), or use the
  installer's Remove option (it deletes the custom scripts and images);
- run the installer, the plugin or the Stream Deck app "as administrator".

If the log shows `New Build detected` at startup, it comes from the patched build (installation.md): ignore
it. Installing a package needs no installer ([package.md](package.md#install)). When an official build
fixes #176, follow [installation.md](installation.md), "Known issue on this PC: PilotsDeck exits at startup".

## Profiles: a second copy, or no automatic switch

A second profile of the same name: install with **Remove old Profiles** checked
([package.md](package.md#install), [update](package.md#update-to-a-newer-package)). No automatic switch to
the C172 G1000 profile: map it once ([package.md](package.md#map-the-c172-g1000-profile-automatic-switching)).

## Sources

| Source | Used for |
|---|---|
| PilotsDeck README at `11bdf1f`, sections 2.1, 3.1, 3.3, 3.5, 4.2.1, 4.2.2 | Yellow alert sign, plugin states, image format, scripts and `lua.log`, log files, verbose log |
| [`Plugin/Resources/ScriptManager.cs`](https://github.com/Fragtality/PilotsDeck/blob/11bdf1f/Plugin/Resources/ScriptManager.cs) at `11bdf1f` | The two missing-script warnings; no script run before the sim connection |
| [`Plugin/Resources/Images/ManagedImage.cs`](https://github.com/Fragtality/PilotsDeck/blob/11bdf1f/Plugin/Resources/Images/ManagedImage.cs) at `11bdf1f` | Wait image for a missing image file, no log line |
| [`Plugin/Simulator/ConnectorMSFS.cs`](https://github.com/Fragtality/PilotsDeck/blob/11bdf1f/Plugin/Simulator/ConnectorMSFS.cs) at `11bdf1f` | `SimConnect not connected - Retry in <n>s`; the sim connection a script needs |
| [`Plugin/Simulator/SimController.cs`](https://github.com/Fragtality/PilotsDeck/blob/11bdf1f/Plugin/Simulator/SimController.cs) at `11bdf1f` | `Running Command (...) on Connector MSFS` |
| [`Plugin/Simulator/ConnectorNone.cs`](https://github.com/Fragtality/PilotsDeck/blob/11bdf1f/Plugin/Simulator/ConnectorNone.cs) at `11bdf1f` | `Failed Script Execution for (...)` |
| [Fragtality/PilotsDeck#176](https://github.com/Fragtality/PilotsDeck/issues/176) | The startup crash; open on 2026-11-14 |
| Plugin log on this PC, 2026-11-14 | Line layout; plugin and sim state lines; MobiFlight lines; lower-case script names |
| [installation.md](installation.md) | The patched build, the MobiFlight module and the keys that need it, `New Build detected` |
