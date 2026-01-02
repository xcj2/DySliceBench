import sys
import math
import itertools
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
h = l()
ans = 0
start = 0
Flag = 0
for i in range(N-1):
    if h[i] > h[i+1]:
        Flag = 1
    if h[i] < h[i+1] and Flag == 1:
        kukan = h[start:i+1]
        ans -= h[i]
        ans += max(kukan)
        start = i+1
        Flag = 0
kukan = h[start:N]
ans += max(kukan)
print(ans)