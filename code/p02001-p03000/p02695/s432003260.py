import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import combinations_with_replacement, accumulate, permutations, combinations, product, groupby
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

N, M, Q = MAP()
graph = [[] for _ in range(N)]
abcd = [LIST() for _ in range(Q)]
ans = 0

for x in combinations_with_replacement(range(1, M+1), N):
	tmp = 0
	for a, b, c, d in abcd:
		a -= 1
		b -= 1
		if x[b]-x[a] == c:
			tmp += d
	ans = max(ans, tmp)
print(ans)
