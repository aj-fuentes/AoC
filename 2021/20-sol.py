import sys
from functools import reduce

f = open(sys.argv[1], "rt")
e = [int(c == "#") for c in f.readline().strip()]

f.readline()

im = [[int(c == "#") for c in line] for line in f]
# print("\n".join("".join("#" if v else "." for v in row) for row in im))

back = 0
step = 1
N = 50
while step <= N:
    im = (
        [
            [back] * (len(im[0]) + 4),
            [back] * (len(im[0]) + 4),
        ]
        + [[back, back] + list(row) + [back, back] for row in im]
        + [
            [back] * (len(im[0]) + 4),
            [back] * (len(im[0]) + 4),
        ]
    )
    new_im = [list(row) for row in im]
    for i in range(len(new_im)):
        for j in range(len(new_im[0])):
            idx = reduce(
                lambda acc, v: 2 * acc + v,
                (
                    im[x][y]
                    if (0 <= x < len(new_im)) and (0 <= y < len(new_im[0]))
                    else back
                    for x in range(i - 1, i + 2)
                    for y in range(j - 1, j + 2)
                ),
            )
            new_im[i][j] = e[idx]
    back = e[-1 if back else 0]
    im = new_im
    step += 1


# print("\n".join("".join("#" if v else "." for v in row) for row in im))
print(sum(sum(row) for row in im))
