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
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
INF = 10**9
mod = 10**9+7

N = i()
L = l()
L.sort()
ans = 0
for i in range(N):
    for j in range(i+1,N):
        if L[i] != L[j]:
            num = L[i]+L[j]
            for k in range(j,N):
                if L[j] != L[k] and num > L[k]:
                    ans += 1
print(ans)