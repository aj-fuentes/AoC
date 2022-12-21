#!/usr/env python3
import sys

code = {}
with open(sys.argv[1]) as f:
    for line in f:
        name, op = line.strip("\n").split(":")
        op = op.strip()
        if op[0].isalpha():
            code[name] = op.split(" ")
        else:
            code[name] = int(op)

opsx = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x // y,
}


class Num:
    def __init__(self):
        self.ops = "x"

    def __repr__(self):
        return self.ops

    def __add__(self, y):
        self.ops = f"({self.ops}+{y})"
        return self

    def __radd__(self, y):
        self.ops = f"({y}+{self.ops})"
        return self

    def __sub__(self, y):
        self.ops = f"({self.ops}-{y})"
        return self

    def __rsub__(self, y):
        self.ops = f"({y}-{self.ops})"
        return self

    def __mul__(self, y):
        self.ops = f"({self.ops}*{y})"
        return self

    def __rmul__(self, y):
        self.ops = f"({y}*{self.ops})"
        return self

    def __floordiv__(self, y):
        self.ops = f"({self.ops}//{y})"
        return self

    def __rfloordiv__(self, y):
        self.ops = f"({y}//{self.ops})"
        return self


def num():
    # togo = ["root"]
    togo = [code["root"][0], code["root"][2]]
    while togo:
        name = togo[-1]
        if isinstance(code[name], (int, Num)):
            togo.pop()
            continue
        name1, op, name2 = code[name]
        if isinstance(code[name1], (int, Num)) and isinstance(code[name2], (int, Num)):
            code[name] = opsx[op](code[name1], code[name2])
            togo.pop()
            continue
        if not isinstance(code[name1], (int, Num)):
            togo.append(name1)
        if not isinstance(code[name2], (int, Num)):
            togo.append(name2)


def sol(n, y):
    def f(x):
        return eval(n.ops, {"x": x})

    a = 0
    b = 10 * y
    fa = f(a)
    fb = f(b)
    assert fa < y < fb or fb < y < fa
    if fa < fb:
        while fa < y < fb:
            m = (a + b) // 2
            fm = f(m)
            if fm == y:
                return m
            if fm < y:
                a = m
            else:
                b = m
    else:
        while fb < y < fa:
            m = (a + b) // 2
            fm = f(m)
            if fm == y:
                return m
            if fm < y:
                b = m
            else:
                a = m


code["humn"] = Num()
num()
print(code["root"])
res = sol(code[code["root"][0]], code[code["root"][2]])
print(res)

