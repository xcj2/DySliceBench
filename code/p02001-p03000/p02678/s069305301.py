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
	n, m = map(int, sys.stdin.readline().split())
	graph = [[] for i in range(n)]
	for i in range(m):
		ai, bi = map(int, sys.stdin.readline().split())
		graph[ai-1].append(bi-1)
		graph[bi-1].append(ai-1)
	stack = deque([0])
	dist = [-1]*len(graph)
	ans = [-1]*n
	log.print(graph)
	while len(stack) != 0:
		v = stack.popleft()
		d = dist[v]
		nexts = graph[v]
		for next in nexts:
			if dist[next] != -1:
				continue
			dist[next] = d + 1
			ans[next] = v
			stack.append(next)
	if -1 in ans:
		print("No")
	else:
		print("Yes")
		for i in range(1, n):
			print(ans[i]+1)

	


main()