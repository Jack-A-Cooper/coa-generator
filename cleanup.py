import os
import shutil
import tkinter as tk
from tkinter import messagebox

# Define the expected structure based on setup script
expected_structure = {
    'src': [
        'main.py',
        'coat_of_arms.py',
        'heraldic_elements.py',
        'user_interface.py',
        'renderer.py',
        'saver.py',
        'utils.py',
        'tests'
    ],
    'src/tests': [
        '__init__.py'
    ]
}

# Files and directories to keep at the root level
root_level_keepers = {'src', 'setup.py', 'README.md', 'requirements.txt', '.gitignore', 'cleanup.py', 'Windows_cleanup.bat'}

# Extensions and file types to ignore during cleanup
ignore_extensions = {'.bat', '.md'}
ignore_no_extension = {'LICENSE', 'CONTRIBUTING', 'CODE_OF_CONDUCT'}

# Directories to exclude from cleanup
exclude_dirs = {'.git', '.venv', '__pycache__'}

# Log file to record deleted files
log_file = 'cleanup_log.txt'

def count_removals(directory, expected_contents, keepers=set()):
    """ Count the number of files and directories that will be removed. """
    total_removals = 0
    actual_contents = set(os.listdir(directory))
    expected_contents = set(expected_contents).union(keepers).union(exclude_dirs)

    for content in actual_contents:
        if content not in expected_contents:
            path_to_check = os.path.join(directory, content)
            if os.path.isdir(path_to_check) and content in exclude_dirs:
                continue
            if any(content.endswith(ext) for ext in ignore_extensions) or content in ignore_no_extension:
                continue
            # If it's a directory, we recursively count its contents
            if os.path.isdir(path_to_check):
                total_removals += 1  # for the directory itself
                for root, dirs, files in os.walk(path_to_check):
                    total_removals += len(files)
                    total_removals += len([d for d in dirs if d not in exclude_dirs])
            else:
                total_removals += 1
    return total_removals


# The count_removals function appears to be correctly implemented.

# Make sure to update the cleanup_directory function as follows:
def cleanup_directory(directory, expected_contents, keepers=set(), log_handle=None):
    """ Remove unexpected files and directories in the given directory and log the actions """
    # Set operations are used directly to determine unexpected contents
    actual_contents = set(os.listdir(directory))
    keepers = set(keepers)
    exclude_dirs_set = set(exclude_dirs)
    
    # Create a combined set of items to keep
    to_keep = expected_contents.union(keepers).union(exclude_dirs_set)
    
    # Calculate the items to remove
    to_remove = actual_contents - to_keep

    for content in to_remove:
        path_to_remove = os.path.join(directory, content)
        # The 'continue' logic is fine here
        if any(content.endswith(ext) for ext in ignore_extensions) or content in ignore_no_extension:
            continue  # Skip ignored file types
        try:
            if os.path.isfile(path_to_remove):
                os.remove(path_to_remove)
                if log_handle:
                    log_handle.write(f"Removed file: {path_to_remove}\n")
            elif os.path.isdir(path_to_remove):
                shutil.rmtree(path_to_remove)
                if log_handle:
                    log_handle.write(f"Removed directory: {path_to_remove}\n")
        except PermissionError as e:
            if log_handle:
                log_handle.write(f"Permission denied when trying to remove: {path_to_remove}. Error: {e}\n")

def main():
    total_removals = count_removals('.', set(), root_level_keepers)
    for directory, contents in expected_structure.items():
        full_path = os.path.join('.', directory)
        if os.path.exists(full_path):
            total_removals += count_removals(full_path, set(contents))

    # Initialize Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Ask user for confirmation before cleanup
    response = messagebox.askyesno(
        "Confirm Cleanup",
        f"This will remove {total_removals} files/dirs not conforming to the setup. Proceed?"
    )

    # Destroy the Tkinter root window
    root.destroy()

    if response:  # If user confirms cleanup
        with open(log_file, 'w') as log_handle:
            # Cleanup top-level directory
            cleanup_directory('.', set(), root_level_keepers, log_handle)

            # Cleanup each expected directory
            for directory, contents in expected_structure.items():
                full_path = os.path.join('.', directory)
                if os.path.exists(full_path):
                    cleanup_directory(full_path, set(contents), keepers=root_level_keepers, log_handle=log_handle)
            
            log_handle.write("Cleanup completed.\n")

        print(f"Cleanup completed. See {log_file} for details.")
    else:
        print("Cleanup canceled by the user.")

if __name__ == '__main__':
    main()