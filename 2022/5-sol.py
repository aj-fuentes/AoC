#!/usr/env python3
import collections
import re
import sys

stacks = collections.defaultdict(list)

res = 0

# [B] [V] [B] [T] [W] [V] [Z] [Z] [M]
#  1   2   3   4   5   6   7   8   9
# 12345678901234567
def stack_line(line):
    for i, c in enumerate(line, start=1):
        # i = 4 * (j - 1) + 2
        if "A" <= c <= "Z":
            j = (i - 2) // 4 + 1
            stacks[j].append(c)


def move_line(line):
    m = re.match(r"move (\d+) from (\d+) to (\d+)", line)
    n, i, j = map(int, m.group(1, 2, 3))
    for _ in range(n):
        stacks[j].append(stacks[i].pop())


def move_line2(line):
    m = re.match(r"move (\d+) from (\d+) to (\d+)", line)
    n, i, j = map(int, m.group(1, 2, 3))
    stacks[j].extend(stacks[i][-n:])
    del stacks[i][-n:]


process = stack_line
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip("\n")
        if not line:
            process = move_line2
            for stack in stacks.values():
                stack.reverse()
            continue
        process(line)

print("".join(stacks[k][-1] for k in sorted(stacks.keys())))
