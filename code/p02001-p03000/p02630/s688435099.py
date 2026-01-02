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

N = i()
A = l()
Q = i()
c = dict(Counter(A))
ans = sum(A)
for i in range(Q):
    B,C = I()
    if B in c:
        b = c.pop(B)
        ans += b*(C-B)
        d = 0
        if C in c:
             d = c.pop(C)
        c[C] = b+d
    print(ans)