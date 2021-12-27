import sys  # noqa


class Node:
    def __init__(self, parent=None, value=-1):
        self.parent = parent
        self.value = value
        self.children = []

    def __repr__(self):
        if self.value != -1:
            return str(self.value)
        return "[{}]".format(",".join(map(repr, self.children)))

    def magnitude(self):
        if self.value != -1:
            return self.value
        return self.children[0].magnitude() * 3 + self.children[1].magnitude() * 2


def parse(line):
    s = []
    for c in line:
        if c.isdigit():
            s.append(Node(value=int(c)))
        elif c == "]":
            n = Node()
            r = s.pop()
            l = s.pop()  # noqa
            r.parent = n
            l.parent = n
            n.children = [l, r]
            s.append(n)
    return s[0]


def explode(root):
    def find(node, level):
        if level == 4:
            return node
        for child in node.children:
            if child.value != -1:
                continue
            res = find(child, level + 1)
            if res is not None:
                return res

    def find_left(node):
        while node.parent and node.parent.children[0] == node:
            node = node.parent
        if node.parent is None:
            # root
            return
        node = node.parent.children[0]
        while node.value == -1:
            node = node.children[1]
        return node

    def find_right(node):
        while node.parent and node.parent.children[1] == node:
            node = node.parent
        if node.parent is None:
            # root
            return
        node = node.parent.children[1]
        while node.value == -1:
            node = node.children[0]
        return node

    node = find(root, 0)
    if node is None:
        return False

    left = find_left(node)
    right = find_right(node)
    # print("explode", repr(root), repr(node), repr(left), repr(right))
    if left:
        left.value += node.children[0].value
    if right:
        right.value += node.children[1].value

    node.children = []
    node.value = 0

    return True


def split(root):
    def find(node):
        if node.value > 9:
            return node
        if node.value > -1:
            return
        for child in node.children:
            res = find(child)
            if res is not None:
                return res

    node = find(root)
    if node is None:
        return False
    # print("split", repr(root), repr(node))
    node.children = [
        Node(node, node.value // 2),
        Node(node, node.value - node.value // 2),
    ]
    node.value = -1
    return True


def add(root1, root2):
    root = Node()
    root.children = [root1, root2]
    root1.parent = root
    root2.parent = root
    while explode(root) or split(root):
        pass
    return root


line = "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]"
o = repr(parse(line))
assert o == line, o
line = "[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]"
o = repr(parse(line))
assert o == line, o

for line, sol in [
    ("[[[[[9,8],1],2],3],4]", "[[[[0,9],2],3],4]"),
    ("[7,[6,[5,[4,[3,2]]]]]", "[7,[6,[5,[7,0]]]]"),
    ("[[6,[5,[4,[3,2]]]],1]", "[[6,[5,[7,0]]],3]"),
    ("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"),
    ("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"),
]:
    root = parse(line)
    explode(root)
    assert repr(root) == sol, repr(root)

root = Node()
root.children = [Node(root, 10), Node(root, 9)]
split(root)
assert repr(root) == "[[5,5],9]", repr(root)

for line, sol in [
    ("[[1,2],[[3,4],5]]", 143),
    ("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]", 1384),
    ("[[[[1,1],[2,2]],[3,3]],[4,4]]", 445),
    ("[[[[3,0],[5,3]],[4,4]],[5,5]]", 791),
]:
    root = parse(line)
    assert root.magnitude() == sol, repr(root)


with open(sys.argv[1], "rt") as f:
    ls = [line.strip() for line in f]
m = 0
for i in range(len(ls)):
    for j in range(len(ls)):
        if i != j:
            m = max(add(parse(ls[i]), parse(ls[j])).magnitude(), m)
print(m)
