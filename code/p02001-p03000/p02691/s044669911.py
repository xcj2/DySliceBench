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
mod = 10**9+7

N = i()
A = l()
L = []
L2 = [0]*(10**6)
for i in range(N):
    if i+A[i]+1 < 10**6:
        L.append(i+A[i]+1)
    if i-A[i]+1 >= 0 and i-A[i]+1 < 10**6:
        L2[i-A[i]+1] += 1
ans = 0
for l in L:
    ans += L2[l]
print(ans)