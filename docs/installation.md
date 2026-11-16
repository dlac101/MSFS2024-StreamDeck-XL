# Installation and environment

## This PC

| Item | Detail |
|---|---|
| Simulator | MSFS 2024, Steam edition |
| Sim user account | Windows account **Admin** (MSFS, Stream Deck, PilotsDeck all run here) |
| Community folder | `C:\Users\Admin\AppData\Roaming\Microsoft Flight Simulator 2024\Packages\Community\` |
| PilotsDeck plugin | `C:\Users\Admin\AppData\Roaming\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin\` |
| This repo | `A:\FS2024 Stuff\msfs2024-streamdeck-xl` (readable and writable by every account) |

Other Windows accounts can't read the Admin account's AppData. That's why the repo lives
on A:, and why profile exports, `InputEvents.txt` and logs need to be copied from the
Admin account into the repo before they can be reviewed elsewhere.

## Versions

| Component | Version | Notes |
|---|---|---|
| PilotsDeck | 0.9.7 | "Latest Build" dev installer (`A:\FS2024 Stuff\PilotsDeck-Installer-latest.exe`), installed 2026-11-11. Latest stable is 0.9.1. |
| Stream Deck app | 7.6.1 | PilotsDeck needs 7.4 or later |
| .NET Desktop Runtime | 10.x | Installed by the PilotsDeck installer |
| MobiFlight WASM module | 1.0.1 | Folder `mobiflight-event-module` in the Community folder: `package_version` in its `manifest.json`, read 2026-11-14. Installed by the PilotsDeck installer. The H-event keys (the G1000 bezel keys, the autopilot page's CRS presses, the A32NX radio page's VHF1, VHF2, XFER and MHz and kHz step keys and the transponder page's keypad) and the A32NX fuel MODE SEL key need it (see "MobiFlight WASM module" below). |
| FSUIPC7 | 7.5.9 | Optional for PilotsDeck on MSFS; free (unregistered) is enough |
| MSFS 2024 | 1.9.24.0 | File version of `FlightSimulator2024.exe`, read 2026-11-11 |

## PilotsDeck rules worth knowing

From the PilotsDeck README:
- **Don't run** the installer, the plugin or the Stream Deck app **"as administrator"** (elevated).
  Being logged in to the account called "Admin" is fine; right-click > "Run as administrator" is not.
- Re-running the installer updates in place. Its **Remove** option deletes all custom images and scripts.
- If the action dropdowns are empty, Windows or antivirus is probably blocking the plugin. Fix:
  `dir -Path $env:APPDATA\Elgato\StreamDeck\Plugins\com.extension.pilotsdeck.sdPlugin -Recurse | Unblock-File`
- Known MSFS 2024 issue (won't connect / "Out of Bound" exception): remove the MobiFlight
  module, re-run the installer, reboot. On this PC that is blocked while the patched build is in use
  (see "MobiFlight WASM module" below).

## Known issue on this PC: PilotsDeck exits at startup (worked around with a patched build)

Found 2026-11-11. PilotsDeck 0.9.7 (2026.10.30.2121) shuts down about 1 s after every start, and the
Stream Deck app then disables it as "unstable". `log\startup.log` ends with
`COMException ... Incorrect function. (0x80070001)` in `H.NotifyIcon ... SetEfficiencyMode`, called from
`PilotsDeck.App.InitMainWindow`, then `Signal Shutdown`.

- Cause: on this PC Windows rejects the power-throttling ("Efficiency mode") API for every process, and
  PilotsDeck treats that as fatal. Other process settings work. Why Windows rejects it is unknown.
- Ruled out: `PowerThrottlingOff` (changed from 1 to 0 plus reboot, no change). Not elevated.
- Reported upstream: [Fragtality/PilotsDeck#176](https://github.com/Fragtality/PilotsDeck/issues/176).
- **Workaround in place (2026-11-11):** a locally built `PilotsDeck.exe` from the same commit
  (`11bdf1f`), with the three `Show(disableEfficiencyMode: true)` calls changed to `false`
  (startup window, action designer, Developer UI). The CFIT libraries were built from
  [Fragtality/CFIT](https://github.com/Fragtality/CFIT) at `267c6b8` with the exact versions 0.9.7 expects.
  The original exe is kept next to it as `PilotsDeck.exe.0.9.7-original`. The build used a
  per-user .NET 10 SDK in `%LOCALAPPDATA%\Microsoft\dotnet` (not on PATH).
- The patched build logs "New Build detected" at startup because its build stamp differs. Ignore it.
- When an official build with the fix ships, run the PilotsDeck installer as usual. Its update step
  deletes every file at the top of the plugin folder except the plugin's configuration and colour files,
  then installs the release, so it replaces the patched exe and also removes
  `PilotsDeck.exe.0.9.7-original`: nothing is left to delete by hand
  (`Installer/Worker/WorkerInstallUpdate.cs` lines 45-69 at `11bdf1f`).

## MobiFlight WASM module (which keys need it)

- PilotsDeck sends every H-event (`H:` address) through the MobiFlight WASM module, not through SimConnect
  (PilotsDeck source at `11bdf1f`, `Plugin/Simulator/MSFS/ToolsMSFS.cs` lines 163-184, `WriteSingleHvar`).
  In this repo those are the C172 G1000 PFD and MFD bezel keys
  ([phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md)), the autopilot page's `CRS+`, `CRS1` and `CRS-`
  presses ([phase3-autopilot.md](phase3-autopilot.md); the long presses of `CRS+` and `CRS-` are K-events),
  and the A32NX radio page's RMP 1 keys (VHF1, VHF2, XFER and the MHz and kHz steps) and
  transponder keypad (0 to 7, CLR) ([phase4-a32nx-radios.md](phase4-a32nx-radios.md)): without the module
  they do nothing. No other key sends an H-event.
- The other address kinds don't use the module: K-events go through SimConnect's event calls
  (`Plugin/Simulator/MSFS/ToolsMSFS.cs`, `WriteSingleKvar`), B-Vars through SimConnect's input-event calls,
  and L-Var reads and writes through PilotsDeck's SimConnect variable manager
  (`Plugin/Simulator/ConnectorMSFS.cs` and `Plugin/Simulator/MSFS/SubManager.cs` at `11bdf1f`). Only H-events
  and calculator code (README 2.1.1, CALCULATOR) go through it. A Lua script's `SimCalculator` call is
  calculator code too: PilotsDeck passes it to `MobiModule.ExecuteCode` (`Plugin/Simulator/ConnectorMSFS.cs`
  lines 551-569 at `11bdf1f`), which sends it to the module with no check that the module is connected
  (CFIT.SimConnectLib at `8c06162c`, `SimConnectLib/Modules/MobiFlight/MobiModule.cs`). The A32NX fuel
  MODE SEL key (`lua:XL24-A32NX:FUELMODE`, ovhdsys 1,8, [phase4-a32nx-overhead.md](phase4-a32nx-overhead.md))
  uses one, so it needs the module; the A32NX's other L-Var and `A32NX.*` event keys and the input-event
  switches work without it.
- Check: after a flight has loaded, the plugin log shows "MobiFlight WASM Client Connection opened" (seen on
  this PC on 2026-11-14 with module 1.0.1, the latest release on MobiFlight's
  [releases page](https://github.com/MobiFlight/MobiFlight-WASM-Module/releases)).
- Reinstalling the module is blocked while the patched plugin build is in use. The README's way (1.4, 4.2.3:
  remove the module, re-run the installer, reboot) is a full installer run: the installer queues the module
  step and the plugin install step together (`Installer/WorkerManager.cs` lines 18-33 at `11bdf1f`), and the
  plugin step deletes the plugin's program files before it installs the release
  (`Installer/Worker/WorkerInstallUpdate.cs` lines 51-69). That replaces the patched `PilotsDeck.exe` and
  brings back the startup crash ([#176](https://github.com/Fragtality/PilotsDeck/issues/176), still open on
  2026-11-14). Until an official build fixes #176, keep the module folder and don't re-run the installer.

## Back up existing profiles

Do this before the first experiment. Signed in as Admin:
1. Stream Deck app > Preferences > Profiles: select each profile you want to keep > Export.
2. Save the exports to `A:\BACKUPS\StreamDeck\<date>\`. Back up there, not in this repo:
   these are your personal profiles, not project files.

## Git for more than one Windows account

Git refuses to work in a repo owned by a different account ("dubious ownership"). Run this
**once in each account** that will use the repo:

```powershell
git config --global --add safe.directory "A:/FS2024 Stuff/msfs2024-streamdeck-xl"
```
