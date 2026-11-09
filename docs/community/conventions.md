---
title: "Documentation conventions"
evidence_status: "Documented"
reviewed: "2026-11-09"
---

# Keep the reference easy to maintain

Use Markdown, short descriptive headings, relative links to other pages and pinned upstream sources. Put every public page in `mkdocs.yml` navigation. Every page has a title, evidence status and reviewed date in YAML front matter. A small MkDocs hook renders that metadata below the heading; edit the YAML rather than duplicating badges by hand.

## Code and terminology

Use fenced code labels `lua`, `typescript`, `csharp`, `yaml` and `json` so readers can see the language boundary. Non-Lua translations are conceptual unless explicitly documented as runnable.

```typescript
// Conceptual translation: a named field read is not a TypeScript type guarantee.
const controller = readReflectedProperty(animal, "Controller");
```

```csharp
// Conceptual translation: wrapper identity is native-handle identity.
bool sameObject = NativeHandleEquals(firstWrapper, secondWrapper);
```

```json
{
  "operation": "read inherited Controller property",
  "verification_status": "Inferred",
  "runtime_verified": false
}
```

Spell out which API belongs to Lua, a UE4SS binding, an engine interface or the game. Separate a class definition from an instance and inheritance from a Pawn/Controller relationship. Userdata is not a plain Lua record.

Examples must be original. Keep published Lua source under `examples/` and include it as text with the snippets extension; the site build must not execute it. Keep personal environment details out of prose, examples, metadata and build output.

## Diagrams

Use fenced `mermaid` blocks for small diagrams beside their textual explanation. The site uses [Material's native Mermaid integration](https://squidfunk.github.io/mkdocs-material/reference/diagrams/), including its theme and navigation support. GitHub can also display these blocks when reviewing Markdown.

Keep labels short, describe arrow meanings, and distinguish inheritance from references, ownership and control flow. Do not use color as the only evidence indicator. Label historical and inferred game-specific relationships directly in the diagram and explain that they are not runtime verified. Update a flow diagram alongside any source change; a successful site build does not prove the depicted game behavior.

Mermaid renders in the reader's browser. Keep surrounding prose useful if rendering is unavailable. Check diagrams in light/dark themes and at narrow widths when browser preview is available; a strict MkDocs build checks the Markdown integration, not browser layout or Mermaid execution.

## Expanding the site

Add a system page only when there is meaningful sourced content. Audio is intentionally absent until there are useful supported observations. New claims should include a small evidence record and a curated API entry, not an SDK dump.

A separately maintained framework could later add a versioned API-reference section, real public symbols, UE4SS integration notes, game adapters, compatibility records and examples. Add that navigation only when those APIs exist. Design proposals must be labeled **proposal** and kept distinct from existing functionality. This project currently implements no framework.

## Toolchain maintenance

Python requirements and GitHub Actions are pinned. Review dependency updates through pull requests and rerun source validation, the strict MkDocs build and generated-site validation. External links may change even when the local build passes.

Material for MkDocs currently announces end of support on May 5, 2027. Keep prose and metadata portable; evaluate the documentation toolchain before that date rather than mixing a frontend rewrite into ordinary content changes. [Upstream notice](https://pypi.org/project/mkdocs-material/)
