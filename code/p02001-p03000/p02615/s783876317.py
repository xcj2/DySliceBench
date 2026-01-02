#!/usr/bin/env python3

import sys
import pprint
from collections import deque


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
	a = deque(sorted(a))
	if len(a) == 2:
		print(max(a))
		exit()
	if len(a) == 3:
		print(a[-1] + a[-2])
		exit()
	ans = 0
	a1 = a.pop()
	a2 = a.pop()
	a3 = a.pop()
	que = deque([[a1, a2], [a2, a3], [a3, a1]])
	ans += a1 + a2
	while len(a) != 0:
		log.print(que, ans)
		between = que.popleft()
		insert = a.pop()
		ans += min(between)
		que.append([between[0], insert])
		que.append([insert, between[1]])
	print(ans)




main()