#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import stdin
from math import isinf


def generate_adj_table(v_table, _init_adj_table):
    for each in v_table:
        start, end, weight = map(int, each)
        _init_adj_table[start][end] = weight

    return _init_adj_table


def floyd(_adj_table):
    for k in v_range:
        for i in v_range:
            for j in v_range:
                _adj_table[i][j] = min(_adj_table[i][j],
                                       _adj_table[i][k] + _adj_table[k][j])
    return _adj_table


def solve(_after_table):
    negative = False
    for m in v_range:
        if _after_table[m][m] < 0:
            negative = True

    if negative:
        print('NEGATIVE CYCLE')
        return None
    else:
        for each in _after_table:
            print(' '.join(('INF' if isinf(ele) else str(ele) for ele in each)))

    return _after_table


if __name__ == '__main__':
    _input = stdin.readlines()
    vertices, edges = map(int, _input[0].split())
    info_list = map(lambda x: x.split(), _input[1:])
    v_range = range(vertices)

    init_adj_table = tuple([float('inf')] * vertices for _ in v_range)
    for n in v_range:
        init_adj_table[n][n] = 0

    adj_table = generate_adj_table(info_list, init_adj_table)
    after_table = floyd(adj_table)
    ans = solve(after_table)