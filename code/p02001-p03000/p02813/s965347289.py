#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def decide_position(num_list:list, n):

    if n == 2:
        if num_list[0] < num_list[1]:
            return 1
        else:
            return 2
    else:
        first_num = num_list[0]
        sorted_num_list = sorted(num_list)
        rank_in_p = sorted_num_list.index(first_num)
        n_kaizyou = 1
        for i in range(n-1, 0, -1):
            n_kaizyou *= i

        position = rank_in_p * n_kaizyou
        num_list.remove(first_num)
        position += decide_position(num_list, n-1)

        return position



def resolve():
    n = int(input())
    p_list = list(map(int, input().split()))
    q_list = list(map(int, input().split()))

    p_rank = decide_position(p_list, n)
    q_rank = decide_position(q_list, n)

    ans_rank = abs(p_rank - q_rank)

    print(ans_rank)






if __name__ == "__main__":
    resolve()

