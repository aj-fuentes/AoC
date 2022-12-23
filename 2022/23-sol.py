#!/usr/env python3
import collections
import sys

with open(sys.argv[1]) as f:
    es = set(
        (i, j)
        for i, line in enumerate(f)
        for j, c in enumerate(line.strip())
        if c == "#"
    )

ds = "NSWE"
N = len(es)


def step(k):
    global es, ds
    k %= 4
    want_to_go = collections.defaultdict(set)
    need_move = False
    for (i, j) in es:
        if not (
            es
            & {
                (i - 1, j - 1),
                (i - 1, j),
                (i - 1, j + 1),
                (i + 1, j - 1),
                (i + 1, j),
                (i + 1, j + 1),
                (i, j - 1),
                (i, j + 1),
            }
        ):
            want_to_go[(i, j)].add((i, j))
        else:
            need_move = True
            for d in ds:
                if d == "N" and not (es & {(i - 1, j - 1), (i - 1, j), (i - 1, j + 1)}):
                    want_to_go[(i - 1, j)].add((i, j))
                    break
                if d == "S" and not (es & {(i + 1, j - 1), (i + 1, j), (i + 1, j + 1)}):
                    want_to_go[(i + 1, j)].add((i, j))
                    break
                if d == "W" and not (es & {(i - 1, j - 1), (i, j - 1), (i + 1, j - 1)}):
                    want_to_go[(i, j - 1)].add((i, j))
                    break
                if d == "E" and not (es & {(i - 1, j + 1), (i, j + 1), (i + 1, j + 1)}):
                    want_to_go[(i, j + 1)].add((i, j))
                    break
            else:
                want_to_go[None].add((i, j))

    new_es = set()
    for to, who in want_to_go.items():
        if to is None:
            # print("The elves", who, "cannot move")
            new_es.update(who)
        elif len(who) == 1:
            # print("Elf", who, "is the only one that wants to go to", to)
            new_es.add(to)
        else:
            # print("All the elves", who, "want to go to", to)
            new_es.update(who)
    es = new_es
    ds = ds[1:] + ds[0]
    return need_move


def show(not_moved=()):
    global es
    for i in range(min(x[0] for x in es), max(x[0] for x in es) + 1):
        print(
            "".join(
                "@" if (i, j) in not_moved else "#" if (i, j) in es else "."
                for j in range(min(x[1] for x in es), max(x[1] for x in es) + 1)
            )
        )


show()
k = 0
while step(k):
    print("== End of Round", k + 1, "==")
    # show()
    # input()
    k += 1
print("Finished on step:", k + 1)

ijmin = float("inf"), float("inf")
ijmax = float("-inf"), float("-inf")
for x in es:
    ijmin = min(ijmin[0], x[0]), min(ijmin[1], x[1])
    ijmax = max(ijmax[0], x[0]), max(ijmax[1], x[1])

res = (ijmax[0] - ijmin[0] + 1) * (ijmax[1] - ijmin[1] + 1) - len(es)
print(res)
