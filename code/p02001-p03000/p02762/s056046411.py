from collections import defaultdict
import sys
input = sys.stdin.readline


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

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
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)


N, M, K = map(int, input().split())
uf = UnionFind(N)
friend = [0] * N
for _ in range(M):
    A, B = map(lambda x: int(x)-1, input().split())
    friend[A] += 1
    friend[B] += 1
    uf.unite(A, B)
block = [0] * N
for _ in range(K):
    C, D = map(lambda x: int(x)-1, input().split())
    if uf.same(C, D):
        block[C] += 1
        block[D] += 1
counter = defaultdict(int)
for i in range(N):
    counter[uf.find(i)] += 1
ans = [0] * N
for i in range(N):
    ans[i] = counter[uf.find(i)] - friend[i] - block[i] - 1
print(' '.join(map(str, ans)))
