# -*- coding: utf-8 -*-
import sys
import math
from bisect import bisect_left
from bisect import bisect_right
import collections
import copy
import heapq
from collections import defaultdict
from heapq import heappop, heappush
import itertools
input = sys.stdin.readline
from collections import defaultdict
from heapq import heappop, heappush

def inputInt(): return int(input())
def inputMap(): return map(int, input().split())
def inputList(): return list(map(int, input().split()))
def inputStr(): return input()[:-1]

inf = float('inf')
mod = 1000000007

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

def main():
	N,K = inputMap()
	A = inputList()

	if N <= 2*K:
		T = [N for i in range(N)]
		print(*T)
		sys.exit()

	for j in range(K):
		T = [0 for i in range(N)]
		for i,val in enumerate(A):
			#print(T)
			tmp_min = max(0,i-val)
			T[tmp_min] += 1

			if i+val+1 > N-1:
				continue
			tmp_max = min(N-1,i+val+1)
			T[tmp_max] -= 1

		for i,val in enumerate(T):
			if i == 0:
				continue
			T[i] += T[i-1]
		A = T

	print(*A)

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
if __name__ == "__main__":
	main()
