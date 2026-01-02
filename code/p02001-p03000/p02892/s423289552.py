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
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007



def warshall_floyd(G):
    dist = deepcopy(G)
    n = len(G)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


def bipartite_or_not(G, s=0):
    n = len(G)
    global color
    color = [0] * n
    color[s] = 1
    dq = deque([s])
    while dq:
        u = dq.popleft()
        for v, bit in enumerate(G[u]):
            if u == v or bit == '0':
                continue
            elif color[v] == 0:
                color[v] = -color[u]
                dq += [v]
            else:
                if color[u] == color[v]:
                    return False
    return True



n = I()
G = SRL(n)
if not bipartite_or_not(G):
    print(-1)
    exit()


for u in range(n):
    for v in range(n):
        if u == v:
            G[u][v] = 0
        elif G[u][v] == '1':
            G[u][v] = 1
        else:
            G[u][v] = INF


dist = warshall_floyd(G)
print(max([dist[u][v] for u in range(n) for v in range(u + 1, n)]) + 1)