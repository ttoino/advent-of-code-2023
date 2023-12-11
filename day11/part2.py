import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    universe = [line.strip() for line in inf.readlines()]

    expanded_rows = []
    for i, line in enumerate(universe):
        if all(c == "." for c in line):
            expanded_rows.append(i)
    

    expanded_cols = []
    for i, line in enumerate(zip(*universe)):
        if all(c == "." for c in line):
            expanded_cols.append(i)
    
    galaxies = set()
    for i, l in enumerate(universe):
        for j, c in enumerate(l):
            if c == "#":
                galaxies.add((i, j))
    
    result = 0
    expansion = 1000000
    for (g1_i, g1_j), (g2_i, g2_j) in it.combinations(galaxies, 2):
        for i in range(min(g1_i, g2_i) + 1, max(g1_i, g2_i) + 1):
            result += expansion if i in expanded_rows else 1
        for j in range(min(g1_j, g2_j) + 1, max(g1_j, g2_j) + 1):
            result += expansion if j in expanded_cols else 1

    outf.write(str(result))