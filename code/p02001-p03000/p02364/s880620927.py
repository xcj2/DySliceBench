#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
input:
6 9
0 1 1
0 2 3
1 2 1
1 3 7
2 4 1
1 4 3
3 4 1
3 5 1
4 5 6

output:
5
"""

import sys
from operator import attrgetter


class Edge(object):
    __slots__ = ('source', 'target', 'weight')

    def __init__(self):
        self.weight = float('inf')
        self.source, self.target = None, None


class UnionFind(object):
    __slots__ = ('size', 'tree_height_rank', 'ancestors')

    def __init__(self, size):
        self.size = int(size)
        self.tree_height_rank = [0] * self.size
        self.ancestors = [i for i in range(self.size)]

    def _find(self, x):
        if x != self.ancestors[x]:
            self.ancestors[x] = self._find(self.ancestors[x])
        return self.ancestors[x]

    def same(self, x, y):
        return self._find(x) == self._find(y)

    def _link(self, x, y):
        if self.tree_height_rank[x] > self.tree_height_rank[y]:
            self.ancestors[y] = x
        else:
            self.ancestors[x] = y
            if self.tree_height_rank[x] == self.tree_height_rank[y]:
                self.tree_height_rank[y] += 1

    def union(self, x, y):
        self._link(self._find(x), self._find(y))


def generate_edge_table(v_table):
    for index, each in enumerate(v_table):
        source, target, weight = map(int, each)
        edge = init_edge_table[index]
        edge.source = source
        edge.target = target
        edge.weight = weight

    return init_edge_table


def graph_Kruskal():
    total_cost = 0
    # sort edge_table by edge's weight
    edge_table.sort(key=attrgetter('weight'))
    # MST--> E = V + 1
    union_find_case = UnionFind(size=vertices + 1)
    for edge in edge_table:
        if not union_find_case.same(edge.source, edge.target):
            total_cost += edge.weight
            union_find_case.union(edge.source, edge.target)

    return total_cost


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    vertices, edges = map(int, _input[0].split())
    v_info = map(lambda x: x.split(), _input[1:])

    init_edge_table = [Edge() for _ in range(edges)]
    edge_table = generate_edge_table(v_info)
    print(graph_Kruskal())