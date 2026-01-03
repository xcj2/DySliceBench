class Graph():  #non-directed
    def __init__(self, n, edge, indexed=1):
        self.n = n
        self.edge = edge
        self.indexed = indexed
        self.graph = [[] for _ in range(n)]
        for e in edge:
            self.graph[e[0] - indexed].append((e[1] - indexed, e[2]))
            self.graph[e[1] - indexed].append((e[0] - indexed, e[2]))

    def kruskal(self):  #UnionFind
        edgemap = {self.edge[i]: i for i in range(len(self.edge))}
        sortedge = sorted(self.edge, key=lambda x: x[2])
        #sortedge = reversed(sortedge) コストの最大化
        uf = UnionFind(self.n)
        res = 0
        restored = []
        for e in sortedge:
            if uf.find(e[0] - self.indexed) != uf.find(e[1] - self.indexed):
                res += e[2]
                restored.append(edgemap[e])
                uf.unite(e[0] - self.indexed, e[1] - self.indexed)
        return res, restored

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        root = x
        while self.parents[root] != root:
            root = self.parents[root]
        while self.parents[x] != root:
            parent = self.parents[x]
            self.parents[x] = root
            x = parent
        return root

    def unite(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot: return
        xrank = self.rank[xroot]
        yrank = self.rank[yroot]
        if xrank < yrank:
            self.parents[xroot] = yroot
            self.size[yroot] += self.size[xroot]
        elif xrank == yrank:
            self.parents[yroot] = xroot
            self.rank[yroot] += 1
            self.size[xroot] += self.size[yroot]
        else:
            self.parents[yroot] = xroot
            self.size[xroot] += self.size[yroot]

import sys
input = sys.stdin.readline

N = int(input())
T = []

for i in range(N):
    x, y = map(int, input().split())
    T.append((x, y, i))

sort_by_x = sorted(T, key=lambda x: x[0])
sort_by_y = sorted(T, key=lambda x: x[1])

E = []

for i in range(N - 1):
    x1, y1, id1 = sort_by_x[i]
    x2, y2 ,id2 = sort_by_x[i + 1]
    E.append((id1, id2, min(abs(x1 - x2), abs(y1 - y2))))
    x1, y1, id1 = sort_by_y[i]
    x2, y2 ,id2 = sort_by_y[i + 1]
    E.append((id1, id2, min(abs(x1 - x2), abs(y1 - y2))))

g = Graph(N, E)

print(g.kruskal()[0])