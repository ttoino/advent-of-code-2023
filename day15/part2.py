import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

def hash(code):
    result = 0
    for char in code:
        result += ord(char)
        result *= 17
        result %= 256
    return result

with open("input") as inf, open("part2.out", "w+") as outf:
    codes = inf.readline().strip().split(",")

    hashmap = tuple({} for _ in range(256))
    for code in codes:
        if code[-1] == '-':
            hashmap[hash(code[:-1])].pop(code[:-1], None)
        else:
            hashmap[hash(code[:-2])][code[:-2]] = int(code[-1])

    result = 0
    for i, hashmap in enumerate(hashmap):
        for j, (code, value) in enumerate(list(hashmap.items())):
            print(f"{i} {j} {code} {value}")
            result += (i + 1) * (j + 1) * value
    
    outf.write(str(result))
