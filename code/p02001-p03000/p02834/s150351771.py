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
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())
def FLIST(n):
    res = [1]
    for i in range(1, n+1): res.append(res[i-1]*i%DVSR)
    return res
def gcd(x, y):
    if x < y: x, y = y, x
    div = x % y
    while div != 0:
        x, y = y, div
        div = x % y
    return y

N,u,v=LI()

TR=[[] for i in range(N+1)]
for _ in range(N-1):
    i,j=LI()
    TR[i].append(j)
    TR[j].append(i)

DIST1=[-1]*(N+1)
DIST2=[-1]*(N+1)
FIFO = deque()

FIFO.append((v,0))
while FIFO:
    edge, dist = FIFO.popleft()
    DIST1[edge] = dist
    for i in TR[edge]:
        if DIST1[i] == -1:
            FIFO.append((i, dist+1))

FIFO.append((u, 0))

farest = 0
while FIFO:
    edge, dist = FIFO.popleft()
    DIST2[edge] = dist
    farest = max(farest, DIST1[edge])
    for i in TR[edge]:
        if DIST2[i] == -1 and dist+1 < DIST1[i]:
            FIFO.append((i, dist+1))

# print(DIST1)
# print(DIST2)
print(max(0, farest-1))
