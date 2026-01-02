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
	A = inputList()

	ans = 0
	for i,val in enumerate(A):
		ii = i+1
		if ii % 2 == 1:
			if val % 2 == 1:
				ans += 1

	print(ans)

if __name__ == "__main__":
	main()
