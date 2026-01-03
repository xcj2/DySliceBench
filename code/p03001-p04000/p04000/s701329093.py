import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

def sum_matrix(array):
	return sum([sum(x) for x in array])
count = {}
H, W, N = MAP()
ab = [LIST() for _ in range(N)]
for a, b in ab:				
	for i in range(a-3, a):
		for j in range(b-3, b):
			if i < 0 or j < 0:
				continue
			if i+2 >= H or j+2 >= W:
				continue
			else:
				if not str(i)+","+str(j) in count:
					count[str(i)+","+str(j)] = 1
				else:
					count[str(i)+","+str(j)] += 1
ans = [0] * 10
for key in count:
	ans[count[key]] += 1
ans[0] = (H-2)*(W-2)-sum(ans)
for i in ans:
	print(i)