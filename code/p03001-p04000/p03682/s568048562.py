import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def main():
    N = I()
    points = []
    G = [[] for _ in range(N)]
    Point = collections.namedtuple('Point', ['n', 'x', 'y'])
    Edge = collections.namedtuple('Edge', ['fr', 'to', 'cost'])
    for i in range(N):
        x, y = LI()
        points.append(Point(i, x, y))
    x_sorted = sorted(points, key=lambda p: p.x)
    y_sorted = sorted(points, key=lambda p: p.y)
    edges = []
    for i in range(N-1):
        p1, p2 = x_sorted[i], x_sorted[i+1]
        cost = p2.x - p1.x
        assert cost >= 0
        edges.append(Edge(p1.n, p2.n, cost))
        edges.append(Edge(p2.n, p1.n, cost))

        p3, p4 = y_sorted[i], y_sorted[i+1]
        cost = p4.y - p3.y
        assert cost >= 0
        edges.append(Edge(p3.n, p4.n, cost))
        edges.append(Edge(p4.n, p3.n, cost))

    # E = 2V, let's prim
    sorted_edge = sorted(edges, key=lambda x: x.cost)
    uf = UnionFind(N)
    res = 0
    for i in range(len(sorted_edge)):
        edge = sorted_edge[i]
        if not uf.same(edge.fr, edge.to):
            uf.union(edge.fr, edge.to)
            res += edge.cost
    print(res)

main()

