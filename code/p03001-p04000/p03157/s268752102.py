"""
prd_xxxさんの解答に自分向けにコメントを付けただけ
https://atcoder.jp/contests/aising2019/submissions/3986546
"""

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

# マス目分のUnionFind木を用意
uf = UnionFind(H*W)


for i in range(H):
    for j in range(W):
        if j < W-1 and S[i][j] != S[i][j+1]:
            uf.unite(i*W+j, i*W+j+1) # 右へ移動可能のときつなぐ
        if i < H-1 and S[i][j] != S[i+1][j]:
            uf.unite(i*W+j, (i+1)*W+j) # 下へ移動可能のときつなぐ

# 親をたどって大本につなぎなおす
for i in range(H*W):
    uf.root(i)

c1 = Counter()
c2 = Counter()

for i in range(H):
    for j in range(W):
        k = i*W + j
        # uf.root(k)は連結成分の番号（ユニオンの番号）を表していて、それらにつながっている黒と白の個数を求める
        if S[i][j] == ".":
            c1[uf.root(k)] += 1
        else:
            c2[uf.root(k)] += 1

ans = 0
for k in c1.keys():
    # それぞれの連結成分について、出発地点となる黒とゴールとなる白の組み合わせの分だけ足していく
    ans += c1[k] * c2[k]

print(ans)