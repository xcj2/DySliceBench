import sys
import math
import heapq
sys.setrecursionlimit(10**7)
INTMAX = 9323372036854775807
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

N,M,L=LI()

LG=10**15
DIST=[[LG for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    a,b,c = LI()
    if c <= L:
        DIST[a][b] = c
        DIST[b][a] = c

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if DIST[i][j] > DIST[i][k] + DIST[k][j]:
                DIST[i][j] = DIST[i][k] + DIST[k][j]

for i in range(1, N+1):
    for j in range(1, N+1):
        DIST[i][j] = 1 if DIST[i][j] <= L else LG

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if DIST[i][j] > DIST[i][k] + DIST[k][j]:
                DIST[i][j] = DIST[i][k] + DIST[k][j]

for i in range(II()):
    st, en = LI()
    if DIST[st][en] >= LG:
        print(-1)
    else:
        print(DIST[st][en] - 1)
