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
	a = []
	b = []
	for i in range(n):
		ai, bi = map(int, sys.stdin.readline().split())
		a.append(ai)
		b.append(bi)
	a_sort = sorted(a)
	if n % 2 == 0:
		min_center = (a_sort[int(n/2)-1] + a_sort[int(n/2)])/2
	else:
		min_center = a_sort[int((n+1)/2)-1]
	b_sort = sorted(b)
	if n % 2 == 0:
		max_center = (b_sort[int(n/2)-1] + b_sort[int(n/2)])/2
	else:
		max_center = b_sort[int((n+1)/2)-1]
	log.print(max_center, min_center)
	if n % 2 == 0:
		print(int((max_center - min_center)*2 + 1))
	else:
		print(int(max_center - min_center + 1))


	
	


main()