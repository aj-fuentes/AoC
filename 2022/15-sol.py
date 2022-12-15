#!/usr/env python3
import re
import sys

ss = []
bs = []

with open(sys.argv[1]) as f:
    for line in f:
        m = re.match(
            r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)",
            line.strip("\n"),
        )
        ss.append(tuple(map(int, m.group(1, 2))))
        bs.append(tuple(map(int, m.group(3, 4))))


# empt = set()
# for (xs, ys), (xb, yb) in zip(ss, bs):
#     r = abs(xs - xb) + abs(ys - yb)
#     d = r - abs(Y - ys)
#     if d < 0:
#         continue
#     for x in range(xs - d, xs + d + 1):
#         empt.add((x, Y))
# empt -= set(bs)

# print(len(empt))
x0, x1 = 0, 21
y0, y1 = 0, 21


def show(x0=0, x1=21, y0=0, y1=21):
    def dist(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    for y in range(y0, y1):
        line = ""
        for x in range(x0, x1):
            if (x, y) in ss:
                line += "S"
            elif (x, y) in bs:
                line += "B"
            elif any(dist((x, y), s) <= dist(s, b) for s, b in zip(ss, bs)):
                line += "#"
            else:
                line += "."
        print(line)


def main(x0, x1, y0, y1):
    for y in range(y0, y1):
        a = []
        for (xs, ys), (xb, yb) in zip(ss, bs):
            r = abs(xs - xb) + abs(ys - yb)
            d = r - abs(y - ys)
            if d > 0:
                a.append((xs - d, xs + d))
        a.sort()
        a.reverse()
        b = list(a.pop())
        while a:
            c = a.pop()
            if c[0] > b[1]:
                return (c[0] - 1) * 4000000 + y
            b[1] = max(b[1], c[1])


print(main(0, 4000001, 0, 4000001))
