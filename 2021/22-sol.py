import sys
from bisect import bisect_left, bisect_right
from itertools import chain
from operator import itemgetter

info = []
for line in open(sys.argv[1], "rt"):
    com, rest = line.strip().split(" ")
    rest = rest.replace("x=", "").replace("y=", "").replace("z=", "")
    xs, ys, zs = map(
        lambda s: tuple(map(int, s.replace("..", ",").split(","))), rest.split(",")
    )
    info.append((com, xs, ys, zs))

# count = 0
# for x in range(-50, 51):
#     for y in range(-50, 51):
#         for z in range(-50, 51):
#             for c, (x0, x1), (y0, y1), (z0, z1) in reversed(info):
#                 if (x0 <= x <= x1) and (y0 <= y <= y1) and (z0 <= z <= z1):
#                     count += int(c == "on")
#                     break
# print(count)


def inside(cube0, cube1):
    _, (x0, x1), (y0, y1), (z0, z1) = cube0
    _, (X0, X1), (Y0, Y1), (Z0, Z1) = cube1
    return X0 <= x0 and x1 <= X1 and Y0 <= y0 and y1 <= Y1 and Z0 <= z0 and z1 <= Z1


def inside_seg(xx, XX):
    return XX[0] <= xx[0] and xx[1] <= XX[1]


cubes = info
cubes = [
    (
        com,
        (xs[0] - 0.5, xs[1] + 0.5),
        (ys[0] - 0.5, ys[1] + 0.5),
        (zs[0] - 0.5, zs[1] + 0.5),
    )
    for com, xs, ys, zs in cubes
]

xs = list(sorted(set(chain.from_iterable(map(itemgetter(1), cubes)))))
ys = list(sorted(set(chain.from_iterable(map(itemgetter(2), cubes)))))
zs = list(sorted(set(chain.from_iterable(map(itemgetter(3), cubes)))))

res = 0
count = 0
for i in range(len(xs) - 1):
    xx = xs[i], xs[i + 1]
    min_y = ys[-1]
    max_y = ys[0]
    x_cubes = []
    for c in cubes:
        if inside_seg(xx, c[1]):
            x_cubes.append(c)
            min_y = min(min_y, c[2][0])
            max_y = max(max_y, c[2][1])
    ylo = bisect_left(ys, min_y)
    yhi = bisect_right(ys, max_y)
    for j in range(ylo, yhi - 1):
        yy = ys[j], ys[j + 1]
        min_z = zs[-1]
        max_z = zs[0]
        xy_cubes = []
        for c in x_cubes:
            if inside_seg(yy, c[2]):
                xy_cubes.append(c)
                min_z = min(min_z, c[3][0])
                max_z = max(max_z, c[3][1])
        zlo = bisect_left(zs, min_z)
        zhi = bisect_right(zs, max_z)
        if not xy_cubes:
            continue
        for k in range(zlo, zhi - 1):
            zz = zs[k], zs[k + 1]
            for c in reversed(xy_cubes):
                count += 1
                if inside_seg(zz, c[3]):
                    if c[0] == "on":
                        res += (
                            int(xx[1] - xx[0]) * int(yy[1] - yy[0]) * int(zz[1] - zz[0])
                        )
                    break
print(res)


# on_segs = [[], [], []]
# off_segs = [[], [], []]
# for com, xs, ys, zs in info:
#     if com == "on":
#         on_segs[0].append(xs)
#         on_segs[1].append(ys)
#         on_segs[2].append(zs)
#     else:
#         off_segs[0].append(xs)
#         off_segs[1].append(ys)
#         off_segs[2].append(zs)

# for segs in on_segs:
#     segs.sort()
# for segs in off_segs:
#     segs.sort()
# print(on_segs[0])
# print(off_segs[0])
