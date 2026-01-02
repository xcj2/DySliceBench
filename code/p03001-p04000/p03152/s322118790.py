
import sys
from collections import deque, defaultdict
import copy
import bisect
sys.setrecursionlimit(10 ** 9)
import math
import heapq
from itertools import product, permutations,combinations
import fractions

import sys
def input():
	return sys.stdin.readline().strip()

N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

mod = 10**9 + 7

F = [1]
for i in range(N*M):
	F.append((F[-1]*(i + 1))%mod)



def pow(x, y, mod=1000000007):
	pow_list = [x]
	i = 1
	while 2**i <= y:
		a = pow_list[-1]**2
		if mod != 0:
			a = a % mod
		pow_list.append(a)
		i += 1
	ans = 1
	for bit in range(len(pow_list)):
		if (2**bit) & y != 0:
			ans *= pow_list[bit]
			if mod != 0:
				ans = ans % mod
	return ans

def fact(n, mod=1000000007):

	return F[n]

def mod_rev(x, mod):
	"""
	関数powが必要
	"""
	return pow(x, mod - 2, mod)


def comb(a, b, mod=1000000007):
	"""
	関数mod_rev, fact, powが必要
	"""
	if a < b or b < 0:
		return 0
	a_fact = fact(a, mod)
	a_b_fact = fact(a - b, mod)
	if mod != 0:
		return (a_fact * mod_rev(a_b_fact, mod))%mod
	else:
		return a_fact//a_b_fact



A.sort()
B.sort()

i = 0
j = 0
max_list = deque([])
ans = 1
mod = 10**9 + 7

if A[-1] != B[-1]:
	print(0)
	exit()

while True:
	if i > 0 and j > 0:
		if A[-i] == A[-i+1] or B[-j] == B[-j+1]:
			print(0)
			exit()
	if j != M and (i == N or A[-(i + 1)] < B[-(j + 1)]):
		ans *= i
		ans %= mod
		max_list.appendleft((B[-(j + 1)], i - 1))
		j += 1
	elif i != N and (j == M or A[-(i + 1)] > B[-(j + 1)]):
		ans *= j
		ans %= mod
		max_list.appendleft((A[-(i + 1)], j - 1))
		i += 1
	elif A[-(i + 1)] == B[-(j + 1)]:
		if i + j != 0:
			max_list.appendleft((A[-(i + 1)], i + j))
		i += 1
		j += 1
	if i == N and j == M:
		break

num = 0
#print(max_list,ans)
for i in range(len(max_list)):
	ans *= comb(max_list[i][0] - i - 1 - num, max_list[i][1])
	ans %= mod
	num += max_list[i][1]

print(ans)