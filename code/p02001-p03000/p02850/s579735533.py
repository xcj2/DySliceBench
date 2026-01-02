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



n = I()
G = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = LI()
    G[a - 1] += [(i, b - 1)]
    G[b - 1] += [(i, a - 1)]


k = 0
for i in G:
    k = max(k, len(i))


col_set = set(range(1, k + 1))
ans = [0] * (n - 1)
visited = [0] * n
visited[0] = 1
dq = deque([(0, 0)])
while dq:
    u, pre_col = dq.popleft()
    col = 1
    for i, v in G[u]:
        if not visited[v]:
            visited[v] = 1
            if pre_col == col:
                col += 1
            ans[i] = col
            dq += [(v, col)]
            col += 1


print(k)
for j in ans:
    print(j)








