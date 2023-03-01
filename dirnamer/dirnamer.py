"""
@Author: Matthew Barton
@Email: 99matthewbarton@gmail.com
"""

import os
import sys

def rename_files(folder_path, name):
    """Rename all of the files within a folder to the name of the folder or input name with an id (ie "folder_name1", "folder_name2)"""
    files = os.listdir(folder_path)
    for i, file in enumerate(files):
        file_path = os.path.join(folder_path, file)
        extension = os.path.splitext(file_path)[1]
        new_file_path = os.path.join(folder_path, name + str(i + 1) + extension)
        os.rename(file_path, new_file_path)


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python rename_files.py <folder_path> <optional: name>")
        sys.exit(1)
    folder_path = sys.argv[1]
    name = os.path.basename(folder_path)
    if len(sys.argv) == 3:
        name = sys.argv[2]
    print(f"Are you sure you want to rename all files in {folder_path} to {name}? (Y/N)")
    confirm = input().lower()
    if confirm == "y":
        rename_files(folder_path, name)
