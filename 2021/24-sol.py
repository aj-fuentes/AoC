code0 = open("24-input", "rt").read().strip()
ins = code0.split("\n")

ops = []

for op in ins:
    if op == "inp w":
        ops.append([])
    ops[-1].append(op)


debug = False


def comp(code, z=0):
    def run(ins):
        global debug
        reg = {"x": 0, "y": 0, "z": z, "w": 0}
        for line in code.split("\n"):
            line = line.strip()
            if debug:
                print(reg)
                print(line)
            if line.startswith("inp"):
                assert line[-1] in reg
                reg[line[-1]] = ins.pop(0)
                continue
            op, a, b = line.split(" ")
            assert a in reg
            b = int(reg.get(b, b))
            if op == "add":
                reg[a] += b
            elif op == "mul":
                reg[a] *= b
            elif op == "mod":
                reg[a] %= b
            elif op == "div":
                reg[a] //= b
            elif op == "eql":
                reg[a] = int(reg[a] == b)
        return tuple(reg[k] for k in "xyzw")

    return run


prog1 = comp(
    """inp x
mul x -1"""
)
assert prog1([3]) == (-3, 0, 0, 0)
prog2 = comp(
    """inp z
inp x
mul z 3
eql z x"""
)
assert prog2([1, 3]) == (3, 0, 1, 0)
assert prog2([2, 3]) == (3, 0, 0, 0)
prog3 = comp(
    """inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2"""
)
for k in range(2 ** 4):
    s = prog3([k])
    assert "".join(map(str, (s[3], s[0], s[1], s[2]))) == f"{k:04b}"


print(
    "\n".join(
        f"{i}:" + " ".join(f"{row[k]: <9}" for k in range(len(row)))
        for i, row in enumerate(ops)
    )
)

cs = ["inp w\n" + rest.strip() for rest in code0.split("inp w\n")[1:]]

for z in range(0, 26):
    for w0 in range(1, 10):
        o0 = comp(cs[0], z)([w0])
        assert o0[2] == 26 * z + w0 + 5
        for w1 in range(1, 10):
            o1 = comp(cs[1], o0[2])([w1])
            assert o1[2] == 26 * o0[2] + w1 + 9
            for w2 in range(1, 10):
                o2 = comp(cs[1], o1[2])([w2])
                assert o2[2] == 26 * o1[2] + w2 + 9

# biggest
# ws = [9] * 14
# ws[10] = 6
# ws[8] = 4
# for k in [3, 5, 6, 7, 9, 12, 13]:
#     prog = comp("\n".join(cs[: k + 1]))
#     min_val = float("inf")
#     min_w = 0
#     for w in range(1, 10):
#         ins = list(ws)
#         ins[k] = w
#         oo = prog(ins)
#         val = oo[2]
#         if val < min_val:
#             ins = list(ws)
#             ins[k] = w
#             min_val = val
#             min_w = w
#             ws[k] = min_w

# print("".join(map(str, ws)))

# smallest
ws = [1] * 14
ws[11] = 7
ws[4] = 4
ws[2] = 9
ws[0] = 8
for k in [3, 5, 6, 7, 9, 12, 13]:
    prog = comp("\n".join(cs[: k + 1]))
    min_val = float("inf")
    min_w = 0
    for w in range(1, 10):
        ins = list(ws)
        ins[k] = w
        oo = prog(ins)
        val = oo[2]
        if val < min_val:
            ins = list(ws)
            ins[k] = w
            print(ins[: k + 1], oo)
            min_val = val
            min_w = w
            ws[k] = min_w

print("".join(map(str, ws)))

# def get_sol():
#     val = [9] * 14

#     def inc(ks):
#         if not ks:
#             yield list(val)
#             return
#         k = ks[0]
#         for w in range(9, 0, -1):
#             val[k] = w
#             yield from inc(ks[1:])

#     for vv in inc([3, 5, 6, 7, 9, 12, 13]):
#         sol = tuple(vv)
#         oo = prog(vv)
#         if oo[2] == 0:
#             return sol


# print(get_sol())

# max_ds = tuple([0] * len(cs))


# def find(out, ds):
#     global max_ds, cs
#     if len(ds) == len(cs):
#         if out == 0:
#             max_ds = max(max_ds, tuple(ds))
#         return

#     code = cs[-len(ds) - 1]
#     for w in range(9, 0, -1):
#         for z in range(0, 4 * 26):
#             pp = comp(code, z)
#             res = pp([w])[2]
#             if res == out:
#                 find(z, [w] + ds)


# find(0, [])
# print(max_ds)
