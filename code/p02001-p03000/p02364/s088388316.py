import heapq

v, e = map(int, input().split())
edges = []
for i in range(e):
    s, t, w = map(int, input().split())
    heapq.heappush(edges, (w, (s, t)))


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


def kruskal(v, edges):
    S = DisjointSet(v)
    K = []

    while len(edges):
        w, edge = heapq.heappop(edges)
        # sorceとtargetがdisjointなら追加
        x, y = S.nodes[edge[0]], S.nodes[edge[1]]
        if not S.bool(x, y):
            S.unite(x, y)
            K.append((edge, w))
    return K


K = kruskal(v, edges)
# print(K)
print(sum(map(lambda x: x[1], K)))

