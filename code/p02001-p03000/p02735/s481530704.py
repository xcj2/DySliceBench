#!/usr/bin/env python3

import sys

sys.setrecursionlimit(10 ** 6)

class Logger:
	def __init__(self, is_debug):
		self.debug = is_debug
	def print(self, *arg):
		if self.debug:
			print("logger:", *arg)
	def plane(self, lst, sep=" ", space=0):
		if self.debug:
			longest = space
			for i in range(len(lst)):
				for j in range(len(lst[i])):
					longest = max(longest, len(str(lst[i][j])))
			for i in range(len(lst)):
				for j in range(len(lst[i])):
					print("logger:", " "*(longest-len(str(lst[i][j])))+str(lst[i][j]), end=sep)
				print()

def main():
	h, w = map(int, sys.stdin.readline().split())
	s = [list(sys.stdin.readline().rstrip())[::-1] for i in [0]*h][::-1]
	cost = [[0]*w for i in [0]*h]
	for y in range(h):
		for x in range(w):
			if y == 0 and x == 0:
				if s[y][x] == "#":
					cost[y][x] = 1
			elif y == 0:
				if s[y][x] == "#" and s[y][x-1] != "#":
					cost[y][x] = cost[y][x-1] + 1
				else:
					cost[y][x] = cost[y][x-1]
			elif x == 0:
				if s[y][x] == "#" and s[y-1][x] != "#":
					cost[y][x] = cost[y-1][x] + 1
				else:
					cost[y][x] = cost[y-1][x]
			else:
				if s[y][x] == "#" and s[y-1][x] != "#":
					cost[y][x] = cost[y-1][x] + 1
				else:
					cost[y][x] = cost[y-1][x]
				if s[y][x] == "#" and s[y][x-1] != "#":
					cost[y][x] = min(cost[y][x], cost[y][x-1] + 1)
				else:
					cost[y][x] = min(cost[y][x], cost[y][x-1])
	logger = Logger(0)
	logger.print(h, w)
	print(cost[h-1][w-1])

main()