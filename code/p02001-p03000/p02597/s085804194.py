# -*- coding: utf-8 -*-
import sys
import math
from bisect import bisect_left
from bisect import bisect_right
from collections import defaultdict
from heapq import heappop, heappush
import itertools
import random
from collections import deque
from decimal import *
import queue

input = sys.stdin.readline

def inputInt(): return int(input())
def inputMap(): return map(int, input().split())
def inputList(): return list(map(int, input().split()))
def inputStr(): return input()[:-1]

inf = float('inf')
mod = 1000000007

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

def main():
	N = inputInt()
	C = inputStr()

	aida = []
	anzen = 0
	ai = 0
	yokei = 0
	flg = False
	for i,val in enumerate(C):
		ai += 1
		if val == "W":
			if flg == False:
				flg = True
		elif val == "R":
			anzen += 1
			if flg == False:
				aida.append(ai)
			else:
				yokei += 1
				aida.append(ai)

	if yokei == 0:
		print(0)
		sys.exit()

	ans = 0
	for i,val in enumerate(aida):
		if val <= anzen:
			continue
		ans += 1

	print(ans)
	#print(aida)
	#print(yokei)


#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
if __name__ == "__main__":
	main()
