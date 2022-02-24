import typing as T
import pathlib
from loguru import logger
from collections import OrderedDict

from constants import A_CASE
from src.data import Project, Skill, Contributor


def read_file(p: pathlib.Path) -> T.Tuple[T.Any]:
    contributors: T.List[Contributor] = []
    projects: T.List[Project] = []
    with open(str(p), 'r') as fp:
        C, P = [int(x) for x in fp.readline().split()]

        for idx in range(C):
            name, skillcount = fp.readline().split()
            kwargs_dict = dict(name=name, skills=list())
            for k in range(int(skillcount)):
                skillname, value = fp.readline().split()
                skill = Skill(skillname, int(value))
                kwargs_dict["skills"].append(skill)
            contributors.append(Contributor(**kwargs_dict))

        for c_idx in range(P):
            l = fp.readline().split()
            name = l[0]
            duration, score, best_before, role_count = [int(x) for x in l[1:]]
            skills = []
            for k in range(role_count):
                skillname, value = fp.readline().split()
                skills.append(Skill(skillname, int(value)))
            projects.append(Project(name=name,
                                    duration=duration,
                                    max_score=score,
                                    best_before=best_before,
                                    skills=skills,
                                    employed=OrderedDict({k:None for k in skills})
                                    ))

    return contributors, projects


if __name__ == "__main__":
    contributors, projects = read_file(A_CASE)
    for c in contributors:
        logger.info(c)
    for p in projects:
        logger.info(p)
