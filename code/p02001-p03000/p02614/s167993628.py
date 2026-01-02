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
	h, w, k = map(int, sys.stdin.readline().split())
	c = []
	for i in range(h):
		c.append(list(input()))
	log.print(c)
	ans = 0
	for i in range(2**h):
		gyou = []
		for l in range(h):
			if i >> l & 1:
				gyou.append(l)
		for j in range(2**w):
			retu = []
			for l in range(w):
				if j >> l & 1:
					retu.append(l)
			count = 0
			for l in range(h):
				for m in range(w):
					if l in gyou or m in retu:
						continue
					if c[l][m] == "#":
						count += 1
			if count == k:
				ans += 1
	print(ans)


main()