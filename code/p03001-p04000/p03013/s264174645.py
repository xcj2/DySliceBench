import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, log2
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
a = [INT() for _ in range(M)]
b = [0] * (N+1)  # こわれているところに１たてる
for i in a:
	b[i] = 1

dp = [0]*(N+1)
dp[0] = 1
if b[1] == 1:
	dp[1] = 0
else:
	dp[1] = 1

for i in range(2, N+1):
	if b[i] == 1:  # こわれてる
		dp[i] = 0
	else:
		dp[i] = (dp[i-1] + dp[i-2])%MOD

print(dp[N])

