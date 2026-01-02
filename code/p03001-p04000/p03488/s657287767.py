from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
from pprint import pprint
from copy import deepcopy
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce
from pprint import pprint


sys.setrecursionlimit(2147483647)
INF = 10 ** 13
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


s = S() + 'T'
x, y = LI()
t_flag = 0
# 0の時横移動、1の時縦移動。
flag = 0
y_now = x_now = 1 << 8000
f_cnt = 0
for j in s:
    if j == 'T':
        if not flag:
            flag = 1
            x_now >>= f_cnt
        elif t_flag:
            y_now = y_now >> f_cnt | y_now << f_cnt
        else:
            x_now = x_now >> f_cnt | x_now << f_cnt
        t_flag ^= 1
        f_cnt = 0
    else:
        f_cnt += 1


if 1 << 8000 + y & y_now and 1 << 8000 - x & x_now:
    print('Yes')
else:
    print('No')