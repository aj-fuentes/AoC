#!/usr/env python3
import functools
import sys

ps = []
with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip("\n")
        if not line:
            continue
        ps.append(eval(line))


def cmp(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return -1 if a < b else 0 if a == b else 1
    if isinstance(a, int):
        return cmp([a], b)
    if isinstance(b, int):
        return cmp(a, [b])
    # both are lists
    for x, y in zip(a, b):
        v = cmp(x, y)
        if v == 0:
            continue
        return v
    # compare length
    return -1 if len(a) < len(b) else 0 if len(a) == len(b) else 1


# res = 0
# for i in range(len(ps) // 2):
#     if cmp(ps[2 * i], ps[2 * i + 1]) == -1:
#         res += i + 1
ps.append([[2]])
ps.append([[6]])
ps.sort(key=functools.cmp_to_key(cmp))

res = 1
for i, x in enumerate(ps, start=1):
    if cmp(x, [[2]]) == 0:
        res *= i
    elif cmp(x, [[6]]) == 0:
        res *= i
        break


print(res)
