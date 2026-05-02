import subprocess

def run_command(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )

        output = result.stdout if result.stdout else result.stderr
        return output.splitlines()

    except Exception as e:
        print(f"[ERROR] {e}")
        return []
