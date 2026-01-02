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
res  = 1
if 0 in a:
    print(0)
    sys.exit()

for i in range(n):
    res *= a[i]
    if res > 10**18:
        print(-1)
        sys.exit()
print(res)