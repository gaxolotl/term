from rich.console import Console
import random

console = Console()

def randomnumber(args):
    try:
        maxi = int(console.input("[bold yellow]Maximum[/bold yellow] >> "))
        mini = int(console.input("[bold yellow]Minimum[/bold yellow] >> "))
        if mini >= maxi:
            print("Minimum must not be higher or equal!")
            return
        number = random.randint(mini, maxi)
        console.print(f"[bold blue]Random Number: {number}[/bold blue]")
    except ValueError:
        print("Must be a number!")

def register(register_command):
    register_command(
        name="randomnumber",
        func=randomnumber,
        description="Generate a random number between 1 and 100.",
        devmode=False
    )