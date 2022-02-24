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
    duration: int
    best_before: int
    score: int
    max_score: int
    skills: T.Dict[Skill, int]
    employed: T.Dict[Skill, Contributor]
    progress: int = 0
    day: int = 0

    @property
    def is_done(self):
        return self.progress >= self.duration

    def update_score(self) -> int:
        if self.day <= self.best_before:
            self.score = self.max_score
        else:
            self.score = max(0, self.day - self.best_before)
        return self.score

    # he “best before” time in days – if the project last day of work is strictly before the indicated day, it earns the full score. If it’s late (that is, the project is still worked on during or after its "best before day"), it gets one point less for each day it is late, but no less than zero points. See also the example in the "Assignments" section below.

    def is_team_valid(self, contributors: T.Sequence[Contributor]) -> T.Dict[Skill, Contributor]:
        """Return the SUBSET of *contributors* that """
        return dict()


@dataclass
class Solution:
    project: Project
