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
mod = 10 ** 9 + 7

N = INT()
A = LIST()

dic = {}
def power(x, y):
   if y == 0:
       return 1
   elif y == 1:
       return x % mod
   elif y % 2 == 0:
       return power(x, y/2) ** 2 % mod
   else:
       return power(x, (y-1)/2) ** 2 * x % mod

for i in range(N):
	if not A[i] in dic:
		dic[A[i]] = 1
	else:
		dic[A[i]] += 1

if N%2 == 0: # 偶数の時
	for i in range(N//2):
		if N-1-2*i not in dic:
			print(0)
			break
		elif dic[N-1-2*i] != 2:
			print(0)
			break
		else:
			pass
	else:
		print(power(2,(N//2)))
else: # 奇数の時
	if A.count(0) != 1:
		print(0)
	else:
		for i in range(N//2-1):
			if N-1-2*i not in dic:
				print(0)
				break
			elif dic[N-1-2*i] != 2:
				print(0)
				break
			else:
				pass
		else:
			print(power(2,(N//2)))