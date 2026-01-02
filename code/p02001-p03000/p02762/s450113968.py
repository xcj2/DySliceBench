from collections import Counter


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.p = [e for e in range(n)]
        self.rank = [0] * n

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

    def update_p(self):
        for u in range(self.n):
            self.find_set(u)


n, m, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
cd = [list(map(int, input().split())) for _ in range(k)]

uf = UnionFind(n)

for a, b in ab:
    a -= 1
    b -= 1
    uf.unite(a, b)

uf.update_p()

counter = Counter(uf.p)

ans = [counter[uf.p[i]] - 1 for i in range(n)]


def f(li):
    for e1, e2 in li:
        e1 -= 1
        e2 -= 1
        if uf.same(e1, e2):
            ans[e1] -= 1
            ans[e2] -= 1


f(ab)
f(cd)

print(*ans)
