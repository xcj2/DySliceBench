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
mod=10**9+7
MAX=10**5+100
g1=[1,1]
g2=[1,1]
for i in range(2,MAX+1):
    num_1=g1[-1]*i%mod
    g1.append(num_1)
    g2.append(pow(num_1,mod-2,mod))
def cmb(n,r):
    return g1[n]*g2[r]*g2[n-r]%mod

N,K = I()
A = l()
A.sort()
ans = 0
for i in range(N-K+1):
    ans -= A[i]*cmb(N-i-1,K-1)
    ans %= mod
A = A[::-1]
for i in range(N-K+1):
    ans += A[i]*cmb(N-i-1,K-1)
    ans %= mod
print(ans%mod)