import sys
from functools import reduce
from operator import mul

gs = []
with open(sys.argv[1]) as f:
    for line in f:
        gs.append(
            [
                {
                    part.strip().split(" ")[1]: int(part.strip().split(" ")[0])
                    for part in s.strip().split(",")
                    # for v, *c in part.strip().split(" ")
                }
                for s in line.strip().split(":")[1].split(";")
            ]
        )

val = {"red": 12, "green": 13, "blue": 14}

res = sum(i for i, g in enumerate(gs, start=1) if all((d[k] <= val[k]) for d in g for k in d))


def mult(x):
    return reduce(mul, x, 1)


inf = float("inf")

res = sum(mult(max(d.get(k, -inf) for d in g) for k in ["green", "red", "blue"]) for g in gs)

print(res)
