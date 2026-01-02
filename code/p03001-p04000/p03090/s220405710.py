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
if not n % 2:
    print(n * (n-1) // 2 - n // 2)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i + j != n + 1 and i < j:
                print(i, j)
else:
    print(n * (n - 1) // 2 - (n - 1) // 2)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i + j != n and i < j:
                print(i, j)