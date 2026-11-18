-- XL24-SF50.lua: hold to repeat for the VisionJet SF50 profile (PilotsDeck standard script, lane A).
-- Pages and keys: docs/visionjet-sf50.md, "Hold to repeat". Not yet sim-tested.
--
-- Each step key is a Simple Button with Hold Switch on and command type Lua Function: key down runs
-- HOLD(n) ("lua:XL24-SF50:HOLD(1)"), key up runs RELEASE(n) ("lua:XL24-SF50:RELEASE(1)") (PilotsDeck
-- README 2.1.2 "Hold Switch": the normal command is sent on key down, the alternate command on key up).
-- HOLD sends one step at once, so a short press does what the key did before (one event).
-- While the key stays down, HOLD sends more steps, faster the longer it is held, and stops when RELEASE
-- runs, at the key's step cap or after MAX_HOLD_MS, whichever comes first. It never runs on: every loop
-- turn checks the release count, and the step cap and MAX_HOLD_MS end every loop even if a key up is lost.
-- PilotsDeck runs each Lua command on its own task, so HOLD may sleep (as XL24-SIMRATE does) while
-- RELEASE runs. The keys show fixed images: the readouts beside them show the sim's values.
-- The script sends events only (SimCommand): no variable is written, and it acts in any aircraft.

local TICK_MS     = 50      -- loop step; PilotsDeck's Sleep(ms) blocks only this task
local MAX_HOLD_MS = 20000   -- no hold repeats longer than this

-- speed profiles: wait `delay` ms, then send `n` events every `every` ms until `upto` ms after the delay;
-- the last stage (upto = nil) runs to the cap
local PROFILES = {
    fast  = { delay = 400, stages = { { upto = 1500, every = 100, n = 1 }, { upto = 3000, every = 50, n = 1 },
                                      { upto = nil,  every = 50,  n = 3 } } },
    alt   = { delay = 400, stages = { { upto = 1500, every = 100, n = 1 }, { upto = nil,  every = 50, n = 1 } } },
    slow  = { delay = 400, stages = { { upto = nil,  every = 150, n = 1 } } },
    baro  = { delay = 400, stages = { { upto = 2000, every = 100, n = 1 }, { upto = nil,  every = 50, n = 1 } } },
    trim  = { delay = 250, stages = { { upto = nil,  every = 50,  n = 1 } } },
}

-- key code = { event, profile, step cap per hold (the first step counts) }
local KEYS = {
    [1]  = { "K:HEADING_BUG_INC",       "fast", 360 },  -- autopilot 2,2 HDG+
    [2]  = { "K:HEADING_BUG_DEC",       "fast", 360 },  -- autopilot 4,2 HDG-
    [3]  = { "H:AS3000_PFD_1_CRS_INC",  "fast", 360 },  -- autopilot 2,3 CRS+
    [4]  = { "H:AS3000_PFD_1_CRS_DEC",  "fast", 360 },  -- autopilot 4,3 CRS-
    [5]  = { "K:AP_ALT_VAR_INC",        "alt",  400 },  -- autopilot 2,4 ALT+
    [6]  = { "K:AP_ALT_VAR_DEC",        "alt",  400 },  -- autopilot 4,4 ALT-
    [7]  = { "K:AP_VS_VAR_INC",         "slow", 40 },   -- autopilot 2,5 VS+
    [8]  = { "K:AP_VS_VAR_DEC",         "slow", 40 },   -- autopilot 4,5 VS-
    [9]  = { "K:AP_SPD_VAR_INC",        "fast", 200 },  -- autopilot 2,6 SPD+
    [10] = { "K:AP_SPD_VAR_DEC",        "fast", 200 },  -- autopilot 4,6 SPD-
    [11] = { "K:KOHLSMAN_INC",          "baro", 200 },  -- radios 2,8 BARO+
    [12] = { "K:KOHLSMAN_DEC",          "baro", 200 },  -- radios 3,8 BARO-
    [13] = { "K:NAV1_RADIO_WHOLE_INC",  "slow", 30 },   -- radios 2,2 MHZ+ (NAV1)
    [14] = { "K:NAV1_RADIO_FRACT_INC",  "fast", 200 },  -- radios 2,3 KHZ+ (NAV1)
    [15] = { "K:NAV2_RADIO_WHOLE_INC",  "slow", 30 },   -- radios 2,4 MHZ+ (NAV2)
    [16] = { "K:NAV2_RADIO_FRACT_INC",  "fast", 200 },  -- radios 2,5 KHZ+ (NAV2)
    [17] = { "K:COM2_RADIO_WHOLE_INC",  "slow", 30 },   -- radios 2,6 MHZ+ (COM2)
    [18] = { "K:COM2_RADIO_FRACT_INC",  "fast", 200 },  -- radios 2,7 KHZ+ (COM2)
    [19] = { "K:NAV1_RADIO_WHOLE_DEC",  "slow", 30 },   -- radios 3,2 MHZ- (NAV1)
    [20] = { "K:NAV1_RADIO_FRACT_DEC",  "fast", 200 },  -- radios 3,3 KHZ- (NAV1)
    [21] = { "K:NAV2_RADIO_WHOLE_DEC",  "slow", 30 },   -- radios 3,4 MHZ- (NAV2)
    [22] = { "K:NAV2_RADIO_FRACT_DEC",  "fast", 200 },  -- radios 3,5 KHZ- (NAV2)
    [23] = { "K:COM2_RADIO_WHOLE_DEC",  "slow", 30 },   -- radios 3,6 MHZ- (COM2)
    [24] = { "K:COM2_RADIO_FRACT_DEC",  "fast", 200 },  -- radios 3,7 KHZ- (COM2)
    [25] = { "K:ELEV_TRIM_UP",          "trim", 160 },  -- trim 2,2 TRIM UP
    [26] = { "K:ELEV_TRIM_DN",          "trim", 160 },  -- trim 4,2 TRIM DN
    [27] = { "K:RUDDER_TRIM_LEFT",      "trim", 160 },  -- trim 3,6 RUD L
    [28] = { "K:RUDDER_TRIM_RIGHT",     "trim", 160 },  -- trim 3,8 RUD R
}

-- per key: presses and releases seen, loop running (filled now, so no table grows while two tasks use it);
-- KEYS holds the codes 1 to 28
local downs, ups, busy = {}, {}, {}
for code = 1, 28 do
    downs[code] = 0
    ups[code] = 0
    busy[code] = false
end

local function held(code)
    return downs[code] > ups[code]
end

-- the stage for time t: the first whose `upto` is nil or later than t, else the last
local function stage_of(profile, t)
    local stages = profile.stages
    local i = 1
    while stages[i + 1] ~= nil and stages[i].upto ~= nil and t >= stages[i].upto do
        i = i + 1
    end
    return stages[i]
end

-- the repeat loop of one hold; both loops count `t` up by TICK_MS on every turn, so the first ends by
-- profile.delay and the second by MAX_HOLD_MS (or the step cap) whatever RELEASE does
local function run(code)
    local key = KEYS[code]
    local profile = PROFILES[key[2]]
    local sent, t, since = 1, 0, 0
    while t < profile.delay do                 -- the auto-repeat delay: a short press ends here
        Sleep(TICK_MS)
        t = t + TICK_MS
        if not held(code) then return end
    end
    while held(code) and sent < key[3] and t < MAX_HOLD_MS do
        local s = stage_of(profile, t - profile.delay)
        if since >= s.every or since == 0 then
            for i = 1, s.n do
                if sent >= key[3] then break end
                SimCommand(key[1])
                sent = sent + 1
            end
            since = 0
        end
        Sleep(TICK_MS)
        t = t + TICK_MS
        since = since + TICK_MS
    end
    if held(code) then
        Log("XL24-SF50: hold " .. tostring(code) .. " stopped at its cap (" .. tostring(sent) .. " steps)")
    end
end

-- key down: one step now, then the repeat loop while the key stays down
function HOLD(code)
    code = tonumber(code)
    if code == nil or KEYS[code] == nil then return end
    downs[code] = downs[code] + 1
    if downs[code] - ups[code] > 1 then ups[code] = downs[code] - 1 end   -- a lost key up: resync
    SimCommand(KEYS[code][1])
    if busy[code] then return end              -- a loop of this key still runs: it serves this hold
    busy[code] = true
    local ok, err = pcall(run, code)
    busy[code] = false
    if not ok then Log("XL24-SF50: error, stopped: " .. tostring(err)) end
end

-- key up: the loop sees it within one TICK_MS
function RELEASE(code)
    code = tonumber(code)
    if code == nil or KEYS[code] == nil then return end
    ups[code] = ups[code] + 1
end
