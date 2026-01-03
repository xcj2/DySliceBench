from collections import Counter


class WeightedUnionFind():
    def __init__(self, n):
        self.parents = [-1] * n
        self.weight = [0] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.weight[x] += self.weight[self.parents[x]]
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return

        if self.parents[rx] > self.parents[ry]:
            rx, ry = ry, rx
            x, y = y, x
            w = -w

        self.parents[rx] += self.parents[ry]
        self.parents[ry] = rx
        self.weight[ry] = + self.weight[x] - w - self.weight[y]

    def find_position(self, x):
        if self.parents[x] < 0:
            return 0
        else:
            return -self.weight[x] + self.find_position(self.parents[x])

    def diff(self, x, y):
        if self.find(x) != self.find(y):
            raise Exception('"{}" belongs to a different tree from "{}"'.format(x, y))
        return self.find_position(y) - self.find_position(x)


N, K, L = map(int, input().split())
uf1 = WeightedUnionFind(N)
uf2 = WeightedUnionFind(N)
for _ in range(K):
    p, q = map(int, input().split())
    uf1.union(p - 1, q - 1, 0)

for _ in range(L):
    r, s = map(int, input().split())
    uf2.union(r - 1, s - 1, 0)

path = [None] * N
for i in range(N):
    path[i] = (uf1.find(i), uf2.find(i))

cnt = Counter(path)
for i in range(N - 1):
    print(cnt[path[i]], end=' ')
print(cnt[path[N - 1]])
