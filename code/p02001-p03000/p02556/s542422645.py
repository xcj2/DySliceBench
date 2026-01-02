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
zahyo = [l() for _ in range(N)]
zahyo2 = [sum(zahyo[i]) for i in range(N)]
zahyo3 = [zahyo[i][0]-zahyo[i][1] for i in range(N)]
ans = 0
print(max(max(zahyo2)-min(zahyo2),max(zahyo3)-min(zahyo3)))