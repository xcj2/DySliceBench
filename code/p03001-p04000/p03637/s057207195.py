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

N = i()
a = l()
num1 = 0
num2 = 0
num3 = 0
for i in range(N):
    if a[i]%4 == 0:
        num3 += 1
    elif a[i]%2 == 0:
        num2 += 1
    else:
        num1 += 1
if num3+1 < num1:
    print('No')
elif num3+1 == num1 and num2 != 0:
    print('No')
else:
    print('Yes')