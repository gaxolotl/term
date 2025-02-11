from rich.console import Console

console = Console()

def reverse(args):
    if not args:
        console.print("[bold red]Error:[/bold red] No message provided.")
        return
    
    message = " ".join(args)  # Join words into a single string
    reversed_message = message[::-1]  # Reverse the string
    console.print(f"[bold yellow]Reversed: {reversed_message}[/bold yellow]")

def register(register_command):
    register_command(
        name="reverse",
        func=reverse,
        description="Reverse the provided message.",
        devmode=False
    )
