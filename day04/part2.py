import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, defaultdict

with open("input") as inf, open("part2.out", "w+") as outf:
    counter = defaultdict(lambda: 1)

    for i, line in enumerate(inf):
        line = line.split(':')[1].strip()

        mine, winning = line.split('|')
        mine = set(map(int, mine.split()))
        winning = set(map(int, winning.split()))

        counter[i]
        for j in range(1, len(mine & winning) + 1):
            counter[i + j] += counter[i]

    outf.write(str(sum(counter.values())))
