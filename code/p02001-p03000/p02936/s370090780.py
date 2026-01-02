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
sys.setrecursionlimit(10 ** 9)



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
mod = 10 ** 9 + 7


n, q = LI()
G = [[] for _ in range(n)]
for a, b in LIR(n - 1):
    G[a - 1] += [b - 1]
    G[b - 1] += [a - 1]

D = [0] * n
for p, x in LIR(q):
    D[p - 1] += x


que = [0]
par = [-1] * n
par[0] = 0
while que:
    u = que.pop()
    for v in G[u]:
        if par[v] == -1:
            par[v] = u
            D[v] += D[u]
            que += [v]


print(*D)










