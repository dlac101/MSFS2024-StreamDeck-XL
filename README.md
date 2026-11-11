# MSFS 2024 Stream Deck XL

A free, aircraft-aware Stream Deck XL cockpit for Microsoft Flight Simulator 2024, built on
[PilotsDeck](https://github.com/Fragtality/PilotsDeck) (MIT). No custom plugin: everything here
is PilotsDeck configuration, Lua scripts and images, delivered as a PilotsDeck profile package (`.ppp`).

The original brief is in [docs/original-plan.md](docs/original-plan.md).

## Status

**Phase 1: four-key proof of concept, not yet tested.** See [docs/poc-c172.md](docs/poc-c172.md).

## Layout

```text
CLAUDE.md               project facts and rules for Claude sessions (any Windows account)
docs/
  original-plan.md      the project brief
  installation.md       this PC's setup, versions, backups, git across accounts
  poc-c172.md           Phase 1 key-by-key setup
  aircraft-mappings.md  every variable/event used, with verification status
  reference/            files copied out of the sim (InputEvents.txt etc.)
tests/
  manual-checklist.md
pilotsdeck/
  MSFS2024-XL/          a PilotsDeck Profile Manager "work folder"
    _Package/           package contents: same layout as the plugin folder
      package.json
      Profiles/         .streamDeckProfile exports
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
