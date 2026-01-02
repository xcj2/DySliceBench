N,M,K = map(int,input().split())
AB = [tuple(map(int,input().split())) for i in range(M)]
CD = [tuple(map(int,input().split())) for i in range(K)]

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

blocks = [[] for _ in range(N)]
for c,d in CD:
    c,d = c-1,d-1
    blocks[c].append(d)
    blocks[d].append(c)

friends = [0] * N
uf = UnionFind(N)
for a,b in AB:
    a,b = a-1,b-1
    friends[a] += 1
    friends[b] += 1
    if uf.is_same(a,b): continue
    uf.unite(a,b)
for i in range(N):
    uf.root(i)

from collections import Counter
ctr = Counter()
for i in range(N):
    r = uf.root(i)
    ctr[r] += 1

ans = []
for i in range(N):
    tmp = ctr[uf.root(i)] - 1 - friends[i]
    for b in blocks[i]:
        if uf.is_same(i,b):
            tmp -= 1
    ans.append(tmp)
print(*ans)