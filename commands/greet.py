from rich.console import Console

console = Console()

def greet(args):
    name = args[0] if args else "stranger"
    console.print(f"[bold green]Hello, {name}![/bold green]")

def register(register_command):
    register_command(
        name="greet",
        func=greet,
        description="Greet the user by name.",
        devmode=False
    )