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

n = INT()
sumlist = [(0,0)]*n
res = 0
for i in range(n):
    aa,bb = MAP()
    sumlist[i] = (aa, bb)

sumlist = sorted(sumlist, key = lambda x:x[0]+x[1], reverse = True)
for i in range(n):
    res += (-1)**i * sumlist[i][i%2]

print(res)
    