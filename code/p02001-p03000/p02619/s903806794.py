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

	for i in range(D):
		tmp = inputInt()
		ans.append(tmp)

	scezhu = [inf for i in range(26)]
	sco = 0
	for i,val in enumerate(ans):
		tmp = S[i][val-1]
		scezhu[val-1] = i
		mins = 0
		for j,vol in enumerate(C):
			if scezhu[j] == inf:
				mins = mins + (vol * (i+1))
				#if i == 1:
					#print(vol * (i+1))
			else:
				mins = mins + (vol * ((i+1)-(scezhu[j]+1)))
				#if i == 1:
					#print(scezhu[i]+1)
		#print(mins)
		tmp -= mins
		sco += tmp
		print(sco)

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
if __name__ == "__main__":
	main()
