# coding: utf-8

import sys
import math
import collections
import itertools
import bisect
INF = 10 ** 13
MOD = 10 ** 9 + 7
def input() : return sys.stdin.readline().strip()
def lcm(x, y) : return (x * y) // math.gcd(x, y)
def I() : return int(input())
def LI() : return [int(x) for x in input().split()]
def RI(N) : return [int(input()) for _ in range(N)]
def LRI(N) : return [[int(x) for x in input().split()] for _ in range(N)]
def LS() : return input().split()
def RS(N) : return [input() for _ in range(N)]
def LRS(N) : return [input().split() for _ in range(N)]
def PL(L) : print(*L, sep="\n")
def YesNo(B) : print("Yes" if B else "No")
def YESNO(B) : print("YES" if B else "NO")

def tobit(N):
    ret = 0
    for n in N:
        ret |= (1 << n)
    
    return ret

N, M = LI()
C = []
for i in range(M):
    a, b = LI()
    C.append([a, tobit([x-1 for x in LI()])])

dp = [INF] * (1 << N)
dp[0] = 0

for i in range(1 << N):
    for cost, key in C:
        dp[i | key] = min(dp[i | key], dp[i] + cost)

print(dp[-1] if dp[-1] != INF else "-1")
