import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd, log
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
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7 
#mod = 998244353
from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10

N = INT()
A = [LIST() for _ in range(N)]

match_id = [[0]*N for _ in range(N)]

def toid(i, j):
	i, j = sorted([i, j])
	return match_id[i][j]

cnt = 0
for i in range(N):
	for j in range(N):
		if i < j:
			match_id[i][j] = cnt
			cnt += 1

V = N*(N-1)//2

gout = [[] for _ in range(V)]
deg = [0]*V
for i in range(N):
	for j in range(N-2):
		gout[toid(i, A[i][j]-1)].append(toid(i, A[i][j+1]-1))
		deg[toid(i, A[i][j+1]-1)] += 1

topo = [v for v in range(V) if deg[v] == 0 ]
day = [0]*V
deq = deque(topo)
ans = 0
while deq:
	v = deq.popleft()
	for t in gout[v]:
		deg[t] -= 1
		if deg[t] == 0:
			deq.append(t)
			day[t] = day[v] + 1
			ans = day[t]
if any(deg):
	print(-1)
	exit()
print(ans+1)