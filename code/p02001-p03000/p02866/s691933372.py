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
D = l()
if D[0] != 0:
    print(0)
    exit()
if D.count(0) != 1:
    print(0)
    exit()
if max(D) == 1:
    print(1)
    exit()
dist = [0]*N
for i in range(N):
    dist[D[i]] += 1
ans = 1
for i in range(2,max(D)+1):
    ans *= dist[i-1]**dist[i]
print(ans%998244353)