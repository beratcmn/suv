import typer
import json
from pathlib import Path

import cli.set
import cli.show
import cli.create
import cli.activate

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
def list(echo: bool = True):
    """Lists all the virtual environments."""

    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r", encoding="UTF-8") as f:
            config = json.load(f)
            venv_path = Path(config["venv_path"])
    else:
        venv_path = DEFAULT_VENV_PATH

    if not venv_path.exists():
        typer.echo("No virtual environments found.")
        raise typer.Exit()

    venvs = []
    if echo:
        typer.echo("Virtual environments:")

    for venv in venv_path.iterdir():
        if venv.is_dir():
            venvs.append(venv.name)

            if echo:
                typer.echo(f" - {venv.name}")

    return venvs


@app.command()
def create(name: str):
    """Create a new virtual environment.

    Args:
        name (str): The name of the virtual environment.
    """

    if name == "":
        name = typer.prompt("Enter the name of the virtual environment")

    typer.echo(f"Creating virtual environment {name}...")
    cli.create.venv(name=name)


@app.command()
def activate(name: str):
    """Activate a virtual environment.

    Args:
        name (str): The name of the virtual environment.
    """
    venvs = list(echo=False)

    if name == "":
        name = typer.prompt("Enter the name of the virtual environment")

    if not venvs:
        typer.echo("No virtual environments found.")
        raise typer.Exit()

    if name not in venvs:
        typer.echo(f"Virtual environment {name} not found.")
        raise typer.Exit()
    cli.activate.activate(name=name)


if __name__ == "__main__":
    check_missing_venv_path()
    app()
