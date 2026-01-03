class UnionFind(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]

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
            self.size[x] += self.size[y]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        x = self.find(x)
        return self.size[x]


def kruskal(n, edges):
    """
    Solve Minimum Spanning Tree by Kruskal's algorithm.
    :param n: Number of nodes
    :param edges: [u, v, cost]
    :return: Total cost
    """
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    total_cost = 0
    for u, v, c in edges:
        if not uf.is_same(u, v):
            total_cost += c
            uf.union(u, v)
    return total_cost


N = int(input())

X, Y = [], []

for i in range(N):
    x, y = map(int, input().split())
    X.append((x, i))
    Y.append((y, i))

X.sort()
Y.sort()

edges = []

for x1, x2 in zip(X[:-1], X[1:]):
    edges.append([x1[1], x2[1], x2[0] - x1[0]])

for y1, y2 in zip(Y[:-1], Y[1:]):
    edges.append([y1[1], y2[1], y2[0] - y1[0]])

print(kruskal(N, edges))