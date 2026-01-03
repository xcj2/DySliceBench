# -*- coding: utf-8 -*-
"""
D - 連結 / Connectivity
https://atcoder.jp/contests/abc049/tasks/arc065_b

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


from collections import Counter

def solve(N, K, L, PQ, RS):
    r_d = DisjointSet(N+1)
    for p, q in PQ:
        r_d.unite(p, q)
    t_d = DisjointSet(N+1)
    for r, s in RS:
        t_d.unite(r, s)
    for i in range(1, N+1):
        r_d.findSet(i)
        t_d.findSet(i)

    connectivity = Counter()
    for i in range(1, N+1):
        connectivity[(r_d.p[i], t_d.p[i])] += 1
    return [connectivity[(r_d.p[i], t_d.p[i])] for i in range(1, N + 1)]


def main(args):
    N, K, L = map(int, input().split())
    PQ = [[int(i) for i in input().split()] for _ in range(K)]
    RS = [[int(i) for i in input().split()] for _ in range(L)]
    ans = solve(N, K, L, PQ, RS)
    print(*ans)


if __name__ == '__main__':
    main(sys.argv[1:])