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
	a = list(map(int, sys.stdin.readline().split()))
	# a_ext = {}
	b_sum_ext = {}
	b_ext = []
	# ai + aj = (j+1) - (i+1)
	# ai + i + 1 = -aj + j + 1

	for i, ai in enumerate(a):
		# a_ext[a[i] + i + 1] = 1
		log.print(a[i]+i+1, -a[i]+i+1)
		b_sum_ext[-a[i]+i+1] = b_sum_ext.get(-a[i]+i+1, 0)+1
	cnt = 0
	log.print(cnt)
	cnt = 0
	for i, ai in enumerate(a):
		b_sum_ext[-a[i]+i+1] = b_sum_ext.get(-a[i]+i+1, 0)-1
		if b_sum_ext.get(a[i] + i + 1, 0) != 0:
			log.print(i+1, a[i] + i + 1)
			cnt += b_sum_ext.get(a[i] + i + 1, 0)
	print(cnt)

	


main()