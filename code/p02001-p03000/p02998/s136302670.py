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

N = int(input())
a = [-1] * (10**5+1)
uf = UnionFind(10**5+1)
xs = [set() for _ in range(10**5+1)]
for _ in range(N):
    x, y = map(int, input().split())
    if a[x] == -1:
        a[x] = y
    else:
        uf.unite(a[x], y)
    xs[y].add(x)

root = defaultdict(set)
for y in range(10**5+1):
    root[uf.find(y)] |= xs[y]
ans = 0
for y in range(10**5+1):
    ans += len(root[uf.find(y)]) - len(xs[y])
print(ans)