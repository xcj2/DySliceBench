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
mod = 10**9+7

N,K = I()
A = l()
i = A.index(1)
ans = 10**9
for j in range(K):
    ans = min(ans,math.ceil(max(i-j,0)/(K-1))+math.ceil(min((N-i-1+j),N-1)/(K-1)))
print(ans)