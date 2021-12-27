import sys
from itertools import permutations, product


def read():
    ss = []
    with open(sys.argv[1], "rt") as f:
        bs = []
        for line in f:
            line = line.strip()
            if not line:
                ss.append(bs)
                bs = []
                continue
            if line.startswith("---"):
                continue
            bs.append(tuple(map(int, line.split(","))))
        ss.append(bs)
    return ss


def dist(bi, bj):
    return sum((vi - vj) ** 2 for vi, vj in zip(bi, bj))


ss = read()
info = [{i: set(dist(bi, bj) for bj in bs) for i, bi in enumerate(bs)} for bs in ss]


def intersect(info0, info1):
    # list o pairs, (i,j) means beacon i is the same as beacon j
    same = [
        (i, j)
        for i, dsi in info0.items()
        for j, dsj in info1.items()
        if len(dsi & dsj) >= 12
    ]
    return same


def coords(i, j, same):
    # return coordinate of scanner j w.r.t i
    for per in permutations([0, 1, 2]):
        for sig in product((-1, 1), (-1, 1), (-1, 1)):
            coords = set()
            for pair in same:
                bi = ss[i][pair[0]]
                bj = ss[j][pair[1]]
                cc = tuple(bi[k] - sig[k] * bj[per[k]] for k in range(3))
                coords.add(cc)
            if len(coords) == 1:
                cc = coords.pop()
                return cc, sig, per


def invp(p):
    return [p.index(k) for k in range(len(p))]


def mulp(p, q):
    return [p[k] for k in q]


for p in permutations([0, 1, 2]):
    assert mulp(invp(p), p) == [0, 1, 2]
    assert mulp(p, invp(p)) == [0, 1, 2]
    assert mulp(p, [0, 1, 2]) == list(p)


def all_coords():
    known = {0: (0, 0, 0)}
    while len(known) < len(ss):
        missing = set(range(len(ss))) - set(known.keys())
        i, j = next(
            (i0, j0)
            for i0 in known
            for j0 in missing
            if len(intersect(info[i0], info[j0])) >= 12
        )
        same = intersect(info[i], info[j])
        rc, rsig, rper = coords(i, j, same)
        ic = known[i]
        jc = tuple(ic[k] + rc[k] for k in range(3))
        known[j] = jc

        # update beacons
        ss[j] = [tuple(rsig[k] * b[rper[k]] for k in range(3)) for b in ss[j]]

    return known


# same = intersect(info[1], info[4])
# print(same)
# print(coords(1, 4, same))
ac = all_coords()
m = 0
for c0 in ac.values():
    for c1 in ac.values():
        m = max(sum(abs(x - y) for x, y in zip(c0, c1)), m)
# tv = [
#     (0, 0, 0),
#     (68, -1246, -43),
#     (1105, -1205, 1229),
#     (-92, -2380, -20),
#     (-20, -1133, 1061),
# ]
# for i in range(len(ac)):
#     print(ac[i], tv[i], ac[i] == tv[i])
#     assert ac[i][0] == tv[i], "breaks center"

true_bs = [
    (-892, 524, 684),
    (-876, 649, 763),
    (-838, 591, 734),
    (-789, 900, -551),
    (-739, -1745, 668),
    (-706, -3180, -659),
    (-697, -3072, -689),
    (-689, 845, -530),
    (-687, -1600, 576),
    (-661, -816, -575),
    (-654, -3158, -753),
    (-635, -1737, 486),
    (-631, -672, 1502),
    (-624, -1620, 1868),
    (-620, -3212, 371),
    (-618, -824, -621),
    (-612, -1695, 1788),
    (-601, -1648, -643),
    (-584, 868, -557),
    (-537, -823, -458),
    (-532, -1715, 1894),
    (-518, -1681, -600),
    (-499, -1607, -770),
    (-485, -357, 347),
    (-470, -3283, 303),
    (-456, -621, 1527),
    (-447, -329, 318),
    (-430, -3130, 366),
    (-413, -627, 1469),
    (-345, -311, 381),
    (-36, -1284, 1171),
    (-27, -1108, -65),
    (7, -33, -71),
    (12, -2351, -103),
    (26, -1119, 1091),
    (346, -2985, 342),
    (366, -3059, 397),
    (377, -2827, 367),
    (390, -675, -793),
    (396, -1931, -563),
    (404, -588, -901),
    (408, -1815, 803),
    (423, -701, 434),
    (432, -2009, 850),
    (443, 580, 662),
    (455, 729, 728),
    (456, -540, 1869),
    (459, -707, 401),
    (465, -695, 1988),
    (474, 580, 667),
    (496, -1584, 1900),
    (497, -1838, -617),
    (527, -524, 1933),
    (528, -643, 409),
    (534, -1912, 768),
    (544, -627, -890),
    (553, 345, -567),
    (564, 392, -477),
    (568, -2007, -577),
    (605, -1665, 1952),
    (612, -1593, 1893),
    (630, 319, -379),
    (686, -3108, -505),
    (776, -3184, -501),
    (846, -3110, -434),
    (1135, -1161, 1235),
    (1243, -1093, 1063),
    (1660, -552, 429),
    (1693, -557, 386),
    (1735, -437, 1738),
    (1749, -1800, 1813),
    (1772, -405, 1572),
    (1776, -675, 371),
    (1779, -442, 1789),
    (1780, -1548, 337),
    (1786, -1538, 337),
    (1847, -1591, 415),
    (1889, -1729, 1762),
    (1994, -1805, 1792),
]
true_bs.sort()

ab = set()
for i in range(len(ac)):
    ci = ac[i]
    for b in ss[i]:
        bi = tuple(ci[k] + b[k] for k in range(3))
        ab.add(bi)
ab = list(sorted(ab))
# for bi, tvbi in zip(ab, true_bs):
#     print(bi, tvbi, bi == tvbi)
print(len(ab), m)
