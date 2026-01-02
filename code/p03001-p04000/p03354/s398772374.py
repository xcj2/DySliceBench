#!/usr/bin/env python3
import sys
input = sys.stdin.readline

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

n, m = map(int, input().split())
*p, = map(int, input().split())
UF = UnionFind(n, m, read = 1)

a = 0
for i in range(n):
    P = p[i] - 1
    if UF.same(P, i):
        a += 1
print(a)