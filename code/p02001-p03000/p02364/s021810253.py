def kruskal(g, size):
    g.sort(key=itemgetter(2), reverse=True)
    uf = union_find(size)
    tree = []
    while len(tree) < size - 1:
        u, v, d = g.pop()
        if not uf.union(u, v):
            tree.append((u, v, d))
    return tree

class union_find:
    def __init__(self, size):
        self.table = [-1 for _ in range(size)]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:return True
        
        if self.table[y] < self.table[x]:x, y = y, x

        self.table[x] += self.table[y]
        self.table[y] = x
        return False
            
    def find(self, x):
        if self.table[x] < 0:return x
        self.table[x] = self.find(self.table[x])
        return self.table[x]

from sys import stdin
from operator import itemgetter

import heapq

readline = stdin.readline


v, e = map(int, readline().split())

g = [list(map(int, readline().split())) for _ in range(e)]

tree = kruskal(g, v)

print(sum(d for s, t, d in tree))