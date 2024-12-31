from rich.console import Console
import os

console = Console()

def listdir(args):
    console.print("[bold blue]Listing directory contents:[/bold blue]")
    os.system('ls')

def register(register_command):
    register_command(
        name="listdir",
        func=listdir,
        description="List contents of the current directory.",
        devmode=False
    )