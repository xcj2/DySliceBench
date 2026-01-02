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

a1 = l()
a2 = l()
a3 = l()
AB = a1+a2+a3
c = Counter(AB)
if 1 in AB and 2 in AB and 3 in AB and 4 in AB and list(reversed(sorted(list(c.values()))))[0] == 2:
    print('YES')
else:
    print('NO')