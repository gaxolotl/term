from rich.console import Console
import platform

console = Console()

def sysinfo(args):
    console.print("[bold green]System Information:[/bold green]")
    console.print(f"System: {platform.system()}")
    console.print(f"Release: {platform.release()}")
    console.print(f"Version: {platform.version()}")
    console.print(f"Architecture: {platform.architecture()[0]}")

def register(register_command):
    register_command(
        name="sysinfo",
        func=sysinfo,
        description="Show system information.",
        devmode=False
    )