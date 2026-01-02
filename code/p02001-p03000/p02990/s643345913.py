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
fact = math.factorial
sys.setrecursionlimit(10**9)
INF = 10**9
mod = 10**9+7

N,K = I()
ans = 0
f1 = fact(N-K+1)
f2 = fact(K-1)
for i in range(1,K+1):
    if N-K-i+1 < 0:
        print(0)
        continue
    print((f1*f2//(fact(i)**2//i*fact(N-K-i+1)*fact(K-i)))%mod)