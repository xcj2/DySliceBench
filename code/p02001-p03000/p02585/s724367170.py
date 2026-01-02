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

check = [0]*N 
score = []

i = 0
while 1:
	while i < N and check[i]:
		i += 1
	if i == N:
		break

	tmp = []
	while check[i] == 0:
		check[i] = 1
		i = P[i]-1
		tmp.append(C[i])
	score.append(tmp)

ans = -INF
for x in score:
	x_acc = list(accumulate([0] + x + x))
	n = len(x)
	tmp_max = -INF

	cnt = 0
	p, q = 0, 0
	for i, j in combinations(range(2*n+1), 2):
		if j-i <= min(K, n):
			if tmp_max < x_acc[j]-x_acc[i]:
				tmp_max = x_acc[j]-x_acc[i]
				cnt = j-i
				p, q = i, j


	tmp_ans = -INF
	lis = x[(q-1)%n+1:]+x[:(q-1)%n+1]

	if 0 >= x_acc[n]:
		tmp_ans = tmp_max

	else:
		if cnt <= K%n:
			tmp_ans = x_acc[n]*(K//n) + tmp_max
		else:
			tmp_max2 = 0
			for i, j in combinations(range(2*n+1), 2):
				if j-i <= K%n:
					if tmp_max2 < x_acc[j]-x_acc[i]:
						tmp_max2 = x_acc[j]-x_acc[i]
			tmp_ans = max(x_acc[n]*(K//n-1)+tmp_max, x_acc[n]*(K//n) + tmp_max2)

	ans = max(ans, tmp_ans)

print(ans)
