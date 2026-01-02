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

N, M = MAP()
LRD = [LIST() for _ in range(M)]

graph = [[] for _ in range(N)]
for L, R, D in LRD:
	graph[L-1].append((R-1, D))
	graph[R-1].append((L-1, -D))

check = [1]*N
i = 0
while i < N:
	while check[i] == 0:
		i += 1
		if i == N:
			print("Yes")
			exit()

	check[i] = 0
	dis = defaultdict(int)
	dis[i] = 0
	q = deque([i])
	while q:
		p = q.popleft()
		for v, dist in graph[p]:
			if check[v] == 1:
				check[v] = 0
				dis[v] = dis[p] + dist
				q.append(v)
			if check[v] == 0 and dis[v] != dis[p] + dist:
				print("No")
				exit()
