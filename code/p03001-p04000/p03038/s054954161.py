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

N, M = MAP()
A = LIST()
BC = [LIST() for _ in range(M)]
A.sort(reverse=True)
BC.sort(key=lambda x:-x[1])
# print(A)
# print(BC)
count = 0
ans = 0
while count < N:
	if BC and A[0] < BC[0][1]:  # BCからとる
		if BC[0][0] + count > N:
			ans += BC[0][1] * (N-count)
			count = N
		else:
			count += BC[0][0]
			ans += BC[0][1] * BC[0][0]
		# print(count, ans)
		BC.pop(0)
	else:
		count += 1
		ans += A.pop(0)
		# print(count, ans)
print(ans)
