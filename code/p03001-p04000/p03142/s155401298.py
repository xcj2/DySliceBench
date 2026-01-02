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

n, m = LI()
G = [set() for _ in range(n)]
RG = [set() for _ in range(n)]
for _ in range(n - 1 + m):
    a, b = LI()
    G[a - 1].add(b - 1)
    RG[b - 1].add(a - 1)

r = 0
while RG[r]:
    for v in RG[r]:
        r = v
        break

def topological_sort():
    in_degree = [0] * n
    D = {}
    for u in range(n):
        in_degree[u] += len(RG[u])
    dq = deque([r])
    cnt = 0
    while dq:
        u = dq.pop()
        D[u] = cnt
        cnt += 1
        for v in G[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                dq += [v]
    return D

D = topological_sort()
for u in range(n):
    par = 0
    ret = -1
    for v in RG[u]:
        if D[v] > ret:
            ret = D[v]
            par = v + 1
    print(par)






