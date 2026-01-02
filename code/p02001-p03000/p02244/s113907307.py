#!/usr/bin/env python3

from itertools import permutations

k = int(input())
queens_input = []
for _ in range(k):
    r, c = map(int, input().split())
    queens_input.append([r, c])
# print(k, queens_input)


def create_square(queens):
    square = [['.' for col in range(8)] for row in range(8)]
    for r, c in queens:
        square[r][c] = 'Q'
    return square


def print_square(square):
    for row in range(8):
        for col in range(8):
            print(square[row][col], end='')
        print('')


def includes(queens, queens_input):
    for q in queens_input:
        if q not in queens:
            return False
    return True


def calc_direction(queen):
    row, col = queen
    v, h, d_r, d_l = [], [], [[row, col]], [[row, col]]
    for i in range(8):
        v.append([i, col])
        h.append([row, i])
    for i in range(1, 8):
        if row - i >= 0 and col + i < 8:
            d_r.append([row - i, col + i])
        if row + i < 8 and col - i >= 0:
            d_r.append([row + i, col - i])
        if row - i >= 0 and col - i >= 0:
            d_l.append([row - i, col - i])
        if row + i < 8 and col + i < 8:
            d_l.append([row + i, col + i])
    return v, h, d_r, d_l


def count(direction, queens):
    res = 0
    for queen in queens:
        res += direction.count(queen)
    return res


def is_valid(queens):
    for queen in queens:
        v, h, d_r, d_l = calc_direction(queen)
        v_c, h_c = count(v, queens), count(h, queens)
        d_r_c, d_l_c = count(d_r, queens), count(d_l, queens)
        if not (v_c == 1 and h_c == 1 and d_r_c == 1 and d_l_c == 1):
            return False
    return True


perms = list(map(list, permutations(list(range(8)), 8)))
for perm in perms:
    queens = []
    for row in range(8):
        queens.append([row, perm[row]])
    if includes(queens, queens_input):
        if is_valid(queens):
            # print(f"queens = {queens}")
            square = create_square(queens)
            print_square(square)
            break

