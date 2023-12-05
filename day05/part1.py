import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter, defaultdict

with open("input") as inf, open("part1.out", "w+") as outf:
    i = inf.read().split('\n\n')

    seeds = list(map(int, i[0].split(':')[1].split()))

    for m in i[1:]:
        for i, seed in enumerate(seeds):
            for l in m.strip().split('\n')[1:]:
                startvalue, startkey, length = tuple(map(int, l.split()))

                if startkey <= seed < startkey + length:
                    seeds[i] = startvalue + seed - startkey
                    break

    outf.write(str(min(seeds)))

