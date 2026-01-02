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


n = I()
P = IR(n)
LIS = [0] * (n + 1)
for i in range(n):
    LIS[P[i]] = LIS[P[i] - 1] + 1



print(n - max(LIS))