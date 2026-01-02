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

K = I()

N = 6
a = [100,101,102,103,104,105]
m = [1000000 for i in range(N)]

# initialize
dp = [0 if i==0 else -1 for i in range(K + 1)]

# DP
for i in range(N):
    dp_tmp = []
    for j in range(K + 1):
        if (dp[j] >= 0):
            dp_next = m[i]
        elif ((j < a[i]) or (dp_tmp[j-a[i]] <= 0)):
            dp_next = -1
        else:
            dp_next = dp_tmp[j-a[i]] - 1
        dp_tmp.append(dp_next)
    dp = dp_tmp

if dp[-1] >= 0:
    print(1)
else:
    print(0)

