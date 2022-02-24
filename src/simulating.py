import typing as T
from collections import OrderedDict
from dataclasses import dataclass, field


@dataclass(frozen=True, eq=True)
class Skill:
    name: str


@dataclass
class Contributor:
    name: str
    skills: T.Dict[Skill, int]


@dataclass
class Project:
    name: str
    best_before: int
    score: int
    skills: T.Dict[Skill, int]
    employed: T.Dict[Skill, Contributor]

    def is_team_valid(self,contributors:T.Sequence[Contributor])->T.Dict[Skill,Contributor]:
        """Return the SUBSET of *contributors* that """


        return dict()



@dataclass
class Solution:
    project: Project
