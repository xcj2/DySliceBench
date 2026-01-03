from collections import*
import sys


class UnionFind(object):
    def __init__(self, n):
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
        return


input = sys.stdin.readline
n, k, l = map(int, input().split())

ro_cl = UnionFind(n)
ra_cl = UnionFind(n)
d = defaultdict(int)

# =================================================================

# なぜかスライスを使うとエラーになる。原因不明。
# w = [list(map(int, input().split())) for i in range(k+l)]
# ro = w[:k]
# ra = w[l:]
# for p, q in ro:
#     ro_cl.union(p-1, q-1)
# for p, q in ra:
#     ra_cl.union(p-1, q-1)

# =================================================================

for i in range(k):
    p, q = map(int, input().split())
    ro_cl.union(p-1, q-1)
for i in range(l):
    p, q = map(int, input().split())
    ra_cl.union(p-1, q-1)

# =================================================================

for i in range(n):
    d[(ro_cl.find(i), ra_cl.find(i))] += 1
print(*[d[(ro_cl.find(i), ra_cl.find(i))]for i in range(n)])