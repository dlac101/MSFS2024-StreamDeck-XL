-- XL24-A32NX.lua: FCU readouts and ND steps for the MSFS2024 A32NX profile (PilotsDeck standard script).
-- Page and keys: docs/phase4-a32nx.md. Not yet sim-tested.
-- EFIS page keys (ADF/VOR steps, MASTER WARN/CAUT press): docs/phase4-a32nx-efis.md.
-- OVHD systems page key (fuel MODE SEL press): docs/phase4-a32nx-overhead.md.
-- RADIO and XPDR page keys: docs/phase4-a32nx-radios.md.
-- PED page keys: docs/phase4-a32nx-pedestal.md.
--
-- Readout keys (Display Value) use SPD, HDG, ALT, VS and BARO as their Value Address
-- ("lua:XL24-A32NX:SPD"); PilotsDeck runs them on every process cycle and shows the text they
-- return. Each one reads the FlyByWire A32NX FCU display L-Vars (fbw-a32nx/docs/a320-simvars.md,
-- "A32NX_FCU_AFS_DISPLAY_{name}_VALUE", dashes and managed-dot L-Vars; the EFIS baro L-Vars of the
-- FlyByWire Flight Deck API) and returns "" when L:A32NX_FCU_HEALTHY is not 1 (no A32NX loaded, or
-- the FCU unpowered): the key is blank, as the real FCU windows.
-- The ND keys call NDMODE(step) and NDRANGE(step) (command type Lua Function,
-- "lua:XL24-A32NX:NDMODE(1)", long press "(-1)"): they read the L-Var, add the step, keep it in
-- range and write it. The ND keys show the L-Var they read, never a value from this script.
-- The ADF/VOR keys (EFIS page) call NAV1(step) and NAV2(step): the switch positions left to right are ADF
-- (value 1), OFF (0), VOR (2) (FlyByWire Flight Deck API, A32NX_Interior_EFIS.xml); step 1 moves one
-- position toward VOR, -1 toward ADF, and stops at the ends; nothing when the FCU is not healthy.
-- The WARN and CAUT keys call MWARN() and MCAUT(): they press the Captain's MASTER WARN / MASTER CAUT
-- button as the cockpit does (A320_NEO_INTERIOR.xml: the push L-Var 1 on press, 0 on release), here 1,
-- 200 ms, 0; the FWC cancels on the 0 -> 1 edge (PseudoFWC.ts). The keys show the lamp L-Var they read.
-- PilotsDeck loads this script when a key that uses it appears and unloads it when none is left.

local HEALTHY    = "L:A32NX_FCU_HEALTHY"
local SPD_VALUE  = "L:A32NX_FCU_AFS_DISPLAY_SPD_MACH_VALUE"
local SPD_DASHES = "L:A32NX_FCU_AFS_DISPLAY_SPD_MACH_DASHES"
local SPD_DOT    = "L:A32NX_FCU_AFS_DISPLAY_SPD_MACH_MANAGED"
local MACH_MODE  = "L:A32NX_FCU_AFS_DISPLAY_MACH_MODE"
local HDG_VALUE  = "L:A32NX_FCU_AFS_DISPLAY_HDG_TRK_VALUE"
local HDG_DASHES = "L:A32NX_FCU_AFS_DISPLAY_HDG_TRK_DASHES"
local HDG_DOT    = "L:A32NX_FCU_AFS_DISPLAY_HDG_TRK_MANAGED"
local ALT_VALUE  = "L:A32NX_FCU_AFS_DISPLAY_ALT_VALUE"
local ALT_DOT    = "L:A32NX_FCU_AFS_DISPLAY_LVL_CH_MANAGED"
local VS_VALUE   = "L:A32NX_FCU_AFS_DISPLAY_VS_FPA_VALUE"
local VS_DASHES  = "L:A32NX_FCU_AFS_DISPLAY_VS_FPA_DASHES"
local FPA_MODE   = "L:A32NX_FCU_AFS_DISPLAY_TRK_FPA_MODE"     -- 1 = TRK/FPA
local BARO_VALUE = "L:A32NX_FCU_EFIS_L_DISPLAY_BARO_VALUE"
local BARO_MODE  = "L:A32NX_FCU_EFIS_L_DISPLAY_BARO_VALUE_MODE" -- 0 = STD, 1 = hPa, 2 = inHg
local ND_MODE    = "L:A32NX_FCU_EFIS_L_EFIS_MODE"             -- 0 ROSE ILS .. 4 PLAN
local ND_RANGE   = "L:A32NX_FCU_EFIS_L_EFIS_RANGE"            -- 0 = 10 .. 5 = 320
SimVar(HEALTHY)
SimVar(SPD_VALUE)
SimVar(SPD_DASHES)
SimVar(SPD_DOT)
SimVar(MACH_MODE)
SimVar(HDG_VALUE)
SimVar(HDG_DASHES)
SimVar(HDG_DOT)
SimVar(ALT_VALUE)
SimVar(ALT_DOT)
SimVar(VS_VALUE)
SimVar(VS_DASHES)
SimVar(FPA_MODE)
SimVar(BARO_VALUE)
SimVar(BARO_MODE)
SimVar(ND_MODE)
SimVar(ND_RANGE)

local function num(address)
    return tonumber(SimRead(address)) or 0
end

local function on(address)
    return num(address) == 1
end

local function round(v)
    return math.floor(v + 0.5)
end

local function healthy()
    return on(HEALTHY)
end

-- " *" after a value whose managed dot is on
local function dot(address)
    if on(address) then return " *" end
    return ""
end

function SPD()
    if not healthy() then return "" end
    if on(SPD_DASHES) then return "---" .. dot(SPD_DOT) end
    local v = num(SPD_VALUE)
    if on(MACH_MODE) then
        return string.format(".%02d", round(v * 100)) .. dot(SPD_DOT)
    end
    return string.format("%03d", round(v)) .. dot(SPD_DOT)
end

function HDG()
    if not healthy() then return "" end
    if on(HDG_DASHES) then return "---" .. dot(HDG_DOT) end
    return string.format("%03d", round(num(HDG_VALUE))) .. dot(HDG_DOT)
end

function ALT()
    if not healthy() then return "" end
    return string.format("%05d", round(num(ALT_VALUE))) .. dot(ALT_DOT)
end

function VS()
    if not healthy() then return "" end
    local fpa = on(FPA_MODE)
    if on(VS_DASHES) then
        if fpa then return "--.-" end
        return "-----"
    end
    local v = num(VS_VALUE)
    if fpa then return string.format("%+.1f", v) end
    return string.format("%+05d", round(v))
end

function BARO()
    if not healthy() then return "" end
    local mode = num(BARO_MODE)
    if mode == 0 then return "STD" end
    if mode == 1 then return string.format("%d", round(num(BARO_VALUE))) end
    if mode == 2 then return string.format("%.2f", num(BARO_VALUE)) end
    return ""
end

-- read the L-Var, add step, keep it in first..last, write it; nothing when the FCU is not healthy
local function step_lvar(address, step, first, last)
    if not healthy() then return end
    step = tonumber(step)
    if step == nil then return end
    local v = round(num(address)) + step
    if v < first then v = first end
    if v > last then v = last end
    SimWrite(address, v)
end

function NDMODE(step)
    step_lvar(ND_MODE, step, 0, 4)
end

function NDRANGE(step)
    step_lvar(ND_RANGE, step, 0, 5)
end

-- EFIS page (P4-2): ADF/VOR switches and the master warning / caution press
local NAVAID_1   = "L:A32NX_FCU_EFIS_L_NAVAID_1_MODE"         -- 0 OFF, 1 ADF, 2 VOR
local NAVAID_2   = "L:A32NX_FCU_EFIS_L_NAVAID_2_MODE"         -- 0 OFF, 1 ADF, 2 VOR
local WARN_PUSH  = "L:PUSH_AUTOPILOT_MASTERAWARN_L"           -- Captain MASTER WARN button, 1 while pressed
local CAUT_PUSH  = "L:PUSH_AUTOPILOT_MASTERCAUT_L"            -- Captain MASTER CAUT button, 1 while pressed
SimVar(NAVAID_1)
SimVar(NAVAID_2)
SimVar(WARN_PUSH)
SimVar(CAUT_PUSH)

-- switch position (0 = left, 1 = middle, 2 = right) of a value, and the value at a position:
-- ADF (value 1) left, OFF (0) middle, VOR (2) right; an unknown value counts as OFF.
-- Compared with ==, not used as table keys, so a value read as 1.0 works the same as 1.
local function navaid_pos(value)
    if value == 1 then return 0 end
    if value == 2 then return 2 end
    return 1
end

local function navaid_value(pos)
    if pos == 0 then return 1 end
    if pos == 2 then return 2 end
    return 0
end

-- read the switch, move it step positions (1 = toward VOR, -1 = toward ADF), keep it on the switch, write it;
-- nothing when the FCU is not healthy
local function step_navaid(address, step)
    if not healthy() then return end
    step = tonumber(step)
    if step == nil then return end
    local p = navaid_pos(round(num(address))) + step
    if p < 0 then p = 0 end
    if p > 2 then p = 2 end
    SimWrite(address, navaid_value(p))
end

function NAV1(step)
    step_navaid(NAVAID_1, step)
end

function NAV2(step)
    step_navaid(NAVAID_2, step)
end

-- press and release a glareshield push button: 1, 200 ms, 0
local function press_button(address)
    SimWrite(address, 1)
    Sleep(200)
    SimWrite(address, 0)
end

function MWARN()
    press_button(WARN_PUSH)
end

function MCAUT()
    press_button(CAUT_PUSH)
end

-- OVHD systems page (P4-3): fuel MODE SEL press, the cockpit's own code (A320_NEO_INTERIOR.xml,
-- PUSH_OVHD_FUEL_MODESEL LEFT_SINGLE_CODE); only when an A32NX fuel L-Var reads more than 0
local FUEL_TOTAL = "L:A32NX_TOTAL_FUEL_QUANTITY"
SimVar(FUEL_TOTAL)

function FUELMODE()
    if num(FUEL_TOTAL) <= 0 then return end
    SimCalculator("(L:A32NX_OVHD_FUEL_MODESEL_MANUAL) ! s0 (>L:A32NX_OVHD_FUEL_MODESEL_MANUAL) " ..
        "1 l0 + sp0 l0 4 (>K:2:FUELSYSTEM_JUNCTION_SET) l0 5 (>K:2:FUELSYSTEM_JUNCTION_SET)")
end

-- RADIO and XPDR pages (P4-4): the Captain's RMP (RMP 1) windows and the ATC/TCAS panel selectors.
-- docs/phase4-a32nx-radios.md. RMPACT() and RMPSTBY() return the frequency RMP 1 shows for the VHF radio
-- it has selected (VhfRadioPanel.tsx: VHF 1 reads the sim's COM 1 frequencies, VHF 2 and VHF 3 the sim's
-- active frequency and RMP 1's own standby L-Var), "" when RMP 1 is off or unpowered (BaseRadioPanels.tsx:
-- DC ESS bus and the ON/OFF switch) or in a NAV mode; "DATA" for VHF 3 when its active frequency is 0.
-- XPDRMODE, TCASMODE and TCASTRAF move the ATC panel's selectors one position (A32NX_Interior_ATC.xml
-- position values) and stop at the ends; the keys show the L-Var they read.
local RMP_MODE    = "L:A32NX_RMP_L_SELECTED_MODE"             -- 1 VHF1, 2 VHF2, 3 VHF3, 6-10 NAV modes
local RMP_SWITCH  = "L:A32NX_RMP_L_TOGGLE_SWITCH"             -- RMP 1 ON/OFF switch, 1 = ON
local RMP_POWER   = "L:A32NX_ELEC_DC_ESS_BUS_IS_POWERED"      -- RMP 1's bus
local VHF1_ACTIVE = "(A:COM ACTIVE FREQUENCY:1, Hz)"
local VHF2_ACTIVE = "(A:COM ACTIVE FREQUENCY:2, Hz)"
local VHF3_ACTIVE = "(A:COM ACTIVE FREQUENCY:3, Hz)"
local VHF1_STBY   = "(A:COM STANDBY FREQUENCY:1, Hz)"
local VHF2_STBY   = "L:A32NX_RMP_L_VHF2_STANDBY_FREQUENCY"    -- Hz
local VHF3_STBY   = "L:A32NX_RMP_L_VHF3_STANDBY_FREQUENCY"    -- Hz
local XPDR_MODE   = "L:A32NX_TRANSPONDER_MODE"                -- 0 STBY, 1 AUTO, 2 ON
local TCAS_MODE   = "L:A32NX_SWITCH_TCAS_Position"            -- 0 STBY, 1 TA, 2 TA/RA
local TCAS_TRAF   = "L:A32NX_SWITCH_TCAS_Traffic_Position"    -- 0 THRT, 1 ALL, 2 ABV, 3 BLW
SimVar(RMP_MODE)
SimVar(RMP_SWITCH)
SimVar(RMP_POWER)
SimVar(VHF1_ACTIVE)
SimVar(VHF2_ACTIVE)
SimVar(VHF3_ACTIVE)
SimVar(VHF1_STBY)
SimVar(VHF2_STBY)
SimVar(VHF3_STBY)
SimVar(XPDR_MODE)
SimVar(TCAS_MODE)
SimVar(TCAS_TRAF)

-- the VHF radio (1 to 3) RMP 1 shows, or nil when it is off, unpowered or in a NAV mode
local function rmp_vhf()
    if not on(RMP_SWITCH) or not on(RMP_POWER) then return nil end
    local m = round(num(RMP_MODE))
    if m == 1 or m == 2 or m == 3 then return m end
    return nil
end

-- Hz as "118.700" (MHz with three decimals), from whole kHz so no rounding shows
local function mhz_text(hz)
    local khz = round(hz / 1000)
    return string.format("%d.%03d", math.floor(khz / 1000), khz % 1000)
end

function RMPACT()
    local v = rmp_vhf()
    if v == nil then return "" end
    local hz = num(VHF1_ACTIVE)
    if v == 2 then hz = num(VHF2_ACTIVE) end
    if v == 3 then hz = num(VHF3_ACTIVE) end
    if hz <= 0 then
        if v == 3 then return "DATA" end
        return ""
    end
    return mhz_text(hz)
end

function RMPSTBY()
    local v = rmp_vhf()
    if v == nil then return "" end
    local hz = num(VHF1_STBY)
    if v == 2 then hz = num(VHF2_STBY) end
    if v == 3 then hz = num(VHF3_STBY) end
    if hz <= 0 then return "" end
    return mhz_text(hz)
end

-- read a selector L-Var, add step, keep it in first..last, write it (no FCU check: the ATC/TCAS panel
-- is not part of the FCU; in another aircraft the L-Var is not read, so nothing moves)
local function step_selector(address, step, first, last)
    step = tonumber(step)
    if step == nil then return end
    local v = round(num(address)) + step
    if v < first then v = first end
    if v > last then v = last end
    SimWrite(address, v)
end

function XPDRMODE(step)
    step_selector(XPDR_MODE, step, 0, 2)
end

function TCASMODE(step)
    step_selector(TCAS_MODE, step, 0, 2)
end

function TCASTRAF(step)
    step_selector(TCAS_TRAF, step, 0, 3)
end

-- PED page (P4-6): pedestal and ECAM readouts and the ENG MODE selector. docs/phase4-a32nx-pedestal.md.
-- SPDBRK shows the speed brake lever (A32NX_SPOILERS_HANDLE_POSITION 0..1, A32NX_SPOILERS_ARMED);
-- GEARIND the LDG GEAR panel as LGCIU 1 drives it (A32NX_Interior_Misc.xml, FBW_Airbus_LANDING_GEAR_Light_Template:
-- downlocked = green, unlocked = red UNLK, DC 2 bus); ABRK the armed autobrake mode and DECEL; RUDTRIM the rudder
-- trim display (L:A32NX_HYD_RUDDER_TRIM_FEEDBACK_ANGLE, degrees, negative = left; blank without DC 2, as the
-- RTPI/instrument.tsx display); BRKPSI the triple brake
-- indicator's left and right needles in 1000 psi (A320_NEO_INTERIOR.xml Airbus_BRK: value / 1000, DC ESS bus).
-- ENGMODE moves the ENG MODE selector one position and runs the selector's own code (Airbus.xml,
-- A32NX_ENGINE_MODE_SELECTOR_TEMPLATE), only when an A32NX fuel L-Var reads more than 0.
local SPLR_POS    = "L:A32NX_SPOILERS_HANDLE_POSITION"        -- 0 retracted .. 1 full
local SPLR_ARMED  = "L:A32NX_SPOILERS_ARMED"                  -- 1 = armed
local GEAR_POWER  = "L:A32NX_ELEC_DC_2_BUS_IS_POWERED"        -- LDG GEAR panel's and rudder trim display's bus
local GEAR_DN_N   = "L:A32NX_LGCIU_1_NOSE_GEAR_DOWNLOCKED"
local GEAR_DN_L   = "L:A32NX_LGCIU_1_LEFT_GEAR_DOWNLOCKED"
local GEAR_DN_R   = "L:A32NX_LGCIU_1_RIGHT_GEAR_DOWNLOCKED"
local GEAR_UNLK_N = "L:A32NX_LGCIU_1_NOSE_GEAR_UNLOCKED"
local GEAR_UNLK_L = "L:A32NX_LGCIU_1_LEFT_GEAR_UNLOCKED"
local GEAR_UNLK_R = "L:A32NX_LGCIU_1_RIGHT_GEAR_UNLOCKED"
local ABRK_MODE   = "L:A32NX_AUTOBRAKES_ARMED_MODE"           -- 0 off, 1 LO, 2 MED, 3 MAX
local ABRK_DECEL  = "L:A32NX_AUTOBRAKES_DECEL_LIGHT"          -- 1 = DECEL light on
local ENG_MODE    = "L:XMLVAR_ENG_MODE_SEL"                   -- 0 CRANK, 1 NORM, 2 IGN/START
local RUD_TRIM    = "L:A32NX_HYD_RUDDER_TRIM_FEEDBACK_ANGLE"  -- degrees, negative = left
local BRK_L       = "L:A32NX_HYD_BRAKE_ALTN_LEFT_PRESS"       -- psi
local BRK_R       = "L:A32NX_HYD_BRAKE_ALTN_RIGHT_PRESS"      -- psi
SimVar(SPLR_POS)
SimVar(SPLR_ARMED)
SimVar(GEAR_POWER)
SimVar(GEAR_DN_N)
SimVar(GEAR_DN_L)
SimVar(GEAR_DN_R)
SimVar(GEAR_UNLK_N)
SimVar(GEAR_UNLK_L)
SimVar(GEAR_UNLK_R)
SimVar(ABRK_MODE)
SimVar(ABRK_DECEL)
SimVar(ENG_MODE)
SimVar(RUD_TRIM)
SimVar(BRK_L)
SimVar(BRK_R)

function SPDBRK()
    if on(SPLR_ARMED) then return "ARM" end
    local p = num(SPLR_POS)
    if p < 0.01 then return "RET" end
    if p > 0.99 then return "FULL" end
    return string.format("%d%%", round(p * 100))
end

function GEARIND()
    if not on(GEAR_POWER) then return "" end
    if on(GEAR_UNLK_N) or on(GEAR_UNLK_L) or on(GEAR_UNLK_R) then return "UNLK" end
    local n = 0
    if on(GEAR_DN_N) then n = n + 1 end
    if on(GEAR_DN_L) then n = n + 1 end
    if on(GEAR_DN_R) then n = n + 1 end
    if n == 0 then return "UP" end
    return string.format("%d GRN", n)
end

function ABRK()
    if on(ABRK_DECEL) then return "DECEL" end
    local m = round(num(ABRK_MODE))
    if m == 1 then return "LO" end
    if m == 2 then return "MED" end
    if m == 3 then return "MAX" end
    return "OFF"
end

function RUDTRIM()
    if not on(GEAR_POWER) then return "" end
    local d = num(RUD_TRIM)
    if math.abs(d) < 0.05 then return "0.0" end
    if d < 0 then return string.format("L %.1f", -d) end
    return string.format("R %.1f", d)
end

function BRKPSI()
    if not on(RMP_POWER) then return "" end
    return string.format("%.1f %.1f", num(BRK_L) / 1000, num(BRK_R) / 1000)
end

-- the selector's own code for each position (compared with ==, not used as a table key)
local function eng_mode_code(v)
    if v == 2 then
        return "2 (>K:TURBINE_IGNITION_SWITCH_SET1) 2 (>K:TURBINE_IGNITION_SWITCH_SET2) " ..
            "(>H:A320_Neo_EICAS_2_Ignition_Start)"
    end
    if v == 1 then return "1 (>K:TURBINE_IGNITION_SWITCH_SET1) 1 (>K:TURBINE_IGNITION_SWITCH_SET2)" end
    return "0 (>K:TURBINE_IGNITION_SWITCH_SET)"
end

function ENGMODE(step)
    if num(FUEL_TOTAL) <= 0 then return end
    step = tonumber(step)
    if step == nil then return end
    local v = round(num(ENG_MODE)) + step
    if v < 0 then v = 0 end
    if v > 2 then v = 2 end
    SimWrite(ENG_MODE, v)
    SimCalculator(eng_mode_code(v))
end
