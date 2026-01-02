from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from functools import reduce


sys.setrecursionlimit(2147483647)
INF = 10 ** 18
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007


n = I()
lr_list = LIR(n)
lr_list.sort()
max_l1 = lr_list[-1][0]
min_r1 = INF


for i, (l, r) in enumerate(lr_list):
    if r < min_r1:
        min_r1 = r
        min_r_ind = i




if n == 2:
    print(lr_list[0][1] - lr_list[0][0] + 1 + lr_list[1][1] - lr_list[1][0] + 1)


else:
    max_diff = 0
    for i in range(n - 1):
        if i == min_r_ind:
            continue
        max_diff = max(max_diff, lr_list[i][1] - lr_list[i][0] + 1)

    ans = max(0, min_r1 -  max_l1 + 1) + max_diff


    min_r2 = lr_list[-1][1]
    for j in range(n - 2, -1, -1):
        if j == min_r_ind:
            continue
        max_l2 = lr_list[j][0]
        ans = max(ans, max(min_r1 - max_l2 + 1, 0) + max(min_r2 - max_l1 + 1, 0))
        min_r2 = min(min_r2, lr_list[j][1])


    max_l2 = lr_list[min_r_ind][0]
    ans = max(ans, max(min_r1 - max_l2 + 1, 0) + max(min_r2 - max_l1 + 1, 0))
    print(ans)