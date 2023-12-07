import itertools as it
from math import ceil, floor, sqrt
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    time = int("".join(inf.readline().strip().split()[1:]))
    distance = int("".join(inf.readline().strip().split()[1:]))

    delta = time * time - 4 * distance
    zeros = (time - sqrt(delta)) / 2, (time + sqrt(delta)) / 2

    result = floor(zeros[1] - 0.01) - ceil(zeros[0] + 0.01) + 1
    
    print(result, file=outf)
