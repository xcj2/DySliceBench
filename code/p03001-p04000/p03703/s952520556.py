import sys
from itertools import accumulate

import numpy as np


class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


n, k = map(int, input().split())
aaa = [0] + list(map(int, sys.stdin))
acc = [a - i * k for i, a in enumerate(accumulate(aaa))]
values = sorted(set(acc))
dct = {v: i for i, v in enumerate(values, start=1)}
bit = Bit(len(values))
ans = 0
for d in acc:
    i = dct[d]
    ans += bit.sum(i)
    bit.add(i, 1)
print(ans)
