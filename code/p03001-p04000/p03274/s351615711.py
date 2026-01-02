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

N, K = MAP()
x = LIST()


ans = INF
idx = bisect(x, 0)
for i in range(idx-K, idx+1):
	if 0 <= i <= N-K:
		if i == idx-K:
			ans = min(ans, abs(x[i]))
		elif i == idx:
			ans = min(ans, x[i+K-1])
		else:
			ans = min(ans, 2*abs(x[i])+x[i+K-1], abs(x[i])+2*x[i+K-1])
print(ans)
