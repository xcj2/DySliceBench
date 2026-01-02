# -*- coding: utf-8 -*-
"""
E - 1 or 2
https://atcoder.jp/contests/abc126/tasks/abc126_e

"""
import sys


class DisjointSet:
    def __init__(self, n):
        self.p = list(range(n))

    def root(self, i):
        if self.p[i] == i:
            return i
        else:
            self.p[i] = self.root(self.p[i])
            return self.p[i]

    def find(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, i, j):
        i = self.root(i)
        j = self.root(j)
        if j >= i:
            self.p[j] = i
        else:
            self.p[i] = j


def solve(N, M, hints):
    d = DisjointSet(N+1)
    for x, y, z in hints:
        d.unite(x, y)
    for i in range(1, N+1):
        d.root(i)

    ans = set(d.p)
    ans.discard(d.p[0])
    return len(ans)


def main(args):
    N, M = map(int, input().split())
    hints = [[int(i) for i in input().split()] for _ in range(M)]
    ans = solve(N, M, hints)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
