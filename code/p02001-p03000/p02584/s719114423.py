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


def main():
	log = Logger(1)
	x, k, d = map(int, sys.stdin.readline().split())
	x = abs(x)
	if x == 0:
		if k % 2 == 0:
			print(0)
		else:
			print(d)
		exit()

	if x % d == 0:
		if x // d >= k:
			print(abs(x - d * k))
		else:
			if (k - x // d) % 2 == 0:
				print(0)
			else:
				print(d)
	else:
		if x // d >= k:
			print(abs(x - d * k))
		else:
			if x >= d:
				if x % d < abs(x % d - d):
					if (k - (x // d)) % 2 == 0:
						print(x % d)
					else:
						print(abs(x % d - d))
				else:
					if (k - (x // d + 1)) % 2 == 0:
						print(abs(x % d - d))
					else:
						print(x % d)
			else:
				if k % 2 == 0:
					print(x)
				else:
					if abs(x - d) < x + d:
						print(abs(x - d))
					else:
						print(x + d)




main()