c = 0
with open("1-input", "rt") as f:
    h = int(f.readline().strip())
    for l in f: # noqa
        nh = int(l.strip())
        if nh > h:
            c += 1
        h = nh
print(c)
