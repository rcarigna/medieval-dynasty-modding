-- SPDX-License-Identifier: MIT
-- Original, untested read-only example. Use only in a disposable single-player session.
-- Ctrl+Alt+F9 requests one scan; no property writes, spawning, save calls, or AI hooks.
local pending = false
local reject = EObjectFlags.RF_ClassDefaultObject | EObjectFlags.RF_ArchetypeObject
    | EObjectFlags.RF_BeginDestroyed | EObjectFlags.RF_FinishDestroyed
    | EObjectFlags.RF_NeedInitialization | EObjectFlags.RF_NeedLoad
    | EObjectFlags.RF_NeedPostLoad | EObjectFlags.RF_NeedPostLoadSubobjects

local function canRead(value)
    return value and value:IsValid() and not value:HasAnyFlags(reject)
end

local function inspectAnimals()
    local world
    for _, control in ipairs(FindAllOf("PlayerController") or {}) do
        if canRead(control) and control:IsLocalController() then
            local pawn = control:GetPropertyValue("Pawn")
            if canRead(pawn) and canRead(control:GetWorld())
                and pawn:GetWorld() == control:GetWorld() then
                world = control:GetWorld()
                break
            end
        end
    end
    if not world then
        print("[read-only] No usable local player/world.\n")
        return
    end
    local candidates = FindAllOf("AnimalBase") or {}
    for index, candidate in ipairs(candidates) do
        if index > 32 then break end
        if canRead(candidate) and candidate:GetWorld() == world then
            local control = candidate:GetPropertyValue("Controller")
            if canRead(control) and control:GetWorld() == world
                and control:GetPropertyValue("Pawn") == candidate then
                print("[read-only] world: " .. world:GetFullName() .. "\n")
                print("[read-only] animal: " .. candidate:GetFullName() .. "\n")
                print("[read-only] animal class: " .. candidate:GetClass():GetFullName() .. "\n")
                print("[read-only] controller: " .. control:GetFullName() .. "\n")
                print("[read-only] controller class: " .. control:GetClass():GetFullName() .. "\n")
                print("[read-only] Pawn backlink matched; no behavior was changed.\n")
                return
            end
        end
    end
    print("[read-only] No pair in the first 32 candidates; result is inconclusive.\n")
end

RegisterKeyBind(Key.F9, {ModifierKey.CONTROL, ModifierKey.ALT}, function()
    if pending then return end
    if not EngineTickAvailable then
        print("[read-only] EngineTick unavailable; no scan queued.\n")
        return
    end
    pending = true
    local queued, reason = pcall(function()
        ExecuteInGameThread(function()
            local ok, problem = pcall(inspectAnimals)
            pending = false
            if not ok then print("[read-only] Read failed: " .. tostring(problem) .. "\n") end
        end, EGameThreadMethod.EngineTick)
    end)
    if not queued then
        pending = false
        print("[read-only] Scheduling failed: " .. tostring(reason) .. "\n")
    end
end)
print("[read-only] Ready. Ctrl+Alt+F9 requests one scan.\n")
