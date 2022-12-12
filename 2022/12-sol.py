#!/usr/env python3
import heapq
import sys

t = []
with open(sys.argv[1]) as f:
    for i, line in enumerate(f):
        t.append([])
        for j, c in enumerate(line.strip("\n")):
            if c == "S":
                start = (i, j)
                c = "a"
            elif c == "E":
                end = (i, j)
                c = "z"
            t[-1].append(ord(c) - ord("a"))


seen = set()
togo = [(0, end)]
N = len(t)
M = len(t[0])
x = [[chr(ord("a") + t[i][j]) for j in range(M)] for i in range(N)]
res = float("inf")
while togo:
    s, (i, j) = heapq.heappop(togo)
    for i0, j0 in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
        if 0 <= i0 < N and 0 <= j0 < M:
            if t[i0][j0] - t[i][j] < -1:
                continue
            if t[i0][j0] == 0:
                res = min(res, s + 1)
            if (i0, j0) in seen:
                continue
            x[i0][j0] = "#"
            seen.add((i0, j0))
            heapq.heappush(togo, (s + 1, (i0, j0)))

print(res)
