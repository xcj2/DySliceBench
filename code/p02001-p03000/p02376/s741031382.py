#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
input:
4 5
0 1 2
0 2 1
1 2 1
1 3 1
2 3 2

output:
3
"""

import sys
from collections import deque


def graph_bfs(source, target, parent):
    visited = [False] * vertices
    queue = deque()
    queue.append(source)
    visited[source] = True

    while queue:
        current = queue.popleft()
        for adj, cp in adj_table[current].items():
            if not visited[adj] and cp:
                queue.append(adj)
                visited[adj] = True
                parent[adj] = current

    return True if visited[target] else False


def graphFordFulkerson(source, sink):
    parent = [-1] * vertices
    max_flow = 0

    while graph_bfs(source, sink, parent):
        path_flow = float('inf')

        bk_1 = sink
        while bk_1 is not source:
            path_flow = min(path_flow, adj_table[parent[bk_1]][bk_1])
            bk_1 = parent[bk_1]

        max_flow += path_flow

        bk_2 = sink
        while bk_2 is not source:
            parent_bk_2 = parent[bk_2]
            adj_table[parent_bk_2].setdefault(bk_2, 0)
            adj_table[bk_2].setdefault(parent_bk_2, 0)

            # print(bk_2, parent_bk_2, path_flow, bk_1, parent[bk_1], parent, adj_table)
            adj_table[parent_bk_2][bk_2] -= path_flow
            adj_table[bk_2][parent_bk_2] += path_flow
            bk_2 = parent[bk_2]

    return max_flow


def generate_adj_table(v_table):
    for each in v_table:
        source, target, cp = map(int, each)
        init_adj_table[source][target] = cp

    return init_adj_table


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    vertices, edges = map(int, _input[0].split())
    v_info = map(lambda x: x.split(), _input[1:])

    init_adj_table = [dict() for _ in range(vertices)]
    adj_table = generate_adj_table(v_info)
    ans = graphFordFulkerson(source=0, sink=vertices - 1)
    print(ans)