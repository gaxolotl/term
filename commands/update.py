import os
import json
from datetime import datetime
from rich.console import Console

console = Console()
UPDATE_FILE = "updates.json"  # JSON file to store update information

def load_updates():
    """Load existing updates from the JSON file or return an empty list if the file doesn't exist."""
    if os.path.exists(UPDATE_FILE):
        with open(UPDATE_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []  # Return empty if the file is corrupted
    return []

def save_updates(updates):
    """Save updates back to the JSON file."""
    with open(UPDATE_FILE, "w") as f:
        json.dump(updates, f, indent=4)  # Pretty formatting

def update(args):
    """Save an update message with a timestamp to the JSON file."""
    if not args:
        console.print("[bold red]Error:[/bold red] No update message provided.")
        return

    update_message = " ".join(args)  # Convert list to a single string
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current timestamp

    # Load existing updates, add new one, and save
    updates = load_updates()
    updates.append({"timestamp": timestamp, "message": update_message})
    save_updates(updates)

    console.print(f"[bold green]Update saved:[/bold green] {update_message}")

def register(register_command):
    register_command(
        name="update",
        func=update,
        description="Save update information to a JSON file.",
        devmode=False
    )
