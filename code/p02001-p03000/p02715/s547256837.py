#!/usr/bin/env python3

import sys
import pprint

sys.setrecursionlimit(10 ** 6)

class Logger:
	def __init__(self, debug):
		self.debug = debug
	def print(self, *args):
		if self.debug:
			pprint.pprint(args)

def is_prime(n):
	for i in range(2, int(-(-n**0.5//1))+1):
		if n % i == 0:
			return False
	return True

def comb(n, r):
	return fact(n) // fact(n-r) // fact(r)

fact_memo = [1, 1]
def fact(n):
	if len(fact_memo) > n:
		return fact_memo[n]
	else:
		for i in range(len(fact_memo), n+1):
			fact_memo.append(fact_memo[i-1] * i)
		return fact_memo[n]


def main():
	log = Logger(1)
	n, k = map(int, sys.stdin.readline().split())
	ans = 0
	mod = 10 ** 9 + 7
	a = [0]*(k+1)
	for i in range(1, k+1):
		a[i-1] = pow(k//i, n, mod)
	ans = 0
	for i in list(range(1, k+1))[::-1]:
		for j in range(1, k//i):
			a[i-1] -= a[i-1 + i * j]
		ans += a[i-1] * i
		ans %= mod
	print(ans)



main()