# coding: utf-8

import sys
import math
import collections
import itertools
from functools import lru_cache
INF = 10 ** 13
MOD = 10 ** 9 + 7
def input() : return sys.stdin.readline().strip()
def gcd(x, y) : return y if x % y == 0 else gcd(y, x % y)
def lcm(x, y) : return (x * y) // gcd(x, y)
def I() : return int(input())
def LI() : return [int(x) for x in input().split()]
def RI(N) : return [int(input()) for _ in range(N)]
def LRI(N) : return [[int(x) for x in input().split()] for _ in range(N)]
def LS() : return input().split()
def RS(N) : return [input() for _ in range(N)]
def LRS(N) : return [input().split() for _ in range(N)]
def PL(L) : print(*L, sep="\n")

H, W = LI()
S = RS(H)

L = [[0] * W for _ in range(H)]
R = [[0] * W for _ in range(H)]
U = [[0] * W for _ in range(H)]
D = [[0] * W for _ in range(H)]

for i in range(H):
    lf = 0
    rf = 0
    for j in range(W):
        if S[i][j] == ".":
            lf += 1
            L[i][j] = lf
        else:
            lf = 0

        if S[i][W-1-j] == ".":
            rf += 1
            R[i][W-1-j] = rf
        else:
            rf = 0

for i in range(W):
    uf = 0
    df = 0
    for j in range(H):
        if S[j][i] == ".":
            df += 1
            D[j][i] = df
        else:
            df = 0

        if S[H-1-j][i] == ".":
            uf += 1
            U[H-1-j][i] = uf
        else:
            uf = 0

ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            ans = max(ans, U[i][j]+D[i][j]+L[i][j]+R[i][j]-3)

print(ans)
