# -*- coding: utf-8 -*-
"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0180

"""
import sys
from sys import stdin
from collections import namedtuple
input = stdin.readline


class DisjointSet(object):
    def __init__(self, size):
        self.rank = []
        self.p = []
        for i in range(size):
            self.makeSet(i)

    def makeSet(self, x):
        self.p.insert(x, x)
        self.rank.insert(x, 0)

    def same(self, x, y):
        return self.findSet(x) == self.findSet(y)

    def unite(self, x, y):
        self.link(self.findSet(x), self.findSet(y))

    def link(self, x, y):
        if self.rank[x] > self.rank[y]:
            self.p[y] = x
        else:
            self.p[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def findSet(self, x):
        if x != self.p[x]:
            self.p[x] = self.findSet(self.p[x])
        return self.p[x]


def kruskal(V, E, es):
    # V: ???????????° (0??????)
    # E: ??¨????????°
    es.sort(key=lambda x: x.c)
    uf = DisjointSet(V)
    res = 0

    for i in range(E):
        e = es[i]
        if not uf.same(e.u, e.v):
            uf.unite(e.u, e.v)
            res += e.c
    return res


edge = namedtuple('edge', ['u', 'v', 'c'])
def main(args):
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break

        es = []
        for _ in range(m):
            s, t, w = map(int, input().split())
            es.append(edge(s, t, w))

        result = kruskal(n, m, es)
        print(result)


if __name__ == '__main__':
    main(sys.argv[1:])
    