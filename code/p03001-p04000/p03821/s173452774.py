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
A = []
B = []
for i in range(N):
    a,b = I()
    A.append(a)
    B.append(b)
num = 0
for i in range(N-1,-1,-1):
    if (A[i]+num)%B[i] == 0:
        k = 0
    else:
        k = B[i]-((A[i]+num)%B[i])
    A[i] += k+num
    num += k
print(num)