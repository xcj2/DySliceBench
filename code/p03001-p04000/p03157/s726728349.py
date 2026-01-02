import sys
input = sys.stdin.readline

from collections import defaultdict

h, w = map(int, input().split())
s = [input() for _ in range(h)]

class UnionFind:
    def __init__(self, n):
        self.rank = [0]*n
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def merge(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            self.rank[y] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

uf = UnionFind(h * w)
for i in range(h):
    for j in range(w):
        if j < w-1:
            if s[i][j] != s[i][j + 1]:
                uf.merge(i*w + j, i*w + j + 1)
        if i < h-1:
            if s[i][j] != s[i+1][j]:
                uf.merge(i*w + j, (i+1)*w + j)

d_w = defaultdict(int)
d_b = defaultdict(int)
for i in range(h):
    for j in range(w):
        parent = uf.find(i*w + j)
        if s[i][j] == ".":
            d_w[parent] += 1
        else:
            d_b[parent] += 1

ans = 0
for i in range(h):
    for j in range(w):
        ans += d_w[i*w + j] * d_b[i*w + j]

print(ans)



