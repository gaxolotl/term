from rich.console import Console

console = Console()

def reverse(args):
    reversed_message = ' '.join(args)[::-1]
    console.print(f"[bold yellow]Reversed: {reversed_message}[/bold yellow]")

def register(register_command):
    register_command(
        name="reverse",
        func=reverse,
        description="Reverse the provided message.",
        devmode=False
    )