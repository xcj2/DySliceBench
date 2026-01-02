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

former = S[:N]
latter = S[N:][::-1]

dic_f = defaultdict(int)
dic_l = defaultdict(int)

for x in product([0, 1], repeat=N):
	tmp_red = ""
	tmp_blue = ""
	for i in range(N):
		if x[i]:
			tmp_red += former[i]
		else:
			tmp_blue += former[i]
	dic_f["{},{}".format(tmp_red, tmp_blue)] += 1

for x in product([0, 1], repeat=N):
	tmp_red = ""
	tmp_blue = ""
	for i in range(N):
		if x[i]:
			tmp_red += latter[i]
		else:
			tmp_blue += latter[i]
	dic_l["{},{}".format(tmp_red, tmp_blue)] += 1

ans = 0

for key in dic_f:
	ans += dic_f[key] * dic_l[key]

print(ans)


