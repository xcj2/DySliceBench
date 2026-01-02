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



n = I()
L = [(0, 0)] + sorted([(k, v) for k, v in Counter(Counter(LI()).values()).items()])
m = len(L)
acc = [0] * m
ret = 0
for j in range(m):
    k, v = L[j]
    ret += k * v
    acc[j] = ret


v_acc = [0] * m
ret = 0
for l in range(m - 1, -1, -1):
    ret += L[l][1]
    v_acc[l] = ret


v_acc += [0]



for i in range(1, n + 1):
    ok = 0
    ng = n // i + 1
    while ng > ok + 1:
        mid = (ng + ok) // 2
        lower_num = bisect_right(L, (mid, INF))
        if acc[lower_num - 1] + v_acc[lower_num] * mid >= i * mid:
            ok = mid
        else:
            ng = mid
    print(ok)