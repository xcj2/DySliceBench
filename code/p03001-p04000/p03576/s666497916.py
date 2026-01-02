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

ans = INF
for (ax, ay), (bx, by) in combinations(xy, 2):
	edge_left = min(ax, bx)
	edge_right = max(ax, bx)
	edge_top = max(ay, by)
	edge_bottom = min(ay, by)
	cnt = 0
	for cx, cy in xy:
		if cx == ax or cx == bx:
			continue
		elif edge_left <= cx <= edge_right and edge_bottom <= cy <= edge_top:
			cnt += 1
	if K <= cnt+2:
		ans = min((edge_right-edge_left)*(edge_top-edge_bottom), ans)

for (ax, ay), (bx, by), (cx, cy) in combinations(xy, 3):
	edge_left = min(ax, bx, cx)
	edge_right = max(ax, bx, cx)
	edge_top = max(ay, by, cy)
	edge_bottom = min(ay, by, cy)
	cnt = 0
	for dx, dy in xy:
		if dx == ax or dx == bx or dx == cx:
			continue
		elif edge_left <= dx <= edge_right and edge_bottom <= dy <= edge_top:
			cnt += 1
	if K <= cnt+3:
		ans = min((edge_right-edge_left)*(edge_top-edge_bottom), ans)

for (ax, ay), (bx, by), (cx, cy), (dx, dy) in combinations(xy, 4):
	edge_left = min(ax, bx, cx, dx)
	edge_right = max(ax, bx, cx, dx)
	edge_top = max(ay, by, cy, dy)
	edge_bottom = min(ay, by, cy, dy)
	cnt = 0
	for ex, ey in xy:
		if ex == ax or ex == bx or ex == cx or ex == dx:
			continue
		elif edge_left <= ex <= edge_right and edge_bottom <= ey <= edge_top:
			cnt += 1
	if K <= cnt+4:
		ans = min((edge_right-edge_left)*(edge_top-edge_bottom), ans)

print(ans)