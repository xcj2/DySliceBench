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
from operator import mul


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


n, m, s = LI()
G = [[] for _ in range(n)]
for _ in range(m):
    u, v, a, b = LI()
    G[u - 1] += [(v - 1, a, b)]
    G[v - 1] += [(u - 1, a, b)]

change = LIR(n)

def dijkstra(s):
    hq = [(0, 0, s)]
    dist = [[INF] * 2451 for _ in range(n)]
    dist[0][s] = 0
    while hq:
        t, u, coin = heappop(hq)
        if t > dist[u][coin]:
            continue
        if t + change[u][1] < dist[u][min(2450, coin + change[u][0])]:
            dist[u][min(2450, coin + change[u][0])] = t + change[u][1]
            heappush(hq, (t + change[u][1], u, min(2450, coin + change[u][0])))
        for v, c, d in G[u]:
            if coin - c >= 0 and t + d < dist[v][coin - c]:
                dist[v][coin - c] = t + d
                heappush(hq, (t + d, v, coin - c))
    return dist

D = dijkstra(min(2450, s))
for t in range(1, n):
    print(min(D[t]))