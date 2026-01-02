import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
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

N = INT()
A = LIST()

A.insert(0, 0)
A.append(0)

ans = 0
for i in range(N+1):
	ans += abs(A[i+1]-A[i])

for i in range(N):
	if A[i]<=A[i+1]<=A[i+2] or A[i+2]<=A[i+1]<=A[i]:  # 消すところが真ん中
		print(ans) 
	else:
		print(ans-2*
			min(
				abs(A[i+2]-A[i+1]), 
				abs(A[i+1]-A[i])
				)
			)
