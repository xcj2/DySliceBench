from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
from copy import deepcopy
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
mod = 1000000007



n, m = LI()
G = [[] for _ in range(n)]
for a, b, c in LIR(m):
    G[a - 1] += [(b - 1, c)]

# 負の閉路がなかったら高々n-1回で更新は終わるはずn回目に更新が起こったとしたら負の閉路がある。
def bellman_ford(G, s=0):
    n = len(G)
    dist = [-INF] * n
    dist[s] = 0
    v_nows = {s}
    for _ in range(n):
        v_changeds = set()
        for u in v_nows:
            for v, c in G[u]:
                if dist[u] + c > dist[v]:
                    dist[v] = dist[u] + c
                    v_changeds.add(v)
        v_nows = v_changeds
    if not v_changeds:
        return dist[n - 1]
    for i in v_nows:
        dist[i] = INF
    dq = deque(v_nows)
    while dq:
        u = dq.popleft()
        if u == n - 1:
            return "inf"
        for v, c in G[u]:
            if dist[v] != INF:
                dist[v] = INF
                dq += [v]
    return dist[n - 1]



print(bellman_ford(G))

