import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

xmas = {'x': 0, 'm': 1, 'a': 2, 's': 3}
ops = {'<': op.lt, '>': op.gt}

with open("input") as inf, open("part1.out", "w+") as outf:
    rules, parts = inf.read().split("\n\n")

    rules = {
        l[:l.index('{')]: [
            r if ':' not in r else (xmas[r[0]], ops[r[1]], int(r[2:r.index(':')]), r[r.index(':') + 1:])
            for r in l[l.index('{') + 1:l.index('}')].split(',')
        ]
        for l in rules.splitlines()
    }
    parts = {tuple(int(n.split('=')[1]) for n in part[1:-1].split(','))
             for part in parts.splitlines()}

    result = 0

    for part in parts:
        print(part, end=': ')
        current = "in"

        while current not in 'AR':
            print(current, end=' -> ')
            for rule in rules[current]:
                if isinstance(rule, str):
                    current = rule
                    break

                elif rule[1](part[rule[0]], rule[2]):
                    current = rule[3]
                    break

        print(current)
        if current == 'A':
            result += sum(part)
    
    outf.write(str(result))
