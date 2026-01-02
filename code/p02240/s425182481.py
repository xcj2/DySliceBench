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
    current_color = 1
    for v in range(vertices):
        if color[v] == -1:
            graph_dfs(v, current_color)
            current_color += 1
    return None


def graph_dfs(vertex, current_color):
    vertices_stack = list()
    vertices_stack.append(vertex)
    color[vertex] = current_color

    while vertices_stack:
        current_vertex = vertices_stack.pop()
        for v in adj_table[current_vertex]:
            if color[v] == -1:
                color[v] = current_color
                vertices_stack.append(v)
    return None


def solve():
    for relation in relation_info:
        key, value = map(int, relation)
        adj_table[key].append(value)
        adj_table[value].append(key)

    assign_color()

    # print(adj_list)
    for question in questions:
        source, target = map(int, question)
        if color[source] == color[target]:
            print("yes")
        else:
            print("no")
    return color


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    vertices, relations = map(int, _input[0].split())

    relation_info = map(lambda x: x.split(), _input[1:relations + 1])

    q_num = int(_input[relations + 1])
    questions = map(lambda x: x.split(), _input[relations + 2:])

    adj_table = tuple([] for _ in range(vertices))
    color = [-1] * vertices
    ans = solve()