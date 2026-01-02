import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7 
#mod = 998244353
from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10

N, K = MAP()
xy = [LIST() for _ in range(N)]
x, y = zip(*xy)

x = sorted(x)
y = sorted(y)

ans = INF
for ax, bx in combinations(x, 2):
	for ay, by in combinations(y, 2):
		cnt = 0
		for cx, cy in xy:
			if ax <= cx <= bx and ay <= cy <= by:
				cnt += 1
		if K <= cnt:
			ans = min(ans, (bx-ax)*(by-ay))

print(ans)