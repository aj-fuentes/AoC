#!/usr/env python3
import sys

with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip("\n")
        for i in range(14, len(line) + 1):
            if len(set(line[i - 14 : i])) == 14:
                print(i)
                break
