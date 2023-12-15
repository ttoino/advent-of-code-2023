import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    patterns = [p.splitlines() for p in inf.read().strip().split("\n\n")]

    result = 0
    for p in patterns:
        for y in range(1, len(p)):
            above, below = p[:y], p[y:]
            minlength = min(len(above), len(below))
            
            if above[-minlength:] == below[:minlength][::-1]:
                result += 100 * len(above)
                break
        else: 
            p = list(zip(*p))
            for x in range(1, len(p)):
                left, right = p[:x], p[x:]
                minlength = min(len(left), len(right))
                if left[-minlength:] == right[:minlength][::-1]:
                    result += len(left)
                    break
            else:
                print("no match")

    outf.write(str(result))
