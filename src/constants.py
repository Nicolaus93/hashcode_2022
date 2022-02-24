import pathlib
from pathlib import Path

PYPKG_DIR = pathlib.Path().absolute()
REPO_DIR = PYPKG_DIR.parent
DATA_DIR = REPO_DIR / 'data'

A_CASE = DATA_DIR / "a_an_example.in.txt"
B_CASE = DATA_DIR / "b_better_start_small.in.txt"
C_CASE = DATA_DIR / "c_collaboration.in.txt"
D_CASE = DATA_DIR / "d_dense_schedule.in.txt"
E_CASE = DATA_DIR / "e_exceptional_skills.in.txt"
F_CASE = DATA_DIR / "f_find_great_mentors.in.txt"

CURRENT_CASE = A_CASE
