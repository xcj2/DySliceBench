import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import accumulate, permutations, combinations, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from heapq import heappush, heappop
from functools import reduce
from pprint import pprint
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, M, S = MAP()
graph = [[] for _ in range(N)]
for _ in range(M):
    U, V, A, B = MAP()
    graph[U-1].append((V-1, A, B))
    graph[V-1].append((U-1, A, B))

C, D = ZIP(N)
M = 2500
if S >= M: S = M-1
dist = [[INF]*M for _ in range(N)]
dist[0][S] = 0
q = [(0, S, 0)]

while q:
    d, coin, n = heappop(q)
    if coin + C[n] < M and d+D[n] < dist[n][coin+C[n]]:
        dist[n][coin+C[n]] = d+D[n]
        heappush(q, (d+D[n], coin + C[n], n))
    for node, cnode, dnode in graph[n]:
        nd = d + dnode
        if coin >= cnode and nd < dist[node][coin-cnode]:
            dist[node][coin-cnode] = nd
            heappush(q, (nd, coin-cnode, node))

for i in range(1, N):
    print(min(dist[i]))
