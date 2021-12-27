import sys

base_pos = []
for line in open(sys.argv[1], "rt"):
    base_pos.append(list(line.strip("\n")))
base_pos.insert(3, list("  #D#C#B#A#"))
base_pos.insert(4, list("  #D#B#A#C#"))


def coords():
    for j in range(1, 12):
        yield (1, j)
    for i in (2, 3, 4, 5):
        for j in (3, 5, 7, 9):
            yield (i, j)


def move(pos, i, j):
    dj = 3 + 2 * ("ABCD".index(pos[i][j]))
    if i == 1:
        if any(pos[k][dj] not in (pos[i][j], ".") for k in [2, 3, 4, 5]):
            return
        j0 = j
        while j0 != dj:
            j0 += 1 if j0 < dj else -1
            if pos[i][j0] != ".":
                return
        i0 = 1
        while pos[i0 + 1][dj] == ".":
            i0 += 1
        assert pos[i0][dj] == "."
        assert pos[i0 + 1][dj] in (pos[i][j], "#")
        yield i0, dj
    elif j == dj:
        if all(pos[k][dj] == pos[i][j] for k in range(i, 6)) and all(
            pos[k][dj] in (pos[i][j], ".") for k in range(i - 1, 1, -1)
        ):
            return
        if any(pos[k][dj] != "." for k in range(i - 1, 0, -1)):
            return
        j0 = j
        while pos[1][j0 + 1] == ".":
            j0 += 1
            if j0 in (1, 2, 4, 6, 8, 10, 11):
                yield 1, j0
        j0 = j
        while pos[1][j0 - 1] == ".":
            j0 -= 1
            if j0 in (1, 2, 4, 6, 8, 10, 11):
                yield 1, j0
    else:
        if any(pos[k][j] != "." for k in range(i - 1, 0, -1)):
            return
        j0 = j
        while pos[1][j0 + 1] == ".":
            j0 += 1
            if j0 in (1, 2, 4, 6, 8, 10, 11):
                yield 1, j0
        j0 = j
        while pos[1][j0 - 1] == ".":
            j0 -= 1
            if j0 in (1, 2, 4, 6, 8, 10, 11):
                yield 1, j0


def won(pos):
    return all(
        pos[i][3 + 2 * k] == c for k, c in enumerate("ABCD") for i in range(2, 6)
    )


def ts(pos):
    return "\n".join("".join(row) for row in pos)


def backtrack():
    best = float("inf")
    to_go = [(base_pos, 0)]
    seen = {}
    while to_go:
        pos, val = to_go.pop()
        ss = hash(ts(pos))
        if ss in seen and seen[ss] <= val:
            continue
        seen[ss] = val
        if val >= best:
            continue
        if won(pos):
            best = min(best, val)
            continue
        for i, j in coords():
            if pos[i][j] == ".":
                continue
            cost = 10 ** ("ABCD".index(pos[i][j]))
            for di, dj in list(move(pos, i, j)):
                new_pos = [list(r) for r in pos]
                new_pos[i][j] = "."
                new_pos[di][dj] = pos[i][j]
                to_go.append((new_pos, val + cost * (abs(j - dj) + abs(i - di))))
    return best


def pp(pos):
    print(ts(pos))


b = backtrack()
print(b)
