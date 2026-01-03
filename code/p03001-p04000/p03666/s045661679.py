from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
from bisect import bisect_left
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
mod = 998244353



n, a, b, c, d = LI()
for add_cnt in range(n):
    subtract_cnt = n - 1 - add_cnt
    min_val = add_cnt * c - subtract_cnt * d
    max_val = add_cnt * d - subtract_cnt * c
    if min_val <= b - a <= max_val:
        print('YES')
        break
else:
    print('NO')

