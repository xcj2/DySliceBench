N, K, L = map(int, input().split())
pq = [map(int, input().split()) for _ in range(K)]
rs = [map(int, input().split()) for _ in range(L)]

class UnionFind:
    def __init__(self, N):
        self.par = [None] * (N+1)
        self.rank = [None] * (N+1)
        for n in range(N+1):
            self.par[n] = n
            self.rank[n] = 1

    def root(self, x):
        if self.par[x] == x:
            return x
        r = self.root(self.par[x])
        self.par[x] = r
        return r

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx != ry:
            if self.rank[rx] > self.rank[ry]:
                self.par[ry] = rx
            else:
                self.par[rx] = ry
                if self.rank[rx] == self.rank[ry]:
                    self.rank[ry] += 1

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

uf_road = UnionFind(N)
uf_train = UnionFind(N)

for p, q in pq:
    uf_road.unite(p, q)
for r, s in rs:
    uf_train.unite(r, s)

from collections import Counter
c = Counter()
for i in range(1, N+1):
    k = (uf_road.root(i), uf_train.root(i))
    c[k] += 1

ret = []
for i in range(1, N+1):
    k = (uf_road.root(i), uf_train.root(i))
    ret.append(c[k])

print(" ".join(str(v) for v in ret))
