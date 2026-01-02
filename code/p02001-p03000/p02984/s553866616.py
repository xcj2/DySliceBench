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
num = sum(A)//2
A += A
for j in range(0,N-2,2):
    num -= A[j]
ans = [0]*N
for i in range(N):
    ans[i] = A[i-1]-num
    num = ans[i]
    ans[i]*= 2
print(*ans)