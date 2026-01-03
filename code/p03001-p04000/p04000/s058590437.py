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
from operator import mul
from functools import reduce


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



h, w, n = LI()
A = []
for a, b in LIR(n):
    for i, j in product((1, 0, -1), (1, 0, -1)):
        if 2 <= a + i <= h - 1 and 2 <= b + j <= w - 1:
            A += [(a + i, b + j)]


ans = [0 for i in range(9)]
for k, v in Counter(A).items():
    ans[v - 1] += 1


print((h - 2) * (w - 2) - sum(ans))
for j in ans:
    print(j)