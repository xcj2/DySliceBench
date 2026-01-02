import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
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

N = INT()
h = LIST()

dp = [INF]*N
dp[0] = 0
for i in range(N):
	if i < N-1:
		dp[i+1] = min(dp[i+1], dp[i]+abs(h[i+1]-h[i]))
	if i < N-2:
		dp[i+2] = min(dp[i+2], dp[i]+abs(h[i+2]-h[i]))
# print(dp)
print(dp[-1])