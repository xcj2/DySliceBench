#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def assign_color():
    _color = 1
    for m in range(vertices_num):
        if vertices_status_list[m] == -1:
            graph_dfs(m, _color)
            _color += 1
    return None


def graph_dfs(vertex, color):
    vertices_stack = list()
    vertices_stack.append(vertex)
    vertices_status_list[vertex] = color

    while vertices_stack:
        current_vertex = vertices_stack[-1]
        vertices_stack.pop()
        for v in adj_list[current_vertex]:
            if vertices_status_list[v] == -1:
                vertices_status_list[v] = color
                vertices_stack.append(v)
    return None


def solve():
    for relation in relation_info:
        key, value = map(int, relation.split())
        adj_list[key].append(value)
        adj_list[value].append(key)

    assign_color()

    # print(adj_list)
    for question in question_list:
        start, target = map(int, question.split())
        if vertices_status_list[start] == vertices_status_list[target]:
            print("yes")
        else:
            print("no")
    return vertices_status_list


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    vertices_num, relation_num = map(int, _input[0].split())

    relation_info = _input[1:relation_num + 1]

    question_num = int(_input[relation_num + 1])
    question_list = _input[relation_num + 2:]

    adj_list = tuple([[] for _ in range(vertices_num)])
    vertices_status_list = [-1] * vertices_num
    ans = solve()