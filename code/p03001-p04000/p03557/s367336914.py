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

N = i()
C = l()
B = l()
A = l()
B.sort()
C.sort()
l = []
for i in range(N):
    l.append(bisect.bisect_left(C,B[i]))
ruiseki = [0]+list(itertools.accumulate(l))
ans = 0
for i in range(N):
    num = bisect.bisect_left(B,A[i])
    ans += ruiseki[num]
print(ans)