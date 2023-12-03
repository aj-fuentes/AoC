import sys

s = 0

ds = "zero,one,two,three,four,five,six,seven,eight,nine".split(",")


def get(line):
    line = line.strip()
    x = -1
    for i in range(len(line)):
        if line[i].isdigit():
            x = int(line[i])
            break
        for j, d in enumerate(ds):
            if line[i:].startswith(d):
                x = j
        if x != -1:
            break
    y = -1
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            y = int(line[i])
            break
        for j, d in enumerate(ds):
            if line[i:].startswith(d):
                y = j
        if y != -1:
            break
    if x == -1 or y == -1:
        print(line)
        import pdb

        pdb.set_trace()
    return 10 * x + y


with open(sys.argv[1]) as f:
    print(sum(map(get, f)))
