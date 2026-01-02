class UF:
    def __init__(self, n):
        self.N = n;
        self.d = [-1]*n
    
    def size(self, a):
        x = self.root(a)
        return -self.d[x]

    def root(self, a):
        if self.d[a] < 0:
            return a
        else:
            self.d[a] = self.root(self.d[a])
            return self.d[a]

    def unite(self, a, b):
        x = self.root(a)
        y = self.root(b)
        if self.size(x) < self.size(y):
            x, y = y, x
        self.d[y] = x
    
    def same(self, a, b):
        return self.root(a) == self.root(b)

class Edge:
    def __init__(self, f, t, w):
        self.f = f
        self.t = t
        self.w = w
    def __lt__(self, other):
        return self.w < other.w


def kruskal(edges, n):
    uf = UF(n)
    sum = 0
    for e in sorted(edges):
        if not uf.same(e.f, e.t):
            uf.unite(e.f, e.t)
            sum += e.w
    return sum


n, m = map(int, input().split())
es = []
for i in range(m):
    s, t, w = map(int, input().split())
    es.append(Edge(s, t, w))
print(kruskal(es, n))