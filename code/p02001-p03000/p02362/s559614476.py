#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
input:
4 5 1
0 1 2
0 2 3
1 2 -5
1 3 1
2 3 2

output:
INF
0
-5
-3

OR
input:
4 6 0
0 1 2
0 2 3
1 2 -5
1 3 1
2 3 2
3 1 0

output:
NEGATIVE CYCLE
"""

import sys
from math import isinf


class Edge(object):
    __slots__ = ('source', 'target', 'cost')

    def __init__(self):
        self.cost = float('inf')
        self.source, self.target = None, None


def generate_edge_table(_v_info):
    for index, each in enumerate(_v_info):
        edge = init_edge_table[index]
        source, target, cost = map(int, each)
        edge.source = source
        edge.target = target
        edge.cost = cost
    return init_edge_table


def bellman_ford():
    distance[root] = 0

    for j in range(vertices - 1):
        for edge in edge_table:
            source, target, cost = edge.source, edge.target, edge.cost
            if distance[source] + cost < distance[target]:
                distance[target] = distance[source] + cost

    for edge in edge_table:
        source, target, cost = edge.source, edge.target, edge.cost
        if distance[source] + cost < distance[target]:
            print('NEGATIVE CYCLE')
            return list()

    return distance


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    vertices, edges, root = map(int, _input[0].split())
    v_info = map(lambda x: x.split(), _input[1:])
    # assert len(init_vertices_table) == vertices_num

    distance = [float('inf')] * vertices
    init_edge_table = tuple(Edge() for _ in range(edges))

    edge_table = generate_edge_table(v_info)

    res = bellman_ford()
    if res:
        print('\n'.join(('INF' if isinf(ele) else str(ele) for ele in res)))