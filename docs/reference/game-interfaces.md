---
title: "Medieval Dynasty interfaces"
evidence_status: "Historical evidence"
reviewed: "2026-11-02"
game_build: "25776186"
ue4ss_version: "3.0.1-1196-g236adf26"
runtime_verified: false
---

# Game-specific interface leads

**No current-build animal/controller relationship is runtime verified here.** The build/loader metadata on this page identifies review context, not a successful test.

Historical citations below identify a few exposed interface names and inheritance relationships. They are links to existing declarations; no generated SDK or game implementation is redistributed.

## AnimalBase

| Field | Entry |
| --- | --- |
| Symbol | `"AnimalBase"` as a short-name query; historical C++ spelling `AAnimalBase` |
| Origin/layer | Medieval Dynasty native class, queried through UE4SS |
| Kind | Game class / query string |
| Purpose | Narrow object discovery to candidate animals |
| Expected behavior | Historical declaration derives from Unreal ACharacter; a matching loaded population might be returned |
| Game build/version | Review context: Steam build 25776186; no runtime verification |
| UE4SS version | Source-review pin: 3.0.1-1196-g236adf26 |
| Verification | **Historical evidence** for name/inheritance; **Inferred** for applicability to this build |
| Supporting evidence | [Historical class declaration](https://github.com/stulu08/Medieval-Dynasty-Mod-Loader/blob/ef78da996dc77a2372fed9eaeabb9210e5c38774/SDK/src/Medieval_Dynasty/Medieval_Dynasty/AnimalBase.h#L11) |
| Known limitations | Does not establish species coverage, loaded population, biological life, AI subtype or property marshaling |
| Related APIs | [FindAllOf](ue4ss.md#ue4ss-globals), [engine Pawn/Controller](unreal.md), [animal example](../examples/animal-inspection.md) |

Original usage fragment, requiring a qualified UE4SS game-thread context:

```lua
local candidates = FindAllOf("AnimalBase") or {}
print("Loaded candidates: " .. tostring(#candidates) .. "\n")
```

Empty results are inconclusive; this query does not load every animal asset.

## BP_AnimalBase_C

| Field | Entry |
| --- | --- |
| Symbol | `"BP_AnimalBase_C"`; historical C++ generated spelling `ABP_AnimalBase_C` |
| Origin/layer | Medieval Dynasty Blueprint-generated class, queried through UE4SS |
| Kind | Game class / query string |
| Purpose | Alternative historical inspection lead |
| Expected behavior | Historical declaration derives from AAnimalBase |
| Game build/version | Review context: build 25776186; no observed class identity |
| UE4SS version | Source-review pin: 3.0.1-1196-g236adf26 |
| Verification | **Historical evidence**; continued runtime availability is **Inferred** |
| Supporting evidence | [Historical declaration](https://github.com/stulu08/Medieval-Dynasty-Mod-Loader/blob/ef78da996dc77a2372fed9eaeabb9210e5c38774/SDK/src/Medieval_Dynasty/BP_AnimalBase/BP_AnimalBase_C.h#L11) |
| Known limitations | Class name is not an instance name or an established /Game asset path; not used as fallback by the starter example |
| Related APIs | [AnimalBase](#animalbase), [FindAllOf](ue4ss.md#ue4ss-globals) |

Original optional query fragment, not an automatic compatibility workaround:

```lua
local blueprintCandidates = FindAllOf("BP_AnimalBase_C") or {}
print("Blueprint candidates: " .. tostring(#blueprintCandidates) .. "\n")
```

## AIControllerRef

| Field | Entry |
| --- | --- |
| Symbol | `AIControllerRef` |
| Origin/layer | Historical Medieval Dynasty Blueprint-visible field, accessed only if its current metadata is observed |
| Kind | Controller-reference property |
| Purpose | Potential future comparison against inherited Pawn.Controller |
| Expected behavior | Declaration suggests a reference, not synchronization or ownership semantics |
| Game build/version | No current-build observation |
| UE4SS version | No successful access recorded; review pin above is context only |
| Verification | **Historical evidence**; current semantics are **Inferred** |
| Supporting evidence | [Historical field declaration](https://github.com/stulu08/Medieval-Dynasty-Mod-Loader/blob/ef78da996dc77a2372fed9eaeabb9210e5c38774/SDK/src/Medieval_Dynasty/BP_AnimalBase/BP_AnimalBase_C.h#L294) |
| Known limitations | Not read by the starter example; do not substitute it for the standard Controller field or assume it is authoritative |
| Related APIs | [Unreal Controller property](unreal.md#reflected-engine-members), [GetPropertyValue](ue4ss.md#uobject-wrapper-methods) |

An original proposed inspection pattern is to first record the receiver's actual class and current property metadata, then compare the two fields without mutating either. No executable access example is supplied because the current receiver/property availability has not been established.

## Current-build verification ledger

No runtime entries exist yet. To add one, record game build/version/store, exact loader revision, effective configuration, map/mode, actual class names, the operation attempted, and a short sanitized result. Preserve failures and nulls as well as successes. [Required evidence fields](../community/evidence.md)

Standard engine properties `Pawn` and `Controller` are documented on the [Unreal interface page](unreal.md); do not mislabel them as custom Medieval Dynasty APIs.
