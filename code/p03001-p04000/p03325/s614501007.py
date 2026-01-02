import sys
import math
import itertools
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
ans = 0
for i in range(N):
    for j in range(100):
        if a[i]%2 == 0:
            ans += 1
            a[i] = a[i]//2
        else:
            break
print(ans)