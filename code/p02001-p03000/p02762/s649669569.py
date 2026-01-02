#!/usr/bin/env python3
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

class DisjointSet:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1] * n
        self.rank = [0] * n

    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def has_same_root(self, x, y):
        return self.root(x) == self.root(y)

    def get_size(self, x):
        return self.size[self.root(x)]

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

n, m, k = [int(item) for item in input().split()]
edge = [[] for _ in range(n)]
friends = [set() for _ in range(n)]
DS = DisjointSet(n)
for _ in range(m):
    a, b = [int(item) for item in input().split()]
    a -= 1; b -= 1
    edge[a].append(b)
    edge[b].append(a)
    friends[a].add(b)
    friends[b].add(a)
    if not DS.has_same_root(a, b):
        DS.unite(a, b)

h_cnt = [0] * n
hostiles = [set() for _ in range(n)]
for _ in range(k):
    c, d = [int(item) for item in input().split()]
    c -= 1; d -= 1 
    hostiles[c].add(d)
    hostiles[d].add(c)

visited = [0] * n
def dfs(par, p, v):
    queue = deque()
    queue.append((p, v))
    visited[v] = True
    while queue:
        p, v = queue.popleft()
        for h in hostiles[v]:
            if h not in friends[v] and DS.has_same_root(h, v):
                h_cnt[v] += 1
        for nv in edge[v]:
            if visited[nv]:
                continue
            if nv == p:
                continue
            queue.append((v, nv))
            visited[nv] = True

for i in range(n):
    if visited[i]:
        continue
    visited[i] = True
    dfs(i, -1, i)

ans = []
for i in range(n):
    ans.append(DS.get_size(i) - 1 - h_cnt[i] - len(edge[i]))
    
print(*ans)