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
	N,M,K = inputMap()
	A = inputList()
	B = inputList()

	sumA = []
	for i,val in enumerate(A):
		if i == 0:
			sumA.append(val)
		else:
			sumA.append(val + sumA[i-1])

	sumB = []
	for i,val in enumerate(B):
		if i == 0:
			sumB.append(val)
		else:
			sumB.append(val + sumB[i-1])

	ans = 0
	for i,val in enumerate(sumA):
		if val > K:
			break
		amari = K - val
		indexs = bisect_right(sumB, amari)
		tmp = (i+1) + indexs
		#print(tmp)
		if ans < tmp:
			ans = tmp

	for i,val in enumerate(sumB):
		if val > K:
			break
		amari = K - val
		indexs = bisect_right(sumA, amari)
		tmp = (i+1) + indexs
		#print(tmp)
		if ans < tmp:
			ans = tmp

	print(ans)

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
if __name__ == "__main__":
	main()
