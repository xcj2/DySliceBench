import sys
from math import factorial
from collections import Counter
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

n = INT()
a = [0]*(n+1)
b = [0]*(n+1)
for i in range(1,n+1):
    aa, bb = MAP()
    a[i] = aa
    b[i] = bb

a = sorted(a)
b = sorted(b)
if n%2 ==1:
    res = b[n//2 + 1]-a[n//2 + 1] +1
else:
    res = b[n//2] + b[n//2 + 1] - a[n//2] - a[n//2 + 1] + 1

print(res)