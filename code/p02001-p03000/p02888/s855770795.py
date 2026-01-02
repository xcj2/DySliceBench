import sys
from collections import Counter, deque, defaultdict
from math import factorial
import bisect
from heapq import heappop, heappush

import math
import itertools
sys.setrecursionlimit(10 ** 5 + 10)
INF = 10**15 +5
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

n = INT()
l = sorted(LIST())
res = 0

for i in range(n-2):
    a = l[i]
    for j in range(i+1, n-1):
        b = l[j]
        index = bisect.bisect_left(l,a+b)
        res += max(index-j-1,0)

print(res)

