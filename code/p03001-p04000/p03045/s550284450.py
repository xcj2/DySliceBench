#!/usr/bin/env python3
import sys
INF = float("inf")


class UnionFind(object):
    """重み付きUnionFind木
    """

    def __init__(self, N, unity=0):
        self.tree = list(range(N))
        self.rank = [0] * N
        self.diff_weight = [unity]*N

    def root(self, i):
        if self.tree[i] == i:
            return i
        else:
            r = self.root(self.tree[i])
            self.diff_weight[i] += self.diff_weight[self.tree[i]]
            self.tree[i] = r
            return r

    def weight(self, i):
        self.root(i)
        return self.diff_weight[i]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y, w):
        w += self.weight(x)
        w -= self.weight(y)
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            x, y = y, x
            w = -w
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        self.tree[y] = x
        self.diff_weight[y] = w
        return True

    def diff(self, x, y):
        return self.weight(x) - self.weight(y)


def solve(N: int, M: int, X: "List[int]", Y: "List[int]", Z: "List[int]"):
    uf = UnionFind(N)
    for x, y, z in zip(X, Y, Z):
        uf.unite(x-1, y-1, z)

    print(len(set([uf.root(i) for i in range(N)])))

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    X = [int()] * (M)  # type: "List[int]"
    Y = [int()] * (M)  # type: "List[int]"
    Z = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
        Z[i] = int(next(tokens))
    solve(N, M, X, Y, Z)


if __name__ == '__main__':
    main()
