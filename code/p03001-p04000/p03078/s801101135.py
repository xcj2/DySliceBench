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

X, Y, Z, K = MAP()
A = LIST()
B = LIST()
C = LIST()

A=sorted(A)[::-1]
B=sorted(B)[::-1]
C=sorted(C)[::-1]
ans = []
for i in range(len(A)):
	for j in range(len(B)):
		for k in range(len(C)):
			if (i+1)*(j+1)*(k+1) <= K:
				ans.append(A[i]+B[j]+C[k])
			else:
				break
for i in sorted(ans)[::-1][0:K]:
	print(i)