---
title: "Introduction to modding"
evidence_status: "Inferred"
reviewed: "2026-11-02"
game_build: "25776186"
ue4ss_version: "3.0.1-1196-g236adf26"
runtime_verified: false
---

# Start with a question you can observe

Medieval Dynasty is an Unreal Engine game. A runtime tool such as UE4SS may expose objects, reflected properties and functions to a Lua script. That makes inspection a useful first experiment; it does not establish a supported game SDK or universal loader compatibility.

The initial reference uses source review of UE4SS 3.0.1-1196-g236adf26 and historical animal interface names. Build 25776186 is a compatibility context that still needs a runtime observation. Nothing here certifies that your installed build matches it.

## A practical learning sequence

1. Learn [what UE4SS adds to Lua](ue4ss.md).
2. Read [the object model](../concepts/object-model.md), especially wrappers and lifetime.
3. Understand the [evidence labels](../community/evidence.md).
4. Review the [small original inspection example](../examples/animal-inspection.md).
5. Record one concrete result with the game build, loader revision, mode, sources and limitations.

Changing a reflected property, spawning an actor, replacing AI, persisting state and synchronizing co-op are separate experiments. An object name in a log establishes none of those.

For first-time tooling setup, continue with [tools and prerequisites](tools.md). This project supplies documentation and source examples, never game binaries or a bundled mod loader.
