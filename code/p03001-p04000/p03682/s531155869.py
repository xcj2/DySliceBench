# D - Built?

import sys

class UnionFind(object):
    def __init__(self, n=1):
        self.root = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find_root(self, x):
        if self.root[x] == x:
            return x
        else:
            self.root[x] = self.find_root(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find_root(x)
        y = self.find_root(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.root[y] = x

    def is_same_root(self, x, y):
        return self.find_root(x) == self.find_root(y)

# edges : [[start, end, edge_weight], ...]
def kruskal(max_v, edges):
    uf = UnionFind(max_v)
    sum_cost = 0
    edges.sort(key = lambda x: x[2])
    for e in edges:
        if not uf.is_same_root(e[0], e[1]):
            uf.unite(e[0], e[1])
            sum_cost += e[2]
    return sum_cost


N = int(sys.stdin.buffer.readline())
xyi = []
for i in range(N):
    x, y = map(int, sys.stdin.buffer.readline().split())
    xyi.append([x,y,i])

edges = []
xyi.sort(key = lambda x:x[0])
for j in range(N):
    if 0 < j:
        edges.append([xyi[j-1][2], xyi[j][2], xyi[j][0]-xyi[j-1][0]])
    if j < N-1:
        edges.append([xyi[j][2], xyi[j+1][2], xyi[j+1][0]-xyi[j][0]])

xyi.sort(key=lambda x: x[1])
for j in range(N):
    if 0 < j:
        edges.append([xyi[j-1][2], xyi[j][2], xyi[j][1]-xyi[j-1][1]])
    if j < N-1:
        edges.append([xyi[j][2], xyi[j+1][2], xyi[j+1][1]-xyi[j][1]])

print(kruskal(N, edges))
