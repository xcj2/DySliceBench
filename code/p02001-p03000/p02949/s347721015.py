import sys
import math
import heapq
from collections import deque
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, m=DVSR): return pow(x, m - 2, m)
def DIV(x, y, m=DVSR): return (x * INV(y, m)) % m
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def FLIST(n):
    res = [1]
    for i in range(1, n+1): res.append(res[i-1]*i%DVSR)
    return res

N,M,P=LI()
EDGES = []
E1 = [[] for i in range(N+1)]
E2 = [[] for i in range(N+1)]

for i in range(M):
    F,T,C=LI()
    EDGES.append((F,T,P-C))
    E1[F].append(T)
    E2[T].append(F)

def bellman_ford(edges):
    # print(edges)
    DIST=[10**18]*(N+1)
    DIST[1] = 0
    for i in range(N):
        for j in range(len(edges)):
            fr, to, cost = edges[j]
            if (DIST[to] > DIST[fr] + cost):
                if (i == N-1):
                    print(-1)
                    exit()
                else:
                    DIST[to] = DIST[fr] + cost
    # print(DIST)
    print(max(-DIST[-1], 0))

def dfs(edge, s):
    use= {s}
    q=[s]
    while q:
        v = q.pop()
        for w in edge[v]:
            if w in use:
                continue
            use.add(w)
            q.append(w)
    return use

use = dfs(E1,1) & dfs(E2, N)
# print(use)
bellman_ford([(a,b,c) for a,b,c in EDGES if (a in use and b in use)])
