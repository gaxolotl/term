import os
import sys
import socket
import shutil
import importlib
from importlib import import_module
from rich.console import Console
from rich.panel import Panel

console = Console()
width = shutil.get_terminal_size().columns

COMMANDS = {}
DEV_COMMANDS = {}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_welcome():
    console.print(Panel("Welcome to Term", style="bold green", expand=True))
    console.print("Enter devmode: [bold blue]devmode /on[/bold blue]")
    console.print("Type [bold yellow]'help'[/bold yellow] for commands")
    console.print("[italic]Nerd font is recommended[/italic]")
    console.print("=" * width)

def print_help():
    console.print(Panel("[bold green]Available Commands[/bold green]", expand=True))
    for name, details in COMMANDS.items():
        console.print(f"[bold blue]{name}[/bold blue] - {details['description']}")
    console.print("=" * 30)

def print_devhelp():
    console.print(Panel("[bold green]Dev Mode Commands[/bold green]", expand=True))
    for name, details in DEV_COMMANDS.items():
        console.print(f"[bold blue]{name}[/bold blue] - {details['description']}")
    console.print("=" * 30)

def register_command(name, func, description, devmode=False):
    command_dict = DEV_COMMANDS if devmode else COMMANDS
    command_dict[name] = {
        "func": func,
        "description": description
    }

def load_commands():
    commands_dir = os.path.join(os.path.dirname(__file__), "commands")
    if not os.path.exists(commands_dir):
        os.makedirs(commands_dir)
    sys.path.insert(0, commands_dir)

    for filename in os.listdir(commands_dir):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3]
            module = import_module(module_name)
            importlib.reload(module)  # Ensure fresh reload
            if hasattr(module, "register"):
                module.register(register_command)
            else:
                console.print(f"[bold yellow]Warning: {filename} does not have a register function.[/bold yellow]")

def main():
    in_devmode = False

    load_commands()
    print_welcome()

    while True:
        username = os.getenv("USERNAME") or os.getenv("USER") or "unknown"
        hostname = socket.gethostname()
        prompt = f" {username}@{hostname} " if in_devmode else f"{username}@{hostname} "
        
        user_input = input(prompt).strip()

        if not user_input:  # Fix for empty input crash
            continue

        if user_input == "exit":
            console.print("[bold red]Exiting...[/bold red]")
            break
        elif user_input == "help":
            print_help() if not in_devmode else print_devhelp()
        elif user_input == "devmode /on" and not in_devmode:
            in_devmode = True
            clear()
            console.print(Panel("[bold green]Dev Mode ON[/bold green]", expand=True))
            console.print("[bold blue]Now you can use developer commands[/bold blue]")
            console.print("[italic]Type 'help' to see devmode commands[/italic]")
        elif user_input == "devmode /off" and in_devmode:
            in_devmode = False
            clear()
            console.print(Panel("[bold green]Dev Mode OFF[/bold green]", expand=True))
            console.print("[bold blue]Now in normal mode[/bold blue]")
        else:
            command_dict = DEV_COMMANDS if in_devmode else COMMANDS
            parts = user_input.split()
            command = parts[0]
            args = parts[1:]

            if command in command_dict:
                try:
                    command_dict[command]["func"](args)  # ✅ Corrected argument handling
                except Exception as e:
                    console.print(f"[bold red]Error: {e}[/bold red]")
            else:
                console.print(f"[bold red]Unknown command: {user_input}[/bold red]")

if __name__ == "__main__":
    main()
