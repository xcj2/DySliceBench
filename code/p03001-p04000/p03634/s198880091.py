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
INF = 10 ** 13
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


n = I()
G = [[] for _ in range(n)]
for a, b, c in LIR(n - 1):
    G[a - 1] += [(b - 1, c)]
    G[b - 1] += [(a - 1, c)]

q, k = LI()
dq = deque([k - 1])
dist = [-1] * n
dist[k - 1] = 0
while dq:
    u = dq.pop()
    for v, c in G[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + c
            dq += [v]

for _ in range(q):
    x, y = LI()
    print(dist[x - 1] + dist[y - 1])


