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


N = INT()
S = input()

s1 = []
dic_s2 = defaultdict(int)

for x in product([0, 1], repeat=N):
	s1_red = ""
	s1_blue = ""
	s2_red = ""
	s2_blue = ""
	for i in range(N):
		if x[i]:
			s1_red += S[i]
			s2_red += S[N+i]
		else:
			s1_blue += S[i]
			s2_blue += S[N+i]

	s1.append((s1_red, s1_blue))
	dic_s2[(s2_blue[::-1], s2_red[::-1])] += 1

ans = 0
for x in s1:
	ans += dic_s2[x]

print(ans)
