# coding: utf-8

import sys
import math
import collections
import itertools
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

N, M = LI()
A = RI(M)

dp = [0] * (N+10)
dp[0] = 1
j = 0
for i in range(N):
    if j < M and i == A[j]:
        j += 1
        continue

    dp[i+1] = ((dp[i] % MOD) + (dp[i+1] % MOD)) % MOD
    dp[i+2] = ((dp[i] % MOD) + (dp[i+2] % MOD)) % MOD

print(dp[N])
