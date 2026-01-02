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
	H,W,K = inputMap()
	maps = []
	for i in range(H):
		s = inputStr()
		maps.append(s)

	ans = 0
	for i in range(2**H):
		iBin = bin(i)[2:]
		pl = ""
		for ttt in range(len(iBin), H):
			pl += "0"
		iBin = pl + iBin
		iBin = iBin[::-1]
		for j in range(2**W):
			jBin = bin(j)[2:]
			pl = ""
			for ttt in range(len(jBin), W):
				pl += "0"
			jBin = pl + jBin
			jBin = jBin[::-1]

			kuro = 0
			for iii,mapH in enumerate(maps):
				if iBin[iii] == "1":
					continue
				for jjj,mapW in enumerate(mapH):
					if jBin[jjj] == "1":
						continue
					if mapW == "#":
						kuro += 1
			#print(kuro)
			if kuro == K:
				ans += 1
	print(ans)




#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
if __name__ == "__main__":
	main()
