import pathlib
from pathlib import Path

PYPKG_DIR = pathlib.Path().absolute()
REPO_DIR = PYPKG_DIR.parent
DATA_DIR = REPO_DIR / 'data'
