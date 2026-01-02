N,M = map(int,input().split())
P = list(map(int,input().split()))
XY = [tuple(map(int,input().split())) for i in range(M)]

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
for x,y in XY:
    x,y = x-1,y-1
    if uf.is_same(x,y): continue
    uf.unite(x,y)
for i in range(N):
    uf.root(i)

from collections import defaultdict
ps = defaultdict(lambda: set())
ids = defaultdict(lambda: set())
rs = set()
for i,p in enumerate(P):
    r = uf.root(i)
    ps[r].add(p-1)
    ids[r].add(i)
    rs.add(r)

ans = 0
for r in rs:
    ans += len(ps[r] & ids[r])
print(ans)