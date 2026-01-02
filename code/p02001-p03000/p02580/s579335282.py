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

H, W, M = MAP()
hw = [LIST() for _ in range(M)]

cnt_h = [0]*(H+1)
cnt_w = [0]*(W+1)

for h, w in hw:
	cnt_h[h] += 1
	cnt_w[w] += 1

h_max = max(cnt_h)
y = [0]*(H+1)
c_y = 0
for i in range(H+1):
	if cnt_h[i] == h_max:
		y[i] += 1


w_max = max(cnt_w)
x = [0]*(W+1)
for i in range(W+1):
	if cnt_w[i] == w_max:
		x[i] += 1

c = 0
for h, w in hw:
	if y[h] == 1 and x[w] == 1:
		c += 1

if c == sum(x)*sum(y):
	print(w_max+h_max-1)
else:
	print(w_max+h_max)



