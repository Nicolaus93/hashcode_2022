import pathlib
import typing as T
from src.constants import A_CASE, F_CASE, E_CASE, D_CASE, C_CASE, B_CASE
from src.data import Project, Contributor
from collections import defaultdict
from loguru import logger
from reading import read_file
from writing import write_file, write_str


def find_assignment(project, contributors):
    available = defaultdict(list)
    for skill in project.skills:
        for c in contributors:
            c_skills = {s.name: s.level for s in c.skills}
            if skill.name in c_skills and skill.level <= c_skills[skill.name] and c.time_when_free + project.duration <= project.best_before:
                c.when_done = c.time_when_free + project.duration
                available[skill].append(c)

    if len(available) != len(project.skills):
        return {}

    assignment = dict()
    assigned_contr = set()
    for skill in available:
        available[skill] = sorted(available[skill], key=lambda x: x.when_done)
        # select the person and remove him from the other lists
        for c in available[skill]:
            if c not in assigned_contr:
                assignment[skill] = c
                assigned_contr.add(c)
                break

        if skill not in assignment:
            return {}

    return assignment


def greedy(projects: T.List[Project], contributors: T.List[Contributor], verbose: bool = False):
    tot_score = 0
    projects = sorted(projects, key=lambda x: x.best_before)
    finished_projects = []
    for p in projects:
        assignment = find_assignment(p, contributors)
        if len(assignment) == 0:
            continue
        elif len(assignment) != len(p.skills):
            logger.info("Something went wrong!")
            continue

        # update time for assigned people
        last_day = -1
        for skill, c in assignment.items():
            # c.time_when_free = c.when_done
            last_day = max(last_day, c.when_done)

        for skill, c in assignment.items():
            c.time_when_free = last_day
            p.employed[skill] = c

        if len(p.employed) != len(p.skills):
            logger.info("Something went wrong!")
            continue

        p.end_date = last_day
        if verbose:
            logger.info(f"score for {p} is: {p.score}.\n{assignment}")
        tot_score += p.score
        finished_projects.append(p)

    logger.info(f"total score = {tot_score}")
    return finished_projects


def score(solution) -> int:
    last_day = 0
    project = solution.project
    for skill, person in solution.employed.items():
        last_day = max(last_day, person.time + project.duration)

    how_much_late = max(0, last_day - project.best_before)
    return max(0, project.score - how_much_late)


if __name__ == '__main__':
    p = pathlib.Path('.')
    cases = [A_CASE, B_CASE, C_CASE, D_CASE, E_CASE, F_CASE]
    for pos, case in enumerate(cases):
        cs, ps = read_file(case)
        res = greedy(ps, cs)
        sol_str = write_str(res)
        logger.info(f"writing solution for {case}")
        write_file(sol_str, p.parent / f"sol{pos},txt")
