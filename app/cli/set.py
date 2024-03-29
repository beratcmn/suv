import typer
from pathlib import Path
import json

CONFIG_FILE = Path.home() / ".suv.json"

app = typer.Typer()


@app.command()
def global_venv_path(path: str):
    """Set the global path for the virtual environments.

    Args:
        path (str): The path to the virtual environments.
    """
    with open(CONFIG_FILE, "r", encoding="UTF-8") as f:
        config = json.load(f)

    config["venv_path"] = path

    with open(CONFIG_FILE, "w", encoding="UTF-8") as f:
        json.dump(config, f, ensure_ascii=False)

    typer.echo(f"Global virtual environment path set to {path}.")


if __name__ == "__main__":
    app()
