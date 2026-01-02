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
D = [l() for _ in range(N)]
cnt = 0
for i in range(N):
    if D[i][0] == D[i][1]:
        cnt += 1
        if cnt == 3:
            break
    else:
        cnt = 0
if cnt == 3:
    print('Yes')
else:
    print('No')