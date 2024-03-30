import typer
from pathlib import Path
import json

CONFIG_FILE = Path.home() / ".suv.json"
DEFAULT_VENV_PATH = Path.home() / "suv-venvs"

app = typer.Typer()


@app.command()
def global_venv_path():
    """Show the global path for the virtual environments."""
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r", encoding="UTF-8") as f:
            config = json.load(f)
            typer.echo(f"Global virtual environment path: {config['venv_path']}")
    else:
        typer.echo(f"Global virtual environment path: {DEFAULT_VENV_PATH}")


@app.command()
def venvs():
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

    typer.echo("Virtual environments:")
    for venv in venv_path.iterdir():
        if venv.is_dir():
            typer.echo(f" - {venv.name}")


if __name__ == "__main__":
    app()
