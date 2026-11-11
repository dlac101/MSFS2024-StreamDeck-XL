# MSFS 2024 Stream Deck XL Development Project

## Goal

Build a free, extensible, aircraft-aware **Stream Deck XL cockpit interface** for **Microsoft Flight Simulator 2024 (PC)**, based on the open-source [PilotsDeck](https://github.com/Fragtality/PilotsDeck) project. The goal is a reliable set of 32-key pages with live simulator feedback, reusable functions, and aircraft-specific behavior. Do not rebuild simulator connectivity already provided by PilotsDeck.

This document is a handoff brief for development on another computer with Codex or Claude.

## Hardware and operating constraints

- **Simulator:** MSFS 2024 Standard Edition, Windows PC.
- **Always present:** Elgato Stream Deck XL (8 × 4 keys).
- **Primary controls (~75% of flights):** Microsoft Xbox Elite controller.
- **Alternative controls (~25%):** Thrustmaster T.16000M joystick and TWCS throttle.
- **Design invariant:** Stream Deck layout and simulator actions should work identically with either flight-control setup; avoid dependence on controller-specific keyboard bindings.
- **Budget:** Prefer free and open-source software. Paid middleware only if a proven capability gap justifies it.

## Technical foundation

- **PilotsDeck:** https://github.com/Fragtality/PilotsDeck
- **Releases:** https://github.com/Fragtality/PilotsDeck/releases
- **Elgato Stream Deck software:** https://www.elgato.com/us/en/s/downloads
- **MobiFlight:** https://www.mobiflight.com/ (verify current plugin/WASM installation requirements against PilotsDeck documentation)
- **Simulator interface:** SimConnect for standard simulator variables/events; MobiFlight WASM and aircraft-specific events/variables for systems that SimConnect does not expose directly.
- **Customization:** Prefer PilotsDeck configuration, composite actions, and Lua scripts. Consider a C# fork or plugin contributions only when necessary.

**Before implementing:** Read the current PilotsDeck README, release notes, configuration guidance, examples, license, and MSFS 2024 support notes. Confirm the current installation/dependency details rather than assuming they have stayed unchanged.

## Architecture

```text
                       MSFS 2024
                           |
               SimConnect / MobiFlight WASM
                           |
                     PilotsDeck plugin
                           |
           Common definitions + Lua utilities
                           |
               Stream Deck XL (32 keys)
                /         |          \
          Universal    Aircraft class   Aircraft-specific
            pages         pages             pages

  Xbox Elite controller ---------\
                                  > Independent flight controls
  T.16000M + TWCS ---------------/
```

### Three levels of pages

1. **Universal:** Parking brake, gear (where applicable), flaps, exterior lights, ATC, maps, views, navigation between pages.
2. **Aircraft-class:** GA autopilot and Garmin avionics; airliner flight guidance and radios; helicopter-specific systems.
3. **Aircraft-specific:** Cessna 172/G1000 NXi first, then additional airplanes as needed. Use aircraft detection/automatic switching where PilotsDeck supports it, with safe fallback pages.

Do not assume every aircraft implements the same commands or variables. Build capability detection and aircraft-specific mappings rather than silently sending a generic event that fails.

## Functional requirements

### Phase 1: Baseline integration

- Install Stream Deck software and a current compatible PilotsDeck release.
- Start MSFS 2024 in a default Cessna 172, preferably the G1000 variant.
- Verify that the plugin connects, can **read** a live simulator value, and can **write** a harmless test control.
- Capture current versions and configuration setup in the repo README.
- Create a minimal profile that can be exported, backed up, and re-imported.

**Acceptance criteria:** A Stream Deck key shows a live simulator value, a separate key actuates a test event, and both survive restarting the sim and Stream Deck software.

### Phase 2: Universal 32-key foundation

Create a consistent main page, for example:

| Row | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| 1 | Battery | Engine | Fuel | Park brake | Gear | Flaps | Trim page | Views |
| 2 | AP | HDG | ALT | VS | NAV | APR | Speed | Flight director |
| 3 | COM | XPDR | ATC | Map | GPS | Baro | Timer | Checklist |
| 4 | NAV light | Beacon | Strobe | Landing | Taxi | Pitot | Anti-ice | More |

This is a **concept layout**, not a promise that every key applies to every aircraft. Hide, gray out, replace, or route unsupported functions appropriately. Use additional pages instead of crowding all controls into one screen.

**Acceptance criteria:** Common functions work in the C172, controls are understandable at a glance, and page navigation is consistent.

### Phase 3: State-aware controls

Prioritize **actual simulator state** over visual assumptions based on the last button press.

- Autopilot key shows engaged/disengaged status even when changed elsewhere.
- Landing light key displays the true state.
- Selected heading and altitude display current selected values.
- COM radio keys show frequency and, where appropriate, active/standby.
- Gear indicator reports actual state or transit when exposed by the aircraft.
- Handle unavailable values, simulator disconnects, and stale data explicitly.

**Acceptance criteria:** Changing a cockpit switch with a mouse updates the corresponding Stream Deck indication without needing to press the Stream Deck key.

### Phase 4: Reusable abstractions and aircraft support

Implement shared action/indicator definitions and data mappings with aircraft-specific overrides.

Suggested interfaces (conceptual, not pre-existing PilotsDeck APIs):

```text
ToggleLight(lightId)
SetAutopilotMode(mode, enabled)
AdjustSelectedHeading(delta)
AdjustSelectedAltitude(delta)
SetComStandby(frequency)
GetAircraftCapabilities()
```

Start with **C172 G1000 NXi**, then add one contrasting aircraft, such as an Airbus or helicopter, to validate that the architecture is genuinely reusable.

**Acceptance criteria:** Shared UI components require little or no modification when adding an aircraft mapping; unsupported functions degrade gracefully.

### Phase 5: Scripted workflows and polish

- Use Lua/composite actions for multi-step controls or convenience functions where safe.
- Avoid irreversible/unexpected automation; provide clear indications and user-initiated controls.
- Add icons, readable labels, colors, and meaningful state changes.
- Add optional checklists and aircraft startup aids after core controls are stable.
- Export a versioned, installable set of profiles with setup instructions.

**Acceptance criteria:** New install can reproduce the configuration from documented prerequisites and repository files.

## Proposed repository layout

```text
msfs2024-streamdeck-xl/
├── README.md
├── docs/
│   ├── architecture.md
│   ├── installation.md
│   ├── aircraft-mappings.md
│   └── troubleshooting.md
├── profiles/
│   ├── universal/
│   ├── ga/
│   ├── airliner/
│   └── helicopter/
├── scripts/
│   ├── common/
│   └── aircraft/
├── assets/
│   ├── icons/
│   └── templates/
├── tests/
│   └── manual-checklist.md
└── CHANGELOG.md
```

Actual file formats and paths should follow PilotsDeck's current import/export and scripting conventions. Do not assume its internal configuration files are intended for direct hand-editing. Store exported files and original scripts with clear licensing and provenance.

## Engineering guidelines

- **Configuration first, Lua second, fork third.** Avoid maintaining a divergent C# fork unless needed.
- **Never rely on button-toggle assumptions** when simulator state can be read.
- **No device-specific dependency** between the Stream Deck and Xbox/HOTAS bindings.
- **Avoid command collisions:** If both controller types are connected, disable or isolate unwanted duplicate flight-axis assignments in MSFS.
- **Fail visibly:** On disconnect or unsupported state, display `N/A`, dim the key, or provide a clear error indicator.
- **Limit update traffic:** Rate-limit displayed values appropriately to avoid needless simulator polling or flickering.
- **Document mappings:** For every aircraft-specific action, record the source variable/event, expected units, and verified test aircraft/version.
- **Make everything reproducible:** Keep profile exports, custom scripts, asset sources, installation directions, and version compatibility notes in Git.
- **Respect licenses:** Check PilotsDeck and profile/icon licenses before redistributing bundled content.

## Initial testing checklist

- [ ] PilotsDeck connects to MSFS 2024.
- [ ] Live simulator values appear on Stream Deck XL.
- [ ] Stream Deck events actuate the intended cockpit controls.
- [ ] Cockpit changes made by mouse update Stream Deck indicators.
- [ ] Indicators handle disconnected simulator without misleading states.
- [ ] Keys work when flying with Xbox Elite controller.
- [ ] Same keys work when flying with T.16000M/TWCS.
- [ ] Switching aircraft selects the intended pages or a safe default.
- [ ] Profile export/import works on a clean installation.
- [ ] No paid dependency is required for baseline functionality.

## Immediate next development task

1. Inspect the current PilotsDeck repo documentation, examples, supported simulator APIs, and Lua capabilities.
2. Install and validate the latest compatible release on the development PC.
3. Build a **four-key proof of concept** for the C172: battery on/off with live indication; parking brake with live indication; current heading display; autopilot master on/off with live indication.
4. Capture a working profile export and any custom scripts in the new repository.
5. Extend to a polished universal 32-key layout only after this round-trip test succeeds.

## AI coding assistant handoff prompt

> I am building a free, aircraft-aware Stream Deck XL integration for Microsoft Flight Simulator 2024 using Fragtality's open-source PilotsDeck project. Read this project plan and inspect PilotsDeck's current README, examples, release notes, configuration and Lua documentation. Prefer existing plugin features and scripts over a fork. First, propose a minimal four-key C172/G1000 NXi proof of concept with bidirectional simulator feedback, and identify exact supported events, variables, profile formats, and installation dependencies from the current documentation. Do not invent API names or variables. Implement the smallest reproducible change, provide installation steps, and a manual test checklist. Keep the design independent of Xbox Elite versus T.16000M/TWCS flight controls.

## Related but optional reference

Tom Tsui's existing Stream Deck XL layouts may provide design inspiration, but **are not a project dependency**. His May 2026 profile download reportedly fails for some users; there is no need to block development waiting for it. PilotsDeck is the primary foundation.
