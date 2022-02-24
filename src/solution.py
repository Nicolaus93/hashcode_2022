import numpy as np
import pandas as pd
import typing as T
from src.data import Project, Contributor
from collections import defaultdict


def read_input(input_file):
    with open(input_file) as f:
        for line in f:
            print(line)


def greedy(projects: T.List[Project], contributors: T.List[Contributor]):

    projects = sorted(projects, key=lambda x: x.best_before)
    for p in projects:
        available = defaultdict(list)
        for skill, level in p.skills.items():
            for c in contributors:
                if skill in c.skills and level >= c.skills[skill] and c.time + p.duration <= p.best_before:
                    c.when_done = c.time + p.duration
                    available[skill].append(c)

        assignment = dict()
        assigned_contr = set()
        for skill in available:
            available[skill] = sorted(available[skill], key=lambda x: x.when_done)
            # select the person and remove him from the other lists
            i = 0
            while i <= len(available[skill]):
                selected = available[skill][i]
                if selected not in assigned_contr:
                    assignment[skill] = selected
                    break
                else:
                    i += 1

            if skill not in assignment:
                return 0

        # update time for assigned people
        for skill, c in assignment.items():
            pass

    return 0


def score(solution) -> int:
    last_day = 0
    project = solution.project
    for skill, person in solution.employed.items():
        last_day = max(last_day, person.time + project.duration)
        # last_day = max(last_day, person.when_done)

    how_much_late = max(0, last_day - project.best_before)
    return max(0, project.score - how_much_late)


if __name__ == '__main__':
    read_input("/home/nico/hashcode_2022/data/a_an_example.in.txt")

