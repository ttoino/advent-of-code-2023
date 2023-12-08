import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter
from math import lcm

pattern = re.compile(r"(\w{3}) = \((\w{3}), (\w{3})\)")

with open("input") as inf, open("part2.out", "w+") as outf:
    instructions, nodes = inf.read().split("\n\n")

    nodes = {
        (r := pattern.match(n)).group(1): {
            "L": r.group(2),
            "R": r.group(3)
        }
        for n in nodes.splitlines()
    }

    current_nodes = [k for k in nodes.keys() if k[-1] == "A"]
    times = []

    for current_node in current_nodes:
        for i, direction in enumerate(it.cycle(instructions)):
            if current_node[-1] == "Z":
                times.append(i)
                break

            current_node = nodes[current_node][direction]

    outf.write(str(lcm(*times)))
