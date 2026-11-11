# Phase 1 proof of concept: four keys, Cessna 172 G1000

Goal: prove the full round trip (sim -> Stream Deck and Stream Deck -> sim) with four keys
before building anything bigger. Each one checks a different part of the plugin:

| Key | What it proves | PilotsDeck action |
|---|---|---|
| Battery | Write a harmless control + read its state back | Dynamic Button |
| Parking brake | Same, different system (sanity check) | Dynamic Button |
| Heading | Read-only live value, formatted text | Display Value |
| AP master | Write + read an autopilot state that can also change elsewhere | Dynamic Button |

Everything below uses **standard MSFS SimVars (A-Vars) and Event IDs (K-Vars)** in the
address syntax from the PilotsDeck README (section 2.1.1, plugin 0.9.x). None of it has
been tested in the 2024 C172 yet; the "Verified" column in
[aircraft-mappings.md](aircraft-mappings.md) is filled in only after a test passes.

## Before you start

1. Back up your existing Stream Deck profiles (see [installation.md](installation.md#back-up-existing-profiles)).
2. In the Stream Deck app, create a new profile for the XL called **`MSFS2024 C172 POC`**.
   Keep this exact name: the Profile Manager uses it to update profiles and keep their
   aircraft mappings.
3. Start MSFS 2024, load a free flight in the **Cessna 172 Skyhawk G1000**, cold and dark or parked.
   Wait for the PilotsDeck keys to stop showing the hourglass ("Waiting" state).

## Key 1: Battery (top-left)

Action: **PilotsDeck > Dynamic Button**

| Field | Value |
|---|---|
| Command type | KVAR |
| Command address | `K:TOGGLE_MASTER_BATTERY` |
| Variable (address) | `(A:ELECTRICAL MASTER BATTERY:1, Bool)` |
| On Value / On Image | `1` / any bundled "on" image |
| Off Value / Off Image | `0` / matching "off" image |
| Title (Stream Deck) | `BAT` |

**If it doesn't work:** the 2024 C172 may wire its master switch differently.
- If the key's image doesn't follow the cockpit switch, try the variable without the index:
  `(A:ELECTRICAL MASTER BATTERY, Bool)`.
- If pressing the key does nothing, look in **InputEvents.txt** (Developer UI > QRH) for a
  battery input event (B-Var) and use that as the command instead. Write down what worked
  in aircraft-mappings.md.

## Key 2: Parking brake

Action: **Dynamic Button**

| Field | Value |
|---|---|
| Command type | KVAR |
| Command address | `K:PARKING_BRAKES` (toggles) |
| Variable | `(A:BRAKE PARKING POSITION, Bool)` |
| On / Off Value | `1` / `0` |
| Title | `PARK` |

## Key 3: Heading (display only)

Action: **Display Value**

| Field | Value |
|---|---|
| Variable | `(A:PLANE HEADING DEGREES MAGNETIC, Degrees)` |
| Format | `3.0:%s°` (three digits, no decimals, e.g. `047°`) |
| Command | none (leave empty, or make the key do nothing) |
| Title | `HDG` (or none: the value is the label) |

This shows the aircraft's magnetic heading. The selected heading (heading bug) belongs to
Phase 3; its variable is `(A:AUTOPILOT HEADING LOCK DIR, Degrees)`.

## Key 4: Autopilot master

Action: **Dynamic Button**

| Field | Value |
|---|---|
| Command type | KVAR |
| Command address | `K:AP_MASTER` (toggles) |
| Variable | `(A:AUTOPILOT MASTER, Bool)` |
| On / Off Value | `1` / `0` |
| Title | `AP` |

The autopilot needs avionics power. With the battery off, expect the key to stay "off";
that's correct behavior, not a failure.

## How to test

Run [tests/manual-checklist.md](../tests/manual-checklist.md), Phase 1 section. The key
test is the reverse direction: **flip each switch with the mouse in the cockpit and check
that the key updates without being pressed.**

## When it passes

1. Export the profile from the Stream Deck app (profile dropdown > Export) to
   `pilotsdeck/MSFS2024-XL/_Package/Profiles/MSFS2024 C172 POC.streamDeckProfile`.
2. Fill in the "Verified" column in aircraft-mappings.md with the date and sim version.
3. Note the **aircraft string** shown in the Developer UI (Monitor view). Profile switching
   in Phase 4 matches on it.
4. Copy `InputEvents.txt` from the plugin folder (Developer UI > QRH) to
   `docs/reference/InputEvents-C172-G1000.txt`. It lists every B-Var the C172 exposes,
   which Phases 2 and 3 will need.
