import sys
import math
import heapq
from collections import deque
from itertools import combinations
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

H,W=LI()
MP=[input() for _ in range(H)]
CORD=[(i,j) for i in range(H) for j in range(W)]

max_dist = 0
for i in range(len(CORD)):
    st = CORD[i]
    if MP[st[0]][st[1]] == ".":
        QUE=deque()
        visited = [[0]*W for i in range(H)]
        visited[st[0]][st[1]] = 1
        QUE.append((st[0], st[1], 0))
        res = 0
        while QUE:
            ii, jj, dist = QUE.popleft()
            max_dist = max(max_dist, dist)
            for iii, jjj in [(ii-1,jj),(ii+1,jj),(ii,jj-1),(ii,jj+1)]:
                if iii >= 0 and jjj >= 0 and iii < H and jjj < W and MP[iii][jjj] != '#' and not visited[iii][jjj]:
                    QUE.append((iii, jjj, dist+1))
                    visited[iii][jjj] = 1


print(max_dist)
