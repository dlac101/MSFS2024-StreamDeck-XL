# scmon: read-only SimConnect monitor

Prints a timestamped line whenever one of the watched SimVars changes, straight from MSFS. Use it to
find out which variable a cockpit control really drives before trusting it on a key. It found that the
2024 C172's BAT switch drives battery index 2, not index 1 (see `docs/aircraft-mappings.md`).

It never writes to the sim. It uses the SimConnect DLLs that come with the PilotsDeck plugin, so build
and run it in the Windows account where PilotsDeck is installed (Admin).

## Build

The .NET 10 SDK is installed per user at `%LOCALAPPDATA%\Microsoft\dotnet` (not on PATH):

```powershell
& "$env:LOCALAPPDATA\Microsoft\dotnet\dotnet.exe" build "A:\FS2024 Stuff\msfs2024-streamdeck-xl\tools\scmon\scmon.csproj" -c Release -o "$env:TEMP\scmon-bin"
```

Build output goes outside the repo (`bin/` and `obj/` are ignored anyway).

## Run

With MSFS running and a flight loaded:

```powershell
& "$env:LOCALAPPDATA\Microsoft\dotnet\dotnet.exe" "$env:TEMP\scmon-bin\scmon.dll" 180 B:electrical_battery_1
```

- First argument: seconds to watch (default 180).
- Second argument (optional): a B-Var or L-Var to poll through PilotsDeck's local API at the same time,
  so you can compare the aircraft's input event with the SimVars on one timeline.

Then work the cockpit control with the mouse and read which values change.

To watch other SimVars, edit the `Vars` list at the top of `Program.cs` (up to 16) and rebuild.

## Why not PilotsDeck's own API?

PilotsDeck has a local HTTP API (`http://localhost:42042/v1/get/<address>`), but it doesn't URL-decode
addresses. Any A-Var whose name contains spaces (almost all of them) arrives garbled and reads `0`.
B-Vars and L-Vars without spaces read fine.
