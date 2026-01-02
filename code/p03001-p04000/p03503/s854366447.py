import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
def s(): return input()
def i(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def L(): return list(map(int,input().split()))
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
INF = 10**9
mod = 10**9+7

N = i()
F = [l() for _ in range(N)]
P = [l() for _ in range(N)]
ans = INF*-1
for bit in range(1,1<<10):
    nans = 0
    B = [(bit>>i)&1 for i in range(10)]
    for i in range(N):
        cnt = 0
        for j in range(10):
            if B[j] == 1 and F[i][j] == 1:
                cnt += 1
        nans += P[i][cnt]
    ans = max(ans,nans)
print(ans)