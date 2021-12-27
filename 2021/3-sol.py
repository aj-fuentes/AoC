import operator
import sys
from collections import Counter


def get_col_num(col, comp, eq_val):
    c = Counter(col)
    if c[0] == c[1]:
        return eq_val
    return 1 if comp(c[1], c[0]) else 0


def get_number(rs, comp, eq_val):
    x = get_col_num([r[0] for r in rs], comp, eq_val)

    for i in range(1, len(rs[0]) + 1):
        rs = [r for r in rs if r[i - 1] == x]
        # print("\n".join("".join(map(str, r)) for r in rs))
        # print("-" * len(rs[0]))
        if len(rs) == 1:
            break
        x = get_col_num([r[i] for r in rs], comp, eq_val)
    # print("*" * len(rs[0]))
    return int("".join(map(str, rs[0])), base=2)


rs = list(list(map(int, n.strip())) for n in open(sys.argv[1], "rt"))
b1 = get_number(list(list(r) for r in rs), operator.gt, 1)
b2 = get_number(list(list(r) for r in rs), operator.lt, 0)
print(b1 * b2)
