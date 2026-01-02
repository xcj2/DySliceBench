import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect_left
from heapq import heappush, heappop

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

N, X = MAP()

a, p = [1]*N, [1]*N
for i in range(N-1):
	a[i+1] = a[i]*2+3
	p[i+1] = p[i]*2+1

def f(N, X):
	if N == 0:
		return 0 if X <= 0 else 1
	elif X <= 1 + a[N-1]:
		return f(N-1, X-1)
	else:
		return p[N-1]+1+f(N-1, X-2-a[N-1])

print(f(N, X))
