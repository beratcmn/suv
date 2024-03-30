import typer
import json
from pathlib import Path

import cli.set
import cli.show
import cli.create

CONFIG_FILE = Path.home() / ".suv.json"
DEFAULT_VENV_PATH = Path.home() / "suv-venvs"

config = {"venv_path": str(DEFAULT_VENV_PATH), "shell": "git bash"}

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


def check_missing_venv_path():
    if not VENV_PATH.exists():
        typer.echo(f"Creating {VENV_PATH}...")
        VENV_PATH.mkdir(parents=True)


@app.command()
def create(name: str = ""):
    """Create a new virtual environment.

    Args:
        name (str): The name of the virtual environment.
    """

    if name == "":
        name = typer.prompt("Enter the name of the virtual environment")

    typer.echo(f"Creating virtual environment {name}...")
    cli.create.venv(name=name)


if __name__ == "__main__":
    check_missing_venv_path()
    app()
