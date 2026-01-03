from collections import Counter

N,K,L = map(int, input().split())

road = [tuple(map(int,input().split())) for i in range(K)]
train = [tuple(map(int,input().split())) for i in range(L)]

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
for p,q in road:
    p,q = p-1, q-1
    if not uf_road.is_same(p,q):
        uf_road.unite(p,q)

uf_train = UnionFind(N)
for r,s in train:
    r,s = r-1, s-1
    if not uf_train.is_same(r,s):
        uf_train.unite(r,s)

total_union_num = Counter()
for i in range(N):
    r = uf_road.root(i)
    t = uf_train.root(i)
    total_union_num[(r,t)] += 1

ans = []
for i in range(N):
    r = uf_road.root(i)
    t = uf_train.root(i)
    ans.append(total_union_num[(r,t)])

print(*ans)
