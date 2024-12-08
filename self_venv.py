import os
import sys
import subprocess

def activate_venv():
    # Determine the platform (Windows or Unix-based)
    if os.name == 'nt':  # Windows
        activate_script = os.path.join(os.getcwd(), 'venv', 'Scripts', 'activate.bat')
    else:  # Unix-based (Linux, macOS, etc.)
        activate_script = os.path.join(os.getcwd(), 'venv', 'bin', 'activate')
    
    # Check if the venv is already activated
    if sys.prefix == os.path.join(os.getcwd(), 'venv'):
        print("Virtual environment is already activated.")
        
    else:
        if os.name == 'nt':
            subprocess.call([activate_script, '&&', 'python', *sys.argv])
        else:
            subprocess.call(['source', activate_script, '&&', 'python', *sys.argv])
        sys.exit()

if __name__ == "__main__":
    activate_venv()
    
    current_dir = os.getcwd()
    script_path = current_dir + "\Script.py"
    # result = subprocess.run(["python", script_path], capture_output=True, text=True)

    with open(script_path) as f:
        code = f.read()
        exec(code)
