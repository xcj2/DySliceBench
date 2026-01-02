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

n = INT()
slp = [LIST() for _ in range(n)]
m = INT()
w = [INT() for _ in range(m)]

dp = [0]*394

v = [0]*394
for s, l, p in slp:
	for x in range(s, l+1):
		v[x] = max(v[x], p)


for i in range(394):
	for j in range(i+1):
		dp[i] = max(dp[i], dp[i-j]+v[j])

ans = []
for i in w:
	if dp[i] == 0:
		print(-1)
		break
	else:
		ans.append(dp[i])
else:
	print(*ans, sep="\n")

