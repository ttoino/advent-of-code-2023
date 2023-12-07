import itertools as it
import more_itertools as mit
import functools as ft
import operator as op
import re
from collections import Counter

mapping = {
    "J": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "Q": 12,
    "K": 13,
    "A": 14
}


def score(line):
    hand, _ = line.split()

    hand_without_jokers = hand.replace("J", "")

    counts = Counter(hand_without_jokers)
    counts = sorted(counts.values(), reverse=True)

    best = (counts[0] if len(counts) > 0 else 0) + hand.count("J")
    second = counts[1] if len(counts) > 1 else 0

    hand = [mapping[x] for x in hand]

    return (best, second, *hand)


with open("input") as inf, open("part2.out", "w+") as outf:
    outf.write(
        str(
            sum(
                map(lambda x: int(x[1].split()[1]) * (x[0] + 1),
                    enumerate(sorted(
                        inf.readlines(),
                        key=score,
                    ))))))
