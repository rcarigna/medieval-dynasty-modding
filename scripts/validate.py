"""Static publication checks; never imports or executes Lua or game tooling.
SPDX-License-Identifier: MIT
"""
from __future__ import annotations

import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml
from pygments.lexers import get_lexer_by_name

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
STATUSES = {"Documented", "Historical evidence", "Inferred", "Runtime verified"}
SKIP = {".git", ".venv", "site", "__pycache__", ".cache", ".wheels"}
BINARY = {".dll", ".exe", ".pdb", ".pak", ".sig", ".uasset", ".uexp", ".sav", ".save"}
LEAKS = [
    re.compile(r"[A-Za-z]:[/\\](?:Users|Program Files|Steam)[/\\ ]", re.I),
    re.compile(r"/(?:home|Users)/[A-Za-z0-9_.-]+/"),
    re.compile(r"https://github\.com/rcarigna/(?!medieval-dynasty-modding(?:/|$|[^A-Za-z0-9_.-]))"),
    re.compile(r"(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,})"),
]
errors: list[str] = []


def problem(message: str) -> None:
    errors.append(message)


def scan_text(label: str, text: str) -> None:
    for pattern in LEAKS:
        if pattern.search(text):
            problem(f"{label}: possible private reference, personal path or credential")


def source_files():
    for path in ROOT.rglob("*"):
        if path.is_file() and not set(path.relative_to(ROOT).parts) & SKIP:
            yield path


def nav_paths(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from nav_paths(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from nav_paths(item)


class SiteConfigLoader(yaml.SafeLoader):
    """Read the one SuperFences callable tag as inert text; never import it."""


SiteConfigLoader.add_constructor(
    "tag:yaml.org,2002:python/name:pymdownx.superfences.fence_code_format",
    lambda loader, node: loader.construct_scalar(node),
)


def site_config():
    return yaml.load(
        (ROOT / "mkdocs.yml").read_text(encoding="utf-8"),
        Loader=SiteConfigLoader,
    )


def source_checks() -> int:
    config = site_config()
    pages = {str(path.relative_to(DOCS)).replace("\\", "/") for path in DOCS.rglob("*.md")}
    nav = list(nav_paths(config["nav"]))
    if len(nav) != len(set(nav)) or set(nav) != pages:
        problem(f"Navigation mismatch: omitted={pages-set(nav)}, missing={set(nav)-pages}")
    for path in source_files():
        relative = path.relative_to(ROOT).as_posix()
        if path.suffix.lower() in BINARY or "\0" in path.read_bytes().decode("utf-8", errors="replace"):
            problem(f"{relative}: binary/game artifact is not allowed")
            continue
        scan_text(relative, path.read_text(encoding="utf-8"))
    for name in pages:
        text = (DOCS / name).read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        if not match:
            problem(f"{name}: missing YAML front matter")
            continue
        meta = yaml.safe_load(match.group(1))
        if not isinstance(meta.get("title"), str) or meta.get("evidence_status") not in STATUSES:
            problem(f"{name}: missing title or invalid evidence classification")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(meta.get("reviewed", ""))):
            problem(f"{name}: missing reviewed date")
        game_specific = name.startswith(("systems/", "reference/game-", "examples/animal-"))
        if game_specific or "game_build" in meta:
            for key in ("game_build", "ue4ss_version", "runtime_verified"):
                if key not in meta:
                    problem(f"{name}: missing {key}")
            if not isinstance(meta.get("runtime_verified"), bool):
                problem(f"{name}: runtime_verified must be a Boolean")
        if meta.get("evidence_status") == "Runtime verified" or meta.get("runtime_verified") is True:
            record = meta.get("evidence_record")
            if not isinstance(record, str):
                problem(f"{name}: runtime claim needs evidence_record")
            else:
                target = (DOCS / record).resolve()
                if not target.is_relative_to(DOCS.resolve()) or not target.is_file():
                    problem(f"{name}: evidence_record must be a real public documentation file")
    example = (ROOT / "examples/animal-inspection/main.lua").read_text(encoding="utf-8")
    if re.search(r"\b(?:SetPropertyValue|SpawnActor|RegisterHook|Possess|SaveGameToSlot|StaticConstructObject)\s*\(", example):
        problem("Example contains a mutation/gameplay-hook API; manual review is required")
    requirements = (ROOT / "requirements.txt").read_text(encoding="utf-8").splitlines()
    for line in requirements:
        if line and not line.startswith("#") and not re.fullmatch(r"[A-Za-z0-9_.-]+==[^\s]+", line):
            problem("Every installed Python dependency must have an exact version pin")
    workflow = yaml.safe_load((ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8"))
    if workflow.get("permissions") != {"contents": "read"}:
        problem("Workflow top-level permissions must be contents:read")
    for job in workflow["jobs"].values():
        for step in job.get("steps", []):
            action = step.get("uses")
            if action and not re.fullmatch(r"actions/[A-Za-z0-9-]+@[a-f0-9]{40}", action):
                problem(f"Unpinned action: {action}")
    for language in ("lua", "typescript", "csharp", "yaml", "json"):
        get_lexer_by_name(language)
    print(f"Source: {len(pages)} pages; navigation, metadata, source boundary and lexer checks completed")
    return len(pages)


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.targets = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        for key in ("href", "src"):
            if key in attrs:
                self.targets.append(attrs[key])


def built_checks(page_count: int) -> None:
    site = (ROOT / "site").resolve()
    index = site / "search/search_index.json"
    if not index.is_file():
        problem("Missing search index")
        return
    search = json.loads(index.read_text(encoding="utf-8"))
    if len(search.get("docs", [])) < page_count:
        problem("Search index does not contain all pages")
    parsed = {}
    for path in site.rglob("*.html"):
        reader = Links()
        text = path.read_text(encoding="utf-8")
        reader.feed(text)
        parsed[path.resolve()] = reader
        scan_text(path.relative_to(site).as_posix(), text)
    for path, reader in parsed.items():
        for raw in reader.targets:
            link = urlsplit(raw)
            if link.scheme or link.netloc or not link.path and not link.fragment:
                continue
            if link.path.startswith("/"):
                # The project site has a fixed Pages subpath.
                prefix = "/medieval-dynasty-modding/"
                if not link.path.startswith(prefix):
                    problem(f"{path.name}: unexpected absolute link {raw}")
                    continue
                target = site / unquote(link.path[len(prefix):])
            else:
                target = path.parent / unquote(link.path)
            if target.is_dir():
                target /= "index.html"
            target = target.resolve()
            if not target.is_relative_to(site) or not target.is_file():
                problem(f"{path.relative_to(site)}: missing generated target {raw}")
            elif link.fragment and target in parsed and unquote(link.fragment) not in parsed[target].ids:
                problem(f"{path.relative_to(site)}: missing generated anchor {raw}")
    scan_text("search/search_index.json", index.read_text(encoding="utf-8"))
    config = site_config()
    palettes = {p["scheme"] for p in config["theme"]["palette"]}
    if palettes != {"default", "slate"}:
        problem("Both light and dark palettes must be configured")
    homepage = (site / "index.html").read_text(encoding="utf-8")
    if "data-md-component=\"search\"" not in homepage or "__palette" not in homepage:
        problem("Rendered search/palette UI was not found")
    if "github.com/rcarigna/medieval-dynasty-modding/edit/main/docs/" not in homepage:
        problem("Rendered source-edit link was not found")
    print(f"Built site: {len(parsed)} HTML pages; local links/anchors, privacy, search, themes and edit links checked")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--built", action="store_true")
    args = parser.parse_args()
    count = source_checks()
    if args.built:
        built_checks(count)
    if errors:
        for message in errors:
            print("ERROR:", message)
        return 1
    print("Validation passed. No Lua, loader or game code was executed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
