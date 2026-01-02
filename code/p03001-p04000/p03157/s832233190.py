class DisjointSet:
    def __init__(self):
        self.rank = {}
        self.p = {}

    def makeSet(self, x):
        self.p[x] = x
        self.rank[x] = 0

    def same(self, x, y):
        return self.findSet(x) == self.findSet(y)

    def unite(self, x, y):
        self.link(self.findSet(x), self.findSet(y))

    def link(self, x, y):
        if(self.rank[x] > self.rank[y]):
            self.p[y] = x
        else:
            self.p[x] = y
            if(self.rank[x] == self.rank[y]):
                self.rank[y] += 1

    def findSet(self, x):
        if(x != self.p[x]):
            self.p[x] = self.findSet(self.p[x])
        return self.p[x]

H, W = map(int, input().split())
S = [list(input()) for i in range(H)]

ds = DisjointSet()
for i in range(H):
    for j in range(W):
        ds.makeSet((i,j))

for i in range(H):
    for j in range(W):
        if i + 1 < H and S[i][j] != S[i+1][j]:
            ds.unite((i,j), (i+1, j))
        if 0 <= i - 1 and S[i][j] != S[i-1][j]:
            ds.unite((i,j), (i-1, j))
        if j + 1 < W and S[i][j] != S[i][j+1]:
            ds.unite((i,j), (i, j+1))
        if 0 <= j - 1 and S[i][j] != S[i][j-1]:
            ds.unite((i,j), (i, j-1))

from collections import defaultdict

c1 = defaultdict(int)
c2 = defaultdict(int)

for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            c1[ds.findSet((i,j))] += 1
        else:
            c2[ds.findSet((i,j))] += 1
ans = 0
for i in c1.keys():
    ans += c1[i] * c2[i]
print(ans)