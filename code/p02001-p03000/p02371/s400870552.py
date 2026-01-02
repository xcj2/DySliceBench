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
from math import isinf
from collections import deque


def generate_adj_table(v_table, init_adj_table):
    for each in v_table:
        source, target, cost = map(int, each)
        init_adj_table[source][target] = cost
        init_adj_table[target][source] = cost

    return init_adj_table


def graph_bfs(current, v_num, adj_table):
    queue = deque()
    distance = [float('inf')] * v_num
    distance[current] = 0
    queue.appendleft(current)

    while queue:
        current = queue.popleft()
        for adj, cost in adj_table[current].items():
            if isinf(distance[adj]):
                distance[adj] = distance[current] + cost
                queue.append(adj)
    return distance


def calc_tree_diameter(v_num, adj_table):
    # init x(random node) -> bridge vertex
    init_v = 0
    distance_1 = graph_bfs(init_v, v_num, adj_table)
    d1, bridge_v = 0, 0
    for v, each in enumerate(distance_1):
        if isinf(each):
            continue
        elif d1 < each:
            d1 = each
            bridge_v = v

    # bridge vertex -> y
    distance_2 = graph_bfs(bridge_v, v_num, adj_table)
    d2 = 0
    for each in distance_2:
        if isinf(each):
            continue
        d2 = max(d2, each)

    return d2


def solve():
    _input = sys.stdin.readlines()
    v_num = int(_input[0])
    edges = map(lambda x: x.split(), _input[1:])

    init_adj_table = tuple(dict() for _ in range(v_num))
    adj_table = generate_adj_table(edges, init_adj_table)
    ans = calc_tree_diameter(v_num, adj_table)
    print(ans)
    return None


if __name__ == '__main__':
    solve()