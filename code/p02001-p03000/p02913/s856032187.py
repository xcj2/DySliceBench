# coding: utf-8

import sys
import math
import collections
import itertools
from inspect import currentframe
INF = 10 ** 10
MOD = 10 ** 9 + 7
def input() : return sys.stdin.readline().strip()
def gcd(x, y) : return y if x % y == 0 else gcd(y, x % y)
def lcm(x, y) : return (x * y) // gcd(x, y)
def I() : return int(input())
def MI() : return map(int, input().split())
def LI() : return [int(x) for x in input().split()]
def RI(N) : return [int(input()) for _ in range(N)]
def LRI(N) : return [[int(x) for x in input().split()] for _ in range(N)]
def chkprint(*args) : names = {id(v):k for k,v in currentframe().f_back.f_locals.items()}; print(', '.join(names.get(id(arg),'???')+' = '+repr(arg) for arg in args))

N = I()
S = input()

def Z_alg(s):
    n = len(s)
    z = [0]*n
    z[0] = n

    L = 0
    R = 0
    for i in range(1, n):
        if(i >= R):  # 過去の結果が全く使えない
            L = i
            R = i
            while(R < n and s[R-L] == s[R]):
                R += 1
            z[i] = R-L
        elif(z[i-L] < R-i):  # 過去の結果が全て使える
            z[i] = z[i-L]
        else:  # 過去の結果が一部使える
            L = i
            while(R < n and s[R-L] == s[R]):
                R += 1
            z[i] = R-L

    return z

ans = 0
for i in range(N):
    z = Z_alg(S[i:])
    
    for j, l in enumerate(z):
        ans = max(ans, min(j, l))

print(ans)
