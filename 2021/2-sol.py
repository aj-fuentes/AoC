import sys

d = 0
vals = list(
    map(
        lambda l: l.strip().split(),
        open(sys.argv[1], "rt"),
    )
)
p = sum(int(x[1]) for x in vals if x[0] == "forward")
d = sum(-int(x[1]) if x[0] == "up" else int(x[1]) for x in vals if x[0] != "forward")
print(p * d)
