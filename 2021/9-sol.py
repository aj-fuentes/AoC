import sys

b = [[ord(c) - ord("0") for c in line.strip()] for line in open(sys.argv[1], "rt")]

m = len(b)
n = len(b[0])


def low_point(i, j):
    v = b[i][j]
    for x, y in [(i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j)]:
        if (0 <= x < m) and (0 <= y < n):
            if v >= b[x][y]:
                return False
    return True


marked = set()


def dfs(i, j):
    size = 0
    to_visit = [(i, j)]
    while to_visit:
        i, j = to_visit.pop()
        if i < 0 or j < 0 or i >= m or j >= n:
            continue
        if (i, j) in marked or b[i][j] == 9:
            continue
        marked.add((i, j))
        size += 1

        to_visit.extend(
            (x, y)
            for (x, y) in [(i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j)]
            if (x, y) not in marked
        )
    return size


sizes = []
for i in range(m):
    for j in range(n):
        if low_point(i, j):
            size = dfs(i, j)
            sizes.append(size)

sizes.sort()
print(sizes[-1] * sizes[-2] * sizes[-3])
