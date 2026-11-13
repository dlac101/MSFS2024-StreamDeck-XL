-- XL24-COMPAD.lua: COM1 frequency pad for the MSFS2024-XL profiles (PilotsDeck standard script).
-- Page and keys: docs/phase2-com1-pad.md. Not yet sim-tested.
--
-- The pad keys call DIGIT(n), BACK, CLEAR, ENTER and ENTER_SWAP (command type Lua Function,
-- "lua:XL24-COMPAD:DIGIT(7)"). The typed digits are shown by a Display Value key that reads the
-- internal variable X:XL24_COMPAD_ENTRY. ENTER sets COM1 standby with K:COM_STBY_RADIO_SET_HZ
-- (MSFS SDK: "[0]: Frequency value (Hz)"); ENTER_SWAP also sends K:COM_STBY_RADIO_SWAP.
-- PilotsDeck loads this script when a key that uses it appears and unloads it when none is left,
-- so leaving the page clears the entry (this file's top level runs again on the next load).

local ENTRY   = "X:XL24_COMPAD_ENTRY"
local SPACING = "(A:COM SPACING MODE:1, Enum)"   -- 0 = 25 kHz, 1 = 8.33 kHz (MSFS SDK)
SimVar(SPACING)

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
    digits = digits .. string.sub(tostring(d), 1, 1)
    show()
end

function BACK()
    digits = string.sub(digits, 1, #digits - 1)
    show()
end

function CLEAR()
    digits = ""
    show()
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

local function send(swap)
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
    CLEAR()
end

function ENTER()
    send(false)
end

function ENTER_SWAP()
    send(true)
end

show()
