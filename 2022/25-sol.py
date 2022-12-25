#!/usr/env python3
import sys

with open(sys.argv[1]) as f:
    snums = [line.strip() for line in f]


def to_dec(num):
    n = 0
    cc = {"-": -1, "=": -2, "1": 1, "0": 0, "2": 2}
    for c in num:
        n = 5 * n + cc[c]
    return n


def to_snafu(num):
    out = ""
    cc = {0: "0", 1: "1", 2: "2", 3: "=", 4: "-"}
    carry = 0
    while num:
        num, c = divmod(num, 5)
        carry, c = divmod(c + carry, 5)
        out += cc[c]
        carry += 1 if c > 2 else 0
    if carry:
        out += cc[carry]
    return "".join(reversed(out))


res = 0
for num in snums:
    dec = to_dec(num)
    res += dec
    snu = to_snafu(dec)
    assert num == snu

print("dec", res)
print("snafu", to_snafu(res))
