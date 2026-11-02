---
title: "A first read-only probe"
evidence_status: "Inferred"
reviewed: "2026-11-02"
game_build: "25776186"
ue4ss_version: "3.0.1-1196-g236adf26"
runtime_verified: false
---

# Make one observation, then stop

The first useful question is: **can an explicitly chosen loader expose one candidate animal and a consistent controller relationship in the selected world?**

Review the [original example](../examples/animal-inspection.md) before considering execution. It is untested in-game. It has no configuration installer or automatic compatibility fix.

## Before any runtime test

1. Record your game build/version, store, map/mode and exact loader artifact/revision. Do not reuse a historical version label as a current observation.
2. Read the loader's upstream installation instructions for that artifact. Inventory every proposed addition/change and reject collisions with existing loaders.
3. Back up your own saves/settings while the game is closed. Resolve cloud synchronization behavior and use a disposable single-player session.
4. Keep only the reviewed example enabled. Bundled gameplay mods or an external enabled.txt can broaden what runs; a mod-list entry alone is not a full isolation guarantee.
5. Define your rollback before copying anything. Do not overwrite original content or production saves for an inspection experiment.

The file layout depends on the chosen UE4SS artifact. In the reviewed experimental layout a Lua mod uses a named mod directory containing `Scripts/main.lua` and an explicit mod-list entry. Do not infer a complete install manifest from that relative convention; inspect the actual archive and its upstream documentation.

## If you choose to test after reviewing the risks

Load a disposable single-player world, approach an animal, wait for streaming to settle, and use the example's manual key combination. Read the loader log. Preserve a short sanitized excerpt and record whether discovery, property access and the controller backlink succeeded independently.

A success records one relationship at one moment, not living status, AI behavior, save support or co-op compatibility. A failure should become a [versioned compatibility report](../community/reporting.md), not an automatic search for new offsets or a reason to run unrelated tooling.

For an unmodified documentation build, none of these runtime steps is performed. See [debugging and rollback](debugging.md).
