#!/usr/env python3
import sys

e = {"A": 1, "B": 2, "C": 3}
d = {"X": 1, "Y": 2, "Z": 3}

table = {
    "A X": 3 + 1,
    "B X": 0 + 1,
    "C X": 6 + 1,
    "A Y": 6 + 2,
    "B Y": 3 + 2,
    "C Y": 0 + 2,
    "A Z": 0 + 3,
    "B Z": 6 + 3,
    "C Z": 3 + 3,
}
table2 = {
    "A X": 3 + 0,
    "B X": 1 + 0,
    "C X": 2 + 0,
    "A Y": 1 + 3,
    "B Y": 2 + 3,
    "C Y": 3 + 3,
    "A Z": 2 + 6,
    "B Z": 3 + 6,
    "C Z": 1 + 6,
}


res = 0
with open(sys.argv[1]) as f:
    for line in f:
        res += table2[line.strip()]

print(res)
