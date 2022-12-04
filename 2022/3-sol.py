#!/usr/env python3
import sys


def p(c):
    return (ord(c) - ord("a") + 1) if c >= "a" else (ord(c) - ord("A") + 27)


res = 0
with open(sys.argv[1]) as f:
    g = []
    for line in f:
        line = line.strip()
        g.append(set(line))
        if len(g) == 3:
            c = g[0] & g[1] & g[2]
            c = c.pop()
            res += p(c)
            g = []

        # c = set(line[: len(line) // 2]) & set(line[len(line) // 2 :])
        # c = c.pop()
        # res += p(c)

print(res)
