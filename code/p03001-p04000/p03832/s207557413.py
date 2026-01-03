
import sys
from collections import deque, defaultdict
import copy
import bisect
#sys.setrecursionlimit(10 ** 9)
import math
import heapq
from itertools import product, permutations,combinations
import fractions

import sys
def input():
	return sys.stdin.readline().strip()


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

def fact(n, mod=100000007):
	ans = 1
	for i in range(n):
		ans *= i + 1
		if mod != 0 and ans >= mod:
			ans = ans % mod
	return ans

def mod_rev(x, mod):
	"""
	関数powが必要
	"""
	return pow(x, mod - 2, mod)

N, A, B, C, D = list(map(int, input().split()))
mod = 1000000007

mod_sho = [0]
for i in range(N):
	mod_sho.append(mod_rev(i + 1, mod))

comb = [[0]*(N + 1) for _ in range(N + 1)]
comb[0][0] = 1
for n in range(1, N + 1):
	comb[n][0] = 1
	comb[n][n] = 1
	for i in range(1, n):
		comb[n][i] = comb[n - 1][i - 1] + comb[n - 1][i]
		comb[n][i] = comb[n][i] % mod
plus_list = []
for i in range(A, B + 1):
	G = []
	for j in range(C, D + 1):
		if i*j > N:
			break
		else:
			G.append(i*j)
	if len(G) > 0:
		plus_list.append(G)

sum = [0]*(N + 1)
sum[0] = 1

if len(plus_list) == 0:
	print(0)
	exit()
num = A - 1
for number in plus_list:
	#print(number)
	num += 1
	sum_next = [0] * (N + 1)
	for n in range(0, N + 1):
		if sum[n] == 0:
			continue
		sum_next[n] += sum[n]
		sum_next[n] = sum_next[n] % mod
		times = 1
		rest = N - n
		seki = 1
		for x in range(1, D + 1):

			if n + x*num <= N:
				seki *= comb[rest][num]
				seki = seki*mod_sho[times]
				seki = seki % mod
				if x >= C:
					sum_next[n + x*num] += (sum[n]*seki) % mod
					sum_next[n + x*num] = sum_next[n + x*num] % mod
					#print(sum_next, sum, seki)
				times += 1
				rest -= num
			else:
				break
	sum = copy.deepcopy(sum_next)


print(sum[N])
