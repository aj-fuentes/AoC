#!/usr/env python3
import collections
import re
import sys

items_list = []
ops = []
tests = []
tos = []
K = 1


def read_monkey(lines):
    global K
    lines.pop()
    items_list.append(
        collections.deque(
            [int(val.strip()) for val in lines.pop().split(":")[1].split(",")]
        )
    )
    op, val = re.match(
        r"Operation: new = old ([+*-]) (\d+|old)", lines.pop().strip()
    ).groups()
    if val == "old":
        ls = {
            "*": lambda x: x * x,
        }
    else:
        val = int(val)
        ls = {
            "+": lambda x, val=val: x + val,
            "*": lambda x, val=val: x * val,
        }
    ops.append(ls[op])
    val = int(lines.pop().strip().split()[-1])
    K *= val
    tests.append(lambda x, val=val: (x % val) == 0)
    tos.append(
        {
            True: int(lines.pop().strip().split()[-1]),
            False: int(lines.pop().strip().split()[-1]),
        }
    )
    if lines:
        lines.pop()


with open(sys.argv[1]) as f:
    lines = f.readlines()
lines.reverse()
while lines:
    read_monkey(lines)

N = len(items_list)
c = [0] * N
M = 10000
for _ in range(M):
    for i in range(N):
        c[i] += len(items_list[i])
        while items_list[i]:
            v = items_list[i].popleft()
            new_v = ops[i](v)
            # print("monkey", i, "inspects", v, "and change to", new_v)
            # new_v //= 3
            new_v %= K
            j = tos[i][tests[i](new_v)]
            # print("throw", new_v, "to", j)
            items_list[j].append(new_v)
    # for i, items in enumerate(items_list):
    #     print(f"Monkey {i}:", ", ".join(map(str, items)))

c.sort()
print(c[-1] * c[-2])
