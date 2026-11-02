---
title: "API provenance and availability"
evidence_status: "Documented"
reviewed: "2026-11-02"
---

# Ask which layer owns the name

A readable expression can span several layers:

```lua
local controller = animal:GetPropertyValue("Controller")
```

`local` and `:` are Lua syntax. `GetPropertyValue` is a UE4SS wrapper method. `Controller` is a reflected Unreal Pawn property. The particular animal object and its concrete class belong to the game.

## Curated reference map

| Surface | Reference | Evidence boundary |
| --- | --- | --- |
| Standard library and host-overridden print | [Lua library](lua.md) | Language behavior versus host output routing |
| Discovery, input, scheduling and UObject wrapper methods | [UE4SS bindings](ue4ss.md) | Documented binding versus actual target-game success |
| Pawn/Controller properties, engine methods, FVector | [Unreal interfaces](unreal.md) | Standard engine concepts versus reflected names/layouts in a game build |
| AnimalBase and BP_AnimalBase_C | [Game-specific entries](game-interfaces.md) | Historical evidence and inferred continuity, not current runtime proof |

## Availability labels

Use the full terms consistently:

- **Documented**: supported by authoritative upstream documentation or implementation at the cited revision.
- **Historical evidence**: found in older declarations or documentation; not a current-build assertion.
- **Inferred**: plausible interpretation or applicability that has not been demonstrated.
- **Runtime verified**: actually observed on a specific game build/loader/context with a reproducible, sanitized record.

The initial site has no runtime-verified Medieval Dynasty animal/controller relationship. A link to a documented function does not promote a game assumption to Runtime verified.

## Discrepancies are useful evidence

At the pinned UE4SS revision, Key tables contain integers despite documentation describing strings. Explicit scheduling with an unavailable requested hook throws in implementation despite documented fallback. [Binding details and source citations](ue4ss.md#read-implementation-and-documentation-together)

Prefer a precisely labeled discrepancy over silently merging the claims. Record the exact pin, which source says what, and whether a runtime observation exists.

## Adding an API entry

Include symbol, origin/layer, kind, purpose, expected behavior, build/loader context, verification status, sources, limitations, related APIs and an original usage example. A source-review build is not automatically a tested build.

Keep C++ convenience wrappers distinct from actual reflected UFunctions. Never copy implementations or bulk SDK content into a reference entry. [Contribution standard](../community/evidence.md)
