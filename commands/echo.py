from rich.console import Console

console = Console()

def echo(args):
    message = " ".join(args)
    console.print(f"[bold magenta]{message}[/bold magenta]")

def register(register_command):
    register_command(
        name="echo",
        func=echo,
        description="Echo a message to the console.",
        devmode=False
    )