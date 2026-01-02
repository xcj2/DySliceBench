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

def main():
	N = inputInt()

	ans = [0 for i in range(N)]
	for x in range(1,100+1):
		for y in range(1,100+1):
			for z in range(1,100+1):
				tmp = x**2 + y**2 + z**2 + x*y + y*z + z*x

				if tmp <= N:
					ans[tmp-1] += 1

	for i in ans:
		print(i)
		
if __name__ == "__main__":
	main()
