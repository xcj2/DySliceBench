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
    for k in _range:
        for i in _range:
            for j in _range:
                _adj_table[i][j] = min(_adj_table[i][j],
                                       _adj_table[i][k] + _adj_table[k][j])
    return _adj_table


def solve(_adj_table):
    after_floyd_table = floyd(_adj_table)

    negative = False
    for m in _range:
        if after_floyd_table[m][m] < 0:
            negative = True

    if negative:
        print('NEGATIVE CYCLE')
        return None
    else:
        for each in after_floyd_table:
            print(' '.join(('INF' if isinf(ele) else str(ele) for ele in each)))

    return after_floyd_table


if __name__ == '__main__':
    _input = stdin.readlines()
    vertices, edges = map(int, _input[0].split())
    info_list = map(lambda x: x.split(), _input[1:])
    _range = range(vertices)

    init_adj_table = tuple([float('inf')] * vertices for i in range(vertices))
    for n in _range:
        init_adj_table[n][n] = 0

    adj_table = generate_adj_table(info_list, init_adj_table)
    solve(adj_table)