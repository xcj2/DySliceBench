from collections import defaultdict

N = int(input())
points = [tuple(map(int, input().split()))for _ in range(N)]

if N == 1:
    print(1)
    exit(0)

points.sort(key=lambda p: p[1])
points.sort(key=lambda p: p[0])
d = defaultdict(int)
max_count = 0
max_f = None
for i in range(N):
    for j in range(i + 1, N):
        xi, yi = points[i]
        xj, yj = points[j]
        key = (xj - xi, yj - yi)
        d[key] += 1
        if d[key] > max_count:
            max_count = d[key]
            max_f = key


class UnionFind(object):

    def __init__(self, N):
        self.tree = [i for i in range(N)]
        self.rank = [0] * (N + 1)

    def find(self, x):
        if self.tree[x] == x:
            return x
        else:
            self.tree[x] = self.find(self.tree[x])  # 経路圧縮
            return self.tree[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        # ランクを考慮しない場合はどちらが親になっても良い
        if self.rank[x] < self.rank[y]:
            self.tree[x] = y
        else:
            self.tree[y] = x

        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

    def has_same_parent(self, x, y):
        return self.find(x) == self.find(y)


p, q = max_f
uf = UnionFind(N)
for i in range(N):
    for j in range(i + 1, N):
        xi, yi = points[i]
        xj, yj = points[j]
        if xj - xi == p and yj - yi == q:
            uf.unite(i, j)

print(len(set(uf.tree)))
