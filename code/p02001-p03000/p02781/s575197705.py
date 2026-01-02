#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import array
from bisect import *
from collections import *
import fractions
import heapq
from itertools import *
import math
import random
import re
import string
import sys

def solve_1(N):
    N_str = str(N)
    ans = 0
    for i, ch in enumerate(N_str):
        if i == 0:
            ans += int(ch)
        else:
            ans += 9
    return ans

def solve_2(N):
    N_str = str(N)

    # N = 72543

    # 6XXXX
    ans = (int(N_str[0]) - 1) * 9 * (len(N_str) - 1)

    # 7XXXX
    flag = False
    for ch in N_str[1:]:
        if flag:
            ans += 9
        else:
            ans += int(ch)
            if ch != '0':
                flag = True

    # XXXX
    for i in range(1, len(N_str) - 1):
        ans += 81 * i

    return ans

def solve_slow_2(n):
    ans = 0
    for i in range(1, n + 1):
        i_str = str(i)
        cnt = 0
        for ch in i_str:
            cnt += ch != '0'
        ans += cnt == 2
    return ans

# for n in range(1, 10000):
#     mine = solve_2(n)
#     gt = solve_slow_2(n)
#     if mine != gt:
#         print("error! n, mine, gt = ", n, mine, gt)
#         sys.exit(0)
#     else:
#         print(n, "ok")


def solve_3(N):
    N_str = str(N)
    size = len(N_str)

    # N = 72543

    # 6XXXX
    ans = (int(N_str[0]) - 1) * (((size - 1) * (size - 2)) // 2) * 81

    # 7XXXX
    # -> XXXX
    if size > 1:
        ans += solve_2(int(N_str[1:]))

    # XXXX
    for size in range(1, len(N_str)):
        ans += 9 * 9 * 9 * (size - 1) * (size - 2) // 2

    return ans

def solve_slow_3(n):
    ans = 0
    for i in range(1, n + 1):
        i_str = str(i)
        cnt = 0
        for ch in i_str:
            cnt += ch != '0'
        ans += cnt == 3
    return ans

# for n in range(1, 10000):
#     mine = solve_3(n)
#     gt = solve_slow_3(n)
#     if mine != gt:
#         print("error! n, mine, gt = ", n, mine, gt)
#         sys.exit(0)
#     else:
#         print(n, "ok")
        

def solve(N, K):
    if K == 1:
        return solve_1(N)
    elif K == 2:
        return solve_2(N)
    else:
        return solve_3(N)


N = int(input())
K = int(input())

print(solve(N, K))

