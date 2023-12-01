import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

with open("input") as inf, open("part1.out", "w+") as outf:
    outf.write(
        str(
            sum(
                map(
                    lambda l: int((r := list(filter(lambda s: s.isdigit(), l)))
                                  [0] + r[-1]), inf.readlines()))))
