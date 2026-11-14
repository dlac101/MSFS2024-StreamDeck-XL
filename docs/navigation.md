# Page navigation

How the pages of a profile connect. Built so far: the C172 G1000 main page, three filled child pages (Trim,
Views: [phase2-trim-views.md](phase2-trim-views.md); Sim rate: [phase2-sim-rate.md](phase2-sim-rate.md)), the More page with three second-level pages (PFD, MFD,
V-speeds: [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md)) and one empty child page, Checklist (see [phase2-main-page.md](phase2-main-page.md)). Everything marked **plan** is not built yet; the
page ideas come from [original-plan.md](original-plan.md).

## Rules

- **One main page per profile.** It is the page the profile opens on (the profile's only listed page).
  Every other page is a Stream Deck **folder**: a child page opened by a folder key ("Create Folder").
  Stream Deck's own page switching (several listed pages, "Go to page") is not used.
- **Back key at 1,1 (top left) on every child page**, the Stream Deck app's back key (`backtoparent`;
  named "Parent Folder" or "Open Folder" in saved profiles). It
  returns to the page the folder key sits on. The position never changes, so position 1,1 on a child
  page never holds a function. This is the form of the installed MSFS-Fenix320-XL profile: all 43 of its
  child pages have their back key at 1,1.
- **At most two levels below the main page** (main > folder > sub-folder), so any page is at most two
  back presses from the main page. The Fenix XL profile goes five levels deep; this project keeps it
  shallow on purpose.
- **Folder keys keep their positions** on the main page across versions and aircraft, so the grid stays
  familiar. A function that doesn't exist on an aircraft leaves its key empty instead of moving others.
- Nothing on any page depends on the connected flight controls (Xbox Elite or T.16000M/TWCS).
- **Key titles at 14 by default** (`tools/profilegen/generate.py`: on Simple and Dynamic Buttons a template
  title size of 10 becomes 14; keys at 15 and folder and back keys at 12 stay). Readout keys (COM Radio,
  Display Value) keep their template size, because they draw their values with the title font: COM1 stays 10.
  Where a title does not fit at 14, the key's `title_size` in the data file sets another size (10 to 15).
  Every key keeps its template's title alignment (folder and back keys at the bottom), except the main page
  folder keys VIEWS, CHECKLIST and MORE: their `title_align` in the data file is `"middle"` (the user's own
  saved edit; `title_align` takes the Elgato manifest State `TitleAlignment` values `"top"`, `"middle"`,
  `"bottom"`).

## Pages

| Main page key | Child page | Holds now | Plan (not built) | Source |
|---|---|---|---|---|
| 1,7 `TRIM` | trim | back key, elevator trim up/down, two trim readouts ([phase2-trim-views.md](phase2-trim-views.md), untested) | Trim controls and trim position readout | original-plan.md, Phase 2 concept layout ("Trim page") |
| 1,8 `VIEWS` | views | back key, 2 view keys (COCKPIT, EXTERNAL: A-Var writes to CAMERA STATE), 3 camera readouts ([phase2-trim-views.md](phase2-trim-views.md), EXTERNAL hand-tested, rest untested) | Camera views. Must work without vJoy or controller bindings (to be researched) | original-plan.md, Phase 2 concept layout and "Universal" level ("views") |
| 3,7 `SIM RATE` | simrate | back key, 1,2 `1X` (the Lua script XL24-SIMRATE.lua steps the rate back to 1x; lit at 1x), 1,3 `SLOWER` (one step down), 1,4 the RATE readout (press one step up, long press of a full second one step down) and 1,5 `FASTER` (one step up) ([phase2-sim-rate.md](phase2-sim-rate.md), repaired P2-6R, not yet sim-tested) | Sim rate: back to 1x, slower, faster and the rate readout (the user's layout, LR298-C5) | the user's request (P2-6, layout LR298-C5); position 3,7 was the Timer reservation |
| 3,8 `CHECKLIST` | checklist | back key only | Optional checklists and startup aids | original-plan.md, Phase 5 |
| 4,8 `MORE` | more | back key and four folder keys (second level, [phase2-g1000-vspeeds.md](phase2-g1000-vspeeds.md), untested): 1,2 `PFD` > pfd (G1000 PFD bezel: 12 softkeys, MENU, PROC, ENT, CLR, FPL, Direct-To, FMS and range knobs by H-event), 1,3 `MFD` > mfd (the same for the MFD), 1,4 `V-SPEEDS` > vspeeds (7 V-speed readouts), 1,5 `COM PAD` > compad (COM1 number pad: digits, CLR, ENT by the Lua script XL24-COMPAD.lua, a COM1 key and two readouts; [phase2-com1-pad.md](phase2-com1-pad.md), untested; position chosen by the user 2026-11-12) | Further folders (second level), for example: autopilot values (selected heading, altitude, VS, speed), NAV tuning, transponder code and IDENT (the same pad) | original-plan.md, Phase 3 and "aircraft-class" level (Garmin avionics); phase2-main-page.md (XPDR code entry, radio page, Phase 3 selected values) |

Main page position 4,7 (Anti-ice) stays a reserved key, not a folder. (3,7 was reserved for a timer; it
is the `SIM RATE` folder now, and a later timer unit takes a free position.)

Other aircraft (plan, Phase 4): each gets its own profile with its own permanent name, the same main-page
grid and the same folder positions where the function applies.

- **Page levels (plan):** original-plan.md sorts functions into three levels: universal (parking brake,
  gear, flaps, lights, ATC, maps, views, page navigation), aircraft-class (GA autopilot and Garmin avionics,
  airliner flight guidance and radios) and aircraft-specific (the C172 G1000 first).
- **Aircraft switching (plan):** original-plan.md asks for automatic switching by aircraft where PilotsDeck
  supports it (the Profile Manager's aircraft mappings), with safe fallback pages. Not built or tested yet.

## Adding a page

1. Add the page to the data file (`tools/profilegen/c172-g1000.json`): a page entry with its `id` and
   `parent`, and on the parent page a key with `"folder": "<id>"` and a title. The back key is added
   automatically at `back_key_pos`.
2. Add the page's keys and document them in the page's own doc, in the form of phase2-main-page.md.
3. Regenerate and check (`python tools/profilegen/generate.py`, then `python tools/profilegen/check.py`),
   then import the new file as phase2-main-page.md describes. `check.py` checks a child page against its
   doc when the page's entry in the data file names the doc (`"spec": "docs/<page doc>.md"`) and the doc has
   a table under the heading `## Key table: <page id>` in the main page's Key table form, listing all 32
   positions (`Back` at 1,1, `Empty` rows included); it then checks the page's keys key by key against
   that table. A child page with no `spec` must hold only its back key.
4. A second-level page (a folder key on a child page, as MORE's): give the first-level page a `spec` and a
   `## Key table: <page id>` with `Folder` rows, and give the new page `"parent": "<first-level page id>"`.
   `check.py` checks folder keys on every page (each opens the child page the data file and the doc's row
   name, and no page is opened twice), the back key at 1,1 on every child page, and at most two folder
   levels below the main page: a folder key on a second-level page fails the check.
