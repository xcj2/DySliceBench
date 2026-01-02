
from bisect import bisect_left
from math import ceil
import sys
if sys.version_info[0:2] >= (3, 3):
    from collections.abc import Sequence
else:
    from collections import Sequence


class LazySequence(Sequence):
    def __init__(self, f, n):
        self.f = f
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, i):
        if not (0 <= i < self.n):
            raise IndexError
        return self.f(i)


class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def __len__(self):
        return self.size

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, v):
        while i <= self.size:
            self.tree[i] += v
            i += i & -i


N = int(input())
a = [0] + [int(s) for s in input().split()]
# a = [0] * (N + 1)


def count_lr(x):
    s = [0] * (N + 1)
    for i in range(1, N + 1):
        s[i] = s[i - 1] + (1 if a[i] >= x else -1)

    ss = sorted(set(s))
    ind = {v: i + 1 for i, v in enumerate(ss)}

    b = Bit(N + 10)
    count = 0
    for i in range(N + 1):
        j = ind[s[i]]
        count += b.sum(j)
        b.add(j, 1)

    return count


# i: 0, 1, ..., 10 ** 9
# x: 10 ** 9, ..., 0
counts = LazySequence(lambda i: count_lr(10 ** 9 - i), 10 ** 9 + 1)
ans = 10 ** 9 - bisect_left(counts, ceil(N * (N + 1) / 4))
print(ans)
