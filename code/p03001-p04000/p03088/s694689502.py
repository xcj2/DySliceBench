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

dp = [{} for i in range(N+1)]

def swap_ok(last4):
	# print(last4)
	for i in range(4):
		t = list(last4)
		if i >= 1:
			t[i-1], t[i] = t[i], t[i-1]
		if ''.join(t).count("AGC") >= 1:
			return False
	return True

def dfs(current, last3):
	if last3 in dp[current]:
		return dp[current][last3]
	if current == N:
		return 1
	ret = 0
	for c in 'AGCT':
		if swap_ok(last3 + c):
			ret = (ret + dfs(current + 1, last3[1:] + c)) % MOD
	dp[current][last3] = ret
	return ret

print(dfs(0, 'ATC'))
