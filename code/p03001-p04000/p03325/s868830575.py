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

N = INT()
a = LIST()
count = 0
flag = 0
"""
while flag == 0:
	print(a)
	for i in range(N):
		if a[i] % 2 == 0:
			a[i] = int(a[i]/2)
			count += 1
			break
	else:
		flag = 1
"""
for i in a:
    while i % 2 == 0:
        count += 1
        i /= 2
print(count)