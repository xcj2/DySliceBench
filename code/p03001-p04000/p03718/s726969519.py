from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
from pprint import pprint
from copy import deepcopy
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor
from operator import mul
from functools import reduce
from pprint import pprint


sys.setrecursionlimit(2147483647)
INF = 10 ** 15
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


class Dinic():
    def __init__(self, G, source, sink):
        self.G = G
        self.sink = sink
        self.source = source

    def add_edge(self, u, v, cap):
        self.G[u][v] = cap
        self.G[v][u] = 0

    def bfs(self):
        level = defaultdict(int)
        q = [self.source]
        level[self.source] = 1
        d = 1
        while q:
            if level[self.sink]:
                break
            qq = []
            d += 1
            for u in q:
                for v, cap in self.G[u].items():
                    if cap == 0:
                        continue
                    if level[v]:
                        continue
                    level[v] = d
                    qq += [v]
            q = qq
        self.level = level

    def dfs(self, u, f):
        if u == self.sink:
            return f
        for v, cap in self.iter[u]:
            if cap == 0 or self.level[v] != self.level[u] + 1:
                continue
            d = self.dfs(v, min(f, cap))
            if d:
                self.G[u][v] -= d
                self.G[v][u] += d
                return d
        return 0

    def max_flow(self):
        flow = 0
        while True:
            self.bfs()
            if self.level[self.sink] == 0:
                break
            self.iter = {u: iter(self.G[u].items()) for u in self.G}
            while True:
                f = self.dfs(self.source, INF)
                if f == 0:
                    break
                flow += f
        return flow

h, w = LI()
s = SR(h)
G = defaultdict(lambda:defaultdict(int))
for i in range(h):
    for j in range(w):
        if s[i][j] == 'o':
            G[i][h + j] = 1
            G[h + j][i] = 1
        elif s[i][j] == 'S':
            G[h + w][i] = INF
            G[h + w][h + j] = INF
        elif s[i][j] == 'T':
            G[i][h + w + 1] = INF
            G[h + j][h + w + 1] = INF

ans = Dinic(G, h + w, h + w + 1).max_flow()
print(ans if ans < INF else -1)
