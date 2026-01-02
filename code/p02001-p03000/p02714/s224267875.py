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
	s = input()
	sumc = []
	sumr = 0
	sumg = 0
	sumb = 0
	for i in range(n):
		if s[i] == "R":
			sumr += 1
		if s[i] == "G":
			sumg += 1
		if s[i] == "B":
			sumb += 1
		sumc.append({
			"R" : sumr,
			"G": sumg,
			"B": sumb
			})
	a = {"R": 0, "G": 1, "B": 2}
	case = 0
	log.print(sumc)
	for i in range(n):
		for j in range(i+1, n-1):
			l = j - i
			if s[i] == s[j]:
				continue
			rgb = list("RGB")
			rgb.pop(rgb.index(s[i]))
			rgb.pop(rgb.index(s[j]))
			case += sumc[n-1][rgb[0]] - sumc[j][rgb[0]]
			if j + l < n and s[j+l] == rgb[0]:
				case -= 1
			log.print(i, j, rgb, case)
	print(case)




	


main()