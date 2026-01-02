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

def prime_fact(n):
	p = {}
	for i in range(2, int(-(-n**0.5//1))+1):
		if n % i == 0:
			while n % i == 0:
				n //= i
				p[i] = p.get(i, 0) + 1
	if n != 1:
		p[n] = p.get(n, 0) + 1
	return p

fact_memo = [1, 1]
def fact(n):
	if len(fact_memo) > n:
		return fact_memo[n]
	else:
		for i in range(len(fact_memo), n+1):
			fact_memo.append(fact_memo[i-1] * i)
		return fact_memo[n]  

def miniComb(n, r):
	a = 1
	for i in range(r):
		a *= n - i
	return a // fact(r)


def main():
	log = Logger(1)
	n, m = map(int, sys.stdin.readline().split())
	p = prime_fact(m)
	ans = 1
	for i in p:
		ans *= miniComb(n + p[i] - 1, p[i])
		ans %= 10 ** 9 + 7
	print(ans)


main()