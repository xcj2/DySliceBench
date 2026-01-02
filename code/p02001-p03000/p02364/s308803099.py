import sys
input = sys.stdin.buffer.readline
from operator import itemgetter


class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n

    def root(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def merge(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x != y:
            if self.parent[x] > self.parent[y]:
                x, y = y, x
            self.parent[x] += self.parent[y]
            self.parent[y] = x

    def is_same(self, x, y):
        return self.root(x) == self.root(y)


def kruskal(n, edges):
    """クラスカル法によって最小全域木の重みを求める"""
    sorted_edges = sorted(edges, key=itemgetter(2))
    uf = UnionFind(n)
    res = 0
    for u, v, cost in sorted_edges:
        if not uf.is_same(u, v):
            uf.merge(u, v)
            res += cost
    return res


n, m = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(m)]


ans = kruskal(n, edges)
print(ans)
