from rich.console import Console
import os
import time

console = Console()

def clear(args):
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print("[bold cyan]Console cleared![/bold cyan]")
    time.sleep(0.3)
    os.system('cls' if os.name == 'nt' else 'clear')

def register(register_command):
    register_command(
        name="clear",
        func=clear,
        description="Clear the console.",
        devmode=False
    )