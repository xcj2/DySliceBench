import sys
from collections import defaultdict
from heapq import heappop, heappush
from operator import itemgetter

readline = sys.stdin.readline

N = int(readline())
town = [None] * N
for i in range(N):
    x, y = map(int, readline().split())
    town[i] = (i, x, y)

class UnionFind(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

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

    def is_same(self, x, y):
        return self.find(x) == self.find(y)


def Kruskal(edges):
    edge = []
    total = 0

    uf = UnionFind(N)
    Q = sorted(edges, reverse=True)

    while len(edge) < N - 1 and Q:
        cost, e = Q.pop()
        if uf.find(e[0]) != uf.find(e[1]):
            total += cost
            edge.append(edge)
            uf.union(*e)
    return total


edges = []
for xy in [1, 2]:
    town = sorted(town, key=itemgetter(xy))
    for i in range(N - 1):
        t1, t2 = town[i], town[i + 1]
        d = t2[xy] - t1[xy]
        edges.append((d, (t1[0], t2[0])))
print(Kruskal(edges))
