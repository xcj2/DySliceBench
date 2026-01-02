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


def bipartite_or_not(G, s=0):
    n = len(G)
    global color
    color = [0] * n
    color[s] = 1
    dq = deque([s])
    while dq:
        u = dq.popleft()
        for v in G[u]:
            if color[v] == 0:
                color[v] = -color[u]
                dq += [v]
            else:
                if color[u] == color[v]:
                    return False
    return True


n, m = LI()
G = [[] for _ in range(n)]
for a, b in LIR(m):
    G[a - 1] += [b - 1]
    G[b - 1] += [a - 1]


if bipartite_or_not(G):
    print(color.count(1) * color.count(-1) - m)
else:
    print(n * (n - 1) // 2 - m)