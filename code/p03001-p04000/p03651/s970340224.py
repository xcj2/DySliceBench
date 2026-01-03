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
A = l()
div = A[0]
if K > max(A):
    print('IMPOSSIBLE')
    exit()
for i in range(1,N):
    div = math.gcd(div,A[i])
if K%div == 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')