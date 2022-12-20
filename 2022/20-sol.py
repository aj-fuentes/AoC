#!/usr/env python3
import sys


class Node:
    def __init__(self, val):
        self.val = int(val)
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.val)


with open(sys.argv[1]) as f:
    vals = list(map(Node, f.read().splitlines()))

N = len(vals)
Z = None
for i, node in enumerate(vals):
    node.val *= 811589153
    node.next = vals[(i + 1) % N]
    node.prev = vals[i - 1]
    if node.val == 0:
        Z = i


def show():
    xx = [0]
    curr = vals[Z].next
    while curr is not vals[Z]:
        xx.append(curr.val)
        curr = curr.next
    print(xx)


print(min(node.val for node in vals), max(node.val for node in vals))

for _ in range(10):
    for node in vals:
        if node.val == 0:
            continue
        k = abs(node.val) % (N - 1)
        if k == 0:
            continue
        node.prev.next = node.next
        node.next.prev = node.prev
        curr = node
        if node.val > 0:
            while k:
                k -= 1
                curr = curr.next
            # print(node.val, "moves between", curr.val, "and", curr.next.val)
            node.prev = curr
            node.next = curr.next
            curr.next = node
            node.next.prev = node
        else:
            while k:
                k -= 1
                curr = curr.prev
            # print(node.val, "moves between", curr.prev.val, "and", curr.val)
            node.next = curr
            node.prev = curr.prev
            curr.prev = node
            node.prev.next = node
        # show()


def check():
    for node in vals:
        curr = node.next
        k = 1
        while curr is not node:
            curr = curr.next
            k += 1
        assert k == len(vals)
        curr = node.prev
        k = 1
        while curr is not node:
            curr = curr.prev
            k += 1
        assert k == len(vals)


# print(vals)
res = 0
k = 0
curr = vals[Z]
assert curr.val == 0
# check()
while k < 3002:
    if k in (1000, 2000, 3000):
        print(curr.val)
        res += curr.val
    # if k in (999, 1999, 2999):
    #     print("prev", curr.val)
    # if k in (1001, 2001, 3001):
    #     print("next", curr.val)
    curr = curr.next
    k += 1

print(res)
