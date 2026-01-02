class WeightedUnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0 for _ in range(n + 1)]
        self.weight = [0 for _ in range(n + 1)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            y = self.find(self.parent[x])
            self.weight[x] += self.weight[self.parent[x]]
            self.parent[x] = y
            return y

    def union(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            if w != self.diff(x, y):
                print("No")
                exit()

        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        else:
            self.parent[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def diff(self, x, y):
        return self.weight[x] - self.weight[y]


N, M = map(int, input().split())
w_union_find = WeightedUnionFind(N)
for i in range(M):
    l, r, d = map(int, input().split())
    w_union_find.union(l, r, d)
print("Yes")
