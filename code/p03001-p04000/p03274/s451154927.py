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

N,K = I()
x = l()
i = bisect.bisect_left(x,0)
x.insert(i,0)
start = max(i-K,0)
stop = min(i+K+1,N+1)
x = x[start:stop]
ans = 10**9
for i in range(len(x)-K):
    a = x[i]
    b = x[i+K]
    ans = min(ans,min(abs(a),abs(b))+abs(a-b))
print(ans)