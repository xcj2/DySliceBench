from collections import Counter

N, M, K = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(M)]
CD = [tuple(map(int, input().split())) for _ in range(K)]


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def root(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)
        if self.rank[x] > self.rank[y]:
            self.parent[root_y] = root_x
        elif self.rank[x] < self.rank[y]:
            self.parent[root_x] = root_y
        elif root_x != root_y:
            self.parent[root_y] = root_x
            self.rank[x] += 1
        pass


uf = UnionFind(N)

for a, b in AB:
    uf.unite(a - 1, b - 1)

roots = [uf.root(i) for i in range(N)]
counter_roots = Counter(roots)

ans = [counter_roots[roots[i]] - 1 for i in range(N)]

for a, b in AB:
    if roots[a - 1] == roots[b - 1]:
        ans[a - 1] -= 1
        ans[b - 1] -= 1
for a, b in CD:
    if roots[a - 1] == roots[b - 1]:
        ans[a - 1] -= 1
        ans[b - 1] -= 1

print(*ans)
