from utils.runner import run_command
from rich import print

def get_subdomains(domain):
    print("[cyan][1/3] Subdomain Enumeration...[/cyan]")

    subfinder = run_command(f"subfinder -d {domain} -silent")
    assetfinder = run_command(f"assetfinder --subs-only {domain}")

    subs = set(subfinder + assetfinder)

    print(f"[green][+] Found: {len(subs)} subdomains[/green]")

    return list(subs)
