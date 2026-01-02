class UnionFind:
    def __init__(self, n):
        self.root = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, x):
        root = self.root
        while root[x] != x:
            root[x] = root[root[x]]
            x = root[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        sx, sy = self.size[x], self.size[y]
        if sx < sy:
            self.root[x] = y
            self.size[y] += sx
        else:
            self.root[y] = x
            self.size[x] += sy


n, m = map(int, input().split())
p = list(map(int, input().split()))


uf = UnionFind(n)
union = uf.union
find = uf.find


for _ in range(m):
    x, y = map(int, input().split())
    union(x - 1, y - 1)

ans = 0
for i, x in enumerate(p):
    if find(i) == find(x - 1):
        ans += 1

print(ans)