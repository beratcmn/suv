import typer
import json
from pathlib import Path
from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Key

CONFIG_FILE = Path.home() / ".suv.json"

app = typer.Typer()
keyboard = KeyboardController()


@app.command()
def activate(name: str):
    typer.echo(f"Activating virtual environment {name}...")
    with open(CONFIG_FILE, "r", encoding="UTF-8") as f:
        config = json.load(f)
    venv_path = Path(config["venv_path"]) / name
    activation_path = str(venv_path / "Scripts/activate").replace("\\", "/")
    keyboard.type(f"source {activation_path}")
    keyboard.press(Key.enter)


if __name__ == "__main__":
    app()
