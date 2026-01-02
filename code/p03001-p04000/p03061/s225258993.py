# import numpy as np
import sys, math
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial, gcd
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10 ** 7)
enu = enumerate
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline()[:-1]
pl = lambda x: print(*x, sep="\n")


class SegmentTree:
    def __init__(self, size, f=lambda x, y: x + y, default=0):
        self.size = 2 ** (size - 1).bit_length()
        self.default = default
        self.dat = [default] * (self.size * 2)
        self.f = f

    def update(self, i, x):
        i += self.size
        self.dat[i] = x
        while i > 0:
            i >>= 1
            self.dat[i] = self.f(self.dat[i * 2], self.dat[i * 2 + 1])

    def query(self, l, r):
        """return f([l,r))
        """
        l += self.size
        r += self.size
        lres, rres = self.default, self.default
        while l < r:
            if l & 1:
                lres = self.f(lres, self.dat[l])
                l += 1

            if r & 1:
                r -= 1
                rres = self.f(self.dat[r], rres)
            l >>= 1
            r >>= 1
        res = self.f(lres, rres)
        return res


N = int(input())
A = list(map(int, input().split()))
s = SegmentTree(N, gcd, 0)
for i, a in enu(A):
    s.update(i, a)

res = 0
for i in range(N):
    val = gcd(s.query(0, i), s.query(i + 1, N))
    if res < val:
        res = val
print(res)

