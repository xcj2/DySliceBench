from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, atan2
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



def dijkstra(G, s=0):
    n = len(G)
    que = [(0, s)]
    dist = [INF] * n
    dist[s] = 0
    while que:
        min_dist, u = heappop(que)
        if min_dist > dist[u]:
            continue
        for v, c in enumerate(G[u]):
            if dist[u] + c < dist[v]:
                dist[v] = dist[u] + c
                heappush(que, (dist[u] + c, v))
    return dist


h, w = LI()
G = LIR(10)
G = [i for i in zip(*G)]
dist = dijkstra(G, 1)
A = LIR(h)
ret = 0
for y in range(h):
    for x in range(w):
        if A[y][x] != -1:
            ret += dist[A[y][x]]


print(ret)