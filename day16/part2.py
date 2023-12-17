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

with open("input") as inf, open("part2.out", "w+") as outf:
    mirrors = [line.strip() for line in inf.readlines()]

    solutions = {}

    def solve(start):
        if start in solutions:
            return

        visited = set()
        beams = [start]
        ends = {start}

        while len(beams) > 0:
            beam = beams.pop()
            (beam_x, beam_y), beam_dir = beam

            if beam in visited:
                continue

            if beam_x < 0:
                ends.add(((0, beam_y), (-beam_dir[0], -beam_dir[1])))
                continue
            elif beam_x >= len(mirrors[0]):
                ends.add(((len(mirrors[0]) - 1, beam_y), (-beam_dir[0], -beam_dir[1])))
                continue
            elif beam_y < 0:
                ends.add(((beam_x, 0), (-beam_dir[0], -beam_dir[1])))
                continue
            elif beam_y >= len(mirrors):
                ends.add((beam_x, (len(mirrors) - 1), (-beam_dir[0], -beam_dir[1])))
                continue

            visited.add(beam)

            mirror = mirrors[beam_y][beam_x]
            beam_dirs = mirror_map[mirror][beam_dir]
            beams += [((beam_x + d[0], beam_y + d[1]), d) for d in beam_dirs]

        solution = len({v[0] for v in visited})
        for e in ends:
            solutions[e] = solution
    
    for x in range(len(mirrors[0])):
        solve(((x, 0), (0, 1)))
        solve(((x, len(mirrors) - 1), (0, -1)))
    for y in range(len(mirrors[0])):
        solve(((0, y), (1, 0)))
        solve(((len(mirrors[0]) - 1, y), (-1, 0)))

    outf.write(str(max(solutions.values())))
