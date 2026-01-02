# -*- coding: utf-8 -*-
import sys
import math
from bisect import bisect_left
from bisect import bisect_right
from collections import defaultdict
from heapq import heappop, heappush
import itertools
from decimal import *

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
	A = inputList()
	Q = inputInt()

	kanninngu = {}
	goukei = sum(A)
	for i,val in enumerate(A):
		if val in kanninngu:
			kanninngu[val] += 1
		else:
			kanninngu[val] = 1

	for i in range(Q):
		B,C = inputMap()

		if B in kanninngu:
			pass
		else:
			print(goukei)
			continue
			
		tmp = kanninngu[B]
		tmp_sum = B * tmp

		moto = 0
		if C in kanninngu:
			moto = kanninngu[C]

		kanninngu[B] = 0
		kanninngu[C] = tmp + moto
		c_sum = C * tmp

		goukei = goukei + (c_sum - tmp_sum)
		print(goukei)



#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
if __name__ == "__main__":
	main()
