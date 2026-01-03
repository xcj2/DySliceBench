from collections import*
import sys
input = sys.stdin.readline


class UnionFind(object):
    def __init__(self, n):
        # 親の番号を格納する。親だった場合は-(その集合のサイズ)
        # 作るときはParentsの値を全て-1にする
        # こうすると全てバラバラになる
        self.parents = [-1 for i in range(n)]

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

    def size(self, x):
        return -self.parents[self.find(x)]


n, k, l = map(int, input().split())
ro_cl = UnionFind(n)
ra_cl = UnionFind(n)
d = defaultdict(int)
for i in range(k):
    p, q = map(int, input().split())
    ro_cl.union(p-1, q-1)
for i in range(l):
    p, q = map(int, input().split())
    ra_cl.union(p-1, q-1)
for i in range(n):
    d[(ro_cl.find(i), ra_cl.find(i))] += 1
print(*[d[(ro_cl.find(i), ra_cl.find(i))]for i in range(n)])