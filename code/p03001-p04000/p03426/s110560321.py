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

H, W, D = MAP()
A = [LIST() for _ in range(H)]

Q = INT()
LR = [LIST() for _ in range(Q)]

dic = [[] for _ in range(D)]

for i in range(H):
	for j in range(W):
		dic[A[i][j]%D].append([A[i][j], i, j])

for lis in dic:
	lis.sort(key=lambda x:x[0])

for lis in dic:
	lis[0][0] = 0
	for i in range(len(lis)):
		if i == len(lis)-1:
			break
		point = (lis[i][1], lis[i][2])
		dist_point = (lis[i+1][1], lis[i+1][2])
		lis[i+1][0] = lis[i][0] + abs(point[0]-dist_point[0]) + abs(point[1]-dist_point[1])

for L, R in LR:
	print(dic[R%D][ceil(R/D)-1][0]-dic[R%D][ceil(L/D)-1][0])
