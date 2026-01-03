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


n = I()
L = LI()
score = [0]  * (n + 1)
a_max = L[:n]
heapify(a_max)
max_sum = sum(a_max)
score[0] = max_sum
for i in range(n):
    heappush(a_max, L[n+i])
    max_sum += L[n + i]
    max_sum -= heappop(a_max)
    score[i+1] = max_sum



a_min = L[2 * n:]
min_sum = sum(a_min)
score[-1] -= min_sum


for i in range(len(a_min)):
    a_min[i] *= -1


heapify(a_min)


for i in range(n):
    min_sum += L[2*n-i-1]
    heappush(a_min, -L[2*n-i-1])
    min_sum += heappop(a_min)
    score[-2-i] -= min_sum



print(max(score))