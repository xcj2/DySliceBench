N,K,L = map(int,input().split())
PQ = [tuple(map(int,input().split())) for i in range(K)]
RS = [tuple(map(int,input().split())) for i in range(L)]

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

roads = UnionFind(N)
rails = UnionFind(N)
for p,q in PQ:
    p,q = p-1,q-1
    roads.unite(p,q)
for r,s in RS:
    r,s = r-1,s-1
    rails.unite(r,s)
for i in range(N):
    roads.root(i)
    rails.root(i)

from collections import Counter
ctr = Counter()
for i in range(N):
    ctr[(roads.parent[i], rails.parent[i])] += 1
ans = []
for i in range(N):
    ans.append(ctr[(roads.parent[i], rails.parent[i])])
print(*ans)