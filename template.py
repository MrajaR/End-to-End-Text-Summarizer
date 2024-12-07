import os
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
    )

project_name = "text_summarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f'src/{project_name}/__init__.py',
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init_.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "main.py",
    "Dockerfile",
    "app.py",
    "setup.py",
    "requirements.txt",
    "config/config.yaml",
    "params.yaml",
    "research/trials.ipynb"
]

for file in list_of_files:
    filepath = Path(file)
    filedir, filename = os.path.split(filepath)

    if filedir != "":  # check if filedir is not empty (there are list of filepath that are not a only a filename in list of files)
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating file: {filepath}")

    else:
        logging.info(f"File already exists: {filepath}")
