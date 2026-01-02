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


n, m = LI()
G = [[] for _ in range(n)]
for x, y in LIR(m):
    G[x - 1] += [y - 1]

dist = [[INF] * n for _ in range(3)]
s, t = LI()
dist[0][s - 1] = 0
dq = deque([(0, s - 1)])
while dq:
    cost, u = dq.popleft()
    for v in G[u]:
        if cost + 1 < dist[(cost + 1) % 3][v]:
            dist[(cost + 1) % 3][v] = cost + 1
            dq += [(cost + 1, v)]


ans = dist[0][t - 1]
if ans == INF:
    print(-1)
else:
    print(ans // 3)



