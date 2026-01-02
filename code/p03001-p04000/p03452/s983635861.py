from sys import exit

class WeightedUnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.weights = [0] * (n+1)

    def find(self, x):
        if self.parent[x] == x:
            return x
        nx = self.find(self.parent[x])
        self.weights[x] += self.weights[self.parent[x]]
        self.parent[x] = nx
        return nx

    def unite(self, x, y, d):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
            self.weights[rx] = d + self.weights[y] - self.weights[x]
        else:
            self.parent[ry] = rx
            self.weights[ry] = - d + self.weights[x] - self.weights[y]
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def diff(self, x, y):
        return self.weights[x] - self.weights[y]

n, m = map(int, input().split())
wuf = WeightedUnionFind(n)
for _ in range(m):
    l, r, d = map(int, input().split())
    l -= 1
    r -= 1
    if not wuf.same(l, r):
        wuf.unite(l, r, d)
    else:
        if wuf.diff(l, r) != d:
            print("No")
            exit()
print("Yes")
