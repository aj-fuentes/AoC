import sys
from heapq import heappop, heappush

b = []
f = open(sys.argv[1], "rt")
for line in f:
    r = list(map(int, line.strip()))
    b.append(list(r))
    for _ in range(4):
        r = [v % 9 + 1 for v in r]
        b[-1].extend(r)
m = len(b)
e = b
for _ in range(4):
    e = [[v % 9 + 1 for v in r] for r in e]
    b.extend(e)

h = [(0, 0, 0)]
m = set((0, 0))


def get_xy(i, j):
    for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
        if 0 <= x < len(b) and 0 <= y < len(b[0]):
            yield x, y


while True:
    c, i, j = heappop(h)
    if i == len(b) - 1 and j == len(b[0]) - 1:
        break
    for (x, y) in get_xy(i, j):
        if (x, y) in m:
            continue
        m.add((x, y))
        heappush(h, (c + b[x][y], x, y))


print(c)
