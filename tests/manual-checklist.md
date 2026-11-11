# Manual test checklist

Copy the relevant section into a dated note (or the CHANGELOG) each time you run it.
Record: date, MSFS 2024 version, PilotsDeck version, aircraft.

## Phase 1: four-key proof of concept (C172 G1000)

Setup: cold and dark or parked, profile `MSFS2024 C172 POC` active.

**Connection**
- [ ] Keys show the hourglass while the sim loads, then live content once in the cockpit.
- [ ] Heading key shows a 3-digit heading that changes as the aircraft turns (taxi or slew).

**Stream Deck -> sim**
- [ ] Battery key turns the battery on; the cockpit switch moves and the key shows "on".
- [ ] Battery key turns it off again.
- [ ] Parking brake key sets and releases the brake.
- [ ] With battery and avionics on, AP key engages and disengages the autopilot.

**Sim -> Stream Deck (the important one)**
- [ ] Battery switched with the mouse: key updates without being pressed.
- [ ] Parking brake changed with the mouse: key updates.
- [ ] AP engaged/disengaged with the mouse on the G1000 (or AP disconnect on the controller): key updates.

**Restart survival**
- [ ] Quit to main menu and reload the flight: keys recover by themselves.
- [ ] Restart MSFS: keys recover.
- [ ] Quit and restart the Stream Deck app: the profile and all four keys are intact.

**Controller independence**
- [ ] All of the above works flying with the Xbox Elite controller.
- [ ] All of the above works flying with the T.16000M + TWCS.

**Disconnected sim**
- [ ] With MSFS closed, keys show the plugin's idle preview, not a stale "on" state.

**Profile round trip**
- [ ] Exported profile saved to `pilotsdeck/MSFS2024-XL/_Package/Profiles/`.
- [ ] Re-imported copy works the same as the original.
