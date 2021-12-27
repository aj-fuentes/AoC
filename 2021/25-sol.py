import sys

b = [list(line.strip()) for line in open(sys.argv[1], "rt")]


def step():
    global b
    res = False
    b0 = [list(row) for row in b]
    for i, row in enumerate(b):
        for j, c in enumerate(row):
            if c == ">":
                j0 = (j + 1) % len(row)
                if b[i][j0] == ".":
                    res = True
                    b0[i][j0] = ">"
                    b0[i][j] = "."
    b = b0
    b0 = [list(row) for row in b]
    for i, row in enumerate(b):
        for j, c in enumerate(row):
            if c == "v":
                i0 = (i + 1) % len(b)
                if b[i0][j] == ".":
                    res = True
                    b0[i0][j] = "v"
                    b0[i][j] = "."
    b = b0
    return res


def pp():
    print("\n".join("".join(row) for row in b))
    print()


c = 1
while step():
    c += 1
    pass
print(c)
