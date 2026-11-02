---
title: "Object discovery and safe property access"
evidence_status: "Inferred"
reviewed: "2026-11-02"
game_build: "25776186"
ue4ss_version: "3.0.1-1196-g236adf26"
runtime_verified: false
---

# Separate discovery from property access

The snippets below are original teaching fragments, not standalone runnable mods. They require a qualified UE4SS environment, the game thread, and a known receiver. Read the [complete example](animal-inspection.md) for scheduling and error boundaries.

## Discovery does not load content

```lua
local results = FindAllOf("PlayerController") or {}
for _, receiver in ipairs(results) do
    -- A returned wrapper still needs validity, flags and world checks.
end
```

The class name is a short-name lookup, not a file path. Empty results do not establish that a class or feature cannot exist. Do not scan the entire object population every frame to compensate for an unknown query. [Pinned API](https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/docs/lua-api/global-functions/findallof.md)

## A protected read needs the right type

```lua
-- Preconditions: receiver is a usable AController in the intended world.
local ok, pawnOrError = pcall(function()
    return receiver:GetPropertyValue("Pawn")
end)
if not ok then
    print("Reflected read failed: " .. tostring(pawnOrError) .. "\n")
end
```

This protects a Lua error boundary. It does not validate those preconditions or make a wrong native pointer safe. On success the returned pawn wrapper may still be invalid; test it separately. A missing reflected property, unsupported marshaling and a valid property holding null are different cases.

The setter-shaped name is deliberately absent. Inspect [property provenance](../reference/unreal.md) before changing a field name, and report a mismatch rather than guessing new game APIs.
