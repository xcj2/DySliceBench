from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate
import sys



def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LIM(): return list(map(lambda x:int(x) - 1, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def LIRM(n): return [LIM() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
mod = 1000000007


n, m = LI()
values = sorted(LI(), reverse=True)
weights = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]


dp = [-float('inf')] * (n+1)
dp[0] = 0



for i in values:
    for j in range(weights[i], n+1):
        dp[j] = max(dp[j - weights[i]] * 10 + i, dp[j])


print(dp[-1])