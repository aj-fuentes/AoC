# from itertools import cycle
from pprint import pprint as pp

ds = [
    (3, 1),
    (4, 3),
    (5, 6),
    (6, 7),
    (7, 6),
    (8, 3),
    (9, 1),
]


def get_wins(ts, other_ts):
    new_ts = [[0] * 21 for _ in range(10)]
    wins = 0
    for p in range(10):
        for s in range(21):
            if ts[p][s] == 0:
                continue
            for v, w in ds:
                new_p = (p + v) % 10
                new_s = s + new_p + 1
                new_w = ts[p][s] * w
                if new_s >= 21:
                    wins += new_w
                else:
                    new_ts[new_p][new_s] += new_w
    k = sum(w for row in other_ts for w in row)
    return new_ts, wins * k


ts1 = [[0] * 21 for _ in range(10)]
ts2 = [[0] * 21 for _ in range(10)]

# real problem
ts1[5][0] = 1
ts2[6][0] = 1

# test problem
# ts1[3][0] = 1
# ts2[7][0] = 1


wins1 = 0
wins2 = 0
while any(w != 0 for row in ts1 for w in row) and any(
    w != 0 for row in ts2 for w in row
):
    ts1, wins = get_wins(ts1, ts2)
    pp(ts1)
    wins1 += wins
    ts2, wins = get_wins(ts2, ts1)
    pp(ts2)
    wins2 += wins

print(wins1, wins2, max(wins1, wins2))


# def dice():
#     for k in cycle(range(1, 101)):
#         yield k


# def play(p1, p2):
#     p1 -= 1
#     p2 -= 1
#     s1 = 0
#     s2 = 0
#     roll = dice()
#     k = 0
#     while max(s1, s2) < 1000:
#         v = next(roll) + next(roll) + next(roll)
#         k += 3
#         p1 += v
#         p1 %= 10
#         s1 += p1 + 1
#         p1, p2 = p2, p1
#         s1, s2 = s2, s1
#     return k * min(s1, s2)


# res = play(6, 7)
# print(res)
