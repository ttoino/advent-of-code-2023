import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

pattern = re.compile(
    r".*?(\d|one|two|three|four|five|six|seven|eight|nine)(?:.*(\d|one|two|three|four|five|six|seven|eight|nine))?.*?"
)

digit_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9'
}

with open("input") as inf, open("part2.out", "w+") as outf:
    outf.write(
        str(
            sum(
                map(
                    lambda l: int(digit_dict[
                        (r := pattern.match(l))[1]] + digit_dict[r[2] or r[1]]),
                    inf.readlines()))))
