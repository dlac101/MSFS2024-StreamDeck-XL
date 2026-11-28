-- XL24-B737.lua: hold to repeat for the Boeing 737 MAX 8 profile (PilotsDeck standard script).
-- Pages and keys: docs/b737-max8.md, "Hold to repeat". Not yet sim-tested.
--
-- Each step key is a Simple Button with Hold Switch on and command type Lua Function: key down runs
-- HOLD(n) ("lua:XL24-B737:HOLD(1)"), key up runs RELEASE(n) ("lua:XL24-B737:RELEASE(1)") (PilotsDeck
-- README 2.1.2 "Hold Switch": the normal command is sent on key down, the alternate command on key up).
-- HOLD sends one step at once, so a short press gives one step.
-- While the key stays down, HOLD sends more steps, faster the longer it is held, and stops when RELEASE
-- runs, at the key's step cap or after MAX_HOLD_MS, whichever comes first. It never runs on: every loop
-- turn checks the release count, and the step cap and MAX_HOLD_MS end every loop even if a key up is lost.
-- PilotsDeck runs each Lua command on its own task, so HOLD may sleep (as XL24-SIMRATE does) while
-- RELEASE runs. The keys show fixed images: the readouts beside them show the sim's values.
--
-- Two kinds of codes (the KEYS table):
-- "event": the step sends a K-event with SimCommand, as XL24-CJ4.lua (BARO and trim).
-- "bvar": the 737's MCP knobs are input events (B-vars) that hold the selected value, so the step writes
--   a value: at key down the script reads the base value (SimRead of the address it registered with
--   SimVar, README 3.5.1), then every step adds the key's step to the value it wrote last, keeps it in
--   the key's limits and writes it with SimCommand("B:<name>:<value>") (README 3.5.1 SimCommand, the
--   B-var form of README 2.1.1). Whether SimRead reads a B-var and whether the value lands as written is
--   a hand test. V/S reads its base from the SimVar the V/S readout shows, because the B-var keeps its
--   old value when the V/S mode ends (docs/b737-max8.md, "Hold to repeat").
-- The script writes only the B-vars of its key table and sends only its events; it does not check
-- which aircraft is loaded.

local TICK_MS     = 50      -- loop step; PilotsDeck's Sleep(ms) blocks only this task
local MAX_HOLD_MS = 20000   -- no hold repeats longer than this

-- speed profiles: wait `delay` ms, then send `n` steps every `every` ms until `upto` ms after the delay;
-- the last stage (upto = nil) runs to the cap
local PROFILES = {
    fast  = { delay = 400, stages = { { upto = 1500, every = 100, n = 1 }, { upto = 3000, every = 50, n = 1 },
                                      { upto = nil,  every = 50,  n = 3 } } },
    alt   = { delay = 400, stages = { { upto = 1500, every = 100, n = 1 }, { upto = nil,  every = 50, n = 1 } } },
    slow  = { delay = 400, stages = { { upto = nil,  every = 150, n = 1 } } },
    baro  = { delay = 400, stages = { { upto = 2000, every = 100, n = 1 }, { upto = nil,  every = 50, n = 1 } } },
    trim  = { delay = 250, stages = { { upto = nil,  every = 50,  n = 1 } } },
}

-- the base value each "bvar" code reads at key down
local SPD_SEL = "B:fcc_speed_sel"
local HDG_SEL = "B:fcc_heading_sel"
local ALT_SEL = "B:fcc_altitude_sel"
local CRS_SEL = "B:fcc_course_1"
local VS_TGT  = "(A:AUTOPILOT VERTICAL HOLD VAR, Feet/minute)"
SimVar(SPD_SEL)
SimVar(HDG_SEL)
SimVar(ALT_SEL)
SimVar(CRS_SEL)
SimVar(VS_TGT)

-- key code = { kind, profile, step cap per hold (the first step counts), ... }
--   "event": { "event", profile, cap, event }
--   "bvar":  { "bvar", profile, cap, base read, B-var written, step, low, high, limit ("clamp", "wrap" or nil) }
-- codes 13 and 14 are not used (the MINS keys are single-step keys)
local KEYS = {
    [1]  = { "bvar",  "fast", 200, SPD_SEL, "B:fcc_speed_sel",          1,    100, 399,   "clamp" }, -- main 2,1 SPD+
    [2]  = { "bvar",  "fast", 200, SPD_SEL, "B:fcc_speed_sel",          -1,   100, 399,   "clamp" }, -- main 4,1 SPD-
    [3]  = { "bvar",  "fast", 360, HDG_SEL, "B:fcc_heading_sel",        1,    0,   359,   "wrap" },  -- main 2,2 HDG+
    [4]  = { "bvar",  "fast", 360, HDG_SEL, "B:fcc_heading_sel",        -1,   0,   359,   "wrap" },  -- main 4,2 HDG-
    [5]  = { "bvar",  "alt",  400, ALT_SEL, "B:fcc_altitude_sel",       100,  0,   50000, "clamp" }, -- main 2,3 ALT+
    [6]  = { "bvar",  "alt",  400, ALT_SEL, "B:fcc_altitude_sel",       -100, 0,   50000, "clamp" }, -- main 4,3 ALT-
    [7]  = { "bvar",  "fast", 360, CRS_SEL, "B:fcc_course_1",           1,    0,   359,   "wrap" },  -- mcp 2,1 CRS+
    [8]  = { "bvar",  "fast", 360, CRS_SEL, "B:fcc_course_1",           -1,   0,   359,   "wrap" },  -- mcp 4,1 CRS-
    [9]  = { "bvar",  "slow", 40,  VS_TGT,  "B:fcc_vertical_speed_sel", 100,  nil, nil,   nil },     -- mcp 2,5 V/S+
    [10] = { "bvar",  "slow", 40,  VS_TGT,  "B:fcc_vertical_speed_sel", -100, nil, nil,   nil },     -- mcp 4,5 V/S-
    [11] = { "event", "baro", 200, "K:KOHLSMAN_INC" },      -- mcp 2,7 BARO+
    [12] = { "event", "baro", 200, "K:KOHLSMAN_DEC" },      -- mcp 4,7 BARO-
    [15] = { "event", "trim", 160, "K:ELEV_TRIM_UP" },      -- trim 2,2 TRIM UP
    [16] = { "event", "trim", 160, "K:ELEV_TRIM_DN" },      -- trim 4,2 TRIM DN
    [17] = { "event", "trim", 160, "K:AILERON_TRIM_LEFT" }, -- trim 2,6 AIL L
    [18] = { "event", "trim", 160, "K:AILERON_TRIM_RIGHT" }, -- trim 2,8 AIL R
    [19] = { "event", "trim", 160, "K:RUDDER_TRIM_LEFT" },  -- trim 3,6 RUD L
    [20] = { "event", "trim", 160, "K:RUDDER_TRIM_RIGHT" }, -- trim 3,8 RUD R
}

-- per key: presses and releases seen, loop running, the value a "bvar" code wrote last (filled now, so no
-- table grows while two tasks use it); KEYS holds the codes 1 to 12 and 15 to 20
local downs, ups, busy, value = {}, {}, {}, {}
for code = 1, 20 do
    downs[code] = 0
    ups[code] = 0
    busy[code] = false
    value[code] = 0
end

local function held(code)
    return downs[code] > ups[code]
end

-- a "bvar" code's next value: the step added, kept in the key's limits
local function next_value(key, v)
    v = v + key[6]
    if key[9] == "clamp" then
        if v < key[7] then v = key[7] end
        if v > key[8] then v = key[8] end
    elseif key[9] == "wrap" then
        local span = key[8] - key[7] + 1
        v = (v - key[7]) % span + key[7]
    end
    return v
end

-- one step of a code: its event, or the next value written to its B-var
local function step(code)
    local key = KEYS[code]
    if key[1] == "event" then
        SimCommand(key[4])
    else
        value[code] = next_value(key, value[code])
        SimCommand(key[5] .. ":" .. string.format("%d", value[code]))
    end
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
                step(code)
                sent = sent + 1
            end
            since = 0
        end
        Sleep(TICK_MS)
        t = t + TICK_MS
        since = since + TICK_MS
    end
    if held(code) then
        Log("XL24-B737: hold " .. tostring(code) .. " stopped at its cap (" .. tostring(sent) .. " steps)")
    end
end

-- key down: one step now, then the repeat loop while the key stays down
function HOLD(code)
    code = tonumber(code)
    if code == nil or KEYS[code] == nil then return end
    downs[code] = downs[code] + 1
    if downs[code] - ups[code] > 1 then ups[code] = downs[code] - 1 end   -- a lost key up: resync
    if busy[code] then                         -- a loop of this key still runs: it serves this hold
        step(code)
        return
    end
    if KEYS[code][1] == "bvar" then            -- a new hold starts from the sim's value
        local base = tonumber(SimRead(KEYS[code][4]))
        if base == nil then                    -- no value read: write nothing rather than start from 0
            Log("XL24-B737: no value for " .. KEYS[code][4] .. ", nothing written")
            return
        end
        value[code] = math.floor(base + 0.5)
    end
    step(code)
    busy[code] = true
    local ok, err = pcall(run, code)
    busy[code] = false
    if not ok then Log("XL24-B737: error, stopped: " .. tostring(err)) end
end

-- key up: the loop sees it within one TICK_MS
function RELEASE(code)
    code = tonumber(code)
    if code == nil or KEYS[code] == nil then return end
    ups[code] = ups[code] + 1
end
