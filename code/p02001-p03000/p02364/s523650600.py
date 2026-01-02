import sys
readline = sys.stdin.readline
from operator import itemgetter
class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [0] * n
    def find_root(self, x):
        if x != self.p[x]:
            self.p[x] = self.find_root(self.p[x])
        return self.p[x]
    def same(self, x, y):
        return self.find_root(x) == self.find_root(y)
    def unite(self, x, y):
        u = self.find_root(x)
        v = self.find_root(y)
        if u == v: return
        if self.rank[u] < self.rank[v]:
            self.p[u] = v
        else:
            self.p[v] = u
            if self.rank[u] == self.rank[v]:
                self.rank[u] += 1
n, m = map(int, readline().split())
edges = [None] * m
for i in range(m):
    s, t, w = map(int, readline().split())
    edges[i] = (s, t, w)
edges.sort(key=itemgetter(2), reverse=True)
uf = UnionFind(n)
ans = 0
for _ in [0] * (n - 1):
    while edges:
        s, t, w = edges.pop()
        if not uf.same(s, t):
            uf.unite(s, t)
            break
    ans += w
print(ans)