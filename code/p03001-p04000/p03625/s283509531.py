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
A = l()
A.sort(reverse=True)
list = []
start = 0
while start < N-1: 
    if A[start] == A[start+1]:
        list.append(A[start])
        start += 2
    else:
        if start == N-2:
            break
        start += 1
if len(list) >= 2:
    print(list[0]*list[1])
else:
    print(0)