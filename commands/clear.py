from rich.console import Console
import os

console = Console()

def clear(args):
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print("[bold cyan]Console cleared![/bold cyan]")

def register(register_command):
    register_command(
        name="clear",
        func=clear,
        description="Clear the console.",
        devmode=False
    )