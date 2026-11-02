---
title: "Reporting compatibility problems"
evidence_status: "Documented"
reviewed: "2026-11-02"
---

# Report an operation, not just “broken”

Use the repository's compatibility issue form. A useful report distinguishes loader startup from discovery, property reads, method dispatch and controller matching.

Include exact game/store/build, UE4SS artifact/revision, map/mode, enabled mods, script revision, reproduction steps and the smallest sanitized excerpt that demonstrates the failure. State if the result has not been reproduced.

## Keep evidence public-safe

Do not upload a save, whole session log, extracted SDK, memory dump, binary or asset. Replace personal filenames/paths and network details with neutral labels. Avoid credentials and account identifiers.

Classify the failing layer:

1. Lua syntax/environment.
2. UE4SS binding/capability/marshaling.
3. Unreal reflection/member lookup/lifetime.
4. Game-specific name or behavior assumption.

Do not propose copied offsets or an unreviewed binary as a workaround. A null controller, a failed lookup and an unsupported property type need separate descriptions. Link a [versioned observation](evidence.md) when there is one.
