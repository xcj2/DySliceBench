# -*- coding: utf-8 -*-

from collections import Counter


class UnionFind:
    def __init__(self, n):
        self.ranks = [[0] * n, [0] * n]
        self.pars = [[i for i in range(n)], [i for i in range(n)]]
        self.n = n

    def find_set(self, node, idx):
        if self.pars[idx][node] == node:
            return node
        else:
            self.pars[idx][node] = self.find_set(self.pars[idx][node], idx)
            return self.pars[idx][node]

    def same_set(self, x, y, idx):
        return self.find_set(x, idx) == self.find_set(y, idx)

    def unite(self, x, y, idx):
        x = self.find_set(x, idx)
        y = self.find_set(y, idx)
        if x == y:
            return
        if self.ranks[idx][x] > self.ranks[idx][y]:
            self.pars[idx][y] = x
        else:
            self.pars[idx][x] = y
            if self.ranks[idx][x] == self.ranks[idx][y]:
                self.ranks[idx][y] += 1


def main():
    n, k, l = map(int, input().split())
    uf = UnionFind(n)
    road = 0
    train = 1

    for i in range(k):
        p, q = map(int, input().split())
        uf.unite(p-1, q-1, road)

    for i in range(l):
        r, s = map(int, input().split())
        uf.unite(r-1, s-1, train)

    roots = [(uf.find_set(i, road), uf.find_set(i, train)) for i in range(n)]
    c = Counter(roots)
    ans = []
    for root in roots:
        ans.append(c[root])

    print(*ans)


if __name__ == "__main__":
    main()
