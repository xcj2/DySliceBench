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
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
mod = 1000000007


n, m = LI()
G = [[] for _ in range(n)]
for _ in range(m):
    l, r, d = LI()
    G[l - 1] += [(r - 1, d)]
    G[r - 1] += [(l - 1, -d)]

A = [0] * n
visited = [0] * n
for i in range(n):
    if visited[i]:
        continue
    visited[i] = 1
    A[i] = 0
    q = [i]
    while q:
        u = q.pop()
        for v, di in G[u]:
            if visited[v]:
                if A[v] != A[u] + di:
                    print("No")
                    exit()
            else:
                A[v] = A[u] + di
                visited[v] = 1
                q += [v]

print("Yes")
