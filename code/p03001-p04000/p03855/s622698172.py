#!/usr/bin/env python3
import sys
from collections import Counter
INF = float("inf")


class UnionFind(object):
    def __init__(self, N):
        self.tree = list(range(N))

    def root(self, i):
        if self.tree[i] == i:
            return i
        else:
            self.tree[i] = self.root(self.tree[i])
            return self.tree[i]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x != y:
            self.tree[x] = y


def solve(N: int, K: int, L: int, p: "List[int]", q: "List[int]", r: "List[int]", s: "List[int]"):
    uf_train = UnionFind(N)
    uf_path = UnionFind(N)

    for i in range(K):
        uf_path.unite(p[i]-1, q[i]-1)
    for i in range(L):
        uf_train.unite(r[i]-1, s[i]-1)

    counter = Counter()
    for i in range(N):
        key = (uf_path.root(i), uf_train.root(i))
        counter[key] += 1

    for i in range(N):
        key = (uf_path.root(i), uf_train.root(i))
        if i != N-1:
            print(counter[key], end=" ")
        else:
            print(counter[key])

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    p = [int()] * (K)  # type: "List[int]"
    q = [int()] * (K)  # type: "List[int]"
    for i in range(K):
        p[i] = int(next(tokens))
        q[i] = int(next(tokens))
    r = [int()] * (L)  # type: "List[int]"
    s = [int()] * (L)  # type: "List[int]"
    for i in range(L):
        r[i] = int(next(tokens))
        s[i] = int(next(tokens))
    solve(N, K, L, p, q, r, s)


if __name__ == '__main__':
    main()
