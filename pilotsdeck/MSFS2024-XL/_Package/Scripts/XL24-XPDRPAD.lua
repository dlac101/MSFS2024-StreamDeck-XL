-- XL24-XPDRPAD.lua: transponder code pad for the MSFS2024-XL profiles (PilotsDeck standard script).
-- Page and keys: docs/phase3-transponder.md. Not yet sim-tested.
--
-- The pad keys call DIGIT(n), BACK, CLEAR and ENTER (command type Lua Function,
-- "lua:XL24-XPDRPAD:DIGIT(7)"). The typed digits are shown by a Display Value key that reads the
-- internal variable X:XL24_XPDRPAD_ENTRY. ENTER sets the squawk code with K:XPNDR_SET
-- (MSFS SDK: "[0]: Frequency value (Bco16 encoded)"): the four octal digits read as one hex number,
-- e.g. 7000 = 0x7000 = 28672, sent as a whole number.
-- PilotsDeck loads this script when a key that uses it appears and unloads it when none is left,
-- so leaving the page clears the entry (this file's top level runs again on the next load).

local ENTRY = "X:XL24_XPDRPAD_ENTRY"

local digits = ""   -- the typed digits, at most 4, each 0 to 7

-- write the entry as "12__"
local function show()
    SimWrite(ENTRY, digits .. string.rep("_", 4 - #digits))
end

function DIGIT(d)
    d = tonumber(d)
    if d == nil or d < 0 or d > 7 or d ~= math.floor(d) then return end
    if #digits >= 4 then return end
    digits = digits .. string.sub(tostring(math.floor(d)), 1, 1)
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

function ENTER()
    if #digits ~= 4 then
        Log("XL24-XPDRPAD: need 4 digits, have '" .. digits .. "'")
        return
    end
    local bco16 = tonumber(digits, 16)          -- "7000" -> 28672 (0x7000)
    if bco16 == nil then
        Log("XL24-XPDRPAD: cannot read '" .. digits .. "' as a code")
        return
    end
    SimCommand("K:XPNDR_SET:" .. string.format("%d", bco16))
    Log("XL24-XPDRPAD: squawk set to " .. digits .. " (K:XPNDR_SET " .. string.format("%d", bco16) .. ")")
    CLEAR()
end

show()
