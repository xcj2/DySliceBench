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
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7
#import numpy as np
#from decimal import *


N, X, Y = MAP()

graph = [[] for _ in range(N)]

for i in range(N-1):
	graph[i].append(i+1)
	graph[i+1].append(i)

graph[X-1].append(Y-1)
graph[Y-1].append(X-1)

dic = defaultdict(int)
for i in range(N):
	q = deque([i])
	dist = [-1]*N
	dist[i] = 0

	while q:
		n = q.popleft()
		for node in graph[n]:
			if dist[node] == -1:
				dist[node] = dist[n] + 1
				q.append(node)

	for i in range(N):
		dic[dist[i]] += 1

for k in range(1, N):
	print(dic[k]//2)