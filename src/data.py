import typing as T
import numpy as np
from dataclasses import dataclass, field


@dataclass(frozen=True, eq=True)
class Skill:
    name: str
    level: int


@dataclass
class Contributor:
    name: str
    skills: T.List[Skill]
    time_when_free: int = 0

    def __hash__(self):
        return hash(self.name)


@dataclass
class Project:
    name: str
    duration: int
    best_before: int
    max_score: int
    skills: T.List[Skill] = field(repr=False)
    employed: T.Dict[Skill, Contributor] = field(repr=False)
    end_date: int = np.inf
    start_date: int = 0

    @property
    def score(self) -> int:
        if self.end_date <= self.best_before:
            return self.max_score
        return max(0, self.end_date - self.best_before)

    def is_team_valid(self, contributors: T.Sequence[Contributor]) -> T.Dict[Skill, Contributor]:
        """Return the SUBSET of *contributors* that """
        return dict()


@dataclass
class Solution:
    project: Project
