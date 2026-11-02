---
title: "Evidence and verification standards"
evidence_status: "Documented"
reviewed: "2026-11-02"
---

# Make the claim no broader than the evidence

| Classification | Required support | Does not establish |
| --- | --- | --- |
| **Documented** | Authoritative upstream docs or implementation, preferably pinned | Successful use in a particular game |
| **Historical evidence** | Dated/pinned older declaration or documentation | Current class identity, layout or behavior |
| **Inferred** | Explicit reasoning from identified sources | An observation that has not happened |
| **Runtime verified** | A specific game/loader/context, reproducible steps and a sanitized observed result | Other builds, maps, modes or behaviors |

A documented `GetPropertyValue` function does not make a guessed game property Runtime verified. A repository link and static source inspection are not a runtime test. Expected output must be labeled illustrative, never captured evidence.

## A reproducible observation

Supply:

- game store, semantic version if observed, and build identifier;
- UE4SS exact artifact/source revision and relevant settings;
- map and single-player/network mode;
- script revision, operation and reproduction steps;
- exact class/member names and a short sanitized log excerpt;
- expected versus observed outcome, errors/nulls and known limits;
- rollback outcome where runtime changes were involved.

Never attach raw saves, complete personal logs, game assets or memory/SDK dumps. Remove personal paths, usernames, addresses, tokens and unrelated session data.

## Page metadata

Game-specific pages carry YAML front matter. This example describes review context and explicitly records no runtime verification:

```yaml
title: Animal interface leads
evidence_status: Historical evidence
reviewed: "2026-11-02"
game_build: "25776186"
ue4ss_version: "3.0.1-1196-g236adf26"
runtime_verified: false
```

A page with Runtime verified metadata must link its sanitized evidence record through `evidence_record` and describe the narrow observation. The validator checks metadata structure, not the truth of a submitted observation; human review remains essential.

Preserve old and failed observations when adding new evidence. Do not silently turn a source-review build into a “tested build.” Cite a stable upstream revision and identify documentation/implementation discrepancies separately.
