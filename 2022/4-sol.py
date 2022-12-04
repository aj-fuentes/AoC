#!/usr/env python3
import sys


def intersect(a, b):
    if b < a:
        a, b = b, a
    if a[1] < b[0]:
        return None
    # a[0]  b[0] a[1]
    if b[1] <= a[1]:
        return b
    return (b[0], a[1])


res = 0
with open(sys.argv[1]) as f:
    for line in f:
        a, b = [tuple(map(int, x.split("-"))) for x in line.strip().split(",")]
        # if intersect(a, b) in [a, b]:
        #     res += 1
        if intersect(a, b) is not None:
            res += 1

print(res)
