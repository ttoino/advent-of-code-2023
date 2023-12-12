import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    result = 0

    for line in inf.readlines():
        springs, groups = line.split(" ")
        groups = list(map(int, groups.split(",")))
        unknown = springs.count("?")

        for replacements in tuple(it.product(*((".#",)*unknown))):
            replaced = springs
            for replacement in replacements:
                replaced = replaced.replace("?", replacement, 1)
            
            new_groups = []
            count = 0
            for s in replaced:
                if s == ".":
                    if count > 0:
                        new_groups.append(count)
                    count = 0
                else:
                    count += 1
            if count > 0:
                new_groups.append(count)
            
            if groups == new_groups:
                result += 1
            
    outf.write(str(result))
