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
mod = 998244353


n, m = LI()
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = LI()
    G[a - 1] += [b - 1]
    G[b - 1] += [a - 1]

ans = [0] * n
q = I()
Q = LIR(q)
dq = deque()
depth = [-1] * n
for v, d, c in Q[::-1]:
    if depth[v - 1] >= d:
        continue
    if ans[v - 1] == 0:
        ans[v - 1] = c
    depth[v - 1] = d
    if d:
        dq += [v - 1]
    while dq:
        u = dq.popleft()
        for x in G[u]:
            if ans[x] == 0:
                ans[x] = c
            if depth[x] >= depth[u] - 1:
                continue
            depth[x] = depth[u] - 1
            if depth[x]:
                dq += [x]

print(*ans, sep="\n")
