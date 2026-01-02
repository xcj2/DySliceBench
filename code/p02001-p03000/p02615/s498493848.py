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

N = i()
A = l()
A.sort(reverse=True)
ans = 0
lis = [A[0]]
A = A[1:]
for i in range(N-1):
    lis.append(A[i])
    lis.append(A[i])
for i in range(N-1):
    ans += lis[i]
print(ans)