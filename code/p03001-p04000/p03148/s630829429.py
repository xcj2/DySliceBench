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
	N,K = inputMap()
	sushi_mii = []
	sushi_kii = []
	syu = [[] for i in range(N)]
	for i in range(N):
		t,d = inputMap()
		t -= 1
		syu[t].append(d)

	for i in syu:
		if len(i) > 0:
			i.sort()
			i = i[::-1]
			for j,val in enumerate(i):
				if j == 0:
					sushi_mii.append(val)
				else:
					sushi_kii.append(val)

	sushi_mii.sort()
	sushi_mii = sushi_mii[::-1]
	sushi_kii.sort()
	sushi_kii = sushi_kii[::-1]

	sushi_mi = []
	sushi_ki = []
	for i,val in enumerate(sushi_mii):
		if i == 0:
			sushi_mi.append(val)
		else:
			tmp = sushi_mi[i-1]
			sushi_mi.append(tmp + val)

	for i,val in enumerate(sushi_kii):
		if i == 0:
			sushi_ki.append(val)
		else:
			tmp = sushi_ki[i-1]
			sushi_ki.append(tmp + val)

	ans = 0
	for i in range(1, min(len(sushi_mi), K)+1):
		x = 0
		tmp = 0
		if K - i > len(sushi_ki):
			continue

		tmp += sushi_mi[i-1]
		x = i

		if K - i > 0:
			tmp += sushi_ki[K - i-1]

		oishi = tmp + x * x
		if ans < oishi:
			ans = oishi
	print(ans)

#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
if __name__ == "__main__":
	main()
