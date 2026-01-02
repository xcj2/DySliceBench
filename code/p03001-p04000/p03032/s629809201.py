import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, log2
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

N, K = MAP()
V = LIST()
R = min(N, K)

max_ = 0
for A in range(R+1):
	for B in range(R+1):
		if A+B > R:
			continue
		if B == 0:
			lis = V[:A]
		else:
			lis = V[:A] +  V[-B:]
		# print(A, B)
		# print(lis)
		lis.sort()
		for i in range(K-(A+B)):
			if lis and lis[0] < 0:
				lis.pop(0)
		tmp = sum(lis)
		max_ = max(max_, tmp)
print(max_)
