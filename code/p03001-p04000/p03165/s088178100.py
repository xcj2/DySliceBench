from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_right, bisect_left
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gamma, log
from operator import mul
from functools import reduce
from copy import deepcopy

sys.setrecursionlimit(2147483647)
INF = 10 ** 20
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): pass
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 10 ** 9 + 7


s = S()
t = S()
S,T = len(s),len(t)
dp = [[0]*(T+1) for _ in range(S+1)]
for i in range(S):
    for j in range(T):
        if s[i]==t[j]:
            dp[i+1][j+1] = 1 + dp[i][j]
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])



ans = ""
while dp[S][T]:
    if dp[S - 1][T] == dp[S][T]:
        S -= 1
    elif dp[S][T - 1] == dp[S][T]:
        T -= 1
    else:
        S -= 1
        T -= 1
        ans = s[S] + ans


if len(ans) == 0:
    print("")
else:
    print(ans)
