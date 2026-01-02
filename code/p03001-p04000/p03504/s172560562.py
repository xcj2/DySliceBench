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
mod = 10 ** 9 + 7


n, c = LI()
L = [0] * (10 ** 5 + 2)
each_channel = [[] for _ in range(c)]
for s, t, k in LIR(n):
    each_channel[k - 1] += [(s, t)]



for i in each_channel:
    i.sort()


for i in range(c):
    pre_t = -1
    for j in range(len(each_channel[i])):
        s, t = each_channel[i][j]
        if j >= 1 and pre_t == s:
            L[pre_t + 1] += 1
            L[t + 1] -= 1
        else:
            L[s] += 1
            L[t + 1] -= 1
        pre_t = t


print(max(accumulate(L)))
