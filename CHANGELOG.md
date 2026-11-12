# Changelog

## Unreleased
- Repo created. Phase 1 four-key proof-of-concept spec written (untested).
- FlyByWire A32NX chosen as the Phase 4 airliner.
- Added CLAUDE.md so Claude sessions in any Windows account get the project context.
- Added MIT license.
- PilotsDeck 0.9.7 exits at startup on this PC (Efficiency mode API rejected by Windows).
  Reported as Fragtality/PilotsDeck#176; running a locally patched build until it's fixed.
  Details in docs/installation.md.
- Phase 1 core test passed (2026-11-11, MSFS 1.9.24.0, PilotsDeck 0.9.7 patched, C172 G1000):
  - Connection: plugin reached READY with the flight loaded; HDG tracks the PFD heading. (The
    hourglass-while-loading check wasn't seen: the keys were made after the flight loaded.)
  - Stream Deck -> sim: BAT, PARK and AP keys switch the cockpit controls.
  - Sim -> Stream Deck: BAT, PARK and AP keys follow mouse clicks in the cockpit.
  - Battery uses the C172's input event `B:electrical_battery_1`: the cockpit switch drives battery
    index 2, so the standard index-1 SimVar and `K:TOGGLE_MASTER_BATTERY` don't stay in sync.
  - Not yet run: restart survival, controller independence, disconnected sim, profile round trip.
- Added docs/reference/InputEvents-C172-G1000.txt (233 input events).
- Phase 2 main page spec written (untested): docs/phase2-main-page.md (C172 G1000, 26 keys, 6 reserved).
