import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
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
#import numpy as np
#from decimal import *

N = INT()
a = LIST()

if max(a) == 0:
	print(*[0]*N)
	exit()

n = ceil(log2(max(a)))+1

A = ["{:b}".format(x).zfill(n) for x in a]


b = a[0]
for i in range(1, N):
	b ^= a[i]
b = "{:b}".format(b).zfill(n)


ans = []

for x in A:
	tmp = 0
	for i in range(n):
		tmp += ((int(b[i])+int(x[i]))%2) * (2**(n-1-i))

	ans.append(tmp)

print(*ans)