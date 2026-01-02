import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, log2
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

N, M = MAP()
LR = [LIST() for _ in range(M)]
lis = [0]*(N+1)

for L, R in LR:
	lis[L] += 1
	if R+1 <= N:
		lis[R+1] -= 1

tmp = 0
max_ = 0
range_ = 0
flag = False
for i in lis:
	tmp += i
	if tmp == M:
		flag = True
		range_ += 1
if flag == True:
	print(range_)
else:
	print(0)
