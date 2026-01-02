#!/usr/bin/env python
# coding: utf-8

import sys

def P(k):
    return (k*(k-1))//2

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.child = [1 for _ in range(n)] # 自分も含めた子の数
        self.ans = (n*(n-1))//2

    def root(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def same(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        return rx == ry

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return

        cx = self.child[rx]
        cy = self.child[ry]
        self.ans -= (P(cx+cy)-P(cx)-P(cy))
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.child[ry] += cx
            self.child[rx] = 0
        else:
            self.par[ry] = rx
            self.child[rx] += cy
            self.child[ry] = 0
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1


def main():
    N, M = list(map(int, sys.stdin.readline().split()))
    edges = []
    for _ in range(M):
        a, b = list(map(int, sys.stdin.readline().split()))
        edges.append((a-1, b-1))

    u = UnionFind(N)
    lans = []
    for e in edges[::-1]:
        lans.append(str(u.ans))
        u.unite(e[0], e[1])
        # print(e, u.ans, u.par, u.child)
    print("\n".join(lans[::-1]))


if __name__ == '__main__':
    main()
