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
	n = int(sys.stdin.readline())
	l = list(map(int, sys.stdin.readline().split()))
	cnt = 0
	for i in range(n):
		for j in range(i, n):
			for k in range(j, n):
				if l[i] != l[j] and l[i] != l[k] and l[j] != l[k]:
					a = sorted([l[i], l[j], l[k]])
					log.print(a)
					if (a[0] + a[1] <= a[2]):
						continue
					cnt += 1
	print(cnt)
	


main()