
#!/usr/bin/env python3

import sys
import pprint
import itertools

sys.setrecursionlimit(10 ** 6)

class Logger:
	def __init__(self, debug):
		self.debug = debug
	def print(self, *args):
		if self.debug:
			pprint.pprint(args)


def main():
	log = Logger(0)
	n, m, x = map(int, sys.stdin.readline().split())
	c = []
	a = []
	for i in range(n):
		ci, *ai = map(int, sys.stdin.readline().split())
		c.append(ci)
		a.append(ai)
	ans = 10**9
	log.print(a)
	for i in range(2**n):
		cost = 0
		rikai = [0]*m
		case = []
		for j in range(n):
			case.append(i>>j & 1)
		for j in range(n):
			if not case[j]:
				continue
			cost += c[j]
			for k in range(m):
				rikai[k] += a[j][k]
		# log.print(case, rikai, len(list(filter(lambda z:z>=x, rikai))))
		if len(list(filter(lambda z:z>=x, rikai))) == m:
			ans = min(cost, ans)
	if ans == 10**9:
		print(-1)
		exit()
	print(ans)





main()