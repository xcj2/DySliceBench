from collections import Counter
N,K,L = map(int,input().split())
roads = [tuple(map(lambda x:int(x)-1,input().split())) for i in range(K)]
rails = [tuple(map(lambda x:int(x)-1,input().split())) for i in range(L)]

class UnionFind:
    def __init__(self,N):
        self.parent = [i for i in range(N)]
        self.rank = [0] * N
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
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        else:
            self.parent[rb] = ra
            if self.rank[ra] == self.rank[rb]: self.rank[ra] += 1
        self.count += 1

uf_road = UnionFind(N)
for a,b in roads:
    if uf_road.is_same(a,b): continue
    uf_road.unite(a,b)

uf_rail = UnionFind(N)
for a,b in rails:
    if uf_rail.is_same(a,b): continue
    uf_rail.unite(a,b)

for i in range(N):
    uf_road.root(i)
    uf_rail.root(i)

ctr = Counter()
for i in range(N):
    r1 = uf_road.root(i)
    r2 = uf_rail.root(i)
    ctr[(r1,r2)] += 1

ans = []
for i in range(N):
    r1 = uf_road.root(i)
    r2 = uf_rail.root(i)
    ans.append(ctr[(r1,r2)])
print(*ans)