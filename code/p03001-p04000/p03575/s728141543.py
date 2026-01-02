"""
union-find木
"""


class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0] * n

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
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)


def abc120_d():
    n, m = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(m)]

    ans = 0
    for i in range(m):
        uf = UnionFind(n)
        for j in range(m):
            if i == j:
                continue
            uf.unite(ab[j][0] - 1, ab[j][1] - 1)

        s = set()
        for j in range(n):
            s.add(uf.find(j))
        if len(s) > 1:
            ans += 1

    print(ans)


if __name__ == '__main__':
    abc120_d()
