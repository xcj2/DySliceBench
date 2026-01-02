#!/usr/bin/env pypy3

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
	n, x, y = map(int, sys.stdin.readline().split())
	x -= 1
	y -= 1
	ans = [0]*(n-1)
	for i in range(n):
		for j in range(i+1, n):
			if i == j:
				continue
			if (i <= x and j <= x) or (y <= i and y <= j):
				ans[abs(i-j)-1] += 1
			elif (i <= x and y <= j):
				ans[x-i + j-y + 1 - 1] += 1
			elif (x < i < y and x < j < y):
				ans[min(abs(i-j), i-x + 1 + y-j)-1] += 1
			elif (i <= x and x < j < y):
				ans[min(abs(i-j), x-i + 1 + y-j)-1] += 1
			elif (x < i < y and y <= j):
				ans[min(abs(i-j), j-y + 1 + i-x)-1] += 1
	for i in range(len(ans)):
		print(ans[i])







main()