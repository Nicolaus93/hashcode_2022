import numpy as np
import pandas as pd


def read_input(input_file):
    with open(input_file) as f:
        for line in f:
            print(line)


def greedy(projects, contributors):
    return


def score(solution) -> int:
    last_day = 0
    project = solution.project
    for skill, person in solution.employed.items():
        last_day = max(last_day, person.time + project.duration)

    how_much_late = max(0, last_day - project.best_before)
    return max(0, project.score - how_much_late)


if __name__ == '__main__':
    read_input("/home/nico/hashcode_2022/data/a_an_example.in.txt")

