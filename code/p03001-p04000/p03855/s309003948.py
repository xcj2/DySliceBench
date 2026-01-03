#!/usr/bin/env python3
class UnionFind():
    def __init__(self, n, m = None, read = 0):
        self.n = n
        self.parents = [-1] * n
        if read:
            if m is None:
                raise ValueError("What is M")
            for i in range(m):
                a, b = map(int, input().split())
                self.union(a - 1, b - 1)

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

C = []
n, k, l = map(int, input().split())
UF_R = UnionFind(n, k, 1)
UF_T = UnionFind(n, l, 1)
for i in range(n):
    R = UF_R.find(i)
    T = UF_T.find(i)
    C += (R, T),
from collections import*
c = Counter(C)
print(*[c[g] for g in C])