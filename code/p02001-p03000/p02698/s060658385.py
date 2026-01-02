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
from itertools import combinations_with_replacement, combinations
from operator import mul
from functools import reduce
from operator import mul


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
A = LI()
G = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = LI()
    G[a - 1] += [b - 1]
    G[b - 1] += [a - 1]

depth = [0] * n
def euler_tour():
    euler = []
    dq = deque([0])
    dq2 = deque()
    visited = [0] * n
    while dq:
        u = dq.pop()
        euler += [u]
        if visited[u]:
            continue
        for v in G[u]:
            if visited[v]:
                dq += [v]
            # [親頂点、子頂点、子頂点、。。。]と入れていく.その後連結
            else:
                depth[v] = depth[u] + 1
                dq2 += [v]
        dq.extend(dq2)
        dq2 = deque()
        visited[u] = 1
    return euler


order = euler_tour()
ans = [1] * n
P = [0] * n
LIS = [A[0]]
pre = 0
ret = 1
for j in range(1, len(order)):
    i = order[j]
    if depth[i] > depth[pre]:
        if A[i] > LIS[-1]:
            LIS += [A[i]]
            ret += 1
            P[i] = (-1, 0)
        else:
            idx = bisect_left(LIS, A[i])
            P[i] = (idx, LIS[idx])
            LIS[idx] = A[i]
        ans[i] = ret
    else:
        idx, e = P[pre]
        if idx == -1:
            LIS.pop()
            ret -= 1
        else:
            LIS[idx] = e
    pre = i

print(*ans, sep='\n')