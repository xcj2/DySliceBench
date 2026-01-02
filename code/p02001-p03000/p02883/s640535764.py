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


n, k = LI()
A = sorted(LI())
F = sorted(LI(), reverse=True)
ok = A[-1] * F[0]
ng = -1
while ok > ng + 1:
    mid = (ok + ng) // 2
    ret = 0
    for i in range(n):
        if A[i] * F[i] > mid:
            ret += (A[i] * F[i] - mid) // F[i] + bool((A[i] * F[i] - mid) % F[i])
    if ret > k:
        ng = mid
    else:
        ok = mid


print(ok)