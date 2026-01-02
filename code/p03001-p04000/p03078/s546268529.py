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

X, Y, Z, K = MAP()
A = sorted(LIST(), reverse = True)
B = sorted(LIST(), reverse = True)
C = sorted(LIST(), reverse = True)

AB = []
for i in range(X):
	for j in range(Y):
		AB.append(A[i]+B[j])

AB.sort(reverse = True)
AB = AB[:3000]
ABC = sorted([C[0]+AB[i] for i in range(min(3000, X*Y))], reverse = True)

for j in range(1, Z):
	ABC_tmp = sorted([C[j]+AB[i] for i in range(min(3000, X*Y))])
	ABC += ABC_tmp
	ABC.sort(reverse = True)
	ABC = ABC[:3000]

print(*ABC[:K], sep= "\n")

