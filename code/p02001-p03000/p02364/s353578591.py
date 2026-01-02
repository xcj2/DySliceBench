class DisjointSet:
    def __init__(self, size):
        self.rank = [0] * size
        self.p = list(range(size))

    def findSet(self, x):
        if x != self.p[x]:
            self.p[x] = self.findSet(self.p[x])
        return self.p[x]

    def same(self, x, y):
        return self.findSet(x) == self.findSet(y)

    def link(self, x, y):
        if self.rank[x] > self.rank[y]:
            self.p[y] = x
        else:
            self.p[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def unite(self, x, y):
        self.link(self.findSet(x), self.findSet(y))


class Edge:
    def __init__(self, source=0, target=0, cost=0):
        self.source = source
        self.target = target
        self.cost = cost

def kruskal(n, edges):
    totalCost = 0
    edges.sort(key=lambda e: e.cost)
    dset = DisjointSet(n)

    for e in edges:
        if not dset.same(e.source, e.target):
            totalCost += e.cost
            dset.unite(e.source, e.target)

    return totalCost


if __name__ == '__main__':
    n, m = [int(v) for v in input().split()]
    edges = []
    for i in range(m):
        s, t, w = [int(v) for v in input().split()]
        edges.append(Edge(s, t, w))

    print(kruskal(n, edges))
