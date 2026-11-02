---
title: "UE4SS bindings"
evidence_status: "Documented"
reviewed: "2026-11-02"
---

# UE4SS APIs and bindings

These interfaces are documented/source-confirmed at **236adf2667832375877669faac4b78872b4736b0** (3.0.1-1196-g236adf26). They are a curated reference, not a compatibility certificate or a list of only the symbols in one example.

## UE4SS globals

| Symbol used | Origin / layers | Type | Inspection purpose | Availability | Reference | Caveats |
| --- | --- | --- | --- | --- | --- | --- |
| `FindAllOf(...)`; `FindAllOf(query)` | UE4SS binding → native Unreal object discovery | Global function | Search non-default instances by short class name, including derived instances under the documented behavior | Documented | [Pinned docs][find], [registration][bindings] | nil for no results; only loaded objects. Search is not restricted to the selected world or bounded by the caller's loop limit |
| `RegisterKeyBind(...)` | UE4SS input facility | Global function | Register manual Ctrl+Alt+F9 callback | Documented | [Pinned docs][keybind], [implementation][bindings] | Registration is outside the example's pcall; callback requires game/debug-console focus under documented behavior |
| `ExecuteInGameThread(...)` | UE4SS scheduling → native engine hook | Global function | Queue one inspection callback, explicitly using EngineTick | Documented | [Pinned docs][execute], [implementation][schedule] | Returns no inspection result/promise. Explicit unavailable-method behavior differs from documentation; see discrepancy section |

There is no ordinary Lua implementation of these three globals in inspection patterns. Running the file in a stock interpreter would not provide them, the key tables, flags or wrapper types.


## Input and scheduling constants

| Symbol used | Origin / layers | Type | Inspection purpose | Availability | Reference | Caveats |
| --- | --- | --- | --- | --- | --- | --- |
| `Key` | UE4SS | Host-populated table | Supply keyboard key code | Documented | [Docs][keys], [source][bindings] | Not a Lua language enum; pinned implementation populates integers |
| `Key.F9` | UE4SS → Windows input key code | Table constant | Select F9 | Documented | [Docs][keys], [source line 547][key-source] | Field name is case-sensitive; actual key delivery is not runtime verified |
| `ModifierKey` | UE4SS | Host-populated table | Supply required modifier codes | Documented | [Docs][modifiers], [source][modifier-source] | Not the modifier-sequence literal; `{…}` is ordinary Lua |
| `ModifierKey.CONTROL` | UE4SS → Windows modifier code | Table constant | Require Ctrl | Documented | [Docs][modifiers], [source][modifier-source] | Source value is integer 0x11; docs' description says strings |
| `ModifierKey.ALT` | UE4SS → Windows modifier code | Table constant | Require Alt | Documented | [Docs][modifiers], [source][modifier-source] | Source value is integer 0x12; same documentation mismatch |
| `EngineTickAvailable` | UE4SS capability exposure | Global Boolean | Refuse scheduling when EngineTick is unavailable | Documented | [Docs][method], [initialization source][capabilities] | Populated during mod setup from hook capability; not an Unreal property or a game-mode check |
| `EGameThreadMethod` | UE4SS | Host-populated enum-style table | Name supported scheduling methods | Documented | [Docs][method], [source][capabilities] | This is a Lua table exposing C++ enum values |
| `EGameThreadMethod.EngineTick` | UE4SS → engine tick hook choice | Table constant | Explicitly select the requested execution context | Documented | [Docs][method], [source][capabilities] | Queues one task; does not make inspect run every frame |


## UObject wrapper methods

These methods are supplied by the UE4SS userdata/metatable surface. Some share names with native engine functions; that does not make them reflected UFunctions.

| Exact expression(s) in inspection patterns | Origin / layers | Type | Inspection purpose | Availability | Reference | Caveats |
| --- | --- | --- | --- | --- | --- | --- |
| `object:IsValid()` | UE4SS wrapper validation over native UObject state | Wrapper method | Reject invalid wrappers in live | Documented | [Wrapper docs][uobject], [implementation][valid-source] | Checks pointer/sentinel, tracked object map and reachability at this pin; not biological life or a lifetime lock |
| `object:HasAnyFlags(EXCLUDED)` | UE4SS binding → Unreal UObject flag test | Wrapper method | Reject any excluded flag bit | Documented | [Wrapper docs][uobject], [implementation][uobject-source] | Native method underneath; EXCLUDED is local, and its list is not exhaustive safety proof |
| `object:GetFullName()`; `object:GetClass():GetFullName()` | UE4SS binding → Unreal object metadata | Wrapper method | Log instance and class identity strings | Documented | [Wrapper docs][uobject], [implementation][uobject-source] | Diagnostic names are not durable identity; second expression operates on a wrapped UClass |
| `object:GetClass()` | UE4SS binding → Unreal UClass | Wrapper method | Obtain reflected type metadata | Documented | [Wrapper docs][uobject], [implementation][uobject-source] | Does not return another animal or a Lua class definition |
| `pc:GetWorld()`; `pawn:GetWorld()`; `animal:GetWorld()`; `controller:GetWorld()`; `best:GetWorld()`; `bestController:GetWorld()` | UE4SS binding → native UObject::GetWorld | Wrapper method | Anchor/filter/recheck a shared UWorld | Documented | [Wrapper docs][uobject], [direct native call][world-source] | Native ownership/context lookup, not FindAllOf or a map-name match; may return an invalid wrapper |
| `pc:GetPropertyValue("Pawn")`; `animal:GetPropertyValue("Controller")`; `controller:GetPropertyValue("Pawn")`; `best:GetPropertyValue("Controller")`; `bestController:GetPropertyValue("Pawn")` | UE4SS binding → Unreal reflection over receiver's class | Wrapper method `GetPropertyValue` | Read the named native relationship | Documented for getter; Historical evidence for expected fields | [Wrapper docs][uobject], [getter implementation][getter-source], [fields below](unreal.md#reflected-engine-members) | String lookup and marshaling can fail. Missing/unusable member is not necessarily the same as a valid property containing null |


## Object flags

All constants below have **Unreal Engine EObjectFlags semantics** and are **exposed as integer entries by UE4SS**. They are not custom Medieval Dynasty flags. References for each row are the pinned [flag table documentation][flags] and [binding source][bindings].

| Symbol used | Origin / layers | Type | Purpose in EXCLUDED | Availability | Reference | Caveats |
| --- | --- | --- | --- | --- | --- | --- |
| `EObjectFlags` | Unreal enum → UE4SS | Host-populated table | Namespace for combined mask | Documented | [Docs][flags], [source][bindings] | Lua `\|` combines values; table itself is not the mask |
| `EObjectFlags.RF_ClassDefaultObject` | Unreal → UE4SS | Flag constant | Exclude class default templates | Documented | [Docs][flags], [source][bindings] | A CDO is not a live animal |
| `EObjectFlags.RF_ArchetypeObject` | Unreal → UE4SS | Flag constant | Exclude archetype templates | Documented | [Docs][flags], [source][bindings] | Template classification is distinct from life/death |
| `EObjectFlags.RF_BeginDestroyed` | Unreal → UE4SS | Flag constant | Reject destruction already begun | Documented | [Docs][flags], [source][bindings] | Absence does not lock lifetime |
| `EObjectFlags.RF_FinishDestroyed` | Unreal → UE4SS | Flag constant | Reject finished destruction state | Documented | [Docs][flags], [source][bindings] | Same limitation |
| `EObjectFlags.RF_NeedInitialization` | Unreal → UE4SS | Flag constant | Reject unfinished native initialization | Documented | [Docs][flags], [source][bindings] | No assertion of gameplay readiness when absent |
| `EObjectFlags.RF_NeedLoad` | Unreal → UE4SS | Flag constant | Reject pending-load objects | Documented | [Docs][flags], [source][bindings] | Not an instruction to load anything |
| `EObjectFlags.RF_NeedPostLoad` | Unreal → UE4SS | Flag constant | Reject pending post-load work | Documented | [Docs][flags], [source][bindings] | Does not check actor health/brain state |
| `EObjectFlags.RF_NeedPostLoadSubobjects` | Unreal → UE4SS | Flag constant | Reject pending subobject post-load work | Documented | [Docs][flags], [source][bindings] | Filter covers only these named bits |


## Read implementation and documentation together

The pinned Key/ModifierKey docs describe strings, but the implementation populates integer entries. The explicit EngineTick scheduling path in source throws if unavailable, although documentation describes fallback. Do not depend on fallback; guard and protect scheduling, then separately protect the eventual work.

The EObjectFlags meanings belong to Unreal Engine; UE4SS provides the Lua table and native wrapper methods. Lua's `|` combines their integer values. Neither a valid wrapper nor an excluded-flags test means “animal is alive.”

See [the provenance standard](provenance.md) and [the object model](../concepts/object-model.md). No API entry here has a runtime-verified game relationship attached.


[bindings]: https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/UE4SS/src/Mod/LuaMod.cpp
[find]: https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/docs/lua-api/global-functions/findallof.md
[keybind]: https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/docs/lua-api/global-functions/registerkeybind.md
[execute]: https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/docs/lua-api/global-functions/executeingamethread.md
[method]: https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/docs/lua-api/table-definitions/egamethreadmethod.md
[keys]: https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/docs/lua-api/table-definitions/key.md
[modifiers]: https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/docs/lua-api/table-definitions/modifierkey.md
[key-source]: https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/UE4SS/src/Mod/LuaMod.cpp#L547
[modifier-source]: https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/UE4SS/src/Mod/LuaMod.cpp#L608
[capabilities]: https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/UE4SS/src/Mod/LuaMod.cpp#L4302
[schedule]: https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/UE4SS/src/Mod/LuaMod.cpp#L4323
[uobject]: https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/docs/lua-api/classes/uobject.md
[uobject-source]: https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/UE4SS/include/LuaType/LuaUObject.hpp
[valid-source]: https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/UE4SS/include/LuaType/LuaUObject.hpp#L763
[world-source]: https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/UE4SS/include/LuaType/LuaUObject.hpp#L642
[getter-source]: https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/UE4SS/include/LuaType/LuaUObject.hpp#L622
[flags]: https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/docs/lua-api/table-definitions/eobjectflags.md
