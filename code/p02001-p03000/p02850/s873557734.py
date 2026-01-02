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

N=II()
mp=[[] for i in range(N+1)]

for i in range(N-1):
    a,b=LI()
    mp[a].append((b, i))
    mp[b].append((a, i))

ma = 0
ma_e = 0
for i, arr in enumerate(mp):
    if len(arr) > ma:
        ma = len(arr)
        ma_e = i

CLS = [0]*(N-1)
VISITED = [0]*(N+1)
Q=deque([(ma_e, 0)])
VISITED[ma_e] = 1

while Q:
    v, c = Q.popleft()
    cnt = 0
    for next_e, i in mp[v]:
        if VISITED[next_e]: continue
        color = ((c + cnt) % ma) + 1
        CLS[i] = color
        # print("{} color{}".format(i, color))

        Q.append((next_e, color))
        VISITED[next_e] = 1
        cnt += 1

print(ma)
for i in CLS: print(i)
