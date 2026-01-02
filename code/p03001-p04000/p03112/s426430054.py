import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect_left

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

A, B, Q = MAP()
s = [-INF]+[INT() for _ in range(A)]+[INF]
t = [-INF]+[INT() for _ in range(B)]+[INF]
x = [INT() for _ in range(Q)]

for q in x:
	b, d = bisect_left(s, q), bisect_left(t, q)
	res = INF
	for S in [s[b-1], s[b]]:
		for T in [t[d-1], t[d]]:
			d1, d2 = abs(S-q) + abs(T-S), abs(T-q) + abs(S-T)
			res = min(res, d1, d2)
	print(res)
