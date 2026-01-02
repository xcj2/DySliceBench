import sys
import math
import itertools
import bisect
from copy import copy,deepcopy
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

K = i()
if K%2 == 0 or K%5 == 0:
    print(-1)
    exit()
m = 7
for i in range(1,10000000):
    if m%K == 0:
        print(i)
        exit()
    m = (m*10+7)%K
print(K-1)