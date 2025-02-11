from rich.console import Console
import os

console = Console()

def mkdir(args):
    if not args:
        console.print("[bold red]Error:[/bold red] Please provide a directory name.")
        return
    dir_name = args[0]  # Use the first argument directly
    try:
        os.makedirs(dir_name, exist_ok=True)
        console.print(f"[bold green]Directory created:[/bold green] {dir_name}")
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

def touch(args):
    if not args:
        console.print("[bold red]Error:[/bold red] Please provide a file name.")
        return
    file_name = " ".join(args)  # Join args to handle multi-word file names
    try:
        with open(file_name, "a"):
            os.utime(file_name, None)
        console.print(f"[bold green]File created:[/bold green] {file_name}")
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

def delete(args):
    if not args:
        console.print("[bold red]Error:[/bold red] Please provide a file name.")
        return
    file_name = " ".join(args)  # Join args for multi-word file names
    try:
        os.remove(file_name)
        console.print(f"[bold green]File deleted:[/bold green] {file_name}")
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

def listfiles(args):
    dir_path = args[0] if args else "."
    try:
        files = os.listdir(dir_path)
        if not files:
            console.print("[bold yellow]No files found.[/bold yellow]")
        else:
            console.print(f"[bold green]Files in {dir_path}:[/bold green]")
            for file in files:
                console.print(f" - {file}")
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

def search(args):
    if len(args) < 2:
        console.print("[bold red]Error:[/bold red] Please provide a directory and a file name.")
        return
    dir_path, file_name = args
    try:
        for root, _, files in os.walk(dir_path):
            if file_name in files:
                console.print(f"[bold green]File found:[/bold green] {os.path.join(root, file_name)}")
                return
        console.print("[bold yellow]File not found.[/bold yellow]")
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

def register(register_command):
    register_command(name="mkdir", func=mkdir, description="Create a new directory.", devmode=False)
    register_command(name="touch", func=touch, description="Create an empty file.", devmode=False)
    register_command(name="delete", func=delete, description="Delete a specified file.", devmode=False)
    register_command(name="listfiles", func=listfiles, description="List all files in a directory.", devmode=False)
    register_command(name="search", func=search, description="Find a file in a directory.", devmode=False)
