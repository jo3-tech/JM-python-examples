"""
Script to setup a virtual environment and install requirements.
"""

import os
import subprocess
import sys
from pathlib import Path

def main():
    # Setup directories.
    project_dir = Path.cwd()
    venv_dir = project_dir / ".venv"
    requirements = project_dir / "requirements.txt"

    # Create venv.
    print("\n")
    print(f"...Creating virtual environment in: {venv_dir}...\n")
    subprocess.check_call([sys.executable, "-m", "venv", str(venv_dir)]) # python -m venv .venv

    # Determine python inside the venv.
    if os.name == "nt":
        python_exe = venv_dir / "Scripts" / "python.exe"
    else:
        python_exe = venv_dir / "bin" / "python"

    # Upgrade pip using python -m pip.
    subprocess.check_call([str(python_exe), "-m", "pip", "install", "--upgrade", "pip"]) # python -m pip install --upgrade pip

    # Install requirements
    if requirements.exists():
        print(f"...Installing requirements from: {requirements}...\n")
        subprocess.check_call([str(python_exe), "-m", "pip", "install", "-r", str(requirements)]) # python -m pip install -r requirements.txt
    else:
        print("...No requirements.txt found — skipping dependency installation...\n")

    # Show how to activate the venv.
    print("...Environment setup complete. ")
    if os.name == "nt":
        # Windows.
        print("Activate it with:")
        print(r"    .venv\Scripts\activate")
    else:
        # Posix (Linux, macOS) or other.
        print("Activate it with:")
        print("    source .venv/bin/activate")
    print("\n")

    print("...End...\n")

if __name__ == "__main__":
    main()
