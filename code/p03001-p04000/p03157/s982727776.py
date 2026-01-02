from collections import Counter

H,W = map(int, input().split())
S = [input() for _ in range(H)]


 
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

uf = UnionFind(H*W)

for i in range(H):
    for j in range(W):
        
        # 横
        if j != W-1 and S[i][j] != S[i][j+1]:
            uf.unite(i*W+j, i*W+j+1)
        
        # 縦
        if i != H-1 and S[i][j] != S[i+1][j]:
            uf.unite(i*W+j, (i+1)*W+j)

for i in range(H*W):
    uf.root(i)

black = Counter()
white = Counter()

#あるユニオンに所属（#.#.の移動できる塊）の#と.の数を数える
for i in range(H):
    for j in range(W):
        k = i*W+j
        if S[i][j] == "#":
            black[uf.root(k)] += 1
        else:
            white[uf.root(k)] += 1

#ユニオンごとに足し合わせ
ans = 0
for k in black.keys():
    ans += black[k] * white[k]

print(ans)