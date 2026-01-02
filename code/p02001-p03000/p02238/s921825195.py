#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

UNVISITED, VISITED_IN_STACK, POPPED_OUT = 0, 1, 2


def generate_adj(v_info):
    for v_detail in v_info:
        v_adj_list = v_detail[2:]
        assert len(v_adj_list) == int(v_detail[1])
        for each in v_adj_list:
            init_adj_matrix[int(v_detail[0]) - 1][int(each) - 1] = 1
    return init_adj_matrix


def graph_dfs(v_init):
    global time
    # init the first node of overall graph iterations(times >= 1)
    vertex_visit_stack.append(v_init)
    vertex_status_list[v_init] = VISITED_IN_STACK
    vertex_d_time[v_init] += time
    # init end
    while len(vertex_visit_stack) > 1:
        current_vertex = vertex_visit_stack[-1]
        next_vertex = get_adj_vertices(_vertex=current_vertex)
        # print('start', current_vertex, next_vertex, vertex_status_list, vertex_visit_stack)

        if next_vertex:
            if vertex_status_list[next_vertex] is UNVISITED:
                vertex_status_list[next_vertex] = VISITED_IN_STACK
                time += 1
                vertex_d_time[next_vertex] += time
                vertex_visit_stack.append(next_vertex)
                # print('on', current_vertex, next_vertex, vertex_status_list, vertex_visit_stack)
        else:
            # print('no out degree', current_vertex)
            vertex_visit_stack.pop()
            vertex_status_list[current_vertex] = POPPED_OUT
            time += 1
            vertex_f_time[current_vertex] += time
        # print('end', current_vertex, vertex_status_list, vertex_visit_stack)

    return None


def get_adj_vertices(_vertex):
    for j in range(vertex_num):
        if adj_matrix[int(_vertex) - 1][j]:
            adj_matrix[int(_vertex) - 1][j] = 0
            return j + 1
    return None


def dfs_start():
    global time
    for i in range(vertex_num):
        if vertex_status_list[i + 1] == UNVISITED:
            # print('round', i + 1)
            graph_dfs(v_init=i + 1)
            time += 1


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    vertex_num = int(_input[0])
    vertex_info = list(map(lambda x: x.split(), _input[1:]))
    init_adj_matrix = [[0] * vertex_num for _ in range(vertex_num)]
    # assert len(vertex_info) == vertex_num
    # config length -> (vertex_num + 1)
    vertex_visit_stack = [-1]
    vertex_status_list = [UNVISITED] * vertex_num
    vertex_status_list.insert(0, -1)
    vertex_d_time, vertex_f_time = ([0] * (vertex_num + 1) for _ in range(2))

    adj_matrix = generate_adj(vertex_info)

    time = 1
    dfs_start()

    for k in range(vertex_num):
        print(k + 1, vertex_d_time[k + 1], vertex_f_time[k + 1])