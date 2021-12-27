import sys

x0, x1, y0, y1 = map(
    int,
    open(sys.argv[1], "rt")
    .read()
    .strip()
    .replace("target area: ", "")
    .replace("x=", "")
    .replace("y=", "")
    .replace("..", ",")
    .split(","),
)
print(x0, x1, y0, y1)

vx = 0
vy = 0
max_y = 0
c = 0
sols = []
for vx0 in range(1000):
    for vy0 in range(1000, -1000, -1):
        x, y, vx, vy = 0, 0, vx0, vy0
        found = False
        loca_max_y = 0
        while x <= x1 and y0 <= y:
            loca_max_y = max(loca_max_y, y)
            if x0 <= x and y <= y1:
                found = True
                c += 1
                sols.append((vx, vy))
                break
            x, y, vx, vy = (x + vx, y + vy, max(vx - 1, 0), vy - 1)
        if found:
            max_y = max(max_y, loca_max_y)
# print(sols)
print(c, max_y)
