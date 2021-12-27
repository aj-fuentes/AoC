import sys  # noqa
from functools import reduce
from operator import mul


def bin_line(line):
    return "".join(f"{int(c, base=16):04b}" for c in line)


def parse_package(line):
    # returns package, len in bits of the package
    v, t = int(line[:3], base=2), int(line[3:6], base=2)
    if t == 4:
        b = ""
        i = 6
        while line[i] == "1":
            b += line[i + 1 : i + 5]
            i += 5
        b += line[i + 1 : i + 5]
        n = int(b, base=2)
        return (v, t, n), i + 5

    ps = []
    if line[6] == "0":
        k = int(line[7 : 7 + 15], base=2)
        tl = 7 + 15 + k
        line = line[7 + 15 :]
        while k:
            p, m = parse_package(line)
            line = line[m:]
            ps.append(p)
            k -= m
    else:
        k = int(line[7 : 7 + 11], base=2)
        tl = 7 + 11
        line = line[7 + 11 :]
        while k:
            p, m = parse_package(line)
            line = line[m:]
            tl += m
            ps.append(p)
            k -= 1
    return (v, t, ps), tl


def eval_package(p):
    v, t, ps = p
    if t == 4:
        return ps
    vs = map(eval_package, ps)
    if t == 0:
        return sum(vs)
    if t == 1:
        return reduce(mul, vs)
    if t == 2:
        return min(vs)
    if t == 3:
        return max(vs)
    if t == 5:
        return int(next(vs) > next(vs))
    if t == 6:
        return int(next(vs) < next(vs))
    if t == 7:
        return int(next(vs) == next(vs))


line = bin_line(open(sys.argv[1], "rt").read().strip())
o = parse_package(line)
print(o[0])
print(eval_package(o[0]))
