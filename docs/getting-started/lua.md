---
title: "Lua for TypeScript and C# developers"
evidence_status: "Documented"
reviewed: "2026-11-02"
---

# Lua for TypeScript and C# developers


The pinned UE4SS source vendors **Lua 5.4.7**, as shown in [lua.h](https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/deps/first/LuaRaw/include/lua.h#L19). This is source evidence, not a measured runtime version. The patterns below are teaching examples; the standalone animal example uses a smaller subset. There is no TypeScript compiler, DOM, React lifecycle, or C# type checker in this script. Native objects are reached through UE4SS bindings.

## Syntax you will actually read

| Probe syntax | TypeScript / C# comparison | Important difference |
| --- | --- | --- |
| `local pending = false` | `let pending = false` / a local `bool` | Lua values carry types; no static annotation or const enforcement |
| `local player, world` | Two locals initialized to absence | Both begin as `nil` |
| `if condition then … end` | `if (condition) { … }` | Blocks end with `end`; braces construct tables |
| `function() … end` | A callback/closure | No arrow syntax; it captures outer locals such as `pending` |
| `-- comment` | `// comment` | Probe comments do not execute |
| `a ~= b` | `a !== b` / `a != b` | Wrapper equality can be customized; see below |
| `a .. b` | String concatenation | `+` is arithmetic, not string interpolation |
| `distance^2` | `distance ** 2` / `Math.Pow(distance, 2)` | Lua `^` is exponentiation, not XOR |
| `flagsA \| flagsB` | Bitwise OR | Distinct from Lua `or` |
| `#animals` | Sequence length | Not a general dictionary count |
| `break` / `return` | Loop exit / function exit | A return inside the per-animal callback exits that callback, not the whole scan |

Uppercase local names such as `MAX_RESULTS` are naming conventions, not enum members or immutable declarations. These syntax forms are implemented by the pinned [Lua parser](https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/deps/first/LuaRaw/src/lparser.c); [Lua's manual](https://lua.org/manual/5.4/manual.html#3) is the language reference.

## Locals, functions and captured state

Top-level `local` names belong to this loaded Lua chunk's lexical scope. Omitting `local` normally assigns into its environment, which is inappropriate for a script's private state. `local function inspectAnimals() … end` defines a local function; it does not call it. It also allows that local function name to be referenced from its own body.

`pending` is captured by the key handler and the later game-thread callback. It outlives an individual key press because registered functions retain the closure. The locals inside `inspectAnimals`, including native-object wrappers, are not retained in those registered callbacks.

Conceptual TypeScript translation:

```ts
let pending = false;
function inspectAnimals() {
  // Variables declared here belong to one inspection.
}
registerKey(() => {
  if (pending) return;
  pending = true;
  postToGameThread(() => {
    // Work happens later; resetting pending belongs to this callback.
  });
});
```

These placeholder APIs are not available TypeScript functions. The flag prevents another scheduled scan while one is pending; it is not a cross-thread lock or a React state hook.

## Tables and iteration

Lua tables cover both record-like and sequence-like uses. In inspection code:

- `{}` is an empty table used as a no-results fallback.
- `{ModifierKey.CONTROL, ModifierKey.ALT}` is a sequence with numeric keys 1 and 2.
- `Key` and `EObjectFlags` are tables populated by UE4SS, not Lua language enums.
- Search results are a UE4SS-created Lua sequence of native-object wrappers.

`for index, animal in ipairs(animals) do … end` iterates consecutive integer keys starting at **1**, stopping at the first absent value. In `for _, pc in ipairs(…)`, `_` is just an ordinary local variable chosen to ignore the index. It is not a discard keyword.

A result loop using these patterns expects dense UE4SS result sequences. Do not substitute arbitrary sparse tables and expect `ipairs` or `#` to behave like JavaScript's array iteration/length. `#` on a table with holes is not a reliable count of its entries. Table iteration is specified by [ipairs](https://lua.org/manual/5.4/manual.html#pdf-ipairs) and implemented in the [pinned base library](https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/deps/first/LuaRaw/src/lbaselib.c).

## Nil, truthiness and short-circuiting

`nil` represents absence. It is the default value of an uninitialized local and an absent table key; assigning `nil` to a table entry removes that entry. It is not a separate `undefined`/`null` pair.

Only `nil` and `false` are false in a condition. In particular, **0**, **""**, an empty table, and an invalid UObject userdata wrapper are all truthy. See the [Lua value rules](https://lua.org/manual/5.4/manual.html#2.1).

`and` and `or` short-circuit and return an operand, rather than always producing a Boolean. A common inspection guard:

```lua
return object and object:IsValid() and not object:HasAnyFlags(reject)
```

avoids invoking methods if `object` is nil/false. It returns nil for a nil argument, so `canRead` is a truthiness predicate rather than a strictly Boolean-returning function. The wrapper's validity and object flags are separate checks.

`FindAllOf(query) or {}` supplies a fallback for nil/false. It is not exactly JavaScript `??`, because false also takes the fallback. An empty Lua table is truthy; this is why the animal-query fallback separately checks `#animals == 0`. Likewise `not bestDistance` remains false when the best squared distance is 0, preserving a valid zero-distance match. Relevant evaluation logic is in the [pinned Lua VM](https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/deps/first/LuaRaw/src/lvm.c).

## Multiple values and pcall

`player, world = pawn, pc:GetWorld()` assigns two evaluated values to two locals. Lua multiple returns are not a tuple object or array that gets destructured.

`pcall(f)` invokes `f` under Lua's protected-call mechanism and returns:

| Outcome | Values |
| --- | --- |
| Normal return | `true` followed by the function's return values |
| Lua error | `false` followed by the error value, which need not be a string |

Thus `local ok, err = pcall(function() … end)` usually gets `true, nil` when a callback returns nothing. The variable named `err` is not intrinsically an error slot. Additional values are discarded if there are fewer assignment targets.

Conceptual C# translation:

```csharp
(bool ok, object? value) TryCall(Action action)
{
    try { action(); return (true, null); }
    catch (Exception error) { return (false, error); }
}
```

This explains the result shape, not native-crash protection. In Lua, `tostring(err)` makes an error value printable. Use `pcall(inspectAnimals)` or `pcall(function() inspectAnimals() end)`; `pcall(inspectAnimals())` would evaluate `inspectAnimals` before entering the protected call. See [pcall](https://lua.org/manual/5.4/manual.html#pdf-pcall) and its [pinned implementation](https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/deps/first/LuaRaw/src/lbaselib.c).

The outer scheduling `pcall` can catch a failure to queue work. It cannot catch an error that happens later inside the queued callback. That is why the standalone example has another `pcall(inspectAnimals)` inside its queued callback. A larger scanner could additionally protect each candidate. No protected call can safely recover every C++ access violation or process crash.

## Colon versus dot

`object:IsValid()` is Lua method-call syntax: conceptually `object.IsValid(object)`, with the receiver passed as the first argument. With a plain Lua receiver, `object.IsValid()` omits that argument. UE4SS native bindings expect the receiver too; a wrong call shape can produce an overload/userdata error.

`pc:GetPropertyValue("Pawn")` uses a method. `position.X` reads a field. `math.sqrt(bestDistance)` calls a function stored in a library table without inserting `math` as an argument. None of these punctuation choices tells you by itself whether the target is Lua code or C++: consult the [provenance table](../reference/provenance.md).

C# readers can think of a native extension-method-like explicit receiver, but this is a syntax comparison, not a CLR implementation. For an expression receiver, colon syntax also evaluates that receiver once; do not literally duplicate a side-effecting expression when expanding it. The [pinned parser's method-call handling](https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/deps/first/LuaRaw/src/lparser.c) implements the extra receiver.

## Userdata and logging mistakes

`animal` is normally a **userdata wrapper** created by UE4SS. It is not an ordinary table or a copy of the animal's state. Dot/colon access may enter C++ and Unreal reflection. Keeping a Lua reference does not grant ownership of the native object's lifetime. [Wrapper model](../concepts/object-model.md#userdata-is-a-native-boundary)

`GetPropertyValue("Controller")` resolves a reflected property, not a JavaScript accessor generated from a TypeScript interface. Two wrappers may compare equal because UE4SS compares their underlying UObject pointers. Do not equate that with wrapper-object identity or comparing their printed names.

`print` is a familiar Lua-library name, but UE4SS replaces it with its output implementation. The local `log` helper adds the prefix and newline; `string.format` handles `%s`, `%d` and `%.1f`. Expect the loader log, not a browser developer console. [Detailed provenance](../reference/lua.md#lua-library-surface)
