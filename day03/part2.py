import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, defaultdict

pattern = re.compile(r"\d+")

with open("input") as inf, open("part2.out", "w+") as outf:
    lines = inf.readlines()
    gears = defaultdict(set)

    for y, line in enumerate(lines):
        line = line.strip()
        for match in pattern.finditer(line):
            num = int(match.group())

            for x in range(max(0, match.start() - 1), min(match.end() + 1, len(line))):
                for yy in range(max(0, y - 1), min(y + 2, len(lines))):
                    if lines[yy][x] == "*":
                        gears[(x, yy)].add(num)

    result = sum(ft.reduce(op.mul, gear) for gear in gears.values() if len(gear) == 2)

    outf.write(str(result))
