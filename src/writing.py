import typing as T
import pathlib
from loguru import logger
from src.data import Project


def write_str(projects: T.Sequence[Project], verbose: bool = False) -> str:
    """Assumes all projects have been finished!"""

    txt: str = ""
    txt += f"{len(projects)}\n"
    for p in projects:
        txt += f"{p.name}\n"
        txt += ' '.join([x.name for x in p.employed.values()])
        txt += '\n'
    if verbose:
        logger.info(txt)
    return txt


def write_file(s, p: pathlib.Path) -> None:
    with open(str(p), 'w') as fp:
        fp.write(s)


if __name__ == "__main__":
    pass
