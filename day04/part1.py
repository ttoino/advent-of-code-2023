import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    result = 0

    for line in inf:
        line = line.split(':')[1].strip()

        mine, winning = line.split('|')
        mine = set(map(int, mine.split()))
        winning = set(map(int, winning.split()))

        if len(mine & winning) != 0:
            result += 2**(len(mine & winning) - 1)

    outf.write(str(result))
