from collections import defaultdict

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

H,W = map(int, input().split())
S = [input() for _ in range(H)]

uf = UnionFind(H*W)

for i in range(H):
    for j in range(W):
        if 0 <= i < H-1:
            if S[i][j] != S[i+1][j]:
                uf.unite(W*i+j, W*(i+1)+j)
 
        if 0 <= j < W-1:
            if S[i][j] != S[i][j+1]:
                uf.unite(W*i+j, W*i+j+1)


black = defaultdict(int)
white = defaultdict(int)
unions = set(uf.parent)
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            black[uf.root(W*i+j)] += 1
        else:
            white[uf.root(W*i+j)] += 1
ans = 0
for u in unions:
    ans += black[u] * white[u]

print(ans)