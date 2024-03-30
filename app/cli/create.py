import typer
from pathlib import Path
import json
import os

from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Key


CONFIG_FILE = Path.home() / ".suv.json"

keyboard = KeyboardController()


def venv(name: str):
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
        activation_path = str(venv_path / "Scripts/activate").replace("\\", "/")
        keyboard.type(f"source {activation_path}")
        keyboard.press(Key.enter)
