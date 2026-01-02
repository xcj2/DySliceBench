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

def gcd(a, b):
	# if a == 0:
	# 	return b
	# elif b == 0:
	# 	return a
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    c = a % b
    return gcd(b, c)

Li = [0]*(N+2)
Ri = [0]*(N+2)
A.append(0)
A.insert(0, 0)

for i in range(N+1):
	Li[i+1] = gcd(Li[i], A[i])

for i in range(N, -1, -1):
	Ri[i] = gcd(Ri[i+1], A[i])

# print(Li)
# print(Ri)

M = []
for i in range(1, N+1):
	M.append(gcd(Li[i],Ri[i+1]))
# print(M)
print(max(M))
