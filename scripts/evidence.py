"""Render evidence metadata as ordinary Markdown. SPDX-License-Identifier: MIT"""


def on_page_markdown(markdown, page, config, files):
    meta = page.meta
    status = meta.get("evidence_status", "Inferred")
    parts = [f"**Evidence: {status}**", f"Source review: {meta.get('reviewed', 'not recorded')}"]
    if "game_build" in meta:
        parts.append(f"Game build {meta['game_build']} (review context)")
        parts.append(f"UE4SS {meta.get('ue4ss_version', 'not recorded')}")
        parts.append("Runtime verified" if meta.get("runtime_verified") is True else "**Not runtime verified**")
    banner = "> " + " · ".join(parts) + "\n\n"
    lines = markdown.splitlines(keepends=True)
    for index, line in enumerate(lines):
        if line.startswith("# "):
            lines.insert(index + 1, "\n" + banner)
            return "".join(lines)
    return banner + markdown
