import typing as T
from dataclasses import dataclass

@dataclass
class Skill:
    name:str


@dataclass
class Contributor:
    name:str
    skills:T.Dict[Skill,int]


@dataclass
class Project:
    name:str
    best_before: int
    score: int
    skills: T.Dict[Skill, int]

@dataclass
class Solution:
    project:Project
    employed:T.Dict[Skill,Contributor]

