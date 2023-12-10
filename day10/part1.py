import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

dir_map = {
    "|": {(0, 1), (0, -1)},
    "-": {(1, 0), (-1, 0)},
    "L": {(1, 0), (0, -1)},
    "J": {(-1, 0), (0, -1)},
    "7": {(-1, 0), (0, 1)},
    "F": {(1, 0), (0, 1)},
    ".": set(),
}

dirs = {(0, 1), (0, -1), (1, 0), (-1, 0)}

with open("input") as inf, open("part1.out", "w+") as outf:
    pipemap = [line.strip() for line in inf]

    start_y, _ = [l for l in enumerate(pipemap) if "S" in l[1]][0]
    start_x = pipemap[start_y].index("S")

    start_dirs = set()
    for (dir_x, dir_y) in dirs:
        x = start_x + dir_x
        y = start_y + dir_y
        reverse_dir = (-dir_x, -dir_y)

        if reverse_dir in dir_map[pipemap[y][x]]:
            start_dirs.add((dir_x, dir_y))
    
    start_char = [k for k, v in dir_map.items() if start_dirs == v][0]
    pipemap[start_y] = pipemap[start_y][:start_x] + start_char + pipemap[start_y][start_x + 1:]

    length = 0

    x, y = (start_x, start_y)
    prev_dir = (0, 0)

    while True:
        length += 1

        dir = (dir_map[pipemap[y][x]] - {(-prev_dir[0], -prev_dir[1])}).pop()
        
        x += dir[0]
        y += dir[1]

        prev_dir = dir

        if (x, y) == (start_x, start_y):
            break

    outf.write(str(length//2))
