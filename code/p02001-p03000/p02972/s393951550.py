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
mod = 10**9+7

N = i()
a = l()
table = [0]*N
ans = []
for i in range(N-1,-1,-1):
    bit = 0
    for j in range(i,N,i+1):
        bit = bit^table[j]
    bit = bit^a[i]
    if bit == 1:
        ans.append(i+1)
    table[i] = bit
print(len(ans))
print(*ans)