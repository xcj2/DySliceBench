import sys
input = sys.stdin.readline
from collections import defaultdict

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

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

N, K, L = list(map(int, input().split()))
uf_road = UnionFind(N)
uf_train = UnionFind(N)

for i in range(K):
    node1, node2 = map(int, input().split())
    uf_road.union(node1 - 1, node2 - 1)

for i in range(L):
    node1, node2 = map(int, input().split())
    uf_train.union(node1 - 1, node2 - 1)

# 全メンバ列挙は遅い
# ans = [len(set(uf_road.members(i)) & set(uf_train.members(i))) for i in range(N)]
d = defaultdict(int)
for i in range(N):
    d[uf_road.find(i), uf_train.find(i)] += 1
print(*(d[uf_road.find(i), uf_train.find(i)] for i in range(N)))
