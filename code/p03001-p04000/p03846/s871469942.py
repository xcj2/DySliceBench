import sys
import math
import itertools
import bisect
from copy import copy,deepcopy
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
A = l()
ans = 1
l = [0]*N
for i in range(N):
    l[A[i]] += 1
for i in range(N):
    c = l[i]
    if N%2 == i%2:
        if c:
            ans *= 0
    else:
        if c == 0:
            ans *= 0
        if c == 1:
            if i != 0:
                ans *= 0
        if c == 2:
            ans *= 2
print(ans%mod)