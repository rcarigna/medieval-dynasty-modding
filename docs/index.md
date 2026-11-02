---
title: "Medieval Dynasty Modding"
evidence_status: "Documented"
reviewed: "2026-11-02"
---

# Make your first investigation understandable

Learn the language, identify the abstraction layer, and record what you actually observed.

This is an unofficial community reference for Medieval Dynasty mod developers. Start with [the introduction](getting-started/introduction.md), then follow the [first-probe guide](getting-started/first-probe.md). Experienced TypeScript or C# developers can jump to [Lua comparisons](getting-started/lua.md).

## Follow a useful path

| Your question | Start here |
| --- | --- |
| What does UE4SS provide? | [UE4SS fundamentals](getting-started/ue4ss.md) |
| Is this Lua, a binding, or a game API? | [Provenance reference](reference/provenance.md) |
| How do pawns and controllers relate? | [Object model](concepts/object-model.md) |
| How can I inspect without altering behavior? | [Original animal example](examples/animal-inspection.md) |
| What is known about animals? | [Animals and wildlife](systems/animals.md) |
| How do I contribute an observation? | [Evidence standards](community/evidence.md) |

## Read evidence before assuming compatibility

**Documented**, **Historical evidence**, **Inferred**, and **Runtime verified** describe different levels of support. A documented UE4SS function does not establish that a Medieval Dynasty class or property works on a particular build.

No current-build animal/controller relationship is runtime verified in the initial reference. Build 25776186 and UE4SS 3.0.1-1196-g236adf26 are source-review context, not a compatibility certificate. [Understand the labels](community/evidence.md).

This project publishes original explanations, examples and curated links. It does not distribute proprietary game implementations, extracted assets, DLLs, saves or generated SDK dumps. Read the [contribution and licensing policy](community/licensing.md).
