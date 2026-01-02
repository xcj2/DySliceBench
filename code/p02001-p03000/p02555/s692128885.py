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
sys.setrecursionlimit(10**9)
INF = 10**9
mod = 10**9+7

def cmb(n,k,p):
    x,y = 1,1
    for i in range(k):
        x=x*(n-i)%p
        y=y*(i+1)%p
    return x*pow(y,p-2,p)%p

s = i()
s -= 3
ans = 0
if s >= 0:
    ans += 1
for i in range(1,10000):
    s -= 3
    if s < 0:
        break
    ans += cmb(s+i,i,mod)
print(ans%mod)