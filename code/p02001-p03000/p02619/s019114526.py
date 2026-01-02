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
	day_length = int(sys.stdin.readline())
	down_happy = list(map(int, sys.stdin.readline().split()))
	daily_happy = [[] for i in range(day_length)]
	contests_kind = 26
	contests = []
	for i in range(day_length):
		si = list(map(int, sys.stdin.readline().split()))
		for j in range(contests_kind):
			daily_happy[i].append(si[j])
	for i in range(day_length):
		contests.append(int(sys.stdin.readline())-1)
	log.print(day_length, down_happy, daily_happy)
	happy = 0
	last_contest_days = [0]*contests_kind
	for day in range(day_length):
		contest = contests[day]
		happy += daily_happy[day][contest]
		last_contest_days[contest] = day + 1
		for i in range(contests_kind):
			happy -= down_happy[i] * (day + 1 - last_contest_days[i])
		print(happy)





main()