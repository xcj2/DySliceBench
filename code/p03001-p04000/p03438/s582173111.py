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
mod = 10**9+7

N = i()
a = l()
b = l()
num = sum(b)-sum(a)
cnt1 = 0
cnt2 = 0
for i in range(N):
    if a[i] > b[i]:
        cnt1 += a[i]-b[i]
    if a[i] < b[i]:
        cnt2 += math.ceil((b[i]-a[i])/2)
if cnt1 > num or cnt2 > num:
    print('No')
else:
    print('Yes')
