import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
	N, M = MAP()
	dp = [INF]*(1<<N)
	dp[0] = 0

	for _ in range(M):
		a, b = MAP()
		c = LIST()
		d = 0
		for x in c:
			d += 1<<(x-1)

		for j in range(1<<N):
			tmp = j|d
			dp[tmp] = min(dp[tmp], dp[j]+a)

	if dp[-1] == INF:
		print(-1)
	else:
		print(dp[-1])

if __name__ == "__main__":
	main()
