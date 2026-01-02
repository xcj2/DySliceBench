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
import pprint
sys.setrecursionlimit(10 ** 9)


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


n, m = LI()
co_to_ind = {}
A = []
B = []
for _ in range(n):
    a, b = LI()
    A += [a]
    B += [b]

S = sorted(A)
co_to_ind = {x:i for i, x in enumerate(S)}
X = [0] * (n + 1)
G = [[] for _ in range(n + 1)]

for i in range(n):
    X[co_to_ind[A[i]]] += B[i]

for i in range(n, 0, -1):
    X[i] ^= X[i - 1]

for i in range(m):
    l, r = LI()
    l = bisect_left(S, l)
    r = bisect_left(S, r + 1)
    G[l] += [(r, i)]
    G[r] += [(l, i)]

ans = []
visited = [0] * (n + 1)
def dfs(u):
    visited[u] = 1
    for v, e in G[u]:
        if visited[v]: continue
        dfs(v)
        if X[v]:
            ans.append(e + 1)
            X[u] ^= 1


for i in range(n + 1):
    if visited[i]: continue
    dfs(i)
    if X[i]:
        print(-1)
        exit()


ans.sort()
print(len(ans))
print(*ans)





