#!/usr/env python3
import collections
import re
import sys

# Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
pat = re.compile(
    r"Blueprint \d+: Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."
)

# [ore, clay, obs, geo]
bps = []

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip("\n")
        v = list(map(int, re.match(pat, line).group(1, 2, 3, 4, 5, 6)))
        bps.append(((v[0], 0, 0), (v[1], 0, 0), (v[2], v[3], 0), (v[4], 0, v[5])))


def skip_robot(bp, robots, i):
    conds = [
        robots[0] >= max(bp[1][0], bp[2][0], bp[3][0]),
        robots[1] >= bp[2][1],
        robots[2] >= bp[3][2],
    ]
    if 0 <= i <= 2:
        return conds[i]
    if i == -1:
        return all(conds)
    return False


# NN = 25
NN = 33


def search(bp, t, v, resources, robots):
    global cache, best
    if t == NN:
        return
    if v > best:
        best = v
    k = (v, resources[2], resources[1], resources[0])
    if any(all(r0 >= r for (r0, r) in zip(k0, k)) for k0 in cache[t][robots]):
        return
    ll = cache[t][robots]
    ll.append(k)
    ll.sort(reverse=True)

    ore, cla, obs = resources
    for i in [0, 1, 2, 3, -1]:
        if skip_robot(bp, robots, i):
            continue
        core, ccla, cobs = bp[i] if i != -1 else (0, 0, 0)
        if ore >= core and cla >= ccla and obs >= cobs:
            search(
                bp,
                t + 1,
                v + robots[3],
                (
                    ore - core + robots[0],
                    cla - ccla + robots[1],
                    obs - cobs + robots[2],
                ),
                tuple(robots[j] + (i == j) for j in range(4)),
            )


res = 1
for i, bp in enumerate(bps[:3], start=1):
    cache = collections.defaultdict(lambda: collections.defaultdict(list))
    best = 0
    search(bp, 0, 0, (0, 0, 0), (1, 0, 0, 0))
    # res += best * i
    res *= best
print(res)
