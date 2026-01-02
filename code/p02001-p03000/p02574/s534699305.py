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

N = INT()
A = LIST()
lim = 10**6+1
g = [[] for _ in range(lim+1)]
g[1].append(1)
for i in range(2, lim+1):
	if g[i] == []:
		for j in range(1, lim//i + 1):
			g[i*j].append(i)

num = [0]*(lim+1)

for a in A:
	if a == 1:
		continue
	for x in g[a]:
		if num[x]:
			break
		num[x] = 1

	else:
		continue
	break
else:
	print("pairwise coprime")
	exit()


#素因数分解
def factorization(n):
	arr = []
	tmp = n
	for i in range(2, int(-(-n**0.5//1))+1):
		if tmp%i == 0:
			cnt = 0
			while tmp%i == 0:
				cnt += 1
				tmp //= i
			arr.append([i, cnt])
	if tmp != 1:
		arr.append([tmp, 1])
	if arr == []:
		arr.append([n, 1])
	return arr
	
dic = defaultdict(int)
for x, y in factorization(A[0]):
	dic[x]=y

for a in A[1:]:
	for x, y in dic.items():
		if a%x:
			dic[x] = 0
		else:
			dic[x] = min(y, a//x)

for x, y in dic.items():
	if x != 1 and y != 0:
		print("not coprime")
		break
else:
	print("setwise coprime")


