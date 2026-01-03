from collections import Counter

n, k, l = map(int, input().split())
pq = [list(map(int, input().split())) for _ in range(k)]
rs = [list(map(int, input().split())) for _ in range(l)]


class UnionFind:
    def __init__(self, x):
        self.p = [e for e in range(x)]
        self.rank = [0] * x

    def same(self, u, v):
        return self.find_set(u) == self.find_set(v)

    def unite(self, u, v):
        self.link(self.find_set(u), self.find_set(v))

    def find_set(self, u):
        if u != self.p[u]:
            self.p[u] = self.find_set(self.p[u])

        return self.p[u]

    def link(self, u, v):
        if self.rank[u] > self.rank[v]:
            self.p[v] = u
        else:
            self.p[u] = v
            if self.rank[u] == self.rank[v]:
                self.rank[v] += 1


road_uf = UnionFind(n)
train_uf = UnionFind(n)

for p, q in pq:
    p -= 1
    q -= 1
    road_uf.unite(p, q)

for r, s in rs:
    r -= 1
    s -= 1
    train_uf.unite(r, s)

group = [(road_uf.find_set(i), train_uf.find_set(i)) for i in range(n)]

c = Counter(group)

ans = []
for e in group:
    ans.append(c[e])

print(*ans)
