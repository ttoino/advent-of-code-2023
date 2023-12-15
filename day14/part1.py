import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    rocks = [line.strip() for line in inf]

    for y, line in enumerate(rocks):
        for x, rock in enumerate(line):
            if rock != "O":
                continue

            new_y = y

            while new_y > 0 and rocks[new_y - 1][x] == ".":
                new_y -= 1
            
            rocks[y] = rocks[y][:x] + "." + rocks[y][x + 1:]
            rocks[new_y] = rocks[new_y][:x] + "O" + rocks[new_y][x + 1:]
    
    result = 0
    for i, line in enumerate(rocks[::-1]):
        result += line.count("O") * (i + 1)
    
    outf.write(str(result))
