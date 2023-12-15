import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    codes = inf.readline().strip().split(",")

    result = 0
    for code in codes:
        hash = 0
        for char in code:
            hash += ord(char)
            hash *= 17
            hash %= 256
        result += hash
    
    outf.write(str(result))
