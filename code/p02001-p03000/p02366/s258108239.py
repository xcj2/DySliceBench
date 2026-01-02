#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

input:
5 4
0 1
1 2
2 3
3 4

output:
1
2
3
"""

import sys

sys.setrecursionlimit(int(1e6))


def generate_adj_table(_v_info):
    for v_detail in _v_info:
        source, target = map(int, v_detail)
        init_adj_table[source].append(target)
        init_adj_table[target].append(source)
    return init_adj_table


def Tarjan(current, parents, visited, disc, low):
    global timer
    current_children_count = 0
    visited[current] = True
    disc[current] = low[current] = timer
    timer += 1

    for adj in adj_table[current]:
        if not visited[adj]:
            parents[adj] = current
            current_children_count += 1

            Tarjan(adj, parents, visited, disc, low)

            low[current] = min(low[current], low[adj])
            # current is root of DFS tree
            if parents[current] == -1 and current_children_count > 1:
                art_set.add(current)

            elif parents[current] != -1 and low[adj] >= disc[current]:
                art_set.add(current)

        elif adj != parents[current]:
            low[current] = min(low[current], disc[adj])

    # print(timer, parents, visited, disc, low)
    return None


def art_points():
    parents = [-1] * vertices
    visited = [False] * vertices
    disc = [float('inf')] * vertices
    low = [float('inf')] * vertices

    for v in range(vertices):
        if not visited[v]:
            Tarjan(v, parents, visited, disc, low)

    return art_set


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    vertices, edges = map(int, _input[0].split())
    v_info = map(lambda x: x.split(), _input[1:])
    init_adj_table = tuple([] for _ in range(vertices))
    adj_table = generate_adj_table(v_info)

    timer = 0
    art_set = set()
    ans = art_points()
    if ans:
        print(*sorted(ans), sep='\n')