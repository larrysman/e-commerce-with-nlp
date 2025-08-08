# PROJECT FILES AND FOLDERS STRUCTURE FOR KIDNEY DISEASE CLASSIFICATION PROJECT

import os
import logging
from pathlib import Path
from typing import List

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s:")

project_name = "e-commerce-with-nlp"


# CREATE THE PROJECT DIRECTORY AND FILES

list_of_files_and_folders = [
    f"{project_name}/.gitignore",
    f"{project_name}/data/__init__.py",
    f"{project_name}/data/product.json",
    f"{project_name}/src/__init__.py",
    f"{project_name}/src/experiment.ipnyb",
    f"{project_name}/requirements.txt",
    f"{project_name}/README.md"
]


# FUNCTION TO CREATE THE PROJECT STRUCTURE

def create_project_structure(list_of_files_and_folders: List[str]) -> None:
    """
    Create the project structure based on the provided list of files and folders.
    If a file or folder does not exist, it will be created.
    If a file exists but is empty, it will be created as an empty file.

    Args:
        List: List containing the files and folders.

    Returns:
        None
    """
    for file_path in list_of_files_and_folders:
        file_path = Path(file_path)
        filedir, filename = os.path.split(file_path)

        if filedir:
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating directory: {filedir} for the file: {filename}")

        if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
            with open(file_path, 'w') as f:
                pass
            logging.info(f"Creating empty file: {file_path}")

        else:
            logging.info(f"File already exists: {file_path} and is not empty.")


if __name__ == "__main__":
    create_project_structure(list_of_files_and_folders)
    logging.info(f"Project structure for '{project_name}' created successfully.")
