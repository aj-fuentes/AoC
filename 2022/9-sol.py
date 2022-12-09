#!/usr/env python3
import sys

pos = set()


def move(h, t, count):
    hx, hy = h
    tx, ty = t
    if abs(hx - tx) <= 1 and abs(hy - ty) <= 1:
        return t
    if hx == tx:
        if hy > ty:
            y = ty + 1
            if count:
                pos.add((tx, y))
        else:
            y = ty - 1
            if count:
                pos.add((tx, y))
        return (tx, y)
    if hy == ty:
        if hx > tx:
            x = tx + 1
            if count:
                pos.add((x, ty))
        else:
            x = tx - 1
            if count:
                pos.add((x, ty))
        return (x, ty)
    tx += 1 if hx > tx else -1
    ty += 1 if hy > ty else -1
    if count:
        pos.add((tx, ty))
    return (tx, ty)


def pp(ts, final=False):
    for i in range(15, -6, -1):
        line = ""
        for j in range(-11, 15):
            if final:
                line += "#" if (j, i) in pos else "."
            else:
                try:
                    idx = ts.index((j, i))
                except ValueError:
                    line += "."
                else:
                    line += "H" if idx == 0 else str(idx)
        print(line)


# t = (0, 0)
# h = (0, 0)
ts = [(0, 0)] * 10
pos.add(ts[-1])
with open(sys.argv[1]) as f:
    for line in f:
        hx, hy = ts[0]
        d, s = line.strip("\n").split()
        s = int(s)
        if d == "R":
            hx += s
        elif d == "L":
            hx -= s
        elif d == "U":
            hy += s
        elif d == "D":
            hy -= s
        same = ts[0] == (hx, hy)
        ts[0] = (hx, hy)
        while not same:
            same = True
            for i in range(1, 10):
                t = move(ts[i - 1], ts[i], i == 9)
                if ts[i] == t:
                    break
                else:
                    same = False
                ts[i] = t
        # print("==", line.strip(), "==")
        # pp(ts)
    # print("==", "Final", "==")
    # pp(ts, True)

print(len(pos))
