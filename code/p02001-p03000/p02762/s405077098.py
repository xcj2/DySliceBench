#!/usr/bin/env python3
def inp():
        n, m = map(int, input().split())
        return n - 1, m - 1

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

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

def rem(cand, p, q):
    cand[p] += 1
    cand[q] += 1

n, m, k = map(int, input().split())
UF = UnionFind(n)
non_cand = [1] * n
for _ in range(m):
    a, b = inp()
    UF.union(a, b)
    rem(non_cand, a, b)
for _ in range(k):
    c, d = inp()
    if UF.same(c, d):
        rem(non_cand, c, d)

ans = [UF.size(i) - non_cand[i] for i in range(n)]

print(*ans)