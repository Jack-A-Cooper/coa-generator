import os
import shutil
import subprocess
import sys

def install_requirements():
    """Install required packages from requirements.txt."""
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

def create_directories():
    """Create directory structure for the coat of arms generator."""
    directories = [
        'src',
        'data',
        'assets',
        'saved_coats_of_arms',
        'tests'
    ]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Directory '{directory}' has been created or already exists.")

def move_files_to_src():
    """Move files to the src directory if they're not already there."""
    src_files = [
        'main.py',
        'coat_of_arms.py',
        'heraldic_elements.py',
        'user_interface.py',
        'renderer.py',
        'saver.py',
        'utils.py'
    ]

    for file_name in src_files:
        # Check if file exists in the current directory
        if os.path.exists(file_name):
            # Move it to the src directory
            shutil.move(file_name, os.path.join('src', file_name))
            print(f"Moved '{file_name}' to 'src/' directory.")

def create_initial_files():
    """Create initial files with basic content if they don't exist."""
    src_files = {
        'main.py': '# TODO: Implement main functionality\n',
        'coat_of_arms.py': '# TODO: Implement coat_of_arms functionality\n',
        'heraldic_elements.py': '# TODO: Implement heraldic_elements functionality\n',
        'user_interface.py': '# TODO: Implement user_interface functionality\n',
        'renderer.py': '# TODO: Implement renderer functionality\n',
        'saver.py': '# TODO: Implement saver functionality\n',
        'utils.py': '# TODO: Implement utils functionality\n',
    }

    for file_name, content in src_files.items():
        file_path = os.path.join('src', file_name)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                file.write(content)
                print(f"File '{file_path}' has been created.")

def main():
    """Run the main functions to set up the coat of arms generator."""
    install_requirements()
    create_directories()
    move_files_to_src()
    create_initial_files()
    print("Setup completed.")

if __name__ == '__main__':
    main()
