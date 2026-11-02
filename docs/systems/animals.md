---
title: "Animals and wildlife"
evidence_status: "Historical evidence"
reviewed: "2026-11-02"
game_build: "25776186"
ue4ss_version: "3.0.1-1196-g236adf26"
runtime_verified: false
---

# Animals: an interface map, not a behavior guarantee

Historical declarations identify a native `AAnimalBase` derived from engine `ACharacter`, and a generated `ABP_AnimalBase_C` below it. These are useful class-query leads. Their current-build population, exact inheritance and concrete species classes remain unverified. [Curated entries and sources](../reference/game-interfaces.md)

An inspection can distinguish:

- the class of a loaded animal instance;
- its world and inherited controller reference;
- the controller's reverse Pawn relationship;
- any error encountered while reading those interfaces.

The [original example](../examples/animal-inspection.md) attempts only that structural observation. It does not check whether an animal is alive, visible, friendly, domestic or controlled by active AI.

## Good next observations

Record exact instance/class names and controller class names with the build, loader, map and mode. Keep separate records for species and different contexts; one successful class search does not cover unloaded content or every animal.

A historical Blueprint field called `AIControllerRef` is separate from inherited Pawn.`Controller`. No equivalence or synchronization between them has been established. Do not substitute one without evidence.

Predator/livestock interaction, custom dog assets, domestication, serialization and new species support are outside the established results. Link a reproducible observation before adding those claims. Continue with [AI/controller boundaries](ai.md).
