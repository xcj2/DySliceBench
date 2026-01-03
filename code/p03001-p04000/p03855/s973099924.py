from collections import defaultdict
import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, N):
        self.parent = list(range(N))
        self.rank = [0] * N
        self.size = [1] * N

    def find(self, x):
        r = x
        while self.parent[r] != r:
            r = self.parent[r]
        while self.parent[x] != r:
            x, self.parent[x] = self.parent[x], r
        return r

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
for _ in range(L):
    r, s = map(int, input().split())
    uf2.unite(r, s)
cnt = defaultdict(int)
for i in range(1, N+1):
    cnt[(uf1.find(i), uf2.find(i))] += 1
ans = [cnt[(uf1.find(i), uf2.find(i))] for i in range(1, N+1)]
print(*ans)