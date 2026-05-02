import os

BASE_DIR = "hx-recon-lite"

structure = {
    "": ["main.py", "requirements.txt"],
    "projects": [],
    "core": ["__init__.py", "subdomain.py", "alive.py", "output.py"],
    "utils": ["__init__.py", "runner.py", "banner.py", "menu.py", "project.py"],
}


def create_structure(base, struct):
    for folder, files in struct.items():
        dir_path = os.path.join(base, folder)

        # ساخت دایرکتوری
        os.makedirs(dir_path, exist_ok=True)

        # ساخت فایل‌ها
        for file in files:
            file_path = os.path.join(dir_path, file)

            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    f.write("")  # فایل خالی
                print(f"[+] Created file: {file_path}")
            else:
                print(f"[=] Exists: {file_path}")


if __name__ == "__main__":
    create_structure(BASE_DIR, structure)
    print("\n[✓] Project structure created successfully.")
