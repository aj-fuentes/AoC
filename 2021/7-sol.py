import sys

ns = list(map(int, open(sys.argv[1], "rt").read().strip().split(",")))
best_s = float("inf")
for k in range(min(ns), max(ns) + 1):
    best_s = min(best_s, sum((abs(x - k) * (abs(x - k) + 1)) // 2 for x in ns))
print(best_s)
