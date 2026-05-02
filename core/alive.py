from utils.runner import run_command
import tempfile
from rich import print


def check_alive(subdomains, threads=50):
    print("[cyan][2/3] DNS Resolve + Alive Check...[/cyan]")

    if not subdomains:
        print("[red][!] No subdomains provided[/red]")
        return {"all": [], "categorized": {}}

    # -------------------------
    # Write subdomains to file
    # -------------------------
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as f:
        for sub in subdomains:
            f.write(sub + "\n")
        temp_file = f.name

    # -------------------------
    # Step 1: DNS Resolve
    # -------------------------
    print("[yellow][*] Resolving domains (dnsx)...[/yellow]")

    resolved = run_command(f"dnsx -l {temp_file} -silent")

    print(f"[green][+] Resolved: {len(resolved)}[/green]")

    if not resolved:
        return {"all": [], "categorized": {}}

    # -------------------------
    # Step 2: httpx
    # -------------------------
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as f2:
        for r in resolved:
            f2.write(r + "\n")
        resolved_file = f2.name

    print("[yellow][*] Running httpx...[/yellow]")

    command = (
        f"httpx -l {resolved_file} "
        f"-silent -threads {threads} "
        f"-status-code -title -follow-redirects "
        f"-timeout 10 -retries 2"
    )

    result = run_command(command)

    # -------------------------
    # Parse
    # -------------------------
    alive = []

    for line in result:
        try:
            parts = line.split(" ")

            url = parts[0]
            status = parts[1]
            title = " ".join(parts[2:]) if len(parts) > 2 else ""

            alive.append({
                "url": url,
                "status": status,
                "title": title
            })

        except:
            continue

    # -------------------------
    # Categorization
    # -------------------------
    categorized = {
        "200": [],
        "300": [],
        "403": [],
        "500": [],
        "other": []
    }

    for item in alive:
        s = item["status"]

        if s.startswith("2"):
            categorized["200"].append(item)
        elif s.startswith("3"):
            categorized["300"].append(item)
        elif s == "403":
            categorized["403"].append(item)
        elif s.startswith("5"):
            categorized["500"].append(item)
        else:
            categorized["other"].append(item)

    # -------------------------
    # Summary
    # -------------------------
    print(f"[green][+] Total Alive: {len(alive)}[/green]")
    print(f"[green]    200: {len(categorized['200'])}[/green]")
    print(f"[yellow]   300: {len(categorized['300'])}[/yellow]")
    print(f"[magenta]  403: {len(categorized['403'])}[/magenta]")
    print(f"[red]      500: {len(categorized['500'])}[/red]")
    print(f"[dim]      other: {len(categorized['other'])}[/dim]")

    return {
        "all": alive,
        "categorized": categorized
    }
