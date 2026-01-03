from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, atan2, degrees
from operator import mul
from functools import reduce
sys.setrecursionlimit(10**8)

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


w, h, n = LI()
l, r, u, d = 0, w, h, 0
for _ in range(n):
    x, y, a = LI()
    if a == 1:
        l = max(l, x)
    elif a == 2:
        r = min(r, x)
    elif a == 3:
        d = max(d, y)
    else:
        u = min(u, y)




if u < d or r < l:
    print(0)
else:
    print((u - d) * (r - l))







