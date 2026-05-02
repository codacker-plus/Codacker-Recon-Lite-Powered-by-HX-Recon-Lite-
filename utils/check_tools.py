import shutil
from rich import print

REQUIRED_TOOLS = [
    "subfinder",
    "assetfinder",
    "amass",
    "dnsx",
    "httpx"
]


def check_tools():
    print("\n[bold cyan]Checking required tools...[/bold cyan]\n")

    missing = []

    for tool in REQUIRED_TOOLS:
        if shutil.which(tool) is None:
            print(f"[red]✗ {tool} not found[/red]")
            missing.append(tool)
        else:
            print(f"[green]✓ {tool} found[/green]")

    if missing:
        print("\n[bold red]Missing tools detected![/bold red]")
        print("Please install them before running HX-Recon-Lite.\n")

        print("[yellow]Missing:[/yellow]", ", ".join(missing))
        exit(1)

    print("\n[bold green]All tools are installed ✔[/bold green]\n")
