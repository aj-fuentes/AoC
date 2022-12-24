#!/usr/env python3
import collections
import heapq
import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()
    bs = {
        (i, j): [c]
        for (i, line) in enumerate(lines)
        for (j, c) in enumerate(line)
        if c in "><v^"
    }
    N = len(lines)
    M = len(lines[0].strip())

sta = (0, 1)
end = (N - 1, M - 2)


def gcd(a, b):
    a, b = (a, b) if a < b else (b, a)
    if a == b:
        return b
    return gcd(a, b - a)


def mcm(a, b):
    return a * b // gcd(a, b)


def build(N, M, bs):
    ts = []
    for _ in range(mcm(N - 2, M - 2)):
        ls = ["#." + "#" * (M - 2)]
        for i in range(1, N - 1):
            out = "#"
            for j in range(1, M - 1):
                cs = bs.get((i, j), ["."])
                out += cs[0] if len(cs) == 1 else str(len(cs))
            out += "#"
            ls.append(out)
        ls.append("#" * (M - 2) + "x#")
        ts.append(ls)
        bs = step(bs)
    return ts


def step(bs):
    global M, N

    dd = {">": (0, 1), "<": (0, -1), "v": (1, 0), "^": (-1, 0)}
    new_bs = collections.defaultdict(list)
    for (i, j), cs in bs.items():
        for c in cs:
            new_bs[
                ((i - 1 + dd[c][0]) % (N - 2) + 1, (j - 1 + dd[c][1]) % (M - 2) + 1)
            ].append(c)
    return new_bs


def show(pos, bs):
    global M, N
    print("#" + ("E" if pos == sta else ".") + "#" * (M - 2))
    for i in range(1, N - 1):
        out = "#"
        for j in range(1, M - 1):
            cs = bs.get((i, j), ["."])
            out += cs[0] if len(cs) == 1 else str(len(cs))
        out += "#"
        print(out)
    print("#" * (M - 2) + ("E" if pos == end else ".") + "#")


best = float("inf")


def search(pos, n, bs):
    global best
    new_bs = step(bs)
    i, j = pos
    if n >= best:
        return
    for (di, dj) in [(1, 0), (0, 1), (0, 0), (-1, 0), (0, -1)]:
        i0, j0 = i + di, j + dj
        if (i0, j0) == end:
            best = min(best, n + 1)
            return
        if (i0, j0) == sta or (
            0 < i0 < N - 1
            and 0 < j0 < M - 1
            and (
                i0,
                j0,
            )
            not in new_bs
        ):
            search(
                (i0, j0),
                n + 1,
                new_bs,
            )


def search2(n, ts):
    global sta, end

    def dist(a):
        return abs(a[0] - end[0]) + abs(a[1] - end[1])

    best = float("inf")
    togo = [(n, dist(sta), sta)]
    seen = set((n, sta[0], sta[1]))
    while togo:
        n, _, (i, j) = heapq.heappop(togo)
        if n >= best:
            continue
        ops = [(1, 0), (0, 1), (0, 0), (-1, 0), (0, -1)]
        if any((i + di, j + dj) == end for (di, dj) in ops):
            if n + 1 < best:
                best = n + 1
                print(best)
                continue
        for (di, dj) in ops:
            i0, j0 = i + di, j + dj
            if (i0, j0) == sta or (
                0 < i0 < N - 1
                and 0 < j0 < M - 1
                and ts[(n + 1) % len(ts)][i0][j0] == "."
            ):
                if ((n + 1) % len(ts), i0, j0) not in seen:
                    heapq.heappush(togo, (n + 1, dist((i0, j0)), (i0, j0)))
                    seen.add(((n + 1) % len(ts), i0, j0))
    return best


ts = build(N, M, bs)
# for i, t in enumerate(ts):
#     print(f"Minute {i}")
#     print("\n".join("".join(row) for row in t))
#     input()
# print(N - 2, M - 2)
# print(gcd(N - 2, M - 2))
# print(mcm(N - 2, M - 2))
# show(sta, bs)
# search2(bs)
# search(sta, 0, bs)
res = search2(0, ts)
sta, end = end, sta
res = search2(res, ts)
sta, end = end, sta
res = search2(res, ts)
print(res)
