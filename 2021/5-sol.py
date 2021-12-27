import sys
from itertools import chain, starmap


def read_segs(f):
    for line in f:
        yield tuple(map(int, line.strip().replace(" -> ", ",").split(",")))


def get_points(x1, y1, x2, y2):
    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        for y in range(y1, y2 + 1):
            yield x1, y
    elif y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        for x in range(x1, x2 + 1):
            yield x, y1
    else:
        yield x1, y1
        x, y = x1, y1
        dx = 1 if x1 < x2 else -1
        dy = 1 if y1 < y2 else -1
        while x != x2 or y != y2:
            x += dx
            y += dy
            yield x, y


def count_points(segs):
    onep = set()
    twop = set()
    for p in chain.from_iterable(starmap(get_points, segs)):
        if p in twop:
            continue
        if p in onep:
            twop.add(p)
            onep.remove(p)
        else:
            onep.add(p)
    return len(twop)


with open(sys.argv[1], "rt") as f:
    segs = list(read_segs(f))

c = count_points(segs)
print(c)
