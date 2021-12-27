import sys

p = [0] * 9
for n in map(int, open(sys.argv[1], "rt").read().strip().split(",")):
    p[n] += 1

for _ in range(256):
    p = [
        p[1],
        p[2],
        p[3],
        p[4],
        p[5],
        p[6],
        p[7] + p[0],
        p[8],
        p[0],
    ]

print(sum(p))
