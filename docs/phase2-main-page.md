# Phase 2: main page, Cessna 172 G1000

**Status: untested.** Nothing on this page has been tried in the sim yet. Every new name below is
recorded as "Unverified" in [aircraft-mappings.md](aircraft-mappings.md) until the Phase 2 checklist
passes.

Goal: one 32-key main page for the Stream Deck XL (8 columns x 4 rows) for the default MSFS 2024
**Cessna 172 Skyhawk G1000**, based on the concept layout in [original-plan.md](original-plan.md)
(Phase 2). Every indicator reads actual sim state; no key guesses its state from its last press.
26 keys are configured, 4 are folder keys that open the Trim, Views, Checklist and More pages (Trim and
Views: [phase2-trim-views.md](phase2-trim-views.md); More: folder keys to the PFD, MFD and V-speeds pages, [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md); Checklist holds only its back key for now), and 2 are reserved (left empty so the grid stays stable for later units).

You don't build it by hand: the profile is generated in the repo, and you import one file into the
Stream Deck app (7.6.1) with PilotsDeck 0.9.7 (the locally patched build, see
[installation.md](installation.md)). See "Import the profile". The tables below stay the reference
for what each key holds; the generator's check compares the profile with them.
How the pages connect, now and later: [navigation.md](navigation.md).

## Layout

Positions are **row,column**, 1-based, row 1 at the top. Folder keys end in `>`. Reserved keys are in brackets.

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 1** | BAT | RPM | FUEL PMP | PARK | GEAR | FLAPS | TRIM > | VIEWS > |
| **Row 2** | AP | HDG | ALT | VS | NAV | APR | FLC | FD |
| **Row 3** | COM1 | XPDR | ATC | MAP | CDI | BARO | [Timer] | CHECKLIST > |
| **Row 4** | NAV LT | BCN | STRB | LDG | TAXI | PITOT | [Anti-ice] | MORE > |

## Key table

Action names are the PilotsDeck README's: **Dynamic Button**, **Display Value**, **COM Radio**,
**Simple Button**. **Folder** = the Stream Deck app's own folder action ("Create Folder"), which opens
a child page. "Empty" = no action on that key. Templates T1 to T5 are explained under
"What each key holds". Source tags are listed under "Sources".

| Pos | Title | Action | Template | Command [source] | Read [source] | Display |
|---|---|---|---|---|---|---|
| 1,1 | `BAT` | Dynamic Button | T1 (template) | `B:electrical_battery_1`, On `1` / Off `0` [AM, IE 141] | `B:electrical_battery_1` [AM] | On/Off image, Special State |
| 1,2 | `RPM` | Display Value | T3 | none | `(A:GENERAL ENG RPM:1, rpm)` [SDK-ENGV] | Format `1.0` |
| 1,3 | `FUEL PMP` | Dynamic Button | T1 | `B:fuel_pump_1`, On `1` / Off `0` [IE 179] | `B:fuel_pump_1` [IE 179] | On/Off image, Special State |
| 1,4 | `PARK` | Dynamic Button | T2 (copy of Phase 1 key) | `K:PARKING_BRAKES` [AM] | `(A:BRAKE PARKING POSITION, Bool)` [AM, SDK-GEARV] | On/Off image |
| 1,5 | `GEAR` | Display Value | T3 | none | `(A:IS GEAR RETRACTABLE, Bool)` [SDK-GEARV] | Mappings `0=FIXED:1=RETR` |
| 1,6 | `FLAPS` | Display Value | T3 | Main `K:FLAPS_INCR`, Second (long press) `K:FLAPS_DECR` [SDK-FCE, README 2.1] | `(A:FLAPS HANDLE INDEX, number)` [SDK-CTLV] | Mappings `0=UP:1=10:2=20:3=30` |
| 1,7 | `TRIM` | Folder | (Stream Deck) | Opens the child page **trim** | none | Folder; the page's keys: [phase2-trim-views.md](phase2-trim-views.md) |
| 1,8 | `VIEWS` | Folder | (Stream Deck) | Opens the child page **views** | none | Folder; the page's keys: [phase2-trim-views.md](phase2-trim-views.md) |
| 2,1 | `AP` | Dynamic Button | T2 (template) | `K:AP_MASTER` [AM] | `(A:AUTOPILOT MASTER, Bool)` [AM] | On/Off image |
| 2,2 | `HDG` | Dynamic Button | T2 | `K:AP_HDG_HOLD` [SDK-APE] | `(A:AUTOPILOT HEADING LOCK, Bool)` [SDK-APV] | On/Off image |
| 2,3 | `ALT` | Dynamic Button | T2 | `K:AP_ALT_HOLD` [SDK-APE] | `(A:AUTOPILOT ALTITUDE LOCK, Bool)` [SDK-APV] | On/Off image |
| 2,4 | `VS` | Dynamic Button | T2 | `K:AP_VS_HOLD` [SDK-APE] | `(A:AUTOPILOT VERTICAL HOLD, Bool)` [SDK-APV] | On/Off image |
| 2,5 | `NAV` | Dynamic Button | T2 | `K:AP_NAV1_HOLD` [SDK-APE] | `(A:AUTOPILOT NAV1 LOCK, Bool)` [SDK-APV] | On/Off image |
| 2,6 | `APR` | Dynamic Button | T2 | `K:AP_APR_HOLD` [SDK-APE] | `(A:AUTOPILOT APPROACH HOLD, Bool)` [SDK-APV] | On/Off image |
| 2,7 | `FLC` | Dynamic Button | T2 | `K:FLIGHT_LEVEL_CHANGE` [SDK-APE] | `(A:AUTOPILOT FLIGHT LEVEL CHANGE, Bool)` [SDK-APV] | On/Off image |
| 2,8 | `FD` | Dynamic Button | T2 | `K:TOGGLE_FLIGHT_DIRECTOR` [SDK-APE] | `(A:AUTOPILOT FLIGHT DIRECTOR ACTIVE, Bool)` [SDK-APV] | On/Off image |
| 3,1 | `COM1` | COM Radio | T4 | `K:COM_STBY_RADIO_SWAP` [SDK-RADE] | Active `(A:COM ACTIVE FREQUENCY:1, MHz)`, Standby `(A:COM STANDBY FREQUENCY:1, MHz)` [SDK-RADV, SDK-UNITS] | Format `3` |
| 3,2 | `XPDR` | Display Value | T3 | none | `(A:TRANSPONDER CODE:1, Bco16)` [SDK-RADV] | Decode BCD, Format `4.0` |
| 3,3 | `ATC` | Simple Button | T5 | `K:SIMUI_WINDOW_HIDESHOW` [SDK-MISCE] | none (a sim window has no state) | fixed image |
| 3,4 | `MAP` | Simple Button | T5 | `K:FLIGHT_MAP` [SDK-MISCE] | none (a sim window has no state) | fixed image |
| 3,5 | `CDI` | Display Value | T3 | `K:TOGGLE_GPS_DRIVES_NAV1` [SDK-RADE] | `(A:GPS DRIVES NAV1, Bool)` [SDK-RADV] | Mappings `0=VLOC:1=GPS` |
| 3,6 | `BARO` | Display Value | T3 | `K:BAROMETRIC` [SDK-INSTE] | `(A:KOHLSMAN SETTING HG:1, inHg)` [SDK-SYSV] | Format `2.2` |
| 3,7 | | Empty | | | | Reserved: Timer |
| 3,8 | `CHECKLIST` | Folder | (Stream Deck) | Opens the child page **checklist** | none | Folder; the page holds only the back key (1,1) |
| 4,1 | `NAV LT` | Dynamic Button | T1 | `B:lighting_nav_0`, On `1` / Off `0` [IE 197] | `B:lighting_nav_0` [IE 197] | On/Off image, Special State |
| 4,2 | `BCN` | Dynamic Button | T1 | `B:lighting_beacon_1`, On `1` / Off `0` [IE 193] | `B:lighting_beacon_1` [IE 193] | On/Off image, Special State |
| 4,3 | `STRB` | Dynamic Button | T1 | `B:lighting_strobe_0`, On `1` / Off `0` [IE 202] | `B:lighting_strobe_0` [IE 202] | On/Off image, Special State |
| 4,4 | `LDG` | Dynamic Button | T1 | `B:lighting_landing_1`, On `1` / Off `0` [IE 196] | `B:lighting_landing_1` [IE 196] | On/Off image, Special State |
| 4,5 | `TAXI` | Dynamic Button | T1 | `B:lighting_taxi_1`, On `1` / Off `0` [IE 203] | `B:lighting_taxi_1` [IE 203] | On/Off image, Special State |
| 4,6 | `PITOT` | Dynamic Button | T1 | `B:deice_pitot_1`, On `1` / Off `0` [IE 139] | `B:deice_pitot_1` [IE 139] | On/Off image, Special State |
| 4,7 | | Empty | | | | Reserved: Anti-ice (the C172 has none beyond pitot heat) |
| 4,8 | `MORE` | Folder | (Stream Deck) | Opens the child page **more** | none | Folder; the page's keys: [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md) |

What each key means on a C172:
- **Engine** is the RPM display (read only). Starter and magnetos stay in the cockpit: no
  irreversible engine command sits on the deck.
- **Fuel** is the electric fuel pump switch.
- **GEAR** shows the aircraft's gear type (`FIXED` on the C172); it sends nothing.
- **Speed** is the G1000's FLC mode (the C172 has no autothrottle).
- **HDG, ALT, VS, FLC** show the mode state only (on/off). The selected heading, altitude, vertical speed
  and speed are not on this page: Phase 3's "selected heading and altitude" item stays open.
- **FLAPS**: press = one notch down (`K:FLAPS_INCR`), long press = one notch up (`K:FLAPS_DECR`). If you
  prefer it the other way round after the test, ask and the two commands get swapped.
- **ATC** and **MAP** open sim windows. They show a fixed image and no state, because there is no state
  to read. If the sim test shows either one does nothing in MSFS 2024, that key becomes Empty and its row
  in aircraft-mappings.md is marked "does not work" (the row stays as a record).

## Sources

| Tag | Source |
|---|---|
| README | PilotsDeck README, https://github.com/Fragtality/PilotsDeck/blob/master/README.md (2.1.1 address syntax, 2.1.2 command options, 2.2.2 common options, action descriptions) |
| SDK-APV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-autopilot-and-assistant-variables/ |
| SDK-APE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-autopilot-and-flight-assistance-events/ |
| SDK-SYSV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-system-variables/ |
| SDK-RADV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-radio-navigation-variables/ |
| SDK-CTLV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-control-variables/ |
| SDK-GEARV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-brake-and-landing-gear-variables/ |
| SDK-ENGV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-engine-variables/ |
| SDK-UNITS | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/simulation-variable-units/ |
| SDK-ELECE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-electrical-events/ |
| SDK-FCE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-flight-control-events/ |
| SDK-RADE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-radio-navigation-events/ |
| SDK-INSTE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-instrumentation-events/ |
| SDK-MISCE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/miscellaneous-events/ |
| SDK-AMISCE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-miscellaneous-events/ |
| SDK-ENGE | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/key-events/aircraft-engine-events/ |
| IE n | [reference/InputEvents-C172-G1000.txt](reference/InputEvents-C172-G1000.txt), line n |
| AM | [aircraft-mappings.md](aircraft-mappings.md), a row already verified in the sim (2026-11-11, MSFS 1.9.24.0) |
| P1 | the Phase 1 profile `MSFS2024 C172 POC`: the verified keys BAT, PARK, HDG, AP |

Address syntax is the README's section 2.1.1: A: plus name, index and unit in brackets for SimVars,
K: plus the event name for SimConnect events, B: plus the name for the aircraft's input events (B-Vars).

## Import the profile

The profile is the file
`pilotsdeck/MSFS2024-XL/_Package/Profiles/MSFS2024 C172 G1000.streamDeckProfile`, generated in the repo
(see "Regenerating the profile"). Signed in as Admin:

1. Back up your existing Stream Deck profiles (see [installation.md](installation.md#back-up-existing-profiles)).
2. **A profile already named `MSFS2024 C172 G1000`** (for example one you started by hand, or an older
   generated version): export it to the backup folder, then delete it in the Stream Deck app **before**
   you import. Don't keep two profiles with this name: the Profile Manager finds profiles by name. After
   replacing a profile, check its aircraft mapping in the Profile Manager. (On 2026-11-11 no profile of
   this name was installed.)
3. Leave the Phase 1 profile **`MSFS2024 C172 POC`** as it is. The new profile has its own copies of the
   four verified keys.
4. With the Stream Deck app running, **double-click the file** in Explorer (or in the Stream Deck app:
   Preferences > Profiles > Import). If the app asks which device, pick the **Stream Deck XL**. If the app
   asks to confirm, choose **Install**. Importing
   doesn't switch the device to the profile: select **`MSFS2024 C172 G1000`** in the profile list.
5. Run the import and round-trip steps of the checklist (the keys against the tables below; each folder
   opens and its back key returns to the main page).
6. Start MSFS 2024, load a free flight in the **Cessna 172 Skyhawk G1000**, cold and dark or parked.
   Wait for the PilotsDeck keys to stop showing the hourglass ("Waiting" state).

On import the Stream Deck app gives the profile, its pages and its keys new IDs and relinks the folder
keys (the installed MSFS-Fenix320-XL profile has other IDs than its export file). What a key does doesn't
change. The folder keys should show the Stream Deck app's own folder look (not yet seen: they carry no image
of their own, and the checklist records how they look); the project has no images of its own yet.

### Regenerating the profile

From the repo root (Python 3, standard library only):

```powershell
python tools/profilegen/generate.py
python tools/profilegen/check.py
```

`generate.py` reads `tools/profilegen/c172-g1000.json` (the pages and keys), `tools/profilegen/templates.json`
(real saved keys it copies) and the Phase 1 export, and writes the profile. The same inputs always give the
same file, byte for byte, with the same Python build (the committed profile was built with Python 3.14.10,
zlib 1.3.1.zlib-ng; another zlib may compress differently, the content stays the same). `check.py` reads
only files in the repo: it compares the profile with this doc's Key table, the Phase 1 export, the
templates and a fresh build (entry names, order and uncompressed content, so a profile not regenerated after
a data change fails). A change to a key goes into the data file and this doc together; then regenerate, run
the check and import the new file (step 2 above).

`python tools/profilegen/check.py --sources` is a provenance check on top: it re-reads the files the
templates came from (the Admin account's installed Stream Deck profiles, which must be unchanged, and
`A:\FS2024 Stuff\PilotsDeck`) and compares the folder and back keys with the Fenix XL export. It needs the
Admin account; a source it can't read is reported as SKIP with its path, not as a failure.

If the Stream Deck app ever refuses the generated file, the first thing to try in `generate.py` is the zip
entry header the app itself writes (`create_system = 10` and flag `0x800`).

## Changing a key by hand

Only to try a fallback or a value during a test. Record what you changed, so it goes into the data file and
this doc and the profile is regenerated; a hand change is lost at the next import.

**Saving fields:** the Stream Deck settings panel saves a text field when you leave it. After typing a
value, press **Tab** (or click elsewhere in the panel) before selecting another key, or the value is lost.
A key that always shows its Off image usually has an empty On Value / Off Value on the **On/Off States** tab.

**K-events are command-only:** with Command Type "MSFS: K-Var (SimEvent)", leave the Commands tab's
On/Off Value empty and **Toggle Switch** unchecked (that option is for push/pull controls that need two commands).

**B-Var switches: "Run as Command" unchecked.** With Command Type "MSFS: B-Var (InputEvent)", "Run as
Command" checked sends the B-Var with no value, and the key does nothing. Unchecked, the B-Var is read and
written as a variable with the On/Off values. Fill **both** On Value `1` and Off Value `0` (the Phase 1
re-export fixed exactly a missing Off Value).

**B-Vars resolve only after the flight loads.** Until the plugin has received the aircraft's input events,
B-Var keys can show Off or the Special State image for a moment. Wait for the hourglass to clear before you
judge a key.

**Copy names exactly.** Some light B-Vars end in `_0`, others in `_1` (for example `B:lighting_nav_0` but
`B:lighting_beacon_1`). Don't "correct" an index.

**Field names.** The Commands, Value and On/Off States tab names are the ones Phase 1 used. The other field
names below (Special State, Any Value, Special Image, Mappings, Format, Different Format, Decode BCD,
Main Command, Second Command, Active, Standby, Swap Image, Swap Active, Background Image) are the README's;
which tab each sits on in 0.9.7 was not checked. Look for the field by its name. The Second Command only
works once the key's long-press option is switched on; the README names no label for it (a saved key
stores it as `HasLongPress`), so look for the option next to the Second Command.

**Copying a key.** Two ways, both in the README:
- Stream Deck app copy and paste: select the key, copy it, select the target position (in this profile
  or another), paste.
- PilotsDeck **COPY** / **PASTE** (common options): COPY puts the selected key's configuration on the
  clipboard; PASTE applies it to the selected key, which must be the **same action type** (drop a fresh
  action of that type on the target position first).

Either way, check the Title afterwards and set it as the table says.

## What each key holds

The page is built from five templates: a template key in full, then copies of it with only the fields
listed for each copy changed. The generator does exactly this ("copy" below = it copies that saved key;
"drop a new" = it starts from a saved key of that action type, see `tools/profilegen/templates.json`).
The steps under T1 to T5 describe what the generator did; follow them by hand only when you change a key
by hand (see "Changing a key by hand").

| Template | Built from | Copies |
|---|---|---|
| T1 B-Var switch (Dynamic Button) | BAT, copied from P1 | FUEL PMP, NAV LT, BCN, STRB, LDG, TAXI, PITOT |
| T2 K-event mode (Dynamic Button) | AP, copied from P1 | PARK (copied from P1 as is); HDG, ALT, VS, NAV, APR, FLC, FD |
| T3 Display Value | HDG, copied from P1 | RPM, GEAR, FLAPS, XPDR, CDI, BARO |
| T4 COM Radio | new | COM1 only |
| T5 Simple Button | new | ATC, then MAP |

### T1: B-Var switch. Template key 1,1 BAT

Copy the Phase 1 BAT key (top-left of `MSFS2024 C172 POC`) to position 1,1 of the new profile. It must
end up exactly like this (the Special State row is new on this page):

| Tab | Field | Value |
|---|---|---|
| Commands | Command Type | MSFS: B-Var (InputEvent) |
| | Command Address | `B:electrical_battery_1` |
| | Run as Command | **unchecked** |
| | On Value / Off Value | `1` / `0` |
| Value | Address | `B:electrical_battery_1` |
| On/Off States | On Value / On Image | `1` / `Images/KorryOnBlueTop.png` (as in Phase 1) |
| | Off Value / Off Image | `0` / `Images/KorryOffWhiteBottom.png` (as in Phase 1) |
| | Special State | **enabled**, **Any Value** checked, Special Image `Images/Fault.png` |
| (Stream Deck) | Title | `BAT` |

The Special State shows the Fault image for any value that is neither On nor Off, so a B-Var that
reports something other than `1`/`0` is visible instead of looking "off" (README: Dynamic Button,
Special State, "Any Value"). Add it on BAT **before** you make the copies, so every copy has it.

**Why not the standard battery SimVar and K-event:** in the 2024 C172 the cockpit BAT switch drives
battery index 2 and the input event, while `K:TOGGLE_MASTER_BATTERY` and
`(A:ELECTRICAL MASTER BATTERY:1, Bool)` act on index 1 (tested 2026-11-11, see aircraft-mappings.md).
The same rule applies to every switch in this template: where the aircraft lists an input event for a
switch, the key reads and writes that B-Var. The standard SimVar/K-event pair is only the fallback
(see "Fallbacks").

**Copies of T1.** For each, copy BAT to the position and change these fields (the Commands tab Command
Address and the Value tab Address are always the same B-Var):

| Pos | Command Address and Value Address | Title | Source |
|---|---|---|---|
| 1,3 | `B:fuel_pump_1` | `FUEL PMP` | IE 179 |
| 4,1 | `B:lighting_nav_0` | `NAV LT` | IE 197 |
| 4,2 | `B:lighting_beacon_1` | `BCN` | IE 193 |
| 4,3 | `B:lighting_strobe_0` | `STRB` | IE 202 |
| 4,4 | `B:lighting_landing_1` | `LDG` | IE 196 |
| 4,5 | `B:lighting_taxi_1` | `TAXI` | IE 203 |
| 4,6 | `B:deice_pitot_1` | `PITOT` | IE 139 |

The 4,1 title is `NAV LT` so it isn't mixed up with the autopilot's `NAV` key (2,5). You can rename it
when you set it up.

Only the battery's `1`/`0` is verified. For the other switches `1` = on, `0` = off is an assumption; the
checklist's diagnostic step finds the real values, and the On/Off values change if they differ.

### T2: K-event mode. Template key 2,1 AP

Copy the Phase 1 AP key to position 2,1. It must end up exactly like this:

| Tab | Field | Value |
|---|---|---|
| Commands | Command Type | MSFS: K-Var (SimEvent) |
| | Command Address | `K:AP_MASTER` |
| | On Value / Off Value | empty (K-events are command-only) |
| | Toggle Switch | unchecked |
| Value | Address | `(A:AUTOPILOT MASTER, Bool)` |
| On/Off States | On Value / On Image | `1` / `Images/KorryOnBlueTop.png` |
| | Off Value / Off Image | `0` / `Images/KorryOffWhiteBottom.png` |
| (Stream Deck) | Title | `AP` |

The autopilot needs avionics power: with the battery or avionics off, the AP keys stay "off". That's
correct behaviour, not a failure.

**PARK (1,4):** copy the Phase 1 PARK key to position 1,4 and change nothing (`K:PARKING_BRAKES`,
`(A:BRAKE PARKING POSITION, Bool)`, On `1` / Off `0`, Title `PARK`). Don't switch it to
`B:landing_gear_parkingbrake` [IE 192]: the verified pair already follows the cockpit.

**Copies of T2 (the G1000 autopilot modes).** For each, copy AP to the position and change these fields:

| Pos | Commands: Command Address | Value: Address | Title | Source |
|---|---|---|---|---|
| 2,2 | `K:AP_HDG_HOLD` | `(A:AUTOPILOT HEADING LOCK, Bool)` | `HDG` | SDK-APE, SDK-APV |
| 2,3 | `K:AP_ALT_HOLD` | `(A:AUTOPILOT ALTITUDE LOCK, Bool)` | `ALT` | SDK-APE, SDK-APV |
| 2,4 | `K:AP_VS_HOLD` | `(A:AUTOPILOT VERTICAL HOLD, Bool)` | `VS` | SDK-APE, SDK-APV |
| 2,5 | `K:AP_NAV1_HOLD` | `(A:AUTOPILOT NAV1 LOCK, Bool)` | `NAV` | SDK-APE, SDK-APV |
| 2,6 | `K:AP_APR_HOLD` | `(A:AUTOPILOT APPROACH HOLD, Bool)` | `APR` | SDK-APE, SDK-APV |
| 2,7 | `K:FLIGHT_LEVEL_CHANGE` | `(A:AUTOPILOT FLIGHT LEVEL CHANGE, Bool)` | `FLC` | SDK-APE, SDK-APV |
| 2,8 | `K:TOGGLE_FLIGHT_DIRECTOR` | `(A:AUTOPILOT FLIGHT DIRECTOR ACTIVE, Bool)` | `FD` | SDK-APE, SDK-APV |

These are push-button modes with no readable switch B-Var, so they read SimVars and send K-events (as the
verified AP key does). Only `K:AP_MASTER` is verified in this aircraft; the checklist's mouse test on the
G1000 bezel is what proves the others. NAV mode with the CDI on GPS may not set `NAV1 LOCK`: the
checklist tests both CDI sources.

### T3: Display Value. Template key 1,2 RPM

Copy the Phase 1 HDG key (a Display Value) to position 1,2 and change it to this:

| Tab | Field | Value |
|---|---|---|
| Value | Address | `(A:GENERAL ENG RPM:1, rpm)` [SDK-ENGV] |
| | Format | `1.0` (no decimals, e.g. `2350`) |
| | Mappings | empty |
| | Decode BCD | unchecked |
| Commands | Command | none (as in Phase 1) |
| (Stream Deck) | Title | `RPM` |

Format syntax is the README's `Zeros.Fraction:Text %s Text` (the Phase 1 HDG key used `3.0:%s°`).
Mappings syntax is `value=Text`, separated by `:` (README, Display Value). PilotsDeck applies
Decode BCD, then Scale, then Round, then the mapping, then Format.

**Copies of T3.** Copy RPM (or the Phase 1 HDG key) to the position, then set these fields; anything not
listed stays as on RPM:

**1,5 GEAR** (shows the gear type; sends nothing)

| Tab | Field | Value |
|---|---|---|
| Value | Address | `(A:IS GEAR RETRACTABLE, Bool)` [SDK-GEARV] |
| | Format | empty |
| | Mappings | `0=FIXED:1=RETR` |
| (Stream Deck) | Title | `GEAR` |

**1,6 FLAPS** (shows the flap handle position; press = one notch down, long press = one notch up)

| Tab | Field | Value |
|---|---|---|
| Value | Address | `(A:FLAPS HANDLE INDEX, number)` [SDK-CTLV] |
| | Format | empty |
| | Mappings | `0=UP:1=10:2=20:3=30` |
| Commands | Main Command: Command Type / Address | MSFS: K-Var (SimEvent) / `K:FLAPS_INCR` [SDK-FCE] |
| | Main Command: On Value / Off Value, Toggle Switch | empty, unchecked |
| | Long press (the option that switches the Second Command on; saved as `HasLongPress`) | **enabled** |
| | Second Command (long press, >= 500 ms): Command Type / Address | MSFS: K-Var (SimEvent) / `K:FLAPS_DECR` [SDK-FCE] |
| | Second Command: On Value / Off Value | empty |
| (Stream Deck) | Title | `FLAPS` |

Four handle positions (0 to 3) is an assumption: the checklist reads
`(A:FLAPS NUM HANDLE POSITIONS, number)` [SDK-CTLV] to check it. The SDK doesn't say whether UP counts,
so `3` or `4` both fit; the checklist's flaps-lever line decides, and the mapping changes if it differs.

**3,2 XPDR** (display only; code entry and IDENT come on a later page)

| Tab | Field | Value |
|---|---|---|
| Value | Address | `(A:TRANSPONDER CODE:1, Bco16)` [SDK-RADV] |
| | Decode BCD | **checked** |
| | Format | `4.0` (four digits, e.g. `1200`, `0400`) |
| | Mappings | empty |
| (Stream Deck) | Title | `XPDR` |

**3,5 CDI** (shows the CDI source; a press toggles it)

| Tab | Field | Value |
|---|---|---|
| Value | Address | `(A:GPS DRIVES NAV1, Bool)` [SDK-RADV] |
| | Format | empty |
| | Mappings | `0=VLOC:1=GPS` |
| Commands | Command Type / Command Address | MSFS: K-Var (SimEvent) / `K:TOGGLE_GPS_DRIVES_NAV1` [SDK-RADE] |
| | On Value / Off Value, Toggle Switch | empty, unchecked |
| (Stream Deck) | Title | `CDI` |

Whether the G1000's CDI softkey and this SimVar/event stay in step is an assumption; the checklist tests
it with the mouse on the CDI softkey.

**3,6 BARO** (shows the altimeter setting; a press syncs it)

| Tab | Field | Value |
|---|---|---|
| Value | Address | `(A:KOHLSMAN SETTING HG:1, inHg)` [SDK-SYSV] |
| | Format | `2.2` (e.g. `29.92`) |
| | Mappings | empty |
| Commands | Command Type / Command Address | MSFS: K-Var (SimEvent) / `K:BAROMETRIC` [SDK-INSTE] |
| | On Value / Off Value, Toggle Switch | empty, unchecked |
| (Stream Deck) | Title | `BARO` |

`K:BAROMETRIC` "syncs altimeter setting to sea level pressure, or 29.92 if above 18000 feet" (SDK-INSTE).
Altimeter index 1 is an assumption (the battery turned out to be on index 2): the checklist records which
index the PFD baro shows on, and the Value address's `:1` changes if it is another one. `K:BAROMETRIC`
takes no altimeter index (SDK-INSTE names none), so changing the index doesn't change the press: if the
PFD is on another index, the checklist checks again that a BARO press changes the PFD baro. The baro
knob's input event `B:as1000_baro_pfd` (IE 38) exists but is not used.

### T4: COM Radio. Key 3,1 COM1

Drop a new **PilotsDeck > COM Radio** action on position 3,1:

| Tab | Field | Value |
|---|---|---|
| Value | Active (top) | `(A:COM ACTIVE FREQUENCY:1, MHz)` [SDK-RADV, SDK-UNITS] |
| | Standby (bottom) | `(A:COM STANDBY FREQUENCY:1, MHz)` [SDK-RADV, SDK-UNITS] |
| | Format (one field, unless Different Format is ticked) | `3` (three decimals, e.g. `118.000`) |
| | Decode BCD | unchecked |
| Commands | Command Type / Command Address | MSFS: K-Var (SimEvent) / `K:COM_STBY_RADIO_SWAP` [SDK-RADE] |
| | On Value / Off Value, Toggle Switch | empty, unchecked |
| | Swap Image, Swap Active | leave the defaults (`Images/ArrowBright.png`, `1500`) |
| (Stream Deck) | Title | `COM1` |

`K:COM_STBY_RADIO_SWAP` "swaps COM 1 frequency with standby" (SDK-RADE). The SDK gives the unit of both
frequencies as `Frequency BCD16`; reading them in `MHz` is an assumption. If the key shows nonsense, use
the fallback (see "Fallbacks"). Tuning stays on the G1000 (a radio page comes later).

### T5: Simple Button. Keys 3,3 ATC and 3,4 MAP

Drop a new **PilotsDeck > Simple Button** on position 3,3:

| Tab | Field | Value |
|---|---|---|
| Commands | Command Type / Command Address | MSFS: K-Var (SimEvent) / `K:SIMUI_WINDOW_HIDESHOW` [SDK-MISCE] |
| | On Value / Off Value, Toggle Switch | empty, unchecked |
| | Background image | leave the default (`Images/Switch.png`) |
| (Stream Deck) | Title | `ATC` |

Copy it to position 3,4 and change: Command Address `K:FLIGHT_MAP` [SDK-MISCE], Title `MAP`.

These two keys show the same image all the time: a sim window has no state to read. **If the sim test
shows either one does nothing in MSFS 2024, that key becomes Empty** (delete the action) and its row in
aircraft-mappings.md is marked "does not work". The row stays.

### Folder keys and reserved keys

Four keys are Stream Deck folders (the app's "Create Folder" action). Each opens a child page; every child
page has its back key at **1,1** (top left), the same on every page, as in the MSFS-Fenix320-XL profile.
The Trim and Views pages hold their keys ([phase2-trim-views.md](phase2-trim-views.md)); More holds folder keys to the PFD, MFD and V-speeds pages ([phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md)); Checklist holds only that back key; its content comes in a later unit (see
[navigation.md](navigation.md)).

| Pos | Title | Opens | The child page holds now |
|---|---|---|---|
| 1,7 | `TRIM` | Trim page | its keys: [phase2-trim-views.md](phase2-trim-views.md) |
| 1,8 | `VIEWS` | Views | its keys: [phase2-trim-views.md](phase2-trim-views.md) |
| 3,8 | `CHECKLIST` | Checklists (Phase 5) | the back key (1,1) only |
| 4,8 | `MORE` | More: further pages (later units) | folder keys to the PFD, MFD and V-speeds pages: [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md) |

Two positions stay empty, so the grid doesn't move when later units fill them:

| Pos | Reserved for |
|---|---|
| 3,7 | Timer (no SimVar for the G1000 timer was found in the SDK) |
| 4,7 | Anti-ice: the C172 has no anti-ice system beyond pitot heat (4,6) |

## Fallbacks

Use a fallback only if the checklist shows the main address doesn't work, and say which one you used when
you report the result. Fallbacks are recorded in aircraft-mappings.md too; none is tested.

| Key | Fallback | Source |
|---|---|---|
| 1,3 FUEL PMP | Command `K:FUEL_PUMP:1` (K-event, command-only), read `(A:GENERAL ENG FUEL PUMP SWITCH:1, Bool)` | SDK-ENGE, SDK-ENGV |
| 1,6 FLAPS | Input event `B:handling_flaps` exists; its values are unknown, so it is not used | IE 184 |
| 2,2 HDG | Command `B:as1000_autopilot_heading_pfd` (push value unknown: needs a sim test first) | IE 25 |
| 2,3 ALT | Command `B:as1000_autopilot_altitude_pfd` (as HDG) | IE 13 |
| 2,4 VS | Command `B:as1000_autopilot_verticalspeed_pfd` (as HDG) | IE 33 |
| 2,5 NAV | Command `B:as1000_autopilot_navigation_pfd` (as HDG) | IE 27 |
| 2,6 APR | Command `B:as1000_autopilot_approach_pfd` (as HDG) | IE 17 |
| 2,7 FLC | Command `B:as1000_autopilot_flightlevelchange_pfd` (as HDG) | IE 23 |
| 2,8 FD | Command `B:as1000_autopilot_fd_pfd` (as HDG) | IE 21 |
| 3,1 COM1 | Active `(A:COM ACTIVE FREQUENCY:1, Frequency BCD16)`, Standby `(A:COM STANDBY FREQUENCY:1, Frequency BCD16)`, Decode BCD checked, Format `2:1%s` (README example for BCD frequencies; shows two decimals only). If it shows `11850.00`, set Scalar `0.01` | SDK-RADV, README |
| 3,2 XPDR | `(A:TRANSPONDER CODE:1, number)`, Decode BCD unchecked | SDK-RADV, SDK-UNITS |
| 3,6 BARO | The altimeter index the checklist finds, e.g. `(A:KOHLSMAN SETTING HG:2, inHg)` | SDK-SYSV |
| 4,1 NAV LT | Command `K:TOGGLE_NAV_LIGHTS`, read `(A:LIGHT NAV, Bool)` | SDK-ELECE, SDK-SYSV |
| 4,2 BCN | Command `K:TOGGLE_BEACON_LIGHTS`, read `(A:LIGHT BEACON, Bool)` | SDK-ELECE, SDK-SYSV |
| 4,3 STRB | Command `K:STROBES_TOGGLE`, read `(A:LIGHT STROBE, Bool)` | SDK-ELECE, SDK-SYSV |
| 4,4 LDG | Command `K:LANDING_LIGHTS_TOGGLE`, read `(A:LIGHT LANDING, Bool)` | SDK-ELECE, SDK-SYSV |
| 4,5 TAXI | Command `K:TOGGLE_TAXI_LIGHTS`, read `(A:LIGHT TAXI, Bool)` | SDK-ELECE, SDK-SYSV |
| 4,6 PITOT | Command `K:PITOT_HEAT_TOGGLE`, read `(A:PITOT HEAT, Bool)` | SDK-AMISCE, SDK-SYSV |

A B-Var command that sends a value uses the README 2.1.1 form (the B-Var name, a colon, the value);
the value to send for a G1000 bezel button is not known yet (Phase 1: a B-Var sent with no value did
nothing), which is why the K-events come first.

## What the keys show when the sim isn't there

From the README: with no simulator running the plugin is **Idle** and keys show a static preview of their
configuration; with the sim running but no flight loaded it is **Waiting** and every key shows the
plugin's Wait image; a command that fails shows a yellow alert sign on the key for a moment. What a
Display Value shows for a value the sim doesn't supply is not in the README: the checklist's "Unavailable
value" block records it, including what COM1, XPDR, BARO, CDI and RPM show cold and dark with the battery off.

Nothing on this page uses keyboard bindings, vJoy or anything tied to a controller: every command is a
SimConnect event or an input event, so the page works the same with the Xbox Elite controller and the
T.16000M + TWCS.

## How to test

Run [tests/manual-checklist.md](../tests/manual-checklist.md), section "Phase 2: main page (C172 G1000)".
Do the diagnostic block first. The key test is again the reverse direction: **change each control with the
mouse in the cockpit and check that the key follows without being pressed.**

## When it passes

1. Any fallback, On/Off value or index that changed in the test goes into the data file
   `tools/profilegen/c172-g1000.json` and this doc; then the profile is regenerated (not exported from the
   app). The Profile Manager packs every profile in `_Package/Profiles/`; `package.json` doesn't list them.
2. Fill in the "Verified" column of the Phase 2 rows in aircraft-mappings.md with the date and sim
   version, for each key that passed. Mark ATC or MAP "does not work" if they did nothing.
3. Record any fallback you used, and any On/Off value or index that changed, in aircraft-mappings.md.
