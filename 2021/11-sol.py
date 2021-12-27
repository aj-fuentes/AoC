import sys
from collections import deque

b = [list(map(int, line.strip())) for line in open(sys.argv[1], "rt")]


def get_xy(i, j):
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            xy = x, y
            if xy == (i, j):
                continue
            if 0 <= x < len(b) and 0 <= y < len(b[0]):
                yield xy


def flash(to_flash):
    to_flash = deque(to_flash)
    while to_flash:
        i, j = to_flash.popleft()
        if b[i][j] <= 9:
            continue
        for x, y in get_xy(i, j):
            if b[x][y] > 9:
                continue
            b[x][y] += 1
            if b[x][y] > 9:
                to_flash.append((x, y))
    c = 0
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] > 9:
                c += 1
                b[i][j] = 0
    return c


def step():
    to_flash = []
    for i in range(len(b)):
        for j in range(len(b[0])):
            b[i][j] += 1
            if b[i][j] > 9:
                to_flash.append((i, j))
    return flash(to_flash)


for i in range(500):
    if step() == len(b) * len(b[0]):
        print("step", i + 1)
        break
