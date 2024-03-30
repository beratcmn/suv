import typer
from pathlib import Path
import json
import os
import cli.activate

CONFIG_FILE = Path.home() / ".suv.json"


def venv(name: str):
    with open(CONFIG_FILE, "r", encoding="UTF-8") as f:
        config = json.load(f)

    path = config["venv_path"]

    venv_path = Path(path) / name
    os.system(f"python -m uv venv {venv_path}")

    activate_prompt = typer.confirm(
        "Do you want to activate the new virtual environment?", default=True
    )

    if activate_prompt:
        cli.activate.activate(venv_path)
