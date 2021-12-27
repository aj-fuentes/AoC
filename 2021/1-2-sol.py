import itertools
import operator
import sys

c = 0
vals = list(map(lambda l: int(l.strip()), open(sys.argv[1], "rt")))
acc = [0] + list(itertools.accumulate(vals, operator.add))
for i in range(4, len(acc)):
    c += (acc[i] - acc[i - 3]) > (acc[i - 1] - acc[i - 4])
print(c)
