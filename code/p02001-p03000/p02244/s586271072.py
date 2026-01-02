#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
input:
2
2 2
5 3

output:
......Q.
Q.......
..Q.....
.......Q
.....Q..
...Q....
.Q......
....Q...
"""

import sys

N = 8
FREE, NOT_FREE = -1, 1


def generate_board(_q_list):
    for queen in _q_list:
        x, y = map(int, queen)
        init_q_check[x][y] = True

    return init_q_check


def print_board():
    for i in range(N):
        for j in range(N):
            if q_check[i][j]:
                if row[i] != j:
                    return None

    for i in range(N):
        print(''.join(('Q' if row[i] == j else '.' for j in range(N))))

    return None


def recursive(i):
    if i == N:
        print_board()
        return None

    for j in range(N):
        if ((col[j] is NOT_FREE) or
                (dpos[i + j] is NOT_FREE) or
                (dneg[i - j + N - 1] is NOT_FREE)):
            continue

        row[i] = j
        col[j] = dpos[i + j] = dneg[i - j + N - 1] = NOT_FREE

        recursive(i + 1)

        row[i] = col[j] = dpos[i + j] = dneg[i - j + N - 1] = FREE

    return q_check


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    q_num = int(_input[0])
    q_list = map(lambda x: x.split(), _input[1:])

    # initialize
    row, col = ([FREE] * N for _ in range(2))
    dpos, dneg = ([FREE] * (2 * N - 1) for _ in range(2))

    init_q_check = [[False] * N for _ in range(N)]
    q_check = generate_board(q_list)

    ans = recursive(0)