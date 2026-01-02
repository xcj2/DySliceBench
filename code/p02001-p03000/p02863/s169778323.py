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
INF = 10**6#float('inf')
mod = 10 ** 9 + 7 
#mod = 998244353
#from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10

N, T = MAP()
AB = [LIST() for _ in range(N)]
AB.sort(key = lambda x:x[0])
t = [0]*T
ans = 0

for A, B in AB:
	for i in range(T-1, 0, -1):
		if t[i]:
			if T <= i+A:
				ans = max(ans, t[i]+B)
			else:
				t[i+A] = max(t[i+A], t[i]+B)
	if T <= A:
		ans = max(ans, B)
	else:
		t[A] = max(t[A], B)

ans = max(ans, max(t))
print(ans)