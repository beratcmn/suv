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


if __name__ == "__main__":
    app()
