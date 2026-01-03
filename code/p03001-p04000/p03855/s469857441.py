from collections import Counter


class UnionFind():
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


N, K, L = map(int, input().split())
uf1 = UnionFind(N)
uf2 = UnionFind(N)
for _ in range(K):
    p, q = map(int, input().split())
    uf1.union(p - 1, q - 1)

for _ in range(L):
    r, s = map(int, input().split())
    uf2.union(r - 1, s - 1)

path = [None] * N
for i in range(N):
    path[i] = (uf1.find(i), uf2.find(i))

cnt = Counter(path)
for i in range(N - 1):
    print(cnt[path[i]], end=' ')
print(cnt[path[N - 1]])
