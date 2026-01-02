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
	s = []
	a = {}
	for i in range(n):
		s.append(input())
	for i in range(n):
		a[s[i]] = a.get(s[i], 0) + 1
	log.print(a)
	print("AC x {}".format(a.get("AC", 0)))
	print("WA x {}".format(a.get("WA", 0)))
	print("TLE x {}".format(a.get("TLE", 0)))
	print("RE x {}".format(a.get("RE", 0)))

	


main()