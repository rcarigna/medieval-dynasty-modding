---
title: "Tools and prerequisites"
evidence_status: "Documented"
reviewed: "2026-11-02"
---

# Keep the toolchain small

| Tool | Why you need it | Source |
| --- | --- | --- |
| A legal PC installation of Medieval Dynasty | The application you intend to inspect | Your game's distributor |
| A text editor and basic Git knowledge | Review scripts and record documentation changes | Your preferred editor; [Git documentation](https://git-scm.com/doc) |
| An explicitly selected UE4SS build | Lua/native binding host for a later approved runtime experiment | [Upstream releases](https://github.com/UE4SS-RE/RE-UE4SS/releases) |
| Lua 5.4 language reference | Understand host-independent syntax | [Lua manual](https://lua.org/manual/5.4/) |
| Isolated backup/test data | Make any later experiment reversible | Maintain your own private backup; do not upload it |

Python and MkDocs are needed to build **this documentation**, not to run a Lua inspection mod. Unreal Editor, an SDK generator, a disassembler and C++ build tools are not prerequisites for reading these pages or reviewing the first example.

Select the loader by exact artifact/revision and verify its published checksum after downloading. A moving “latest” URL or the same Unreal minor version is not a compatibility guarantee. Do not redistribute its DLLs in a mod example.

Review [compatibility](../concepts/compatibility.md) before installation and [debugging/rollback](debugging.md) before launching a modified game. Store names and version differences matter; this reference makes no claim that every PC distribution is equivalent.
