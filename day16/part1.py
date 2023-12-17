import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

mirror_map = {
    '.': {
        (1, 0): [(1, 0)],
        (-1, 0): [(-1, 0)],
        (0, 1): [(0, 1)],
        (0, -1): [(0, -1)]
    },
    '/': {
        (1, 0): [(0, -1)],
        (0, -1): [(1, 0)],
        (-1, 0): [(0, 1)],
        (0, 1): [(-1, 0)]
    },
    '\\': {
        (1, 0): [(0, 1)],
        (0, 1): [(1, 0)],
        (-1, 0): [(0, -1)],
        (0, -1): [(-1, 0)]
    },
    '-': {
        (1, 0): [(1, 0)],
        (-1, 0): [(-1, 0)],
        (0, 1): [(1, 0), (-1, 0)],
        (0, -1): [(1, 0), (-1, 0)]
    },
    '|': {
        (0, 1): [(0, 1)],
        (0, -1): [(0, -1)],
        (1, 0): [(0, 1), (0, -1)],
        (-1, 0): [(0, 1), (0, -1)]
    }
}

with open("input") as inf, open("part1.out", "w+") as outf:
    mirrors = [line.strip() for line in inf.readlines()]

    visited = set()
    beams = [((0, 0), (1, 0))]

    while len(beams) > 0:
        beam = beams.pop()
        (beam_x, beam_y), beam_dir = beam

        if beam in visited or beam_x < 0 or beam_x >= len(
                mirrors[0]) or beam_y < 0 or beam_y >= len(mirrors):
            continue

        visited.add(beam)

        mirror = mirrors[beam_y][beam_x]
        beam_dirs = mirror_map[mirror][beam_dir]
        beams += [((beam_x + d[0], beam_y + d[1]), d) for d in beam_dirs]

    outf.write(str(len({v[0] for v in visited})))
