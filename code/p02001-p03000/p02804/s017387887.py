import sys
from math import factorial
from fractions import Fraction
import heapq, bisect, fractions
import math
import itertools
sys.setrecursionlimit(10 ** 5 + 10)
INF = 10**15 +5
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
MOD = 10**9 + 7

n, k = MAP()
a = LIST()

def mpow(a, n):
    if n == 0:return 1
    if n == 1:return a%MOD
    if n%2 == 1:return (a%MOD * mpow(a, n-1)%MOD)%MOD
    t = mpow(a, n//2)
    return (t*t)%MOD

fac = [1]*(n+1)
inv_fac = [1]*(n+1)
for i in range(n):
    fac[i+1] = (fac[i]*(i+1))%MOD
inv_fac[n] = mpow(fac[n], MOD-2)
for i in range(n, 0, -1):
    inv_fac[i-1] = (inv_fac[i]*i)%MOD

def cmb(n, r):
    if n == 0 and r == 0:return 1
    if n<r or n<0:return 0
    return (fac[n]*(inv_fac[r]*inv_fac[n-r])%MOD)%MOD
 
a.sort(reverse = True)
res = 0
for i in range(n-k+1):
    res += (a[i]*cmb(n-i-1, k-1))%MOD
    res = res%MOD
 
a.reverse()
for i in range(n-k+1):
    res -= (a[i]*cmb(n-i-1, k-1))%MOD
    res = res%MOD
 
print(res)