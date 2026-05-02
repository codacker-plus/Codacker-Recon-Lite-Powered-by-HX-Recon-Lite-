import os
from rich.prompt import Prompt
from rich import print
from utils.viewer import show_table

PROJECTS_DIR = "projects"


def list_projects():
    if not os.path.exists(PROJECTS_DIR):
        os.makedirs(PROJECTS_DIR)

    projects = os.listdir(PROJECTS_DIR)

    if not projects:
        print("[red]No projects found[/red]")
        return None

    for i, p in enumerate(projects, 1):
        print(f"[cyan]{i}[/cyan] - {p}")

    choice = Prompt.ask("Select project number")

    try:
        selected = projects[int(choice) - 1]
        return selected
    except:
        print("[red]Invalid selection[/red]")
        return None


def load_project():
    project = list_projects()
    if not project:
        return

    project_path = os.path.join(PROJECTS_DIR, project)

    while True:
        print(f"\n[bold green]Project: {project}[/bold green]")
        print("1. View Subdomains")
        print("2. View Alive")
        print("3. Back")

        choice = Prompt.ask("Choose option")

        if choice == "1":
            file_path = os.path.join(project_path, "subdomains.txt")

            if not os.path.exists(file_path):
                print("[red]subdomains.txt not found[/red]")
                continue

            with open(file_path) as f:
                lines = [l.strip() for l in f if l.strip()]

            show_table(lines, title="Subdomains")

        elif choice == "2":
            file_path = os.path.join(project_path, "alive.txt")

            if not os.path.exists(file_path):
                print("[red]alive.txt not found[/red]")
                continue

            with open(file_path) as f:
                lines = [l.strip() for l in f if l.strip()]

            show_table(lines, title="Alive Targets")

        elif choice == "3":
            break
