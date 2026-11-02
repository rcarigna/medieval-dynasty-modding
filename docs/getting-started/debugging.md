---
title: "Debugging, logging and rollback"
evidence_status: "Documented"
reviewed: "2026-11-02"
---

# Locate the failing layer

| Symptom | Investigate | Do not conclude |
| --- | --- | --- |
| Parse error before a “ready” message | Lua syntax/version and top-level setup | Animal interfaces are unavailable |
| Missing global / wrong argument or userdata type | UE4SS build, binding name and colon versus dot | The native class is absent |
| Reflected member not found or unsupported marshaling | Exact receiver class, member name and property kind | A valid property simply contains null |
| No animal candidates | Class-name assumptions, loaded population and world | The game has no animals |
| No matching controller backlink | Possession/lifecycle/context or a read failure | Every animal has no AI |
| Native crash | Loader compatibility, layout, native lifetime/invocation | Lua pcall can recover the process |

UE4SS replaces the familiar `print` name with its output implementation. With logging enabled, inspect the loader's log, not a browser console. A source-level read is not runtime evidence; fabricated “expected output” must never be presented as a captured log. [Output implementation](https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/UE4SS/src/LuaLibrary.cpp#L121)

## Record just enough evidence

Include exact versions, the failed operation, concrete class names if observed, and a small redacted excerpt. Remove usernames, absolute paths, save names, network addresses and unrelated session data. Keep full backups/logs private.

## Reversible installation discipline

Close the game before cleanup. Remove only additions listed in your own before/after inventory; restore changed original settings/files from backups. Inspect any unexpected file before removing it. A newly created loader directory can contain generated logs; an existing directory cannot be treated as disposable.

Account for autosaves and cloud sync even if a script makes no explicit save call. A loader's removal does not undo saved gameplay state. Verify a normal startup after cleanup using your chosen test process; ordinary game-generated writes still need accounting.

This site does not provide a universal deletion command or a machine-specific rollback manifest. See [the first-probe checklist](first-probe.md) and [compatibility reports](../community/reporting.md).
