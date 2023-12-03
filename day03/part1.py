import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

pattern = re.compile(r"\d+")

with open("input") as inf, open("part1.out", "w+") as outf:
    lines = inf.readlines()
    result = 0

    for y, line in enumerate(lines):
        line = line.strip()
        for match in pattern.finditer(line):
            num = int(match.group())
            part = False

            for x in range(max(0, match.start() - 1), min(match.end() + 1, len(line))):
                for yy in range(max(0, y - 1), min(y + 2, len(lines))):
                    part = part or (not lines[yy][x].isdigit() and lines[yy][x] != ".")

            if part:
                result += num

    outf.write(str(result))