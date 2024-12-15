import os
import sys
import subprocess

def activate_venv():
    # Define the script to run within the virtual environment
    script_to_run = "main_SVRS.py"

    # Determine the platform-specific activation command
    if os.name == 'nt':  # Windows
        activate_command = f'.\\venv\\Scripts\\activate.bat && python {script_to_run}'
    else:  # macOS/Linux
        activate_command = f'source ./venv/bin/activate && python {script_to_run}'

    process = subprocess.Popen(activate_command, shell=True, text=True)

    # Wait for the process to complete
    process.wait()

if __name__ == "__main__":
    activate_venv()
