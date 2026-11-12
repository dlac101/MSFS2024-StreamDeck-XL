# Page navigation

How the pages of a profile connect. Built so far: the C172 G1000 main page and four empty child pages
(see [phase2-main-page.md](phase2-main-page.md)). Everything marked **plan** is not built yet; the
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

## Pages

| Main page key | Child page | Holds now | Plan (not built) | Source |
|---|---|---|---|---|
| 1,7 `TRIM` | trim | back key only | Trim controls and trim position readout | original-plan.md, Phase 2 concept layout ("Trim page") |
| 1,8 `VIEWS` | views | back key only | Camera views. Must work without vJoy or controller bindings (to be researched) | original-plan.md, Phase 2 concept layout and "Universal" level ("views") |
| 3,8 `CHECKLIST` | checklist | back key only | Optional checklists and startup aids | original-plan.md, Phase 5 |
| 4,8 `MORE` | more | back key only | A menu of further folders (second level), for example: autopilot values (selected heading, altitude, VS, speed), radios (COM/NAV tuning, transponder code and IDENT) | original-plan.md, Phase 3; phase2-main-page.md (XPDR code entry, radio page, Phase 3 selected values) |

Main page positions 3,7 (Timer) and 4,7 (Anti-ice) stay reserved keys, not folders.

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
   then import the new file as phase2-main-page.md describes. `check.py` checks child pages that hold only
   the back key, and folder keys on the main page only: the first unit that fills a child page (or adds a
   second folder level) extends it first, so it checks that page's keys against the page's doc.
