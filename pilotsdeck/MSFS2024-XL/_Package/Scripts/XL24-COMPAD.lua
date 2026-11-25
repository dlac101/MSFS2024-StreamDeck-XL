-- XL24-COMPAD.lua: COM1 frequency pad for the MSFS2024-XL profiles (PilotsDeck standard script).
-- Page and keys: docs/phase2-com1-pad.md. Not yet sim-tested.
--
-- The pad keys call DIGIT(n), BACK, CLEAR, ENTER and ENTER_SWAP (command type Lua Function,
-- "lua:XL24-COMPAD:DIGIT(7)"). The typed digits are shown by a Display Value key that reads the
-- internal variable X:XL24_COMPAD_ENTRY. ENTER sets COM1 standby with K:COM_STBY_RADIO_SET_HZ
-- (MSFS SDK: "[0]: Frequency value (Hz)"); ENTER_SWAP also sends K:COM_STBY_RADIO_SWAP.
-- PilotsDeck loads this script when a key that uses it appears and unloads it when none is left,
-- so leaving the page clears the entry (this file's top level runs again on the next load).
--
-- Press feedback (docs/visionjet-sf50.md, "COM pad: centered text and press feedback"): a key that took
-- effect sets its own internal variable X:XL24_COMPAD_LIT_<key> to 1 for a short time, then back to 0; a key
-- may show an image for 1. A digit, BACK and CLEAR count when they changed the entry (local to this script).
-- ENTER and ENTER_SWAP count only when the sim reads back the sent frequency (COM1 standby for ENTER, COM1
-- active for ENTER_SWAP). A refused press lights nothing. A profile whose keys don't read these variables
-- (the C172) shows nothing of it. By PilotsDeck's source each Lua command runs on its own task, so the Sleeps
-- (the end of a light, the reads after ENT) should not hold up the next press (not proven; XL24-SF50.lua
-- relies on the same).

local ENTRY   = "X:XL24_COMPAD_ENTRY"
local SPACING = "(A:COM SPACING MODE:1, Enum)"   -- 0 = 25 kHz, 1 = 8.33 kHz (MSFS SDK)
SimVar(SPACING)

local STANDBY = "(A:COM STANDBY FREQUENCY:1, MHz)"   -- as the COM1 key reads them
local ACTIVE  = "(A:COM ACTIVE FREQUENCY:1, MHz)"
SimVar(STANDBY)
SimVar(ACTIVE)

local LIT         = "X:XL24_COMPAD_LIT_"  -- plus "0" to "9", "CLR" or "ENT": "1" while lit, else "0"
local LIT_MS      = 250                   -- a digit or CLR stays lit this long
local ENT_LIT_MS  = 1000                  -- ENT stays lit this long
local READBACK_MS = 1500                  -- wait at most this long for the sim to read back the frequency
local POLL_MS     = 50                    -- PilotsDeck's own process interval
local TOLERANCE   = 1                     -- kHz; COM channels are at least 5 kHz apart

-- per key: how often it was lit or put out (only the latest light of a key ends it; filled now, so no table
-- grows while two tasks use it)
local KEYS = { "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "CLR", "ENT" }
local lights = {}
for i = 1, 12 do lights[KEYS[i]] = 0 end
local sends = 0   -- ENTER and ENTER_SWAP presses; a readback wait ends when a newer press came

local function unlight(key)
    lights[key] = lights[key] + 1
    SimWrite(LIT .. key, "0")
end

-- light a key for ms, then put it out, unless the same key was lit again or put out in the meantime ("1" is
-- written before the count moves, so a call that puts the key out in between leaves it out in the end)
local function light(key, ms)
    SimWrite(LIT .. key, "1")
    local mine = lights[key] + 1
    lights[key] = mine
    Sleep(ms)
    if lights[key] == mine then SimWrite(LIT .. key, "0") end
end

local digits = ""   -- the typed digits, at most 6 (MHz digits 1-3, kHz digits 4-6)

-- write the entry as "118.5__" (decimal point fixed after the third digit)
local function show()
    local s = digits .. string.rep("_", 6 - #digits)
    SimWrite(ENTRY, string.sub(s, 1, 3) .. "." .. string.sub(s, 4, 6))
end

-- may digit d be typed next? COM frequencies run from 118.000 to 136.990 MHz.
local function allowed(d)
    local n = #digits
    if n == 0 then return d == 1 end
    if n == 1 then return d >= 1 and d <= 3 end
    if n == 2 then
        local second = string.sub(digits, 2, 2)
        if second == "1" then return d >= 8 end
        if second == "3" then return d <= 6 end
        return true
    end
    return n < 6
end

function DIGIT(d)
    d = tonumber(d)
    if d == nil or d < 0 or d > 9 or d ~= math.floor(d) then return end
    if not allowed(d) then return end
    local key = string.sub(tostring(d), 1, 1)
    digits = digits .. key
    show()
    light(key, LIT_MS)
end

function BACK()
    local typed = #digits > 0
    digits = string.sub(digits, 1, #digits - 1)
    show()
    if typed then light("CLR", LIT_MS) end
end

function CLEAR()
    local typed = #digits > 0
    digits = ""
    show()
    if typed then light("CLR", LIT_MS) end
end

-- the frequency in Hz as a string of digits, or nil if the entry is not a COM frequency
local function frequencyHz()
    if #digits < 3 then return nil end
    local s = digits
    -- 25 kHz radios: "118.52" means 118.525 and "118.57" means 118.575
    if #s == 5 and SimRead(SPACING) == 0 then
        local last = string.sub(s, 5, 5)
        if last == "2" or last == "7" then s = s .. "5" end
    end
    s = s .. string.rep("0", 6 - #s)            -- kHz, 6 digits: "118525"
    local khz = tonumber(s)
    if khz == nil or khz < 118000 or khz > 136990 then return nil end
    return s .. "000"                           -- Hz: "118525000"
end

-- true when `address` (MHz) reads the frequency `hz` within READBACK_MS; false when it doesn't, or when a
-- newer ENTER or ENTER_SWAP press came (`mine` is no longer the latest)
local function readsBack(address, hz, mine)
    local khz = tonumber(hz) / 1000
    local waited = 0
    while sends == mine do
        local mhz = tonumber(SimRead(address))
        if mhz ~= nil and math.abs(mhz * 1000 - khz) < TOLERANCE then return true end
        if waited >= READBACK_MS then return false end
        Sleep(POLL_MS)
        waited = waited + POLL_MS
    end
    return false
end

local function send(swap)
    sends = sends + 1
    local mine = sends
    unlight("ENT")                              -- an earlier light says nothing about this press
    local hz = frequencyHz()
    if hz == nil then
        Log("XL24-COMPAD: not a COM frequency: '" .. digits .. "'")
        return
    end
    SimCommand("K:COM_STBY_RADIO_SET_HZ:" .. hz)
    if swap then
        Sleep(100)
        SimCommand("K:COM_STBY_RADIO_SWAP")
        Log("XL24-COMPAD: COM1 standby set to " .. hz .. " Hz and swapped to active")
    else
        Log("XL24-COMPAD: COM1 standby set to " .. hz .. " Hz")
    end
    digits = ""
    show()
    if readsBack(swap and ACTIVE or STANDBY, hz, mine) then
        light("ENT", ENT_LIT_MS)
    elseif sends == mine then
        Log("XL24-COMPAD: COM1 did not read back " .. hz .. " Hz")
    end
end

function ENTER()
    send(false)
end

function ENTER_SWAP()
    send(true)
end

-- nothing may stay lit from an earlier load
for i = 1, 12 do SimWrite(LIT .. KEYS[i], "0") end
show()
