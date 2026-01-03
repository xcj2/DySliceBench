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

N,M = I()
a = [l() for _ in range(N)]
b = [l() for _ in range(M)]
for i in range(N):
    num1 = INF
    num2 = 0
    for j in range(M):
        if abs(b[j][0]-a[i][0])+abs(b[j][1]-a[i][1]) < num1:
            num1 = abs(b[j][0]-a[i][0])+abs(b[j][1]-a[i][1])
            num2 = j+1
    print(num2)