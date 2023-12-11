import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    universe = [line.strip() for line in inf.readlines()]

    expanded_universe = []
    for line in universe:
        if all(c == "." for c in line):
            expanded_universe.append(line)
        expanded_universe.append(line)
    
    universe = zip(*expanded_universe)

    expanded_universe = []
    for line in universe:
        if all(c == "." for c in line):
            expanded_universe.append(line)
        expanded_universe.append(line)
    
    galaxies = set()

    for i, l in enumerate(expanded_universe):
        for j, c in enumerate(l):
            if c == "#":
                galaxies.add((i, j))
    
    result = 0
    for g1, g2 in it.combinations(galaxies, 2):
        result += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

    outf.write(str(result))
