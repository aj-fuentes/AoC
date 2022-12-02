#!/usr/env python3
import sys

cals = []
with open(sys.argv[1]) as f:
    s = 0
    for line in f:
        line = line.strip()
        if line:
            s += int(line)
        else:
            cals.append(s)
            s = 0
cals.sort()
print(sum(cals[-3:]))
