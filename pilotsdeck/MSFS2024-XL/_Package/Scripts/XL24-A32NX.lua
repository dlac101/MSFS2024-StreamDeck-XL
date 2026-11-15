-- XL24-A32NX.lua: FCU readouts and ND steps for the MSFS2024 A32NX profile (PilotsDeck standard script).
-- Page and keys: docs/phase4-a32nx.md. Not yet sim-tested.
-- EFIS page keys (ADF/VOR steps, MASTER WARN/CAUT press): docs/phase4-a32nx-efis.md.
-- OVHD systems page key (fuel MODE SEL press): docs/phase4-a32nx-overhead.md.
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
