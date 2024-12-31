from rich.console import Console
import os

console = Console()

def devinfo(args):
    console.print("[bold yellow]This is developer information![/bold yellow]")
    os.system('tree')

def register(register_command):
    register_command(
        name="devinfo",
        func=devinfo,
        description="Show developer-specific info.",
        devmode=True
    )
