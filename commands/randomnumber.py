from rich.console import Console
import random

console = Console()

def randomnumber(args):
    number = random.randint(1, 100)
    console.print(f"[bold blue]Random Number: {number}[/bold blue]")

def register(register_command):
    register_command(
        name="randomnumber",
        func=randomnumber,
        description="Generate a random number between 1 and 100.",
        devmode=False
    )