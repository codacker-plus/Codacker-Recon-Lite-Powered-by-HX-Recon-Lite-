import sys
import os

from utils.banner import show_banner
from utils.project import (
    init_projects,
    create_project,
    list_projects,
    load_project,
    delete_project
)
from utils.menu import main_menu, project_menu
from utils.check_tools import check_tools

from core.subdomain import get_subdomains
from core.alive import check_alive
from core.output import save_outputs

# 🔥 NEW (viewer)
from utils.viewer import show_table


# -----------------------------
# RECON ENGINE
# -----------------------------
def run_recon(project):
    domain = project["domain"]
    name = project["name"]
    path = f"projects/{name}"

    print(f"\n[+] Running Recon for: {domain}\n")

    subs = get_subdomains(domain)
    alive_data = check_alive(subs)

    save_outputs(path, domain, subs, alive_data)

    print("\n[✓] Recon Completed\n")


# -----------------------------
# VIEW SUBDOMAINS (RICH VIEWER)
# -----------------------------
def show_subdomains(project_name):
    path = f"projects/{project_name}/subdomains.txt"

    if not os.path.exists(path):
        print("[!] No subdomains found. Run recon first.")
        return

    with open(path) as f:
        subs = [s.strip() for s in f if s.strip()]

    if not subs:
        print("[!] Empty file")
        return

    show_table(subs, title="Subdomains")


# -----------------------------
# VIEW ALIVE TARGETS
# -----------------------------
def show_alive(project_name):
    path = f"projects/{project_name}/alive.txt"

    if not os.path.exists(path):
        print("[!] No alive results found. Run recon first.")
        return

    with open(path) as f:
        lines = [l.strip() for l in f if l.strip()]

    if not lines:
        print("[!] Empty file")
        return

    show_table(lines, title="Alive Targets")


# -----------------------------
# NEW PROJECT
# -----------------------------
def new_project():
    name = input("Project Name: ").strip()
    domain = input("Domain: ").strip()

    if not name or not domain:
        print("[!] Invalid input")
        return

    create_project(name, domain)

    project = {"name": name, "domain": domain}

    print(f"[+] Project created: {name}")

    run_recon(project)


# -----------------------------
# LOAD PROJECT FLOW
# -----------------------------
def load_project_flow():
    projects = list_projects()

    if not projects:
        print("[!] No projects found")
        return

    print("\nAvailable Projects:\n")

    for i, p in enumerate(projects):
        print(f"[{i}] {p}")

    try:
        choice = int(input("\nSelect project: "))
        selected = projects[choice]
    except:
        print("[!] Invalid selection")
        return

    project = load_project(selected)

    if not project:
        print("[!] Failed to load project")
        return

    # 🔥 PROJECT MENU LOOP
    while True:
        opt = project_menu()

        if opt == "1":
            run_recon(project)

        elif opt == "2":
            show_subdomains(selected)

        elif opt == "3":
            show_alive(selected)

        elif opt == "4":
            delete_project(selected)
            print("[!] Project deleted")
            break

        elif opt == "5":
            break

        else:
            print("[!] Invalid option")


# -----------------------------
# MAIN
# -----------------------------
def main():
    try:
        check_tools()  # ✅ فقط یکبار اجرا بشه

        init_projects()
        show_banner()

        while True:
            choice = main_menu()

            if choice == "1":
                new_project()

            elif choice == "2":
                load_project_flow()

            elif choice == "3":
                print("\nGoodbye 👋")
                sys.exit()

            else:
                print("[!] Invalid option")

    except KeyboardInterrupt:
        print("\n\nGoodbye 👋")
        sys.exit()


if __name__ == "__main__":
    main()
