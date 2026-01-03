from collections import defaultdict
import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, N):
        self.parent = list(range(N))
        self.rank = [0] * N
        self.size = [1] * N

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.size[y] += self.size[x]
        else:
            self.parent[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]

N, K, L = map(int, input().split())
uf1 = UnionFind(N+1)
for _ in range(K):
    p, q = map(int, input().split())
    uf1.unite(p, q)
uf2 = UnionFind(N+1)
cnt = [defaultdict(int) for _ in range(N+1)]
for i in range(1, N+1):
    cnt[i][uf1.find(i)] = 1
for _ in range(L):
    r, s = map(int, input().split())
    if uf2.same(r, s):
        continue
    a = uf2.find(r)
    b = uf2.find(s)
    uf2.unite(r, s)
    c = uf2.find(r)
    if a == c:
        for k, v in cnt[b].items():
            cnt[c][k] += v
    else:
        for k, v in cnt[a].items():
            cnt[c][k] += v
ans = [0] * (N+1)
for i in range(1, N+1):
    ans[i] = cnt[uf2.find(i)][uf1.find(i)]
print(*ans[1:])