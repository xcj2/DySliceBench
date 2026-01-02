# -*- coding: utf-8 -*-
import sys
import copy
import collections
from bisect import bisect_left
from bisect import bisect_right
from collections import defaultdict
from heapq import heappop, heappush
import numpy as np

def main():
	N = int(input())
	A = list(map(int, input().split(" ")))
	
	ans = A[0]
	for i, val in enumerate(A):
		if i == 0:
			continue
		ans = lcm(ans, val)
		
	ans -= 1
	tmp = 0
	for i, val in enumerate(A):
		tmp = tmp + (ans % val)
	
	print(tmp)
	
def gcd(a, b):
	if a > b:
		a, b = b, a
		
	while a > 0:
		a, b = b % a, a
	return b
	
def lcm(a, b):
	g = gcd(a, b)
	return a // g * b
	
if __name__ == "__main__":
	main()
