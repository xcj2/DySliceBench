import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd, log2
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
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

a = [1]
r = -1
loc = 1
b = [0]*(N+1)
b[1] = 1


for i in range(N):
	loc = A[loc-1]
	#print(loc)
	if b[loc] == 0:
		a.append(loc)
		b[loc] = 1
		#print(a)
	else:
		r = i+1
		loop_start = loc
		break

#print(a)
#print(r)
#print(loop_start)

for i in range(N):
	if a[i] == loop_start:
		l = i
		break

first = a[:l]
loop = a[l:]

#print(l, r)
#print(first)
#print(loop)


K += 1

if K <= len(first):
	print(a[K-1])
else:
	K -= len(first)
	K %= len(loop)
	print(loop[K-1])
