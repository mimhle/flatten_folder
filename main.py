import os
import shutil
from typing import Literal
import argparse


def main(
        directory: str,
        action: Literal['move', 'copy'] = "move",
        delete_parent: bool = False,
) -> None:
    # get list of folders in directory
    list_of_folders = os.listdir(directory)
    # get all files in directory
    files = []
    for folder in list_of_folders:
        if os.path.isdir(os.path.join(directory, folder)):
            files += [os.path.join(directory, folder, file) for file in os.listdir(os.path.join(directory, folder))]

    # move files to directory
    for file in files:
        if action == "move":
            shutil.move(
                file,
                directory,
            )
        elif action == "copy":
            shutil.copy(
                file,
                directory,
            )
        else:
            raise ValueError("Action must be move or copy")

    # delete folders
    if delete_parent:
        for folder in list_of_folders:
            if os.path.isdir(os.path.join(directory, folder)):
                shutil.rmtree(os.path.join(directory, folder))

    # print(files)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="directory to clean")
    parser.add_argument("action", choices=["move", "copy"], help="action to perform")
    parser.add_argument("-d", "--delete-parent", action="store_true", help="delete parent folder")
    args = parser.parse_args()

    main(
        args.directory,
        args.action,
        args.delete_parent,
    )
