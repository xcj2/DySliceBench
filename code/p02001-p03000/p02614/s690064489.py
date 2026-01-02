#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import itertools
from copy import deepcopy

def input():
    return sys.stdin.readline()

def count_black(combi, field, h, w):

    height_list = []
    width_list = []
    for num in combi:
        if num <= h:
            height_list.append(num)
        else:
            width_list.append(num-(h))

    #print(height_list)
    #print(width_list)

    for line in height_list:
        for i in range(w):
            field[line-1][i] = "x"

    for row in width_list:
        for i in range(h):
            field[i][row-1] = "x"

    black_cnt = 0
    for line in field:
        black_cnt += line.count("#")

    return black_cnt





def resolve():
    h, w, k = map(int, input().split())
    field = [list(input().rstrip()) for i in range(h)]
    # field[y][x]

    lst = []

    for i in range(1, h+1):
        lst.append(i)

    lst_length = len(lst)
    for j in range(1, w+1):
        lst.append(lst_length+j)


    # 全列挙
    p = []
    for i in range(len(lst)):
        p.append(itertools.combinations(lst, i+1))

    ans_num = 0

    for v in p:
        for vv in v:
            temp_field = deepcopy(field)
            black_num = count_black(vv, temp_field, h, w)
            if black_num == k:
                ans_num += 1

    # 最後にまったく修正しない場合
    black_cnt = 0
    for line in field:
        black_cnt += line.count("#")

    if black_cnt == k:
        ans_num += 1

    print(ans_num)

if __name__ == "__main__":
    resolve()

