import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
# from bisect import *
from collections import *
# from heapq import *
# INF = 500000
mod = 10**9+7

class UnionFind:

    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.height = [0] * n
        self.size = [1] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def getsize(self, x):
        return self.size[self.find(x)]

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.height[x] < self.height[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = self.par[x]
            self.size[x] += self.size[y]
            if self.height[x] == self.height[x]:
                self.height[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

N, M, K = map(int, input().split())
es = [[] for i in range(N)]
for i in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    es[u].append(v)
    es[v].append(u)
uf = UnionFind(N)
g = [-1]*N
def dfs(v, num):
    g[v] = num
    for u in es[v]:
        if g[u] == -1:
            uf.unite(v, u)
            dfs(u, num)
num = 0
for v in range(N):
    if g[v] == -1:
        dfs(v, num)
        num += 1
ans = [uf.getsize(v)-len(es[v])-1 for v in range(N)]
for i in range(K):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if uf.same(u, v):
        ans[u] -= 1
        ans[v] -= 1
print(*ans)
