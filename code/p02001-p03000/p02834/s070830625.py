from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from bisect import bisect_right, bisect_left
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gamma, log
from operator import mul
from functools import reduce


sys.setrecursionlimit(2147483647)
INF = 1 << 100
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


n, u, v = LI()
G = [[] for _ in range(n)]
for a, b in LIR(n - 1):
    G[a - 1] += [b - 1]
    G[b - 1] += [a - 1]


def bfs(root):
    dq = deque([root])
    dist = [-1] * n
    dist[root] = 0
    while dq:
        u = dq.popleft()
        for v in G[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                dq += [v]
    return dist


dist_u = bfs(u - 1)
dist_v = bfs(v - 1)
ans = 0
for i in range(n):
    if dist_v[i] > dist_u[i]:
        ans = max(ans, dist_v[i] - 1)


print(ans)
