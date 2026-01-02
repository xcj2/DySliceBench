#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
input:
5 6
0 1
1 0
1 2
2 4
4 3
3 2
4
0 1
0 3
2 3
3 4

output:
1
0
1
1
"""

import sys
from math import isinf

sys.setrecursionlimit(int(1e5))


def generate_adj_table(_v_info):
    for v_detail in _v_info:
        v_from, v_to = map(int, v_detail)
        init_adj_table[v_from].append(v_to)
    return init_adj_table


def Tarjan(current, low, disc, scc_stack, in_scc_stack):
    global timer
    disc[current] = low[current] = timer
    timer += 1

    in_scc_stack[current] = True
    scc_stack.append(current)

    current_scc_set = set()
    for adj in adj_table[current]:
        if isinf(disc[adj]):
            Tarjan(adj, low, disc, scc_stack, in_scc_stack)
            low[current] = min(low[current], low[adj])

        elif in_scc_stack[adj]:
            low[current] = min(low[current], disc[adj])

    scc_candidate = -1
    if disc[current] == low[current]:
        while scc_candidate != current:
            scc_candidate = scc_stack.pop()
            current_scc_set.add(scc_candidate)
            in_scc_stack[scc_candidate] = False

        init_scc_sets_list.append(current_scc_set)

    return None


def scc():
    disc = [float('inf')] * vertices
    low = [float('inf')] * vertices
    scc_stack = list()
    in_scc_stack = [False] * vertices

    for v in range(vertices):
        if isinf(disc[v]):
            Tarjan(v, low, disc, scc_stack, in_scc_stack)

    return init_scc_sets_list


def solve():
    for question in q_list:
        flag = False
        ele1, ele2 = map(int, question)
        for each in scc_sets_list:
            if (ele1 in each) and (ele2 in each):
                flag = True
                break
        if flag:
            print('1')
        else:
            print('0')

    return None


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    vertices, edges = map(int, _input[0].split())
    v_info = map(lambda x: x.split(), _input[1:edges + 1])
    q_num = int(_input[edges + 1])
    q_list = map(lambda x: x.split(), _input[edges + 2:])

    init_adj_table = tuple([] for _ in range(vertices))
    adj_table = generate_adj_table(v_info)

    timer = 0
    init_scc_sets_list = []
    scc_sets_list = scc()
    solve()