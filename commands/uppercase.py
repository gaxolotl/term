from rich.console import Console

console = Console()

def uppercase(args):
    message = ' '.join(args).upper()
    console.print(f"[bold yellow]{message}[/bold yellow]")

def register(register_command):
    register_command(
        name="uppercase",
        func=uppercase,
        description="Convert a message to uppercase.",
        devmode=False
    )