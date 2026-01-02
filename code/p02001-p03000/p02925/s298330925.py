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

match = defaultdict(int)
cnt = 0
for i, j in combinations(range(N), 2):
	match[(i, j)] = cnt
	match[(j, i)] = cnt
	cnt += 1

V = N*(N-1)//2
graph = [[] for _ in range(V)]
dag = [0]*V
for i in range(N):
	for j in range(N-2):
		graph[match[(i, A[i][j]-1)]].append(match[(i, A[i][j+1]-1)])
		dag[match[(i, A[i][j+1]-1)]] += 1

q = deque([i for i in range(V) if dag[i]==0])
day = [1]*V
ans = 1

while q:
	p = q.popleft()
	for v in graph[p]:
		dag[v] -= 1
		if dag[v] == 0:
			day[v] = day[p]+1
			ans = day[v]
			q.append(v)


if any(dag):
	print(-1)
else:
	print(ans)


