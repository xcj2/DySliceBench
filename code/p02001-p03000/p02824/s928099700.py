import sys
from math import factorial
from fractions import Fraction
import heapq, bisect, fractions
import math
import itertools
sys.setrecursionlimit(10 ** 5 + 10)
INF = 10**15 +5
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
MOD = 10**9 + 7

n, m, v, p = MAP()
a = LIST()
a = sorted(a, reverse=True)

def hantei(i):
    if i < p: return True
    if a[p-1] > a[i] + m: return False
    if ((i-p+1)*(a[i]+m)-sum(a[p-1:i]))+m*(p-1+n-i) < m*v: return False
    return True

if hantei(n-1):
    print(n)
    sys.exit()
    
right = n-1
left = 0

while right-left > 1:
    mid = (right+left)//2
    if hantei(mid):
        left = mid
    else:
        right = mid

print(right)
