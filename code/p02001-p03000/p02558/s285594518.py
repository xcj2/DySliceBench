class UnionFind:
    __slots__ = ["N", "root"]

    def __init__(self, N):
        self.N = N
        self.root = [-1] * N

    def find(self, x):
        r = x
        while self.root[r] >= 0:
            r = self.root[r]

        while self.root[x] >= 0:
            self.root[x], x = r, self.root[x]

        return r

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        elif self.root[y] < self.root[x]:
            x, y = y, x
        self.root[x] += self.root[y]
        self.root[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)


import sys
input = sys.stdin.readline


def main():
    n, q = map(int, input().split())
    uf = UnionFind(n)
    res = []
    for _ in range(q):
        t, u, v = map(int, input().split())
        if t:
            res.append(int(uf.same(u, v)))
        else:
            uf.union(u, v)
    print("\n".join(map(str, res)))


main()
