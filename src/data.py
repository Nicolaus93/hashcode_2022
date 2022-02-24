import typing as T
from dataclasses import dataclass,field

@dataclass(frozen=True,eq=True)
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
    employed:T.Dict[Skill,Contributor] =  field(default_factory=dict)

@dataclass
class Solution:
    project:Project

