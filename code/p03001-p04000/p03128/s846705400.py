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


sys.setrecursionlimit(2147483647)
INF = float('INF')
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


n, m = LI()
A = LI()
L = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
match_set = {L[a] for a in A}
dp = [-INF] * (n + 1)
dp[0] = 0
for i in range(n + 1):
    for s in match_set:
        if i - s >= 0:
            dp[i] = max(dp[i - s] + 1, dp[i])

D = defaultdict(int)
for a in A:
    D[L[a]] = max(D[L[a]], a)

kv = sorted(D.items())
digit = dp[n]
ans = ''
while n:
    max_num = 0
    for cost, num in kv:
        if n - cost >= 0 and dp[n - cost] == digit - 1:
            if num > max_num:
                max_num = num
                c = cost
    ans += str(max_num)
    digit -= 1
    n -= c


print(ans)










