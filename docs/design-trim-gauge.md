# Design: elevator trim gauge, Cessna 172 G1000

**Status: built (P3-4), generated, not yet sim-tested.** The key is in the profile; its reference is
[phase2-trim-views.md](phase2-trim-views.md) (trim 3,4). It adds no new variable: the gauge reads the same
SimVar as the trim page's `TRIM` readout (3,2) did until P3-TRIM2 took that readout off, which is already in
[aircraft-mappings.md](aircraft-mappings.md) as Unverified.

Goal: show the elevator trim as a bar with a pointer, as the Flight Tracker Stream Deck plugin (FT-SD) does
with its custom gauge (the user likes how it shows trim), instead of only a number. PilotsDeck has its own
action for this, **Display Gauge** (README 2.3): a bar or an arc, an indicator triangle at the current
value, an optional center line and the value as text. No Lua and no plugin change are needed.

## Where it sits

Trim page (main 1,7 `TRIM`), new key at **3,4**. The page's keys at the time (P3-4) stayed as they were
([phase2-trim-views.md](phase2-trim-views.md)): `TRIM UP` 2,2, `TRIM` 3,2 (percent), `TRIM DEG` 3,3,
`TRIM DN` 4,2. After the trim page's sim test, the user may move the gauge to 3,2 in place of the
percent readout (the gauge also draws the number), so the column reads UP, gauge, DN. P3-TRIM2 later took
`TRIM` 3,2 and `TRIM DEG` 3,3 off and added aileron and rudder trim keys and gauges; the page as it is
now is in [phase2-trim-views.md](phase2-trim-views.md).

| | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 | Col 7 | Col 8 |
|---|---|---|---|---|---|---|---|---|
| **Row 2** | | TRIM UP | | | | | | |
| **Row 3** | | TRIM | TRIM DEG | **TRIM gauge (new)** | | | | |
| **Row 4** | | TRIM DN | | | | | | |

## The key

| Field (Display Gauge) | Value | Why |
|---|---|---|
| Address | `(A:ELEVATOR TRIM PCT EX2, percent)` | Same as 3,2 had (until P3-TRIM2) [SDK-CTLV]: -100 = down limit, 0 = neutral, 100 = up limit |
| Minimum / Maximum | `-100` / `100` | The SimVar's range |
| Draw Arc | off (a bar) | FT-SD's trim gauges are bars; a trim wheel moves in a line |
| Orientation | vertical, values increasing **up** | Matches TRIM UP above and TRIM DN below on the same page |
| Size | `52; 12` (length; thickness: PilotsDeck sizes the bar before it turns it), Offset `-6; 0` | Tall, narrow bar; adjust in the panel |
| Center Line | on, white | Marks neutral (0) |
| Indicator | on, triangle, a bright color (yellow) | The pointer FT-SD calls the chevron |
| Warning Range | off | No source gives the C172's takeoff trim range, so none is drawn (not invented) |
| Text | on, Format `1.0` | The percent as a number under or beside the bar |
| Title | `TRIM`, top | As FT-SD's header |

The generator's template is `display_gauge` in `tools/profilegen/templates.json`, derived from the Phase 1
HDG key (`p1:2,0`, a Display Value saved by PilotsDeck 0.9.7: every simple PilotsDeck action saves the same
settings). The MSFS-Fenix320-XL profile's 18 Display Gauge keys are arcs saved by older builds
(BUILD_VERSION 7 and 10); they were a lead for the field names (`DrawArc`, `BarOrientation`, `GaugeSize`,
`Offset`, `CenterLine`, `IndicatorSize`, `IndicatorColor`, `ShowText`, `Format`, `MinimumValue`,
`MaximumValue`) only, and no file is copied. `BarOrientation` Up = `-90`, from the PilotsDeck source
(IAction.cs) and the installed plugin's own code; no hand-saved key was needed. PilotsDeck draws the number
on the turned bar, so on this vertical bar it stands sideways on the right edge and reads bottom to top.

## Icon build option (local only, never committed)

The Guenseli icon pack holds gauge **parts**, not finished gauges: faces, scales, needles, arrows and
masks that a Display Gauge or a Composite Action draws its moving part over. For pitch trim there are, for
example:

- `FSR 500 Turboprop/icons/Trim_back.png`: a pitch trim face labelled DOWN at the top, T/O RNG in the
  middle and UP at the bottom (so with this face the bar must increase **downward**).
- `LORBY SD Gauges/Trim_Pitch_Back.png` with `Trim_Pitch_Arrow.png`, and `pitch_trim_scale.png`.
- `Standard Avionics Suite/icons/Trim_PITCH.png` (white on transparent).

In the local icon build (`generate.py --icons`, [icons.md](icons.md)) the gauge key could take one of these as
its background. For now it takes none: `tools/profilegen/icons-c172-g1000.json` leaves trim 3,4 as it is (no
pack face is known to fit an upward bar). The pack's licence is personal use only, so this stays in the
git-ignored local build.
A needle-over-face gauge (Composite Action) would look closest to a real instrument but needs more setup;
the plain Display Gauge comes first.

## How to test

The steps are in [tests/manual-checklist.md](../tests/manual-checklist.md), section "P3-4: Trim gauge (C172
G1000)". In short:

1. Trim fully down, neutral and fully up with the cockpit wheel: the pointer goes to the bottom, the
   center line and the top; the number goes from -100 through 0 to 100.
2. TRIM UP / TRIM DN on the deck: the pointer and the number go up / down with each press.

## Sources

| Tag | Source |
|---|---|
| README | PilotsDeck README, https://github.com/Fragtality/PilotsDeck/blob/master/README.md, 2.3 "Display Gauge" (bar or arc, Orientation, Size `Width; Height`, Indicator, Center Line, Warning Range, Text Settings) |
| SDK-CTLV | https://docs.flightsimulator.com/msfs2024/retail/programming-apis/simvars/aircraft-simvars/aircraft-control-variables/ (`ELEVATOR TRIM PCT EX2`) |
| FT-SD | https://github.com/nguyenquyhy/Flight-Tracker-StreamDeck (GPL-3.0), docs/USERGUIDE.md "Generic Gauge" (custom gauge, trim example). Idea only; no code or images taken. |
| REF-FNX | The MSFS-Fenix320-XL profile in ProfilesV3: saved Display Gauge keys (`com.extension.pilotsdeck.action.display.gauge`). Lead for field names only. |
