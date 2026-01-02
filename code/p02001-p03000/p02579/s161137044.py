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
	h, w = map(int, sys.stdin.readline().split())
	ch, cw = map(int, sys.stdin.readline().split())
	dh, dw = map(int, sys.stdin.readline().split())
	s = [sys.stdin.readline().rstrip() for i in [0]*h]
	graph = [[[] for i in [0]*w] for j in [0]*h]
	
	def getMaze(x, y):
		if not (0 <= x < w and 0 <= y < h):
			return -1
		return s[y][x]

	for y in range(h):
		for x in range(w):
			if s[y][x] == "#":
				continue
			


	# log.print(graph)
	stack = deque([(cw-1, ch-1)])
	dist = [[float("inf")]*w for i in range(h)]
	while len(stack) != 0:
		x, y = stack.popleft()
		log.print(x, y, dist[y][x])
		if dist[y][x] == float("inf"):
			dist[y][x] = 0
		d = dist[y][x]
		nexts = []
		for i in range(-2, 2+1):
			for j in range(-2, 2+1):
				if (i, j) == (0, 0):
					continue
				if getMaze(x + i, y + j) == ".":
					if (i, j) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
						nexts.append((x + i, y + j, 0))
					else:
						nexts.append((x + i, y + j, 1))
		for next in nexts:
			nx, ny, cost = next
			if dist[ny][nx] > d + cost:
				dist[ny][nx] = d + cost
				if cost == 1:
					stack.append((nx, ny))
				else:
					stack.appendleft((nx, ny))
	log.print(dist)
	if dist[dh-1][dw-1] == float("inf"):
		print(-1)
	else:
		print(dist[dh-1][dw-1])
	
	


main()