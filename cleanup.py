import os
import shutil
import tkinter as tk
from tkinter import messagebox

# Define the expected structure based on setup script
expected_structure = {
    'assets': [
        'charges'
    ],
    'assets/charges': [
        '__init__.py',
        'cross moline.svg',
        'crow.svg',
        'eagle.svg',
        'rose.svg',
        'scimitar.svg',
        'tower.svg'
    ],
    'resources': [
        'examples'
    ],
    'resources/examples': [
        '__init__.py',
        'coa gen example.png'
    ],
    'saved': [
        '__init__.py'
    ],
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
    ],
}

# Files and directories to keep at the root level
root_level_keepers = {'src', 'setup.py', 'README.md', 'requirements.txt', '.gitignore', 'cleanup.py', 'Windows_cleanup.bat'}

# Extensions and file types to ignore during cleanup
ignore_extensions = {'.bat', '.md'}
ignore_no_extension = {'LICENSE', 'CONTRIBUTING', 'CODE_OF_CONDUCT'}

# Directories to exclude from cleanup
exclude_dirs = {'.git', '.venv', '__pycache__'}

# Directories to preserve completely (do not delete any files within)
preserve_dirs = {'saved', 'assets', 'assets/charges', 'resources', 'resources/examples'}

# Log file to record deleted files
log_file = 'cleanup_log.txt'

def get_removal_list(directory, expected_contents, keepers=set()):
    """ Generate a list of files and directories that will be removed. """
    removal_list = []
    actual_contents = set(os.listdir(directory))
    expected_contents = set(expected_contents).union(keepers).union(exclude_dirs)

    for content in actual_contents:
        path_to_check = os.path.join(directory, content)
        # Skip preserved directories and .png files in resources/examples
        if content in preserve_dirs or os.path.commonpath([path_to_check]) in preserve_dirs:
            if content == "examples" and directory == os.path.join('.', 'resources'):
                if path_to_check.endswith('.png'):
                    continue
            continue
        if content not in expected_contents:
            if os.path.isdir(path_to_check) and content in exclude_dirs:
                continue
            if any(content.endswith(ext) for ext in ignore_extensions) or content in ignore_no_extension:
                continue
            # If it's a directory, we recursively add its contents to the removal list
            if os.path.isdir(path_to_check):
                removal_list.append(path_to_check)  # Add the directory itself
                for root, dirs, files in os.walk(path_to_check):
                    for name in files:
                        if root == os.path.join('.', 'resources', 'examples') and name.endswith('.png'):
                            continue  # Preserve .png files in resources/examples
                        removal_list.append(os.path.join(root, name))
                    for name in dirs:
                        if name not in exclude_dirs:
                            removal_list.append(os.path.join(root, name))
            else:
                removal_list.append(path_to_check)
    return removal_list

def cleanup_directory(directory, expected_contents, keepers=set(), log_handle=None):
    """ Remove unexpected files and directories in the given directory and log the actions """
    actual_contents = set(os.listdir(directory))
    keepers = set(keepers)
    exclude_dirs_set = set(exclude_dirs)
    
    # Create a combined set of items to keep
    to_keep = expected_contents.union(keepers).union(exclude_dirs_set)

    # Calculate the items to remove
    to_remove = actual_contents - to_keep

    for content in to_remove:
        path_to_remove = os.path.join(directory, content)
        # Skip if it's in the preserve_dirs
        if content in preserve_dirs or os.path.commonpath([path_to_remove]) in preserve_dirs:
            # Skip .png files within resources/examples
            if content == "examples" and directory == os.path.join('.', 'resources'):
                if path_to_remove.endswith('.png'):
                    continue
            continue
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
    # Generate the list of items to be removed
    removal_list = get_removal_list('.', set(), root_level_keepers)
    for directory, contents in expected_structure.items():
        full_path = os.path.join('.', directory)
        if os.path.exists(full_path):
            removal_list.extend(get_removal_list(full_path, set(contents)))

    # Initialize Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Display the list of items to be removed
    if removal_list:
        removal_list_str = "\n".join(removal_list)
        messagebox.showinfo(
            "Files/Directories to be Removed",
            f"The following files/directories will be removed:\n\n{removal_list_str}"
        )
    else:
        messagebox.showinfo("Cleanup", "No files or directories to remove.")

    # Ask user for confirmation before cleanup
    response = messagebox.askyesno(
        "Confirm Cleanup",
        f"This will remove {len(removal_list)} items. Proceed?"
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
