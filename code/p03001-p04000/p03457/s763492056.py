from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial


INF = float('inf')
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LIM(): return list(map(lambda x:int(x) - 1, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def LIRM(n): return [LIM() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
mod = 1000000007


n = I()
L = [[0, 0, 0]] + LIR(n)
for i in range(n):
    t, x, y = L[i]
    nxt_t, nxt_x, nxt_y = L[i+1]
    if nxt_t - t < abs(nxt_x - x) + abs(nxt_y - y) or (abs(nxt_x - x) + abs(nxt_y - y) - nxt_t - t) % 2:
        print('No')
        break
else:
    print('Yes')