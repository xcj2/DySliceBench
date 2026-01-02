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
import pprint
sys.setrecursionlimit(10 ** 9)


INF = 10 ** 20
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


n, m, v, p = LI()
A = LI()
A.sort()
def bi(x):
    if A[x] + m < A[-p]:
        return 0
    if x + p >= v:
        return 1
    ret = (x + p) * m
    l = x + 1
    r = n - p + 1
    for i in range(l, r):
        ret += A[x] + m - A[i]
        if ret >= v * m:
            return 1
    return 0


ok = n - p
ng = -1
while ok > ng + 1:
    mid = (ok + ng) // 2
    if bi(mid):
        ok = mid
    else:
        ng = mid


print(n - ok)