import json
import os
from rich.console import Console

console = Console()
UPDATE_FILE = "updates.json"

def view_updates(args):
    """Display stored updates."""
    if not os.path.exists(UPDATE_FILE):
        console.print("[bold yellow]No updates found.[/bold yellow]")
        return

    with open(UPDATE_FILE, "r") as f:
        try:
            updates = json.load(f)
        except json.JSONDecodeError:
            console.print("[bold red]Error:[/bold red] Corrupted updates file.")
            return

    if not updates:
        console.print("[bold yellow]No updates recorded yet.[/bold yellow]")
        return

    console.print("[[bold yellow]UTC+2[/bold yellow]] [bold blue]Update Log:[/bold blue]")
    for update in updates:
        console.print(f"[{update['timestamp']}] {update['message']}")

def register(register_command):
    register_command(
        name="vupdate",
        func=view_updates,
        description="View saved update logs.",
        devmode=False
    )
