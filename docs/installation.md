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
| MobiFlight WASM module | _TBD_ | Installed by the PilotsDeck installer: check the Community folder |
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
  module, re-run the installer, reboot.

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
- When an official build with the fix ships, run the PilotsDeck installer as usual. It replaces
  the patched exe, and the `-original` file can then be deleted.

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
