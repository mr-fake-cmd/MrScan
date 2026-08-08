import shutil
import subprocess


def command_exists(cmd):
    return shutil.which(cmd) is not None


def run(cmd):
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return result.stdout.strip()

        return ""

    except Exception:
        return ""