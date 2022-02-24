import numpy as np
import pandas as pd
import typing as T

from src.constants import A_CASE
from src.data import Project, Contributor
from collections import defaultdict
from loguru import logger
from reading import read_file


def read_input(input_file):
    with open(input_file) as f:
        for line in f:
            print(line)


def greedy(projects: T.List[Project], contributors: T.List[Contributor]):
    tot_score = 0
    projects = sorted(projects, key=lambda x: x.best_before)
    for p in projects:
        available = defaultdict(list)
        for skill, level in p.skills.items():
            for c in contributors:
                if skill in c.skills and level <= c.skills[skill] and c.time_when_free + p.duration <= p.best_before:
                    c.when_done = c.time_when_free + p.duration
                    available[skill].append(c)

        assignment = dict()
        assigned_contr = set()
        for skill in available:
            available[skill] = sorted(available[skill], key=lambda x: x.when_done)
            # select the person and remove him from the other lists
            # for c in available[skill]:
            i = 0
            while i <= len(available[skill]):
                selected = available[skill][i]
                if selected not in assigned_contr:
                    assignment[skill] = selected
                    break
                else:
                    i += 1

            if skill not in assignment:
                continue  # go over the next project

        # update time for assigned people
        last_day = -1
        for skill, c in assignment.items():
            # c.time_when_free = c.when_done
            last_day = max(last_day, c.when_done)

        for skill, c in assignment.items():
            c.time_when_free = last_day

        p.end_date = last_day
        logger.info(f"score for {p} is: {p.score}.\n{assignment}")
        tot_score += p.score

    return tot_score


def score(solution) -> int:
    last_day = 0
    project = solution.project
    for skill, person in solution.employed.items():
        last_day = max(last_day, person.time + project.duration)
        # last_day = max(last_day, person.when_done)

    how_much_late = max(0, last_day - project.best_before)
    return max(0, project.score - how_much_late)


if __name__ == '__main__':
    cs, ps = read_file(A_CASE)
    res = greedy(ps, cs)
    print(res)
