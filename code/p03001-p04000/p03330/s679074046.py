import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush, heappop
from functools import reduce, lru_cache
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7 
#mod = 998244353
from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10

N, C = MAP()
D = [LIST() for _ in range(C)]
c = [LIST() for _ in range(N)]

c_kind = [[0]*(C+1) for _ in range(3)]

cost = [[0]*(C+1) for _ in range(3)]


for i in range(N):
	for j in range(N):
		c_kind[(i+j+2)%3][c[i][j]] = 1


for color in range(1, C+1):
	for i in range(N):
		for j in range(N):
			cost[(i+j+2)%3][color] += D[c[i][j]-1][color-1]

ans = INF
for a, b, c in permutations(range(1, C+1), 3):
	ans = min(ans, cost[0][a]+cost[1][b]+cost[2][c])

print(ans)
