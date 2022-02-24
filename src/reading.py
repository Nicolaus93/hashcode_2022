import typing as T
import pathlib
from loguru import logger
import pandas as pd

from constants import CURRENT_CASE
from src.data import Project,Skill,Contributor

def read_file(p:pathlib.Path)->T.Tuple[T.Any]:

    contributors:T.List[Contributor] = []
    projects:T.List[Project] = []
    with open(str(p) ,'r') as fp:
        C,P= [int(x) for x in fp.readline().split()]

        for idx in range(C):
            name, skillcount = fp.readline().split()
            kwargs_dict= dict(name=name,skills=dict())
            for k in range(int(skillcount)):
                skillname, value = fp.readline().split()
                kwargs_dict['skills'][Skill(skillname)] = int(value)
            contributors.append(Contributor(**kwargs_dict))

        for c_idx in enumerate(P):
            req_days, score, best_before, role_count = fp.readline().split()

           #
            print("DO!")

    # the first line contains:
    # the name of the project (ASCII string of at most 20 characters, all of which are lowercase or uppercase English alphabet letters a-z and A-Z or numbers 0-9),
    # an integer Di (1 ≤Di ≤ 105) – the number of days it takes to complete the project,
    # an integer Si (1 ≤ Si ≤ 105) – the score awarded for project’s completion,
    # an integer Bi (1 ≤ Bi ≤ 105) – the “best before” day for the project,
    # an integer Ri (1 ≤ Ri ≤ 100) – the number of roles in the project.
    # the next Ri lines describe the skills in the project:
    # a string Xk – the name of the skill (ASCII string of at most 20 characters, all of which are lowercase or uppercase English alphabet letters a-z and A-Z, numbers 0-9, dashes '-' or pluses '+'),
    # an integer Lk (1≤Lk≤100) – the required skill level.

    return contributors,projects


read_file(CURRENT_CASE)