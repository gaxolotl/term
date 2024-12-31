from rich.console import Console
import socket

console = Console()

def hostname(args):
    host = socket.gethostname()
    console.print(f"[bold cyan]Hostname: {host}[/bold cyan]")

def register(register_command):
    register_command(
        name="hostname",
        func=hostname,
        description="Show the system hostname.",
        devmode=False
    )