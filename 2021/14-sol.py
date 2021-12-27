import sys
from collections import Counter, defaultdict

f = open(sys.argv[1], "rt")
s = "^" + f.readline().strip() + "$"
f.readline()
d = {}
for line in f:
    p, n = line.strip().replace(" ", "").split("->")
    d[tuple(p)] = n
f.close()

ps = Counter()
for i in range(len(s) - 1):
    ps[(s[i], s[i + 1])] += 1

for _ in range(40):
    new_ps = Counter()
    for p, n in ps.items():
        if p in d:
            new_ps[(p[0], d[p])] += n
            new_ps[(d[p], p[1])] += n
        else:
            new_ps[p] = n
    ps = new_ps

c = Counter()
for k, v in ps.items():
    c[k[0]] += v
    c[k[1]] += v
del c["^"]
del c["$"]
for k in c:
    c[k] //= 2
r = c.most_common()
print(r[0][1] - r[-1][1])
