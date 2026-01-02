class DisjointSet():
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * (n)

    def make_set(self, x):
        self.par[x] = x
        self.rank[x] = 0

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.find(self.par[x])

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same_check(self, x, y):
        return self.find(x) == self.find(y)

class Edge():
    def __init__(self, source=0, target=0, cost=0):
        self.source = source
        self.target = target
        self.cost = cost

    def __lt__(self, e):
        return self.cost < e.cost

def kruskal(N, edges):
    # 今回は総コストのみ
    total_cost = 0
    edges = sorted(edges)

    dset = DisjointSet(N)

    source, target = 0, 0
    for i in range(E):
        e = edges[i]
        if not dset.same_check(e.source, e.target):
            total_cost += e.cost
            dset.unite(e.source, e.target)
    return total_cost

V, E = list(map(int, input().split(' ')))
edges = []
for i in range(E):
    s, t, d = list(map(int, input().split(' ')))
    edges.append(Edge(s, t, d))
print(kruskal(V, edges))

