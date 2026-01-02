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


d, g = LI()
g //= 100
p, c = list(zip(*LIR(d)))
c = [c[i] // 100 for i in range(d)]



ans = INF
for i in range(2 ** d):
    cnt = 0
    score = 0
    for j in range(d):
        if 1 << j & i:
            cnt += p[j]
            score += (j + 1) * p[j]
            score += c[j]


    max_score = -INF
    for k in range(d):
        if not (1 << k) & i:
            max_score = max(max_score, k + 1)
    if score < g:
        remain_num = (g - score) // max_score + bool((g - score) % max_score)
        if remain_num >= p[max_score - 1]:
            continue
        cnt += remain_num
    ans = min(ans, cnt)


print(ans)