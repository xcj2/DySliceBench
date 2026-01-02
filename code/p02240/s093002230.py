#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
input:
10 9
0 1
0 2
3 4
5 7
5 6
6 7
6 8
7 8
8 9
3
0 1
5 9
1 3

output:
yes
yes
no

"""

import sys


def assign_color():
    v_color = 0
    for v in range(v_num):
        if color[v] == -1:
            graph_dfs(v, v_color)
            # use int as color to represent different connected groups
            v_color += 1
    return None


def graph_dfs(current, v_color):
    stack = list()
    stack.append(current)
    color[current] = v_color

    while stack:
        current = stack.pop()
        for adj in adj_table[current]:
            if color[adj] == -1:
                color[adj] = v_color
                stack.append(adj)
    return None


def solve():
    for edge in edges:
        source, target = map(int, edge)
        adj_table[source].append(target)
        adj_table[target].append(source)

    assign_color()

    for question in questions:
        q_source, q_target = map(int, question)
        if color[q_source] == color[q_target]:
            print("yes")
        else:
            print("no")

    return color


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    v_num, r_num = map(int, _input[0].split())

    edges = map(lambda x: x.split(), _input[1:r_num + 1])

    q_num = int(_input[r_num + 1])
    questions = map(lambda x: x.split(), _input[r_num + 2:])

    adj_table = tuple([] for _ in range(v_num))
    color = [-1] * v_num
    ans = solve()