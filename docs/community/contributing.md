---
title: "Contributing"
evidence_status: "Documented"
reviewed: "2026-11-02"
---

# Improve one useful explanation or observation

Ordinary Markdown pull requests are the normal contribution path. Small fixes, better examples, clarified failure modes and carefully versioned observations are welcome.

## Before opening a pull request

1. Confirm your material is original or that you have permission to contribute it under this project's licenses.
2. Read the [content policy](licensing.md) and [evidence standard](evidence.md).
3. For every game-specific claim, identify its source and verification classification.
4. Use authoritative upstream links rather than copying implementation code or documentation wholesale.
5. Keep examples small, independently understandable and read-only unless their mutation risks and rollback are explicitly reviewed.
6. Run the repository's validation and strict build commands.

Describe what the change teaches, what sources support it, and what remains unknown. Any runtime evidence must name the precise build/loader/context. If you did not run an example, say so.

## Rights and attribution

By submitting original prose you agree to contribute it under CC BY 4.0; by submitting original code, inline examples, scripts or configuration you agree to contribute them under MIT. You must have the rights to do so. Identify third-party material and its applicable terms; a source link is not permission to relicense copied content.

Do not submit proprietary implementations, extracted game content, binaries, generated SDK dumps, private saves or sensitive logs. When uncertain, propose an interface-name observation and a source link instead of an upload.

## Review responsibilities

Maintainers check abstraction-layer labels, version metadata, source quality, rights, internal links and example behavior. Automated checks cannot decide whether an interface was actually observed or whether a contributor owns their material.

Use [documentation conventions](conventions.md) for new pages and [compatibility reporting](reporting.md) for version failures.
