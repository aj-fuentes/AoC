import sys

vals = list(
    map(
        lambda l: l.strip().split(),
        open(sys.argv[1], "rt"),
    )
)
p = 0
a = 0
d = 0

for m, v in vals:
    v = int(v)
    if m == "forward":
        p += v
        d += a * v
    elif m == "up":
        a -= v
    else:
        a += v

print(p * d)
