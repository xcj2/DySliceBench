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

n, k = MAP()
a = LIST()


end = [n]*n

for i in range(min(k, 41)):
    b = [0]*(n+1)
    for j in range(n):
        b[max(j-a[j], 0)] +=1
        if j+a[j] <n:
            b[j+a[j]+1] -=1
    for j in range(1,n):
        b[j] += b[j-1]
    a = b[:n]

for i in range(n):
    print(str(int(a[i]))+" ",end = "" )