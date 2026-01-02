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

N,M,K = I()
A = l()
B = l()
ruiseki = [-1]+list(itertools.accumulate(A))
num = 0
ans = bisect.bisect_right(ruiseki,K)-1
for i in range(M):
    num += B[i]
    if num > K:
        break
    ans = max(ans,bisect.bisect_right(ruiseki,K-num)+i)
print(ans)