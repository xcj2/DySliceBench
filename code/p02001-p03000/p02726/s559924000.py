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

def dijkstra(E, start): #最短経路のみ
	N_d = len(E)
	dist = [INF] * N_d
	dist[start] = 0
	q = [(0, start)]
	while q:
		dist_v, v = heappop(q)
		if dist[v] != dist_v:
			continue
		for u, dist_vu in E[v]:
			dist_u  = dist_v + dist_vu
			if dist[u] > dist_u:
				dist[u] = dist_u
				heappush(q, (dist_u, u))
	return dist	

N, X, Y = MAP()

graph = [[[1, 1]]] + [[[i-1, 1], [i+1, 1]] for i in range(1, N-1)] + [[[N-2, 1]]]
graph[X-1].append([Y-1, 1])
graph[Y-1].append([X-1, 1]) 

dic = defaultdict(int)

ans = 0
for i in range(N):
	ans = dijkstra(graph, i)
	for key in ans:
		dic[key] += 1

for i in range(1, N):
	print(dic[i]//2)
