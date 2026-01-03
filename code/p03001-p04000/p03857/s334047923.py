#!/usr/bin/env pypy3

import collections


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


def main():
    n, k, l = (int(x) for x in input().split())
    uf_roads = UnionFind(n)
    for _ in range(k):
        p, q = (int(x) - 1 for x in input().split())
        uf_roads.unite(p, q)
    uf_rails = UnionFind(n)
    for _ in range(l):
        r, s = (int(x) - 1 for x in input().split())
        uf_rails.unite(r, s)
    ctr = collections.Counter((uf_roads.root(i), uf_rails.root(i))
                              for i in range(n))
    ans = [ctr[(uf_roads.root(i), uf_rails.root(i))] for i in range(n)]
    print(" ".join(str(a) for a in ans))

if __name__ == '__main__':
    main()
