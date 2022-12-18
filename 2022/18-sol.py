#!/usr/env python3
import collections
import sys

ps = []
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip("\n")
        ps.append(tuple(map(int, line.split(","))))


def outside(ps):
    X, Y, Z = ((min(p[i] for p in ps) - 1, max(p[i] for p in ps) + 1) for i in range(3))

    seen = set(ps)
    togo = [(X[0], Y[0], Z[0])]
    while togo:
        x, y, z = togo.pop()
        for x0, y0, z0 in [
            (x + 1, y, z),
            (x - 1, y, z),
            (x, y + 1, z),
            (x, y - 1, z),
            (x, y, z + 1),
            (x, y, z - 1),
        ]:
            if (
                X[0] <= x0 <= X[1]
                and Y[0] <= y0 <= Y[1]
                and Z[0] <= z0 <= Z[1]
                and (x0, y0, z0) not in seen
            ):
                seen.add((x0, y0, z0))
                togo.append((x0, y0, z0))
    return seen - set(ps)


def faces(p):
    (x, y, z) = p
    return [
        [(x, y, z), (x + 1, y, z), (x + 1, y + 1, z), (x, y + 1, z)],
        [(x, y, z), (x + 1, y, z), (x + 1, y, z + 1), (x, y, z + 1)],
        [(x, y, z), (x, y + 1, z), (x, y + 1, z + 1), (x, y, z + 1)],
        [(x + 1, y + 1, z + 1), (x, y + 1, z + 1), (x, y, z + 1), (x + 1, y, z + 1)],
        [(x + 1, y + 1, z + 1), (x, y + 1, z + 1), (x, y + 1, z), (x + 1, y + 1, z)],
        [(x + 1, y + 1, z + 1), (x + 1, y, z + 1), (x + 1, y, z), (x + 1, y + 1, z)],
    ]


seen = collections.Counter(tuple(sorted(f)) for p in ps for f in faces(p))
res = sum(c == 1 for _, c in seen.items())
print(res)

qs = outside(ps)
qseen = collections.Counter(tuple(sorted(f)) for p in qs for f in faces(p))
res = sum(c == 1 and qseen.get(f, 0) == 1 for f, c in seen.items())
print(res)
