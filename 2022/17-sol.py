#!/usr/env python3
import itertools
import sys

with open(sys.argv[1]) as f:
    ms = f.read().strip("\n")

moves = itertools.cycle(list(enumerate(ms)))


class Piece:
    def __init__(self, shape):
        self.shape = shape
        self.width = len(shape[0])

    def __repr__(self):
        return "\n".join(self.shape)

    def check(self, pos, filled):
        return all(filled[y][x] == "." for x, y in self.filled(pos) if y < len(filled))

    def filled(self, pos):
        xp, yp = pos
        for y, r in enumerate(reversed(self.shape), start=yp):
            for x, c in enumerate(r, start=xp):
                if c == "#":
                    yield x, y


pieces = [
    Piece(
        [
            "####",
        ]
    ),
    Piece(
        [
            ".#.",
            "###",
            ".#.",
        ]
    ),
    Piece(
        [
            "..#",
            "..#",
            "###",
        ]
    ),
    Piece(
        [
            "#",
            "#",
            "#",
            "#",
        ]
    ),
    Piece(
        [
            "##",
            "##",
        ]
    ),
]

maxY = -1
filled = []


def show(piece=()):
    maxP = max((y for _, y in piece), default=maxY)
    for y in range(max(maxY, maxP), -1, -1):
        line = "|"
        for x in range(7):
            line += "@" if (x, y) in piece else filled[y][x] if y < len(filled) else "."
        line += "|"
        print(line)
    print("+-------+")


def key(s, i, xp, yp, maxY, piece):
    return (
        s % 5,
        i,
        "\n".join(
            "".join(
                "@"
                if (x, y) in piece
                else filled[y][x]
                if 0 <= y < len(filled)
                else "."
                for x in range(7)
            )
            for y in range(maxY, yp - 4, -1)
        ),
    )


def add(filled, pfilled):
    for x, y in pfilled:
        if y >= len(filled):
            for y in range(len(filled), y + 1):
                filled.append(list("......."))
        filled[y][x] = "#"


maxs = [0]
i = 0
NN = 2022
NN = 1000000000000
bips = {}
for s, p in enumerate(itertools.cycle(pieces), start=1):
    if s == NN + 1:
        break
    xp, yp = 2, maxY + 4
    for i, m in moves:
        if m == "<":
            if xp > 0 and p.check((xp - 1, yp), filled):
                xp -= 1
        else:
            if xp + p.width < 7 and p.check((xp + 1, yp), filled):
                xp += 1
        if yp == 0 or not p.check((xp, yp - 1), filled):
            break
        yp -= 1

    pfilled = list(p.filled((xp, yp)))
    pmaxY = max(y for _, y in pfilled)
    # show(pfilled)
    # input()
    add(filled, pfilled)
    maxY = max(maxY, pmaxY)
    maxs.append(maxY)
    # assert maxs[s] == maxY
    kk = key(s, i, xp, yp, maxY, pfilled)
    if kk in bips and pmaxY == maxY:
        # print(kk[-1])
        # print(kk[:-1])
        # print("s", s, "bips s", bips[kk])
        # assert maxY == pmaxY
        s0 = bips[kk]
        m, n = divmod(NN - s0, s - s0)
        # assert NN == m * (s - s0) + n + s0
        print(m * (maxY - maxs[s0]) + maxs[s0 + n] + 1)
        sys.exit(0)
    else:
        bips[kk] = s


print(maxY + 1)
