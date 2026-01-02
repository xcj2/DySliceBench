#!/usr/bin/env pypy3

import itertools


class UnionFind(object):

    def __init__(self, number_of_nodes):
        self.par = list(range(number_of_nodes))
        self.rank = [0] * number_of_nodes

    def root(self, node):
        if self.par[node] == node:
            return node
        else:
            r = self.root(self.par[node])
            self.par[node] = r
            return r

    def in_the_same_set(self, node1, node2):
        return self.root(node1) == self.root(node2)

    def unite(self, node1, node2):
        x = self.root(node1)
        y = self.root(node2)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


def count_bridges(n, m, edges):
    res = 0
    for rem_idx in range(m):
        uf = UnionFind(n)
        for i in range(m):
            if i != rem_idx:
                a, b = edges[i]
                uf.unite(a, b)
        for u, v in itertools.product(range(n), repeat=2):
            if not uf.in_the_same_set(u, v):
                res += 1
                break
    return res


def main():
    n, m = (int(x) for x in input().split())
    edges = [tuple(int(x) - 1 for x in input().split()) for _ in range(m)]
    print(count_bridges(n, m, edges))


if __name__ == '__main__':
    main()
