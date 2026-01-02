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

FIFO=deque()
N,M=LI()
MP=[[[],[],[]] for i in range(N+1)]

# グラフ作成
for _ in range(M):
    i,j=LI()
    MP[i][0].append((j,1))
    MP[i][1].append((j,2))
    MP[i][2].append((j,0))

S,T=LI()
FIFO.append((S,0,0))
visited = [[False,False,False] for i in range(N+1)]
visited[S][0] = True

res = -1
while FIFO:
    i, rest_i, dist = FIFO.popleft()
    if i == T and rest_i == 0:
        res = dist // 3
        break
    for j, rest_j in MP[i][rest_i]:
        if not visited[j][rest_j]:
            visited[j][rest_j] = True
            FIFO.append((j, rest_j, dist+1))

print(res)
