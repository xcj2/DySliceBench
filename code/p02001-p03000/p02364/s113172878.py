from heapq import heapify, heappop, heappush
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
G = []
for _ in [0]*M:
    a, b, c = map(int, input().split())
    heappush(G, (c, a, b))


class UnionFind:
    def __init__(self, n=0):
        self.d = [-1]*n
        self.u = n

    def root(self, x):
        if self.d[x] < 0:
            return x
        self.d[x] = self.root(self.d[x])
        return self.d[x]

    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x == y:
            return False
        if x > y:
            x, y = y, x
        self.d[x] += self.d[y]
        self.d[y] = x
        self.u -= 1
        return True

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.d[self.root(x)]

    def num_union(self):
        return self.u


u = UnionFind(N)
ans = 0
while u.num_union() > 1:
    c, a, b = heappop(G)
    if u.same(a, b):
        continue
    u.unite(a, b)
    ans += c
print(ans)

