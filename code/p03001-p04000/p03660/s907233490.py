import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from heapq import heappop, heappush

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

N = INT()
ab = [LIST() for _ in range(N-1)]

def dijkstra(E, start):
   N_d = len(E)
   dist = [INF] * N_d
   dist[start] = 0
   q = [(0, start)]
   while q:
       dist_v, v = heappop(q)
       if dist[v] != dist_v:
           continue
       for u, dist_vu in E[v]:
           dist_u = dist_v + dist_vu
           if dist_u < dist[u]:
               dist[u] = dist_u
               heappush(q, (dist_u, u))
   return dist

E = [[] for _ in range(N)]

for a, b in ab:
	E[a-1].append((b-1, 1))
	E[b-1].append((a-1, 1))

d_f = dijkstra(E, 0)
d_s = dijkstra(E, N-1)

f = 0
s = 0
for i in range(N):
	if d_f[i] <= d_s[i]:
		f += 1
	else:
		s += 1

if f > s:
	print("Fennec")
else:
	print("Snuke")
