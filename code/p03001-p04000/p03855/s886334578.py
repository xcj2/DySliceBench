from collections import Counter

class UnionFind:
    def __init__(self, N):
        self.p = list(range(N))
        self.rank = [0] * N
        self.size = [1] * N

    def find_root(self, x):
        if self.p[x] != x:
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
            self.size[v] += self.size[u]
            self.size[u] = 0
        else:
            self.p[v] = u
            self.size[u] += self.size[v]
            self.size[v] = 0

            if self.rank[u] == self.rank[v]:
                self.rank[u] += 1

    def get_size(self, x):
        return self.size[self.find_root(x)]


n, K, L = map(int, input().split())
pq = [tuple(int(x)-1 for x in input().split()) for _ in range(K)]
rs = [tuple(int(x)-1 for x in input().split()) for _ in range(L)]

uk = UnionFind(n)
for p, q in pq:
    uk.unite(p, q)

ul = UnionFind(n)
for p, q in rs:
    ul.unite(p, q)

res = [uk.find_root(i) * 1000000 +  ul.find_root(i) for i in range(n)]
c = Counter(res)
ans = [0] * n

for i in range(n):
    ans[i] = c[res[i]]

print(*ans, sep=' ')

