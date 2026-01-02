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
	n, k = map(int, sys.stdin.readline().split())
	a = list(map(int, sys.stdin.readline().split()))
	here = 1
	patarrn = []
	dist = [0]*n
	while 1:
		here = a[here-1]
		if dist[here-1]:
			break
		dist[here-1] = 1
		patarrn.append(here-1)
	log.print(here, patarrn)
	b = patarrn.index(here-1)
	if k <= len(patarrn):
		print(patarrn[k-1]+1)
		exit()
	patarrn = patarrn[b:]
	log.print(patarrn, b, patarrn[(k-b) % len(patarrn) - 1])
	print(patarrn[(k-b) % len(patarrn) - 1]+1)


main()