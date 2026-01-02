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
h = LIST()
ans = 0
while sum(h) > 0:
	flag = False
	for i in range(N):
		if flag and h[i] == 0:
			flag = False
			ans += 1
		elif h[i] != 0:
			h[i] -= 1
			flag = True
	if flag:
		ans += 1
print(ans)
