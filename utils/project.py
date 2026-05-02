import os
import json
import shutil

PROJECT_DIR = "projects"

def init_projects():
    if not os.path.exists(PROJECT_DIR):
        os.makedirs(PROJECT_DIR)

def create_project(name, domain):
    path = os.path.join(PROJECT_DIR, name)
    os.makedirs(path, exist_ok=True)

    data = {
        "name": name,
        "domain": domain
    }

    with open(os.path.join(path, "config.json"), "w") as f:
        json.dump(data, f, indent=4)

    return path

def list_projects():
    return os.listdir(PROJECT_DIR)

def load_project(name):
    path = os.path.join(PROJECT_DIR, name)
    config_path = os.path.join(path, "config.json")

    if not os.path.exists(config_path):
        return None

    with open(config_path) as f:
        return json.load(f)

def delete_project(name):
    path = os.path.join(PROJECT_DIR, name)
    shutil.rmtree(path, ignore_errors=True)
