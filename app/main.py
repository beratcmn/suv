import typer
import json
from pathlib import Path

import cli.set
import cli.show
import cli.create

CONFIG_FILE = Path.home() / ".suv.json"
DEFAULT_VENV_PATH = Path.home() / "suv-venvs"

config = {"version": "0.0.1", "venv_path": str(DEFAULT_VENV_PATH), "shell": "git bash"}

if CONFIG_FILE.exists():
    with open(CONFIG_FILE, encoding="UTF-8") as f:
        config = json.load(f)
else:
    typer.echo(f"Creating {CONFIG_FILE}...")
    with open(CONFIG_FILE, "w", encoding="UTF-8") as f:
        json.dump(config, f, ensure_ascii=False)

VENV_PATH = Path(
    config["venv_path"] if config["venv_path"] != "" else DEFAULT_VENV_PATH
)

app = typer.Typer()
app.add_typer(cli.set.app, name="set")
app.add_typer(cli.show.app, name="show")
app.add_typer(cli.create.app, name="create")


def check_missing_venv_path():
    if not VENV_PATH.exists():
        typer.echo(f"Creating {VENV_PATH}...")
        VENV_PATH.mkdir(parents=True)


if __name__ == "__main__":
    check_missing_venv_path()
    app()
