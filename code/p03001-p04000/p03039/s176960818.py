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

N, M, K = MAP()

def C(n, r):
	return (((factorial[n] * power(factorial[r], MOD-2) % MOD) * power(factorial[n-r], MOD-2)) % MOD)

def power(x, y):
	if y == 0:
		return 1
	elif y == 1:
		return x % MOD
	elif y % 2 == 0:
		return power(x, int(y/2)) ** 2 % MOD
	else:
		return power(x, int((y-1)/2)) ** 2 * x % MOD

factorial = [1]
for n in range(1, 2*10**5+1):
    factorial.append(factorial[n-1]*n%MOD)

pat = C(N*M-2, K-2)

X = 0
for d in range(1, M):
	X = (X + (d*(M-d)*(N*N)))%MOD

Y = 0
for d in range(1, N):
	Y = (Y + (d*(N-d)*(M*M)))%MOD

print(pat*(X+Y)%MOD)
