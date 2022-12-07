#!/usr/env python3
import re
import sys

root = {}
cwd = root


with open(sys.argv[1]) as f:
    for line in f:
        line = line.strip("\n")
        if line.startswith("$ cd"):
            p = line.split()[2]
            if p == "/":
                cwd = root
            elif p == "..":
                cwd = cwd[".."]
            else:
                for d in p.split("/"):
                    if d not in cwd:
                        cwd[d] = {"..": cwd}
                    cwd = cwd[d]
        elif line.startswith("$ ls"):
            pass
        else:
            m = re.match(r"(\d+) (.+)", line)
            if m:
                cwd[int(m.group(1))] = m.group(2)


res = 0


def comp(tree, path, lim=100000):
    global res
    loc = 0
    for k in tree:
        if isinstance(k, int):
            loc += k
        elif k != "..":
            loc += comp(tree[k], path + "/" + k)
    if loc <= lim:
        res += loc
    return loc


tot = comp(root, "")
print(res)

res2 = float("inf")
cap = 70000000
need = 30000000
free = cap - tot


def comp2(tree):
    global res2
    loc = 0
    for k in tree:
        if isinstance(k, int):
            loc += k
        elif k != "..":
            loc += comp2(tree[k])
    if free + loc >= need:
        res2 = min(res2, loc)
    return loc


comp2(root)
print(res2)
