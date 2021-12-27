import sys
from collections import defaultdict

g = defaultdict(list)
for line in open(sys.argv[1], "rt"):
    a, b = line.strip().split("-")
    g[a].append(b)
    g[b].append(a)


def backtrack(n, p, double):
    if n == "end":
        return 1
    if n.islower() and (n in p):
        if double:
            return 0
        double = True
    return sum(backtrack(m, p + [n], double) for m in g[n] if m != "start")


res = backtrack("start", [], False)
print(res)
