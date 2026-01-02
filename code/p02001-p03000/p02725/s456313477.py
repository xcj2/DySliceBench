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
	log = Logger(0)
	k, n = map(int, sys.stdin.readline().split())
	a = list(map(int, sys.stdin.readline().split()))
	mind = 10**9
	for i in range(n):
		if i == 0:
			mind = min(mind, k - abs(a[i] - a[i+1]), k - abs(a[i] + k - a[-1]))
			continue
		if i == n - 1:
			mind = min(mind, k - abs(k - a[i] + a[0]), k - abs(a[i] - a[i-1]))
			continue
		mind = min(mind, k - abs(a[i] - a[i+1]), k - abs(a[i] - a[i-1]))
	print(mind)


main()