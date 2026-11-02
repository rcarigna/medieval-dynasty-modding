---
title: "Compatibility and game updates"
evidence_status: "Inferred"
reviewed: "2026-11-02"
game_build: "25776186"
ue4ss_version: "3.0.1-1196-g236adf26"
runtime_verified: false
---

# Compatibility is a tuple, not a badge

Record the game build/version and store, loader artifact/revision, effective configuration, map, mode and observed operation. “UE 4.27” or “latest UE4SS” is not enough.

The initial reference reviews UE4SS 3.0.1-1196-g236adf26. Historical game interfaces are leads for build 25776186, not evidence that the loader or animal example has succeeded there. No animal/controller relationship is runtime verified in this initial site.

## Updates can invalidate different layers

| Change | What may need rechecking |
| --- | --- |
| Game patch | Class names, reflection metadata, native layouts, signatures, lifecycle |
| Loader change | Lua API surface, property marshaling, hook availability, configuration defaults |
| Different map/mode/store | Loaded classes, authority, local-player selection, actor/controller availability |
| Additional mods | Hook/load order, overwritten assets, input conflicts and changed runtime state |

Begin again with loader startup and object visibility. Do not “repair” an unknown version by copying numeric offsets from a historical SDK. A class query, a property read, a controller backlink and a behavior change are separate validation gates.

## Single-player and co-op

A local player controller can exist in single-player, on a host, or on a client. Locality is not authority. A visible or locally spawned actor is not proof of a shared replicated actor. Custom Lua state does not replicate by existing in a host process. [Engine replication reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/actor-replication?application_version=4.27)

The starter example requires an independently selected disposable single-player context. It does not enforce that mode. No host-only, matching-client-mod or crossplay compatibility is claimed.

Report a precise failure through the [compatibility template](../community/reporting.md). Keep historical evidence when a new runtime result is added; do not overwrite a failed build's record with a generic “works now.”
