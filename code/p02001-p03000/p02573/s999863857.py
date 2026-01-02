import sys


def _ia(): return map(int, sys.stdin.readline().strip().split())


class UnionFind:
    def __init__(self, n):
        self._par = [-1]*n

    def root(self, x):
        if self._par[x] < 0:
            return x
        else:
            self._par[x] = self.root(self._par[x])
            return self._par[x]

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self._par[x] > self._par[y]:
            x, y = y, x
        self._par[x] += self._par[y]
        self._par[y] = x

    def size(self, x):
        return -self._par[self.root(x)]


def main():
    n, m = _ia()
    uf = UnionFind(n)
    for _ in range(m):
        a, b = map(lambda x: x-1, _ia())
        uf.unite(a, b)
    return max(uf.size(i) for i in range(n))


if __name__ == "__main__":
    print(main())
