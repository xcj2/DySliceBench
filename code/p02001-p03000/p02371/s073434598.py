#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
input:
4
0 1 2
1 2 1
1 3 3

output:
5
"""

import sys
from collections import deque
from math import isinf


def generate_adj_table(v_table):
    for each in v_table:
        v_from, v_to, edge_weight = map(int, each)
        init_adj_table[v_from][v_to] = edge_weight
        init_adj_table[v_to][v_from] = edge_weight

    return init_adj_table


def graph_bfs(v_init):
    global distance
    distance = [float('inf')] * vertices
    distance[v_init] = 0
    queue.appendleft(v_init)

    while queue:
        current = queue.popleft()
        adj_weight = adj_table[current]
        for adj in adj_weight.keys():
            if isinf(distance[adj]):
                distance[adj] = distance[current] + adj_weight[adj]
                queue.append(adj)
    return None


def solve():
    graph_bfs(init_v)
    diameter, bridge_v = 0, 0
    for v in range(vertices):
        if isinf(distance[v]):
            continue
        if diameter < distance[v]:
            diameter = distance[v]
            bridge_v = v

    graph_bfs(bridge_v)
    diameter = 0
    for v in range(vertices):
        if isinf(distance[v]):
            continue
        diameter = max(diameter, distance[v])

    return diameter


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    vertices = int(_input[0])
    v_info = map(lambda x: x.split(), _input[1:])

    queue = deque()
    distance = [float('inf')] * vertices

    init_adj_table = tuple(dict() for _ in range(vertices))
    adj_table = generate_adj_table(v_info)

    init_v = 0
    print(solve())