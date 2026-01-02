#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import stdin


def generate_adj_table(v_table):
    for each in v_table:
        start, end, weight = map(int, each)
        init_adj_table[start][end] = weight

    return init_adj_table


def floyd():
    for k in _range:
        for i in _range:
            for j in _range:
                adj_table[i][j] = min(adj_table[i].get(j, float("INF")),
                                      adj_table[i].get(k, float("INF")) + adj_table[k].get(j, float("INF")))
    return adj_table


def solve():
    ans = floyd()
    negative = False
    for m in range(vertices):
        if ans[m][m] < 0:
            negative = True

    if negative:
        print('NEGATIVE CYCLE')
    else:
        for a in _range:
            print(*(str(each[-1]).upper() for each in sorted(ans[a].items())))

    return None


if __name__ == '__main__':
    _input = stdin.readlines()
    vertices, edges = map(int, _input[0].split())
    info_list = map(lambda x: x.split(), _input[1:])
    _range = range(vertices)

    init_adj_table = tuple({i: 0} for i in range(vertices))
    adj_table = generate_adj_table(info_list)
    solve()