import sys
import re
import queue
import collections
import math
from math import ceil, floor, sqrt, pi, factorial, gcd
from copy import deepcopy
from collections import Counter, deque
from heapq import heapify, heappop, heappush
from itertools import accumulate, product, combinations, combinations_with_replacement
from bisect import bisect, bisect_left, bisect_right
from functools import reduce
from decimal import Decimal, getcontext
# input = sys.stdin.readline
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7
num_list = []
str_list = []

def gcd_list(numbers):
    return reduce(gcd, numbers)

def main():
	N = i_input()
	A = i_list()

	d = dict()

	max_A = max(A)
	count_list = []

	MAXN = 10**6+10
	sieve = [i for i in range(MAXN+1)]
	p = 2
	while p*p <= MAXN:
		if sieve[p] == p:
			for q in range(2*p,MAXN+1,p):
				if sieve[q] == q:
					sieve[q] = p
		p += 1


	for i in range(0,max(A)):
		count_list.append(0)

	for a in A:
		tmp = set()
		while a > 1:
			tmp.add(sieve[a])
			a //= sieve[a]

		for p in tmp:
			count_list[p-1] += 1


	if (max(count_list)<=1):
		print("pairwise coprime")
	elif(gcd_list(A)==1):
		print("setwise coprime")
	else:
		print("not coprime")

	return

if __name__ == '__main__':
	main()