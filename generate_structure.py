import os

def generate_markdown_directory_tree(startpath):
    """
    Generates a markdown representation of the directory tree starting at startpath.
    :param startpath: The directory path to start the tree generation from.
    :return: A string containing the markdown representation of the tree.
    """

    def construct_directory_md(root, prefix=""):
        items = os.listdir(root)
        items.sort(key=lambda x: (not os.path.isdir(os.path.join(root, x)), x.lower()))
        paths = [os.path.join(root, item) for item in items if not item.startswith('.')]
        markdown = ""

        for i, path in enumerate(paths):
            if os.path.isdir(path):
                if i == len(paths) - 1:
                    connector = "└── "
                    next_prefix = prefix + "    "
                else:
                    connector = "├── "
                    next_prefix = prefix + "│   "
                markdown += f"{prefix}{connector}{os.path.basename(path)}/\n"
                markdown += construct_directory_md(path, next_prefix)
            else:
                connector = "└── " if i == len(paths) - 1 else "├── "
                markdown += f"{prefix}{connector}{os.path.basename(path)}\n"

        return markdown

    markdown_tree = f"{os.path.basename(startpath)}/\n│\n{construct_directory_md(startpath)}"
    return markdown_tree.rstrip() + '\n'

# Use the current directory or change it to the path where you want to start making the tree
current_directory = os.getcwd()
markdown_tree = generate_markdown_directory_tree(current_directory)

# Print the markdown to console
print(markdown_tree)

# Save the markdown to a file with utf-8 encoding
with open("DIRECTORY_STRUCTURE.md", 'w', encoding='utf-8') as md_file:
    md_file.write(markdown_tree)
