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
INF = 10**9
mod = 10**9+7

N,M = I()
a = l()
num1 = format(a[0],'b')[::-1].find('1')
num2 = 1
for i in range(N):
  num2 = lcm(num2,a[i])
  if num1 != format(a[i],'b')[::-1].find('1'):
    print(0)
    exit()
num2 = num2//2
print(math.ceil(M//num2/2))