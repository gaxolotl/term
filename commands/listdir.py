from rich.console import Console
import os

console = Console()

def listdir(args):
    path = args[0] if args else "."  # Default to current directory if no path is given

    try:
        files = os.listdir(path)  # Get list of files in the directory
        if not files:
            console.print("[bold yellow]Directory is empty.[/bold yellow]")
        else:
            console.print("[bold blue]Listing directory contents:[/bold blue]")
            for file in files:
                console.print(f"  - {file}")  # Print each file/folder
    except FileNotFoundError:
        console.print(f"[bold red]Error:[/bold red] Directory '{path}' not found.")
    except PermissionError:
        console.print(f"[bold red]Error:[/bold red] Permission denied for '{path}'.")

def register(register_command):
    register_command(
        name="listdir",
        func=listdir,
        description="List contents of the current directory or specified path.",
        devmode=False
    )
