class Node():
    def __init__(self, id):
        self.id = id
        self.p = self
        self.rank = 0


class DisjointSet():
    def __init__(self, n):
        self.nodes = {}
        for i in range(n):
            self.makeSet(i)

    def makeSet(self, i):
        self.nodes[i] = Node(i)

    def findSet(self, x):
        if x.p is not x:
            x.p = self.findSet(x.p)
        return x.p

    def unite(self, x, y):
        # ランクの低い方を子にする
        px = self.findSet(x)
        py = self.findSet(y)
        if px.rank > py.rank:
            py.p = px
        else:
            px.p = py
        if x.rank == y.rank:
            py.rank += 1

    def bool(self, x, y):
        return self.findSet(x) == self.findSet(y)


n, q = map(int, input().split())
uf = DisjointSet(n)
for i in range(q):
    com, ix, iy = map(int, input().split())
    if com == 0:
        # unite
        uf.unite(uf.nodes[ix], uf.nodes[iy])
    else:
        # same
        print(1 if uf.bool(uf.nodes[ix], uf.nodes[iy]) else 0)

