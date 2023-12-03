import sys
from collections import defaultdict

ts = []

with open(sys.argv[1]) as f:
    ts = [line.strip() for line in f]


def sym(c):
    return c != "." and not c.isdigit()


def check(i, j, k):
    for x in [i - 1, i + 1]:
        if not (0 <= x < len(ts)):
            continue
        for y in range(j - 1, j + k + 1):
            if not (0 <= y < len(ts[x])):
                continue
            if sym(ts[x][y]):
                return True
    if j > 0 and sym(ts[i][j - 1]):
        return True
    if j + k < len(ts[i]) and sym(ts[i][j + k]):
        return True


def sol1():
    s = 0
    for i, row in enumerate(ts):
        j = 0
        while j < len(row):
            k = 0
            while j + k < len(row) and row[j + k].isdigit():
                k += 1
            if k and check(i, j, k):
                num = row[j : j + k]
                print(num)
                s += int(num)
            j += k + 1
    return s


print(sol1())


def check2(i, j, k):
    for x in [i - 1, i + 1]:
        if not (0 <= x < len(ts)):
            continue
        for y in range(j - 1, j + k + 1):
            if not (0 <= y < len(ts[x])):
                continue
            if ts[x][y] == "*":
                yield (x, y)
    if j > 0 and ts[i][j - 1] == "*":
        yield (i, j - 1)
    if j + k < len(ts[i]) and ts[i][j + k] == "*":
        yield (i, j + k)


def sol2():
    data = defaultdict(list)
    s = 0
    for i, row in enumerate(ts):
        j = 0
        while j < len(row):
            k = 0
            while j + k < len(row) and row[j + k].isdigit():
                k += 1
            if k:
                num = int(row[j : j + k])
                for p in check2(i, j, k):
                    data[p].append(num)
            j += k + 1
    print(data)
    s = 0
    for vals in data.values():
        if len(vals) == 2:
            s += vals[0] * vals[1]
    return s


print(sol2())
