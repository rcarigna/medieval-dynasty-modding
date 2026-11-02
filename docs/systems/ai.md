---
title: "AI controllers and behavior"
evidence_status: "Inferred"
reviewed: "2026-11-02"
game_build: "25776186"
ue4ss_version: "3.0.1-1196-g236adf26"
runtime_verified: false
---

# A controller reference is not the AI implementation

Unreal controllers direct pawns. A consistent animal/controller backlink can establish a structural relationship at one instant. It does not prove the controller subtype, an active behavior tree, the current decision task, or a safe replacement point. [Engine framework](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-framework-quick-reference?application_version=4.27)

The starter example does not test AIController inheritance or inspect a brain component. The concrete controller class is an unanswered runtime question.

## Behavior trees are an engine concept

Unreal behavior trees can use Blackboard data to select tasks. Knowing this engine architecture does not establish that every Medieval Dynasty animal uses it or that its tree can be swapped safely. [Epic behavior-tree reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-trees?application_version=4.27)

Observe classes, component identities and reflected interfaces before proposing a behavioral intervention. Historical names alone cannot establish scheduling, possession, initialization, authority or cleanup semantics.

## Keep experiments separate

Document object visibility first. Evaluate any behavior modification as a separate, reversible proposal with its own evidence, risk and undo criteria. Runtime persistence and co-op replication require further independent observations. This site supplies no framework, AI replacement or proposed public API disguised as existing functionality.
