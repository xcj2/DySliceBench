# -*- coding: utf-8 -*-
import sys
import math
from bisect import bisect_left
from bisect import bisect_right
from collections import defaultdict
from heapq import heappop, heappush
import itertools
import random
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
	D = inputInt()
	C = inputList()
	S = []
	ans = []
	for i in range(D):
		s = inputList()
		S.append(s)

	for i,val in enumerate(S):
		tmp = max(val)
		for j,vol in enumerate(val):
			if tmp == vol:
				ans.append(j+1)
				break

	for i in range(D):
		print(ans[i])

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
if __name__ == "__main__":
	main()
