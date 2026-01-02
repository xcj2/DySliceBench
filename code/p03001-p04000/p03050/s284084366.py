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
ans = 0

# cnt = 0
# for i in range(1, N+1):
# 	if N%i == N//i:
# 		# print(i)
# 		cnt += i
	# print(i, "N%i=", N%i, "N//i=", N//i)

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

yaku = make_divisors(N)
if int(N**(1/2))*(int(N**(1/2))+1) == N:
	for i, num in enumerate(sorted(yaku)):
		if i == len(yaku)//2-1:
			break
		ans += N//num-1
	print(ans)
else:
	for i, num in enumerate(sorted(yaku)):
		if i == len(yaku)//2:
			break
		ans += N//num-1
	print(ans)