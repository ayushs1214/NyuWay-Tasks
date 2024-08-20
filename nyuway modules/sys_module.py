# sys_module_example.py
import sys

def study_sys_module():
    print("Sys Module:")
    # Get command line arguments
    args = sys.argv
    print(f"Command Line Arguments: {args}")

    # Get the path of the Python interpreter
    python_path = sys.executable
    print(f"Python Interpreter Path: {python_path}")

    # Get Python version
    python_version = sys.version
    print(f"Python Version: {python_version}")

if __name__ == "__main__":
    study_sys_module()