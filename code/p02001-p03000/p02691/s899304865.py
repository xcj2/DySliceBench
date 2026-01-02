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
a = LIST()
l1 = [i+1+a[i] for i in range(n)]
l2 = [i+1-a[i] for i in range(n)]
c1 = Counter(l1)
c2 = Counter(l2)
res = 0
inter = set(l1) & set(l2)
for value in inter:
    res += c1[value]*c2[value]

print(res)