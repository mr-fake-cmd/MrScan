import json
import os

from rich.console import Console
from rich.panel import Panel

console = Console()

CONFIG_FILE = "config.json"

DEFAULT_CONFIG = {
    "theme": "default",
    "timeout": 5,
    "auto_save": True,
}


def save_config(cfg):
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=4)


def load_config():
    if not os.path.exists(CONFIG_FILE):
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG.copy()

    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        for key, value in DEFAULT_CONFIG.items():
            data.setdefault(key, value)

        return data

    except (json.JSONDecodeError, OSError):
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG.copy()


def settings_dashboard():

    cfg = load_config()

    console.print(
        Panel.fit(
            f"""1. Theme      : {cfg['theme']}
2. Timeout    : {cfg['timeout']} sec
3. Auto Save  : {cfg['auto_save']}

0. Back""",
            title="Settings",
        )
    )

    choice = console.input("\nSelect > ")

    if choice == "1":
        cfg["theme"] = "dark" if cfg["theme"] == "default" else "default"

    elif choice == "2":
        value = console.input("Timeout (seconds): ")
        if value.isdigit():
            cfg["timeout"] = int(value)

    elif choice == "3":
        cfg["auto_save"] = not cfg["auto_save"]

    save_config(cfg)