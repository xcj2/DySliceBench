#!/usr/bin/env python3

import sys
import pprint
import math

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
# s = n(n+1)/2 

def main():
	log = Logger(0)
	n = int(sys.stdin.readline())
	if n == 1:
		print(0)
		exit()
	p = prime_fact(n)
	ans = 0
	if len(p.keys()) == 0:
		print(1)
		exit(0)
	keys = list(p.keys())
	key = keys[0]
	i = 1
	j = 0
	while 1:
		if p[key] < i:
			j += 1
			if len(keys) == j:
				break
			key = keys[j]
			i = 1
			continue
		log.print(p, n, key)
		z = key ** i
		n /= z
		p[key] -= i
		ans += 1
		i += 1
	print(ans)


main()