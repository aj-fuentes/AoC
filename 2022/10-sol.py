#!/usr/env python3
import sys

cycle = 0
X = 1


def inc_cycle():
    global cycle
    cycle += 1
    if cycle in range(20, 221, 40):
        return cycle * X
    return 0


def inc_cycle2():
    global cycle
    cycle += 1
    if X - 1 <= (cycle % 40) <= X + 1:
        return "#"
    return "."


with open(sys.argv[1]) as f:
    # res = 0
    res = ""
    for line in f:
        line = line.strip("\n")
        if line == "noop":
            res += inc_cycle2()
        else:
            res += inc_cycle2()
            X += int(line.split()[1])
            res += inc_cycle2()

while res:
    print(res[:40])
    res = res[40:]
