import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd, floor
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

N, K = MAP()
A = LIST()

cnt = 0
while 1:
	a = [0]*(N+1)
	flg = 1
	for i in range(N):
		a[max(0, i-A[i])] += 1
		a[min(N, i+A[i]+1)] -= 1
		if max(0, i-A[i]) == 0 and min(N, i+A[i]+1) == N:
			flg *= 1
		else:
			flg *= 0
	A = list(accumulate(a))
	cnt += 1
	if cnt == K:
		print(*A[:-1])
		exit()
	if flg:
		break

A = [N]*N
print(*A)
