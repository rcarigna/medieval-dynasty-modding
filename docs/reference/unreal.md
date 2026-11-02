---
title: "Unreal Engine interfaces"
evidence_status: "Historical evidence"
reviewed: "2026-11-02"
game_build: "25776186"
ue4ss_version: "3.0.1-1196-g236adf26"
runtime_verified: false
---

# Engine concepts accessed through UE4SS

These are standard Unreal classes/members, not game-specific functions invented by this project. The expected reflected spellings are corroborated by historical declarations. Successful dispatch/marshaling in a selected Medieval Dynasty build remains unverified.

## Reflected engine members

`GetPropertyValue` supplies access; it does not define the following properties. The engine member names are not invented Medieval Dynasty APIs.

| Exact expression / name | Origin / layers | Type | Inspection purpose | Availability | Reference | Caveats |
| --- | --- | --- | --- | --- | --- | --- |
| `pc:IsLocalController()` | Unreal AController UFunction → UE4SS reflected dispatch | Engine method | Filter controller search to a local player anchor | Historical evidence; standard engine concept documented | [Historical declaration][local-controller], [framework][framework] | Not a UE4SS-specific method, and not a single-player/authority predicate |
| `GetPropertyValue("Pawn")`; property `"Pawn"` | Unreal AController property → UE4SS named getter | Reflected UObject-reference property | Read player's pawn and animal-controller backlink | Historical evidence + Documented access mechanism | [Controller field][pawn-field], [getter docs][uobject] | Inherited by PlayerController; historical SDK marks field native-private. It is not the literal class query APawn |
| `GetPropertyValue("Controller")`; property `"Controller"` | Unreal APawn property → UE4SS named getter | Reflected UObject-reference property | Read animal's current controller and recheck it | Historical evidence + Documented access mechanism | [Pawn field][controller-field], [getter docs][uobject] | Separate from historical game AIControllerRef; no automatic proof of AI subtype/activity |
| `player:K2_GetActorLocation()`; `animal:K2_GetActorLocation()` | Unreal AActor UFunction → UE4SS reflected dispatch | Engine method returning FVector | Obtain player/animal world locations | Historical evidence + Documented dispatch mechanism | [Historical declaration][location], [binding docs][uobject] | Exact reflected name matters; SDK's GetActorLocation convenience wrapper is not the Lua call used |
| `position.X`; `origin.X` | Unreal FVector component → UE4SS struct member access | Numeric struct field | X contribution to squared distance | Historical evidence for layout; Inferred for successful current marshaling | [Vector declaration][vector], [struct wrapper source][struct] | Case-sensitive; no colon, no UObject lifetime check on the numeric field |
| `position.Y`; `origin.Y` | Unreal FVector component → UE4SS struct member access | Numeric struct field | Y contribution | Historical evidence; Inferred for current marshaling | [Vector declaration][vector], [struct wrapper source][struct] | Same marshaling dependency |
| `position.Z`; `origin.Z` | Unreal FVector component → UE4SS struct member access | Numeric struct field | Z contribution | Historical evidence; Inferred for current marshaling | [Vector declaration][vector], [struct wrapper source][struct] | Includes vertical separation; not horizontal-only/path distance |


## Implicit native types and local names

| Type/context, not a literal class query | Origin | Evidence | Role / caveat |
| --- | --- | --- | --- |
| UObject and UClass | Unreal concepts exposed through UE4SS wrappers | Documented: [wrapper docs][uobject] | Instance versus class metadata; neither is a plain Lua record |
| UWorld | Unreal concept returned by wrapper GetWorld | Documented: [binding implementation][world-source] | Actual selected world is unobserved |
| AActor, APawn, ACharacter | Standard Unreal inheritance | Documented concepts, Historical evidence declarations: [Actor][actor-header], [Pawn][controller-field], [Character][character-class] | Historical AAnimalBase is a Character/Pawn/Actor; runtime applicability unverified |
| AController, APlayerController | Standard Unreal controller types | Documented concepts, Historical evidence: [Controller][pawn-field], [PlayerController][player-class] | The source does not require/check the animal controller to be an AIController |
| FVector | Unreal struct marshaled to Lua | Historical evidence [declaration][vector]; Documented [binding][struct] | X/Y/Z are struct-member reads, not properties on an animal |


## Binding versus engine member

`GetPropertyValue` belongs to the UE4SS wrapper. The `Pawn` field is declared on AController, and `Controller` on APawn. The exact reflected `K2_GetActorLocation` method is not the same name as a generated C++ SDK convenience helper.

The returned FVector's X/Y/Z fields are struct members, not UObject properties on the actor. Conventional centimeters explain a possible meters conversion; they do not calibrate a particular game's scale.

[Object model](../concepts/object-model.md) · [Game-specific classes](game-interfaces.md) · [Evidence labels](../community/evidence.md)


[uobject]: https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/docs/lua-api/classes/uobject.md
[world-source]: https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/UE4SS/include/LuaType/LuaUObject.hpp#L642
[struct]: https://github.com/UE4SS-RE/RE-UE4SS/blob/236adf2667832375877669faac4b78872b4736b0/UE4SS/include/LuaType/LuaUScriptStruct.hpp
[local-controller]: https://github.com/stulu08/Medieval-Dynasty-Mod-Loader/blob/ef78da996dc77a2372fed9eaeabb9210e5c38774/SDK/src/UE4/Engine/Controller.h#L78
[pawn-field]: https://github.com/stulu08/Medieval-Dynasty-Mod-Loader/blob/ef78da996dc77a2372fed9eaeabb9210e5c38774/SDK/src/UE4/Engine/Controller.h#L29
[controller-field]: https://github.com/stulu08/Medieval-Dynasty-Mod-Loader/blob/ef78da996dc77a2372fed9eaeabb9210e5c38774/SDK/src/UE4/Engine/Pawn.h#L81
[location]: https://github.com/stulu08/Medieval-Dynasty-Mod-Loader/blob/ef78da996dc77a2372fed9eaeabb9210e5c38774/SDK/src/UE4/Engine/Actor.h
[actor-header]: https://github.com/stulu08/Medieval-Dynasty-Mod-Loader/blob/ef78da996dc77a2372fed9eaeabb9210e5c38774/SDK/src/UE4/Engine/Actor.h
[vector]: https://github.com/stulu08/Medieval-Dynasty-Mod-Loader/blob/ef78da996dc77a2372fed9eaeabb9210e5c38774/SDK/src/UE4/Math/Vector.h
[player-class]: https://github.com/stulu08/Medieval-Dynasty-Mod-Loader/blob/ef78da996dc77a2372fed9eaeabb9210e5c38774/SDK/src/UE4/Engine/PlayerController.h
[character-class]: https://github.com/stulu08/Medieval-Dynasty-Mod-Loader/blob/ef78da996dc77a2372fed9eaeabb9210e5c38774/SDK/src/UE4/Engine/Character.h
[framework]: https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-framework-quick-reference?application_version=4.27
