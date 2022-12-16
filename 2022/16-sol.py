#!/usr/env python3
import collections
import sys

g = collections.defaultdict(list)
rs = {}
with open(sys.argv[1]) as f:
    for line in f:
        parts = line.strip("\n").split(";")
        p = parts[0].split()
        a = p[1]
        rs[a] = int(p[-1].split("=")[-1])
        p = parts[1].split()
        p.reverse()
        for b in p:
            if b.startswith("valve"):
                break
            g[a].append(b.replace(",", ""))
        g[a].reverse()


def paths():
    def levels(n):
        missing = set(g.keys())
        missing.remove(n)
        ls = [{n}]
        while missing:
            ls.append(set(y for x in ls[-1] for y in g[x] if y in missing))
            missing -= ls[-1]
        return ls

    return {
        (x, y): k for x in g for (k, l) in enumerate(levels(x)[1:], start=1) for y in l
    }


ps = paths()

#              D20 - E3 - F0
#            /     \      |
#         A0 - B13 - C2   G0
#          |              |
#         I0 - J21        H22


res = 0
T = 30


def estimate(n, t, f, seen):
    global T
    missing = set(g.keys()) - seen
    vals = map(rs.get, missing)
    for v in sorted(vals, reverse=True):
        if t + 2 >= T:
            break
        t += 2
        f += (T - t) * v

    return f


cache = {}


def backtrack(n, t, f, seen):
    global res, T, cache
    kk = tuple(sorted(seen))
    if n == "AA" and kk in cache:
        res = cache[kk]
        return
    if t >= T:
        return
    t += 1
    f += (T - t) * rs[n]
    if f > res:
        res = f

    if estimate(n, t, f, seen) < res:
        return
    for m in g.keys():
        if m in seen:
            continue
        if m == n:
            continue
        backtrack(m, t + ps[(n, m)], f, seen | {n})


# backtrack("AA", -1, 0, set())
T = 26


def conf(S0, S1):
    global res
    res = 0
    backtrack("AA", -1, 0, S0)
    res0 = res
    res = 0
    backtrack("AA", -1, 0, S1)
    res1 = res
    return res0 + res1


best = 0


def backtrack2(S0, S1):
    global best
    if not S0:
        return
    v, x = max((conf(S0 - {x}, S1 | {x}), x) for x in S0)
    if v > best:
        best = v
        print(best)
    backtrack2(S0 - {x}, S1 | {x})


backtrack2(set(g.keys()), set())
print(best)
