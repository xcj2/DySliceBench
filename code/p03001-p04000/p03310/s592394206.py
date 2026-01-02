from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor


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
mod = 1000000007


n = I()
L = list(accumulate(LI() + [0]))
ret = INF
for second_point in range(2, n-1):
    left_sum = L[second_point - 1]
    right_sum = L[-1] - left_sum
    if L[bisect_left(L, left_sum/2)] - left_sum/2 < left_sum/2 - L[bisect_left(L, left_sum/2) - 1] or not bisect_left(L, left_sum/2):
        p = L[bisect_left(L, left_sum/2)]
    else:
        p = L[bisect_left(L, left_sum/2) - 1]
    q = left_sum - p
    if L[bisect_left(L, left_sum + right_sum/2)] - right_sum/2 - left_sum < left_sum + right_sum/2 - L[bisect_left(L, left_sum + right_sum/2) - 1]:
        s = L[-1] - L[bisect_left(L, left_sum + right_sum/2)]
    else:
        s = L[-1] - L[bisect_left(L, left_sum + right_sum/2) - 1]
    r = right_sum - s
    ret = min(ret, max(p, q, r, s) - min(p, q, r, s))


print(ret)