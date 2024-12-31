from rich.console import Console

console = Console()

def count(args):
    try:
        limit = int(args[0]) if args else 10
        for i in range(1, limit + 1):
            console.print(f"[bold blue]{i}[/bold blue]")
    except ValueError:
        console.print("[bold red]Please provide a valid number![/bold red]")

def register(register_command):
    register_command(
        name="count",
        func=count,
        description="Count up to a specified number.",
        devmode=False
    )