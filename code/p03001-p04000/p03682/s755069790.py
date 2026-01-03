import sys
sys.setrecursionlimit(10**7)
from collections import defaultdict

import collections
import itertools
import operator


class UnionFind:
    def __init__(self, elems=None):
        class KeyDict(dict):
            def __missing__(self, key):
                self[key] = key
                return key

        self.parent = KeyDict()
        self.rank = collections.defaultdict(int)

        if elems is not None:
            for elem in elems:
                _, _ = self.parent[elem], self.rank[elem]

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

    def are_same(self, x, y):
        return self.find(x) == self.find(y)

    def grouper(self):
        roots = [(x, self.find(x_par)) for x, x_par in self.parent.items()]
        root = operator.itemgetter(1)
        for _, group in itertools.groupby(sorted(roots, key=root), root):
            yield [x for x, _ in group]


'''
def init(n):
    return list(range(n+1))#
def find(lis, x):
    if lis[x] == x:
        return x
    else:
        lis[x] = find(lis, lis[x])
        return lis[x]

def sameset(lis, x, y):
    return find(lis, x) == find(lis, y)

def union(lis, x, y):
    x = find(lis, x)
    y = find(lis, y)
    if x != y:
        lis[x] = y
'''

N = int(input())
#union_find_tree = init(N)

town = []

for i in range(N):
    x, y = map(int, input().split())
    town.append((i, x, y))

x_sorted_town = sorted(town, key=lambda x: x[1])
y_sorted_town = sorted(town, key=lambda x: x[2])

graph = []

pre_tx = x_sorted_town[0]
pre_ty = y_sorted_town[0]
pre_nx = town[pre_tx[0]]
pre_ny = town[pre_ty[0]]
for tx, ty in zip(x_sorted_town[1:], y_sorted_town[1:]):
    nx = town[tx[0]]
    ny = town[ty[0]]
    wx = min(abs(tx[1] - pre_tx[1]), abs(nx[2] - pre_nx[2]))
    wy = min(abs(ty[2] - pre_ty[2]), abs(ny[1] - pre_ny[1]))
    graph.append((nx[0], pre_nx[0], wx))
    graph.append((ny[0], pre_ny[0], wy))
    pre_tx = tx
    pre_ty = ty
    pre_nx = nx
    pre_ny = ny

uf = UnionFind()

cost = 0
for (s,t,w) in sorted(graph, key=lambda x: x[2]):
    if not uf.are_same(s,t):
        uf.unite(s,t)
        cost += w
print(cost)