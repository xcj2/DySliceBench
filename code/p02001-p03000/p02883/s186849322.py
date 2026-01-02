import sys
from collections import Counter, deque, defaultdict
from math import factorial
from fractions import Fraction
import heapq, bisect
import math
import itertools
sys.setrecursionlimit(10 ** 5 + 10)
INF = 10**15 +5
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

n, k = MAP()
a = LIST()
f = LIST()
a = sorted(a, reverse = True)
f = sorted(f)

def ok(x):
    res = 0
    for i in range(n):
        res += max(a[i] - x//f[i], 0)
    return res <= k

l = -1
r = INF
while l+1 < r:
    mid = (l+r)//2
    if ok(mid):
        r = mid
    else:
        l = mid
print(r)