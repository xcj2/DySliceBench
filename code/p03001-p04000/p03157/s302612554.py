#!/usr/bin/env pypy3

import itertools
import sys


DELTAS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class UnionFind(object):

    def __init__(self, number_of_nodes):
        self.par = list(range(number_of_nodes))
        self.rank = [0] * number_of_nodes
        self.groups = [{i} for i in range(number_of_nodes)]

    def root(self, node):
        if self.par[node] == node:
            return node
        else:
            r = self.root(self.par[node])
            self.par[node] = r
            return r

    def in_the_same_set(self, node1, node2):
        return self.root(node1) == self.root(node2)

    def elements_of_group(self, node):
        return self.groups[self.root(node)]

    def unite(self, node1, node2):
        x = self.root(node1)
        y = self.root(node2)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            self.par[y] = x
            self.groups[x].update(self.groups[y])
            self.groups[y].clear()
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


def solve(h, w, stage):
    n = h * w
    uf = UnionFind(n)
    for r0, c0 in itertools.product(range(h), range(w)):
        x0 = w * r0 + c0
        ib = stage[r0][c0]
        for dr, dc in DELTAS:
            r, c = r0 + dr, c0 + dc
            if 0 <= r < h and 0 <= c < w and ib != stage[r][c]:
                x = w * r + c
                uf.unite(x0, x)
    res = 0
    is_black = [None] * n
    for r0, c0 in itertools.product(range(h), range(w)):
        x0 = w * r0 + c0
        is_black[x0] = stage[r0][c0]
    for x1 in range(n):
        eg = uf.groups[x1]
        # print(x1, eg, file=sys.stderr)
        total = len(eg)
        num_black = sum(is_black[x] for x in eg)
        res += (total - num_black) * num_black
    return res


def main():
    h, w = (int(z) for z in input().split())
    stage = [[c == "#" for c in input()] for _ in range(h)]
    res = solve(h, w, stage)
    print(res)


if __name__ == "__main__":
    main()