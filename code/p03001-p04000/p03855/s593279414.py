import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

N, K, L = mapint()
uf_road = UnionFind(N)
for _ in range(K):
    x, y = mapint()
    uf_road.union(x-1, y-1)

uf_rail = UnionFind(N)
for _ in range(L):
    x, y = mapint()
    uf_rail.union(x-1, y-1)
from collections import Counter
lis = []
for i in range(N):
    road = uf_road.find(i)
    rail = uf_rail.find(i)
    lis.append(road*(10**6)+rail)
c = Counter(lis)
ans = []
for i in range(N):
    road = uf_road.find(i)
    rail = uf_rail.find(i)
    ans.append(str(c[(road*(10**6)+rail)]))
print(' '.join(ans))
