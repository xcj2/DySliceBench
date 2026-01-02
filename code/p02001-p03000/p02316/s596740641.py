import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from heapq import heappop, heappush, heapify, heappushpop
from itertools import permutations, combinations, product, accumulate
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

N, W = MAP()
vw = [LIST() for _ in range(N)]

dp = [[0]*(W+1) for _ in range(N+1)]

for i in range(N):
	for j in range(W+1):
		if j < vw[i][1]:
			dp[i+1][j] = dp[i][j]
		else:
			dp[i+1][j] = max(dp[i][j], dp[i+1][j-vw[i][1]]+vw[i][0])

print(dp[N][W])

