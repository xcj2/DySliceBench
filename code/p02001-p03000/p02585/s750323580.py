import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush, heappop
from functools import reduce, lru_cache
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
P = LIST()
C = LIST()

loop_point = [0]*N
loop_count = [0]*N
searched = [0]*N

for i in range(N):
	if searched[i]:
		continue
	idx = i
	points = 0
	cnt = 0
	while not searched[P[idx]-1]:
		idx = P[idx]-1
		searched[idx] = 1
		cnt += 1
		points += C[idx]
	loop_count[i] = cnt
	loop_point[i] = points

	while not loop_point[P[idx]-1]:
		idx_next = P[idx]-1
		loop_count[idx_next] = loop_count[idx]
		loop_point[idx_next] = loop_point[idx]
		idx = idx_next

ans = -INF
for i in range(N):
	p = 0
	idx = i
	loop = loop_point[i] > 0 and K > loop_count[i]
	for j in range(1, min(K+1, loop_count[i]+1)):
		idx = P[idx] - 1
		p += C[idx]
		if loop:
			final_p = p + loop_point[i]*((K-j)//loop_count[i])
		else:
			final_p = p
		ans = ans if ans > final_p else final_p
print(ans)