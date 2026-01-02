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

D = i()
c = l()
s = [l() for _ in range(D)]
t = [i() for _ in range(D)]
last = [0]*26
ans = 0
for i in range(D):
    last[t[i]-1] = i+1
    ans += s[i][t[i]-1]
    for j in range(26):
        ans -= c[j]*(i+1-last[j])
    print(ans)