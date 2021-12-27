import sys

p = {")": "(", "]": "[", "}": "{", ">": "<"}

xs = []
for line in open(sys.argv[1], "rt"):
    s = []
    invalid = False
    for c in line.strip():
        if c in "({[<":
            s.append(c)
        elif not s or p[c] != s[-1]:
            invalid = True
            break
        else:
            s.pop()
    if invalid:
        continue
    x = 0
    while s:
        c = s.pop()
        x = 5 * x + "0([{<".index(c)
    xs.append(x)

xs.sort()
print(xs[len(xs) // 2])
