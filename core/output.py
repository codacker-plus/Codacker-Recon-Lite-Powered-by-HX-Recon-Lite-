import json
import os
from datetime import datetime
from rich import print


def save_outputs(project_path, domain, subdomains, alive_data):
    print("[cyan][3/3] Saving Results...[/cyan]")

    alive = alive_data["all"]
    categorized = alive_data["categorized"]

    data = {
        "domain": domain,
        "timestamp": str(datetime.now()),
        "summary": {
            "total_subdomains": len(subdomains),
            "alive": len(alive)
        },
        "subdomains": subdomains,
        "alive": alive
    }

    # JSON
    with open(os.path.join(project_path, "result.json"), "w") as f:
        json.dump(data, f, indent=4)

    # TXT
    with open(os.path.join(project_path, "subdomains.txt"), "w") as f:
        f.write("\n".join(subdomains))

    with open(os.path.join(project_path, "alive.txt"), "w") as f:
        f.write("\n".join([x["url"] for x in alive]))

    # Categorized outputs
    with open(os.path.join(project_path, "alive_200.txt"), "w") as f:
        f.write("\n".join([x["url"] for x in categorized["200"]]))

    with open(os.path.join(project_path, "alive_403.txt"), "w") as f:
        f.write("\n".join([x["url"] for x in categorized["403"]]))

    with open(os.path.join(project_path, "alive_500.txt"), "w") as f:
        f.write("\n".join([x["url"] for x in categorized["500"]]))

    print("[green][✓] Saved (JSON + categorized TXT files)[/green]")
