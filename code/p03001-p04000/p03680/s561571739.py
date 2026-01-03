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
a = [i() for _ in range(N)]
now = 1
ans = 1
for i in range(N):
    if a[now-1] == 2:
        print(ans)
        exit()
    now = a[now-1]
    ans += 1
print(-1)