# coding: utf-8

import sys
import math
import collections
import itertools
import bisect
INF = 10 ** 13
MOD = 10 ** 9 + 7
def input() : return sys.stdin.readline().strip()
def gcd(x, y) : return x if y == 0 else gcd(y, x%y)
def lcm(x, y) : return (x * y) // gcd(x, y)
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

N, M, X = LI()
CA = LRI(N)

ans = INF
for bit in range(1 << N):
    Ms = [0] * M
    tmp = 0
    for i in range(N):
        if (bit >> i) & 1:
            for j in range(M):
                Ms[j] += CA[i][j+1]
            
            tmp += CA[i][0]
    
    flag = True
    for m in Ms:
        if m < X:
            flag = False
    
    if flag:
        ans = min(ans, tmp)

print("-1" if ans == INF else ans)
