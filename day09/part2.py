import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part2.out", "w+") as outf:
    result = 0

    for l in inf.readlines():
        l = [int(x) for x in l.strip().split()]
        ll = [l]

        while not all(x == 0 for x in ll[-1]):
            ll.append([y - x for x, y in it.pairwise(ll[-1])])
        
        prev = ll[-1][0]

        for l in ll[::-1]:
            prev = l[0] - prev
        
        result += prev
        
    outf.write(str(result))
