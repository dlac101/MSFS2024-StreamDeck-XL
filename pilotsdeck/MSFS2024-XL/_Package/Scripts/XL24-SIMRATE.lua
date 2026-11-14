-- XL24-SIMRATE.lua: sim rate keys for the MSFS2024-XL profiles (PilotsDeck standard script).
-- Page and keys: docs/phase2-sim-rate.md. Not yet sim-tested.
--
-- The 1X key calls SET(n) (command type Lua Function, "lua:XL24-SIMRATE:SET(1)"). SET steps
-- the rate with K:SIM_RATE_INCR or K:SIM_RATE_DECR (MSFS SDK: no parameter), one step at a time,
-- until the read rate (A:SIMULATION RATE, number) equals the target. K:SIM_RATE_SET:n did nothing
-- when sent from the deck (2026-11-12). The keys light from the read rate, never from this script.
-- Never runs away: at most MAX_STEPS events per press, each one only after the previous one changed
-- the read rate; it stops (one Log line) when the rate stays, passes the target or is not read.
-- A press while a run is still going is ignored. PilotsDeck loads this script when a key that uses
-- it appears and unloads it when none is left.

local RATE      = "(A:SIMULATION RATE, number)"   -- MSFS SDK: 0.0625 to 128, powers of two
local MAX_STEPS = 8      -- 128x to 1x is 7 steps of x2; never more than this per press
local WAIT_MS   = 2000   -- longest wait for the read rate to change after one step
local POLL_MS   = 100
SimVar(RATE)

local busy = false   -- true while a SET run is going

local function rate()
    return tonumber(SimRead(RATE)) or 0
end

local function same(a, b)
    return math.abs(a - b) < b * 0.01
end

-- the new rate, or nil if it did not change within WAIT_MS
local function changed(old)
    local waited = 0
    while waited < WAIT_MS do
        Sleep(POLL_MS)
        waited = waited + POLL_MS
        local r = rate()
        if not same(r, old) then return r end
    end
    return nil
end

local function step_to(target)
    for i = 1, MAX_STEPS do
        local r = rate()
        if r <= 0 then
            Log("XL24-SIMRATE: no rate read, stopped")
            return
        end
        if same(r, target) then return end
        local up = r < target
        if up then
            SimCommand("K:SIM_RATE_INCR")
        else
            SimCommand("K:SIM_RATE_DECR")
        end
        local n = changed(r)
        if n == nil then
            Log("XL24-SIMRATE: rate stayed " .. tostring(r) .. ", stopped")
            return
        end
        if (up and n > target) or ((not up) and n < target) then
            Log("XL24-SIMRATE: passed " .. tostring(target) .. ", now " .. tostring(n) .. ", stopped")
            return
        end
    end
    Log("XL24-SIMRATE: " .. tostring(MAX_STEPS) .. " steps done, stopped")
end

function SET(target)
    target = tonumber(target)
    if target == nil or target < 0.0625 or target > 128 or busy then return end
    busy = true
    -- pcall (Lua base library, in PilotsDeck's NeoLua engine) so busy is cleared even if a run errors
    local ok, err = pcall(step_to, target)
    busy = false
    if not ok then Log("XL24-SIMRATE: error, stopped: " .. tostring(err)) end
end
