class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.sizes = [0]*n

    def find(self, x):
        if x == self.par[x]:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            retrn;
        if self.sizes[x] < self.sizes[y]:
            x,y = y,x

        self.par[y] = x;
        self.sizes[x] += self.sizes[y]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, a):
        return sizes[self.find[x]]

class Edge:
    def __init__(self, s, t, w):
        self.s = s
        self.t = t
        self.w = w
    def __lt__(self, other):
        return self.w < other.w

def kruskal(edges, n):
    edges = sorted(edges)
    uf = UnionFind(n)
    min_cost = 0

    for edge in edges:
        if not uf.same(edge.s, edge.t):
            min_cost += edge.w
            uf.unite(edge.s, edge.t)

    return min_cost

v, e = map(int, input().split())
es = []
for i in range(e):
    s, t, w = map(int, input().split())
    es.append(Edge(s, t, w))
print(kruskal(es, v))

