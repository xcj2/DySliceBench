"""
union-find木
"""


class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            x, y = y, x
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        self.size[x] += self.size[y]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]

def abc120_d():
    n, m = map(int, input().split())
    ab = [map(lambda x: int(x) - 1, input().split()) for _ in range(m)]

    ans = n * (n - 1) // 2
    uf = UnionFind(n)
    res = []
    for a, b in reversed(ab):
        res.append(ans)
        if not uf.same(a, b):
            ans -= uf.get_size(a) * uf.get_size(b)
        uf.unite(a, b)
    print("\n".join(map(str, reversed(res))))


if __name__ == '__main__':
    abc120_d()
