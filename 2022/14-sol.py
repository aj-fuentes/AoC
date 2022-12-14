#!/usr/env python3
import sys

s = set()
w = set()
v = 0
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip("\n")
        parts = [
            tuple(map(int, part.split(","))) for part in line.split() if part != "->"
        ]
        (x0, y0) = parts[0]
        for (x1, y1) in parts:
            if x0 == x1:
                s |= set(
                    (x0, y)
                    for y in (range(y0, y1 + 1) if y0 <= y1 else range(y1, y0 + 1))
                )
            else:
                s |= set(
                    (x, y0)
                    for x in (range(x0, x1 + 1) if x0 <= x1 else range(x1, x0 + 1))
                )
            x0, y0 = x1, y1
    w |= s
    v = max(y for _, y in w)


def move(x, y):
    global s
    for p in [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]:
        if p not in s and p[1] < v + 2:
            return p
    return (x, y)




def show():
    global s, w, xs
    for y in range(0, v + 3):
        print(
            "".join(
                "#" if ((x, y) in w or y == v + 2) else "o" if (x, y) in s else "."
                for x in range(*xs)
            )
        )


def check():
    for (x, y) in s:
        if (x, y) not in w:
            assert (x, y + 1) in s
            assert (x - 1, y + 1) in s
            assert (x + 1, y + 1) in s


def main():
    global s, v
    res = 0
    while True:
        p = (500, 0)
        q = move(*p)
        while q != p:
            p = q
            q = move(*p)
        # if q[1] == v:
        #     return res
        if p == (500, 0):
            return res + 1
        s.add(p)
        res += 1


res = main()
xs = (min(x for x, _ in s), max(x for x, _ in s) + 1)
print(res)
