# -*- coding: utf-8 -*-
"""
E - 1 or 2
https://atcoder.jp/contests/abc126/tasks/abc126_e

"""
import sys


class DisjointSet(object):
    def __init__(self, n):
        self.rank = [0] * n
        self.p = list(range(n))
        self.size = [1] * n

    def same(self, x, y):
        return self.findSet(x) == self.findSet(y)

    def unite(self, x, y):
        self.link(self.findSet(x), self.findSet(y))

    def link(self, x, y):
        if self.rank[x] > self.rank[y]:
            self.size[self.p[x]] += self.size[self.p[y]]
            self.p[y] = self.findSet(x)
        else:
            self.size[self.p[y]] += self.size[self.p[x]]
            self.p[x] = self.findSet(y)
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def findSet(self, x):
        if x != self.p[x]:
            self.p[x] = self.findSet(self.p[x])
        return self.p[x]

def solve(N, M, hints):
    d = DisjointSet(N+1)
    for x, y, z in hints:
        d.unite(x, y)
    for i in range(1, N+1):
        d.findSet(i)

    ans = set(d.p[1:])
    return len(ans)


def main(args):
    N, M = map(int, input().split())
    hints = [[int(i) for i in input().split()] for _ in range(M)]
    ans = solve(N, M, hints)
    print(ans)


if __name__ == '__main__':
    main(sys.argv[1:])
