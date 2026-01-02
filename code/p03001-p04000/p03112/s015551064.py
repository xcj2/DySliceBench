from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
from bisect import bisect_left, bisect_right
import random
from itertools import permutations, accumulate, combinations
import sys
import string



INF = float('inf')
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 10 ** 9 + 7


a, b, q = LI()
s_list = [-INF] + IR(a) + [INF]
t_list = [-INF] + IR(b) + [INF]
x_list = IR(q)


for x in x_list:
    right_shrine_index = bisect_left(s_list, x)
    left_shrine_index = right_shrine_index - 1
    right_temple_index = bisect_left(t_list, x)
    left_temple_index = right_temple_index - 1
    ret = INF
    ret = min(ret, max(s_list[right_shrine_index], t_list[right_temple_index]) - x)
    ret = min(ret, x - min(s_list[left_shrine_index], t_list[left_temple_index]))
    ret = min(ret, min(s_list[right_shrine_index] - x, x - t_list[left_temple_index]) * 2 + max(s_list[right_shrine_index] - x, x - t_list[left_temple_index]))
    ret = min(ret, min(t_list[right_temple_index] - x, x - s_list[left_shrine_index]) * 2 + max(t_list[right_temple_index] - x, x - s_list[left_shrine_index]))
    print(ret)