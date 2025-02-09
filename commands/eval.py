from rich.console import Console
import platform

console = Console()

def execute(args):
    text = input(">>> ")
    eval(text)

def register(register_command):
    register_command(
        name="eval",
        func=execute,
        description="Execute python code.",
        devmode=True
    )