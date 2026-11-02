# Medieval Dynasty Modding

An **unofficial** community reference for developers learning Lua, UE4SS and Unreal Engine interfaces in Medieval Dynasty. Not affiliated with or endorsed by Render Cube, Toplitz Productions or Epic Games.

The project contains original documentation and original read-only examples. It distributes no game assets, game code, generated SDK dumps or tool DLLs.

- Documentation entry point: [docs/index.md](docs/index.md)
- Intended Pages address: https://rcarigna.github.io/medieval-dynasty-modding/
- [Contribute](CONTRIBUTING.md) · [Content and licensing policy](docs/community/licensing.md)
- [Publication setup](PUBLICATION.md)

The intended Pages address is a deployment target, not evidence of a completed deployment.

## Build locally

Use Python 3.13 in an isolated environment.

```sh
python -m venv .venv
# Activate .venv using your platform's standard activation command.
python -m pip install --only-binary=:all: -r requirements.txt
python scripts/validate.py
python -m mkdocs build --strict
python scripts/validate.py --built
```

The optional `python -m mkdocs serve` command starts a documentation preview only. No build or validation command imports or executes Lua examples.

Dependencies and Actions are pinned. For deliberate updates, edit requirements.in, install in a fresh environment and regenerate the complete requirements.txt lock; then run the same validation commands. Material for MkDocs announces end of support on May 5, 2027; see its [upstream notice](https://pypi.org/project/mkdocs-material/). Content stays in portable Markdown.

## Licensing

Original prose: [CC BY 4.0](LICENSE-DOCS.md). Original code, inline code examples, scripts and configuration: [MIT](LICENSE-CODE). Third-party material remains under its own terms and is linked rather than redistributed. See [NOTICE.md](NOTICE.md).

No Medieval Dynasty animal/controller relationship is claimed to be runtime verified merely because an upstream API is documented.
