# os_module_example.py
import os

def study_os_module():
    print("OS Module:")
    # Get current working directory
    cwd = os.getcwd()
    print(f"Current Working Directory: {cwd}")

    # List files in current directory
    files = os.listdir('.')
    print(f"Files in Current Directory: {files}")

    # Create a new directory
    os.mkdir('new_directory')
    print("Created new_directory")

    # Rename the directory
    os.rename('new_directory', 'renamed_directory')
    print("Renamed directory to renamed_directory")

    # Remove the directory
    os.rmdir('renamed_directory')
    print("Removed renamed_directory")

if __name__ == "__main__":
    study_os_module()
