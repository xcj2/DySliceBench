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



sys.setrecursionlimit(2147483647)
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


n, m, r = LI()
graph = [[INF] * n for _ in range(n)]
L = LI()
for u, v, c in LIR(m):
    graph[u - 1][v - 1] = c
    graph[v - 1][u - 1] = c

for i in range(n):
    graph[i][i] = 0


for i in range(n):
    for j in range(n):
        for k in range(n):
            graph[j][k]=min(graph[j][i]+graph[i][k], graph[j][k])



ans = INF
for i in permutations(L):
    ret = 0
    for j in range(r - 1):
        ret += graph[i[j]-1][i[j+1]-1]
    ans = min(ans, ret)


print(ans)