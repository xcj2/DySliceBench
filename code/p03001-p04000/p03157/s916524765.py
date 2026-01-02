#!/usr/bin/env pypy3

import collections
import itertools


DELTAS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class UnitDict(dict):

    def __init__(self, iterable=None, wrapper=lambda x: x):
        super().__init__(self)
        self.wrapper = wrapper
        if iterable is not None:
            self.update(iterable)

    def __missing__(self, key):
        self[key] = self.wrapper(key)
        return self[key]


class DisjointSetDataStructure(object):

    def __init__(self, nodes=None):
        self.par = UnitDict(wrapper=lambda x: x)
        self.rank = collections.defaultdict(int)
        self.groups = UnitDict(wrapper=lambda x: {x})
        if nodes is not None:
            for node in nodes:
                _, _, _ = self.par[node], self.rank[node], self.groups[node]
        
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
    dds = DisjointSetDataStructure()
    for r0, c0 in itertools.product(range(h), range(w)):
        cell0 = stage[r0][c0]
        for dr, dc in DELTAS:
            r, c = r0 + dr, c0 + dc
            if 0 <= r < h and 0 <= c < w and cell0 != stage[r][c]:
                dds.unite((r0, c0), (r, c))
    res = 0
    for nodes in dds.groups.values():
        num_total = len(nodes)
        num_black = sum(stage[r][c] for r, c in nodes)
        res += num_black * (num_total - num_black)
    return res


def main():
    h, w = (int(z) for z in input().split())
    stage = [[c == "#" for c in input()] for _ in range(h)]
    res = solve(h, w, stage)
    print(res)


if __name__ == "__main__":
    main()