from rich.console import Console

console = Console()

def uppercase(args):
    if not args:
        console.print("[bold red]Error:[/bold red] No message provided.")
        return
    
    message = " ".join(args).upper()  # Join list into a string and convert to uppercase
    console.print(f"[bold yellow]{message}[/bold yellow]")

def register(register_command):
    register_command(
        name="uppercase",
        func=uppercase,
        description="Convert a message to uppercase.",
        devmode=False
    )
