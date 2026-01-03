# 連結
import sys
from collections import Counter, defaultdict
input = sys.stdin.readline
N, K, L = map(int, input().split())


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * (n+1)

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
        return [i for i in range(self.n+1) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


A = UnionFind(N)
B = UnionFind(N)


ans = [0 for i in range(N+1)]
for _ in range(K):
    p, q = map(int, input().split())
    A.union(p, q)
for _ in range(L):
    p, q = map(int, input().split())
    B.union(p, q)

members = defaultdict(list)
for i in range(1, N+1):
    K = A.find(i)
    members[A.find(i)].append(i)

roots = A.roots()

for parent in roots:
    if parent == 0:
        continue

    group = members[parent]
    # ここでN**2のループをしている危険性があるので予め連想配列で処理する
    B_parent = [B.find(child) for child in group]
    C = dict(Counter(B_parent))
    for child in group:
        ans[child] = C[B.find(child)]
print(*ans[1:])