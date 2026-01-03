class UnionFind:
    def __init__(self, N):
        self.parent = list(range(N))
        self.rank = [0] * N
        self.size = [1] * N

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.size[y] += self.size[x]
        else:
            self.parent[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]

def kruskal(edges, size):
    uf = UnionFind(size)
    edges = sorted(edges, key=lambda e: e[2])
    ret = 0
    for u, v, weight in edges:
        if not uf.same(u, v):
            uf.unite(u, v)
            ret += weight
    return ret

N = int(input())
x = [0] * N
y = [0] * N
for i in range(N):
    a, b = map(int, input().split())
    x[i] = (a, i)
    y[i] = (b, i)
x.sort()
y.sort()
edges = []
for i in range(N-1):
    x1, u = x[i]
    x2, v = x[i+1]
    edges.append((u, v, x2 - x1))
    y1, u = y[i]
    y2, v = y[i+1]
    edges.append((u, v, y2 - y1))
ans = kruskal(edges, N)
print(ans)