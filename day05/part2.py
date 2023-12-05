import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    i = inf.read().split('\n\n')

    seedRanges = list(map(tuple, mit.chunked(map(int, i[0].split(':')[1].split()), 2)))
    nextRanges = []

    for m in i[1:]:
        while len(seedRanges) > 0:
            sstart, slength = seedRanges.pop(0)

            for l in m.strip().split('\n')[1:]:
                vstart, kstart, length = tuple(map(int, l.split()))

                if sstart + slength <= kstart or kstart + length <= sstart:
                    continue

                if kstart <= sstart and sstart + slength <= kstart + length:
                    nextRanges.append((vstart + sstart - kstart, slength))
                    break

                if kstart <= sstart:
                    nlength = kstart + length - sstart
                    nextRanges.append((vstart + sstart - kstart, nlength))
                    seedRanges.insert(0, (sstart + nlength, slength - nlength))
                    break

                nlength = sstart + slength - kstart
                nextRanges.append((vstart - kstart + (sstart + slength - nlength), nlength))
                seedRanges.insert(0, (sstart, slength - nlength))
                break

            else:
                nextRanges.append((sstart, slength))
        
        seedRanges = nextRanges
        nextRanges = []

    outf.write(str(min(map(lambda x: x[0], seedRanges))))
