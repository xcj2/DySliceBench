import sys
from collections import defaultdict

input = sys.stdin.readline


class UnionFind(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x

    def is_same(self, x, y):
        return self.find(x) == self.find(y)


N, K, L = map(int, input().split())

uf1 = UnionFind(N)
for _ in range(K):
    p, q = map(int, input().split())
    uf1.union(p - 1, q - 1)

uf2 = UnionFind(N)
for _ in range(L):
    s, t = map(int, input().split())
    uf2.union(s - 1, t - 1)

c = defaultdict(int)
for i in range(N):
    x = uf1.find(i)
    y = uf2.find(i)
    c[(x, y)] += 1

for i in range(N):
    x = uf1.find(i)
    y = uf2.find(i)
    print(c[(x, y)], end=' ')
print()
