import typer
from pathlib import Path
import json
import os

CONFIG_FILE = Path.home() / ".suv.json"

app = typer.Typer()


@app.command()
def venv(name: str):
    """Create a new virtual environment.

    Args:
        name (str): The name of the virtual environment.
    """

    typer.echo(f"Creating virtual environment {name}...")

    with open(CONFIG_FILE, "r", encoding="UTF-8") as f:
        config = json.load(f)

    path = config["venv_path"]

    venv_path = Path(path) / name
    os.system(f"python -m uv venv {venv_path}")

    activate = typer.confirm(
        "Do you want to activate the new virtual environment?", default=True
    )

    if activate:
        typer.echo(f"Activating virtual environment {name}...")
        activate_script = venv_path / "Scripts/activate_this.py"
        with open(activate_script) as file_:
            exec(file_.read(), dict(__file__=activate_script))


if __name__ == "__main__":
    app()
