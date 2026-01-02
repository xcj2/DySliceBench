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


k = I()
cost = [INF] * k
cost[1] = 1
que = deque([1])
while que:
    cur = que.popleft()
    nxt = (cur * 10) % k
    if cost[cur] < cost[nxt]:
        cost[nxt] = cost[cur]
        que.appendleft(nxt)
    nxt = (cur + 1) % k
    if cost[cur] + 1 < cost[nxt]:
        cost[nxt] = cost[cur] + 1
        que.append(nxt)



print(cost[0])
