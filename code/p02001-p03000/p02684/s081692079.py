import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import accumulate, permutations, combinations, product, groupby, combinations_with_replacement
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, K = MAP()
A = LIST()
A = [x-1 for x in A]
D = 60
to = [[0]*N for _ in range(D)]
to[0] = A.copy()

for i in range(D-1):
	for j in range(N):
		to[i+1][j] = to[i][to[i][j]]

v = 0
for i in range(D-1, -1, -1):
	l = 1<<i
	if l <= K:
		v = to[i][v]
		K -= l
print(v+1)
