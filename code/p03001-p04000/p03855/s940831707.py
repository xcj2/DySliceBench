# -*- coding: utf-8 -*-
"""
D - 連結 / Connectivity
https://atcoder.jp/contests/abc049/tasks/arc065_b

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


from collections import Counter

def solve(N, K, L, PQ, RS):
    r_d = DisjointSet(N+1)
    for p, q in PQ:
        r_d.unite(p, q)
    t_d = DisjointSet(N+1)
    for r, s in RS:
        t_d.unite(r, s)
    for i in range(1, N+1):
        r_d.root(i)
        t_d.root(i)

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