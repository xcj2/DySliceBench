import sys
from collections import defaultdict

sys.setrecursionlimit(1000000)
input = lambda: sys.stdin.readline().rstrip()


class UnionFind:
    def __init__(self, size):
        self.par = [i for i in range(size)]
        self.rk = [0] * size

    def find(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rk[x] < self.rk[y]:
            self.par[x] = y
        elif self.rk[x] > self.rk[y]:
            self.par[y] = x
        else:
            self.par[x] = y
            self.rk[y] += 1


N, M, K = map(int, input().split())
uf = UnionFind(N)
friend = defaultdict(set)
for _ in range(M):
    a, b = map(lambda x: int(x) - 1, input().split())
    uf.unite(a, b)
    friend[a].add(b)
    friend[b].add(a)

block = defaultdict(set)
for _ in range(K):
    c, d = map(lambda x: int(x) - 1, input().split())
    block[c].add(d)
    block[d].add(c)

group = defaultdict(set)
for i in range(N):
    group[uf.find(i)].add(i)

ans = [0] * N
for people in group.values():
    for p in people:
        ans[p] = len(people) - 1 - sum(1 if i in people else 0 for i in friend[p]) - sum(1 if i in people else 0 for i in block[p])

print(' '.join(map(str, ans)))


