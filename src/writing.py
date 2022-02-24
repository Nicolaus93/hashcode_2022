import typing as T
import pathlib
from loguru import logger
from collections import OrderedDict
import pandas as pd

from constants import CURRENT_CASE, A_CASE
from src.data import Project, Skill, Contributor


def write_str(projects: T.Sequence[Project]) -> str:
    """Assumes all projects have been finished!"""

    txt: str = ""
    txt += f"{len(projects)}\n"
    for p in projects:
        txt += f"{p.name}\n"
        txt += ' '.join([x.name for x in p.employed.values()])
        txt += '\n'
    logger.info(txt)
    return txt


def write_file(s, p: pathlib.Path) -> None:
    with open(str(p), 'w') as fp:
        fp.write(s)


if __name__ == "__main__":
    pass
