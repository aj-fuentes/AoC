#!/usr/env python3
import sys

with open(sys.argv[1]) as f:
    lines = [line.strip("\n") for line in f.readlines()]
    ts = list(map(list, lines[:-2]))
    pw = lines[-1]

# ls = [sum(x == " " for x in line) for line in ts]
# rs = [sum(x == " " for x in reversed(line)) for line in ts]
# us = [sum(line[j] == " " for line in ts) for j in range(len(ts[0]))]
# ds = [sum(line[j] == " " for line in reversed(ts)) for j in range(len(ts[0]))]
print("\n".join("".join(line) for line in ts))
print(pw)

N = len(ts)
M = max(map(len, ts))
K = abs(M - N)
ts = [line + list(" " * (M - len(line))) for line in ts]
# assert all(len(line) == M for line in ts)


sq = [
    (K * a, K * b)
    for a in range(N // K)
    for b in range(M // K)
    if ts[K * a][K * b] != " "
]


def get_sq(i, j):
    global sq
    return next(
        (
            k
            for (k, (a, b)) in enumerate(sq, start=1)
            if 0 <= i - a < K and 0 <= j - b < K
        ),
        -1,
    )


def show_sq():
    for i, line in enumerate(ts):
        out = ""
        for j, c in enumerate(line):
            out += str(get_sq(i, j)) if c != " " else c
        print(out)


# print(sq)
show_sq()
sq_map = {
    x[:2]: x[2:] for x in ["1U2U", "1L3U", "1R6R", "2D5D", "2L6D", "3D5L", "4R6U"]
}
sq_map = {
    x[:2]: x[2:] for x in ["1U6L", "1L4L", "2U6D", "2R5R", "2D3R", "3L4U", "5D6R"]
}
sq_map.update({v: k for (k, v) in sq_map.items()})
print(sq_map)


def inc(i0, j0, dir):
    global M, N
    di, dj = {"R": (0, 1), "L": (0, -1), "D": (1, 0), "U": (-1, 0)}[dir]
    i1, j1 = (i0 + di) % N, (j0 + dj) % M
    while ts[i1][j1] == " ":
        i1, j1 = (i1 + di) % N, (j1 + dj) % M
    return i1, j1, dir


def inc_cube(i0, j0, dir):
    global M, N, K
    di, dj = {"R": (0, 1), "L": (0, -1), "D": (1, 0), "U": (-1, 0)}[dir]
    i1, j1 = (i0 + di) % N, (j0 + dj) % M

    x = get_sq(i0, j0)
    # print(x, get_sq(i1, j1), str(x) + dir, (str(x) + dir) not in sq_map)
    if x == get_sq(i1, j1) or (str(x) + dir) not in sq_map:
        return i1, j1, dir
    # x != z -> change of square
    # xdir in sq_map -> the change is relevant
    dx = dir
    ax, bx = sq[x - 1]
    ix, jx = i0 - ax, j0 - bx

    assert 0 <= ix < K and 0 <= jx < K

    y, dy = sq_map[str(x) + dir]
    ay, by = sq[int(y) - 1]
    iy, jy = {
        "UU": (0, K - 1 - jx),
        "UR": (K - 1 - jx, K - 1),
        "UD": (K - 1, jx),
        "UL": (jx, 0),
        "DU": (0, jx),
        "DR": (jx, K - 1),
        "DD": (K - 1, K - 1 - jx),
        "DL": (K - 1 - jx, 0),
        "RU": (0, K - 1 - ix),
        "RR": (K - 1 - ix, K - 1),
        "RD": (K - 1, ix),
        "RL": (ix, 0),
        "LU": (0, ix),
        "LR": (ix, K - 1),
        "LD": (K - 1, K - 1 - ix),
        "LL": (K - 1 - ix, 0),
    }[dx + dy]
    assert 0 <= iy < K and 0 <= jy < K

    return ay + iy, by + jy, {"U": "D", "D": "U", "R": "L", "L": "R"}[dy]


def move(pos, dir, steps):
    global done, M, N
    i, j = pos
    for _ in range(steps):
        # i0, j0, dir = inc(i, j, dir)
        i0, j0, dir0 = inc_cube(i, j, dir)
        if ts[i0][j0] == "#":
            break
        if ts[i0][j0] == " ":
            import pdb

            pdb.set_trace()
        assert ts[i0][j0] == "."
        i, j, dir = i0, j0, dir0
        # assert ts[i0][j0] == "."
        done[(i, j)] = dir
        # show((i, j))
        # input()

    return (i, j), dir


def show(pos0=None):
    global done
    si = 0 if pos0 is None else max(pos0[0] - 10, 0)
    ei = N if pos0 is None else min(pos0[0] + 11, N)
    for i, line in enumerate(ts[si:ei], start=si):
        out = ""
        for j, c in enumerate(line):
            out += (str.lower if (i, j) == pos0 else str.upper)(done.get((i, j), c))
        print(out)


d = "R"
m = 0
pos = 0, ts[0].index(".")
done = {pos: d}
for c in pw:
    # print("c", c)
    if c.isdigit():
        m = 10 * m + int(c)
    else:
        pos, d = move(pos, d, m)
        # assert ts[pos[0]][pos[1]] == "."
        m = 0
        d = {
            ("R", "R"): "D",
            ("D", "R"): "L",
            ("L", "R"): "U",
            ("U", "R"): "R",
            ("R", "L"): "U",
            ("U", "L"): "L",
            ("L", "L"): "D",
            ("D", "L"): "R",
        }[(d, c)]
        done[pos] = d
        # show(pos)
        # input()
pos, d = move(pos, d, m)  # final move

print()
# show()
print(pos, d)
print((pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + "RDLU".index(d))
