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

flag = True
ans_list = []
N = 1
while(flag == True):
	N = INT()
	if N == 0:
		flag = False
	else:
		A = LIST()
		A.sort()
		ans = abs(A[0] - A[1])
		for i in range(N - 1):
			ans = min(ans, abs(A[i] - A[i + 1]))
		ans_list.append(ans)

		# ans = abs(A[0] - A[1])
for ans in ans_list:
	print(ans)
	

