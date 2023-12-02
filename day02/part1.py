import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

maxs = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

with open("input") as inf, open("part1.out", "w+") as outf:
    result = 0

    for line in inf:
        id, results = line.strip().split(': ')
        id = int(id.split(' ')[1])

        possible = True

        for r in results.split('; '):
            for rr in r.split(', '):
                count, color = rr.split(' ')

                if int(count) > maxs[color]:
                    possible = False

        if possible:
            result += id

    outf.write(str(result))
