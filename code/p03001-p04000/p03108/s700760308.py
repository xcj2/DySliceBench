# -*- coding: utf-8 -*-
"""
D - Decayed Bridges
https://atcoder.jp/contests/abc120/tasks/abc120_d#

"""
import sys

class DisjointSet(object):
    def __init__(self, n):
        self.rank = []
        self.p = []
        self.size = []
        for i in range(n+1):
            self.makeSet(i)

    def makeSet(self, x):
        self.p.insert(x, x)
        self.rank.insert(x, 0)
        self.size.insert(x, 1)

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


def solve(bridges, N, M):
    ans = [(N**2 - N)//2]
    d = DisjointSet(N)
    for f, t in reversed(bridges):
        if d.same(f, t):
            ans.append(ans[-1])
        else:
            n1 = d.size[d.p[f]]
            n2 = d.size[d.p[t]]
            ans.append(ans[-1] - (n1*n2))
            d.unite(f, t)
    return ans


def main(args):
    N, M = map(int, input().split())
    bridges = []
    for _ in range(M):
        f, t = map(int, input().split())
        bridges.append([f, t])
    ans = solve(bridges, N, M)

    for a in (ans[::-1])[1:]:
        print(a)


if __name__ == '__main__':
    main(sys.argv[1:])
