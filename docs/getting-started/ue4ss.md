---
title: "UE4SS fundamentals"
evidence_status: "Documented"
reviewed: "2026-11-02"
---

# UE4SS is the host and bridge

Lua supplies closures, tables, iteration and protected calls. UE4SS adds native-bound globals such as `FindAllOf` and `ExecuteInGameThread`, input binding, and userdata wrappers for Unreal objects. A stock Lua interpreter does not supply these globals.

Think in layers:

```text
Lua syntax → UE4SS binding → Unreal reflected interface → game-defined object
```

For example, `animal:GetPropertyValue("Controller")` uses Lua colon syntax, a UE4SS getter, an inherited Unreal Pawn property, and a particular game instance. None of those names establishes whether the object currently exists.

## What discovery returns

`FindAllOf("PlayerController")` is a class-name search for currently loaded instances under the documented lookup semantics. It returns Lua-accessible wrappers, not a JSON snapshot or a copy of the game state. Search results can include another world or become unsuitable before later access. [Pinned lookup documentation](https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/docs/lua-api/global-functions/findallof.md)

`GetClass`, `GetFullName` and `GetWorld` help identify what a wrapper refers to. `IsValid` and object flags help reject unsuitable objects, but do not prove actor health, AI activity or native memory safety. [Pinned wrapper documentation](https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/docs/lua-api/classes/uobject.md)

## Learn the distinction before changing code

A binding error, missing reflected property, empty search result and a wrong game-specific class assumption are different failures. Start with [API provenance](../reference/provenance.md) and the [first-probe workflow](first-probe.md). The initial example only reads; it does not unlock consoles, patch assets, create actors, hook gameplay functions or modify AI.
