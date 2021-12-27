import sys
from itertools import permutations

ds = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg",
]
ds_ = set(ds)


def check_permutation(row, p):
    m = dict(zip("abcdefg", p))

    def get_d(d):
        return "".join(sorted(m[c] for c in d))

    # a b c d e f g
    # c f g a b d e
    # if p == ("c", "f", "g", "a", "b", "d", "e"):
    #     import pdb;pdb.set_trace()
    for d in map(get_d, row[:-4]):
        if d not in ds_:
            return
    res = 0
    for d in map(get_d, row[-4:]):
        res = res * 10 + ds.index(d)
    return res


def decode(info):
    res = []
    for row in info:
        for p in permutations("abcdefg"):
            n = check_permutation(row, p)
            if n is not None:
                res.append(n)
    return res


info = []
for line in open(sys.argv[1], "rt"):
    info.append(line.strip().replace(" | ", " ").split())
res = decode(info)
print(res)
print(sum(res))
