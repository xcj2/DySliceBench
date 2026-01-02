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

N, Q = MAP()
S = input()
lr = [LIST() for _ in range(Q)]

accum = []
count = 0

for i in range(len(S)-1):
	accum.append(count)
	if S[i] == "A" and S[i+1] == "C":
		count += 1
accum.append(count)
# print(accum)
for l, r in lr:
	print(accum[r-1]-accum[l-1])
