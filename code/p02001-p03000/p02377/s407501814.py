import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import accumulate, permutations, combinations, product, groupby, combinations_with_replacement
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

class MinCostFlow:
    def __init__(self, n):
        self.n = n
        self.g = [[] for i in range(n)]


    def add_edge(self, fr, to, cap, cost):
        G = self.g
        G[fr].append([to, cap, cost, len(G[to])])
        G[to].append([fr, 0, -cost, len(G[fr])-1])

    def flow(self, s, t, f):
        N = self.n
        G = self.g
        INF = 10**18

        prevv = [0]*N
        preve = [0]*N

        res = 0
        while f > 0:
            dist = [INF]*N
            dist[s] = 0
            update = True

            while update:
                update = False
                for v in range(N):
                    if dist[v] == INF: continue
                    for i in range(len(G[v])):
                        to, cap, cost, rev = G[v][i]
                        if cap > 0 and dist[to] > dist[v]+cost:
                            dist[to] = dist[v]+cost
                            prevv[to] = v
                            preve[to] = i
                            update = True

            if dist[t] == INF:
                return -1

            d = f
            v = t
            while v != s:
                d = min(d, G[prevv[v]][preve[v]][1])
                v = prevv[v]
            f -= d
            res += d*dist[t]

            v = t
            while v != s:
                e = G[prevv[v]][preve[v]]
                e[1] -= d
                G[v][e[3]][1] += d
                v = prevv[v]

        return res
            

V, E, F = MAP()
mcf = MinCostFlow(V)
for _ in range(E):
    u, v, c, d = MAP()
    mcf.add_edge(u, v, c, d)
print(mcf.flow(0, V-1, F))

