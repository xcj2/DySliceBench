import sys
input = sys.stdin.readline
N,M = map(int,input().split())
L = [list(map(int,input().split())) for i in range(N)]

from collections import defaultdict
d = defaultdict(lambda: [])
for i,ls in enumerate(L):
    for l in ls[1:]:
        d[l].append(i)

class UnionFind:
    def __init__(self,N):
        self.parent = [i for i in range(N)]
        self._size = [1] * N
        self.count = 0
    def root(self,a):
        if self.parent[a] == a:
            return a
        else:
            self.parent[a] = self.root(self.parent[a])
            return self.parent[a]
    def is_same(self,a,b):
        return self.root(a) == self.root(b)
    def unite(self,a,b):
        ra = self.root(a)
        rb = self.root(b)
        if ra == rb: return
        if self._size[ra] < self._size[rb]: ra,rb = rb,ra
        self._size[ra] += self._size[rb]
        self.parent[rb] = ra
        self.count += 1
    def size(self,a):
        return self._size[self.root(a)]

uf = UnionFind(N)

for ls in d.values():
    for a,b in zip(ls,ls[1:]):
        if uf.is_same(a,b): continue
        uf.unite(a,b)

print('YES' if uf.size(0)==N else 'NO')