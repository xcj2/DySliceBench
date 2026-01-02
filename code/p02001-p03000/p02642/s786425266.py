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

	A.sort()
	zyuufuku = {}
	for i,val in enumerate(A):
		if i == 0:
			continue
		if val == A[i-1]:
			if val in zyuufuku:
				pass
			else:
				zyuufuku[val] = 1

	refd = [0 for i in range(1000000 + 1)]
	for i,val in enumerate(A):
		if val in zyuufuku:
			if zyuufuku[val] > 2:
				continue
			else:
				zyuufuku[val] += 1
		for j in range(val,1000000 + 1,val):
			refd[j] += 1

	ans = 0
	for i,val in enumerate(A):
		if val in zyuufuku:
			continue
		if refd[val] < 2:
			ans += 1

	print(ans)

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
if __name__ == "__main__":
	main()
