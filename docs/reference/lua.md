---
title: "Lua library reference"
evidence_status: "Documented"
reviewed: "2026-11-02"
---

# Lua library used in inspection

This is a curated set of library calls and patterns. The [standalone example](../examples/animal-inspection.md) uses a subset; the [Lua guide](../getting-started/lua.md) explains the language syntax.

**Documented** describes the language/library contract. It is not a Medieval Dynasty runtime verification.

## Lua library surface

| Symbol used | Origin / layers | Type | Inspection purpose | Availability | Reference | Caveats |
| --- | --- | --- | --- | --- | --- | --- |
| `print(...)` | Lua standard-library name → UE4SS replacement | Global native-bound function | Emit prefixed probe output | Documented | [Base library][base], [host registration][bindings], [host output][output] | This pin registers LuaLibrary::global_print; do not assume terminal stdout |
| `ipairs(...)` | Lua standard library | Iterator factory | Visit player-controller and animal result sequences | Documented | [Implementation][base], [manual][ipairs] | Starts at 1, stops at the first nil; not arbitrary-key enumeration |
| `pcall(...)` | Lua standard library | Protected-call function | Catch scheduling, inspection and per-candidate Lua errors | Documented | [Implementation][base], [manual][pcall] | Returns status plus results/error value; native process crashes are not caught |
| `tostring(err)`; `tostring(failure)` | Lua standard library | Conversion function | Convert caught error values for concatenation | Documented | [Implementation][base], [manual][tostring] | An error need not be a string; conversion is not a traceback |
| `string` | Lua standard library | Library table | Namespace for formatting | Documented | [String library][strings] | This is a table, not a class/static C# type |
| `string.format(...)` | Lua standard library | Table function | Format counts/distance with `%s`, `%d`, `%.1f` | Documented | [String library][strings], [manual][format] | Dot call; wrong number/type of arguments can raise a Lua error |
| `math` | Lua standard library | Library table | Namespace for numeric helpers | Documented | [Math library][maths] | Numeric helpers do not know Unreal's unit system |
| `math.min(#animals, MAX_CANDIDATES)` | Lua standard library | Table function | Report number considered under cap | Documented | [Math library][maths] | Does not constrain the preceding native search/allocation |
| `math.sqrt(bestDistance)` | Lua standard library | Table function | Convert squared straight-line distance to length | Documented | [Math library][maths] | Input is the earlier sample; division by 100 is a separate assumption |



[base]: https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/deps/first/LuaRaw/src/lbaselib.c
[strings]: https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/deps/first/LuaRaw/src/lstrlib.c
[maths]: https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/deps/first/LuaRaw/src/lmathlib.c
[bindings]: https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/UE4SS/src/Mod/LuaMod.cpp
[output]: https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/UE4SS/src/LuaLibrary.cpp#L121
[ipairs]: https://lua.org/manual/5.4/manual.html#pdf-ipairs
[pcall]: https://lua.org/manual/5.4/manual.html#pdf-pcall
[tostring]: https://lua.org/manual/5.4/manual.html#pdf-tostring
[format]: https://lua.org/manual/5.4/manual.html#pdf-string.format
