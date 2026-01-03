# ABC065d
import sys
from operator import itemgetter
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dist(x1, y1, x2, y2):
    return min(abs(x1-x2), abs(y1-y2))


n = int(input())
Aedges = []
Aedges2 = []
for i in range(n):
    x, y = map(int, input().split())
    Aedges.append((x, y, i))
    Aedges2.append((x, y, i))
Aedges.sort()
Aedges2.sort(key=itemgetter(1))
# print(Aedges)
# print(Aedges2)

edges = []

for i in range(1, n):
    edges.append((Aedges[i][0]-Aedges[i-1][0], Aedges[i][2], Aedges[i-1][2]))
for i in range(1, n):
    edges.append((Aedges2[i][1]-Aedges2[i-1][1],
                  Aedges2[i][2], Aedges2[i-1][2]))

edges.sort()


class UnionFind:
    def __init__(self, n):
        self.tree = [i for i in range(n)]

    def root(self, x):
        if(self.tree[x] == x):
            return x
        self.tree[x] = self.root(self.tree[x])
        return self.tree[x]  # 経路圧縮

    def same(self, x, y):  # xとyが同じ木に属するか
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if(x == y):
            return
        self.tree[x] = y


def kruskal(n, edges):  # edges: wでソート済み
    U = UnionFind(n)
    res = 0
    for e in edges:
        w, s, t = e
        if not U.same(s, t):
            res += w
            U.unite(s, t)
    return res


print(kruskal(n, edges))
