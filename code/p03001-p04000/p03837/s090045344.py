import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from heapq import heappop, heappush, heapify, heappushpop
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

N, M = MAP()
abc = [LIST() for _ in range(M)]
# ワーシャルフロイド法
def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

d = [[INF for i in range(N)] for i in range(N)] 
#d[u][v] : 辺uvのコスト(存在しないときはinf)
for x, y, z in abc:
    d[x-1][y-1] = z
    d[y-1][x-1] = z
for i in range(N):
    d[i][i] = 0 #自身のところに行くコストは０
warshall_floyd(d)
count = 0
for a, b, c in abc:
	for i in range(N):
		if d[i][a-1] + c == d[a-1][b-1]:
			break
	else:
		count += 1
print(count)