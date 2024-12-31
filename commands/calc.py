from rich.console import Console

console = Console()

def calc(args):
    try:
        result = eval(' '.join(args))
        console.print(f"[bold green]Result: {result}[/bold green]")
    except Exception as e:
        console.print(f"[bold red]Error: {e}[/bold red]")

def register(register_command):
    register_command(
        name="calc",
        func=calc,
        description="Perform a basic calculation.",
        devmode=False
    )