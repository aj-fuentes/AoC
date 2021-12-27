import sys

ps = []
f = open(sys.argv[1], "rt")
for line in f:
    line = line.strip()
    if not line:
        break
    ps.append(tuple(map(int, line.split(","))))

ps = set(ps)
for line in f:
    c, v = line.strip().split(" ")[-1].split("=")
    v = int(v)
    for x, y in list(ps):
        if c == "x":
            if x > v:
                ps.remove((x, y))
                if 2 * v >= x:
                    ps.add((2 * v - x, y))
        else:
            if y > v:
                ps.remove((x, y))
                if 2 * v >= y:
                    ps.add((x, 2 * v - y))

n = max(p[0] for p in ps) + 1
m = max(p[1] for p in ps) + 1
t = [["."] * m for _ in range(n)]
for x, y in ps:
    t[x][y] = "#"
print("\n".join("".join(r) for r in t))
print(len(ps))
