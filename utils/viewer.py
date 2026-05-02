from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich import box

console = Console()


def show_table(lines, title="Results", page_size=20):
    total = len(lines)

    # 🟢 اگر دیتا کم بود → بدون pagination
    if total <= page_size:
        table = Table(title=title, box=box.SIMPLE)
        table.add_column("#", style="dim", width=6)
        table.add_column("Value", style="white")

        for i, line in enumerate(lines, 1):
            table.add_row(str(i), line)

        console.print(table)
        console.print(f"\n[green]Total:[/green] {total}")

        input("\nPress Enter to go back...")
        return

    # 🔵 اگر دیتا زیاد بود → pagination
    current = 0

    while True:
        console.clear()

        table = Table(title=title, box=box.SIMPLE)
        table.add_column("#", style="dim", width=6)
        table.add_column("Value", style="white")

        end = current + page_size

        for i, line in enumerate(lines[current:end], start=current + 1):
            table.add_row(str(i), line)

        console.print(table)

        console.print(
            f"\n[cyan]Showing[/cyan] {current+1}-{min(end,total)} of {total}"
        )

        cmd = Prompt.ask(
            "[n] next | [p] prev | [q] quit",
            default="n"
        ).lower()

        if cmd == "n":
            if end < total:
                current += page_size
        elif cmd == "p":
            if current - page_size >= 0:
                current -= page_size
        elif cmd == "q":
            break
