from collections import Counter
import sys

sys.setrecursionlimit(20000)


def _ia(): return map(int, sys.stdin.readline().strip().split())


class UnionFind:
    def __init__(self, n):
        self._par = [-1]*(n+1)
        self._rnk = [0]*(n+1)

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
        elif self._rnk[x] > self._rnk[y]:
            self._par[x] += self._par[y]
            self._par[y] = x
        else:
            self._par[y] += self._par[x]
            self._par[x] = y
            if self._rnk[x] == self._rnk[y]:
                self._rnk[y] += 1

    def same(self, x, y):
        return self.root(x) == self.root(y)


def main():
    n, m = _ia()
    uf = UnionFind(n)
    for _ in range(m):
        a, b = map(lambda x: x-1, _ia())
        uf.unite(a, b)
    c = Counter([uf.root(i) for i in range(n)])
    return max(c.values())


if __name__ == "__main__":
    print(main())
