#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

UNVISITED, VISITED_IN_STACK, POPPED_OUT = 0, 1, 2


def generate_adj_matrix(v_info):
    for v_detail in v_info:
        v_adj_list = v_detail[2:]
        # assert len(v_adj_list) == int(v_detail[1])
        for each in v_adj_list:
            init_adj_matrix[int(v_detail[0]) - 1][int(each) - 1] = 1
    return init_adj_matrix


def graph_dfs(v_init):
    global time

    # init the first node of overall graph iterations(times >= 1)
    vertices_visit_stack.append(v_init)
    vertices_status_list[v_init] = VISITED_IN_STACK
    vertices_d_time[v_init] += time
    # init end

    while len(vertices_visit_stack) > 1:
        current_vertex = vertices_visit_stack[-1]
        next_vertex = get_adj_vertices(vertex=current_vertex)

        if next_vertex:
            if vertices_status_list[next_vertex] is UNVISITED:
                vertices_status_list[next_vertex] = VISITED_IN_STACK
                time += 1
                vertices_d_time[next_vertex] += time
                vertices_visit_stack.append(next_vertex)
        else:
            vertices_visit_stack.pop()
            vertices_status_list[current_vertex] = POPPED_OUT
            time += 1
            vertices_f_time[current_vertex] += time

    return None


def get_adj_vertices(vertex):
    index = int(vertex) - 1
    for j in range(vertices_num):
        if adj_matrix[index][j]:
            adj_matrix[index][j] = 0
            return j + 1
    return None


def dfs_start():
    global time
    for i in range(vertices_num):
        if vertices_status_list[i + 1] == UNVISITED:
            # print('round: ', i + 1)
            graph_dfs(v_init=i + 1)
            time += 1


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    vertices_num = int(_input[0])
    vertices_info = list(map(lambda x: x.split(), _input[1:]))
    init_adj_matrix = [[0] * vertices_num for _ in range(vertices_num)]
    # assert len(vertex_info) == vertex_num

    # config length = (vertex_num + 1)
    vertices_visit_stack = [-1]
    vertices_status_list = [UNVISITED] * vertices_num
    vertices_status_list.insert(0, -1)
    vertices_d_time, vertices_f_time = ([0] * (vertices_num + 1) for _ in range(2))

    adj_matrix = generate_adj_matrix(vertices_info)
    # timing start from 1
    time = 1
    dfs_start()
    for k in range(vertices_num):
        print(k + 1, vertices_d_time[k + 1], vertices_f_time[k + 1])