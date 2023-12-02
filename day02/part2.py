import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    result = 0

    for line in inf:
        results = line.strip().split(': ')[1]

        counts = {"red": 0, "green": 0, "blue": 0}

        for r in results.split('; '):
            for rr in r.split(', '):
                count, color = rr.split(' ')
                counts[color] = max(int(count), counts[color])

        result += counts["red"] * counts["green"] * counts["blue"]

    outf.write(str(result))
