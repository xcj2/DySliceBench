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
	A = inputList()

	katamuki = []
	for i,val in enumerate(A):
		if i == 0:
			continue
		if val < A[i-1]:
			katamuki.append("down")
		elif val > A[i-1]:
			katamuki.append("up")
		else:
			katamuki.append("to")

	ans = 1000
	for i,val in enumerate(A):
		if i == len(A)-1:
			break
		if val <= ans:
			if katamuki[i] == "up":
				tmp = ans // val
				ans = ans - (val * tmp)
				ans = ans + (tmp * A[i+1])

	print(ans)



#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
if __name__ == "__main__":
	main()
