# MSFS 2024 Stream Deck XL

A free, aircraft-aware Stream Deck XL cockpit for Microsoft Flight Simulator 2024, built on
[PilotsDeck](https://github.com/Fragtality/PilotsDeck) (MIT). No custom plugin: everything here
is PilotsDeck configuration, Lua scripts and images, delivered as a PilotsDeck profile package (`.ppp`).

The original brief is in [docs/original-plan.md](docs/original-plan.md).

## Status

**Phase 1: four-key proof of concept, core test passed 2026-11-11** (C172 G1000, MSFS 1.9.24.0):
all four keys work in both directions. Restart, controller and disconnected-sim checks are still to run.
See [docs/poc-c172.md](docs/poc-c172.md) and [tests/manual-checklist.md](tests/manual-checklist.md).
PilotsDeck runs on this PC with a locally patched build until
[Fragtality/PilotsDeck#176](https://github.com/Fragtality/PilotsDeck/issues/176) is fixed
([details](docs/installation.md#known-issue-on-this-pc-pilotsdeck-exits-at-startup-worked-around-with-a-patched-build)).

**Phase 2: main page (C172 G1000), profile generated, untested.** Import one file; see [docs/phase2-main-page.md](docs/phase2-main-page.md).
Its Trim and Views pages are filled (untested): [docs/phase2-trim-views.md](docs/phase2-trim-views.md).
Under More: G1000 PFD and MFD bezel pages and a V-speeds page (untested): [docs/phase2-g1000-vspeeds.md](docs/phase2-g1000-vspeeds.md).
Sim rate page (behind main page 3,7; repaired after the first sim test, not yet sim-tested): 1X (back to 1x in one press, by a Lua script that steps the rate; the script `XL24-SIMRATE.lua` must be copied into the plugin's Scripts folder), SLOWER (one step down), a RATE readout (press one step up, hold a full second one step down) and FASTER (one step up): [docs/phase2-sim-rate.md](docs/phase2-sim-rate.md).
Optional local icon build of the same profile (Guenseli pack, personal use only, never committed; untested): [docs/icons.md](docs/icons.md).
COM1 number pad under More (MORE 1,5; a Lua script sets the frequency; generated, not yet sim-tested; the script must be copied into the plugin's Scripts folder): [docs/phase2-com1-pad.md](docs/phase2-com1-pad.md).
Autopilot page under More (MORE 1,6; GFC 700 mode keys lit from sim state, heading, course, altitude, VS and FLC speed readouts with step keys; generated, not yet sim-tested): [docs/phase3-autopilot.md](docs/phase3-autopilot.md).
Designed, not built: an elevator trim bar gauge on the Trim page ([docs/design-trim-gauge.md](docs/design-trim-gauge.md)).
## Layout

```text
docs/
  original-plan.md      the project brief
  installation.md       this PC's setup, versions, backups, git across accounts
  poc-c172.md           Phase 1 key-by-key setup
  phase2-main-page.md   Phase 2 main page: import, regenerate, key-by-key reference (C172 G1000)
  phase2-trim-views.md  Phase 2 Trim and Views child pages: key-by-key reference (C172 G1000)
  phase2-g1000-vspeeds.md  Phase 2 More, G1000 PFD/MFD bezel and V-speeds pages (C172 G1000)
  phase2-sim-rate.md    Phase 2 Sim rate child page: 1X (Lua script XL24-SIMRATE.lua), SLOWER, RATE and FASTER, key-by-key reference (C172 G1000)
  phase2-com1-pad.md    Phase 2 COM1 pad (MORE > COM PAD): number pad, Lua script, key-by-key reference (C172 G1000)
  phase3-autopilot.md   Phase 3 Autopilot page (MORE > AUTOPILOT, GFC 700): mode keys, readouts, key-by-key reference (C172 G1000)
  design-trim-gauge.md  design (not built): elevator trim bar gauge on the Trim page (C172 G1000)
  navigation.md         how pages connect (folders, back key) and the planned pages
  roadmap.md            what is built, what the plan and community profiles offer, gap list and planned units
  icons.md              optional local icon build (Guenseli pack, personal use only, never committed)
  aircraft-mappings.md  every variable/event used, with verification status
  reference/            files copied out of the sim (InputEvents.txt etc.)
tests/
  manual-checklist.md
tools/
  scmon/                read-only SimConnect monitor for checking which variable a control drives
  profilegen/           generates and checks the .streamDeckProfile files from a page data file
pilotsdeck/
  MSFS2024-XL/          a PilotsDeck Profile Manager "work folder"
    _Package/           package contents: same layout as the plugin folder
      package.json
      Profiles/         .streamDeckProfile files (Phase 1 export; Phase 2 generated)
      Scripts/          standard Lua scripts; global/ and image/ subfolders
      Images/
    _Releases/          built .ppp/.zip packages (not committed)
```

## Building the package

In PilotsDeck's Profile Manager, open **Create Package**, load the work folder
`A:\FS2024 Stuff\msfs2024-streamdeck-xl\pilotsdeck\MSFS2024-XL`, then **Create Package**.
The output goes to `_Releases/`.

## Ground rules (from the plan)

- Configuration first, Lua second, fork never (unless forced).
- Read actual sim state; never assume a toggle worked.
- Nothing depends on which flight controls are connected (Xbox Elite or T.16000M/TWCS).
- Record every aircraft variable/event in `docs/aircraft-mappings.md` with its verification status.

## License

[MIT](LICENSE). PilotsDeck itself is MIT-licensed by its author; this project only ships configuration,
Lua scripts and images for it.
