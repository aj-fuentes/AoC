#!/usr/env python3
import sys

tab = []
with open(sys.argv[1]) as f:
    for line in f:
        tab.append(list(map(int, line.strip("\n"))))

vis = set()
N = len(tab)
M = len(tab[0])
for i in range(N):
    m = -1
    for j in range(M):
        if m < tab[i][j]:
            vis.add((i, j))
            m = tab[i][j]
    m = -1
    for j in range(M - 1, -1, -1):
        if m < tab[i][j]:
            vis.add((i, j))
            m = tab[i][j]

for j in range(M):
    m = -1
    for i in range(N):
        if m < tab[i][j]:
            vis.add((i, j))
            m = tab[i][j]
    m = -1
    for i in range(N - 1, -1, -1):
        if m < tab[i][j]:
            vis.add((i, j))
            m = tab[i][j]

res = 0
for i in range(1, N - 1):
    for j in range(1, M - 1):
        m = tab[i][j]
        c = 0
        for k in range(i - 1, -1, -1):
            c += 1
            if tab[k][j] >= m:
                break
        t, c = c, 0
        for k in range(i + 1, N):
            c += 1
            if tab[k][j] >= m:
                break
        t, c = t * c, 0
        for k in range(j - 1, -1, -1):
            c += 1
            if tab[i][k] >= m:
                break
        t, c = t * c, 0
        for k in range(j + 1, M):
            c += 1
            if tab[i][k] >= m:
                break
        t *= c
        res = max(res, t)


print(len(vis))
print(res)
